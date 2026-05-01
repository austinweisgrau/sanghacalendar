"""
Shared classification utilities for ingestion scrapers.
Kept separate so scrapers that don't need iCal parsing don't transitively
require the `icalendar` package.
"""

from urllib.parse import urlparse

from data.schemas.event import LocationType


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
    url_slug = urlparse(event_url).path.lower() if event_url else ""
    text = (title + " " + description + " " + location + " " + url_slug).lower()

    if any(kw in text for kw in HYBRID_KEYWORDS):
        return LocationType.HYBRID, True
    if any(kw in location.lower() for kw in ("zoom.us", "meet.google", "teams.microsoft")):
        return LocationType.ONLINE, True
    if any(kw in text for kw in ONLINE_KEYWORDS):
        return LocationType.ONLINE, True

    return LocationType.IN_PERSON, False


def is_likely_sit(title: str, description: str = "") -> tuple[bool, bool]:
    """
    Heuristic sit detection. Returns (is_sit, certain).
    certain=False when no keywords matched at all (LLM should confirm).

    Note: EXCLUDE_KEYWORDS are checked against title only, not description.
    Descriptions often contain HTML/WordPress shortcodes with words like "class"
    that would cause false negatives if we searched the full text.
    SIT_KEYWORDS are checked against title + description to maximize recall.
    """
    full_text = (title + " " + description).lower()
    title_lower = title.lower()
    has_sit = any(kw in full_text for kw in SIT_KEYWORDS)
    has_exclude = any(kw in title_lower for kw in EXCLUDE_KEYWORDS)
    if has_exclude:
        return False, True
    if has_sit:
        return True, True
    return True, False  # no signal — optimistically include, but uncertain
