"""
Portland, ME — Phase 3 expansion.

Portland is Maine's largest city (~70k city, ~550k metro) and cultural hub. Its
progressive, college-town character supports a small but active dharma scene spanning
Theravada Insight, Tibetan (Shambhala and Kagyu), Triratna, and Plum Village lineages.
Maine has no other significant Buddhist metro, making Portland the state's sole entry.

Centers included:
  - Portland Shambhala Meditation Center (portland_shambhala_me) — Tibetan (Shambhala)
    81 Oak St, Portland ME 04101. portland.shambhala.org
    Tue 7–8:30pm weekly open sitting + 3rd Sat 9–11:30am + Sun 9–10am.
    Shambhala International (Trungpa lineage). iCal 403 (Cloudflare); seeded.

  - Nagaloka Buddhist Center (nagaloka_portland) — Other (Triratna)
    1 Forest Ave, 2nd floor, Portland ME 04101. nagalokabuddhistcenter.org
    Sun 8:30–10am in-person + Mon 6:30–8pm in-person. Wix site, no iCal; seeded.
    Triratna Buddhist Community (formerly Friends of the Western Buddhist Order).
    Founded 2002.

  - Open Door Meditation Community (open_door_portland) — Theravada (Insight)
    160 Presumpscot St, Unit 2D, Portland ME 04103. opendoorportland.org
    Sun 9–10am in-person + Wed 5:30–6:45pm in-person. Insight / Vipassana lineage.
    Also Tue 6:30–8pm and daily 6–6:45am Zoom sits. Squarespace site, no iCal; seeded.

  - Vajra Vidya Portland (vajra_vidya_portland) — Tibetan (Karma Kagyu)
    159 State St, Portland ME 04101. portlandmainebuddhism.org
    Sun 9–10am open meditation ("best introduction," open to everyone).
    Karma Kagyu lineage, Khenchen Thrangu Rinpoche founder. No iCal; seeded.

  - Peaceful Harbor Sangha (peaceful_harbor_sangha_me) — Other (Plum Village)
    160 Presumpscot St, Portland ME 04103. peacefulharborsangha.org
    Sun 6:30–8pm in-person. Thich Nhat Hanh / Plum Village tradition. Lay-led.
    Contact: Peter Eglinton, peglinton@protonmail.com. No iCal; seeded.

Research notes (2026-10-22):
  - Portland Shambhala: shambhala-koeln.de feed returns 403 (Cloudflare). Three core
    sits seeded: Tuesday evening open sitting (most reliable/weekly), 3rd Saturday
    community morning, and Sunday community meditation.
  - Nagaloka: Wix site has no iCal. Founded 2002, part of Triratna Community (UK-based
    movement founded by Sangharakshita). Address confirmed via Yelp (updated March 2026).
  - Open Door: Squarespace site (opendoorportland.org). Monday sit currently on hiatus;
    seeded Sunday + Wednesday in-person sits. 160 Presumpscot address confirmed.
  - Vajra Vidya Portland: Karma Kagyu / Thrangu Rinpoche lineage (Shambhala-adjacent
    but distinct — not Shambhala Int'l). Sunday morning open session is the public entry
    point; Mon/Wed study groups require prior training. Live event calendar but no iCal.
  - Peaceful Harbor Sangha: Plum Village lay community, meets at 160 Presumpscot (same
    building as Open Door). Sunday evenings. Contact: Peter Eglinton.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "portland_shambhala_me": Center(
        id="portland_shambhala_me",
        name="Portland Shambhala Meditation Center",
        url="https://portland.shambhala.org",
        address="81 Oak Street",
        city="Portland",
        state="ME",
        zip_code="04101",
        lat=43.6570,
        lng=-70.2578,
        neighborhood="West End, Portland",
        tradition=Tradition.TIBETAN,
        notes=(
            "Portland Shambhala Meditation Center is Maine's Shambhala community, "
            "practicing in the Chögyam Trungpa Rinpoche lineage. Located at 81 Oak "
            "Street in Portland's West End. Weekly programs include Tuesday Evening "
            "Meditation (7–8:30pm), Sunday Community Meditation (9–10am), and 3rd "
            "Saturday Open Community Meditation (9–11:30am). Weekday morning "
            "meditation on Mondays and Fridays (8–9am). Shambhala Training programs, "
            "Poetry Pocket evenings (4th Tue), and dharma talks offered throughout "
            "the year. portland.shambhala.org."
        ),
    ),
    "nagaloka_portland": Center(
        id="nagaloka_portland",
        name="Nagaloka Buddhist Center",
        url="https://www.nagalokabuddhistcenter.org",
        address="1 Forest Avenue, 2nd Floor",
        city="Portland",
        state="ME",
        zip_code="04101",
        lat=43.6573,
        lng=-70.2603,
        neighborhood="Downtown Portland",
        tradition=Tradition.OTHER,
        notes=(
            "Nagaloka Buddhist Center is part of the Triratna Buddhist Community — "
            "a worldwide movement (formerly Friends of the Western Buddhist Order) "
            "founded by Sangharakshita in the UK, emphasizing lay practice and "
            "accessible dharma. Located on the 2nd floor of 1 Forest Avenue in "
            "downtown Portland (elevator available). Founded in 2002. Sunday Morning "
            "Meditation (8:30–10am in-person): guided meditation, dharma talk, and "
            "community tea. Monday Night Meditation (6:30–8pm in-person): sitting "
            "practice, study, and discussion. Wednesday Sangha Nights on Zoom "
            "(6:30–8pm). All backgrounds welcome; no experience needed. "
            "(207) 774-1545. nagalokabuddhistcenter.org."
        ),
    ),
    "open_door_portland": Center(
        id="open_door_portland",
        name="Open Door Meditation Community",
        url="https://www.opendoorportland.org",
        address="160 Presumpscot Street, Unit 2D",
        city="Portland",
        state="ME",
        zip_code="04103",
        lat=43.6770,
        lng=-70.2495,
        neighborhood="East Deering, Portland",
        tradition=Tradition.THERAVADA,
        notes=(
            "Open Door Meditation Community is southern Maine's Insight Meditation "
            "sangha — a welcoming, inclusive community in the Theravada/Vipassana "
            "tradition. Located at 160 Presumpscot Street, Unit 2D (East Deering "
            "neighborhood, Portland). In-person sessions: Sunday Community Sit "
            "(9–10am) and Wednesday Evening Meditation (5:30–6:45pm). Also offers "
            "Tuesday evening Zoom (6:30–8pm) and daily early-morning Zoom sit "
            "(6–6:45am). Daylong and multi-day retreats, BIPOC Circle, Sutta Study, "
            "and Yoga programming offered throughout the year. Dharma teachers: "
            "Amy Bird, Susa Talan, Lynn Teo, Adam Pepi. All experience levels "
            "welcome; sliding-scale dana. opendoorportland.org."
        ),
    ),
    "vajra_vidya_portland": Center(
        id="vajra_vidya_portland",
        name="Vajra Vidya Portland",
        url="https://portlandmainebuddhism.org",
        address="159 State Street",
        city="Portland",
        state="ME",
        zip_code="04101",
        lat=43.6631,
        lng=-70.2640,
        neighborhood="West End, Portland",
        tradition=Tradition.TIBETAN,
        notes=(
            "Vajra Vidya Portland is a Tibetan Buddhist center in the Karma Kagyu "
            "lineage, founded by Khenchen Thrangu Rinpoche. Located at 159 State "
            "Street in Portland's West End. The Sunday Morning Open Meditation "
            "(9–10am) is open to everyone and the best introduction to the community "
            "— includes sitting meditation with a stretch break, prayers in English, "
            "and tea. Advanced study groups meet Monday evenings (Hinayana/Mahayana "
            "Study Group, 6:30–8pm) and Wednesday evenings (Three-Yana Study Group, "
            "6:30–8:15pm, for those who have taken refuge). Medicine Buddha practice "
            "1st Tuesday 9am and 3rd Sunday 10am. info@portlandmainebuddhism.org. "
            "portlandmainebuddhism.org."
        ),
    ),
    "peaceful_harbor_sangha_me": Center(
        id="peaceful_harbor_sangha_me",
        name="Peaceful Harbor Sangha",
        url="https://www.peacefulharborsangha.org",
        address="160 Presumpscot Street",
        city="Portland",
        state="ME",
        zip_code="04103",
        lat=43.6770,
        lng=-70.2495,
        neighborhood="East Deering, Portland",
        tradition=Tradition.OTHER,
        notes=(
            "Peaceful Harbor Sangha is a Plum Village / Thich Nhat Hanh community "
            "meeting in Portland, Maine. Practices in the tradition of mindful living "
            "emphasizing understanding, loving-kindness, sitting and walking "
            "meditation, and study of Buddhist teachings. Meets Sunday evenings "
            "6:30–8pm in person at 160 Presumpscot Street, Portland. Lay-led; "
            "all backgrounds welcome. Contact: Peter Eglinton, "
            "peglinton@protonmail.com. peacefulharborsangha.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
