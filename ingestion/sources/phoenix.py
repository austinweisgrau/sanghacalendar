"""
Phoenix, AZ meditation center sources — Phase 3 expansion.

iCal feeds:
  None — main centers use Wix (no accessible iCal) or are closed.

Recurring sits (no accessible iCal):
  - Kadampa Meditation Center Phoenix — Wix site; schedule seeded from website nav.
    Sun morning, Mon evening, Wed evening GP classes. 614 E Townley Ave, Phoenix AZ 85020.

Research notes (2026-05-09):
  - Phoenix Shambhala: CLOSED Dec 31, 2025 — merged into Albuquerque Shambhala.
  - KMC Phoenix (meditationinarizona.org): Wix site, no iCal accessible.
  - Phoenix Zen Center: no web presence found.
  - Atlanta, Houston: limited accessible centers; deferred to later heartbeat.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kadampa_phoenix": Center(
        id="kadampa_phoenix",
        name="Kadampa Meditation Center Phoenix",
        url="https://www.meditationinarizona.org",
        address="614 East Townley Ave",
        city="Phoenix",
        state="AZ",
        zip_code="85020",
        lat=33.5731,
        lng=-112.0539,
        neighborhood="Sunnyslope / North Phoenix",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Phoenix (KMC Phoenix) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located in the Sunnyslope neighborhood of "
            "North Phoenix. Offers regular General Program meditation classes open to all: "
            "Sunday morning, Monday evening, and Wednesday evening at the main Phoenix location. "
            "Satellite sits in Scottsdale, Surprise, Fountain Hills, and Mesa. "
            "No experience necessary; all are welcome. Also operates Tucson KMC AZ and "
            "Williams World Peace Temple retreat center."
        ),
    ),
}

# No iCal feeds — Wix site, not accessible via ?ical=1
ICAL_FEEDS = {}
