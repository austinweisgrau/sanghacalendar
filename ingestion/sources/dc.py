"""
Washington DC meditation center sources — Phase 3 DC expansion.
Defines known DC-area centers and their ingestion strategies.

Primary source: IMCW (Insight Meditation Community of Washington) via EventAgent API.
IMCW is a distributed community with drop-in sits at 10+ venues across DC, MD, and VA.
"""

import hashlib
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Optional

import httpx
from dateutil.rrule import rrulestr

from data.schemas.event import Center, Event, LocationType, SourceType, Tradition
from ingestion.utils import is_likely_sit

log = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "imcw": Center(
        id="imcw",
        name="Insight Meditation Community of Washington",
        url="https://imcw.org",
        address="276 Carroll St NW",
        city="Washington",
        state="DC",
        zip_code="20012",
        lat=38.9776,
        lng=-77.0128,
        neighborhood="Takoma",
        tradition=Tradition.THERAVADA,
        notes=(
            "IMCW — the largest Insight/Vipassana community in the DC metro area. "
            "Co-founded by Tara Brach and Jonathan Foust. Offers drop-in meditation "
            "classes at 10+ venues across DC, Maryland, and Northern Virginia. "
            "Classes include 30-minute guided meditation, dharma talk, and Q&A. "
            "Hybrid in-person and online programs. Free, all welcome."
        ),
    ),
    "shambhala_dc": Center(
        id="shambhala_dc",
        name="Shambhala Meditation Center of Washington DC",
        url="https://dc.shambhala.org",
        address="278 Carroll St NW",
        city="Washington",
        state="DC",
        zip_code="20012",
        lat=38.9779,
        lng=-77.0127,
        neighborhood="Takoma",
        tradition=Tradition.TIBETAN,
        notes=(
            "DC Shambhala Center — Shambhala Buddhist meditation center "
            "(Chögyam Trungpa lineage), one block from Takoma Metro. "
            "Open Public Sitting first Sunday monthly 1:30–2:30pm at Seekers Church "
            "(276 Carroll St NW). Free meditation instruction available. "
            "iCal feed (shambhala-koeln.de center=205) currently unreachable."
        ),
    ),
}

# ---------------------------------------------------------------------------
# IMCW EventAgent venue registry
# Maps EventAgent venue names to location data for DC-metro venues.
# Venues NOT in this map are excluded (rural retreat centers, Baltimore, etc.)
# ---------------------------------------------------------------------------

_VENUE_MAP: dict[str, dict] = {
    # DC venues
    "Iona": dict(
        address="4510 Nebraska Ave NW", city="Washington", state="DC",
        zip_code="20016", lat=38.9476, lng=-77.0880, neighborhood="Tenleytown", online=False,
    ),
    "Yoga District": dict(
        address="1834 11th St NW", city="Washington", state="DC",
        zip_code="20001", lat=38.9195, lng=-77.0282, neighborhood="U Street / Cardoza", online=False,
    ),
    "Unity of Washington DC": dict(
        address="1225 R St NW", city="Washington", state="DC",
        zip_code="20009", lat=38.9121, lng=-77.0283, neighborhood="Logan Circle", online=False,
    ),
    "Seekers Church": dict(
        address="276 Carroll St NW", city="Washington", state="DC",
        zip_code="20012", lat=38.9776, lng=-77.0128, neighborhood="Takoma", online=False,
    ),
    "Seekers Church > Downstairs": dict(
        address="276 Carroll St NW", city="Washington", state="DC",
        zip_code="20012", lat=38.9776, lng=-77.0128, neighborhood="Takoma", online=False,
    ),
    "Seekers Church > Upstairs": dict(
        address="276 Carroll St NW", city="Washington", state="DC",
        zip_code="20012", lat=38.9776, lng=-77.0128, neighborhood="Takoma", online=False,
    ),
    # Maryland suburbs
    "River Road Unitarian Universalist Congregation (RRUUC)": dict(
        address="6301 River Rd", city="Bethesda", state="MD",
        zip_code="20817", lat=38.9698, lng=-77.1304, neighborhood="Bethesda", online=False,
    ),
    # Northern Virginia suburbs
    "Body Grace": dict(
        address="243 Church St NW", city="Vienna", state="VA",
        zip_code="22180", lat=38.9013, lng=-77.2666, neighborhood="Vienna", online=False,
    ),
    "Unitarian Universalist Church (UUCA)": dict(
        address="4444 Arlington Blvd", city="Arlington", state="VA",
        zip_code="22204", lat=38.8726, lng=-77.1221, neighborhood="Arlington", online=False,
    ),
    # Online venues
    "Online": dict(city="Washington", state="DC", online=True),
    "Zoom": dict(city="Washington", state="DC", online=True),
    "Zoom hosted by Secure Zoom 1": dict(city="Washington", state="DC", online=True),
    "Zoom hosted by Secure Zoom 2": dict(city="Washington", state="DC", online=True),
    "Zoom hosted by Secure Zoom 3": dict(city="Washington", state="DC", online=True),
    "Zoom hosted by Secure Zoom 4": dict(city="Washington", state="DC", online=True),
    # IMCW YouTube (for hybrid/recorded special events)
    "IMCW YouTube": dict(city="Washington", state="DC", online=True),
}

