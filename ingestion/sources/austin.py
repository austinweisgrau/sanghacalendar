"""
Austin, TX meditation center sources — Phase 3 expansion.

iCal feeds:
  - Kadampa Meditation Center Austin (meditationinaustin.org/events/?ical=1)

Recurring sits (no accessible iCal):
  - Austin Zen Center — site under maintenance as of 2026-05-08; schedule seeded from
    archived content. Soto Zen, 3014 Washington Square, Austin TX 78705.
"""

import logging

from data.schemas.event import Center, Tradition

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kadampa_austin": Center(
        id="kadampa_austin",
        name="Kadampa Meditation Center Austin",
        url="https://meditationinaustin.org",
        address="7101 Easy Wind Drive, Unit 3108",
        city="Austin",
        state="TX",
        zip_code="78752",
        lat=30.3785,
        lng=-97.7115,
        neighborhood="North Austin / Rundberg",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Austin (KMC Austin) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU). Located at Vessel Offsite in North Austin. "
            "Regular in-person programs at the main Austin location + a Georgetown branch "
            "(402 W 8th St, Georgetown Public Library, TX 78626). Classes include Heart Jewel, "
            "Foundation Program, Sunday General Program, and special weekend empowerments. "
            "All are welcome; no experience necessary. Free or donation-based intro classes available."
        ),
    ),
    "austin_zen": Center(
        id="austin_zen",
        name="Austin Zen Center",
        url="https://austinzencenter.org",
        address="3014 Washington Square",
        city="Austin",
        state="TX",
        zip_code="78705",
        lat=30.3073,
        lng=-97.7421,
        neighborhood="Hyde Park / Central Austin",
        tradition=Tradition.ZEN,
        notes=(
            "Austin Zen Center (AZC) is a Soto Zen Buddhist temple in the Suzuki Roshi / San "
            "Francisco Zen Center lineage, located in Hyde Park, Central Austin. Founded in "
            "the 1980s. Offers a full residential and lay practice schedule: Morning Program "
            "(zazen + kinhin + service, Tue–Fri 6am), Midday Sit (Tue–Thu 12pm informal zazen), "
            "Evening Program (zazen + service, Tue–Thu 5:40pm), and Saturday Program "
            "(8am beginner instruction + informal zazen, 9:15am zazen, 10:15am Dharma talk). "
            "Drop-in welcome. Online participation available for many programs."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Phase 3 Austin — iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "kadampa_austin": {
        # WordPress The Events Calendar (ECPv6) — confirmed working 2026-05-08
        "url": "https://meditationinaustin.org/events/?ical=1",
        "filter_to_sits": True,
    },
}
