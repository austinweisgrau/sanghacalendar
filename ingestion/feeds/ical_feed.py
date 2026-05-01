"""
Subscribe to and parse iCal feeds.
Handles filtering to actual meditation sits via keyword matching + LLM fallback.
"""

import hashlib
import re
from datetime import datetime, timezone
from typing import Optional

import httpx
from icalendar import Calendar

from data.schemas.event import Event, LocationType, SourceType, Tradition
from ingestion.llm_classifier import classify_event
from ingestion.utils import detect_location_type, is_likely_sit


def event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def fetch_feed(
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
    Fetch an iCal feed and return normalized Event objects.
    Uses keyword heuristics first; falls back to Claude Haiku for uncertain cases.
    """
    resp = httpx.get(url, follow_redirects=True, timeout=15)
    resp.raise_for_status()

    cal = Calendar.from_ical(resp.content)
    events = []

    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        title       = str(component.get("SUMMARY", "")).strip()
        description = str(component.get("DESCRIPTION", "")).strip()
        location    = str(component.get("LOCATION", "")).strip()
        dtstart     = component.get("DTSTART")
        dtend       = component.get("DTEND")
        event_url   = str(component.get("URL", "")) or None

        if not dtstart:
            continue

        # Fallback for feeds that omit SUMMARY (e.g. IMC Berkeley Google Calendar exports)
        if not title:
            raw_desc = str(component.get("DESCRIPTION", ""))
            clean = re.sub(r'<[^>]+>', ' ', raw_desc).strip()
            first_line = clean.split('\n')[0][:80].strip() if clean else ""
            title = first_line or f"{org_name} Sit"

        # Normalize to UTC ISO string (ends in +00:00) so the same event always
        # hashes to the same ID regardless of whether the feed uses TZID or Z.
        def _to_utc_iso(dt_val) -> str:
            if hasattr(dt_val, "tzinfo") and dt_val.tzinfo is not None:
                return dt_val.astimezone(timezone.utc).isoformat()
            # date-only or naive — return as-is
            return dt_val.isoformat() if hasattr(dt_val, "isoformat") else str(dt_val)

        start_str = _to_utc_iso(dtstart.dt)
        end_str   = _to_utc_iso(dtend.dt) if dtend else None

        # --- Sit classification ---
        sit_result, sit_certain = is_likely_sit(title, description)
        if filter_to_sits and not sit_certain and not sit_result:
            continue  # definitively not a sit

        # --- Location classification ---
        loc_type, loc_certain = detect_location_type(title, description, location, event_url or "")

        # --- LLM fallback for uncertain cases ---
        if not sit_certain or not loc_certain:
            llm = classify_event(title, description, location, event_url or "")
            if llm:
                if not loc_certain:
                    loc_type = LocationType(llm["location_type"])
                if not sit_certain:
                    sit_result = llm["is_sit"]

        if filter_to_sits and not sit_result:
            continue

        events.append(Event(
            id=event_id(org_id, title, start_str),
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
            is_sit=sit_result,
            source=SourceType.ICAL_FEED,
            source_url=url,
            event_url=event_url,
            last_verified=datetime.now(timezone.utc).date().isoformat(),
            notes=description[:300] if description else None,
        ))

    return events
