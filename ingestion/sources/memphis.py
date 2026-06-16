"""
Memphis, TN + Batesville, MS — Phase 3 expansion (heartbeat 79).

Memphis (pop. ~620k; metro ~1.35M) is a significant city in the Mid-South with a modest
but authentic Buddhist community. Tradition coverage: Soto Zen, Nyingma Tibetan, and
Plum Village. No live iCal feeds found for Memphis proper; sits seeded as recurring.

Magnolia Grove Monastery (Batesville, MS — 60 miles south) is the preeminent Plum Village
practice center in the Southeast US, commonly referenced as the Memphis-area retreat
destination. Live Eventbrite calendar for monthly Days of Mindfulness.

Centers included:
  - Memphis Zen Community (memphis_zen)
    Soto Zen (Soto lineage — founded 1998)
    3387 Walnut Grove Rd, Memphis TN 38111
    memphiszen.org · Weekly Sunday 5:00–6:30pm (in-person; website unreachable as of 2026-06)

  - Pema Karpo Meditation Center (pema_karpo_memphis)
    Nyingma Tibetan Buddhism (founded ~1990s; 11-acre campus)
    3921 Frayser Raleigh Rd, Memphis TN 38128
    pemakarpo.org · Sunday 11am–12:30pm (online/Zoom), Wed 7–8pm (online/Zoom)

  - Magnolia Grove Monastery (magnolia_grove_monastery)
    Plum Village / Thich Nhat Hanh lineage (fully ordained monastery)
    123 Towles Rd, Batesville MS 38606
    magnoliagrovemonastery.org · Monthly Days of Mindfulness (Sundays) via Eventbrite

Research notes (2026-06-16):
  - Memphis Zen Community: Active since 1998, Soto lineage. Sunday 5–6:30pm drop-in at
    3387 Walnut Grove Rd, Memphis TN 38111. Website (memphiszen.org) currently unreachable.
    Schedule confirmed via MeditationLy directory. Seed as recurring.
  - Pema Karpo Meditation Center: Nyingma Tibetan center on 11-acre campus in north Memphis.
    Online-primary: Sunday 11am–12:30pm via Zoom (all services online unless announced
    otherwise). Wednesday 7–8pm Sadhana of Shakyamuni Buddha via Shambhala Online. In-person
    events are irregular — communicated via email list. No website calendar.
  - Magnolia Grove Monastery: Fully-ordained Plum Village monastery (monks + nuns) in
    Batesville MS, ~60 miles south of Memphis. Monthly Sunday Days of Mindfulness (typically
    8:30am–2pm). Active Eventbrite organizer (ID: 10606160031) with events through Dec 2026.
    Also offers personal retreats and themed retreats. Key Southeast US Plum Village center.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "memphis_zen": Center(
        id="memphis_zen",
        name="Memphis Zen Community",
        url="https://memphiszen.org",
        address="3387 Walnut Grove Rd",
        city="Memphis",
        state="TN",
        zip_code="38111",
        lat=35.1249,
        lng=-90.0073,
        neighborhood="Midtown Memphis",
        tradition=Tradition.ZEN,
        notes=(
            "Memphis Zen Community is a Soto Zen group practicing at 3387 Walnut Grove Rd, "
            "Midtown Memphis. Weekly Sunday sits 5:00–6:30pm (in-person). Founded 1998. "
            "Website currently unreachable; schedule confirmed via meditation directories."
        ),
    ),
    "pema_karpo_memphis": Center(
        id="pema_karpo_memphis",
        name="Pema Karpo Meditation Center",
        url="https://pemakarpo.org",
        address="3921 Frayser Raleigh Rd",
        city="Memphis",
        state="TN",
        zip_code="38128",
        lat=35.2175,
        lng=-90.0183,
        neighborhood="Frayser",
        tradition=Tradition.TIBETAN,
        notes=(
            "Pema Karpo Meditation Center is a Nyingma Tibetan Buddhist center on an 11-acre "
            "campus in north Memphis (Frayser neighborhood). Offers weekly online services: "
            "Sunday 11am–12:30pm CT via Zoom and Wednesday 7–8pm Sadhana of Shakyamuni Buddha "
            "via Shambhala Online. In-person events are communicated via email list. "
            "Contact: pemakarpomeditation@gmail.com."
        ),
    ),
    "magnolia_grove_monastery": Center(
        id="magnolia_grove_monastery",
        name="Magnolia Grove Monastery",
        url="https://magnoliagrovemonastery.org",
        address="123 Towles Rd",
        city="Batesville",
        state="MS",
        zip_code="38606",
        lat=34.3186,
        lng=-89.9447,
        neighborhood="Batesville",
        tradition=Tradition.ZEN,
        notes=(
            "Magnolia Grove Monastery is a fully-ordained Plum Village monastery "
            "(Thich Nhat Hanh lineage) with both monks and nuns, located on a rural "
            "campus in Batesville, MS (~60 miles south of Memphis). The preeminent Plum "
            "Village practice center in the Southeast US. Monthly Sunday Days of Mindfulness "
            "(typically 8:30am–2pm) are free, registration required via Eventbrite. Also "
            "offers personal retreats and seasonal themed retreats. "
            "magnoliagrovemonastery.org · (662) 267-6437."
        ),
    ),
}

# Magnolia Grove Monastery — Eventbrite organizer ID: 10606160031
# Monthly Days of Mindfulness confirmed through December 2026.
EVENTBRITE_FEEDS = {
    "magnolia_grove_monastery": {
        "organizer_id": "10606160031",
        "filter_to_sits": False,  # Days of Mindfulness are the primary program — include all
    },
}

# No live iCal feeds available for Memphis proper — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
