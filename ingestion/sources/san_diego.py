"""
San Diego meditation center sources — Phase 3 expansion.

Covers San Diego metro area.

iCal feeds:
  - Kadampa Meditation Center San Diego (kmc_san_diego)
    Google Calendar: sddharma.com_81dvn4rrqjn21vv23kqo4m66hs@group.calendar.google.com
    Special events: empowerments, retreats, Tsog days through 2026.
    Note: regular GP classes (Sun/Mon/Thu) seeded separately as recurring sits.
  - San Diego Shambhala (shambhala_san_diego)
    Cologne iCal server: shambhala-koeln.de/ical.php?center=254 — 232 events.
    Sunday public sitting, Wednesday online, EcoDharma group, Nyinthün, etc.

Recurring sits (seeded in sangha-seed-recurring.js):
  - KMC San Diego: Sun 10:30am, Mon 6:30pm, Thu 6:30pm
    (Wix-based website, no iCal — schedule from meditateinsandiego.org)

Research notes (2026-05-11):
  - Deer Park Monastery (Escondido, 35 mi north): retreat monastery, no drop-in sits, skip.
  - Diamond Way San Diego: no accessible web presence found.
  - Nalandabodhi: Seattle-based, no SD location.
  - San Diego Zen Center (sdzc.org): domain not resolving — skip for now.
  - Insight Meditation San Diego: domain not resolving — skip for now.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_san_diego": Center(
        id="kmc_san_diego",
        name="Kadampa Meditation Center San Diego",
        url="https://meditateinsandiego.org",
        address="3502 Adams Ave",
        city="San Diego",
        state="CA",
        zip_code="92116",
        lat=32.7437,
        lng=-117.1381,
        neighborhood="Normal Heights / North Park",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center San Diego (KMC San Diego) is a Tibetan Buddhist center "
            "in the New Kadampa Tradition (NKT-IKBU), located in the Normal Heights neighborhood "
            "of San Diego. Offers regular General Program meditation classes open to all — no "
            "experience needed: Sunday 10:30am, Monday 6:30pm, and Thursday 6:30pm. Special "
            "events including empowerments, day retreats, and silent retreats are held monthly. "
            "Branch locations in Chula Vista and Oceanside. Free to attend; donations welcome."
        ),
    ),
    "shambhala_san_diego": Center(
        id="shambhala_san_diego",
        name="San Diego Shambhala Meditation Center",
        url="https://sandiego.shambhala.org",
        address="4622 Clairemont Dr",
        city="San Diego",
        state="CA",
        zip_code="92117",
        lat=32.8030,
        lng=-117.1978,
        neighborhood="Clairemont / Bay Park",
        tradition=Tradition.TIBETAN,
        notes=(
            "San Diego Shambhala Meditation Center is a contemplative community in the Shambhala "
            "lineage of Chögyam Trungpa Rinpoche. Meets in a home practice space in the Clairemont "
            "neighborhood of San Diego. Offers a Sunday morning public meditation sit (10–11am, "
            "in-person), bi-weekly Wednesday evening online meditation (7pm via Zoom), a monthly "
            "EcoDharma & EcoSattva group, and occasional Nyinthün all-day group practice sessions. "
            "Open to all; drop-in welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "kmc_san_diego_gcal": {
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "sddharma.com_81dvn4rrqjn21vv23kqo4m66hs%40group.calendar.google.com"
            "/public/basic.ics"
        ),
        "center_id": "kmc_san_diego",
        "filter_to_sits": True,
    },
    "shambhala_san_diego": {
        "url": "https://shambhala-koeln.de/ical.php?center=254",
        "center_id": "shambhala_san_diego",
        "filter_to_sits": True,
    },
}
