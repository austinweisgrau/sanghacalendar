"""
Jersey City, NJ — Phase 3 expansion.

Jersey City (~300k, Hudson County) is a dense, diverse city directly across
the Hudson from Lower Manhattan, served by PATH trains. Two confirmed
active centers offering regular public sits as of October 2026:

Centers included:
  - Kadampa Meditation Center NYC — Jersey City Class (kadampa_jersey_city)
    — New Kadampa Tradition (NKT), Tibetan-derived, Gelug lineage
    Barrow Mansion, 83 Wayne St, Jersey City NJ 07302
    meditationinnewyork.org/jersey-city-meditation-and-buddhism/
    Sunday General Program: Sundays 11:30am–1:00pm
    Taught by Jessica Rispoli and rotating NKT teachers.
    Long-running satellite class of KMC New York City.
    $10/class; free for supporting members.
    No standalone iCal; recurring sit seeded.

  - Sun of Awareness Sangha (sun_of_awareness_jc)
    — Plum Village / Thich Nhat Hanh (Vietnamese Zen / Engaged Buddhism)
    275 Grove St, 3rd floor, Jersey City NJ 07302 (at Yoga Shunya)
    sunofawareness.wordpress.com
    Founded 2009 by Robb Kushner. Affiliated with Community of Mindfulness
    NY Metro and Blue Cliff Monastery (Pine Bush, NY).
    Sunday sit: Sundays 9:00–10:30am
    Format: silent/guided sitting, walking meditation, dharma reading + sharing
    In-person only; free ($5–10 donation to venue welcome).
    No machine-readable calendar; recurring sit seeded.

Research notes (2026-10-10):
  - Kadampa JC class is a long-running satellite of KMC NYC; confirmed active
    with current fall 2026 series ("The Love Meditations").
  - Sun of Awareness has been running since 2009; small lay sangha, no live
    calendar feed. Status should be periodically reconfirmed.
  - Newark Center for Meditative Culture (2 Park Place, Newark) researched —
    events calendar empty as of Oct 2026 (between seasonal series). Skipped
    pending schedule confirmation; contact info@newarkmeditation.org.
  - No Shambhala center in Newark/JC; nearest is Princeton (NJ) or Manhattan.
  - No Zen center with public sits found in Newark/JC proper.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kadampa_jersey_city": Center(
        id="kadampa_jersey_city",
        name="Kadampa Meditation Center NYC — Jersey City",
        url="https://meditationinnewyork.org/jersey-city-meditation-and-buddhism/",
        address="83 Wayne St",
        city="Jersey City",
        state="NJ",
        zip_code="07302",
        lat=40.7183,
        lng=-74.0450,
        neighborhood="Van Vorst Park / Downtown Jersey City (Barrow Mansion)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center NYC — Jersey City is a long-running satellite "
            "class of KMC New York City (meditationinnewyork.org), offering weekly "
            "Buddhist meditation and teachings in the New Kadampa Tradition (NKT). "
            "Held at the historic Barrow Mansion (83 Wayne St), steps from Grove St "
            "PATH station in downtown Jersey City. Teacher: Jessica Rispoli and "
            "rotating NKT teachers. Sunday General Program: Sundays 11:30am–1:00pm "
            "(guided meditation + Buddhist teachings; topic rotates with seasonal "
            "series). $10/class; free for NKT supporting members. "
            "meditationinnewyork.org/jersey-city-meditation-and-buddhism/."
        ),
    ),
    "sun_of_awareness_jc": Center(
        id="sun_of_awareness_jc",
        name="Sun of Awareness Sangha",
        url="https://sunofawareness.wordpress.com/",
        address="275 Grove St, 3rd Floor",
        city="Jersey City",
        state="NJ",
        zip_code="07302",
        lat=40.7185,
        lng=-74.0462,
        neighborhood="Downtown Jersey City (Yoga Shunya)",
        tradition=Tradition.ZEN,
        notes=(
            "Sun of Awareness Sangha is a Plum Village / Thich Nhat Hanh lay sangha "
            "in downtown Jersey City, founded 2009 by Robb Kushner. Affiliated with "
            "the Community of Mindfulness New York Metro network and Blue Cliff "
            "Monastery (Pine Bush, NY). Meets Sundays 9:00–10:30am at Yoga Shunya "
            "(275 Grove St, 3rd floor — enter double doors left of Bar Majestic, then "
            "upstairs). Format: silent or guided sitting meditation, walking "
            "meditation, dharma reading and sharing, closing sit. All welcome; "
            "beginners-friendly. Free ($5–10 donation to Yoga Shunya welcome). "
            "Contact: Robb Kushner, 201-349-4481, robbkushner@gmail.com. "
            "sunofawareness.wordpress.com."
        ),
    ),
}


# No live iCal feeds — recurring sits seeded in scripts/sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
EVENTBRITE_FEEDS: dict = {}
