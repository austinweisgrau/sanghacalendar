#!/usr/bin/env python3
"""
Sangha Calendar — Shambhala Network iCal ingest.
Fetches iCal feeds from shambhala-koeln.de for all US/CA centers,
filters for sits, and POSTs to the sangha calendar API.

NOTE: The shambhala-koeln.de server has been intermittently down.
This script is ready to run when the server comes back up.
Test with: python3 sangha-shambhala-ingest.py --dry-run --test-first

Usage:
  python3 sangha-shambhala-ingest.py [--dry-run] [--test-first]
"""

import hashlib, json, re, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

TOKEN_PATH = "/workspace/group/memory/sangha-ingest-token.txt"
API_URL    = "https://sangha-calendar.fly.dev/api/admin/events"
ICAL_BASE  = "http://shambhala-koeln.de/ical.php?center="

# ── US Shambhala centers (IDs confirmed from each center's website) ───────────
# Format: (center_id, org_id, org_name, address, city, state, neighborhood, lat, lng)

CENTERS = [
    # California
    (178, "shambhala_berkeley",    "Berkeley Shambhala Center",      "2288 Fulton St",            "Berkeley",      "CA", "South Campus Berkeley", 37.8696, -122.2677),
    (177, "shambhala_sf",          "San Francisco Shambhala Center", "1630 Taraval St",            "San Francisco", "CA", "West Portal",           37.7432, -122.4768),
    (183, "shambhala_tamalpais",   "Tamalpais Shambhala",            "Marin County",               "Marin",         "CA", "Marin County",          37.9735, -122.5260),
    (180, "shambhala_sonoma",      "Sonoma Shambhala",               "Sonoma County",              "Sonoma",        "CA", "Sonoma County",         38.2919, -122.4580),
    (179, "shambhala_davis",       "Davis Shambhala",                "Davis",                      "Davis",         "CA", "Davis",                 38.5449, -121.7405),
    (208, "shambhala_la",          "Los Angeles Shambhala Center",   "2340 Erie St",               "Los Angeles",   "CA", "Los Angeles",           34.0195, -118.2912),
    (254, "shambhala_san_diego",   "San Diego Shambhala Center",     "San Diego",                  "San Diego",     "CA", "San Diego",             32.7157, -117.1611),

    # Colorado
    (191, "shambhala_boulder",     "Boulder Shambhala Center",       "1345 Spruce St",             "Boulder",       "CO", "Boulder",               40.0150, -105.2705),
    (218, "shambhala_denver",      "Denver Shambhala Center",        "1007 Marion St",             "Denver",        "CO", "Capitol Hill",          39.7318, -104.9698),
    (188, "shambhala_fort_collins","Fort Collins Shambhala",         "Fort Collins",               "Fort Collins",  "CO", "Fort Collins",          40.5853, -105.0844),

    # New York
    (202, "shambhala_nyc",         "New York Shambhala Center",      "118 W 22nd St",              "New York",      "NY", "Chelsea",               40.7431, -73.9945),
    (209, "shambhala_albany",      "Albany Shambhala Center",        "Albany",                     "Albany",        "NY", "Albany",                42.6526, -73.7562),
    (227, "shambhala_new_haven",   "New Haven Shambhala",            "New Haven",                  "New Haven",     "CT", "New Haven",             41.3083, -72.9279),

    # Massachusetts
    (204, "shambhala_boston",      "Boston Shambhala Center",        "646 Beacon St",              "Boston",        "MA", "Kenmore",               42.3484, -71.0997),
    (213, "shambhala_pioneer_valley","Pioneer Valley Shambhala",     "Northampton",                "Northampton",   "MA", "Pioneer Valley",        42.3251, -72.6412),

    # Washington
    (211, "shambhala_seattle",     "Seattle Shambhala Center",       "2216 2nd Ave",               "Seattle",       "WA", "Belltown",              47.6117, -122.3449),
    (242, "shambhala_bellingham",  "Bellingham Shambhala",           "Bellingham",                 "Bellingham",    "WA", "Bellingham",            48.7519, -122.4787),

    # Oregon
    (214, "shambhala_portland",    "Portland Shambhala Center",      "2320 SE Belmont St",         "Portland",      "OR", "Southeast Portland",    45.5122, -122.6587),

    # Illinois
    (170, "shambhala_chicago",     "Chicago Shambhala Center",       "1231 W Belmont Ave",         "Chicago",       "IL", "Lakeview",              41.9395, -87.6588),

    # Texas
    (212, "shambhala_austin",      "Austin Shambhala Center",        "Austin",                     "Austin",        "TX", "Austin",                30.2672, -97.7431),
    (217, "shambhala_dallas",      "Dallas Shambhala Center",        "Dallas",                     "Dallas",        "TX", "Dallas",                32.7767, -96.7970),
    (223, "shambhala_houston",     "Houston Shambhala Center",       "Houston",                    "Houston",       "TX", "Houston",               29.7604, -95.3698),

    # DC / Mid-Atlantic
    (205, "shambhala_dc",          "Washington DC Shambhala Center", "1130 19th St NW",            "Washington",    "DC", "Dupont Circle",         38.9076, -77.0418),
    (201, "shambhala_baltimore",   "Baltimore Shambhala Center",     "Baltimore",                  "Baltimore",     "MD", "Baltimore",             39.2904, -76.6122),
    (284, "shambhala_annapolis",   "Annapolis Shambhala",            "Annapolis",                  "Annapolis",     "MD", "Annapolis",             38.9784, -76.4922),
    (210, "shambhala_philly",      "Philadelphia Shambhala Center",  "Philadelphia",               "Philadelphia",  "PA", "Philadelphia",          39.9526, -75.1652),

    # Southeast
    (196, "shambhala_atlanta",     "Atlanta Shambhala Center",       "Atlanta",                    "Atlanta",       "GA", "Atlanta",               33.7490, -84.3880),
    (220, "shambhala_durham",      "Durham Shambhala Center",        "Durham",                     "Durham",        "NC", "Durham",                35.9940, -78.8986),
    (175, "shambhala_birmingham",  "Birmingham Shambhala Center",    "Birmingham",                 "Birmingham",    "AL", "Birmingham",            33.5186, -86.8104),
    (256, "shambhala_st_pete",     "St. Petersburg Shambhala",       "St. Petersburg",             "St. Petersburg","FL", "St. Petersburg",        27.7676, -82.6403),
    (264, "shambhala_palm_beach",  "Palm Beach Shambhala",           "Palm Beach",                 "Palm Beach",    "FL", "Palm Beach",            26.7056, -80.0364),

    # Midwest / Other
    (195, "shambhala_minneapolis", "Minneapolis Shambhala Center",   "Minneapolis",                "Minneapolis",   "MN", "Minneapolis",           44.9778, -93.2650),
    (226, "shambhala_madison",     "Madison Shambhala Center",       "Madison",                    "Madison",       "WI", "Madison",               43.0731, -89.4012),
    (207, "shambhala_milwaukee",   "Milwaukee Shambhala Center",     "Milwaukee",                  "Milwaukee",     "WI", "Milwaukee",             43.0389, -87.9065),
    (240, "shambhala_cleveland",   "Cleveland Shambhala Center",     "Cleveland",                  "Cleveland",     "OH", "Cleveland",             41.4993, -81.6944),
    (241, "shambhala_columbus",    "Columbus Shambhala Center",      "Columbus",                   "Columbus",      "OH", "Columbus",              39.9612, -82.9988),
    (193, "shambhala_lexington",   "Lexington Shambhala Center",     "Lexington",                  "Lexington",     "KY", "Lexington",             38.0406, -84.5037),
    (79,  "shambhala_tulsa",       "Tulsa Shambhala",                "Tulsa",                      "Tulsa",         "OK", "Tulsa",                 36.1540, -95.9928),
    (107, "shambhala_huntsville",  "Huntsville Shambhala",           "Huntsville",                 "Huntsville",    "AL", "Huntsville",            34.7304, -86.5861),
    (60,  "shambhala_indiana",     "Hoosier Heartland Shambhala",    "Indiana",                    "Indianapolis",  "IN", "Indiana",               39.7684, -86.1581),

    # Southwest
    (267, "shambhala_phoenix",     "Phoenix Shambhala Center",       "Phoenix",                    "Phoenix",       "AZ", "Phoenix",               33.4484, -112.0740),
    (268, "shambhala_albuquerque", "Albuquerque Shambhala Center",   "Albuquerque",                "Albuquerque",   "NM", "Albuquerque",           35.0844, -106.6504),

    # Vermont / New England
    (215, "shambhala_burlington",  "Burlington Shambhala Center",    "Burlington",                 "Burlington",    "VT", "Burlington",            44.4759, -73.2121),
]

