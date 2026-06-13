"""
Lexington, Kentucky — Phase 3 expansion (heartbeat 78).

Lexington (pop. ~325k; metro ~530k) is Kentucky's second-largest city, home to the
University of Kentucky. The Buddhist scene is modest but spans multiple traditions,
anchored by a Shambhala center (with working iCal feed) and several small sitting groups.

Centers included:
  - Lexington Shambhala Meditation Center (shambhala_lexington)
    Tibetan / Shambhala (Kagyu-Nyingma lineage)
    305 W Maxwell Street, Lexington KY 40508
    lexington.shambhala.org · Shambhala iCal center=193 (verified working)
    Sat 10am Café Shambhala + Tue 6:30pm Tune In sits

  - Lexington Zen Center (lexington_zen)
    Zen (Korean Kwan Um / Dae Gak lineage — Furnace Mountain)
    649 Price Avenue, Lexington KY 40508 (Quaker Meetinghouse)
    lexingtonzencenter.org · First Sunday monthly 2pm in-person
    No iCal — seeded as recurring.

  - Bluegrass Zen (bluegrass_zen_lexington)
    Zen (Chan / Pacific Zen Institute — David Parks, Roshi)
    3564 Clays Mill Road, Lexington KY 40503 (UUCL)
    bluegrasszen.org · Thursday 6:30pm in-person
    No iCal — seeded as recurring.

  - UUCL Sunday Sangha (uucl_sunday_sangha_lexington)
    Other / Interfaith (TNH/Plum Village influenced)
    3564 Clays Mill Road, Lexington KY 40503 (UUCL)
    sites.google.com/uucl.org/sundaysangha · Sunday 9am hybrid
    No iCal — seeded as recurring.

Research notes (2026-06-13):
  - Lexington Shambhala: active center at 305 W Maxwell St (near UK campus). Offers
    Café Shambhala Saturdays 10am–noon (sitting + dharma reading + discussion +
    newcomer instruction) and Tuesday Tune In (6pm/6:30pm/7pm staggered 30-min sitting
    blocks, free instruction). The shambhala-koeln.de iCal feed (center=193) verified
    live returning valid VCALENDAR data as of 2026-06-13. Timezone America/Kentucky/Louisville.
  - Lexington Zen Center: Korean/American Chogye lineage, student community of Zen Master
    Dae Gak (Furnace Mountain Retreat Center, Clay City KY). Meets first Sunday of each
    month at 2pm at Quaker Meetinghouse, 649 Price Ave — two 25-min sits with walking
    meditation between. All other Sundays Zoom only. Small community; email before visiting.
  - Bluegrass Zen: Chan lineage affiliated with Pacific Zen Institute, teacher Rev. David
    Parks, Roshi (based in Waco KY). Thursday evenings 6:30pm at UUCL Purple Room, 3564
    Clays Mill Rd. Also has a Berea location (Mondays 6:30pm). Open to all.
  - UUCL Sunday Sangha: TNH/Plum Village-influenced interfaith group, meets at Unitarian
    Universalist Church of Lexington. Sundays 9–10:45am: silent sit 9–9:30am (in-person
    only), break, then hybrid group discussion 9:45–10:45am via Google Meet. Contact:
    sangha@uucl.org. Separate from Bluegrass Zen which meets Thursdays at the same venue.
  - Lexington Nichiren Buddhist Community: very small home group, no public calendar — skip.
  - No Kadampa (NKT) center in Lexington; nearest is Louisville.
  - Shambhala Louisville: not in Shambhala directory, appears defunct.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_lexington": Center(
        id="shambhala_lexington",
        name="Lexington Shambhala Meditation Center",
        url="https://lexington.shambhala.org",
        address="305 W Maxwell Street",
        city="Lexington",
        state="KY",
        zip_code="40508",
        lat=38.0413,
        lng=-84.5043,
        neighborhood="University / Downtown",
        tradition=Tradition.TIBETAN,
        notes=(
            "Lexington Shambhala Meditation Center is a community in the Kagyu-Nyingma "
            "lineage founded by Chögyam Trungpa Rinpoche and led by Sakyong Mipham "
            "Rinpoche. Located at 305 W Maxwell Street near the University of Kentucky "
            "campus. Two weekly public programs: Café Shambhala (Saturdays 10am–noon) — "
            "group sitting meditation + dharma reading + discussion + social time, with "
            "free instruction for newcomers; Tuesday Tune In (Tuesdays, 6–7pm) — "
            "three staggered 30-minute sitting periods with free instruction for "
            "first-timers. All programs open to the public regardless of experience. "
            "lexington.shambhala.org."
        ),
    ),
    "lexington_zen": Center(
        id="lexington_zen",
        name="Lexington Zen Center",
        url="https://lexingtonzencenter.org",
        address="649 Price Avenue",
        city="Lexington",
        state="KY",
        zip_code="40508",
        lat=38.0530,
        lng=-84.5000,
        neighborhood="Downtown / Northside",
        tradition=Tradition.ZEN,
        notes=(
            "Lexington Zen Center is a Korean/American Zen community in the Chogye "
            "lineage, founded as a student group of Zen Master Dae Gak of Furnace "
            "Mountain Retreat Center (Clay City, KY). Meets at the Friends (Quaker) "
            "Meetinghouse, 649 Price Avenue. First Sunday of each month: 2pm in-person "
            "sit — two 25-minute periods of zazen separated by walking meditation. "
            "All other Sundays via Zoom (contact for link). Small, welcoming community; "
            "email before visiting as meetings are occasionally cancelled. "
            "lexingtonzencenter.org."
        ),
    ),
    "bluegrass_zen_lexington": Center(
        id="bluegrass_zen_lexington",
        name="Bluegrass Zen",
        url="https://bluegrasszen.org",
        address="3564 Clays Mill Road",
        city="Lexington",
        state="KY",
        zip_code="40503",
        lat=38.0132,
        lng=-84.5472,
        neighborhood="Southwest Lexington",
        tradition=Tradition.ZEN,
        notes=(
            "Bluegrass Zen is a Chan (Chinese Zen) community affiliated with the "
            "Pacific Zen Institute, led by Rev. David Parks, Roshi (based in Waco, KY). "
            "Lexington sits meet Thursday evenings at 6:30pm in the Purple Room at the "
            "Unitarian Universalist Church of Lexington, 3564 Clays Mill Road. "
            "Also has a Berea location (Mondays 6:30pm at Community Church of Berea). "
            "Open to all; no experience required. Meetup: open-door-zen-kentucky. "
            "bluegrasszen.org."
        ),
    ),
    "uucl_sunday_sangha": Center(
        id="uucl_sunday_sangha",
        name="UUCL Sunday Sangha",
        url="https://sites.google.com/uucl.org/sundaysangha",
        address="3564 Clays Mill Road",
        city="Lexington",
        state="KY",
        zip_code="40503",
        lat=38.0132,
        lng=-84.5472,
        neighborhood="Southwest Lexington",
        tradition=Tradition.OTHER,
        notes=(
            "UUCL Sunday Sangha is an interfaith mindfulness community meeting at the "
            "Unitarian Universalist Church of Lexington, influenced by the Plum Village "
            "tradition of Thich Nhat Hanh. Sunday mornings 9–10:45am: silent sitting "
            "meditation (9–9:30am, in-person only), short break, then hybrid group "
            "dharma discussion (9:45–10:45am, in-person + Google Meet). Open to all "
            "regardless of background. Contact: sangha@uucl.org. Note: Bluegrass Zen "
            "also meets at UUCL on Thursday evenings. "
            "sites.google.com/uucl.org/sundaysangha."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "shambhala_lexington": {
        "url": "https://shambhala-koeln.de/ical.php?center=193",
        "filter_to_sits": True,
    },
}
