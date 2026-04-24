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


# Keywords that strongly suggest a meditation sit
SIT_KEYWORDS = [
    "sit", "zazen", "sitting", "meditation", "vipassana", "samadhi",
    "open practice", "drop-in", "morning sit", "evening sit", "daily sit",
    "meditation group", "sangha sit",
]

# Keywords that disqualify (talks, workshops, multi-day retreats, etc.)
EXCLUDE_KEYWORDS = [
    "retreat", "sesshin", "workshop", "dharma talk", "lecture", "seminar",
    "course", "class", "training", "daylong", "ceremony", "social",
    "book club", "study group", "teacher training", "orientation",
]


ONLINE_KEYWORDS = [
    "online", "virtual", "zoom", "webinar", "livestream", "live stream",
    "google meet", "teams", "remote", "via zoom", "via google",
]

HYBRID_KEYWORDS = ["hybrid", "in-person and online", "online and in-person"]


def detect_location_type(title: str, description: str = "", location: str = "") -> LocationType:
    text = (title + " " + description + " " + location).lower()
    if any(kw in text for kw in HYBRID_KEYWORDS):
        return LocationType.HYBRID
    # A Zoom/Meet URL in the location field is a strong online signal
    if any(kw in location.lower() for kw in ("zoom.us", "meet.google", "teams.microsoft")):
        return LocationType.ONLINE
    if any(kw in text for kw in ONLINE_KEYWORDS):
        return LocationType.ONLINE
    return LocationType.IN_PERSON


def is_likely_sit(title: str, description: str = "") -> bool:
    """Heuristic: is this event a meditation sit?"""
    text = (title + " " + description).lower()
    has_sit_keyword = any(kw in text for kw in SIT_KEYWORDS)
    has_exclude_keyword = any(kw in text for kw in EXCLUDE_KEYWORDS)
    return has_sit_keyword and not has_exclude_keyword


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
    If filter_to_sits=True, applies keyword heuristics to drop non-sits.
    """
    resp = httpx.get(url, follow_redirects=True, timeout=15)
    resp.raise_for_status()

    cal = Calendar.from_ical(resp.content)
    events = []

    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        title = str(component.get("SUMMARY", "")).strip()
        description = str(component.get("DESCRIPTION", "")).strip()
        location = str(component.get("LOCATION", "")).strip()
        dtstart = component.get("DTSTART")
        dtend = component.get("DTEND")
        event_url = str(component.get("URL", "")) or None

        if not title or not dtstart:
            continue

        start_str = dtstart.dt.isoformat() if hasattr(dtstart.dt, "isoformat") else str(dtstart.dt)
        end_str = dtend.dt.isoformat() if dtend and hasattr(dtend.dt, "isoformat") else None

        if filter_to_sits and not is_likely_sit(title, description):
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
            location_type=detect_location_type(title, description, location),
            source=SourceType.ICAL_FEED,
            source_url=url,
            event_url=event_url,
            last_verified=datetime.now(timezone.utc).date().isoformat(),
            notes=description[:300] if description else None,
        ))

    return events
