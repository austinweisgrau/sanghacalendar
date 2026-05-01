"""
LLM-assisted static HTML calendar scraper.

For centers that publish events as unstructured HTML text (Squarespace,
WordPress without a calendar plugin, custom pages) — fetch the page, extract
text, and ask Claude Haiku to pull out structured event data.

No iCal feed, no JSON API: just a page of text with dates and event names.

Usage:
    from ingestion.scrapers.static_html import fetch_static_html_calendar
    events = fetch_static_html_calendar(
        url="https://bayzen.org/calendar",
        org_id="bay_zen",
        org_name="Bay Zen Center",
        ...
    )

Requires ANTHROPIC_API_KEY in environment. If not set, returns empty list
and logs a warning (so the overall ingest still runs for other sources).
"""

import hashlib
import json
import logging
import os
import re
from datetime import date, datetime, timezone
from typing import Optional

import httpx

from data.schemas.event import Event, LocationType, SourceType, Tradition
from ingestion.utils import detect_location_type, is_likely_sit

log = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

EXTRACT_PROMPT = """\
You are extracting upcoming events from a Buddhist meditation center's website calendar page.
Today is {today}. Extract ONLY events that start on or after today.

Raw page text:
---
{page_text}
---

Return a JSON array of events. For each event:
{{
  "title": "event name",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD or null (only if multi-day and different from start)",
  "start_time": "HH:MM or null",
  "end_time": "HH:MM or null",
  "is_sit": true/false,
  "location_type": "in-person" | "online" | "hybrid",
  "notes": "any extra info from the page, or null"
}}

Rules:
- is_sit = true if sitting meditation is the primary activity (zazen, zazenkai, meditation period, sesshin)
- is_sit = false for pure ceremonies, work days, potlucks, closures, dharma talks/classes, retreats where sitting isn't primary
- sesshin and zazenkai: is_sit = true (they are extended sitting retreats)
- location_type = "online" if explicitly Zoom/online; "hybrid" if both; "in-person" otherwise
- If year is not stated, infer from context (current year {year} unless the month has passed, then {next_year})
- Skip closures, recess periods, and administrative events (re-opening announcements)
- Skip past events (before today {today})
- Return [] if no upcoming events found

Return ONLY valid JSON array, no markdown, no explanation."""


def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _html_to_text(html: str) -> str:
    """Strip HTML tags to plain text, preserving whitespace structure."""
    # Remove script/style blocks entirely
    html = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    # Replace common block tags with newlines
    html = re.sub(r'<(br|p|div|li|tr|h[1-6])[^>]*>', '\n', html, flags=re.IGNORECASE)
    # Strip remaining tags
    html = re.sub(r'<[^>]+>', ' ', html)
    # Decode common HTML entities
    html = html.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>') \
               .replace('&nbsp;', ' ').replace('&#8212;', '—').replace('&#8211;', '–') \
               .replace('&mdash;', '—').replace('&ndash;', '–').replace('&rsquo;', "'") \
               .replace('&lsquo;', "'").replace('&rdquo;', '"').replace('&ldquo;', '"')
    # Collapse whitespace
    lines = [line.strip() for line in html.split('\n')]
    lines = [ln for ln in lines if ln]
    return '\n'.join(lines)


def _call_llm(page_text: str, today: str, year: int, next_year: int) -> list[dict]:
    """Call Claude Haiku to extract events from page text. Returns list of raw event dicts."""
    try:
        import anthropic
    except ImportError:
        log.warning("anthropic package not installed — static_html scraper requires it")
        return []

    key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_SDK_API_KEY")
    if not key:
        log.warning("ANTHROPIC_API_KEY not set — skipping static HTML scrape")
        return []

    client = anthropic.Anthropic(api_key=key)
    prompt = EXTRACT_PROMPT.format(
        today=today,
        year=year,
        next_year=next_year,
        page_text=page_text[:8000],  # cap at 8k chars to stay within context
    )

    try:
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        # Strip markdown fences if present
        raw = re.sub(r'^```(?:json)?\s*', '', raw, flags=re.MULTILINE)
        raw = re.sub(r'\s*```$', '', raw, flags=re.MULTILINE)
        return json.loads(raw)
    except json.JSONDecodeError as e:
        log.error(f"LLM returned invalid JSON for static HTML scrape: {e}")
        return []
    except Exception as e:
        log.error(f"LLM call failed for static HTML scrape: {e}")
        return []