# ── Keyword filters ──────────────────────────────────────────────────────────

SIT_KW   = ["sit","sitting","zazen","meditation","practice","samadhi","open house meditation","drop-in"]
EXCL_KW  = ["retreat","workshop","seminar","lecture","course","class","training","dinner","social","fundraiser","study group","book"]

def is_sit(title: str, desc: str = "") -> bool:
    t = (title + " " + desc).lower()
    if any(k in t for k in EXCL_KW):
        return False
    return any(k in t for k in SIT_KW)

def event_id(org_id: str, title: str, start: str) -> str:
    return hashlib.sha256(f"{org_id}:{title}:{start}".encode()).hexdigest()[:16]

# ── iCal parsing (minimal, no external deps) ─────────────────────────────────

def parse_ical_simple(text: str) -> list:
    """Minimal iCal parser — extracts VEVENT blocks without external libs."""
    events = []
    blocks = re.split(r'BEGIN:VEVENT', text)[1:]  # skip first (before any VEVENT)
    for block in blocks:
        end = block.find('END:VEVENT')
        block = block[:end] if end != -1 else block

        def get(key):
            # Handle folded lines (lines starting with space/tab are continuations)
            unfolded = re.sub(r'\r?\n[ \t]', '', block)
            m = re.search(rf'^{key}[^:]*:(.+)$', unfolded, re.MULTILINE)
            return m.group(1).strip() if m else ""

        def parse_dt(val):
            val = re.sub(r'Z$', '', val)
            val = re.sub(r'T', 'T', val)
            for fmt in ('%Y%m%dT%H%M%S', '%Y%m%d'):
                try:
                    return datetime.strptime(val, fmt)
                except ValueError:
                    pass
            return None

        summary  = get('SUMMARY')
        desc     = get('DESCRIPTION')
        dtstart  = parse_dt(get('DTSTART'))
        dtend    = parse_dt(get('DTEND'))
        url      = get('URL')

        if summary and dtstart:
            events.append({'summary': summary, 'description': desc,
                           'dtstart': dtstart, 'dtend': dtend, 'url': url})
    return events

