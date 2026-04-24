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
from datetime import datetime, timezone

import anthropic
import httpx

from ingestion.feeds.ical_feed import fetch_feed
from ingestion.sources.east_bay import CENTERS, ICAL_FEEDS

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
        result = json.loads(msg.content[0].text.strip())
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
