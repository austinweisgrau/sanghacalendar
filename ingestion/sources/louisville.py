"""
Louisville, KY — Phase 3 expansion.

Louisville has a compact but diverse practice community spanning Zen, Theravada,
Tibetan, and Plum Village traditions. The city's Buddhist scene clusters around
the Highlands / Bardstown Road corridor and the St. Matthews neighborhood.

Centers included:
  - Louisville Zen Center (louisville_zen_center) — Zen (Rinzai-Soto, Kapleau lineage)
    917 Rosemary Dr (primary) / 1507 Bardstown Rd (Sun sits), Louisville KY 40205
    louisvillezen.org — Tue 6:30pm, Sun 6:30pm (hybrid in-person + Zoom)
    No iCal; static HTML site. Recurring sits seeded.

  - Open Mind Zen Louisville (omz_louisville) — Zen (White Plum Asanga)
    1013 Bardstown Rd, Louisville KY 40204
    omzlouisville.com / openmindzen.com — Sat 10:30am (hybrid)
    Global OMZ iCal feed only covers Melbourne location; Louisville sits seeded as recurring.

  - Louisville Community of Mindful Living / Sangha Lou (sangha_lou) — Zen (Plum Village / TNH)
    115 S Ewing Ave, Louisville KY 40206
    sanghalou.org — Sun 10am–noon (hybrid in-person + Zoom)
    No iCal; recurring sits seeded.

  - Louisville Vipassana Community (louisville_vipassana_community) — Theravada/Vipassana
    Clifton Unitarian Universalist Church, 2231 Payne St, Louisville KY 40206
    louisville-vipassana-community.org — Mon 6:30pm (hybrid in-person + Zoom)
    No iCal (basic HTML site); recurring sits seeded.

  - Drepung Gomang Center for Engaging Compassion (drepung_gomang_louisville) — Tibetan (Gelugpa)
    411 N Hubbards Lane, Louisville KY 40207
    drepunggomangusa.org — Wed 12:10pm noontime + Wed 7pm community meditation
    Calendarize iCal feed is JS-rendered (URL not extractable via static scrape); recurring sits seeded.

  - Kentucky Meditation Peace Center (kmpc_louisville) — Theravada
    4815 Manslick Rd, Louisville KY 40216
    kmpc.co — Mon 7pm, Wed 7pm weekly group meditation
    No iCal; recurring sits seeded.

Research notes (2026-05-19):
  - Louisville Zen Center: Rinzai-Soto hybrid, descended from Rochester Zen Center
    (Philip Kapleau lineage). Meets at two locations: 917 Rosemary Dr (Tue) and
    1507 Bardstown Rd (Sun). Hybrid in-person + Zoom. Newcomer orientation at 6pm
    before Tuesday 6:30pm sit.
  - Open Mind Zen Louisville: White Plum Asanga lineage. openmindzen.com parent site
    has a WordPress iCal feed (?ical=1) but venue-specific feed returns empty — only
    Melbourne location events appear in global feed. Sat 10:30am hybrid + daily 7am Zoom.
  - Sangha Lou: Plum Village / Thich Nhat Hanh tradition. Sunday 10am–noon, in-person
    + Zoom hybrid. Small lay community.
  - Louisville Vipassana Community: IMS-style Insight Meditation, meets at Clifton UU.
    Monday evening 6:30–8pm hybrid (guided sit + dharma talk). Tue/Wed 7:30am Zoom only.
  - Drepung Gomang (DGCEC): Gelugpa Tibetan center with resident Geshe. Strong academic
    and practice programming. Wed noontime sit (12:10–12:40pm) and Wed evening (7–8pm).
    WildApricot also used for registrations. Calendarize iCal URL is JS-populated.
  - KMPC: Kentucky Meditation Peace Center and Buddhist Vihara (same address as KMCBV at
    4815 Manslick Rd — two organizational names, one physical space). Resident monks teach
    Vipassana. Mon + Wed 7–8:30pm.
  - Shambhala Louisville: not in Shambhala's current center directory — appears defunct.
  - SGI-USA Kentucky: member discussion meetings, not open public sits. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "louisville_zen_center": Center(
        id="louisville_zen_center",
        name="Louisville Zen Center",
        url="https://www.louisvillezen.org",
        address="917 Rosemary Drive",
        city="Louisville",
        state="KY",
        zip_code="40205",
        lat=38.2355,
        lng=-85.7116,
        neighborhood="Highlands / Tyler Park",
        tradition=Tradition.ZEN,
        notes=(
            "Louisville Zen Center is a Rinzai-Soto Zen community in the lineage of "
            "Rochester Zen Center (Philip Kapleau Roshi). Meets at two Louisville "
            "locations: 917 Rosemary Dr (Tuesday evenings) and 1507 Bardstown Rd at "
            "Infinite Bliss Yoga (Sunday evenings). Both sits run 6:30–8pm, hybrid "
            "in-person and Zoom. Newcomer orientation offered at 6pm before the Tuesday "
            "sit. Also participates in daily morning Zoom sits hosted by Rochester Zen "
            "Center (7–8am most weekdays). Free for first-timers; suggested $5–10 "
            "donation for non-members. Drop-in welcome."
        ),
    ),
    "omz_louisville": Center(
        id="omz_louisville",
        name="Open Mind Zen Louisville",
        url="https://www.omzlouisville.com",
        address="1013 Bardstown Road",
        city="Louisville",
        state="KY",
        zip_code="40204",
        lat=38.2253,
        lng=-85.7212,
        neighborhood="Highlands / Bardstown Road",
        tradition=Tradition.ZEN,
        notes=(
            "Open Mind Zen Louisville (OMZL) is a lay Zen community in the White Plum "
            "Asanga lineage, meeting at the Garner Large art space on Bardstown Road "
            "(enter through the orange door in the alley). Saturday Morning Meditation "
            "(10:30am–noon): in-person zazen + Dharma talk, hybrid Zoom available. "
            "Daily morning Zoom zazen (7–8am) drop-in. Part of the Open Mind Zen "
            "network (openmindzen.com). No registration required; beginner-friendly."
        ),
    ),
    "sangha_lou": Center(
        id="sangha_lou",
        name="Louisville Community of Mindful Living (Sangha Lou)",
        url="https://www.sanghalou.org",
        address="115 S Ewing Avenue",
        city="Louisville",
        state="KY",
        zip_code="40206",
        lat=38.2322,
        lng=-85.7069,
        neighborhood="Crescent Hill",
        tradition=Tradition.ZEN,
        notes=(
            "Louisville Community of Mindful Living (Sangha Lou) practices in the "
            "tradition of Thich Nhat Hanh and Plum Village. Sunday gatherings "
            "(10am–noon) include guided sitting meditation, walking meditation, dharma "
            "sharing, and discussion — hybrid in-person at 115 S Ewing Ave and Zoom. "
            "Open to all regardless of background. Emphasis on applied mindfulness, "
            "interbeing, and engaged Buddhism."
        ),
    ),
    "louisville_vipassana_community": Center(
        id="louisville_vipassana_community",
        name="Louisville Vipassana Community",
        url="http://www.louisville-vipassana-community.org",
        address="2231 Payne Street",
        city="Louisville",
        state="KY",
        zip_code="40206",
        lat=38.2504,
        lng=-85.7105,
        neighborhood="Clifton",
        tradition=Tradition.THERAVADA,
        notes=(
            "Louisville Vipassana Community offers weekly Insight Meditation gatherings "
            "in the IMS / Spirit Rock tradition. Monday Evening Meditation (6:30–8pm) "
            "meets at Clifton Unitarian Universalist Church — guided sitting, walking "
            "meditation, dharma talk, and discussion. Hybrid in-person + Zoom. "
            "Also Tuesday and Wednesday morning Zoom-only sits (7:30–8:05am). "
            "Drop-in welcome; donation-based."
        ),
    ),
    "drepung_gomang_louisville": Center(
        id="drepung_gomang_louisville",
        name="Drepung Gomang Center for Engaging Compassion",
        url="https://www.drepunggomangusa.org",
        address="411 N Hubbards Lane",
        city="Louisville",
        state="KY",
        zip_code="40207",
        lat=38.2632,
        lng=-85.6900,
        neighborhood="St. Matthews",
        tradition=Tradition.TIBETAN,
        notes=(
            "Drepung Gomang Center for Engaging Compassion (DGCEC) is the Louisville "
            "branch of Drepung Gomang monastery — one of the three great Gelugpa "
            "monasteries of Tibet, now re-established in South India. Resident Geshe "
            "offers Tibetan Buddhist teachings, meditation, and community practice. "
            "Weekly Wednesday Noontime Meditation (12:10–12:40pm, in-person) and "
            "Wednesday Evening Community Meditation (7–8pm, in-person, with chanting "
            "and prayers). All sessions open to the public; no prior experience needed."
        ),
    ),
    "kmpc_louisville": Center(
        id="kmpc_louisville",
        name="Kentucky Meditation Peace Center",
        url="https://kmpc.co",
        address="4815 Manslick Road",
        city="Louisville",
        state="KY",
        zip_code="40216",
        lat=38.1755,
        lng=-85.8014,
        neighborhood="Pleasure Ridge Park / SW Jefferson",
        tradition=Tradition.THERAVADA,
        notes=(
            "Kentucky Meditation Peace Center and Buddhist Vihara (KMPC) is a Theravada "
            "Buddhist center in southwest Louisville with resident monks teaching "
            "Vipassana insight meditation. Weekly group meditation sessions: Monday and "
            "Wednesday evenings (7–8:30pm), both in-person. Guided meditation for all "
            "levels — beginners welcome. Also operates as Kentucky Meditation Center "
            "and Buddhist Vihara (KMCBV) at the same address."
        ),
    ),
}

# No live iCal feeds successfully extractable for Louisville centers —
# all sits seeded as recurring in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