# Venues explicitly excluded (rural retreat centers, out-of-metro)
_EXCLUDED_VENUES = {
    "Seven Oaks Retreat Center",   # Madison VA — 2 hours from DC
    "Claymont Great Barn",         # Charles Town WV — 1 hour from DC
    "St. Francis Episcopal Church", # Great Falls VA — 45 min, occasional only
    "Creative Alliance",           # Baltimore MD — not DC metro
    "Blueberry Gardens Healing Center",  # Ashton MD — retreat center
}


# ---------------------------------------------------------------------------
# IMCW EventAgent scraper
# ---------------------------------------------------------------------------

def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _get_ea_key() -> Optional[str]:
    """Extract EventAgent API key from IMCW events page HTML."""
    try:
        resp = httpx.get(
            "https://imcw.org/events/", headers=HEADERS, follow_redirects=True, timeout=20
        )
        resp.raise_for_status()
        m = re.search(r'"ea-key"\s*:\s*"([^"]+)"', resp.text)
        if m:
            return m.group(1)
        log.error("IMCW: ea-key not found in events page HTML")
        return None
    except httpx.HTTPError as e:
        log.error(f"IMCW: failed to fetch events page: {e}")
        return None


def _expand_rrule(rrule_str: str, window_days: int = 90) -> list[datetime]:
    """Expand an iCal RRULE string to datetime instances within the next window_days.

    Strips TZID qualifiers before parsing so all datetimes are naive.
    IMCW uses America/New_York — times are stored as local ET for display.
    """
    now = datetime.now()
    until = now + timedelta(days=window_days)
    # Strip TZID qualifiers: "DTSTART;TZID=America/New_York:..." → "DTSTART:..."
    clean = re.sub(r";TZID=[^:]+", "", rrule_str)
    try:
        rule = rrulestr(clean, ignoretz=True)
        return list(rule.between(now, until, inc=True))
    except Exception as e:
        log.warning(f"IMCW: rrule expansion failed: {e}")
        return []


def _resolve_venue(venues_str: str) -> Optional[dict]:
    """
    Resolve a venues string (e.g. "Body Grace and Zoom hosted by Secure Zoom 1")
    to location metadata. Returns None if all venues are excluded or unknown.
    Prefers physical venue; marks as HYBRID if also has online component.
    """
    parts = [v.strip() for v in venues_str.split(" and ")]
    physical: Optional[dict] = None
    has_online = False

    for part in parts:
        if part in _EXCLUDED_VENUES:
            # Entire event excluded if the physical venue is a retreat center
            return None
        if part in _VENUE_MAP:
            info = _VENUE_MAP[part]
            if info.get("online"):
                has_online = True
            else:
                physical = info
        # Unknown venue name: not in map, not in excluded → treat as unknown/skip

    if physical is not None:
        loc_type = LocationType.HYBRID if has_online else LocationType.IN_PERSON
        return {"loc_type": loc_type, **physical}
    elif has_online:
        return {"loc_type": LocationType.ONLINE, "city": "Washington", "state": "DC", "online": True}
    else:
        return None  # all venues unrecognized or excluded


