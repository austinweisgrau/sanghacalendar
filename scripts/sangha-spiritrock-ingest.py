#!/usr/bin/env python3
"""
Sangha Calendar — Spirit Rock Meditation Center ingest.
Uses Spirit Rock's public Algolia API (found in page source) to pull drop-in events.
Runs alongside the iCal and Momence ingest scripts.

Usage:
  python3 sangha-spiritrock-ingest.py [--dry-run]
"""

import hashlib, json, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

TOKEN_PATH = "/workspace/group/memory/sangha-ingest-token.txt"
API_URL    = "https://sangha-calendar.fly.dev/api/admin/events"

# Algolia public search credentials (from Spirit Rock page source)
ALGOLIA_APP_ID  = "E6YG7CMGYO"
ALGOLIA_API_KEY = "04e497e32c17a3fc1bd4e4b8b2e45413"
ALGOLIA_INDEX   = "events"
ALGOLIA_URL     = f"https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{ALGOLIA_INDEX}/query"

CENTER = {
    "org_id":       "spirit_rock",
    "org_name":     "Spirit Rock Meditation Center",
    "address":      "5000 Sir Francis Drake Blvd",
    "city":         "Woodacre",
    "state":        "CA",
    "neighborhood": "West Marin",
    "lat":          38.0124,
    "lng":          -122.7215,
    "tradition":    "theravada",
    "source_url":   "https://www.spiritrock.org/calendar",
}

# Program types that are drop-in sits (Spirit Rock Algolia field)
DROP_IN_TYPES = {"dropIn", "drop-in", "drop_in"}

def fetch_drop_ins(days_ahead: int = 60) -> list:
    now_epoch   = int(datetime.now(timezone.utc).timestamp())
    cutoff_epoch = int((datetime.now(timezone.utc) + timedelta(days=days_ahead)).timestamp())

    payload = json.dumps({
        "filters": f"startDate > {now_epoch} AND startDate < {cutoff_epoch}",
        "attributesToRetrieve": ["title", "startDate", "endDate", "programType", "url", "description", "identityFocus"],
        "hitsPerPage": 200,
    }).encode()

    req = urllib.request.Request(ALGOLIA_URL, data=payload, method="POST", headers={
        "X-Algolia-Application-Id": ALGOLIA_APP_ID,
        "X-Algolia-API-Key": ALGOLIA_API_KEY,
        "Content-Type": "application/json",
    })

    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read())
    hits = data.get("hits", [])

    # Filter to drop-in types
    drop_ins = []
    for h in hits:
        pt = h.get("programType", [])
        if isinstance(pt, str):
            pt = [pt]
        if any(t in DROP_IN_TYPES for t in pt):
            drop_ins.append(h)

    return drop_ins

def epoch_to_local(epoch: int) -> str:
    # Spirit Rock's Algolia stores naive local PT times disguised as UTC epochs.
    # Treat as UTC directly (no offset conversion) to get correct local time.
    dt = datetime.utcfromtimestamp(epoch)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")

def event_id(org_id: str, title: str, start: str) -> str:
    key = f"{org_id}:{title}:{start}"
    return hashlib.sha256(key.encode()).hexdigest()[:16]

def main():
    dry_run = "--dry-run" in sys.argv
    today   = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    token   = open(TOKEN_PATH).read().strip()

    print("Fetching Spirit Rock drop-in events from Algolia...")
    try:
        hits = fetch_drop_ins()
    except Exception as e:
        print(f"✗ Algolia fetch failed: {e}")
        sys.exit(1)

    print(f"  → {len(hits)} drop-in events found")

    events = []
    for h in hits:
        title      = h.get("title", "").strip()
        start_ep   = h.get("startDate")
        end_ep     = h.get("endDate")
        url        = h.get("url", "")
        desc       = (h.get("description", "") or "").strip()[:300]
        id_focus   = h.get("identityFocus") or None

        if not title or not start_ep:
            continue

        start_local = epoch_to_local(int(start_ep))
        end_local   = epoch_to_local(int(end_ep)) if end_ep else None

        # Detect online events from title/desc
        loc_type = "online"
        if any(k in title.lower() or k in desc.lower() for k in ["in-person", "on land", "on-land", "woodacre"]):
            loc_type = "in-person"
        elif "zoom" in title.lower() or "zoom" in desc.lower():
            loc_type = "online"

        events.append({
            "id":                 event_id(CENTER["org_id"], title, start_local),
            "org_id":             CENTER["org_id"],
            "org_name":           CENTER["org_name"],
            "title":              title,
            "start_time":         start_local,
            "end_time":           end_local,
            "address":            CENTER["address"],
            "city":               CENTER["city"],
            "state":              CENTER["state"],
            "neighborhood":       CENTER["neighborhood"],
            "lat":                CENTER["lat"],
            "lng":                CENTER["lng"],
            "tradition":          CENTER["tradition"],
            "location_type":      loc_type,
            "is_sit":             True,
            "identity_focus":     id_focus,
            "accessibility_notes": None,
            "source":             "algolia",
            "source_url":         CENTER["source_url"],
            "event_url":          url or CENTER["source_url"],
            "last_verified":      today,
            "recurrence":         "weekly",
            "notes":              desc[:300] or None,
        })

    print(f"  → {len(events)} events formatted")

    if dry_run:
        for e in events:
            print(f"  {e['start_time']} | {e['title']} | {e['location_type']}")
        print("\n[dry-run] Not posting.")
        return

    if not events:
        print("Nothing to post.")
        return

    payload = json.dumps({"events": events}).encode()
    req = urllib.request.Request(API_URL, data=payload, method="POST", headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            print(f"✅ Upserted: {result['upserted']}")
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP {e.code}: {e.read().decode()}")
        sys.exit(1)

if __name__ == "__main__":
    main()
