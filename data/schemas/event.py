"""
Canonical event schema for Sangha Calendar.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class Tradition(str, Enum):
    THERAVADA = "theravada"
    ZEN = "zen"
    TIBETAN = "tibetan"
    SECULAR = "secular"
    PLURALIST = "pluralist"
    OTHER = "other"
    UNKNOWN = "unknown"


class SourceType(str, Enum):
    ICAL_FEED = "ical_feed"
    EVENTBRITE = "eventbrite"
    WORDPRESS = "wordpress"
    SQUARESPACE = "squarespace"
    STATIC_HTML = "static_html"
    MANUAL = "manual"


@dataclass
class Center:
    """A meditation center or organization."""
    id: str                          # slug, e.g. "ebmc"
    name: str                        # "East Bay Meditation Center"
    url: str
    address: str
    city: str
    state: str
    zip_code: str
    lat: Optional[float] = None
    lng: Optional[float] = None
    neighborhood: Optional[str] = None
    tradition: Tradition = Tradition.UNKNOWN
    notes: Optional[str] = None


@dataclass
class Event:
    """A single meditation sit event."""
    id: str                          # stable hash of org+title+time
    org_id: str                      # references Center.id
    org_name: str
    title: str

    # Time — store as ISO strings for serialization simplicity
    start_time: str                  # e.g. "2026-04-28T07:00:00"
    end_time: Optional[str] = None

    # Location
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    neighborhood: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None

    # Classification
    tradition: Tradition = Tradition.UNKNOWN
    is_sit: bool = True              # confirmed as a meditation sit (not a talk/workshop)
    accessibility_notes: Optional[str] = None
    identity_focus: Optional[str] = None   # e.g. "BIPOC", "LGBTQ+", "women"

    # Source
    source: SourceType = SourceType.MANUAL
    source_url: Optional[str] = None
    event_url: Optional[str] = None
    last_verified: Optional[str] = None   # ISO date

    # Recurrence (if extracted from iCal RRULE or page text)
    recurrence: Optional[str] = None  # e.g. "weekly", "monthly", raw RRULE

    notes: Optional[str] = None
