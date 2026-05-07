"""
Seattle meditation center sources — Phase 3 Seattle expansion.
Defines known Seattle-area centers and their ingestion strategies.

iCal feeds:
  - Seattle Insight Meditation Society (seattleinsight.org/events/?ical=1)
  - KMC Washington / Kadampa Seattle (meditateinseattle.org/events/?ical=1)

Custom scrapers:
  - Nalandabodhi Seattle (nalandabodhi.org/?ical=1, filtered to Seattle location)

Recurring sits (seeded separately):
  - Shambhala Seattle — Thu 7pm, Sun 10am in-person; Mon 6:30pm online; Wed 7pm hybrid
  - Seattle Buddhist Center (Triratna) — Thu 7pm, Sun 6pm in-person
"""

import hashlib
import logging
from datetime import datetime, timezone

import httpx
from icalendar import Calendar

from data.schemas.event import Center, Event, LocationType, SourceType, Tradition
from ingestion.feeds.ical_feed import fetch_feed
from ingestion.utils import detect_location_type, is_likely_sit

log = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "seattle_insight": Center(
        id="seattle_insight",
        name="Seattle Insight Meditation Society",
        url="https://seattleinsight.org",
        address="4001 9th Ave NE",
        city="Seattle",
        state="WA",
        zip_code="98105",
        lat=47.6568,
        lng=-122.3142,
        neighborhood="University District",
        tradition=Tradition.THERAVADA,
        notes=(
            "Seattle Insight Meditation Society (SIMS) is the primary Vipassana / Insight "
            "center in Seattle, teaching in the Theravada tradition (IMS / Spirit Rock lineage). "
            "Weekly programs: Monday Evening Meditation & Dharma Talk, Stillpoint Sit, Thursday "
            "Guided Meditation and Thursday Night Sangha (in-person), Sunday Morning Sit & Dharma "
            "Talk (hybrid). LGBTQIA+ Sangha and other identity affinity groups offered. "
            "Drop-in welcome. By donation."
        ),
    ),
    "kmc_washington": Center(
        id="kmc_washington",
        name="Kadampa Meditation Center Washington",
        url="https://meditateinseattle.org",
        address="6556 24th Ave NW",
        city="Seattle",
        state="WA",
        zip_code="98117",
        lat=47.6830,
        lng=-122.3871,
        neighborhood="Crown Hill",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Washington (KMC Washington) offers Tibetan Buddhist "
            "meditation classes in the New Kadampa Tradition (NKT-IKBU) founded by Geshe "
            "Kelsang Gyatso. Drop-in classes include Thursday Evening Meditation 7pm, Sunday "
            "Morning classes 10am, Monday Evening classes 7pm, and morning prostrations "
            "on weekdays. Spanish-language Sunday class also offered. Beginners welcome."
        ),
    ),
    "nalandabodhi_seattle": Center(
        id="nalandabodhi_seattle",
        name="Nalandabodhi Seattle (Nalanda West)",
        url="https://nalandabodhi.org",
        address="3902 Woodland Park Ave N",
        city="Seattle",
        state="WA",
        zip_code="98103",
        lat=47.6574,
        lng=-122.3363,
        neighborhood="Fremont",
        tradition=Tradition.TIBETAN,
        notes=(
            "Nalandabodhi Seattle operates out of Nalanda West in Seattle's Fremont neighborhood, "
            "home of Dzogchen Ponlop Rinpoche's North American headquarters. Offers weekly open "
            "meditation practice: Thursday Evening Open Meditation 6pm and Sunday Open Meditation "
            "10am (both in-person at Nalanda West). Tibetan Buddhist — Kagyu/Nyingma Dzogchen "
            "lineage. Kum Nye (Tibetan Yoga) also offered Tuesdays 5pm. Free, all welcome."
        ),
    ),
    "shambhala_seattle": Center(
        id="shambhala_seattle",
        name="Shambhala Meditation Center of Seattle",
        url="https://seattle.shambhala.org",
        address="3107 E Harrison St",
        city="Seattle",
        state="WA",
        zip_code="98112",
        lat=47.6197,
        lng=-122.3023,
        neighborhood="Capitol Hill",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Buddhist meditation center (Chögyam Trungpa lineage) in Seattle's "
            "Capitol Hill neighborhood. Regular public programs: Thursday Evening Open House "
            "7–8:30pm (in-person, all welcome), Sunday Morning Open House 10–11:30am (in-person), "
            "Monday Shambhala Practice Night 6:30pm (online), Wednesday Heart of Recovery 7pm "
            "(hybrid). Queer Dharma group monthly. Free introductory meditation instruction available."
        ),
    ),
    "seattle_buddhist_center": Center(
        id="seattle_buddhist_center",
        name="Seattle Buddhist Center",
        url="https://seattlebuddhistcenter.org",
        address="12056 15th Ave NE, Suite C-2",
        city="Seattle",
        state="WA",
        zip_code="98125",
        lat=47.7203,
        lng=-122.3145,
        neighborhood="Northgate / Pinehurst",
        tradition=Tradition.PLURALIST,
        notes=(
            "Seattle Buddhist Center is part of the Triratna Buddhist Community (formerly FWBO), "
            "an international network emphasizing meditation, friendship, and ethical engagement. "
            "Weekly drop-in programs: Thursday Night Meditation 7–8pm (in-person), Sunday Sangha "
            "Night 6–8pm (in-person with dharma discussion and meditation). Recovery Dharma "
            "Fridays 7pm. Beginners welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds — standard The Events Calendar WordPress feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "seattle_insight": {
        "url": "https://seattleinsight.org/events/?ical=1",
        "filter_to_sits": True,
    },
    "kmc_washington": {
        "url": "https://meditateinseattle.org/events/?ical=1",
        "filter_to_sits": True,
    },
}


