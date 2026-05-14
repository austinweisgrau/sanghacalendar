"""
Ann Arbor, MI meditation center sources — Phase 3 expansion.

Ann Arbor (~120k population, home of University of Michigan) has a small but
established Buddhist scene anchored by three distinct centers.

iCal feeds:
  - Jewel Heart (Tibetan/Gelugpa): Google Calendar public ICS
    annarbor@jewelheart.org — active, weekly courses and special events.

Recurring sits (seeded in sangha-seed-recurring.js):
  - Insight Meditation Ann Arbor (IMAA) — Sun 10am in-person, Sat 10am online,
    Mon–Fri 7:30am online. 180 Little Lake Dr #1, Ann Arbor MI 48103.
  - Zen Buddhist Temple Ann Arbor — Sun 10am in-person.
    1214 Packard St, Ann Arbor MI 48104.
  - Jewel Heart — Tue 6pm free weekly meditation (in-person).
    1129 Oak Valley Dr, Ann Arbor MI 48108.

Research notes (2026-05-14):
  - Jewel Heart (jewelheart.org): Tibetan Buddhist (Gelugpa/Mahayana) center
    founded by Kyabje Gelek Rimpoche. Current director: Demo Rinpoche. International
    HQ at 1129 Oak Valley Drive, Ann Arbor MI 48108 (since 1988; 14th Dalai Lama
    taught here 2008). Active Google Calendar (annarbor@jewelheart.org): weekly courses
    (Tuesdays 6pm free community meditation, Sundays 9:30am White Tara guided meditation,
    Wednesdays periodic courses), monthly special events, retreats.
  - Insight Meditation Ann Arbor (insightmeditationannarbor.org): Theravada/Vipassana
    founded by Rodney Smith lineage. 180 Little Lake Dr Suite 1, Ann Arbor MI 48103
    (near Westgate Shopping Center, west side). Regular schedule: Sunday in-person
    meditation (10–11:15am, 45-min sit + dharma talk), Saturday online Zoom (10–11:30am),
    Mon–Fri morning online Zoom (7:30–8:00am). WordPress site, no Events Calendar plugin;
    no accessible iCal. Sits seeded as recurring.
  - Zen Buddhist Temple Ann Arbor (zenbuddhisttemple.org/annarbor): Korean Zen (Son
    Buddhism), Buddhist Society of Compassionate Wisdom (Samu Sunim lineage). Resident
    priests: Haju Sunim and Maum. 1214 Packard St, Ann Arbor MI 48104 (near UMich campus,
    Burns Park neighborhood). Sunday Public Service 10am (in-person + livestreamed). Also
    Recovery Dharma (Sundays noon, online) and 5-week Meditation Courses (Thursdays 6:30pm,
    periodic). Wix site, no iCal. Sunday 10am sit seeded as recurring.
  - Still Mountain (stillmountain.org): Tai Chi center, not a Buddhist center — skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "jewel_heart_ann_arbor": Center(
        id="jewel_heart_ann_arbor",
        name="Jewel Heart",
        url="https://www.jewelheart.org",
        address="1129 Oak Valley Drive",
        city="Ann Arbor",
        state="MI",
        zip_code="48108",
        lat=42.2209,
        lng=-83.6972,
        neighborhood="Southeast Ann Arbor",
        tradition=Tradition.TIBETAN,
        notes=(
            "Jewel Heart is a Tibetan Buddhist (Gelugpa/Mahayana) center founded by Kyabje "
            "Gelek Rimpoche and now led by resident director Demo Rinpoche. International "
            "headquarters at 1129 Oak Valley Drive, Ann Arbor — Gelek Rimpoche taught here "
            "from 1988; the 14th Dalai Lama offered teachings here in 2008. Regular public "
            "offerings include a free weekly Community Meditation (Tuesdays 6–6:45pm, "
            "in-person), Sunday programs (White Tara Guided Meditation 9:30–10:30am, onsite "
            "+ online), and periodic Wednesday courses. Special events, empowerments, and "
            "retreats offered throughout the year. All levels welcome; weekly sit is free."
        ),
    ),
    "insight_meditation_ann_arbor": Center(
        id="insight_meditation_ann_arbor",
        name="Insight Meditation Ann Arbor",
        url="https://insightmeditationannarbor.org",
        address="180 Little Lake Drive, Suite 1",
        city="Ann Arbor",
        state="MI",
        zip_code="48103",
        lat=42.2810,
        lng=-83.7912,
        neighborhood="West Ann Arbor (near Westgate)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Ann Arbor (IMAA) is a Theravada / Insight Meditation "
            "community offering drop-in sits for all levels. Regular schedule: Sunday "
            "in-person meditation (10–11:15am: 45-minute sit followed by dharma talk, "
            "at 180 Little Lake Drive Suite 1); Saturday online meditation via Zoom "
            "(10–11:30am); weekday morning sits Mon–Fri via Zoom (7:30–8:00am, with "
            "option to continue to 8:30am). Classes in Mindfulness-Based Stress "
            "Reduction (MBSR) and longer courses also offered. No experience required; "
            "free and donation-based."
        ),
    ),
    "zen_buddhist_temple_ann_arbor": Center(
        id="zen_buddhist_temple_ann_arbor",
        name="Zen Buddhist Temple — Ann Arbor",
        url="https://www.zenbuddhisttemple.org/annarbor",
        address="1214 Packard Street",
        city="Ann Arbor",
        state="MI",
        zip_code="48104",
        lat=42.2631,
        lng=-83.7423,
        neighborhood="Burns Park (near UMich campus)",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Buddhist Temple Ann Arbor is a Korean Zen (Son Buddhism) temple in "
            "the Burns Park neighborhood near the University of Michigan campus, part "
            "of the Buddhist Society of Compassionate Wisdom (founded by Samu Sunim). "
            "Resident priests: Haju Sunim and Maum. Public Sunday Service (10am, "
            "in-person + livestreamed): meditation, dharma talk, ceremonies. Recovery "
            "Dharma (Sundays noon, online) and periodic 5-week Meditation Courses "
            "(Thursdays 6:30–8:30pm) also offered. Daily practice for residents and "
            "members (6am + 6:30pm). Drop-in welcome for Sunday services. Free."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "jewel_heart_gcal": {
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "annarbor%40jewelheart.org/public/basic.ics"
        ),
        "center_id": "jewel_heart_ann_arbor",
        "filter_to_sits": True,
    },
}
