"""
Ingestion coordinator — orchestrates the scraper agent swarm.

For each source:
1. Determine scrape strategy (iCal / Eventbrite / WP / static)
2. Dispatch to appropriate scraper
3. Classify events (is_sit filter)
4. Normalize to canonical schema
5. Upsert to event store

Can be run on a schedule (monthly) with Abraxis in the loop for
LLM-assisted classification of ambiguous events.
"""

import logging

from data.schemas.event import Event
from data.store import dedup_events, init_db, upsert_events
from ingestion.feeds.ical_feed import fetch_feed
from ingestion.scrapers.eventbrite import fetch_eventbrite_organizer
from ingestion.scrapers.static_html import fetch_static_html_calendar

from ingestion.sources.east_bay import CENTERS, EVENTBRITE_FEEDS, ICAL_FEEDS, STATIC_HTML_FEEDS
from ingestion.sources import nyc as nyc_sources
from ingestion.sources.nyc import fetch_shambhala_nyc, fetch_zenstudies_nyc
from ingestion.sources import la as la_sources
from ingestion.sources.la import fetch_insightla
from ingestion.sources import boston as boston_sources
from ingestion.sources import dc as dc_sources
from ingestion.sources.dc import fetch_imcw
from ingestion.sources import chicago as chicago_sources
from ingestion.sources.chicago import fetch_tockify_chicago
from ingestion.sources import seattle as seattle_sources
from ingestion.sources.seattle import fetch_nalandabodhi_seattle, run_seattle_ical
from ingestion.sources import denver as denver_sources
from ingestion.sources import portland as portland_sources
from ingestion.sources import austin as austin_sources

log = logging.getLogger(__name__)


def run_east_bay_phase1() -> list[Event]:
    """Phase 1: subscribe to known iCal feeds, filter to sits."""
    all_events: list[Event] = []

    for org_id, feed_cfg in ICAL_FEEDS.items():
        center = CENTERS[org_id]
        log.info(f"Fetching {center.name}...")
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
            log.error(f"  ✗ Failed: {e}")

    return all_events


