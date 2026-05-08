"""
Minneapolis/Saint Paul, MN meditation center sources — Phase 3 expansion.

Primary source: Common Ground Meditation Center via Sanity CMS public API.
Recurring sits (no accessible iCal):
  - Minnesota Zen Meditation Center — Squarespace, no iCal
  - Clouds in Water Zen — Squarespace, no iCal
  - Shambhala Minneapolis — Cloudflare-blocked WordPress, no iCal
"""

import hashlib
import logging
from datetime import datetime, timedelta, timezone
from typing import Optional
from urllib.parse import quote

import httpx

from data.schemas.event import Center, Event, LocationType, SourceType, Tradition
from ingestion.utils import is_likely_sit

log = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
}

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "common_ground": Center(
        id="common_ground",
        name="Common Ground Meditation Center",
        url="https://commongroundmeditation.org",
        address="2700 East 26th Street",
        city="Minneapolis",
        state="MN",
        zip_code="55406",
        lat=44.9620,
        lng=-93.2305,
        neighborhood="Seward / Longfellow",
        tradition=Tradition.THERAVADA,
        notes=(
            "Common Ground Meditation Center is Minneapolis's premier Insight / Vipassana "
            "meditation center, offering a wide range of programs in the IMS / Spirit Rock "
            "tradition. Located at 2700 East 26th Street in the Seward neighborhood. "
            "Programs include daily Open Meditation (7am, various teachers), weekly practice "
            "groups with senior teachers Mark Nunberg and Shelly Graf, community groups, "
            "daylong and residential retreats, and courses for all levels. "
            "Free and by-donation options available. A welcoming, accessible practice home."
        ),
    ),
    "mn_zen": Center(
        id="mn_zen",
        name="Minnesota Zen Meditation Center",
        url="https://mnzencenter.org",
        address="3343 East Bde Maka Ska Pkwy",
        city="Minneapolis",
        state="MN",
        zip_code="55408",
        lat=44.9434,
        lng=-93.3173,
        neighborhood="Lakewood / Bde Maka Ska",
        tradition=Tradition.ZEN,
        notes=(
            "Minnesota Zen Meditation Center (MZMC) is a Soto Zen center in the Dainin "
            "Katagiri Roshi lineage, founded in 1972. Located on the west shore of "
            "Bde Maka Ska (Lake Calhoun). Regular programs: morning zazen Mon–Fri 6:30am, "
            "Sat–Sun 7:30am; evening zazen Mon–Thu 5:30pm, Fri 6pm; Wednesday dharma talks "
            "7:30pm; Sunday Morning Program 9:30am (zazen + service + dharma talk). "
            "Sesshin, workshops, and study programs offered. Resident teacher: Myo Denis Lahey. "
            "Website: mnzencenter.org (Squarespace — no iCal feed available)."
        ),
    ),
    "clouds_in_water": Center(
        id="clouds_in_water",
        name="Clouds in Water Zen Center",
        url="https://cloudsinwater.org",
        address="308 Prince St",
        city="Saint Paul",
        state="MN",
        zip_code="55107",
        lat=44.9397,
        lng=-93.0961,
        neighborhood="Lowertown / Saint Paul",
        tradition=Tradition.ZEN,
        notes=(
            "Clouds in Water Zen Center is a Soto Zen center in Lowertown, Saint Paul, "
            "founded by Roshi Diane Musho Hamilton (now teacher emerita) and led by "
            "Abbot Dokai Georgesen. Regular practice: Monday 7–8:30am zazen (in-person + Zoom), "
            "Tuesday 7–8:30am zazen, Wednesday 7–8:30am zazen + dharma study, "
            "Thursday 7–8:30am zazen, Friday 7–8:30am zazen. "
            "Sunday morning 9:30am zazen + dharma talk. Drop-in welcome, registration recommended."
            "Website: cloudsinwater.org (Squarespace — no iCal feed available)."
        ),
    ),
    "shambhala_minneapolis": Center(
        id="shambhala_minneapolis",
        name="Shambhala Meditation Center of Minneapolis",
        url="https://minneapolis.shambhala.org",
        address="1544 Nicollet Ave",
        city="Minneapolis",
        state="MN",
        zip_code="55403",
        lat=44.9657,
        lng=-93.2896,
        neighborhood="Whittier / Minneapolis",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Center of Minneapolis (Chögyam Trungpa lineage) in the "
            "Whittier neighborhood. Regular programs include Shambhala Training weekends, "
            "weekly community meditation evenings, and open houses. "
            "Website: minneapolis.shambhala.org (Cloudflare-protected — no direct iCal access)."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Common Ground — Sanity CMS public API scraper
#
# Common Ground's website (commongroundmeditation.org) is built on Next.js
# with a Sanity CMS backend. The Sanity public API is accessible without
# authentication at: https://4tyz2xuc.apicdn.sanity.io/
#
# Events schema:
#   _type: 'event'
#   startDate/endDate: "YYYY-MM-DD"
#   startTime/endTime: "HH:MM"
#   realm: ["in-person", "online"]    (array)
#   venues: ["cityCenter", ...]        (array of string slugs)
#   eventTemplate->: {title, descriptionShort, programtype}
#
# "cityCenter" venue = 2700 East 26th Street, Minneapolis MN 55406
# ---------------------------------------------------------------------------

SANITY_PROJECT_ID = "4tyz2xuc"
SANITY_DATASET = "production"
SANITY_API_VERSION = "2023-10-02"

# Title keywords that disqualify as a sit (non-meditation events)
_NON_SIT_KEYWORDS = (
    "cleaning",
    "maintenance",
    "garden",
    "work day",
    "work practice",
    "yoga",
    "qigong",
    "tai chi",
    "children",
    "teen",
    "pre-teen",
    "youth",
    "affinity group",
    "book club",
    "interview",
    "board",
    "volunteer",
)


def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _is_sit_title(title: str) -> bool:
    """Quick keyword check for obvious non-sit events."""
    tl = title.lower()
    if any(kw in tl for kw in _NON_SIT_KEYWORDS):
        return False
    return True


def fetch_common_ground(window_days: int = 90) -> list[Event]:
    """
    Fetch events from Common Ground Meditation Center via Sanity public API.

    Queries the GROQ API for events in the next window_days days, resolving
    eventTemplate references to get titles and descriptions. Filters to sits.
    """
    today = datetime.now().date()
    end_date = today + timedelta(days=window_days)

    groq = (
        f"*[_type == 'event' && startDate >= '{today.isoformat()}' "
        f"&& startDate <= '{end_date.isoformat()}']"
        "{startDate,startTime,endDate,endTime,realm,venues,zoomLink,"
        "eventTemplate->{title,descriptionShort,programtype}}"
    )
    url = (
        f"https://{SANITY_PROJECT_ID}.apicdn.sanity.io/v{SANITY_API_VERSION}"
        f"/data/query/{SANITY_DATASET}?query={quote(groq)}"
    )

    log.info(f"Common Ground: fetching events from Sanity API ({window_days}-day window)...")
    try:
        resp = httpx.get(url, headers=HEADERS, follow_redirects=True, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        log.error(f"Common Ground: Sanity API error: {e}")
        return []

    raw_events = data.get("result", [])
    log.info(f"Common Ground: {len(raw_events)} raw events from Sanity")

    center = CENTERS["common_ground"]
    today_str = datetime.now(timezone.utc).date().isoformat()
    events: list[Event] = []

    for item in raw_events:
        tmpl = item.get("eventTemplate") or {}
        title = (tmpl.get("title") or "").strip()
        if not title:
            continue

        # Quick filter: skip obvious non-sits
        if not _is_sit_title(title):
            continue

        # Start/end times
        start_date = item.get("startDate", "")
        start_time = item.get("startTime", "")
        end_date_str = item.get("endDate", "")
        end_time = item.get("endTime", "")

        if not start_date:
            continue

        start_str = f"{start_date}T{start_time}:00" if start_time else f"{start_date}T00:00:00"
        end_str = (
            f"{end_date_str}T{end_time}:00"
            if end_date_str and end_time
            else None
        )

        # Location type from realm field
        realm = item.get("realm") or []
        has_online = "online" in realm
        has_inperson = "in-person" in realm

        if has_inperson and has_online:
            loc_type = LocationType.HYBRID
        elif has_online:
            loc_type = LocationType.ONLINE
        else:
            loc_type = LocationType.IN_PERSON

        # Description
        description = (tmpl.get("descriptionShort") or "").strip()
        zoom_link = item.get("zoomLink")
        if zoom_link and has_online:
            description = f"{description}\nZoom: {zoom_link}".strip()

        # Sit check
        sit_result, sit_certain = is_likely_sit(title, description)
        if not sit_result and sit_certain:
            continue  # definitely not a sit

        events.append(Event(
            id=_event_id("common_ground", title, start_str),
            org_id="common_ground",
            org_name=center.name,
            title=title,
            start_time=start_str,
            end_time=end_str,
            address=center.address,
            city=center.city,
            state=center.state,
            neighborhood=center.neighborhood,
            lat=center.lat,
            lng=center.lng,
            tradition=center.tradition,
            location_type=loc_type,
            is_sit=sit_result,
            source=SourceType.STATIC_HTML,
            source_url="https://commongroundmeditation.org/calendar",
            event_url="https://commongroundmeditation.org/calendar",
            last_verified=today_str,
            notes=description[:300] if description else None,
        ))

    log.info(f"Common Ground: {len(events)} events after filtering")
    return events
