"""
Subscribe to and parse iCal feeds.
Handles filtering to actual meditation sits via keyword matching + LLM fallback.
"""

import hashlib
from datetime import datetime, timezone
from typing import Optional
from urllib.parse import urlparse

import httpx
from icalendar import Calendar

from data.schemas.event import Event, LocationType, SourceType, Tradition
from ingestion.llm_classifier import classify_event


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


def detect_location_type(
    title: str,
    description: str = "",
    location: str = "",
    event_url: str = "",
) -> tuple[LocationType, bool]:
    """
    Heuristic location detection. Returns (LocationType, certain).
    certain=False means no positive signal was found — LLM should be consulted.
    """
    # Also scan the URL slug — catches "online-midday-sangha" style naming
    url_slug = urlparse(event_url).path.lower() if event_url else ""
    text = (title + " " + description + " " + location + " " + url_slug).lower()

    if any(kw in text for kw in HYBRID_KEYWORDS):
        return LocationType.HYBRID, True
    # Zoom/Meet/Teams URL in LOCATION field is a definitive online signal
    if any(kw in location.lower() for kw in ("zoom.us", "meet.google", "teams.microsoft")):
        return LocationType.ONLINE, True
    if any(kw in text for kw in ONLINE_KEYWORDS):
        return LocationType.ONLINE, True

    # No positive signal — default in-person but flag as uncertain
    return LocationType.IN_PERSON, False


def is_likely_sit(title: str, description: str = "") -> tuple[bool, bool]:
    """
    Heuristic sit detection. Returns (is_sit, certain).
    certain=False when no keywords matched at all (LLM should confirm).
    """
    text = (title + " " + description).lower()
    has_sit = any(kw in text for kw in SIT_KEYWORDS)
    has_exclude = any(kw in text for kw in EXCLUDE_KEYWORDS)
    if has_exclude:
        return False, True
    if has_sit:
        return True, True
    return True, False  # no signal — optimistically include, but uncertain


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

        if not title or not dtstart:
            continue

        start_str = dtstart.dt.isoformat() if hasattr(dtstart.dt, "isoformat") else str(dtstart.dt)
        end_str   = dtend.dt.isoformat() if dtend and hasattr(dtend.dt, "isoformat") else None

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