def _event_id(org_id: str, title: str, start: str) -> str:
    raw = f"{org_id}:{title}:{start}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def fetch_nalandabodhi_seattle() -> list[Event]:
    """
    Fetch Nalandabodhi's global iCal feed and filter to Seattle-only events
    (LOCATION contains 'Nalandabodhi Seattle' or 'Nalanda West').
    """
    url = "https://nalandabodhi.org/?ical=1"
    center = CENTERS["nalandabodhi_seattle"]

    resp = httpx.get(url, headers=HEADERS, follow_redirects=True, timeout=20)
    resp.raise_for_status()

    cal = Calendar.from_ical(resp.content)
    events: list[Event] = []

    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        raw_location = str(component.get("LOCATION", "")).strip()

        # Only keep Seattle events
        loc_lower = raw_location.lower()
        if "nalandabodhi seattle" not in loc_lower and "nalanda west" not in loc_lower:
            continue

        title = str(component.get("SUMMARY", "")).strip()
        description = str(component.get("DESCRIPTION", "")).strip()
        dtstart = component.get("DTSTART")
        dtend = component.get("DTEND")
        event_url = str(component.get("URL", "")) or None

        if not dtstart or not title:
            continue

        def _to_utc_iso(dt_val) -> str:
            if hasattr(dt_val, "tzinfo") and dt_val.tzinfo is not None:
                return dt_val.astimezone(timezone.utc).isoformat()
            return dt_val.isoformat() if hasattr(dt_val, "isoformat") else str(dt_val)

        start_str = _to_utc_iso(dtstart.dt)
        end_str = _to_utc_iso(dtend.dt) if dtend else None

        sit_result, sit_certain = is_likely_sit(title, description)
        if not sit_result and sit_certain:
            continue

        loc_type, _ = detect_location_type(title, description, raw_location, event_url or "")

        events.append(Event(
            id=_event_id("nalandabodhi_seattle", title, start_str),
            org_id="nalandabodhi_seattle",
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
            is_sit=sit_result if sit_certain else True,
            source=SourceType.ICAL_FEED,
            source_url=url,
            event_url=event_url,
            last_verified=datetime.now(timezone.utc).date().isoformat(),
            notes=description[:300] if description else None,
        ))

    return events


def run_seattle_ical() -> list[Event]:
    """Fetch Seattle iCal feeds (Seattle Insight + KMC Washington)."""
    all_events: list[Event] = []

    for org_id, feed_cfg in ICAL_FEEDS.items():
        center = CENTERS[org_id]
        log.info(f"Fetching {center.name} (Seattle iCal)...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=org_id,
                org_name=center.name,
                tradition=center.tradition,
                filter_to_sits=feed_cfg.get("filter_to_sits", True),
                address=center.address,
                city=center.city,
                state=center.state,
                neighborhood=center.neighborhood,
                lat=center.lat,
                lng=center.lng,
            )
            log.info(f"  → {len(events)} sits found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Seattle iCal {org_id} failed: {e}")

    return all_events