def _parse_event(
    raw: dict,
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
    source_url: str,
) -> Optional[Event]:
    """Convert a raw LLM-extracted event dict to an Event object."""
    title = str(raw.get("title", "")).strip()
    if not title:
        return None

    start_date = raw.get("start_date")
    if not start_date:
        return None

    start_time = raw.get("start_time")
    end_date = raw.get("end_date") or start_date
    end_time = raw.get("end_time")

    # Build ISO datetime strings
    if start_time:
        start_str = f"{start_date}T{start_time}:00"
    else:
        start_str = f"{start_date}T00:00:00"

    if end_time:
        end_str = f"{end_date}T{end_time}:00"
    elif end_date and end_date != start_date:
        end_str = f"{end_date}T23:59:00"
    else:
        end_str = None

    # Skip past events (belt-and-suspenders check)
    try:
        if datetime.fromisoformat(start_str) < datetime.now():
            return None
    except Exception:
        pass

    is_sit = raw.get("is_sit", True)
    if filter_to_sits and not is_sit:
        return None

    loc_type_raw = raw.get("location_type", "in-person")
    try:
        loc_type = LocationType(loc_type_raw)
    except ValueError:
        loc_type = LocationType.IN_PERSON

    notes = raw.get("notes")

    return Event(
        id=_event_id(org_id, title, start_str),
        org_id=org_id,
        org_name=org_name,
        title=title,
        start_time=start_str,
        end_time=end_str,
        address=address,
        city=city,
        state=state,
        neighborhood=neighborhood,
        lat=lat,
        lng=lng,
        tradition=tradition,
        location_type=loc_type,
        is_sit=is_sit,
        source=SourceType.STATIC_HTML,
        source_url=source_url,
        event_url=None,
        last_verified=datetime.now(timezone.utc).date().isoformat(),
        notes=notes,
    )


def fetch_static_html_calendar(
    url: str,
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
    Scrape a static HTML calendar page using LLM extraction.

    Fetches the page, strips HTML to plain text, then asks Claude Haiku
    to extract event data as structured JSON. Requires ANTHROPIC_API_KEY.

    Args:
        url: Calendar page URL to scrape
        org_id: Internal center slug (e.g. "bay_zen")
        org_name: Human-readable center name
        filter_to_sits: If True, exclude non-sit events (talks, ceremonies, etc.)
        ...standard location/tradition args...

    Returns:
        List of upcoming Event objects extracted from the page.
    """
    log.info(f"Fetching static HTML calendar: {url}")

    try:
        resp = httpx.get(url, headers=HEADERS, follow_redirects=True, timeout=20)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        log.error(f"Failed to fetch {url} for {org_name}: {e}")
        return []

    page_text = _html_to_text(resp.text)
    log.debug(f"  Extracted {len(page_text)} chars of text from {url}")

    today = datetime.now().date().isoformat()
    year = datetime.now().year
    next_year = year + 1

    raw_events = _call_llm(page_text, today, year, next_year)
    log.info(f"  LLM extracted {len(raw_events)} raw events from {org_name}")

    events = []
    for raw in raw_events:
        ev = _parse_event(
            raw, org_id, org_name, tradition, filter_to_sits,
            address, city, state, neighborhood, lat, lng, url,
        )
        if ev:
            events.append(ev)

    log.info(f"  → {len(events)} events parsed for {org_name}")
    return events
