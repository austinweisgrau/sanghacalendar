"""
NYC meditation center sources — Phase 3a + 3b.
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
}


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