# ── Main ─────────────────────────────────────────────────────────────────────

def fetch_ical(center_id: int, timeout: int = 10) -> str | None:
    url = f"{ICAL_BASE}{center_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception as e:
        return None

def main():
    dry_run    = "--dry-run" in sys.argv
    test_first = "--test-first" in sys.argv
    today      = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    now        = datetime.now()
    cutoff     = now + timedelta(days=60)

    token = open(TOKEN_PATH).read().strip()

    # Quick server liveness check
    if test_first:
        print("Testing shambhala-koeln.de server...")
        result = fetch_ical(178, timeout=5)
        if not result or 'VCALENDAR' not in result:
            print("✗ Server is DOWN or not returning iCal data. Aborting.")
            print("  Re-run without --test-first to force attempt anyway.")
            sys.exit(1)
        print("✓ Server is responding. Proceeding with full ingest.")

    all_events = []
    failed     = []
    empty      = []

    for (center_id, org_id, org_name, address, city, state, neighborhood, lat, lng) in CENTERS:
        text = fetch_ical(center_id)
        if not text or 'VCALENDAR' not in text:
            failed.append(f"{org_name} (center={center_id})")
            continue

        raw_events = parse_ical_simple(text)
        count = 0
        for e in raw_events:
            if e['dtstart'] < now or e['dtstart'] > cutoff:
                continue
            if not is_sit(e['summary'], e['description']):
                continue

            start_str = e['dtstart'].strftime('%Y-%m-%dT%H:%M:%S')
            end_str   = e['dtend'].strftime('%Y-%m-%dT%H:%M:%S') if e['dtend'] else None

            t = (e['summary'] + ' ' + e['description']).lower()
            if any(k in t for k in ['hybrid', 'in-person and online']):
                loc_type = 'hybrid'
            elif any(k in t for k in ['online', 'virtual', 'zoom']):
                loc_type = 'online'
            else:
                loc_type = 'in-person'

            all_events.append({
                "id":                 event_id(org_id, e['summary'], start_str),
                "org_id":             org_id,
                "org_name":           org_name,
                "title":              e['summary'],
                "start_time":         start_str,
                "end_time":           end_str,
                "address":            address,
                "city":               city,
                "state":              state,
                "neighborhood":       neighborhood,
                "lat":                lat,
                "lng":                lng,
                "tradition":          "tibetan",
                "location_type":      loc_type,
                "is_sit":             True,
                "identity_focus":     None,
                "accessibility_notes": None,
                "source":             "ical_feed",
                "source_url":         f"{ICAL_BASE}{center_id}",
                "event_url":          e['url'] or f"https://{org_id.replace('shambhala_', '').replace('_', '')}.shambhala.org",
                "last_verified":      today,
                "recurrence":         "weekly",
                "notes":              e['description'][:300] if e['description'] else None,
            })
            count += 1

        if count == 0:
            empty.append(org_name)

    print(f"\nTotal: {len(all_events)} events from {len(CENTERS) - len(failed) - len(empty)} centers")
    if failed:
        print(f"Failed ({len(failed)}): {', '.join(failed[:5])}{'...' if len(failed) > 5 else ''}")
    if empty:
        print(f"No sits ({len(empty)}): {', '.join(empty[:5])}{'...' if len(empty) > 5 else ''}")

    if dry_run:
        cities = sorted(set(e['city'] for e in all_events))
        print(f"\nCities covered: {', '.join(cities)}")
        for e in all_events[:20]:
            print(f"  {e['start_time']} | {e['city']:20} | {e['title']}")
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
