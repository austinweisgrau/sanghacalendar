"""
Abraxis-driven ingestion — runs on Abraxis's weekly/monthly schedule.

Differs from the app's coordinator.py in that:
- Uses Claude for full classification (not just uncertain heuristic fallbacks)
- POSTs results to the Fly app via /api/admin/events (no SSH required)
- Handles enrichment: identity_focus, accessibility, tradition refinement

Usage (from /workspace/group/sangha-calendar/):
  source /workspace/group/.venv/bin/activate
  SANGHA_APP_URL=https://sangha-calendar.fly.dev \\
  INGEST_TOKEN=<token> \\
  python -m ingestion.abraxis_ingest

For local dev, set SANGHA_APP_URL=http://localhost:8080
"""

import hashlib
import json
import logging
import os
import re
from datetime import datetime, timezone

import anthropic
import httpx

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
from ingestion.sources.dc import fetch_imcw
from ingestion.sources import chicago as chicago_sources
from ingestion.sources.chicago import fetch_tockify_chicago
from ingestion.sources.seattle import fetch_nalandabodhi_seattle, run_seattle_ical
from ingestion.sources import denver as denver_sources
from ingestion.sources import portland as portland_sources
from ingestion.sources import austin as austin_sources
from ingestion.sources.minneapolis import fetch_common_ground
from ingestion.sources import houston as houston_sources
from ingestion.sources import albuquerque as albuquerque_sources
from ingestion.sources import miami as miami_sources
from ingestion.sources import san_diego as san_diego_sources
from ingestion.sources import atlanta as atlanta_sources
from ingestion.sources import sacramento as sacramento_sources
from ingestion.sources import ann_arbor as ann_arbor_sources
from ingestion.sources import st_louis as st_louis_sources
from ingestion.sources import cincinnati as cincinnati_sources
from ingestion.sources import kansas_city as kansas_city_sources
from ingestion.sources import richmond as richmond_sources
from ingestion.sources import columbus as columbus_sources
from ingestion.sources import raleigh as raleigh_sources  # noqa: F401 (no live feeds)

log = logging.getLogger(__name__)

APP_URL     = os.environ["SANGHA_APP_URL"].rstrip("/")
INGEST_TOKEN = os.environ["INGEST_TOKEN"]
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY")


def enrich_event(event: dict, client: anthropic.Anthropic) -> dict:
    """
    Ask Claude to enrich a single event dict with:
    - location_type (verify/override heuristic)
    - identity_focus (BIPOC, LGBTQ+, etc.)
    - tradition refinement
    - is_sit confirmation
    """
    prompt = f"""You are classifying a meditation event for a public calendar. Return JSON only.

org: {event.get('org_name')}
title: {event.get('title')}
location field: {event.get('address', '')} {event.get('city', '')}
event url: {event.get('event_url') or '(none)'}
notes/description: {(event.get('notes') or '')[:500]}

Return exactly this JSON (no markdown):
{{
  "location_type": "in-person" | "online" | "hybrid",
  "is_sit": true | false,
  "identity_focus": "<group if event targets a specific identity, e.g. BIPOC, LGBTQ+, women, disabled> | null",
  "tradition": "theravada" | "zen" | "tibetan" | "secular" | "pluralist" | "other" | "unknown"
}}

Rules:
- location_type "online" if primary attendance is via video, even if a venue is listed
- is_sit true only if sitting meditation is the PRIMARY activity
- identity_focus: extract from title/description if present, otherwise null
- tradition: best match given org name and context"""

    try:
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
        raw = re.sub(r'^```(?:json)?\s*', '', raw, flags=re.MULTILINE)
        raw = re.sub(r'\s*```$', '', raw, flags=re.MULTILINE)
        result = json.loads(raw)
        event.update({
            "location_type":  result.get("location_type", event.get("location_type")),
            "is_sit":         result.get("is_sit", event.get("is_sit", True)),
            "identity_focus": result.get("identity_focus"),
            "tradition":      result.get("tradition", event.get("tradition")),
        })
    except Exception as e:
        log.warning(f"Enrichment failed for '{event.get('title')}': {e}")
    return event