def fetch_imcw(window_days: int = 90) -> list[Event]:
    """
    Fetch events from IMCW via EventAgent API.

    Strategy:
    - Extract ea-key from imcw.org/events/ HTML
    - Call EventAgent ListView endpoint (returns ~20 events total)
    - For Ongoing (recurring) events: expand RRULE for next window_days
    - For Singleton/Course events: use startDate directly
    - Filter to DC-metro venues; exclude retreat centers
    """
    ea_key = _get_ea_key()
    if not ea_key:
        return []

    try:
        resp = httpx.get(
            "https://api.eventagent.ai/api/ListView/?tz=America/New_York",
            headers={**HEADERS, "ea-key": ea_key, "Accept": "application/json"},
            timeout=30,
        )
        resp.raise_for_status()
        items = resp.json()
    except Exception as e:
        log.error(f"IMCW: EventAgent API error: {e}")
        return []

    if not isinstance(items, list):
        log.error(f"IMCW: unexpected response type from EventAgent: {type(items)}")
        return []

    log.info(f"IMCW: {len(items)} events from EventAgent API")

    now = datetime.now(timezone.utc)
    today_str = now.date().isoformat()
    center = CENTERS["imcw"]
    events: list[Event] = []

    for item in items:
        title = item.get("name", "").strip()
        if not title:
            continue

        venues_str = item.get("venues", "")
        venue_info = _resolve_venue(venues_str)
        if venue_info is None:
            log.debug(f"IMCW: skipping '{title}' — no DC-metro venue: {venues_str!r}")
            continue

        loc_type: LocationType = venue_info["loc_type"]
        duration_ms = item.get("duration", 3600000)
        duration = timedelta(milliseconds=duration_ms)
        detail_url = item.get("detailUrl", "")
        event_url = f"https://imcw.org{detail_url}" if detail_url else None
        description = (item.get("summary") or "")[:400]
        event_type = item.get("type", "Singleton")
        rrule_str = item.get("rrule")
        # Ongoing (recurring) IMCW events are drop-in meditation classes — always is_sit
        if event_type == "Ongoing":
            sit_result = True
        else:
            sit_result, _ = is_likely_sit(title, description)

        def make_event(start_dt: datetime, _title: str = title) -> Event:
            end_dt = start_dt + duration
            start_str = start_dt.strftime("%Y-%m-%dT%H:%M:%S")
            end_str = end_dt.strftime("%Y-%m-%dT%H:%M:%S")
            return Event(
                id=_event_id("imcw", _title, start_str),
                org_id="imcw",
                org_name=center.name,
                title=_title,
                start_time=start_str,
                end_time=end_str,
                address=venue_info.get("address"),
                city=venue_info.get("city", "Washington"),
                state=venue_info.get("state", "DC"),
                neighborhood=venue_info.get("neighborhood"),
                lat=venue_info.get("lat"),
                lng=venue_info.get("lng"),
                tradition=center.tradition,
                location_type=loc_type,
                is_sit=sit_result,
                source=SourceType.STATIC_HTML,
                source_url="https://imcw.org/events/",
                event_url=event_url,
                last_verified=today_str,
                notes=description if description else None,
            )

        if event_type == "Ongoing" and rrule_str:
            instances = _expand_rrule(rrule_str, window_days)
            log.info(f"  IMCW recurring: '{title}' @ {venues_str} → {len(instances)} instances")
            for dt in instances:
                events.append(make_event(dt))
        else:
            # Singleton or Course — single occurrence
            start_str_raw = item.get("startDate", "")
            if not start_str_raw:
                continue
            try:
                start_dt = datetime.fromisoformat(start_str_raw)
                # Normalize to naive UTC for comparison
                if start_dt.tzinfo is not None:
                    start_utc = start_dt.astimezone(timezone.utc).replace(tzinfo=None)
                else:
                    start_utc = start_dt
                now_naive = now.replace(tzinfo=None)
                if start_utc < now_naive:
                    continue
                if start_utc > now_naive + timedelta(days=window_days):
                    continue
            except ValueError:
                log.warning(f"IMCW: bad startDate: {start_str_raw!r}")
                continue
            events.append(make_event(start_dt.replace(tzinfo=None)))

    log.info(f"IMCW total: {len(events)} events")
    return events
