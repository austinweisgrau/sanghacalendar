"""
NYC meditation center sources — Phase 3a + 3b + 3c.
Defines all known NYC centers and their ingestion strategies.
"""

import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from typing import Optional

import httpx

from data.schemas.event import Center, Event, LocationType, SourceType, Tradition
from ingestion.feeds.ical_feed import fetch_feed
from ingestion.utils import detect_location_type, is_likely_sit

log = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# ---------------------------------------------------------------------------
# Phase 3a — Direct iCal subscribe (easy wins)
# ---------------------------------------------------------------------------

CENTERS = {
    "nyimc": Center(
        id="nyimc",
        name="New York Insight Meditation Center",
        url="https://www.nyimc.org",
        address="115 West 29th Street, 12th Floor",
        city="Manhattan",
        state="NY",
        zip_code="10001",
        lat=40.7473,
        lng=-73.9932,
        neighborhood="Midtown South",
        tradition=Tradition.THERAVADA,
        notes="Theravada / Secular Vipassana. Weekly Community Sit (Thursdays, co-presented with Tibet House US), Wednesday Community Meditation Gathering, monthly Sitting on Sunday. MBSR courses and retreats.",
    ),
    "brooklyn_zen_center": Center(
        id="brooklyn_zen_center",
        name="Brooklyn Zen Center",
        url="https://brooklynzen.org",
        address="326 Clinton St",
        city="Brooklyn",
        state="NY",
        zip_code="11231",
        lat=40.6820,
        lng=-73.9984,
        neighborhood="Carroll Gardens",
        tradition=Tradition.ZEN,
        notes="Soto Zen, socially-engaged and progressive. Daily online morning meditation Mon–Fri 7:30am ET; Wednesday Dharma Share 7pm (in-person); Saturday Morning Program 9am–12:40pm (most Saturdays, in-person). Monthly zazenkai one-day sits.",
    ),
    "kadampa_nyc": Center(
        id="kadampa_nyc",
        name="Kadampa Meditation Center New York",
        url="https://meditationinnewyork.org",
        address="127 W 24th St",
        city="Manhattan",
        state="NY",
        zip_code="10011",
        lat=40.7455,
        lng=-73.9960,
        neighborhood="Chelsea",
        tradition=Tradition.TIBETAN,
        notes="New Kadampa Tradition (NKT-IKBU) Tibetan Buddhist center. 30+ drop-in classes per week. Mon/Wed evenings 7pm; Tue lunchtime 11:15am; Tue/Fri evenings 5:30pm; Sun 11am.",
    ),
    # ---- Phase 3b ----
    "shambhala_nyc": Center(
        id="shambhala_nyc",
        name="Shambhala Meditation Center of New York",
        url="https://ny.shambhala.org",
        address="151 W 30th St, 3rd Floor",
        city="Manhattan",
        state="NY",
        zip_code="10001",
        lat=40.7476,
        lng=-73.9935,
        neighborhood="Midtown South",
        tradition=Tradition.TIBETAN,
        notes="Shambhala Buddhist center (Chögyam Trungpa lineage). Tuesday evening meditation 1st/3rd Tuesdays 7:15pm (in-person); Virtual Healing Circle monthly (last Sat 12:30pm); Sunday Dharma Gatherings 2nd Sunday monthly; Learn to Meditate online Tuesdays 6pm.",
    ),
    "nyzccc": Center(
        id="nyzccc",
        name="NY Zen Center for Contemplative Care",
        url="https://zencare.org",
        address="119 W 23rd St, 4th Floor",
        city="Manhattan",
        state="NY",
        zip_code="10011",
        lat=40.7435,
        lng=-73.9949,
        neighborhood="Chelsea",
        tradition=Tradition.ZEN,
        notes="Soto Zen center focused on contemplative care and healthcare-oriented Dharma. Mid-Day Zazen Mon–Sat 12:30pm (online/Zoom). Sunday: 10am zazen + 11:30am dharma talk (in-person + online). Monday + Wednesday evenings 6pm (hybrid).",
    ),
    "tibet_house_us": Center(
        id="tibet_house_us",
        name="Tibet House US",
        url="https://thus.org",
        address="22 W 15th St",
        city="Manhattan",
        state="NY",
        zip_code="10011",
        lat=40.7382,
        lng=-73.9972,
        neighborhood="Chelsea / Flatiron",
        tradition=Tradition.TIBETAN,
        notes="Cultural center of HH the Dalai Lama in America. Lunchtime Meditation Mon–Fri 1:00–1:45pm ET (online, various teachers). Occasional in-person lectures, exhibitions, and special programs.",
    ),
    # ---- NYC Phase 3c ----
    "zenstudies_nyc": Center(
        id="zenstudies_nyc",
        name="New York Zendo Shobo-Ji",
        url="https://zenstudies.org/new-york-zendo/",
        address="223 E 67th St",
        city="Manhattan",
        state="NY",
        zip_code="10065",
        lat=40.7657,
        lng=-73.9600,
        neighborhood="Upper East Side",
        tradition=Tradition.ZEN,
        notes="Rinzai Zen zendo. Daily Morning Zazen Mon–Thu 6:45am; Evening Zazen Mon/Tue/Wed 7pm; Sunday Morning Service 10am. Monthly sesshins and intro meditation classes. Part of the Zen Studies Society (also operates Dai Bosatsu Zendo in the Catskills).",
    ),
    "zcnyc": Center(
        id="zcnyc",
        name="Zen Center of New York City (Fire Lotus Temple)",
        url="https://zcnyc.org",
        address="500 State St",
        city="Brooklyn",
        state="NY",
        zip_code="11217",
        lat=40.6824,
        lng=-73.9887,
        neighborhood="Boerum Hill",
        tradition=Tradition.ZEN,
        notes="Soto Zen center in the Mountains and Rivers Order (Zen Mountain Monastery). Sunday Morning Program 9:30am–12:30pm; daily zazen; LGBTQIA+ Sitting Group 1st/3rd Tuesdays 6pm (Zoom); TGNC Practice Night 2nd Thursdays 6:30pm (in-person); monthly half-day sits.",
    ),
    # ---- Brooklyn Phase 3d ----
    "kadampa_brooklyn": Center(
        id="kadampa_brooklyn",
        name="Kadampa Meditation Center Brooklyn",
        url="https://www.brooklynmeditation.org",
        address="444 Atlantic Ave",
        city="Brooklyn",
        state="NY",
        zip_code="11217",
        lat=40.6847,
        lng=-73.9892,
        neighborhood="Boerum Hill",
        tradition=Tradition.TIBETAN,
        notes="New Kadampa Tradition (NKT-IKBU) Tibetan Buddhist center, est. 2005. Main Brooklyn location plus Williamsburg, Bay Ridge, and Bed-Stuy branches. Drop-in classes Mon–Sun. Monday 7pm, Wednesday 7pm, Thursday 12:15pm lunchtime, Sunday 11:30am General Program. Summer outdoor meditation in Prospect Park.",
    ),
    "shantideva_brooklyn": Center(
        id="shantideva_brooklyn",
        name="Shantideva Center",
        url="https://shantidevanyc.org",
        address="432 6th Ave",
        city="Brooklyn",
        state="NY",
        zip_code="11215",
        lat=40.6742,
        lng=-73.9780,
        neighborhood="Park Slope",
        tradition=Tradition.TIBETAN,
        notes="FPMT (Foundation for the Preservation of the Mahayana Tradition) center in Park Slope. Gelug Tibetan lineage of Lama Yeshe and Lama Zopa Rinpoche. Very active programming: Monday 7:30pm Meditation 101, Thursday 1pm lunchtime meditation, Saturday 9:30am in-depth training. Both in-person and online offerings.",
    ),
    "rock_blossom_sangha": Center(
        id="rock_blossom_sangha",
        name="Rock Blossom Sangha",
        url="https://rockblossom.org",
        address="1012 8th Ave",
        city="Brooklyn",
        state="NY",
        zip_code="11215",
        lat=40.6665,
        lng=-73.9803,
        neighborhood="Park Slope",
        tradition=Tradition.ZEN,
        notes="Plum Village tradition (Thich Nhat Hanh / Order of Interbeing) sangha in Park Slope. Meets Sundays 6pm in-person at Church of Gethsemane (hybrid) and Thursdays 6:30pm online via Zoom. Part of Community of Mindfulness NY Metro.",
    ),
    "dharma_punx_nyc": Center(
        id="dharma_punx_nyc",
        name="Dharma Punx NYC",
        url="https://www.dharmapunxnyc.com",
        address="105 Grand St",
        city="Brooklyn",
        state="NY",
        zip_code="11249",
        lat=40.7145,
        lng=-73.9650,
        neighborhood="Williamsburg",
        tradition=Tradition.THERAVADA,
        notes="Secular/Theravada meditation community led by Josh Korda and Kathy Cherry. Monthly in-person sits on 1st Tuesdays 7pm at 105 Grand St, Williamsburg (Grand Street Healing Project). Weekly Zoom sits Tuesdays 7pm. All by donation. Hosts retreats at Garrison Institute and Omega.",
    ),
}


