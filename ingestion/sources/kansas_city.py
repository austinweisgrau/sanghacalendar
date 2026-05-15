"""
Kansas City, MO meditation center sources — Phase 3 expansion.

Kansas City has a modest but well-established Buddhist scene anchored by the Rime
Buddhist Center (one of the oldest and largest non-sectarian centers in the region)
and the Kansas Zen Center's KC branch.

No centers offer publicly accessible iCal feeds; all sits are seeded as recurring
events in scripts/sangha-seed-recurring.js.

Centers included:
  - Rime Buddhist Center (Waldo/Brookside) — Non-sectarian Rimé pluralist, 4+ sits/week
  - Kansas Zen Center — Kansas City branch (Country Club Plaza) — Kwan Um Zen, Thu weekly

Research notes (2026-05-15):
  - Rime Buddhist Center (rimecenter.org): 2939 Wayne Ave, Kansas City MO 64109.
    30+ year old non-sectarian center rooted in Rimé philosophy (draws from all four
    Tibetan schools plus Zen). One of the most active centers in KC.
    Regular schedule: Mon–Fri 12–12:30pm daily group meditation (in-person);
    Monday 7–8pm Zen Meditation (in-person); Wednesday 7–7:30pm Group Meditation
    (in-person); Thursday 7–7:30pm Group Meditation + Medicine Buddha Sadhana
    (in-person); Sunday 10:30am Service/Practice (in-person, childcare available).
    No iCal feed; custom website calendar.
  - Kansas Zen Center — KC branch (kansaszencenter.org): Meets at Unity Temple on the
    Plaza, 707 W 47th St (47th & Jefferson), Kansas City MO 64112. Kwan Um School of
    Zen (Korean Zen), teacher Zen Master Bon Hae (Judy Roitman). KC branch: Thursday
    7pm in-person only. Main center in Lawrence KS has fuller schedule.
    Per-event ICS links on Events page; no subscription feed.
  - Temple Buddhist Center / IMCKC (templebuddhistcenter.com / imckc.com): Vipassana/
    Theravada-leaning, also at Unity Temple on the Plaza. JS-rendered Squarespace
    calendar; specific sit times not confirmed from static pages. Deferred.
  - Shambhala Kansas City: Appears defunct (kcshambhala.org gone). Skip.
  - Heartland Community of Mindful Living: Plum Village tradition, online-only Zoom.
    Deferred — no in-person.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "rime_buddhist_center": Center(
        id="rime_buddhist_center",
        name="Rime Buddhist Center",
        url="https://www.rimecenter.org",
        address="2939 Wayne Avenue",
        city="Kansas City",
        state="MO",
        zip_code="64109",
        lat=39.0278,
        lng=-94.5594,
        neighborhood="Waldo/Brookside",
        tradition=Tradition.PLURALIST,
        notes=(
            "Rime Buddhist Center is one of the most active non-sectarian Buddhist "
            "centers in the Midwest, operating for over 30 years in Kansas City's "
            "Waldo/Brookside neighborhood. Founded on Rimé philosophy (drawing from "
            "all four major Tibetan schools plus Zen), the center welcomes all "
            "traditions and levels of experience. Regular schedule: Mon–Fri "
            "12–12:30pm daily group meditation; Monday 7–8pm Zen Meditation; "
            "Wednesday 7–7:30pm Group Meditation; Thursday 7–7:30pm Group "
            "Meditation + Medicine Buddha Sadhana; Sunday 10:30am Service/Practice "
            "(childcare available). All are in-person. Free; donations welcome."
        ),
    ),
    "kansas_zen_center_kc": Center(
        id="kansas_zen_center_kc",
        name="Kansas Zen Center — Kansas City",
        url="https://www.kansaszencenter.org",
        address="707 West 47th Street",
        city="Kansas City",
        state="MO",
        zip_code="64112",
        lat=39.0462,
        lng=-94.5905,
        neighborhood="Country Club Plaza (at Unity Temple)",
        tradition=Tradition.ZEN,
        notes=(
            "The Kansas City branch of the Kansas Zen Center holds weekly Thursday "
            "evening sits at Unity Temple on the Plaza (47th & Jefferson, Kansas City "
            "MO 64112). Practice follows the Kwan Um School of Zen (Korean Zen) under "
            "Zen Master Bon Hae (Judy Roitman). The KC branch meets in-person on "
            "Thursdays at 7pm; the first Thursday includes Q&A with Zen Master Bon Hae "
            "and the fourth Thursday features kong-an (koan) interviews. The main center "
            "is in Lawrence, KS with a fuller hybrid schedule. Drop-in welcome. Free."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

# No Kansas City centers have accessible iCal subscription feeds.
# All sits are seeded as recurring events in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
