#!/usr/bin/env python3
"""
Sangha Calendar — Momence platform ingest.
Fetches events from any Momence-based contemplative center, filters for sits,
and POSTs to the sangha calendar API.

Usage:
  python3 sangha-momence-ingest.py [--dry-run]
"""

import hashlib, json, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

TOKEN_PATH = "/workspace/group/memory/sangha-ingest-token.txt"
API_URL    = "https://sangha-calendar.fly.dev/api/admin/events"

# ── Momence centers ──────────────────────────────────────────────────────────
# To add a new center: find the host ID from their Momence booking URL.
# URL pattern: https://momence.com/host/{host_id}/...
# or inspect: https://readonly-api.momence.com/host-plugins/host/{host_id}/host-schedule/sessions

CENTERS = [
    {
        "org_id":       "berkeley_alembic",
        "org_name":     "Berkeley Alembic",
        "momence_host": 71603,
        "address":      "2820 7th St",
        "city":         "Berkeley",
        "state":        "CA",
        "neighborhood": "West Berkeley",
        "lat":          37.8614,
        "lng":          -122.2994,
        "tradition":    "nonsectarian",
        "source_url":   "https://www.berkeleyalembic.org/schedule",
    },
    # Future centers — add host IDs as discovered:
    # {
    #   "org_id":       "sf_dharmadhatu",
    #   "org_name":     "San Francisco Dharmadhatu",
    #   "momence_host": XXXXX,
    #   ...
    # },
]

# ── Keyword filters ──────────────────────────────────────────────────────────

SIT_KW = [
    "meditation", "sit", "sitting", "zazen", "vipassana", "mindfulness",
    "samadhi", "silent", "contemplative", "dhamma", "dharma sit",
    "half-day retreat", "retreat",  # Alembic BYOM half-day qualifies
    "deconstructing yourself",       # Taft's weekly guided meditation
    "kirtan",                        # devotional chanting (include)
    "non-dual", "nondual", "tantric meditation",
]

EXCL_KW = [
    "workshop", "training", "course", "class series", "lecture",
    "book club", "study group", "therapy", "psychotherapy",
    "dance", "qigong", "yoga", "movement", "somatic",
    "office hours", "co-working", "co working",
    "psychedelic integration", "psychedelic circle",
    "dating", "relationship", "men's group", "women's circle",
    "exhibition", "art show", "concert", "performance",
    "simulation hypothesis", "chalice",  # Alembic noise
]

# Names we explicitly want regardless of keyword matching
EXPLICIT_INCLUDE = [
    "deconstructing yourself",
    "weekly half-day retreat",
]

# ── Helpers ──────────────────────────────────────────────────────────────────

def is_sit(name: str, desc: str = "") -> bool:
    n = name.lower()
    d = desc.lower()
    if any(k in n for k in EXPLICIT_INCLUDE):
        return True
    full = n + " " + d
    if any(k in full for k in EXCL_KW):
        return False
    return any(k in full for k in SIT_KW)

def event_id(org_id: str, title: str, start: str) -> str:
    key = f"{org_id}:{title}:{start}"
    return hashlib.sha256(key.encode()).hexdigest()[:16]

def fetch_sessions(host_id: int, page_size: int = 100) -> list:
    url = f"https://readonly-api.momence.com/host-plugins/host/{host_id}/host-schedule/sessions?pageSize={page_size}&page=0"
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Origin": "https://www.berkeleyalembic.org",
        "Referer": "https://www.berkeleyalembic.org/",
    })
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read()).get("payload", [])

def to_local(utc_str: str, offset_hours: int = -7) -> str:
    """Convert UTC ISO string to local time string (no tz suffix)."""
    dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
    local = dt.astimezone(timezone(timedelta(hours=offset_hours)))
    return local.strftime("%Y-%m-%dT%H:%M:%S")

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv
    today   = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    now     = datetime.now(timezone.utc)
    cutoff  = now + timedelta(days=60)   # fetch 60 days out

    token = open(TOKEN_PATH).read().strip()
    all_events = []

    for center in CENTERS:
        org_id   = center["org_id"]
        org_name = center["org_name"]
        print(f"\n[{org_name}] Fetching from Momence host {center['momence_host']}...")

        try:
            sessions = fetch_sessions(center["momence_host"])
        except Exception as e:
            print(f"  ✗ Failed to fetch: {e}")
            continue

        count = 0
        for s in sessions:
            if s.get("isCancelled"):
                continue

            starts = s.get("startsAt", "")
            ends   = s.get("endsAt", "")
            try:
                dt_start = datetime.fromisoformat(starts.replace("Z", "+00:00"))
            except Exception:
                continue

            if dt_start < now or dt_start > cutoff:
                continue

            name = s.get("sessionName", "").strip()
            desc = (s.get("level", "") or "").strip()
            link = s.get("link", "")

            if not is_sit(name, desc):
                continue

            start_local = to_local(starts)
            end_local   = to_local(ends) if ends else None

            price     = s.get("price")
            price_min = s.get("dynamicTicketPriceMin")
            notes_str = f"${price}" if price else (f"${price_min}+" if price_min else "free/donation")
            if desc:
                notes_str += f" — {desc[:200]}"

            all_events.append({
                "id":                 event_id(org_id, name, start_local),
                "org_id":             org_id,
                "org_name":           org_name,
                "title":              name,
                "start_time":         start_local,
                "end_time":           end_local,
                "address":            center["address"],
                "city":               center["city"],
                "state":              center["state"],
                "neighborhood":       center.get("neighborhood"),
                "lat":                center["lat"],
                "lng":                center["lng"],
                "tradition":          center["tradition"],
                "location_type":      "in-person",
                "is_sit":             True,
                "identity_focus":     None,
                "accessibility_notes": None,
                "source":             "momence",
                "source_url":         center["source_url"],
                "event_url":          link or center["source_url"],
                "last_verified":      today,
                "recurrence":         "weekly",
                "notes":              notes_str[:400],
            })
            count += 1

        print(f"  → {count} sits found")

    print(f"\nTotal: {len(all_events)} events")

    if dry_run:
        for e in all_events:
            print(f"  {e['start_time']} | {e['title']} | {e['org_name']}")
        print("\n[dry-run] Not posting.")
        return

    if not all_events:
        print("Nothing to post.")
        return

    payload = json.dumps({"events": all_events}).encode()
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
