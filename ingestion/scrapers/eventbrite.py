"""
Eventbrite organizer page scraper.

Fetches events from a public Eventbrite organizer page by parsing
the __NEXT_DATA__ JSON blob embedded in the page HTML.

No API key required — uses the public organizer listing page.

Usage:
    from ingestion.scrapers.eventbrite import fetch_eventbrite_organizer
    events = fetch_eventbrite_organizer(
        organizer_id="336367203",
        org_id="nyingma_institute",
        org_name="Nyingma Institute",
        ...
    )
"""

import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from typing import Optional

import httpx

from data.schemas.event import Event, LocationType, SourceType, Tradition
from ingestion.utils import detect_location_type, is_likely_sit

log = logging.getLogger(__name__)

EVENTBRITE_BASE = "https://www.eventbrite.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _parse_eventbrite_datetime(dt_str: Optional[str]) -> Optional[str]:
    """
    Parse Eventbrite datetime strings like "2026-05-10T14:00:00" or
    "2026-05-10T14:00:00Z" into ISO format.
    """
    if not dt_str:
        return None
    try:
        # Eventbrite returns local times in their API/JSON blobs
        # Try to parse as-is
        dt_str = dt_str.rstrip("Z")
        if "T" in dt_str:
            return dt_str
        return dt_str
    except Exception:
        return dt_str


def _extract_events_from_next_data(data: dict) -> list[dict]:
    """
    Navigate the __NEXT_DATA__ structure to find event listings.
    Eventbrite's Next.js page embeds event data in various locations
    depending on page version.

    Handles two formats:
    1. API v3 style: {"name": "...", "start": {"local": "..."}}
    2. __NEXT_DATA__ style: {"name": "...", "start_date": "...", "start_time": "..."}
    """
    events = []

    def _is_event(obj: dict) -> bool:
        # Format 1: nested start object
        if (
            "name" in obj
            and isinstance(obj.get("start"), dict)
            and "local" in obj.get("start", {})
        ):
            return True
        # Format 2: flat start_date + start_time (Eventbrite __NEXT_DATA__)
        if "start_date" in obj and "start_time" in obj and "name" in obj:
            return True
        return False

    def _search(obj, depth=0):
        if depth > 10:
            return
        if isinstance(obj, list):
            for item in obj:
                _search(item, depth + 1)
        elif isinstance(obj, dict):
            if _is_event(obj):
                events.append(obj)
                return
            for v in obj.values():
                _search(v, depth + 1)

    _search(data)
    return events


def _parse_event_obj(
    raw: dict,
    org_id: str,
    org_name: str,
    tradition: Tradition,
    address: Optional[str],
    city: Optional[str],
    state: Optional[str],
    neighborhood: Optional[str],
    lat: Optional[float],
    lng: Optional[float],
    filter_to_sits: bool,
) -> Optional[Event]:
    """Convert a raw Eventbrite event dict to an Event."""
    # Extract title
    title = (
        raw.get("name", {}).get("text") if isinstance(raw.get("name"), dict)
        else raw.get("name") or raw.get("summary", "")
    )
    if not title:
        return None
    title = str(title).strip()

    # Extract start/end times — handle two formats:
    # 1. Nested:   {"start": {"local": "2026-05-01T06:00:00"}}  (API v3 style)
    # 2. Flat:     {"start_date": "2026-05-01", "start_time": "06:00:00"}  (__NEXT_DATA__ style)
    start_obj = raw.get("start")
    end_obj = raw.get("end")
    if isinstance(start_obj, dict):
        start_str = start_obj.get("local") or start_obj.get("utc")
        end_str = (end_obj.get("local") or end_obj.get("utc")) if isinstance(end_obj, dict) else None
    else:
        # Flat fields: combine start_date + start_time
        start_date = raw.get("start_date", "")
        start_time = raw.get("start_time", "")
        start_str = f"{start_date}T{start_time}" if start_date and start_time else start_date or None
        end_date = raw.get("end_date", "")
        end_time = raw.get("end_time", "")
        end_str = f"{end_date}T{end_time}" if end_date and end_time else end_date or None

    start_str = _parse_eventbrite_datetime(start_str)
    end_str = _parse_eventbrite_datetime(end_str)

    if not start_str:
        return None

    # Skip past events
    try:
        start_dt = datetime.fromisoformat(start_str.rstrip("Z"))
        if start_dt < datetime.now():
            return None
    except Exception:
        pass

    # Description
    description = (
        raw.get("description", {}).get("text") if isinstance(raw.get("description"), dict)
        else raw.get("description") or ""
    )
    description = str(description or "").strip()

    # Event URL
    event_url = raw.get("url") or raw.get("eventbrite_url")

    # Venue / location
    venue = raw.get("venue") or {}
    if isinstance(venue, dict):
        venue_address = venue.get("address", {})
        if isinstance(venue_address, dict):
            loc_address = venue_address.get("address_1") or venue_address.get("localized_address_display")
            loc_city = venue_address.get("city") or city
            loc_state = venue_address.get("region") or state
        else:
            loc_address, loc_city, loc_state = address, city, state
        venue_name = venue.get("name", "")
        loc_str = f"{venue_name} {loc_address or ''} {loc_city or ''}".strip()
    else:
        loc_address, loc_city, loc_state = address, city, state
        loc_str = ""

    # Use provided address/city/state as fallback
    final_address = loc_address or address
    final_city = loc_city or city
    final_state = loc_state or state

    # Sit / location classification
    sit_result, sit_certain = is_likely_sit(title, description)
    if filter_to_sits and not sit_result and sit_certain:
        return None

    loc_type, _ = detect_location_type(title, description, loc_str, event_url or "")

    return Event(
        id=_event_id(org_id, title, start_str),
        org_id=org_id,
        org_name=org_name,
        title=title,
        start_time=start_str,
        end_time=end_str,
        address=final_address,
        city=final_city,
        state=final_state,
        neighborhood=neighborhood,
        lat=lat,
        lng=lng,
        tradition=tradition,
        location_type=loc_type,
        is_sit=sit_result,
        source=SourceType.EVENTBRITE,
        source_url=f"{EVENTBRITE_BASE}/o/{org_id}-{raw.get('organizer_id', '')}",
        event_url=event_url,
        last_verified=datetime.now(timezone.utc).date().isoformat(),
        notes=description[:300] if description else None,
    )


