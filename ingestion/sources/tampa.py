"""
Tampa Bay, FL — Phase 3 expansion.

Tampa Bay has a modest but active Buddhist community spread across Tampa,
St. Petersburg, and Clearwater. Four centers anchor the practice scene.

Centers included:
  - Kadampa Meditation Center Tampa Bay (kmc_tampa_bay) — NKT Tibetan, Safety Harbor
    201 6th Ave S, Safety Harbor FL 34695
    Recurring sits: Sun 10am, Tue 10am, Thu 7pm
    Wix site — no accessible iCal; sits seeded as recurring.

  - Clear Water Zen Center (clear_water_zen) — Soto Zen, Clearwater
    2476 Nursery Rd, Clearwater FL 33764
    Recurring sits: Sun 9:30am, Mon 7pm, Wed 7pm (beginner), Fri 7pm
    Google Sites — no iCal; sits seeded as recurring.

  - Florida Community of Mindfulness (fcm_tampa) — Plum Village, Tampa
    6501 N Nebraska Ave, Tampa FL 33604
    Wild Apricot RSS at floridamindfulness.org/page-1861378/RSS
    Regular: Daily 7am Morning Meditation + Sunday 9:30am Meditation & Dharma Talk
    Teacher: Fred Eppsteiner; Thich Nhat Hanh lineage.

  - Shambhala Meditation Center of St. Petersburg (shambhala_stpete) — Shambhala, St. Pete
    5901 Haines Rd N, St. Petersburg FL 33714
    Recurring sits: Sun 10am community practice, Tue 7pm (online)
    WordPress dynamic — no accessible iCal; sits seeded as recurring.

Research notes (2026-05-17):
  - Shambhala St. Pete: dynamic WordPress site; FullCalendar JS-rendered. Cologne
    iCal server center ID unknown. Recurring sits seeded from website schedule.
    Sun 10am–noon extended sitting (in-person), Tue 7pm online contemplations.
    First Sunday monthly: 9am "Learn to Meditate" intro.
  - KMC Tampa Bay: Wix site (meditationintampabay.org). Main center at Safety Harbor;
    branch classes throughout Tampa Bay metro. 3 sit types: Sun 10am, Tue 10am, Thu 7pm.
    Tampa city branch (308 E 7th Ave) listed as CLOSED on Yelp — main center is Safety Harbor.
  - Clear Water Zen Center (clearwaterzencenter.org): Google Sites platform, no iCal.
    Founded 1980s by Ken Rosen. Non-sectarian Zen. Weekly schedule confirmed:
    Sun 9:30am–11:30am (formal zazen, dharma talk), Mon 7–8pm (open meditation),
    Wed 6:45pm (beginner class, starts 7pm), Fri 7–8pm (open meditation).
    Periodic Saturday zazenkai + mini sesshin.
  - FCM Tampa: Wild Apricot. RSS feed confirmed working at /page-1861378/RSS.
    Daily 7am Morning Meditation + Sunday 9:30am Meditation and Dharma Talk are
    the primary sitting events. Other offerings: Mindful Yoga, Qigong, Meditation
    in Recovery (filtered out by is_likely_sit).

  Skipped for now:
  - Florida Buddhist Vihara (Theravada, Brandon/Tampa): retreat-focused, unclear
    public sit schedule.
  - Brahma Kumaris Tampa: not a Buddhist center.
  - Samadhi Buddhist Meditation Center (St. Pete): small group, Wix site, Wed 7:30pm.
    Monitor for confirmed schedule + accessibility.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_tampa_bay": Center(
        id="kmc_tampa_bay",
        name="Kadampa Meditation Center Tampa Bay",
        url="https://meditationintampabay.org",
        address="201 6th Ave S",
        city="Safety Harbor",
        state="FL",
        zip_code="34695",
        lat=27.9869,
        lng=-82.6932,
        neighborhood="Safety Harbor",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Tampa Bay is a New Kadampa Tradition (NKT-IKBU) "
            "Tibetan Buddhist center in Safety Harbor, serving the greater Tampa Bay "
            "metro. Weekly drop-in classes include Sunday 'Meditations for World Peace' "
            "(10–11:15am), Tuesday General Program (10–11am), and Thursday General Program "
            "(7–8:15pm). All sessions include guided meditation and Buddhist teachings. "
            "Branch classes held throughout Tampa Bay. Free or by donation for new students; "
            "membership available. The center also hosts special events, retreats, "
            "and empowerments throughout the year."
        ),
    ),
    "clear_water_zen": Center(
        id="clear_water_zen",
        name="Clear Water Zen Center",
        url="https://www.clearwaterzencenter.org",
        address="2476 Nursery Rd",
        city="Clearwater",
        state="FL",
        zip_code="33764",
        lat=27.9328,
        lng=-82.7555,
        neighborhood="South Clearwater",
        tradition=Tradition.ZEN,
        notes=(
            "Clear Water Zen Center is a non-sectarian Zen meditation community in "
            "Clearwater, founded in the 1980s by Ken Rosen. The center offers multiple "
            "weekly sitting periods open to all: Sunday 9:30am–11:30am (formal zazen "
            "rounds with dharma talk), Monday 7–8pm (open meditation, three 20-min "
            "rounds), Wednesday 6:45pm (beginner class with instruction, starts 7pm), "
            "and Friday 7–8pm (open meditation). Periodic full-day zazenkai on Saturdays "
            "and multi-day mini sesshin several times per year. Drop-in welcome; no "
            "experience needed. Free; donations appreciated."
        ),
    ),
    "fcm_tampa": Center(
        id="fcm_tampa",
        name="Florida Community of Mindfulness",
        url="https://www.floridamindfulness.org",
        address="6501 N Nebraska Ave",
        city="Tampa",
        state="FL",
        zip_code="33604",
        lat=27.9987,
        lng=-82.4530,
        neighborhood="Seminole Heights",
        tradition=Tradition.THERAVADA,
        notes=(
            "The Florida Community of Mindfulness (FCM) is a contemplative community in "
            "the Plum Village tradition of Thich Nhat Hanh, led by teacher Fred Eppsteiner. "
            "Located in the Seminole Heights neighborhood of Tampa. Regular sitting practice "
            "includes daily Morning Meditation (7–8am, in-person and online) and Sunday "
            "Meditation and Dharma Talk (9:30–11:30am, in-person and online). Also hosts "
            "Mindful Yoga, Qigong, Meditation in Recovery, Days of Mindfulness, and "
            "longer retreats. Wake Up Tampa Bay (young adults 18–35) meets bi-monthly "
            "on Fridays. Open to all; sliding scale fees for special programs."
        ),
    ),
    "shambhala_stpete": Center(
        id="shambhala_stpete",
        name="Shambhala Meditation Center of St. Petersburg",
        url="https://stpetersburg.shambhala.org",
        address="5901 Haines Rd N",
        city="St. Petersburg",
        state="FL",
        zip_code="33714",
        lat=27.8284,
        lng=-82.6788,
        neighborhood="North St. Petersburg",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Center of St. Petersburg is one of five Shambhala "
            "Florida centers, following the Chögyam Trungpa Rinpoche lineage. Regular "
            "offerings include Sunday Community Practice (10am–noon, in-person extended "
            "sitting and walking meditation with instruction at 11am and discussion), "
            "and Tuesday Evening Contemplations (7–8pm, Zoom only). First Sunday monthly: "
            "'Learn to Meditate' intro class (9am–noon). Also hosts Heart of Recovery "
            "(Wednesdays), Pema Chodron Study Group (Mondays), and Shambhala Training "
            "weekends. Drop-in welcome; no experience required."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Wild Apricot RSS feeds
# ---------------------------------------------------------------------------

RSS_FEEDS = {
    "fcm_tampa": {
        "url": "https://www.floridamindfulness.org/page-1861378/RSS",
        "center_id": "fcm_tampa",
        # Keywords that identify meditation sits in the title
        "title_keywords": [
            "Morning Meditation",
            "Sunday Meditation",
            "Day of Mindfulness",
            "Meditation and Dharma",
        ],
        "filter_to_sits": True,
        "duration_min": 60,
    },
}