def run_east_bay_phase2() -> list[Event]:
    """Phase 2: Eventbrite scrapers for non-iCal centers."""
    all_events: list[Event] = []

    for org_id, feed_cfg in EVENTBRITE_FEEDS.items():
        center = CENTERS[org_id]
        log.info(f"Fetching {center.name} (Eventbrite)...")
        try:
            events = fetch_eventbrite_organizer(
                organizer_id=feed_cfg["organizer_id"],
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
            log.info(f"  → {len(events)} events found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Failed: {e}")

    return all_events


def run_east_bay_phase2b() -> list[Event]:
    """Phase 2b: LLM-assisted static HTML scrapers for centers without structured feeds."""
    all_events: list[Event] = []

    for org_id, feed_cfg in STATIC_HTML_FEEDS.items():
        center = CENTERS[org_id]
        log.info(f"Fetching {center.name} (static HTML)...")
        try:
            events = fetch_static_html_calendar(
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
            log.info(f"  → {len(events)} events found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Failed: {e}")

    return all_events


def run_nyc_phase3a() -> list[Event]:
    """Phase 3a: NYC — direct iCal subscribe for three confirmed easy feeds."""
    all_events: list[Event] = []

    for org_id, feed_cfg in nyc_sources.ICAL_FEEDS.items():
        center = nyc_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (NYC)...")
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
            log.error(f"  ✗ Failed: {e}")

    return all_events


def run_nyc_phase3b() -> list[Event]:
    """Phase 3b: NYC — Shambhala NYC scraper + Tibet House Eventbrite."""
    all_events: list[Event] = []

    # Shambhala NYC — parse eventsDatas JSON from calendar page
    try:
        events = fetch_shambhala_nyc()
        log.info(f"  Shambhala NYC → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Shambhala NYC failed: {e}")

    # Tibet House US — Eventbrite
    for org_id, feed_cfg in nyc_sources.EVENTBRITE_FEEDS.items():
        center = nyc_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Eventbrite NYC)...")
        try:
            events = fetch_eventbrite_organizer(
                organizer_id=feed_cfg["organizer_id"],
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
            log.info(f"  → {len(events)} events found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Failed: {e}")

    return all_events


def run_nyc_phase3c() -> list[Event]:
    """Phase 3c: NYC — Zen Studies Society iCal + ZCNYC static HTML."""
    all_events: list[Event] = []

    # Zen Studies Society / NY Zendo Shobo-Ji — iCal with prefix stripping
    try:
        events = fetch_zenstudies_nyc()
        log.info(f"  NY Zendo Shobo-Ji → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ NY Zendo Shobo-Ji failed: {e}")

    # ZCNYC / Fire Lotus Temple — LLM-assisted static HTML
    for org_id, feed_cfg in nyc_sources.STATIC_HTML_FEEDS.items():
        center = nyc_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (NYC static HTML)...")
        try:
            events = fetch_static_html_calendar(
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
            log.info(f"  → {len(events)} events found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Failed: {e}")

    return all_events


def run_la_phase3() -> list[Event]:
    """Phase 3 LA: InsightLA schema.org scraper + Shambhala LA iCal + ZCLA static HTML."""
    all_events: list[Event] = []

    # InsightLA — schema.org Event HTML parser
    try:
        events = fetch_insightla()
        log.info(f"  InsightLA → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ InsightLA failed: {e}")

    # Shambhala LA and other iCal feeds
    for org_id, feed_cfg in la_sources.ICAL_FEEDS.items():
        center = la_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (LA iCal)...")
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
            log.info(f"  → {len(events)} events found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ LA iCal feed {org_id} failed: {e}")

    # ZCLA and other static HTML targets
    for org_id, feed_cfg in la_sources.STATIC_HTML_FEEDS.items():
        center = la_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (LA static HTML)...")
        try:
            events = fetch_static_html_calendar(
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
            log.info(f"  → {len(events)} events found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ LA static HTML feed failed: {e}")

    return all_events


def run_boston_phase3() -> list[Event]:
    """Phase 3 Boston: Boston Shambhala iCal feed."""
    all_events: list[Event] = []

    for org_id, feed_cfg in boston_sources.ICAL_FEEDS.items():
        center = boston_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Boston iCal)...")
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
            log.info(f"  → {len(events)} events")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Boston iCal feed {org_id} failed: {e}")

    return all_events


def run_dc_phase3() -> list[Event]:
    """Phase 3 DC: IMCW EventAgent scraper."""
    all_events: list[Event] = []

    try:
        events = fetch_imcw()
        log.info(f"  IMCW → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ IMCW fetch failed: {e}")

    return all_events


def run_chicago_phase3() -> list[Event]:
    """Phase 3 Chicago: Sit Around Chicago Tockify aggregator iCal feed."""
    all_events: list[Event] = []

    try:
        events = fetch_tockify_chicago()
        log.info(f"  Sit Around Chicago (Tockify) → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Tockify Chicago fetch failed: {e}")

    return all_events


def run_seattle_phase3() -> list[Event]:
    """Phase 3 Seattle: iCal feeds + Nalandabodhi custom scraper."""
    all_events: list[Event] = []

    # Direct iCal feeds (Seattle Insight + KMC Washington)
    all_events.extend(run_seattle_ical())

    # Nalandabodhi — global iCal filtered to Seattle
    try:
        events = fetch_nalandabodhi_seattle()
        log.info(f"  Nalandabodhi Seattle → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Nalandabodhi Seattle failed: {e}")

    return all_events


def run_denver_phase3() -> list[Event]:
    """Phase 3 Denver/Boulder: iCal feeds for ZCD, Boulder Zen, Orgyen Khandroling."""
    all_events: list[Event] = []

    for org_id, feed_cfg in denver_sources.ICAL_FEEDS.items():
        center = denver_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Denver/Boulder iCal)...")
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
            log.error(f"  ✗ Denver/Boulder iCal {org_id} failed: {e}")

    return all_events


def run_portland_phase3() -> list[Event]:
    """Phase 3 Portland: iCal feeds for Dharma Rain Zen + Kagyu Changchub Chuling."""
    all_events: list[Event] = []

    for org_id, feed_cfg in portland_sources.ICAL_FEEDS.items():
        center = portland_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Portland iCal)...")
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
            log.error(f"  ✗ Portland iCal {org_id} failed: {e}")

    return all_events


def run_austin_phase3() -> list[Event]:
    """Phase 3 Austin: iCal feed for Kadampa Austin."""
    all_events: list[Event] = []

    for org_id, feed_cfg in austin_sources.ICAL_FEEDS.items():
        center = austin_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Austin iCal)...")
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
            log.error(f"  ✗ Austin iCal {org_id} failed: {e}")

    return all_events


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    init_db()
    events = (
        run_east_bay_phase1()
        + run_east_bay_phase2()
        + run_east_bay_phase2b()
        + run_nyc_phase3a()
        + run_nyc_phase3b()
        + run_nyc_phase3c()
        + run_la_phase3()
        + run_boston_phase3()
        + run_dc_phase3()
        + run_chicago_phase3()
        + run_seattle_phase3()
        + run_denver_phase3()
        + run_portland_phase3()
        + run_austin_phase3()
    )
    n = upsert_events(events)
    print(f"\n✓ {n} events upserted")
    d = dedup_events()
    if d:
        print(f"✓ {d} duplicate events removed")


if __name__ == "__main__":
    main()
