"""
Connecticut — Phase 3 expansion (Hartford / New Haven area).

Connecticut has a dispersed Buddhist community across the Hartford and New Haven
metro areas, with centers spanning Kwan Um Zen, Shambhala, Kadampa (NKT),
Karma Kagyu (Nalandabodhi), and the Tibetan Karma Kagyu (KTC) lineages.
No live iCal feeds are accessible: Shambhala New Haven is Cloudflare-blocked,
KMC Connecticut uses a JS-rendered calendar, and the other centers have no
machine-readable feeds. All sits are seeded as recurring instances via
sangha-seed-recurring.js.

Centers included:
  - New Haven Zen Center (new_haven_zen) — Kwan Um School of Zen
    193 Mansfield St, New Haven CT 06511. newhavenzen.org
    Wed 7:30pm, Sun 9am. No iCal; recurring seeded.

  - Shambhala Meditation Center of New Haven (shambhala_new_haven) — Tibetan/Shambhala
    493 Whitney Ave (2nd Fl), New Haven CT 06511. newhaven.shambhala.org
    Sun 9:30am open meditation. Cloudflare-blocked; recurring seeded.

  - Odiyana Kadampa Meditation Center (odiyana_kadampa) — NKT Tibetan
    450 New London Turnpike, Glastonbury CT 06033. meditationinconnecticut.org
    Sun 11am, Thu 7pm. JS-rendered calendar; recurring seeded.

  - Nalandabodhi Connecticut (nalandabodhi_ct) — Tibetan Kagyu/Nyingma
    3 Barnard Lane, Suite 305, Bloomfield CT 06002. ct.nalandabodhi.org
    Sun 10am. WordPress calendar w/o iCal export; recurring seeded.

  - Hartford Karma Thegsum Choling (hartford_ktc) — Tibetan Karma Kagyu
    157 Elizabeth Street, Hartford CT 06105. ktchartford.org
    Tue 7pm practice and study. JS-heavy site; recurring seeded.

Research notes (2026-05-21):
  - New Haven Zen Center: Kwan Um School of Zen (Korean Zen). 193 Mansfield St,
    New Haven (East Rock neighborhood). Wed evening: 7pm chanting + 7:30pm zazen
    (seed 7:30pm sit start). Sun morning: 9am sitting through ~10:50am. Drop-in
    welcome; contact nhzc@newhavenzen.org. Strong 40+ year community.
  - Shambhala New Haven: 493 Whitney Ave 2nd floor (East Rock Health & Wellness).
    Sun 9:30–11:30am open meditation (sitting + walking alternating, instruction
    available, dharma talk 1st Sunday). Cloudflare blocks curl; seed as recurring.
    Tue 7:30pm is Heart of Recovery program (addiction recovery focus) — skipped
    as it's a specialized program, not a general public sit.
  - Odiyana Kadampa (NKT): 450 New London Turnpike, Glastonbury CT (suburb of
    Hartford). Sun 11am–12:15pm "Meditation Made Easy" and Thu 7–8:15pm drop-in
    class. Fee-based ($8–12, free for members) but open to all. JS-rendered
    calendar; no iCal. Founded by Gen Kelsang Wangden.
  - Nalandabodhi CT: 3 Barnard Lane Suite 305, Bloomfield CT (Hartford suburb).
    Founded by Dzogchen Ponlop Rinpoche (Kagyu/Nyingma). Sun 10–10:50am
    meditation (in-person Bloomfield or Zoom) + 11–11:30am dharma discussion.
    WordPress Full Calendar plugin with no iCal export. Active community.
  - Hartford KTC: 157 Elizabeth Street, Hartford CT 06105. Affiliated with
    Karma Triyana Dharmachakra (KTD), Woodstock NY — same Karma Kagyu lineage
    as Columbus KTC, Richmond KTC, etc. Tuesday evening practice and study
    group (est. 7pm). Website JS-heavy; schedule requires direct contact.
    Phone: (860) 232-8366.
  - Buddhist Faith Fellowship (Middletown): WordPress site; tested
    bffct.org/bff/upcoming-events/?ical=1 — returns HTML (no iCal plugin).
    Events page is tribe_events-free. Sunday meets only 2x/month; deferred.
  - Hartford Shambhala: Listed in old directories at 149 Kenyon St / 58 Ballard
    Dr, West Hartford. Contact is personal AOL email. No active website found.
    Likely dormant small study group — skipped.
  - Greater Hartford Sangha (Plum Village): Weebly site, AOL email, last activity
    unclear. Skipped as likely dormant.
  - New Haven Insight: Yale-affiliated group, Dwight Chapel. Mon + Thu 8pm;
    website down; schedule tied to academic calendar — too unstable to seed.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "new_haven_zen": Center(
        id="new_haven_zen",
        name="New Haven Zen Center",
        url="https://www.newhavenzen.org",
        address="193 Mansfield Street",
        city="New Haven",
        state="CT",
        zip_code="06511",
        lat=41.3117,
        lng=-72.9278,
        neighborhood="East Rock",
        tradition=Tradition.ZEN,
        notes=(
            "The New Haven Zen Center (NHZC) is a Kwan Um School of Zen community "
            "founded in 1977, practicing Korean Zen in the lineage of Zen Master "
            "Seungsahn. Located in the East Rock neighborhood of New Haven, NHZC "
            "offers two weekly public sitting programs: Wednesday Evening (7:30 PM — "
            "sitting, walking, and chanting; newcomer orientation 2nd and 4th "
            "Wednesdays at 6:30 PM) and Sunday Morning (9 AM — sitting, walking, "
            "and chanting through ~10:50 AM with dharma talk). Drop-in welcome; "
            "no experience required. Free; dana appreciated."
        ),
    ),
    "shambhala_new_haven": Center(
        id="shambhala_new_haven",
        name="Shambhala Meditation Center of New Haven",
        url="https://newhaven.shambhala.org",
        address="493 Whitney Avenue, 2nd Floor",
        city="New Haven",
        state="CT",
        zip_code="06511",
        lat=41.3238,
        lng=-72.9303,
        neighborhood="East Rock / Whitney Avenue",
        tradition=Tradition.TIBETAN,
        notes=(
            "The Shambhala Meditation Center of New Haven is part of the international "
            "Shambhala community, rooted in the Tibetan Buddhist teachings of Chögyam "
            "Trungpa Rinpoche and Sakyong Mipham Rinpoche. Located on the second floor "
            "of East Rock Health & Wellness at 493 Whitney Avenue, the center offers "
            "Sunday Morning Open Meditation (9:30–11:30 AM) — alternating sitting and "
            "walking periods with instruction available for newcomers and a dharma talk "
            "on the first Sunday of each month. Open to all; no experience required; "
            "drop-in welcome. Suggested donation."
        ),
    ),
    "odiyana_kadampa": Center(
        id="odiyana_kadampa",
        name="Odiyana Kadampa Meditation Center",
        url="https://www.meditationinconnecticut.org",
        address="450 New London Turnpike",
        city="Glastonbury",
        state="CT",
        zip_code="06033",
        lat=41.7084,
        lng=-72.5950,
        neighborhood="Glastonbury (Hartford suburb)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Odiyana Kadampa Meditation Center is Connecticut's New Kadampa Tradition "
            "(NKT-IKBU) center, offering modern Tibetan Buddhist teachings and guided "
            "meditation at 450 New London Turnpike in Glastonbury, a Hartford suburb. "
            "Two weekly drop-in public classes: Sunday Morning (11 AM–12:15 PM, "
            "'Meditation Made Easy') and Thursday Evening (7–8:15 PM). Classes combine "
            "guided meditation with Buddhist philosophy in the Kadampa style and are "
            "open to all levels. Suggested donation $8–12; free for members."
        ),
    ),
    "nalandabodhi_ct": Center(
        id="nalandabodhi_ct",
        name="Nalandabodhi Connecticut",
        url="https://ct.nalandabodhi.org",
        address="3 Barnard Lane, Suite 305",
        city="Bloomfield",
        state="CT",
        zip_code="06002",
        lat=41.8438,
        lng=-72.7197,
        neighborhood="Bloomfield (Hartford suburb)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Nalandabodhi Connecticut is part of the Nalandabodhi international "
            "sangha founded by Dzogchen Ponlop Rinpoche, practicing in the Kagyu "
            "and Nyingma lineages of Tibetan Buddhism. The Connecticut center meets "
            "at 3 Barnard Lane, Suite 305, Bloomfield (a Hartford suburb), and on "
            "Zoom. Sunday morning program: 10–10:50 AM guided meditation followed "
            "by 11–11:30 AM dharma discussion. Hybrid in-person and Zoom. Open to "
            "all; free; no experience required."
        ),
    ),
    "hartford_ktc": Center(
        id="hartford_ktc",
        name="Hartford Karma Thegsum Choling",
        url="https://ktchartford.org",
        address="157 Elizabeth Street",
        city="Hartford",
        state="CT",
        zip_code="06105",
        lat=41.7627,
        lng=-72.6990,
        neighborhood="West End, Hartford",
        tradition=Tradition.TIBETAN,
        notes=(
            "Hartford Karma Thegsum Choling (KTC) is a Tibetan Buddhist meditation "
            "center affiliated with Karma Triyana Dharmachakra (KTD Monastery) in "
            "Woodstock, New York — the North American seat of His Holiness the "
            "Gyalwang Karmapa in the Karma Kagyu lineage. Located in Hartford's "
            "West End neighborhood, the center offers a Tuesday Evening practice "
            "and study group (7 PM). Open to all; no experience required; "
            "contact (860) 232-8366 for current schedule and programs."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds — none accessible for Connecticut centers
# ---------------------------------------------------------------------------

ICAL_FEEDS: dict = {}
