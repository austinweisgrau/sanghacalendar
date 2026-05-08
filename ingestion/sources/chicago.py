"""
Chicago meditation center sources — Phase 3 Chicago expansion.

Primary source: Sit Around Chicago Tockify aggregator calendar
(https://www.sitaroundchicago.org) — community-maintained iCal covering
10+ Chicago-area Buddhist centers in a single feed.

The Tockify feed uses SUMMARY format: "CenterName: Event Title"
and LOCATION with full addresses. We parse both to extract per-center
org_id, tradition, city, and address.
"""

import hashlib
import logging
import re
from datetime import datetime, timezone
from typing import Optional

import httpx
from icalendar import Calendar

from data.schemas.event import Center, Event, LocationType, SourceType, Tradition
from ingestion.utils import detect_location_type, is_likely_sit
from ingestion.llm_classifier import classify_event

log = logging.getLogger(__name__)

TOCKIFY_CHICAGO_URL = "https://tockify.com/api/feeds/ics/sitaroundchicagocalendar"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
}

# ---------------------------------------------------------------------------
# Center registry — for bio pages and coordinator use
# ---------------------------------------------------------------------------

CENTERS = {
    "ancient_dragon_chicago": Center(
        id="ancient_dragon_chicago",
        name="Ancient Dragon Zen Gate",
        url="https://www.ancientdragon.org",
        address="2255 W Giddings St",
        city="Chicago",
        state="IL",
        zip_code="60625",
        lat=41.9680,
        lng=-87.6840,
        neighborhood="Ravenswood",
        tradition=Tradition.ZEN,
        notes=(
            "Soto Zen center in Chicago's Ravenswood neighborhood, affiliated with "
            "San Francisco Zen Center (Shunryu Suzuki lineage). Sunday morning zazen "
            "9:30am, Monday evening zazen at The Cenacle in Lincoln Park. Online "
            "morning zazen sessions daily via Zoom. Free, all welcome."
        ),
    ),
    "daiyuzenji_chicago": Center(
        id="daiyuzenji_chicago",
        name="Daiyuzenji Rinzai Zen Temple",
        url="https://daiyuzenji.org",
        address="3717 N Ravenswood Ave #112",
        city="Chicago",
        state="IL",
        zip_code="60613",
        lat=41.9457,
        lng=-87.6776,
        neighborhood="Ravenswood",
        tradition=Tradition.ZEN,
        notes=(
            "Rinzai Zen temple in Ravenswood. Hybrid public sittings: Tuesday & Thursday "
            "evenings 7–9pm (two zazen periods), Friday mornings 5:30–6:15am (in-person), "
            "Sunday mornings 8:30–10:30am (hybrid, RSVP for Zoom). Traditional Rinzai "
            "practice in the koan and shikantaza style."
        ),
    ),
    "zbtc_evanston": Center(
        id="zbtc_evanston",
        name="Zen Buddhist Temple of Chicago",
        url="https://www.zbtc.org",
        address="608 Dempster St",
        city="Evanston",
        state="IL",
        zip_code="60202",
        lat=42.0451,
        lng=-87.6905,
        neighborhood="Evanston",
        tradition=Tradition.ZEN,
        notes=(
            "The oldest continuously operating Zen center in the Chicago area, founded "
            "1949 by Soyu Matsuoka Roshi. Soto Zen services Sundays 10am–12pm and "
            "2–4pm, and Wednesdays 7–9pm. In-person and online."
        ),
    ),
    "shambhala_chicago": Center(
        id="shambhala_chicago",
        name="Shambhala Meditation Center of Chicago",
        url="https://chicago.shambhala.org",
        address="37 N Carpenter St",
        city="Chicago",
        state="IL",
        zip_code="60607",
        lat=41.8826,
        lng=-87.6524,
        neighborhood="West Loop",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Buddhist meditation center (Chögyam Trungpa lineage) in the "
            "West Loop. Sunday mornings 9:30–11am, Tuesday evenings 7–8:30pm, and "
            "Sunday evenings 5:30–7:30pm Queer Dharma group. Free introductory "
            "meditation instruction available. Calendar at chicago.shambhala.org."
        ),
    ),
    "cbmg_chicago": Center(
        id="cbmg_chicago",
        name="Chicago Buddhist Meditation Group",
        url="https://chicagomeditation.org",
        address="4512 N Lincoln Ave",
        city="Chicago",
        state="IL",
        zip_code="60625",
        lat=41.9629,
        lng=-87.6822,
        neighborhood="Ravenswood",
        tradition=Tradition.PLURALIST,
        notes=(
            "Non-sectarian meditation community meeting weekly on Sundays at 3:30pm CT "
            "at 4512 N Lincoln Ave (Ravenswood). Hybrid in-person and Zoom. Guided "
            "meditation, dharma sharing, and discussion. Free, beginners welcome."
        ),
    ),
    "zen_chicago": Center(
        id="zen_chicago",
        name="Chicago Zen Meditation Community",
        url="https://zenchicago.org",
        address="1460 W Chicago Ave",
        city="Chicago",
        state="IL",
        zip_code="60642",
        lat=41.8962,
        lng=-87.6686,
        neighborhood="West Town",
        tradition=Tradition.ZEN,
        notes=(
            "Soto Zen center in West Town with an extensive hybrid schedule: weekday "
            "morning zazen Mon–Sat 8:30am, Monday afternoons 1:15pm, Monday and "
            "Wednesday evenings, Saturday morning zazen and last-Saturday zazenkai. "
            "Zoom links available for most sessions."
        ),
    ),
    "insight_chicago": Center(
        id="insight_chicago",
        name="Insight Chicago Meditation Community",
        url="https://www.insightchicago.org",
        address="",
        city="Chicago",
        state="IL",
        zip_code="",
        lat=41.8781,
        lng=-87.6298,
        neighborhood="Various locations",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight / Vipassana meditation community with multiple sanghas across "
            "Chicago: Sunday Night Meditation Sangha, Northside Meditation Sangha "
            "(Wednesdays), Evanston Sangha (Mon/Thu), and more. Teachers in the "
            "IMS / Spirit Rock lineage. Regular daylong retreats."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Tockify center-name → (org_id, tradition) mapping
# ---------------------------------------------------------------------------

# Maps the prefix in "CenterName: Event Title" SUMMARY to our org_id + tradition.
# Centers not in this map get a slug-derived org_id and UNKNOWN tradition.
TOCKIFY_CENTER_MAP: dict[str, tuple[str, Tradition]] = {
    "Ancient Dragon Zen Gate":           ("ancient_dragon_chicago", Tradition.ZEN),
    "Daiyuzenji Rinzai Zen Temple":      ("daiyuzenji_chicago",     Tradition.ZEN),
    "Zen Buddhist Temple of Chicago":    ("zbtc_evanston",          Tradition.ZEN),
    "Shambhala Chicago":                 ("shambhala_chicago",      Tradition.TIBETAN),
    "Chicago Buddhist Meditation Group": ("cbmg_chicago",           Tradition.PLURALIST),
    "Chicago Zen Meditation Community":  ("zen_chicago",            Tradition.ZEN),
    "Insight Chicago Meditation Community": ("insight_chicago",     Tradition.THERAVADA),
    "Bultasa Buddhist Temple":           ("bultasa_chicago",        Tradition.ZEN),
    "Bultasa Zen Group":                 ("bultasa_chicago",        Tradition.ZEN),
    "Chicago Karma Thegsum Choling":     ("ktc_chicago",            Tradition.TIBETAN),
    "Dharma Drum Mountain":              ("dharma_drum_chicago",    Tradition.ZEN),
    "Diamond Way Buddhist Center Chicago": ("diamond_way_chicago",  Tradition.TIBETAN),
    "Great Plains Zen Center":           ("great_plains_zen",       Tradition.ZEN),
    "Bodhi Path":                        ("bodhi_path_chicago",     Tradition.TIBETAN),
    "Chan/ Zen at Rockefeller Chapel":   ("rockefeller_chan",       Tradition.ZEN),
    "The Buddhist Temple of Chicago":    ("buddhist_temple_chicago",Tradition.OTHER),
    "Buddhist Peace Fellowship Chicago": ("bpf_chicago",            Tradition.PLURALIST),
}


# ---------------------------------------------------------------------------
# Kadampa Chicago — Eventbrite (not in Tockify aggregator)
# ---------------------------------------------------------------------------

CENTERS_EXTRA = {
    "kadampa_chicago": Center(
        id="kadampa_chicago",
        name="Kadampa Meditation Center Chicago",
        url="https://meditateinchicago.org",
        address="1507 E 53rd St",
        city="Chicago",
        state="IL",
        zip_code="60615",
        lat=41.7993,
        lng=-87.5912,
        neighborhood="Hyde Park",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Chicago (NKT tradition) in Hyde Park. Offers weekly "
            "drop-in classes, guided meditations, and retreats drawing on Geshe Kelsang Gyatso's "
            "teachings. Main location at 1507 E 53rd St; events listed on Eventbrite."
        ),
    ),
}

