"""
Los Angeles meditation center sources — Phase 3 LA expansion.
Defines known LA centers and their ingestion strategies.
"""

import hashlib
import html as html_module
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
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "insightla": Center(
        id="insightla",
        name="InsightLA",
        url="https://insightla.org",
        address="1430 Olympic Blvd",
        city="Santa Monica",
        state="CA",
        zip_code="90404",
        lat=34.0230,
        lng=-118.4807,
        neighborhood="Mid-City Santa Monica",
        tradition=Tradition.THERAVADA,
        notes=(
            "InsightLA — Insight/Vipassana meditation center. Founded by Trudy Goodman. "
            "Affiliated with IMS/Spirit Rock lineage (Jack Kornfield). Offers weekly community "
            "sits, dharma nights, MBSR, and retreats at the Santa Monica center and Big Bear "
            "Retreat House. Strong emphasis on accessibility and social engagement."
        ),
    ),
    "zcla": Center(
        id="zcla",
        name="Zen Center of Los Angeles",
        url="https://zcla.org",
        address="923 S. Mariposa Ave",
        city="Los Angeles",
        state="CA",
        zip_code="90006",
        lat=34.0546,
        lng=-118.3012,
        neighborhood="Koreatown",
        tradition=Tradition.ZEN,
        notes=(
            "ZCLA — Soto/Rinzai Zen, Taizan Maezumi Roshi lineage (White Plum Asanga). "
            "One of the oldest Zen centers in the US. Daily zazen, sesshins, study groups. "
            "Intro to Zen classes, Half-Day Zazen, Sunday services."
        ),
    ),
    "dharma_vijaya": Center(
        id="dharma_vijaya",
        name="Dharma Vijaya Buddhist Vihara",
        url="https://dharmavijaya.org",
        address="1847 Crenshaw Blvd",
        city="Los Angeles",
        state="CA",
        zip_code="90019",
        lat=34.0330,
        lng=-118.3375,
        neighborhood="Crenshaw / Mid-City",
        tradition=Tradition.THERAVADA,
        notes=(
            "Dharma Vijaya Buddhist Vihara is a Sri Lankan Theravada temple "
            "in the Crenshaw neighborhood of Los Angeles. Founded in 1980, it "
            "is one of the oldest Theravada Buddhist temples in Southern California. "
            "Regular public meditation: Tuesday and Friday 7–8pm (guided meditation "
            "and Dhamma talk, all levels welcome). First Sunday of each month: "
            "one-day meditation retreat, 7am–5pm. Monks hold a daily morning "
            "puja, sutta recitation, and loving-kindness meditation at 6am. "
            "1847 Crenshaw Blvd, Los Angeles CA 90019. dharmavijaya.org."
        ),
    ),
    "shambhala_la": Center(
        id="shambhala_la",
        name="Shambhala Meditation Center of Los Angeles",
        url="https://la.shambhala.org",
        address="3580 W 1st St",
        city="Los Angeles",
        state="CA",
        zip_code="90004",
        lat=34.0693,
        lng=-118.2979,
        neighborhood="Koreatown / Westlake",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Buddhist tradition (Chögyam Trungpa lineage). "
            "Weekly sitting meditation, Shambhala Training weekends, dharma talks. "
            "Open to all — no experience required. Events via Shambhala central iCal server."
        ),
    ),
}

# Phase 3 LA — iCal feeds
ICAL_FEEDS = {
    "shambhala_la": {
        # Shambhala central iCal server — center=208 (LA). 388 events as of 2026-05-08.
        "url": "https://shambhala-koeln.de/ical.php?center=208",
        "filter_to_sits": False,
    },
}

# Phase 3 LA — Static HTML scraper (LLM-assisted) targets
STATIC_HTML_FEEDS = {
    "zcla": {
        # Custom PHP calendar at zcla.org/calendars/ — server-side rendered HTML
        # Events listed as text with overlib.js popups
        "url": "https://zcla.org/calendars/",
        "filter_to_sits": True,
    },
}


# ---------------------------------------------------------------------------
# InsightLA — schema.org Event HTML parser
# ---------------------------------------------------------------------------

def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


_ATTENDANCE_MAP = {
    "OnlineEventAttendanceMode": LocationType.ONLINE,
    "OfflineEventAttendanceMode": LocationType.IN_PERSON,
    "MixedEventAttendanceMode": LocationType.HYBRID,
}


