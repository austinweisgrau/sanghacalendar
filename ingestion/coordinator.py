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
from data.store import init_db, upsert_events
from ingestion.feeds.ical_feed import fetch_feed
from ingestion.scrapers.eventbrite import fetch_eventbrite_organizer
from ingestion.scrapers.static_html import fetch_static_html_calendar
from ingestion.sources.east_bay import CENTERS, EVENTBRITE_FEEDS, ICAL_FEEDS, STATIC_HTML_FEEDS

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


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    init_db()
    events = run_east_bay_phase1() + run_east_bay_phase2() + run_east_bay_phase2b()
    n = upsert_events(events)
    print(f"\n✓ {n} events upserted")


if __name__ == "__main__":
    main()