# Feed configurations for Phase 3a direct-subscribe centers
ICAL_FEEDS = {
    "nyimc": {
        # WordPress + The Events Calendar Pro
        # Returns 403 without browser User-Agent — ical_feed.py already sets headers
        "url": "https://www.nyimc.org/events/?ical=1",
        "filter_to_sits": True,
    },
    "brooklyn_zen_center": {
        # WordPress + Event Organiser plugin
        # PRODID:-//Brooklyn Zen Center//NONSGML Events//EN
        "url": "https://brooklynzen.org/?ical=1",
        "filter_to_sits": True,
    },
    "kadampa_nyc": {
        # WordPress + The Events Calendar (meditationinnewyork.org — NYC branch site)
        # filter_to_sits=False to include classes and programs (not just sits)
        "url": "https://meditationinnewyork.org/events/?ical=1",
        "filter_to_sits": False,
    },
}

# Phase 3b — Eventbrite feeds
EVENTBRITE_FEEDS = {
    "tibet_house_us": {
        # organizer_id from thus.org Eventbrite page
        "organizer_id": "3903735193",
        "filter_to_sits": False,  # include lectures, exhibitions, special programs
    },
    # Phase 3d — Brooklyn
    "kadampa_brooklyn": {
        # Kadampa Meditation Center Brooklyn (also covers Williamsburg branch)
        # organizer_id: "Kadampa Meditation Center Brooklyn / Vajradhara"
        "organizer_id": "341863409",
        "filter_to_sits": False,  # include all classes and programs
    },
}