def fetch_eventbrite_organizer(
    organizer_id: str,
    org_id: str,
    org_name: str,
    tradition: Tradition = Tradition.UNKNOWN,
    filter_to_sits: bool = True,
    address: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    neighborhood: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
) -> list[Event]:
    """
    Fetch upcoming events for an Eventbrite organizer.

    Scrapes the public organizer page and parses the __NEXT_DATA__ JSON blob.
    No API key required.

    Args:
        organizer_id: Eventbrite organizer numeric ID (e.g. "336367203")
        org_id: Internal center slug (e.g. "nyingma_institute")
        org_name: Human-readable center name
        ...standard location/tradition args...

    Returns:
        List of Event objects for upcoming events.
    """
    url = f"{EVENTBRITE_BASE}/o/{organizer_id}/"
    log.info(f"Fetching Eventbrite organizer page: {url}")

    try:
        resp = httpx.get(url, headers=HEADERS, follow_redirects=True, timeout=20)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        log.error(f"Failed to fetch Eventbrite page for {org_name}: {e}")
        return []

    html = resp.text

    # Extract __NEXT_DATA__ JSON
    match = re.search(r'<script[^>]+id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
    if not match:
        log.warning(f"No __NEXT_DATA__ found on Eventbrite page for {org_name}")
        # Fallback: try to find event URLs via href patterns
        return _scrape_event_links(html, org_id, org_name, tradition, filter_to_sits,
                                    address, city, state, neighborhood, lat, lng)

    try:
        next_data = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        log.error(f"Failed to parse __NEXT_DATA__ for {org_name}: {e}")
        return []

    raw_events = _extract_events_from_next_data(next_data)
    log.info(f"  Found {len(raw_events)} raw events in __NEXT_DATA__")

    if not raw_events:
        # Fallback to link scraping
        log.info("  Falling back to event link scraping")
        return _scrape_event_links(html, org_id, org_name, tradition, filter_to_sits,
                                    address, city, state, neighborhood, lat, lng)

    events = []
    for raw in raw_events:
        event = _parse_event_obj(
            raw, org_id, org_name, tradition,
            address, city, state, neighborhood, lat, lng,
            filter_to_sits,
        )
        if event:
            events.append(event)

    log.info(f"  → {len(events)} events parsed for {org_name}")
    return events


def _scrape_event_links(
    html: str,
    org_id: str,
    org_name: str,
    tradition: Tradition,
    filter_to_sits: bool,
    address: Optional[str],
    city: Optional[str],
    state: Optional[str],
    neighborhood: Optional[str],
    lat: Optional[float],
    lng: Optional[float],
) -> list[Event]:
    """
    Fallback: extract event URLs from organizer page HTML, then fetch each event
    page and parse its JSON-LD structured data.
    """
    # Find all event links like /e/event-slug-12345678901
    event_urls = list(dict.fromkeys(
        re.findall(r'href="(https://www\.eventbrite\.com/e/[^"?]+)"', html)
    ))
    log.info(f"  Found {len(event_urls)} event URLs via link scraping")

    events = []
    for event_url in event_urls[:20]:  # cap at 20 to avoid hammering
        try:
            ev = _fetch_event_page(
                event_url, org_id, org_name, tradition, filter_to_sits,
                address, city, state, neighborhood, lat, lng,
            )
            if ev:
                events.append(ev)
        except Exception as e:
            log.warning(f"  Failed to parse event {event_url}: {e}")

    return events


def _fetch_event_page(
    event_url: str,
    org_id: str,
    org_name: str,
    tradition: Tradition,
    filter_to_sits: bool,
    address: Optional[str],
    city: Optional[str],
    state: Optional[str],
    neighborhood: Optional[str],
    lat: Optional[float],
    lng: Optional[float],
) -> Optional[Event]:
    """Fetch a single Eventbrite event page and parse its JSON-LD."""
    resp = httpx.get(event_url, headers=HEADERS, follow_redirects=True, timeout=15)
    resp.raise_for_status()
    html = resp.text

    # Look for JSON-LD structured data
    jsonld_matches = re.findall(
        r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',
        html, re.DOTALL
    )
    for jsonld_str in jsonld_matches:
        try:
            data = json.loads(jsonld_str)
            if isinstance(data, list):
                data = data[0]
            if data.get("@type") == "Event":
                return _parse_jsonld_event(
                    data, event_url, org_id, org_name, tradition, filter_to_sits,
                    address, city, state, neighborhood, lat, lng,
                )
        except (json.JSONDecodeError, KeyError):
            continue

    # Fallback: try __NEXT_DATA__ on event page
    match = re.search(r'<script[^>]+id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
    if match:
        try:
            next_data = json.loads(match.group(1))
            raw_events = _extract_events_from_next_data(next_data)
            for raw in raw_events:
                raw["url"] = event_url
                ev = _parse_event_obj(
                    raw, org_id, org_name, tradition,
                    address, city, state, neighborhood, lat, lng,
                    filter_to_sits,
                )
                if ev:
                    return ev
        except Exception:
            pass

    return None


def _parse_jsonld_event(
    data: dict,
    event_url: str,
    org_id: str,
    org_name: str,
    tradition: Tradition,
    filter_to_sits: bool,
    address: Optional[str],
    city: Optional[str],
    state: Optional[str],
    neighborhood: Optional[str],
    lat: Optional[float],
    lng: Optional[float],
) -> Optional[Event]:
    """Parse a JSON-LD Event schema object."""
    title = str(data.get("name", "")).strip()
    if not title:
        return None

    start_str = _parse_eventbrite_datetime(data.get("startDate"))
    end_str = _parse_eventbrite_datetime(data.get("endDate"))

    if not start_str:
        return None

    # Skip past events
    try:
        start_dt = datetime.fromisoformat(start_str.rstrip("Z"))
        if start_dt < datetime.now():
            return None
    except Exception:
        pass

    description = str(data.get("description", "")).strip()

    # Location from JSON-LD
    loc_obj = data.get("location", {})
    if isinstance(loc_obj, dict):
        loc_name = loc_obj.get("name", "")
        loc_addr_obj = loc_obj.get("address", {})
        if isinstance(loc_addr_obj, dict):
            loc_address = loc_addr_obj.get("streetAddress") or address
            loc_city = loc_addr_obj.get("addressLocality") or city
            loc_state = loc_addr_obj.get("addressRegion") or state
        else:
            loc_address, loc_city, loc_state = address, city, state
        loc_str = f"{loc_name} {loc_address or ''} {loc_city or ''}".strip()
    else:
        loc_address, loc_city, loc_state = address, city, state
        loc_str = ""

    sit_result, sit_certain = is_likely_sit(title, description)
    if filter_to_sits and not sit_result and sit_certain:
        return None

    loc_type, _ = detect_location_type(title, description, loc_str, event_url)

    return Event(
        id=_event_id(org_id, title, start_str),
        org_id=org_id,
        org_name=org_name,
        title=title,
        start_time=start_str,
        end_time=end_str,
        address=loc_address or address,
        city=loc_city or city,
        state=loc_state or state,
        neighborhood=neighborhood,
        lat=lat,
        lng=lng,
        tradition=tradition,
        location_type=loc_type,
        is_sit=sit_result,
        source=SourceType.EVENTBRITE,
        source_url=f"{EVENTBRITE_BASE}/o/{org_id}",
        event_url=event_url,
        last_verified=datetime.now(timezone.utc).date().isoformat(),
        notes=description[:300] if description else None,
    )