def post_events(events: list[dict]) -> int:
    resp = httpx.post(
        f"{APP_URL}/api/admin/events",
        headers={"Authorization": f"Bearer {INGEST_TOKEN}", "Content-Type": "application/json"},
        json={"events": events},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("upserted", 0)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY) if ANTHROPIC_KEY else None
    if not client:
        log.warning("No ANTHROPIC_API_KEY — skipping enrichment, using heuristics only")

    all_events = []
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
            log.info(f"  → {len(events)} sits from heuristics")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Feed failed: {e}")

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
            log.error(f"  ✗ Eventbrite feed failed: {e}")

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
            log.error(f"  ✗ Static HTML feed failed: {e}")

    # NYC Phase 3a — direct iCal feeds
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
            log.error(f"  ✗ NYC feed failed: {e}")

    # NYC Phase 3b — Shambhala NYC scraper + Tibet House Eventbrite
    try:
        shambhala_events = fetch_shambhala_nyc()
        log.info(f"  Shambhala NYC → {len(shambhala_events)} events")
        all_events.extend(shambhala_events)
    except Exception as e:
        log.error(f"  ✗ Shambhala NYC failed: {e}")

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
            log.error(f"  ✗ Eventbrite NYC feed failed: {e}")

    # NYC Phase 3c — Zen Studies Society iCal + ZCNYC static HTML
    try:
        zenstudies_events = fetch_zenstudies_nyc()
        log.info(f"  NY Zendo Shobo-Ji → {len(zenstudies_events)} events")
        all_events.extend(zenstudies_events)
    except Exception as e:
        log.error(f"  ✗ NY Zendo Shobo-Ji failed: {e}")

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
            log.error(f"  ✗ NYC static HTML feed failed: {e}")

    # LA Phase 3 — InsightLA schema.org scraper
    log.info("--- LA Phase 3: InsightLA ---")
    try:
        insightla_events = fetch_insightla()
        log.info(f"  InsightLA → {len(insightla_events)} events")
        all_events.extend(insightla_events)
    except Exception as e:
        log.error(f"  ✗ InsightLA failed: {e}")

    # LA Phase 3 — Shambhala LA and other iCal feeds
    log.info("--- LA Phase 3: iCal feeds ---")
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

    # ZCLA and other LA static HTML targets
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

    # Boston Phase 3 — Shambhala Boston iCal
    log.info("--- Boston Phase 3: Shambhala Boston iCal ---")
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

    # DC Phase 3 — IMCW EventAgent scraper
    log.info("--- DC Phase 3: IMCW EventAgent ---")
    try:
        events = fetch_imcw()
        log.info(f"  IMCW → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ IMCW fetch failed: {e}")

    # Chicago Phase 3 — Sit Around Chicago Tockify aggregator
    log.info("--- Chicago Phase 3: Tockify aggregator ---")
    try:
        events = fetch_tockify_chicago()
        log.info(f"  Sit Around Chicago → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Tockify Chicago fetch failed: {e}")

    # Chicago Phase 3 — Kadampa Chicago Eventbrite
    for org_id, feed_cfg in chicago_sources.EVENTBRITE_FEEDS.items():
        center = chicago_sources.CENTERS_EXTRA[org_id]
        log.info(f"  Fetching {center.name} (Eventbrite Chicago)...")
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
            log.info(f"    → {len(events)} events found")
            all_events.extend(events)
        except Exception as e:
            log.error(f"  ✗ Kadampa Chicago Eventbrite failed: {e}")

    # Seattle Phase 3 — iCal feeds + Nalandabodhi custom scraper
    log.info("--- Seattle Phase 3: iCal feeds + Nalandabodhi ---")
    try:
        seattle_events = run_seattle_ical()
        log.info(f"  Seattle iCal feeds → {len(seattle_events)} events")
        all_events.extend(seattle_events)
    except Exception as e:
        log.error(f"  ✗ Seattle iCal feeds failed: {e}")

    try:
        events = fetch_nalandabodhi_seattle()
        log.info(f"  Nalandabodhi Seattle → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Nalandabodhi Seattle failed: {e}")

    # Denver/Boulder Phase 3 — iCal feeds (ZCD, Boulder Zen, Orgyen Khandroling)
    log.info("--- Denver/Boulder Phase 3: iCal feeds ---")
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

    # Portland Phase 3 — iCal feeds (Dharma Rain Zen + KCC)
    log.info("--- Portland Phase 3: iCal feeds ---")
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

    # Austin Phase 3 — iCal feeds (Kadampa Austin)
    log.info("--- Austin Phase 3: iCal feeds ---")
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

    # Minneapolis Phase 3 — Common Ground via Sanity API
    log.info("--- Minneapolis Phase 3: Common Ground Sanity API ---")
    try:
        events = fetch_common_ground()
        log.info(f"  Common Ground → {len(events)} events")
        all_events.extend(events)
    except Exception as e:
        log.error(f"  ✗ Common Ground Sanity API failed: {e}")

    # Houston Phase 3 — iCal feeds (Chung Tai Zen Center + Dawn Mountain)
    log.info("--- Houston Phase 3: iCal feeds ---")
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

    # Houston Phase 3 — Squarespace JSON (Houston Zen Center dharma talks/classes)
    log.info("--- Houston Phase 3: Squarespace JSON ---")
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

    # New Mexico Phase 3 — ABQ Shambhala + Upaya Zen Center Santa Fe
    log.info("--- New Mexico Phase 3: iCal feeds ---")
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

    # Miami / South Florida Phase 3 — KMC Fort Lauderdale Google Calendar iCal feeds
    log.info("--- Miami Phase 3: iCal feeds ---")
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

    # San Diego Phase 3 — KMC SD (Google Calendar) + SD Shambhala (Cologne iCal)
    log.info("--- San Diego Phase 3: iCal feeds ---")
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

    # Atlanta Phase 3 — Atlanta Shambhala (Cologne iCal center=196)
    log.info("--- Atlanta Phase 3: iCal feeds ---")
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

    # Atlanta Phase 3 — Red Clay Sangha (Wild Apricot RSS)
    log.info("--- Atlanta Phase 3: RSS feeds ---")
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

    # Atlanta Phase 3 — Drepung Loseling (static HTML monthly calendar)
    log.info("--- Atlanta Phase 3: static HTML feeds ---")
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

    # Sacramento Phase 3 — SBMG + VSZS (WordPress iCal) + Lion's Roar (Google Calendar)
    log.info("--- Sacramento Phase 3: iCal feeds ---")
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

    # St. Louis Phase 3 — Confluence Zen Center iCal
    log.info("--- St. Louis Phase 3: iCal feeds ---")
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

    # Ann Arbor Phase 3 — Jewel Heart (Google Calendar iCal)
    log.info("--- Ann Arbor Phase 3: iCal feeds ---")
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

    # Cincinnati Phase 3 — all sits seeded as recurring; no iCal feeds
    log.info("--- Cincinnati Phase 3: no iCal feeds (recurring sits only) ---")

    # Kansas City Phase 3 — all sits seeded as recurring; no iCal feeds
    log.info("--- Kansas City Phase 3: no iCal feeds (recurring sits only) ---")

    # Richmond VA Phase 3 — IMCR iCal (special events/retreats)
    log.info("--- Richmond VA Phase 3: IMCR iCal feed ---")
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

    # Columbus OH Phase 3 — KTC iCal feed
    log.info("--- Columbus OH Phase 3: Columbus KTC iCal feed ---")
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

    # Convert dataclasses to dicts
    dicts = []
    for e in all_events:
        d = {
            "id": e.id, "org_id": e.org_id, "org_name": e.org_name,
            "title": e.title, "start_time": e.start_time, "end_time": e.end_time,
            "address": e.address, "city": e.city, "state": e.state,
            "neighborhood": e.neighborhood, "lat": e.lat, "lng": e.lng,
            "tradition": e.tradition.value if hasattr(e.tradition, "value") else e.tradition,
            "location_type": e.location_type.value if hasattr(e.location_type, "value") else e.location_type,
            "is_sit": e.is_sit, "accessibility_notes": e.accessibility_notes,
            "identity_focus": e.identity_focus,
            "source": e.source.value if hasattr(e.source, "value") else e.source,
            "source_url": e.source_url, "event_url": e.event_url,
            "last_verified": e.last_verified, "recurrence": e.recurrence, "notes": e.notes,
        }
        if client:
            d = enrich_event(d, client)
        dicts.append(d)

    log.info(f"Posting {len(dicts)} events to {APP_URL}...")
    n = post_events(dicts)
    print(f"\n✓ {n} events upserted via API")


if __name__ == "__main__":
    main()
