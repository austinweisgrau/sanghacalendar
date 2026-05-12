"""
Las Vegas, NV meditation center sources — Phase 3 expansion.

iCal feeds:
  None — all Las Vegas centers use platforms without accessible iCal feeds
  (Bravesites, static HTML, diamondway.org network site).

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - Chaiya Meditation Monastery — daily sits: 9am, 2pm, 5pm (Mon–Sun)
    7925 Virtue Ct, Las Vegas, NV 89113 (Enterprise/Southwest LV).
    Theravada (Burmese lineage). Free, drop-in. Also available on Zoom.
  - Zen Center of Las Vegas — Sunday 1pm drop-in (Kwan Um Zen school)
    7925 Virtue Ct, Las Vegas, NV 89113 (same campus as Chaiya).
    Teacher: Zen Master Ji Haeng. Also 1st Sunday noon Beginners Intro.
  - Diamond Way Buddhist Center Las Vegas — Tuesday 7pm weekly
    3743 N Rosecrest Circle, Las Vegas, NV 89121.
    Karma Kagyu Tibetan (Lama Ole Nydahl). Drop-in welcome.
  - Nevada Buddhist Temple — Wednesday 7pm in-person + daily 7:30pm online
    2040 Abels Lane, North Las Vegas, NV 89115.
    Theravada, Sri Lankan lineage. Resident monk: Bhante Deepananda.

Research notes (2026-05-12):
  - Chaiya (chaiyacmm.org): Bravesites platform — no iCal. Very active daily program;
    4 daily sessions (9am, 11am, 2pm, 5pm). Seeded 3 representative times.
  - Zen Center LV (zenlasvegas.com): static HTML schedule, no feed. Same address as Chaiya.
    Kwan Um School of Zen, Teacher: Zen Master Ji Haeng. Sun 1pm primary sit.
  - Diamond Way LV (diamondway.org/lasvegas/): no iCal. Tue 7pm weekly + 1st Tue Open House.
  - Nevada Buddhist Vihara (nbvlv.org): WordPress/Astra shell, no Events Calendar plugin.
    Wed 7pm in-person meditation, daily 7:30pm online chanting + meditation (except Wed/Fri).
  - Kadampa LV (meditationinlasvegas.org): site redirects to Arizona IKRC — appears CLOSED.
  - Las Vegas Buddhist Sangha (lvbs.org): Jodo Shinshu / Pure Land devotional tradition — skip.
  - Bhodhiyana Meditation Center (bhodhiyana.org): website offline — skip for now.
  - Lohan Spiritual Center (lvlohans.org): syncretic (Chan/Tibetan/Taoist/Native American) —
    associated with Shaolin martial arts school. Complex tradition classification; deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "chaiya_las_vegas": Center(
        id="chaiya_las_vegas",
        name="Chaiya Meditation Monastery",
        url="https://chaiyacmm.org",
        address="7925 Virtue Ct",
        city="Las Vegas",
        state="NV",
        zip_code="89113",
        lat=36.0602,
        lng=-115.2246,
        neighborhood="Enterprise / Southwest Las Vegas",
        tradition=Tradition.THERAVADA,
        notes=(
            "Chaiya Meditation Monastery (CMM) is a Theravada Buddhist monastery in the "
            "Enterprise area of southwest Las Vegas, founded in the Burmese Theravada "
            "tradition. One of the most active Buddhist centers in the Las Vegas valley, "
            "offering four daily meditation sessions open to the public: 9–10 AM, "
            "11 AM–12:15 PM, 2–3 PM, and 5–6:15 PM. All sessions are free and open to "
            "beginners; no experience required. Also available on Zoom (ID: 568 279 3041, "
            "passcode: Cmm45678). Special programs include Vesak, Vassa (Rains Retreat), "
            "and group ordinations."
        ),
    ),
    "zen_center_las_vegas": Center(
        id="zen_center_las_vegas",
        name="Zen Center of Las Vegas",
        url="https://zenlasvegas.com",
        address="7925 Virtue Ct",
        city="Las Vegas",
        state="NV",
        zip_code="89113",
        lat=36.0602,
        lng=-115.2246,
        neighborhood="Enterprise / Southwest Las Vegas",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Center of Las Vegas is a Korean Zen community in the Kwan Um School of Zen, "
            "the lineage of Zen Master Seung Sahn. Located on the same campus as Chaiya "
            "Meditation Monastery in southwest Las Vegas. Teacher: Zen Master Ji Haeng. "
            "Weekly Sunday practice at 1 PM — all levels welcome, drop-in. First Sunday of "
            "each month includes a free Beginners Introduction at noon. "
            "Donations appreciated but not required."
        ),
    ),
    "diamond_way_las_vegas": Center(
        id="diamond_way_las_vegas",
        name="Diamond Way Buddhist Center Las Vegas",
        url="https://diamondway.org/lasvegas/",
        address="3743 N Rosecrest Circle",
        city="Las Vegas",
        state="NV",
        zip_code="89121",
        lat=36.1448,
        lng=-115.0803,
        neighborhood="East Las Vegas",
        tradition=Tradition.TIBETAN,
        notes=(
            "Diamond Way Buddhist Center Las Vegas is a Tibetan Buddhist center in the "
            "Karma Kagyu lineage of Lama Ole Nydahl. Located in east Las Vegas. Offers a "
            "weekly public meditation every Tuesday at 7 PM — no prior experience required, "
            "drop-in welcome. First Tuesday of each month is a free Open House with an "
            "introduction to Buddhism and meditation. Part of the global Diamond Way "
            "Buddhist network with 600+ centers worldwide."
        ),
    ),
    "nevada_buddhist_temple": Center(
        id="nevada_buddhist_temple",
        name="Nevada Buddhist Temple",
        url="https://www.nevadabuddhisttemple.org",
        address="2040 Abels Lane",
        city="North Las Vegas",
        state="NV",
        zip_code="89115",
        lat=36.2103,
        lng=-115.1214,
        neighborhood="North Las Vegas",
        tradition=Tradition.THERAVADA,
        notes=(
            "Nevada Buddhist Temple is a Sri Lankan Theravada Buddhist temple in North Las "
            "Vegas, with resident monk Bhante Deepananda. Offers weekly Wednesday Evening "
            "Meditation (7–8 PM in-person) and daily online meditation and chanting via "
            "Zoom (7:30 PM, except Wednesday and Friday). Monthly 'Meditation with a Monk' "
            "sessions and traditional observances including Vesak, Poson, and Kathina. "
            "All programs are free and open to the public."
        ),
    ),
}

# No iCal feeds available for any Las Vegas centers
ICAL_FEEDS = {}
