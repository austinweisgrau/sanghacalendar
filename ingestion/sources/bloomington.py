"""
Bloomington, IN — Phase 3 expansion.

Bloomington is home to Indiana University and an unusually rich Buddhist scene
for a mid-size college town. The Tibetan Mongolian Buddhist Cultural Center
(founded by Thubten Norbu, the Dalai Lama's elder brother) anchors a diverse
community spanning Tibetan, Zen, Shambhala, and secular mindfulness traditions.

Centers included:
  - TMBCC (tmbcc) — Tibetan (Gelug)
    3655 S Snoddy Rd, Bloomington IN 47401. tmbcc.org
    Mon 6:30pm group meditation, Wed 6pm open meditation, Sun 10:30am teachings
    No iCal (WordPress site, ?ical=1 returns 404); recurring sits seeded.

  - Kadampa Meditation Center Bloomington (kmc_bloomington) — NKT Tibetan
    234 N. Morton St, Bloomington IN 47404. meditationinbloomington.org
    Tue 6pm, Wed 12:15pm, Sun 11am drop-in classes
    No iCal (Wix site, JS-rendered calendar); recurring sits seeded.

  - Open Mind Zen Indiana (open_mind_zen_indiana) — Zen (Open Mind Zen)
    Bloomington Friends Meeting House, 3820 E. Moores Pike, Bloomington IN 47402
    Mon 7pm weekly sit (Oct–May active schedule; sits continue year-round)
    No iCal (plain HTML schedule page); recurring sit seeded.

  - Hoosier Heartland Shambhala Meditation Group (hoosier_heartland_shambhala) — Shambhala
    Multiple venues in Bloomington:
      Mon noon — Unitarian Universalist Church, 2120 N Fee Ln (hybrid)
      Thu 6pm — TMBCC, 3655 Snoddy Rd (in-person)
      Fri 6pm — Center for Wholism, 2401 N. Walnut St (in-person)
    No iCal (Shambhala Network site, no machine-readable feed); recurring sits seeded.

Research notes (2026-05-20):
  - TMBCC: 108-acre campus; Kumbum Chamtse Ling temple. Founded by Thubten Norbu
    (Tenzin Gyatso's eldest brother). ?ical=1 returns 404. Schedule confirmed via
    tmbcc.org and Yelp (updated April 2026): Mon 6:30pm group meditation, Wed 6pm
    open meditation, Sun 10:30am Buddhist philosophy teachings.
  - KMC Bloomington: 234 N. Morton St downtown. Wix site, no iCal. Four weekly
    drop-in classes confirmed: Tue 6–7:15pm, Wed 12:15–12:45pm lunchtime,
    Sun 11am–12:15pm general program. NKT center offering modern Kadampa
    teachings + guided meditation. Suggested donation.
  - Open Mind Zen Indiana: Meets at Bloomington Friends Meeting House. Contemporary
    Zen lineage. Mon 7pm confirmed from schedule page (openmindzenbloomington.org).
    Has a Columbus IN satellite (bi-weekly Sun 2:30pm) — not added here.
  - Hoosier Heartland Shambhala: Three weekly sits across three venues. Schedule
    confirmed from hhsmg.shambhala.org/ongoing-offerings/. Thu sit is held AT
    TMBCC campus (cross-tradition cooperation). Mon sit is hybrid with Zoom.
  - Ganden Dheling (Unity Center, Mon 7pm): Website 403; uncertain if still active.
    Skipped pending verification.
  - Gaden KhachoeShing Monastery (2150 E Dolan Rd): Monastery; regular classes
    "not published publicly" per website. Monthly tsog/puja calendar only.
    Skipped (no clear weekly public sits).
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "tmbcc": Center(
        id="tmbcc",
        name="Tibetan Mongolian Buddhist Cultural Center",
        url="https://tmbcc.org",
        address="3655 S Snoddy Road",
        city="Bloomington",
        state="IN",
        zip_code="47401",
        lat=39.1198,
        lng=-86.5097,
        neighborhood="South Bloomington",
        tradition=Tradition.TIBETAN,
        notes=(
            "The Tibetan Mongolian Buddhist Cultural Center (TMBCC) is one of the "
            "most significant Tibetan Buddhist institutions in North America. Founded "
            "by Thubten Norbu — elder brother of His Holiness the 14th Dalai Lama — "
            "on 108 acres in southern Bloomington, the campus includes the Kumbum "
            "Chamtse Ling temple and Kumbum West monastery. The center offers "
            "three weekly public meditation programs: Monday Group Meditation "
            "(6:30–7:30 PM), Wednesday Open Meditation (6–7 PM, open to anyone "
            "wishing to sit in stillness, prayer, or practice), and Sunday Buddhist "
            "Philosophy Teachings (10:30 AM–noon). Free and open to all."
        ),
    ),
    "kmc_bloomington": Center(
        id="kmc_bloomington",
        name="Kadampa Meditation Center Bloomington",
        url="https://www.meditationinbloomington.org",
        address="234 N. Morton Street",
        city="Bloomington",
        state="IN",
        zip_code="47404",
        lat=39.1662,
        lng=-86.5340,
        neighborhood="Downtown Bloomington",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Bloomington (KMC Bloomington) is Indiana "
            "University's New Kadampa Tradition (NKT) center, offering modern "
            "Tibetan Buddhist teachings and guided meditation in a welcoming "
            "downtown setting. Three weekly drop-in public classes: Tuesday "
            "Evening (6–7:15 PM), Wednesday Lunchtime (12:15–12:45 PM), and "
            "Sunday General Program (11 AM–12:15 PM). Classes combine guided "
            "meditation with Buddhist teachings in the Kadampa style. Drop-in "
            "welcome; suggested donation."
        ),
    ),
    "open_mind_zen_indiana": Center(
        id="open_mind_zen_indiana",
        name="Open Mind Zen Indiana",
        url="https://openmindzenbloomington.org",
        address="3820 E. Moores Pike",
        city="Bloomington",
        state="IN",
        zip_code="47402",
        lat=39.1539,
        lng=-86.4839,
        neighborhood="East Bloomington / Friends Meeting House",
        tradition=Tradition.ZEN,
        notes=(
            "Open Mind Zen Indiana (OMZI) is a contemporary Zen sangha meeting "
            "at the Bloomington Friends Meeting House. Practice includes zazen "
            "sitting and walking meditation, koan study, dharma talks, workshops, "
            "and retreats. Weekly Monday evening sits (7–9 PM) are open to all; "
            "no experience required. OMZI is a 501(c)(3) nonprofit affiliated with "
            "the Open Mind Zen tradition."
        ),
    ),
    "hoosier_heartland_shambhala": Center(
        id="hoosier_heartland_shambhala",
        name="Hoosier Heartland Shambhala Meditation Group",
        url="https://hhsmg.shambhala.org",
        address="2120 N Fee Lane",
        city="Bloomington",
        state="IN",
        zip_code="47408",
        lat=39.1810,
        lng=-86.5282,
        neighborhood="North Bloomington / UU Church",
        tradition=Tradition.TIBETAN,
        notes=(
            "The Hoosier Heartland Shambhala Meditation Group (HHSMG) offers "
            "three weekly open sits in Bloomington, requiring no prior experience. "
            "Monday Open Sit (noon–1 PM) at the Unitarian Universalist Church, "
            "2120 N Fee Ln — hybrid in-person and Zoom. Thursday Evening Sit "
            "(6–7:30 PM) at the Tibetan Mongolian Buddhist Cultural Center "
            "(TMBCC), 3655 Snoddy Rd. Friday Night Sit (6–7:30 PM, with "
            "instruction 6–6:30 PM) at the Center for Wholism, 2401 N. Walnut "
            "St. All sits are free and open to the public. Part of the "
            "international Shambhala Buddhist community (Chögyam Trungpa lineage)."
        ),
    ),
}

# No live iCal feeds extractable for Bloomington centers —
# all sits seeded as recurring in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