EVENTBRITE_FEEDS = {
    "kadampa_chicago": {
        "organizer_id": "32772634747",
        "filter_to_sits": False,  # include classes, retreats, special programs
    },
}


def _slug(name: str) -> str:
    """Convert center name to a stable org_id slug."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:40]


def _parse_location(raw: str) -> tuple[Optional[str], Optional[str], Optional[str], bool]:
    """
    Parse a Tockify LOCATION field into (address, city, state, is_online).

    Tockify LOCATION examples:
      "608 Dempster St, Evanston, IL 60202, USA"
      "ADZG Online Zendo"
      "Online (zoom)"
      "https://chicago.shambhala.org/..."
    Returns (address, city, state, is_online).
    """
    loc = raw.replace("\\,", ",").strip()

    # Online detection
    online_keywords = ("online", "zoom", "http://", "https://", "facebook")
    if any(kw in loc.lower() for kw in online_keywords):
        return None, None, None, True

    # Try structured address parse: "Street, City, ST ZIPCODE, USA"
    parts = [p.strip() for p in loc.split(",")]
    if len(parts) >= 3:
        # Find the part matching "ST 12345" or "ST"
        state_idx = None
        for i, part in enumerate(parts):
            m = re.match(r"^([A-Z]{2})\s*\d{0,5}$", part.strip())
            if m:
                state_idx = i
                break
        if state_idx is not None and state_idx >= 2:
            city = parts[state_idx - 1].strip()
            state = parts[state_idx].strip()[:2]
            address = ", ".join(parts[:state_idx - 1]).strip()
            return address or None, city or None, state or None, False

    # Fallback: return raw as address, no city
    return loc[:200] if loc else None, None, "IL", False


def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def fetch_tockify_chicago() -> list[Event]:
    """
    Fetch the Sit Around Chicago Tockify aggregator iCal feed and return
    normalized Event objects, one per sit.

    SUMMARY format: "CenterName: Event Title" — we split on first ": "
    to extract center name and event title separately.
    """
    resp = httpx.get(TOCKIFY_CHICAGO_URL, headers=HEADERS, follow_redirects=True, timeout=20)
    resp.raise_for_status()

    # Fix Tockify's malformed duration values "P15M" (should be "PT15M" for minutes).
    # Newer icalendar versions are strict about ISO 8601 duration format.
    raw_ical = resp.content
    raw_ical = raw_ical.replace(b"REFRESH-INTERVAL:P15M", b"REFRESH-INTERVAL:PT15M")
    raw_ical = raw_ical.replace(b"X-PUBLISHED-TTL:P15M", b"X-PUBLISHED-TTL:PT15M")
    cal = Calendar.from_ical(raw_ical)
    events: list[Event] = []

    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        raw_summary = str(component.get("SUMMARY", "")).strip()
        description = str(component.get("DESCRIPTION", "")).strip()
        raw_location = str(component.get("LOCATION", "")).strip()
        dtstart = component.get("DTSTART")
        dtend = component.get("DTEND")
        event_url = str(component.get("URL", "")) or None

        if not dtstart:
            continue

        # Split "CenterName: Event Title" on first ": "
        if ": " in raw_summary:
            center_name, title = raw_summary.split(": ", 1)
            center_name = center_name.strip()
            title = title.strip()
        else:
            center_name = "Sit Around Chicago"
            title = raw_summary

        # Resolve org_id and tradition
        if center_name in TOCKIFY_CENTER_MAP:
            org_id, tradition = TOCKIFY_CENTER_MAP[center_name]
        else:
            org_id = _slug(center_name)
            tradition = Tradition.UNKNOWN

        # Normalize timestamps to UTC ISO
        def _to_utc_iso(dt_val) -> str:
            if hasattr(dt_val, "tzinfo") and dt_val.tzinfo is not None:
                return dt_val.astimezone(timezone.utc).isoformat()
            return dt_val.isoformat() if hasattr(dt_val, "isoformat") else str(dt_val)

        start_str = _to_utc_iso(dtstart.dt)
        end_str = _to_utc_iso(dtend.dt) if dtend else None

        # Parse location
        address, city, state, is_online = _parse_location(raw_location)
        if city is None:
            city = "Chicago"
        if state is None:
            state = "IL"

        # Sit classification
        sit_result, sit_certain = is_likely_sit(title, description)
        if not sit_certain and not sit_result:
            continue  # definitively not a sit

        # Location classification
        if is_online:
            loc_type = LocationType.ONLINE
            loc_certain = True
        else:
            loc_type, loc_certain = detect_location_type(title, description, raw_location, event_url or "")

        # LLM fallback for uncertain cases
        if not sit_certain or not loc_certain:
            llm = classify_event(title, description, raw_location, event_url or "")
            if llm:
                if not loc_certain:
                    loc_type = LocationType(llm["location_type"])
                if not sit_certain:
                    sit_result = llm["is_sit"]

        if not sit_result:
            continue

        events.append(Event(
            id=_event_id(org_id, title, start_str),
            org_id=org_id,
            org_name=center_name,
            title=title,
            start_time=start_str,
            end_time=end_str,
            address=address,
            city=city,
            state=state,
            neighborhood=None,
            lat=None,
            lng=None,
            tradition=tradition,
            location_type=loc_type,
            is_sit=sit_result,
            source=SourceType.ICAL_FEED,
            source_url=TOCKIFY_CHICAGO_URL,
            event_url=event_url,
            last_verified=datetime.now(timezone.utc).date().isoformat(),
            notes=description[:300] if description else None,
        ))

    return events
