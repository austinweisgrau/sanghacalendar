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

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from data.schemas.event import Event
from ingestion.feeds.ical_feed import fetch_feed
from ingestion.sources.east_bay import CENTERS, ICAL_FEEDS

log = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent / "data" / "events"


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


def save_events(events: list[Event], label: str = "east_bay") -> Path:
    """Save events to JSON."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / f"{label}.json"
    data = [vars(e) for e in events]
    out_path.write_text(json.dumps(data, indent=2, default=str))
    log.info(f"Saved {len(events)} events to {out_path}")
    return out_path


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    events = run_east_bay_phase1()
    out = save_events(events, "east_bay_phase1")
    print(f"\n✓ {len(events)} events written to {out}")


if __name__ == "__main__":
    main()
