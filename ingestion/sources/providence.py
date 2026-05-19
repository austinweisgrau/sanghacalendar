"""
Providence, RI — Phase 3 expansion.

Rhode Island has a small but serious practice community anchored by the
Providence Zen Center (Kwan Um School of Zen), one of the most active Korean
Zen centers in the US, founded by Seung Sahn. The city also has a Kadampa
center, two Insight Meditation communities, and the Plum Village–affiliated
Rhode Island Community of Mindfulness.

Centers included:
  - Providence Zen Center (pzc) — Korean Zen (Kwan Um School)
    99 Pound Road, Cumberland RI 02864 (~15 mi north of Providence)
    providencezen.org — founded by Seung Sahn Sunim
    Tockify ICS feed: https://tockify.com/api/feeds/ics/providence.zen.center
    Public programs: Sun 9:30am Dharma Program, Wed 6:15pm sit + chanting,
    West Side Zen Group (satellite). Drop-in daily sits for residents.

  - Atisha Kadampa Buddhist Center / AKBC (akbc_providence) — NKT Tibetan
    339 Ives St, Providence RI 02906 (Fox Point)
    meditationinrhodeisland.org
    Recurring: Sun 11am, Mon 12:15pm, Thu 12:15pm, Wed 6pm
    No iCal (WordPress Flywheel, JS-rendered calendar); recurring sits seeded.

  - Insight Meditation Community of Providence / IMCP (imcp) — Theravada
    354 Broadway, Providence RI 02909
    insightprovidence.org
    Recurring: 1st & 3rd Thursday, time ~7pm
    No iCal; sits seeded with week_of_month.

  - Insight Meditation Sangha Providence (insight_pvd) — Vipassana
    27 Sims Avenue, Providence RI 02909
    insightpvd.com
    Recurring: Wednesday evenings
    No iCal; sits seeded.

  - RI Community of Mindfulness / Radiant Bell Sangha (ricm_radiant_bell) — Plum Village
    Bell Street Chapel, 5 Bell Street, Providence RI 02909
    mindfulnessri.org
    Recurring: Saturday mornings 8am–9:30am
    No iCal; sits seeded.

Research notes (2026-05-19):
  - Providence Zen Center Tockify ICS verified working.
    Feed URL: https://tockify.com/api/feeds/ics/providence.zen.center
    Events include: Sunday Dharma Program, Wed Community Dinner + Sit,
    West Side Zen Group (satellite in Providence proper), Online Zen Practice,
    Kido Circles. filter_to_sits=True passes most with uncertain flag; LLM
    enrichment classifies correctly.
  - Shambhala Providence: confirmed CLOSED (Facebook page confirms; center
    no longer active). Skip.
  - PZC is in Cumberland RI (~15 mi north of Providence) but is universally
    known as the Providence metro's main Zen center. Listed as city="Cumberland"
    with both Providence and Cumberland added to RI state filter.
  - AKBC Wix/Flywheel calendar has no ICS export. Recurring sits seeded.
  - IMCP meets only 1st and 3rd Thursday — using week_of_month in seed script.
  - Insight PVD (insightpvd.com): small community group; Wednesday sits.
  - RICM Radiant Bell Sangha: Plum Village TNH lineage, Sat mornings at Bell
    Street Chapel. Hope Street Sangha also exists (1st & 4th Wed) — skipping
    to avoid double-counting with Insight PVD on Wed.
  - Wat Thormikaram (177 Hanover St): Khmer Theravada, community-focused,
    no public drop-in sit program. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "pzc": Center(
        id="pzc",
        name="Providence Zen Center",
        url="https://providencezen.org",
        address="99 Pound Road",
        city="Cumberland",
        state="RI",
        zip_code="02864",
        lat=41.9728,
        lng=-71.4300,
        neighborhood="Cumberland",
        tradition=Tradition.ZEN,
        notes=(
            "Providence Zen Center is the founding temple of the Kwan Um School of Zen "
            "in the West, established by Korean master Seung Sahn Sunim in 1972. It is one "
            "of the most active residential Zen centers in North America, hosting daily "
            "formal practice (108 bows, chanting, zazen) alongside public programs. The "
            "Sunday Dharma Program (9–11 AM) includes beginner meditation instruction, "
            "sitting, walking, and a Dharma talk — drop-ins welcome. Wednesday evenings "
            "feature a community dinner followed by meditation instruction and chanting "
            "(7 PM sit). The West Side Zen Group meets in Providence proper on Fridays. "
            "Residential students sit daily; intensive retreats (Kyol Che, YMJJ) are "
            "offered throughout the year. Located in Cumberland, RI, about 15 miles north "
            "of downtown Providence."
        ),
    ),
    "akbc_providence": Center(
        id="akbc_providence",
        name="Atisha Kadampa Buddhist Center",
        url="https://meditationinrhodeisland.org",
        address="339 Ives Street",
        city="Providence",
        state="RI",
        zip_code="02906",
        lat=41.8198,
        lng=-71.3955,
        neighborhood="Fox Point",
        tradition=Tradition.TIBETAN,
        notes=(
            "Atisha Kadampa Buddhist Center (AKBC) is Rhode Island's New Kadampa Tradition "
            "(NKT) center, offering modern Tibetan Buddhist teachings in the Fox Point "
            "neighborhood of Providence. Weekly classes include a Sunday morning program "
            "(11 AM–12:15 PM), lunchtime sits on Mondays and Thursdays (12:15–12:45 PM), "
            "and a Wednesday evening class (6–7:30 PM). All classes combine guided "
            "meditation with Buddhist teachings in the Kadampa style. Beginners welcome. "
            "AKBC also runs a satellite group in Little Compton, RI."
        ),
    ),
    "imcp": Center(
        id="imcp",
        name="Insight Meditation Community of Providence",
        url="https://www.insightprovidence.org",
        address="354 Broadway",
        city="Providence",
        state="RI",
        zip_code="02909",
        lat=41.8220,
        lng=-71.4272,
        neighborhood="Broadway / West End",
        tradition=Tradition.THERAVADA,
        notes=(
            "The Insight Meditation Community of Providence (IMCP) is a small, "
            "practitioner-led Vipassana sangha meeting on the 1st and 3rd Thursday of "
            "each month. Evenings include 40 minutes of silent sitting, a Dharma reading, "
            "and a discussion/sharing circle. Rooted in the Theravada/Insight tradition, "
            "affiliated with the Insight Meditation Society and the Open Sangha Foundation. "
            "Drop-in, donation-based. Contact through insightprovidence.org."
        ),
    ),
    "insight_pvd": Center(
        id="insight_pvd",
        name="Insight Meditation Sangha Providence",
        url="https://www.insightpvd.com",
        address="27 Sims Avenue",
        city="Providence",
        state="RI",
        zip_code="02909",
        lat=41.8164,
        lng=-71.4256,
        neighborhood="West End",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Sangha Providence (insightpvd.com) is a Vipassana "
            "community in Providence's West End offering weekly Wednesday evening "
            "meditation. Sitting practice in the Insight/Theravada tradition; community "
            "discussion and dharma study also offered. Drop-in friendly, donation-based. "
            "Also holds periodic retreats and practice groups."
        ),
    ),
    "ricm_radiant_bell": Center(
        id="ricm_radiant_bell",
        name="RI Community of Mindfulness – Radiant Bell Sangha",
        url="https://www.mindfulnessri.org",
        address="5 Bell Street",
        city="Providence",
        state="RI",
        zip_code="02909",
        lat=41.8248,
        lng=-71.4290,
        neighborhood="College Hill / Wayland Square",
        tradition=Tradition.ZEN,
        notes=(
            "The Radiant Bell Sangha is part of the Rhode Island Community of Mindfulness "
            "(RICM), a network of Plum Village–tradition sanghas in the state inspired by "
            "Thich Nhat Hanh. Saturday morning gatherings (8–9:30 or 10 AM) at Bell "
            "Street Chapel in Providence include sitting meditation, walking meditation, "
            "and a Dharma talk or reading. Free and open to everyone; beginners welcome. "
            "RICM also hosts the Hope Street Sangha (1st & 4th Wednesdays) and other "
            "regional groups across Rhode Island."
        ),
    ),
}

# Providence Zen Center — Tockify ICS feed (verified 2026-05-19)
ICAL_FEEDS = {
    "pzc": {
        "url": "https://tockify.com/api/feeds/ics/providence.zen.center",
        "filter_to_sits": True,
    },
}
