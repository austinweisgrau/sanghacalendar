"""
Honolulu, HI — Phase 3 expansion.

Hawaii has one of the highest Buddhist populations per capita in the US,
rooted in Japanese American heritage (Jodo Shinshu, Soto Zen) plus a
growing Vipassana and Tibetan community.

Centers included:
  - Honolulu Diamond Sangha (diamond_sangha_honolulu) — Soto/Rinzai Zen
    2747 Waiomao Road, Palolo, Honolulu HI 96816
    diamondsangha.org — Robert Aitken Roshi lineage
    Recurring: Mon–Fri 5:30am, Wed 7pm, Sun 9am
    No iCal — static calendar PDF; recurring sits seeded.

  - Soto Mission of Hawaii / Shoboji (soto_mission_honolulu) — Soto Zen
    1708 Nuuanu Avenue, Honolulu HI 96817
    sotomission.org — Soto school Hawaii
    Recurring: Mon/Wed/Fri 6:30am, Sun 9:30am
    Explicitly drop-in: "no reservation required"
    No iCal; sits seeded.

  - Bodhi Tree Dharma Center (bodhi_tree_honolulu) — Multi-tradition
    654A N. Judd Street, Honolulu HI 96817
    bodhitreehawaii.com — Vipassana / Plum Village / Mindfulness
    Recurring: Mon 6:30pm (Vipassana), Tue 6:30pm (Plum Village),
               Wed 6pm (Stillness), Sat 9am (Guided Vipassana)
    No iCal; calendar managed via Meetup. Sits seeded.

  - Aloha Sangha (aloha_sangha_honolulu) — Theravada / Insight
    2439 Holomua Place, Palolo Valley, Honolulu HI 96816
    alohasangha.com — active since 1998
    Recurring: Thu 6pm
    No iCal; sits seeded.

Research notes (2026-05-18):
  - Daihonzan Chozen-ji (3565 Kalihi St): Rinzai Zen, appointment-only,
    no drop-in visitors. Skip.
  - Hawaii Kadhampa Buddhist Association (Waipahu, ~20 mi west): different
    Kadhampa lineage (not NKT). Sat 10am — too far from Honolulu core.
  - Kagyu Thegchen Ling (26 Gartley Pl): stale events page (2023). Deferred.
  - Honolulu Shambhala: no active center found.
  - Insight Meditation Hawaii: Big Island based; Honolulu sits are Zoom-only.
  - KMC Hawaii: no NKT center found in Hawaii.
  - Buddhist Study Center (1436 University Ave): Shin Buddhism (Jodo Shinshu)
    — devotional/educational, not meditation-focused. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "diamond_sangha_honolulu": Center(
        id="diamond_sangha_honolulu",
        name="Honolulu Diamond Sangha",
        url="https://www.diamondsangha.org",
        address="2747 Waiomao Road",
        city="Honolulu",
        state="HI",
        zip_code="96816",
        lat=21.3033,
        lng=-157.8018,
        neighborhood="Palolo",
        tradition=Tradition.ZEN,
        notes=(
            "Honolulu Diamond Sangha (Ko Ko An Zendo) is one of the most historically "
            "significant Zen communities in Hawaii, founded in the lineage of Robert Aitken "
            "Roshi — a founder of engaged Buddhism in the West and co-founder of the "
            "international Diamond Sangha network. Situated in Palolo Valley, the zendo "
            "offers early morning zazen Mon–Fri, evening sitting on Wednesdays, and Sunday "
            "morning practice. Newcomers attend a one-time orientation (1st Saturday); "
            "regular students sit freely thereafter."
        ),
    ),
    "soto_mission_honolulu": Center(
        id="soto_mission_honolulu",
        name="Soto Mission of Hawaii",
        url="https://www.sotomission.org",
        address="1708 Nuuanu Avenue",
        city="Honolulu",
        state="HI",
        zip_code="96817",
        lat=21.3219,
        lng=-157.8431,
        neighborhood="Nuuanu",
        tradition=Tradition.ZEN,
        notes=(
            "Soto Mission of Hawaii (Shoboji) is a Soto Zen temple on Nuuanu Avenue in "
            "downtown Honolulu. One of the oldest Japanese-lineage Zen communities in Hawaii. "
            "Morning zazen is explicitly open to the public on Mondays, Wednesdays, and Fridays "
            "at 6:30 AM — no reservation required, just arrive five minutes early in comfortable "
            "clothes. Free (donations appreciated). Sunday service at 9:30 AM. Welcoming to "
            "complete beginners."
        ),
    ),
    "bodhi_tree_honolulu": Center(
        id="bodhi_tree_honolulu",
        name="Bodhi Tree Dharma Center",
        url="https://www.bodhitreehawaii.com",
        address="654A N. Judd Street",
        city="Honolulu",
        state="HI",
        zip_code="96817",
        lat=21.3179,
        lng=-157.8443,
        neighborhood="Palama",
        tradition=Tradition.THERAVADA,
        notes=(
            "Bodhi Tree Dharma Center is a multi-tradition meditation hub in Honolulu's "
            "Palama neighborhood, hosting several regular sanghas including Vipassana "
            "meditation, the Honolulu Mindfulness Community (Plum Village / Thich Nhat Hanh "
            "lineage), and a Stillness & Awakenings practice group. Classes run Monday through "
            "Saturday. Donation-based, beginner-friendly. The Honolulu Mindfulness Community "
            "(HMC) meets here most Tuesday evenings."
        ),
    ),
    "aloha_sangha_honolulu": Center(
        id="aloha_sangha_honolulu",
        name="Aloha Sangha",
        url="https://www.alohasangha.com",
        address="2439 Holomua Place",
        city="Honolulu",
        state="HI",
        zip_code="96816",
        lat=21.2989,
        lng=-157.7997,
        neighborhood="Palolo Valley",
        tradition=Tradition.THERAVADA,
        notes=(
            "Aloha Sangha is a small, donation-based Theravada / Insight Meditation community "
            "in Palolo Valley, operating since 1998. Thursday evening sits (6–7:30 PM) combine "
            "qigong, two 25-minute seated sessions, a short dharma talk, and Q&A. "
            "Beginner-friendly; no meditation experience required. Located in a residential "
            "setting in upper Palolo Valley — street parking limited, walking from 10th Ave "
            "recommended."
        ),
    ),
}

# No live iCal feeds — all Honolulu centers use recurring sit seeding
ICAL_FEEDS = {}