def _parse_insightla_events(html: str, center: Center) -> list[Event]:
    """Parse schema.org Event markup from InsightLA HTML page."""
    # Split on event block boundaries
    raw_blocks = re.split(r'<div class="event" itemscope', html)
    if len(raw_blocks) < 2:
        log.warning("InsightLA: no event blocks found in HTML")
        return []

    now = datetime.now()
    events = []

    for block in raw_blocks[1:]:  # skip content before first event
        # Event name — inside h2.event-title as a meta tag
        name_match = re.search(r'class="event-title".*?itemprop="name"\s+content="([^"]+)"', block, re.DOTALL)
        if not name_match:
            # Fallback: anchor text inside event-title
            name_match = re.search(r'class="event-title"[^>]*>.*?<a[^>]*>([^<]+)</a>', block, re.DOTALL)
        if not name_match:
            continue
        title = html_module.unescape(name_match.group(1).strip())

        # Start date
        start_match = re.search(r'itemprop="startDate"\s+content="([^"]+)"', block)
        if not start_match:
            continue
        start_str = start_match.group(1).strip()

        # Parse and skip past events
        try:
            start_dt = datetime.fromisoformat(start_str)
        except ValueError:
            log.warning(f"InsightLA: bad startDate format: {start_str!r}")
            continue
        if start_dt < now:
            continue

        # End date
        end_str: Optional[str] = None
        end_match = re.search(r'itemprop="endDate"\s+content="([^"]+)"', block)
        if end_match:
            end_str = end_match.group(1).strip()

        # Attendance mode → location type
        attendance_match = re.search(r'itemprop="eventAttendanceMode"\s+content="[^"]+/([^"]+)"', block)
        if attendance_match:
            loc_type = _ATTENDANCE_MAP.get(attendance_match.group(1), LocationType.IN_PERSON)
        else:
            loc_type = LocationType.IN_PERSON

        # Event URL
        event_url: Optional[str] = None
        url_match = re.search(r'class="event-title"[^>]*>.*?<a href="(https://insightla\.org/event/[^"]+)"', block, re.DOTALL)
        if url_match:
            event_url = url_match.group(1)

        # Description
        desc: Optional[str] = None
        desc_match = re.search(r'itemprop="description"\s+content="([^"]+)"', block)
        if desc_match:
            desc = desc_match.group(1).strip()[:400]

        # is_sit filter
        sit_result, _ = is_likely_sit(title, desc or "")

        events.append(Event(
            id=_event_id("insightla", title, start_str),
            org_id="insightla",
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
            source=SourceType.STATIC_HTML,
            source_url="https://insightla.org/fullcalendar/",
            event_url=event_url,
            last_verified=datetime.now(timezone.utc).date().isoformat(),
            notes=desc,
        ))

    return events


def fetch_insightla(pages: int = 2) -> list[Event]:
    """
    Fetch events from InsightLA's fullcalendar page.

    InsightLA uses a custom WordPress theme with Events Manager (em_) plugin.
    Events are server-side rendered with schema.org Event markup — no JS needed.
    The page uses YITH Infinite Scrolling with standard pagination (?paged=N).

    Args:
        pages: Number of pages to fetch (default 2; ~20 events/page).
    """
    center = CENTERS["insightla"]
    base_url = "https://insightla.org/fullcalendar/"
    all_events: list[Event] = []
    seen_ids: set[str] = set()

    for page in range(1, pages + 1):
        url = base_url if page == 1 else f"{base_url}?paged={page}"
        log.info(f"Fetching InsightLA calendar page {page}: {url}")

        try:
            resp = httpx.get(url, headers=HEADERS, follow_redirects=True, timeout=30)
            resp.raise_for_status()
        except httpx.HTTPError as e:
            log.error(f"InsightLA fetch failed (page {page}): {e}")
            break

        events = _parse_insightla_events(resp.text, center)
        log.info(f"  Page {page}: {len(events)} events parsed")

        new_count = 0
        for ev in events:
            if ev.id not in seen_ids:
                seen_ids.add(ev.id)
                all_events.append(ev)
                new_count += 1

        # Stop if page returned no new events (reached end of pagination)
        if new_count == 0 and page > 1:
            break

    log.info(f"InsightLA total: {len(all_events)} unique events")
    return all_events