# Phase 3c — Static HTML feeds (LLM-assisted)
STATIC_HTML_FEEDS = {
    "zcnyc": {
        # Zen Center of NYC — WordPress Simple Calendar backed by private Google Calendar.
        # Events are server-side rendered in the HTML. Scrape monthly calendar view.
        "url": "https://zcnyc.org/calendar/",
        "filter_to_sits": True,
    },
    # Phase 3d — Brooklyn
    "shantideva_brooklyn": {
        # Shantideva Center (FPMT Park Slope) — website calendar.
        "url": "https://shantidevanyc.org/calendar/",
        "filter_to_sits": False,  # include classes, guided meditation, workshops
    },
}


# ---------------------------------------------------------------------------
# Phase 3c — Zen Studies Society / New York Zendo Shobo-Ji iCal with prefix handling
# ---------------------------------------------------------------------------

def fetch_zenstudies_nyc() -> list[Event]:
    """
    Fetch the NY Zendo Shobo-Ji iCal feed and strip location prefixes from titles.

    The Zen Studies Society iCal feed prefixes every event title with a location code:
      "NYZ: Morning Zazen"  → in-person at 223 E 67th St, Manhattan
      "Online: ..."         → online-only event
      "DBZ: ..."            → Dai Bosatsu Zendo (Catskills retreat center, not NYC)

    We strip the "NYZ: " and "Online: " prefixes for clean display, and skip
    all "DBZ:" events since they're not in NYC.
    """
    center = CENTERS["zenstudies_nyc"]
    url = "https://zenstudies.org/events/new-york-zendo-calendar/?ical=1"
    log.info(f"Fetching Zen Studies Society / NY Zendo iCal feed")

    try:
        raw_events = fetch_feed(
            url=url,
            org_id="zenstudies_nyc",
            org_name=center.name,
            tradition=center.tradition,
            filter_to_sits=True,
            address=center.address,
            city=center.city,
            state=center.state,
            neighborhood=center.neighborhood,
            lat=center.lat,
            lng=center.lng,
        )
    except Exception as e:
        log.error(f"Failed to fetch Zen Studies NYC iCal: {e}")
        return []

    # Post-process: strip location prefixes, skip Catskills (DBZ) events
    nyc_events = []
    for event in raw_events:
        title = event.title
        if title.startswith("DBZ:"):
            # Dai Bosatsu Zendo — Catskills retreat center, not NYC
            continue
        elif title.startswith("NYZ: "):
            event.title = title[5:]
        elif title.startswith("Online: "):
            event.title = title[8:]
            # Ensure location_type is set correctly for online events
            if event.location_type == LocationType.IN_PERSON:
                event.location_type = LocationType.ONLINE
        nyc_events.append(event)

    log.info(f"  → {len(nyc_events)} NY Zendo events (filtered from {len(raw_events)} raw)")
    return nyc_events


