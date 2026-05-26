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
from ingestion.scrapers.squarespace import fetch_squarespace_calendar
from ingestion.scrapers.static_html import fetch_static_html_calendar
from ingestion.scrapers.wild_apricot_rss import fetch_wild_apricot_rss

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
from ingestion.sources import minneapolis as minneapolis_sources
from ingestion.sources.minneapolis import fetch_common_ground
from ingestion.sources import houston as houston_sources
from ingestion.sources import albuquerque as albuquerque_sources
from ingestion.sources import miami as miami_sources
from ingestion.sources import san_diego as san_diego_sources
from ingestion.sources import atlanta as atlanta_sources
from ingestion.sources import nashville as nashville_sources
from ingestion.sources import detroit as detroit_sources
from ingestion.sources import sacramento as sacramento_sources
from ingestion.sources import pittsburgh as pittsburgh_sources
from ingestion.sources import ann_arbor as ann_arbor_sources
from ingestion.sources import st_louis as st_louis_sources
from ingestion.sources import cincinnati as cincinnati_sources
from ingestion.sources import kansas_city as kansas_city_sources
from ingestion.sources import richmond as richmond_sources
from ingestion.sources import columbus as columbus_sources
from ingestion.sources import raleigh as raleigh_sources  # noqa: F401 (no live feeds)
from ingestion.sources import salt_lake_city as slc_sources  # noqa: F401 (no live feeds)
from ingestion.sources import new_orleans as new_orleans_sources
from ingestion.sources import tampa as tampa_sources
from ingestion.sources import charlotte as charlotte_sources  # noqa: F401 (no live feeds)
from ingestion.sources import tucson as tucson_sources  # noqa: F401 (no live feeds)
from ingestion.sources import rochester as rochester_sources  # noqa: F401 (no live feeds)
from ingestion.sources import louisville as louisville_sources  # noqa: F401 (no live feeds)
from ingestion.sources import providence as providence_sources
from ingestion.sources import indianapolis as indianapolis_sources  # noqa: F401 (no live feeds)
from ingestion.sources import oklahoma_city as oklahoma_city_sources  # noqa: F401 (no live feeds)
from ingestion.sources import bloomington as bloomington_sources  # noqa: F401 (no live feeds)
from ingestion.sources import cleveland as cleveland_sources  # noqa: F401 (no live feeds)
from ingestion.sources import madison as madison_sources
from ingestion.sources import connecticut as connecticut_sources  # noqa: F401 (no live feeds)
from ingestion.sources import omaha as omaha_sources  # noqa: F401 (no live feeds)
from ingestion.sources import boise as boise_sources  # noqa: F401 (no live feeds)
from ingestion.sources import spokane as spokane_sources
from ingestion.sources import fresno as fresno_sources  # noqa: F401 (no live feeds)
from ingestion.sources import asheville as asheville_sources  # noqa: F401 (no live feeds)
from ingestion.sources import burlington as burlington_sources
from ingestion.sources import eugene as eugene_sources  # noqa: F401 (no live feeds)
from ingestion.sources import santa_cruz as santa_cruz_sources
from ingestion.sources import wichita as wichita_sources  # noqa: F401 (no live feeds)
from ingestion.sources import missoula as missoula_sources  # noqa: F401 (no live feeds)
from ingestion.sources import bozeman as bozeman_sources
from ingestion.sources import lehigh_valley as lehigh_valley_sources  # noqa: F401 (no live feeds)
from ingestion.sources import knoxville as knoxville_sources  # noqa: F401 (no live feeds)
from ingestion.sources import chattanooga as chattanooga_sources  # noqa: F401 (no live feeds)
from ingestion.sources import colorado_springs as colorado_springs_sources  # noqa: F401 (no live feeds)

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
    """Phase 3 Chicago: Sit Around Chicago Tockify aggregator iCal feed + Kadampa Eventbrite."""
    all_events: list[Event] = []

    try:
        events = fetch_tockify_chicago()
        log.info(f"  Sit Around Chicago (Tockify) → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Tockify Chicago fetch failed: {e}")

    # Kadampa Chicago — Eventbrite (not in Tockify aggregator)
    for org_id, feed_cfg in chicago_sources.EVENTBRITE_FEEDS.items():
        center = chicago_sources.CENTERS_EXTRA[org_id]
        log.info(f"Fetching {center.name} (Eventbrite Chicago)...")
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


