"""
Squarespace JSON calendar scraper.

Squarespace sites expose event listings as JSON via /?format=json on their
events collection pages. This returns structured event data with millisecond
timestamps and HTML descriptions — no API key or authentication needed.

Usage:
    from ingestion.scrapers.squarespace import fetch_squarespace_calendar
    events = fetch_squarespace_calendar(
        url="https://houstonzen.org/events-calendar",
        org_id="houston_zen",
        org_name="Houston Zen Center",
        ...
    )
"""

import hashlib
import logging
import re
from datetime import datetime, timezone
from typing import Optional
from urllib.parse import urlparse

import httpx

from data.schemas.event import Event, SourceType, Tradition
from ingestion.utils import detect_location_type, is_likely_sit

log = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/html, */*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _strip_html(html: str) -> str:
    """Strip HTML tags and decode basic entities."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = text.replace("&amp;", "&").replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", text).strip()


def _ms_to_iso(ms: int) -> Optional[str]:
    """Convert millisecond epoch timestamp to ISO 8601 string (UTC)."""
    if not ms:
        return None
    try:
        dt = datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
        return dt.isoformat()
    except Exception:
        return None


def fetch_squarespace_calendar(
    url: str,
    org_id: str,
    org_name: str,
    tradition: Tradition,
    filter_to_sits: bool = True,
    address: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    neighborhood: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
) -> list[Event]:
    """
    Fetch events from a Squarespace calendar page via the ?format=json API.

    Args:
        url: Base URL of the Squarespace events page (without ?format=json).
        org_id: Canonical org identifier.
        org_name: Human-readable org name.
        tradition: Buddhist tradition enum.
        filter_to_sits: If True, only return events that look like sits.
        address, city, state, neighborhood, lat, lng: Center location info.

    Returns:
        List of Event objects.
    """
    json_url = url.rstrip("/") + "?format=json"
    log.info(f"Fetching Squarespace JSON: {json_url}")

    try:
        resp = httpx.get(json_url, headers=HEADERS, timeout=20, follow_redirects=True)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        log.error(f"  ✗ Failed to fetch {json_url}: {e}")
        return []

    items = data.get("items", [])
    log.info(f"  → {len(items)} raw items from Squarespace")

    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    events: list[Event] = []
    now = datetime.now(tz=timezone.utc)

    for item in items:
        title = item.get("title", "").strip()
        if not title:
            continue

        start_ms = item.get("startDate")
        end_ms = item.get("endDate")
        if not start_ms:
            continue

        start_iso = _ms_to_iso(start_ms)
        end_iso = _ms_to_iso(end_ms) if end_ms else None

        # Skip past events
        try:
            start_dt = datetime.fromtimestamp(start_ms / 1000, tz=timezone.utc)
            if start_dt < now:
                continue
        except Exception:
            pass

        excerpt_html = item.get("excerpt", "")
        description = _strip_html(excerpt_html) if excerpt_html else ""

        full_url_path = item.get("fullUrl", "")
        event_url = f"{base_url}{full_url_path}" if full_url_path else url

        sit_result, _ = is_likely_sit(title, description)
        if filter_to_sits and not sit_result:
            log.debug(f"  skip (not sit): {title}")
            continue

        loc_type, _ = detect_location_type(title, description, address or "", event_url)

        event = Event(
            id=_event_id(org_id, title, start_iso),
            org_id=org_id,
            org_name=org_name,
            title=title,
            start_time=start_iso,
            end_time=end_iso,
            tradition=tradition,
            location_type=loc_type,
            address=address,
            city=city,
            state=state,
            neighborhood=neighborhood,
            lat=lat,
            lng=lng,
            is_sit=sit_result,
            source=SourceType.SQUARESPACE,
            source_url=url,
            event_url=event_url,
            last_verified=now.date().isoformat(),
            notes=description[:500] if description else None,
        )

        events.append(event)

    log.info(f"  → {len(events)} events after {'sit filter' if filter_to_sits else 'no filter'}")
    return events