# ---------------------------------------------------------------------------
# Phase 3b — Shambhala NYC scraper
# ---------------------------------------------------------------------------

def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def fetch_shambhala_nyc() -> list[Event]:
    """
    Scrape events from Shambhala NYC calendar page.

    The page embeds `const eventsDatas = {"items": [...]}` in a script tag.
    Each item has:
      title, _EventStartDate, _EventEndDate, _EventTimezone (America/New_York),
      _EventURL / guid, intro_text, tribe_events_cat, event_types, center_name
    """
    center = CENTERS["shambhala_nyc"]
    url = "https://ny.shambhala.org/calendar/"
    log.info(f"Fetching Shambhala NYC calendar: {url}")

    try:
        resp = httpx.get(url, headers=HEADERS, follow_redirects=True, timeout=20)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        log.error(f"Failed to fetch Shambhala NYC calendar: {e}")
        return []

    html = resp.text

    # Extract the eventsDatas JSON blob
    match = re.search(
        r'const\s+eventsDatas\s*=\s*(\{.*?\})\s*;',
        html,
        re.DOTALL,
    )
    if not match:
        log.warning("Shambhala NYC: no eventsDatas found in page HTML")
        return []

    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        log.error(f"Shambhala NYC: failed to parse eventsDatas JSON: {e}")
        return []

    items = data.get("items", [])
    log.info(f"  Found {len(items)} raw events in eventsDatas")

    now = datetime.now()
    events = []
    for item in items:
        if not isinstance(item, dict):
            continue
        title = str(item.get("title", "")).strip()
        if not title:
            continue

        start_str_raw = item.get("_EventStartDate", "")
        end_str_raw = item.get("_EventEndDate", "")

        # Format: "2026-05-06 19:15:00" — treat as America/New_York local time
        try:
            start_dt = datetime.strptime(start_str_raw, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            log.warning(f"  Skipping event with bad start date: {title!r} → {start_str_raw!r}")
            continue

        # Skip past events
        if start_dt < now:
            continue

        start_str = start_dt.strftime("%Y-%m-%dT%H:%M:%S")

        end_str: Optional[str] = None
        if end_str_raw:
            try:
                end_dt = datetime.strptime(end_str_raw, "%Y-%m-%d %H:%M:%S")
                end_str = end_dt.strftime("%Y-%m-%dT%H:%M:%S")
            except (ValueError, TypeError):
                pass

        event_url = item.get("_EventURL") or item.get("guid")
        description = str(item.get("intro_text", "")).strip()

        sit_result, _ = is_likely_sit(title, description)
        loc_type, _ = detect_location_type(title, description, center.address or "", event_url or "")

        events.append(Event(
            id=_event_id("shambhala_nyc", title, start_str),
            org_id="shambhala_nyc",
            org_name=center.name,
            title=title,
            start_time=start_str,
            end_time=end_str,
            address=center.address,
            city=center.city,
            state=center.state,
            neighborhood=center.neighborhood,
            lat=center.lat,
            lng=center.lng,
            tradition=center.tradition,
            location_type=loc_type,
            is_sit=sit_result,
            source=SourceType.WORDPRESS,
            source_url=url,
            event_url=event_url,
            last_verified=datetime.now(timezone.utc).date().isoformat(),
            notes=description[:300] if description else None,
        ))

    log.info(f"  → {len(events)} upcoming events for Shambhala NYC")
    return events
