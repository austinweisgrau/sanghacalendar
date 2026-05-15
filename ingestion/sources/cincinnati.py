"""
Cincinnati, OH meditation center sources — Phase 3 expansion.

Cincinnati has a modest but active Buddhist scene spanning Zen, Tibetan, and
pluralist/Theravada traditions. No centers offer publicly accessible iCal feeds;
all sits are seeded as recurring events in sangha-seed-recurring.js.

Centers included:
  - Cincinnati Zen Center (Vine St, Cincinnati) — Korean/Soto Zen, 4 days/week
  - Buddhist Dharma Center of Cincinnati (Northside) — Ecumenical, daily Zoom + in-person
  - Gaden Samdrupling Buddhist Monastery (Colerain Township) — Gelugpa Tibetan, Wed drop-in

Research notes (2026-05-15):
  - Cincinnati Zen Center (cincinnatizencenter.org): 6015 Vine St, Cincinnati OH 45216.
    Founded under Korean Zen teacher Zen Master Dae Gak (Furnace Mountain lineage).
    Regular schedule: Sun 8am, Mon 7pm, Wed 5:30pm, Thu 7pm — all in-person, drop-in welcome.
    Sat 8:30am — virtual Zoom only. Calendar page is JS-rendered; no iCal feed accessible.
  - Buddhist Dharma Center of Cincinnati (cincinnatidharma.org): 15 Moline Court (off
    Hamilton Ave North), Northside neighborhood. Ecumenical/non-sectarian (Theravada-leaning).
    Daily 7am Zoom (Mon-Sun), Sun 10am hybrid, Tue 7pm in-person, Wed 7pm hybrid.
    JEvents (Joomla) calendar — iCal export endpoint returns 403. Seeding key sits.
  - Gaden Samdrupling Buddhist Monastery (gslmonastery.org): 3046 Pavlova Drive,
    Colerain Township / West Side. Gelugpa Tibetan (Gaden lineage). Wed 7–8pm Open
    Meditation is specifically public drop-in. Fri Introduction to Buddhism also open.
    No iCal feed; custom visual calendar.
  - Cincinnati Shambhala: No active web presence — appears defunct. Skip.
  - Tri-State Dharma (tristatedharma.org): Insight Meditation, currently Zoom-only.
    Daily morning sits (8:30am) and Sunday 9:30am via Zoom. Deferred — no in-person.
  - Loveland Zen (lovelandzen.org): ~20 miles NE at Grailville, Loveland OH.
    Monday evenings hybrid. Deferred — outer suburb, too far from city.
  - Being Peace Sangha (beingpeacecommunity.org): Thich Nhat Hanh lineage, online-only.
    Deferred — no in-person presence.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "cincinnati_zen_center": Center(
        id="cincinnati_zen_center",
        name="Cincinnati Zen Center",
        url="https://www.cincinnatizencenter.org",
        address="6015 Vine Street",
        city="Cincinnati",
        state="OH",
        zip_code="45216",
        lat=39.1851,
        lng=-84.5036,
        neighborhood="Hartwell (North Cincinnati)",
        tradition=Tradition.ZEN,
        notes=(
            "Cincinnati Zen Center sits in the Hartwell neighborhood of North Cincinnati, "
            "offering four in-person weekly sits and one virtual Saturday sit. Founded "
            "under the guidance of Zen Master Dae Gak (Furnace Mountain Sangha), the "
            "center blends Korean Zen (Kwan Um School) and Soto Zen influences. "
            "Regular in-person schedule: Sunday 8am, Monday 7pm, Wednesday 5:30pm, "
            "Thursday 7pm — all drop-in welcome; arrive 10–15 minutes early for first visit. "
            "Saturday 8:30am is virtual Zoom only. Doors lock at the start of sits. Free."
        ),
    ),
    "buddhist_dharma_center_cincinnati": Center(
        id="buddhist_dharma_center_cincinnati",
        name="Buddhist Dharma Center of Cincinnati",
        url="https://www.cincinnatidharma.org",
        address="15 Moline Court",
        city="Cincinnati",
        state="OH",
        zip_code="45223",
        lat=39.1716,
        lng=-84.5222,
        neighborhood="Northside",
        tradition=Tradition.PLURALIST,
        notes=(
            "The Buddhist Dharma Center of Cincinnati is a non-sectarian, ecumenical "
            "practice community in the Northside neighborhood. Rooted in the Theravada/"
            "Insight tradition but welcoming all approaches, the center offers daily "
            "7am Zoom sits (every day of the week), in-person and hybrid weekly sits, "
            "and periodic day-long retreats. Sunday 10am hybrid: ritual, two sits, and "
            "walking meditation. Tuesday 7pm: silent in-person sitting. Wednesday 7pm "
            "hybrid: instruction and discussion. Free; donations welcome."
        ),
    ),
    "gaden_samdrupling_monastery": Center(
        id="gaden_samdrupling_monastery",
        name="Gaden Samdrupling Buddhist Monastery",
        url="https://www.gslmonastery.org",
        address="3046 Pavlova Drive",
        city="Cincinnati",
        state="OH",
        zip_code="45251",
        lat=39.2147,
        lng=-84.6198,
        neighborhood="Colerain Township (West Side)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Gaden Samdrupling Buddhist Monastery (GSL) is a Tibetan Buddhist monastery "
            "of the Gelug school (Gaden lineage), located on Cincinnati's West Side. "
            "The Wednesday 7–8pm Open Meditation is specifically open to the public as "
            "a drop-in silent meditation session — prayer books provided. Friday evenings "
            "offer an Introduction to Buddhism with Ven. Jamyan Lama. Saturday 10am "
            "Dharma Practice (Lama Choepa) is a more liturgical session. One of the "
            "few Tibetan monasteries in the greater Cincinnati/Ohio region."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

# No Cincinnati centers have accessible iCal feeds.
# All sits are seeded as recurring events in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
