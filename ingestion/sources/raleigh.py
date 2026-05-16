"""
Raleigh-Durham-Chapel Hill (Research Triangle), NC — Phase 3 expansion.

The Research Triangle is home to several strong Buddhist communities anchored
around Duke, UNC, and NC State. Centers are spread across Durham, Chapel Hill,
and rural Chatham County (Pittsboro).

Centers included:
  - Durham Shambhala Meditation Center — Tibetan/Shambhala, recurring sits
    733 Rutherford St, Durham NC 27705
  - Chapel Hill Zen Center — Soto Zen (SFZC lineage), recurring sits
    5322 NC Highway 86, Chapel Hill NC 27514
  - North Carolina Zen Center — Soto Zen (Rinzai-influenced), recurring sits
    390 Ironwood, Pittsboro NC 27312

Research notes (2026-05-16):
  - Durham Shambhala (durham.shambhala.org): Uses Shambhala custom WordPress.
    No iCal feed accessible. Recurring programs confirmed from program-details pages:
      Sun 9am–noon: Sunday Morning Meditation (in-person, 733 Rutherford St)
      Thu 7–8:30pm: Thursday Night Open House (in-person; meditation instruction + sit)
      Sat 10:30am–noon: Saturday Dharma Discussions (Zoom only)
      Wed 7–8pm: Heart of Recovery Support Group (in-person)
    Address: 733 Rutherford St, Durham NC 27705.

  - Chapel Hill Zen Center (chzc.org): Soto Zen in Shunryu Suzuki-roshi lineage
    (affiliated with SFZC). No iCal (WordPress 404 on ?ical=1). Schedule from homepage:
      Mon–Fri 6am: morning zazen (in-person + Zoom — "at 6 and 6:50 AM")
      Sun 9am: Sunday morning zazen (in-person — "at 9 and 9:50 AM")
      Tue 7pm: Tuesday evening zazen (in-person — "at 7 and 7:50 PM")
    Address: 5322 NC Highway 86, Chapel Hill NC 27514 (2.5 mi north of I-40 exit 266).

  - NC Zen Center (nczencenter.org): Pittsboro, 15 acres of wooded land south of
    Chapel Hill. Uses The Events Calendar WP plugin but iCal feed returns empty (0 bytes).
    Schedule confirmed from events page:
      Sun 10am–noon: Zazen, Chanting, Teisho (in-person; two sits + dharma talk)
      Mon 7–7:50am: Morning Zazen (Zoom only)
      Tue 7–8:30pm: Dharma Study and Zazen (in-person)
      Wed 7–7:50am: Morning Zazen (hybrid in-person + Zoom)
      Thu 7–8:30pm: Zazen and Chanting Service (in-person; two sits + dokusan)
      Fri 7–7:50am: Morning Zazen (hybrid in-person + Zoom)

  Skipped for now:
  - Kadampa Center Raleigh (FPMT, kadampa-center.org): Drupal 7, JS-rendered calendar.
    No accessible iCal. Resident teacher Geshe Gelek. Monitor for calendar access.
  - Kosala Kadampa (NKT, meditationinthetriangle.org): Squarespace, no iCal.
  - Sit Raleigh (sitraleigh.com): Google Sites page. Small community; one Tue 7pm sit.
    Could seed in future if requested.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "durham_shambhala": Center(
        id="durham_shambhala",
        name="Durham Shambhala Meditation Center",
        url="https://durham.shambhala.org",
        address="733 Rutherford Street",
        city="Durham",
        state="NC",
        zip_code="27705",
        lat=36.0018,
        lng=-78.9281,
        neighborhood="Duke Park",
        tradition=Tradition.TIBETAN,
        notes=(
            "Durham Shambhala Meditation Center is part of the international Shambhala "
            "network, offering meditation instruction rooted in the Tibetan and Shambhala "
            "warrior traditions. Weekly schedule: Thursday Night Open House (7–8:30pm, "
            "in-person — free meditation instruction + group sit + refreshments); Sunday "
            "Morning Meditation (9am–noon, in-person); Saturday Dharma Discussions "
            "(10:30am–noon, online via Zoom); Heart of Recovery (Wed 7pm, in-person). "
            "All are welcome; no experience required."
        ),
    ),
    "chapel_hill_zen": Center(
        id="chapel_hill_zen",
        name="Chapel Hill Zen Center",
        url="https://www.chzc.org",
        address="5322 NC Highway 86",
        city="Chapel Hill",
        state="NC",
        zip_code="27514",
        lat=35.9763,
        lng=-79.0485,
        neighborhood="North Chapel Hill",
        tradition=Tradition.ZEN,
        notes=(
            "The Chapel Hill Zen Center practices Soto Zen in the lineage of Shunryu "
            "Suzuki-roshi (San Francisco Zen Center tradition). Located 2.5 miles north "
            "of I-40 exit 266 on NC-86. Weekly schedule: Monday–Friday morning zazen at "
            "6am and 6:50am (in-person and Zoom); Tuesday evening zazen at 7pm and 7:50pm "
            "(in-person); Sunday morning zazen at 9am and 9:50am (in-person). Meditation "
            "instruction offered on Tuesday evenings and Sunday mornings. All welcome; "
            "please contact before first visit."
        ),
    ),
    "nc_zen_center": Center(
        id="nc_zen_center",
        name="North Carolina Zen Center",
        url="https://nczencenter.org",
        address="390 Ironwood Road",
        city="Pittsboro",
        state="NC",
        zip_code="27312",
        lat=35.7268,
        lng=-79.1823,
        neighborhood="Rural Chatham County",
        tradition=Tradition.ZEN,
        notes=(
            "The North Carolina Zen Center (NCZC) is a residential Zen Buddhist community "
            "and retreat center on 15 wooded acres south of Chapel Hill. Teshin Roshi "
            "leads a full week of practice: Sunday (10am–noon, two sits + chanting service "
            "+ dharma talk); Monday morning Zoom zazen (7–7:50am); Tuesday evening dharma "
            "study + zazen (7–8:30pm, in-person); Wednesday morning zazen (7–7:50am, "
            "hybrid); Thursday evening zazen + chanting service + dokusan (7–8:30pm, "
            "in-person); Friday morning zazen (7–7:50am, hybrid). Residential practice "
            "and personal retreats available. All levels welcome."
        ),
    ),
}

# No live iCal feeds — all centers are seeded as recurring sits via
# scripts/sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