def run_minneapolis_phase3() -> list[Event]:
    """Phase 3 Minneapolis: Common Ground via Sanity API."""
    all_events: list[Event] = []

    try:
        events = fetch_common_ground()
        log.info(f"  Common Ground → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Common Ground fetch failed: {e}")

    return all_events


def run_houston_phase3() -> list[Event]:
    """Phase 3 Houston: iCal feeds + Squarespace JSON for Houston centers."""
    all_events: list[Event] = []

    for org_id, feed_cfg in houston_sources.ICAL_FEEDS.items():
        center = houston_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Houston iCal)...")
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
            log.error(f"  ✗ Houston iCal {org_id} failed: {e}")

    # Houston Zen Center — Squarespace JSON (dharma talks, classes, retreats)
    for org_id, feed_cfg in houston_sources.SQUARESPACE_FEEDS.items():
        center = houston_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Squarespace)...")
        try:
            events = fetch_squarespace_calendar(
                url=feed_cfg["url"],
                org_id=org_id,
                org_name=center.name,
                tradition=center.tradition,
                filter_to_sits=feed_cfg.get("filter_to_sits", False),
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
            log.error(f"  ✗ Houston Squarespace {org_id} failed: {e}")

    return all_events


def run_albuquerque_phase3() -> list[Event]:
    """Phase 3 New Mexico: ABQ Shambhala (center=268) + Upaya Zen Center Santa Fe iCal."""
    all_events: list[Event] = []

    for org_id, feed_cfg in albuquerque_sources.ICAL_FEEDS.items():
        center = albuquerque_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (NM iCal)...")
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
            log.error(f"  ✗ NM iCal {org_id} failed: {e}")

    return all_events


def run_miami_phase3() -> list[Event]:
    """Phase 3 Miami/South Florida: KMC Fort Lauderdale Google Calendar iCal feeds."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in miami_sources.ICAL_FEEDS.items():
        center = miami_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Miami iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ Miami iCal {feed_id} failed: {e}")

    return all_events


def run_san_diego_phase3() -> list[Event]:
    """Phase 3 San Diego: KMC San Diego (Google Calendar) + SD Shambhala (Cologne iCal)."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in san_diego_sources.ICAL_FEEDS.items():
        center = san_diego_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (San Diego iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ San Diego iCal {feed_id} failed: {e}")

    return all_events


def run_atlanta_phase3() -> list[Event]:
    """Phase 3 Atlanta: Shambhala (Cologne iCal), Red Clay Sangha (RSS), Drepung Loseling (HTML)."""
    all_events: list[Event] = []

    # Atlanta Shambhala — Cologne iCal
    for feed_id, feed_cfg in atlanta_sources.ICAL_FEEDS.items():
        center = atlanta_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Atlanta iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ Atlanta iCal {feed_id} failed: {e}")

    # Red Clay Sangha — Wild Apricot RSS
    for feed_id, feed_cfg in atlanta_sources.RSS_FEEDS.items():
        center = atlanta_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Wild Apricot RSS: {feed_id})...")
        try:
            events = fetch_wild_apricot_rss(
                url=feed_cfg["url"],
                org_id=center.id,
                org_name=center.name,
                tradition=center.tradition,
                title_keywords=feed_cfg["title_keywords"],
                filter_to_sits=feed_cfg.get("filter_to_sits", True),
                duration_min=feed_cfg.get("duration_min", 90),
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
            log.error(f"  ✗ Atlanta RSS {feed_id} failed: {e}")

    # Drepung Loseling — static HTML monthly calendar
    for feed_id, feed_cfg in atlanta_sources.STATIC_HTML_FEEDS.items():
        center = atlanta_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (static HTML: {feed_id})...")
        try:
            events = fetch_static_html_calendar(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ Atlanta static HTML {feed_id} failed: {e}")

    return all_events


def run_nashville_phase3() -> list[Event]:
    """Phase 3 Nashville: recurring sits only (seeded via sangha-seed-recurring.js)."""
    # Nashville sources have no active iCal feeds — all sits seeded as recurring.
    # This function exists for structural consistency and future iCal additions.
    return []


def run_detroit_phase3() -> list[Event]:
    """Phase 3 Detroit: recurring sits only (seeded via sangha-seed-recurring.js)."""
    # Detroit/SE Michigan sources have no accessible iCal feeds — all sits seeded as
    # recurring. This function exists for structural consistency and future iCal additions.
    return []


def run_sacramento_phase3() -> list[Event]:
    """Phase 3 Sacramento: SBMG + VSZS (WordPress iCal) + Lion's Roar (Google Calendar)."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in sacramento_sources.ICAL_FEEDS.items():
        center = sacramento_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Sacramento iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ Sacramento iCal {feed_id} failed: {e}")

    return all_events


def run_pittsburgh_phase3() -> list[Event]:
    """Phase 3 Pittsburgh: recurring sits only (seeded via sangha-seed-recurring.js)."""
    # Pittsburgh sources have no active iCal feeds — all sits seeded as recurring.
    # This function exists for structural consistency and future iCal additions.
    return []


def run_st_louis_phase3() -> list[Event]:
    """Phase 3 St. Louis: Confluence Zen Center iCal feed."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in st_louis_sources.ICAL_FEEDS.items():
        center = st_louis_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (St. Louis iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ St. Louis iCal {feed_id} failed: {e}")

    return all_events


def run_ann_arbor_phase3() -> list[Event]:
    """Phase 3 Ann Arbor: Jewel Heart (Google Calendar iCal)."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in ann_arbor_sources.ICAL_FEEDS.items():
        center = ann_arbor_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Ann Arbor iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ Ann Arbor iCal {feed_id} failed: {e}")

    return all_events


def run_cincinnati_phase3() -> list[Event]:
    """Phase 3 Cincinnati: recurring sits only (seeded via sangha-seed-recurring.js)."""
    # Cincinnati sources have no active iCal feeds — all sits seeded as recurring.
    # This function exists for structural consistency and future iCal additions.
    return []


def run_kansas_city_phase3() -> list[Event]:
    """Phase 3 Kansas City: recurring sits only (seeded via sangha-seed-recurring.js)."""
    # Kansas City sources have no active iCal feeds — all sits seeded as recurring.
    # This function exists for structural consistency and future iCal additions.
    return []


def run_richmond_phase3() -> list[Event]:
    """Phase 3 Richmond VA: IMCR iCal (special events/retreats) + recurring sits."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in richmond_sources.ICAL_FEEDS.items():
        center = richmond_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Richmond iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ Richmond iCal {feed_id} failed: {e}")

    return all_events


def run_columbus_phase3() -> list[Event]:
    """Phase 3 Columbus OH: KTC iCal feed + recurring sits (seeded via sangha-seed-recurring.js)."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in columbus_sources.ICAL_FEEDS.items():
        center = columbus_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Columbus iCal: {feed_id})...")
        try:
            events = fetch_feed(
                url=feed_cfg["url"],
                org_id=center.id,
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
            log.error(f"  ✗ Columbus iCal {feed_id} failed: {e}")

    return all_events


def run_raleigh_phase3() -> list[Event]:
    """Phase 3 Raleigh-Durham-Chapel Hill NC: all centers seeded as recurring sits."""
    # No live iCal feeds — all Triangle centers use recurring sit seeding
    # via scripts/sangha-seed-recurring.js
    return []


def run_salt_lake_city_phase3() -> list[Event]:
    """Phase 3 Salt Lake City UT: all centers seeded as recurring sits."""
    # No live iCal feeds — all SLC centers use recurring sit seeding
    # via scripts/sangha-seed-recurring.js
    return []


def run_new_orleans_phase3() -> list[Event]:
    """Phase 3 New Orleans LA: Mid City Zen Google Calendar iCal."""
    all_events: list[Event] = []

    for org_id, feed_cfg in new_orleans_sources.ICAL_FEEDS.items():
        center = new_orleans_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (New Orleans iCal)...")
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
            log.error(f"  ✗ New Orleans iCal {org_id} failed: {e}")

    return all_events


def run_tampa_phase3() -> list[Event]:
    """Phase 3 Tampa Bay: Florida Community of Mindfulness (Wild Apricot RSS)."""
    all_events: list[Event] = []

    for feed_id, feed_cfg in tampa_sources.RSS_FEEDS.items():
        center = tampa_sources.CENTERS[feed_cfg["center_id"]]
        log.info(f"Fetching {center.name} (Wild Apricot RSS: {feed_id})...")
        try:
            events = fetch_wild_apricot_rss(
                url=feed_cfg["url"],
                org_id=center.id,
                org_name=center.name,
                tradition=center.tradition,
                title_keywords=feed_cfg["title_keywords"],
                filter_to_sits=feed_cfg.get("filter_to_sits", True),
                duration_min=feed_cfg.get("duration_min", 90),
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
            log.error(f"  ✗ Tampa RSS {feed_id} failed: {e}")

    return all_events


def run_charlotte_phase3() -> list[Event]:
    """Phase 3 Charlotte NC: all centers seeded as recurring sits."""
    # No live iCal feeds — all Charlotte centers use recurring sit seeding
    # via scripts/sangha-seed-recurring.js
    return []


def run_tucson_phase3() -> list[Event]:
    """Phase 3 Tucson AZ: all centers seeded as recurring sits."""
    # KMC Arizona (Tucson) has no accessible iCal — sits seeded as recurring
    # via scripts/sangha-seed-recurring.js
    return []


def run_honolulu_phase3() -> list[Event]:
    """Phase 3 Honolulu HI: all centers seeded as recurring sits."""
    # All Honolulu centers (Diamond Sangha, Soto Mission, Bodhi Tree, Aloha Sangha)
    # have no accessible iCal feeds — sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_rochester_phase3() -> list[Event]:
    """Phase 3 Rochester NY: all centers seeded as recurring sits."""
    # RZC (Cloudflare blocks iCal), Endless Path Zendo (static HTML), Dharma Refuge (Weebly)
    # all seeded via scripts/sangha-seed-recurring.js
    return []


def run_louisville_phase3() -> list[Event]:
    """Phase 3 Louisville KY: all centers seeded as recurring sits."""
    # No live iCal feeds extractable; all sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_indianapolis_phase3() -> list[Event]:
    """Phase 3 Indianapolis IN: all centers seeded as recurring sits."""
    # No live iCal feeds extractable; all sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_oklahoma_city_phase3() -> list[Event]:
    """Phase 3 Oklahoma City OK: all centers seeded as recurring sits."""
    # No live iCal feeds extractable; all sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_bloomington_phase3() -> list[Event]:
    """Phase 3 Bloomington IN: all centers seeded as recurring sits."""
    # No live iCal feeds extractable; all sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_cleveland_phase3() -> list[Event]:
    """Phase 3 Cleveland OH: all centers seeded as recurring sits."""
    # No live iCal feeds extractable; all sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_connecticut_phase3() -> list[Event]:
    """Phase 3 Connecticut (Hartford/New Haven): all centers seeded as recurring sits."""
    # No live iCal feeds accessible; all sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_omaha_phase3() -> list[Event]:
    """Phase 3 Omaha/Lincoln NE: all centers seeded as recurring sits."""
    # No live iCal feeds accessible; all sits seeded via scripts/sangha-seed-recurring.js
    return []


def run_madison_phase3() -> list[Event]:
    """Phase 3 Madison WI: Shambhala Madison iCal feed + recurring-only centers."""
    all_events: list[Event] = []

    for org_id, feed_cfg in madison_sources.ICAL_FEEDS.items():
        center = madison_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Madison iCal)...")
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
            log.error(f"  ✗ Madison iCal feed {org_id} failed: {e}")

    return all_events


def run_spokane_phase3() -> list[Event]:
    """Phase 3 Spokane WA: Zen Center of Spokane iCal feed + recurring-only centers."""
    all_events: list[Event] = []

    for org_id, feed_cfg in spokane_sources.ICAL_FEEDS.items():
        center = spokane_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Spokane iCal)...")
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
            log.error(f"  ✗ Spokane iCal feed {org_id} failed: {e}")

    return all_events


def run_burlington_phase3() -> list[Event]:
    """Phase 3 Burlington VT: Shambhala iCal + Vermont Zen Center Tockify + recurring-only centers."""
    all_events: list[Event] = []

    for org_id, feed_cfg in burlington_sources.ICAL_FEEDS.items():
        center = burlington_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Burlington iCal)...")
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
            log.error(f"  ✗ Burlington iCal feed {org_id} failed: {e}")

    # Burlington Buddhist Sangha + Burlington Dharma Collective — seeded via sangha-seed-recurring.js
    return all_events


def run_santa_cruz_phase3() -> list[Event]:
    """Phase 3 Santa Cruz CA: Ocean Gate Zen Tockify ICS + recurring-only centers."""
    all_events: list[Event] = []

    for org_id, feed_cfg in santa_cruz_sources.ICAL_FEEDS.items():
        center = santa_cruz_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Santa Cruz iCal)...")
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
            log.error(f"  ✗ Santa Cruz iCal feed {org_id} failed: {e}")

    # SCZC, Insight Santa Cruz, Land of Medicine Buddha — seeded via sangha-seed-recurring.js
    return all_events


def run_providence_phase3() -> list[Event]:
    """Phase 3 Providence RI: Providence Zen Center Tockify ICS + recurring-only centers."""
    events: list[Event] = []

    # Providence Zen Center — Tockify ICS feed
    for org_id, feed_cfg in providence_sources.ICAL_FEEDS.items():
        center = providence_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Providence Tockify iCal)...")
        try:
            evts = fetch_feed(
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
            log.info(f"  → {len(evts)} sits from {center.name}")
            events.extend(evts)
        except Exception as e:
            log.error(f"  ✗ Providence iCal {org_id} failed: {e}")

    # AKBC, IMCP, Insight PVD, RICM Radiant Bell — all seeded via sangha-seed-recurring.js
    return events


def run_bozeman_phase3() -> list[Event]:
    """Phase 3 Bozeman MT: Bozeman Dharma Center WordPress iCal feed."""
    all_events: list[Event] = []

    for org_id, feed_cfg in bozeman_sources.ICAL_FEEDS.items():
        center = bozeman_sources.CENTERS[org_id]
        log.info(f"Fetching {center.name} (Bozeman iCal)...")
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
            log.error(f"  ✗ Bozeman iCal feed {org_id} failed: {e}")

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
        + run_minneapolis_phase3()
        + run_houston_phase3()
        + run_albuquerque_phase3()
        + run_miami_phase3()
        + run_san_diego_phase3()
        + run_atlanta_phase3()
        + run_nashville_phase3()
        + run_detroit_phase3()
        + run_sacramento_phase3()
        + run_pittsburgh_phase3()
        + run_ann_arbor_phase3()
        + run_st_louis_phase3()
        + run_cincinnati_phase3()
        + run_kansas_city_phase3()
        + run_richmond_phase3()
        + run_columbus_phase3()
        + run_raleigh_phase3()
        + run_salt_lake_city_phase3()
        + run_new_orleans_phase3()
        + run_tampa_phase3()
        + run_charlotte_phase3()
        + run_tucson_phase3()
        + run_honolulu_phase3()
        + run_rochester_phase3()
        + run_louisville_phase3()
        + run_providence_phase3()
        + run_indianapolis_phase3()
        + run_oklahoma_city_phase3()
        + run_bloomington_phase3()
        + run_cleveland_phase3()
        + run_madison_phase3()
        + run_connecticut_phase3()
        + run_omaha_phase3()
        + run_spokane_phase3()
        + run_burlington_phase3()
        + run_santa_cruz_phase3()
        + run_bozeman_phase3()
        # Lehigh Valley PA Phase 3 — all centers seeded via sangha-seed-recurring.js
        # Chattanooga TN Phase 3 — all centers seeded via sangha-seed-recurring.js
    )
    n = upsert_events(events)
    print(f"\n✓ {n} events upserted")
    d = dedup_events()
    if d:
        print(f"✓ {d} duplicate events removed")


if __name__ == "__main__":
    main()
