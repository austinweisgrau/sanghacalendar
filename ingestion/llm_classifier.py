"""
LLM-assisted event classification using Claude Haiku.
Used as a fallback when keyword heuristics are uncertain.
Requires ANTHROPIC_API_KEY env var — silently skips if not set.
"""

import json
import logging
import os
from typing import Optional

log = logging.getLogger(__name__)


def _client():
    try:
        import anthropic
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            return None
        return anthropic.Anthropic(api_key=key)
    except ImportError:
        return None


def classify_event(
    title: str,
    description: str = "",
    location: str = "",
    event_url: str = "",
) -> Optional[dict]:
    """
    Ask Claude to classify an event's location_type and whether it's a sit.
    Returns dict with keys: location_type, is_sit, confidence
    Returns None if API unavailable or call fails.
    """
    client = _client()
    if not client:
        return None

    prompt = f"""Classify this meditation event. Respond with JSON only, no explanation.

Title: {title}
Location field: {location or "(empty)"}
URL: {event_url or "(none)"}
Description (first 400 chars): {description[:400] or "(empty)"}

Return exactly this JSON structure:
{{
  "location_type": "in-person" | "online" | "hybrid",
  "is_sit": true | false,
  "confidence": "high" | "low"
}}

Rules:
- location_type is "online" if the event takes place via video/phone, even if a physical address appears in the location field
- location_type is "hybrid" if both in-person and online attendance are offered
- is_sit is true only if sitting meditation is the PRIMARY activity (not a talk, workshop, retreat, or class)
- Use confidence "low" if the data is ambiguous"""

    try:
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}],
        )
        return json.loads(msg.content[0].text.strip())
    except Exception as e:
        log.warning(f"LLM classification failed for '{title}': {e}")
        return None
