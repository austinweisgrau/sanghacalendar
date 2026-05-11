"""
Wild Apricot RSS calendar scraper.

Wild Apricot membership sites expose event listings via RSS at /Calendar/RSS.
Each <item> has:
  - <title>Event Name (DD Mon YYYY)</title>
  - <pubDate>Day, DD Mon YYYY HH:MM:SS GMT</pubDate>  — event START time in UTC
  - <description>HTML content</description>
  - <link>event URL</link>

Usage:
    from ingestion.scrapers.wild_apricot_rss import fetch_wild_apricot_rss
    events = fetch_wild_apricot_rss(
        url="https://redclaysangha.org/Calendar/RSS",
        org_id="red_clay_sangha",
        org_name="Red Clay Sangha",
        ...
        title_keywords=["Meditation", "Mindfulness", "Insight Dialog"],
    )
"""

import hashlib
import logging
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Optional
from xml.etree import ElementTree as ET

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
    "Accept": "application/rss+xml, application/xml, text/xml, */*;q=0.8",
}


def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _strip_html(html: str) -> str:
    """Strip HTML tags and decode basic entities."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = (text
            .replace("&amp;", "&")
            .replace("&nbsp;", " ")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&#8211;", "–")
            .replace("&#8212;", "—"))
    return re.sub(r"\s+", " ", text).strip()


def _clean_title(raw: str) -> str:
    """Strip the trailing ' (DD Mon YYYY)' date suffix Wild Apricot appends."""
    return re.sub(r"\s*\(\d{1,2}\s+\w+\s+\d{4}\)\s*$", "", raw).strip()


def _parse_pubdate(date_str: str) -> Optional[datetime]:
    """Parse RFC 2822 pubDate to UTC datetime."""
    try:
        return parsedate_to_datetime(date_str).astimezone(timezone.utc)
    except Exception:
        return None


def fetch_wild_apricot_rss(
    url: str,
    org_id: str,
    org_name: str,
    tradition: Tradition,
    title_keywords: list[str],
    address: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    neighborhood: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    duration_min: int = 90,
    filter_to_sits: bool = True,
) -> list[Event]:
    """
    Fetch events from a Wild Apricot RSS feed and filter to meditation sits.

    Args:
        url: Wild Apricot RSS URL (e.g. https://example.org/Calendar/RSS).
        org_id: Canonical org identifier.
        org_name: Human-readable org name.
        tradition: Buddhist tradition enum.
        title_keywords: Only include events whose title contains one of these strings.
        address, city, state, neighborhood, lat, lng: Center location info.
        duration_min: Default event duration in minutes (used when no end time).
        filter_to_sits: If True, also run is_likely_sit check after keyword filter.

    Returns:
        List of Event objects for future sits.
    """
    log.info(f"Fetching Wild Apricot RSS: {url}")

    try:
        resp = httpx.get(url, headers=HEADERS, timeout=20, follow_redirects=True)
        resp.raise_for_status()
        content = resp.text
    except Exception as e:
        log.error(f"  ✗ Failed to fetch {url}: {e}")
        return []

    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        log.error(f"  ✗ XML parse error for {url}: {e}")
        return []

    items = root.findall(".//item")
    log.info(f"  → {len(items)} raw items in RSS feed")

    now = datetime.now(tz=timezone.utc)
    events: list[Event] = []
    keywords_lower = [k.lower() for k in title_keywords]

    for item in items:
        raw_title = item.findtext("title", "").strip()
        title = _clean_title(raw_title)
        pub_date_str = item.findtext("pubDate", "")
        event_url = item.findtext("link", url)
        description_html = item.findtext("description", "")
        description = _strip_html(description_html)

        # Keyword filter — must match at least one keyword
        title_lower = title.lower()
        if not any(kw in title_lower for kw in keywords_lower):
            continue

        # Parse event start time from pubDate (Wild Apricot stores UTC start time)
        start_dt = _parse_pubdate(pub_date_str)
        if not start_dt:
            log.debug(f"  skip (no date): {title}")
            continue

        # Skip past events
        if start_dt <= now:
            continue

        # Build end time from duration
        from datetime import timedelta
        end_dt = start_dt + timedelta(minutes=duration_min)

        start_iso = start_dt.isoformat()
        end_iso = end_dt.isoformat()

        # Optional is_likely_sit check
        if filter_to_sits:
            sit_result, _ = is_likely_sit(title, description)
            if not sit_result:
                log.debug(f"  skip (not sit): {title}")
                continue
        else:
            sit_result = True

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
            source=SourceType.RSS_FEED,
            source_url=url,
            event_url=event_url,
            last_verified=now.date().isoformat(),
            notes=description[:500] if description else None,
        )
        events.append(event)

    log.info(f"  → {len(events)} events after keyword+sit filter")
    return events
