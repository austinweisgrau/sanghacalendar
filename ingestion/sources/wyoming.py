"""
Wyoming — Phase 3 expansion (heartbeat 121).

Wyoming (pop. ~580k) is one of the least densely populated states, but has a
small active Buddhist community concentrated in Jackson (Jackson Hole), Laramie,
and Casper.

Centers included:
  - teton_sangha
    Vipassana / Theravada (Spirit Rock / IMS lineage)
    HOME YOGA, 150 E Hansen St, Jackson WY 83001
    Monday 7:00–8:00pm in-person
    tetonsangha.org — no iCal; seeded as recurring.

  - snowflake_sangha_jackson
    Plum Village / Thich Nhat Hanh (Zen)
    Hansen Hall, St. John's Episcopal Church, 170 N Glenwood St, Jackson WY 83001
    Thursday 6:00–7:00pm in-person
    snowflakesangha.org — no iCal; seeded as recurring.

  - heruka_kadampa_laramie
    New Kadampa Tradition (NKT) / Tibetan Vajrayana
    Albany County Public Library, 310 S 8th St, Laramie WY 82070
    Tuesday 3:00–4:00pm in-person (satellite of Fort Collins Heruka KMC)
    LIVE iCal feed: meditationinwyoming.org/calendar/?ical=1

  - uu_casper_meditation
    Buddhist-led meditation (non-sectarian / mixed)
    UU Community of Casper, 1040 W 15th St, Casper WY 82604
    Friday 6:00–7:00pm in-person (Stuart Mackenzie, Buddhist-led)
    LIVE iCal feed: uucasper.org/events/?ical=1

Research notes (2026-11-10):
  - Teton Sangha: Vipassana / IMS-lineage group in Jackson. Weekly Monday sit,
    7:00–8:00pm at HOME YOGA (150 E Hansen St). 1st and 3rd Mondays include a
    dharma talk/discussion after 30 min sitting. Annual fall retreat. Very active
    website (tetonsangha.org). No iCal feed found (custom calendar software).
  - Snowflake Sangha: Plum Village / TNH affiliate in Jackson. Weekly Thursday
    sit, 6:00–7:00pm at Hansen Hall, St. John's Episcopal Church (170 N Glenwood
    St). Walking + sitting meditation + reading/discussion. Free.
    snowflakesangha.org.
  - Heruka KMC Laramie: NKT satellite of Fort Collins Heruka Kadampa MC. Tuesday
    3:00–4:00pm free meditation at Albany County Public Library (310 S 8th St,
    Large Meeting Room). Teacher: Kerrin Perniciaro. iCal feed confirmed at
    meditationinwyoming.org/calendar/?ical=1 (WordPress Events Calendar,
    text/calendar 200 OK).
  - UU Casper Meditation: Weekly Friday Buddhist-led meditation at Unitarian
    Universalist Community of Casper Sanctuary (1040 W 15th St). 6:00–7:00pm,
    one hour sitting + walking meditation, teacher Stuart Mackenzie (Buddhist).
    Beginners welcome, free. WordPress Events Calendar iCal confirmed:
    uucasper.org/events/?ical=1 (text/calendar 200 OK).
  - Laramie Shambhala Center (510 S 12th St): listed in directories but no
    active website or confirmed schedule found; deferred pending verification.
  - Jackson Teton Dharmata group: retreat-focused Dharmata Foundation affiliate;
    no regular weekly sit schedule confirmed; deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "teton_sangha": Center(
        id="teton_sangha",
        name="Teton Sangha",
        url="https://www.tetonsangha.org",
        address="150 E Hansen Ave",
        city="Jackson",
        state="WY",
        zip_code="83001",
        lat=43.4799,
        lng=-110.7626,
        neighborhood="Jackson (Jackson Hole)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Teton Sangha is a Vipassana / Theravada practice community in Jackson, WY, "
            "in the Spirit Rock / IMS lineage. Weekly sit at HOME YOGA (150 E Hansen Ave): "
            "Monday evenings 7:00–8:00pm. 1st and 3rd Mondays include a 20-minute "
            "dharma talk and discussion after 30 minutes of sitting; other Mondays are "
            "30 minutes of silent sitting. Annual fall multi-day retreat. Free / dana. "
            "Drop-in welcome. info@tetonsangha.org. tetonsangha.org."
        ),
    ),
    "snowflake_sangha_jackson": Center(
        id="snowflake_sangha_jackson",
        name="Snowflake Sangha",
        url="https://www.snowflakesangha.org",
        address="170 N Glenwood St",
        city="Jackson",
        state="WY",
        zip_code="83001",
        lat=43.4789,
        lng=-110.7638,
        neighborhood="Jackson (Jackson Hole)",
        tradition=Tradition.ZEN,
        notes=(
            "Snowflake Sangha is a Plum Village / Thich Nhat Hanh (TNH) lineage "
            "community in Jackson, WY. Weekly sit at Hansen Hall, St. John's Episcopal "
            "Church (170 N Glenwood St): Thursday evenings 6:00–7:00pm. Practice includes "
            "sitting and walking meditation plus a reading and discussion. Free, open to "
            "all backgrounds. snowflakesangha.org."
        ),
    ),
    "heruka_kadampa_laramie": Center(
        id="heruka_kadampa_laramie",
        name="Heruka Kadampa Meditation Center — Laramie",
        url="https://www.meditateinfortcollins.org/laramie/",
        address="310 S 8th St",
        city="Laramie",
        state="WY",
        zip_code="82070",
        lat=41.3081,
        lng=-105.5917,
        neighborhood="Downtown Laramie",
        tradition=Tradition.TIBETAN,
        notes=(
            "Heruka Kadampa Meditation Center (NKT Tibetan / Gelug) — Laramie satellite. "
            "Free meditations at the Albany County Public Library (310 S 8th St, Large "
            "Meeting Room): Tuesday afternoons 3:00–4:00pm. Instructor: Kerrin Perniciaro "
            "(resident teacher at the main Fort Collins center). No experience required; "
            "beginners welcome. Free of charge. Part of the same NKT community as Heruka "
            "KMC in Fort Collins and Cheyenne. (970) 798-0090. "
            "meditateinfortcollins.org/laramie/."
        ),
    ),
    "uu_casper_meditation": Center(
        id="uu_casper_meditation",
        name="UU Casper Buddhist Meditation",
        url="https://uucasper.org",
        address="1040 W 15th St",
        city="Casper",
        state="WY",
        zip_code="82604",
        lat=42.8609,
        lng=-106.3421,
        neighborhood="Casper",
        tradition=Tradition.THERAVADA,
        notes=(
            "Buddhist-led meditation at the Unitarian Universalist Community of Casper "
            "Sanctuary (1040 W 15th St). Friday evenings 6:00–7:00pm: one hour of "
            "sitting and walking meditation, led by Stuart Mackenzie (Buddhist). "
            "Beginners welcome; no experience needed. Free, open to all. "
            "uucasper.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "heruka_kadampa_laramie": {
        "url": "https://meditationinwyoming.org/calendar/?ical=1",
        "filter_to_sits": True,
    },
    "uu_casper_meditation": {
        "url": "https://uucasper.org/events/?ical=1",
        "filter_to_sits": True,
    },
}
