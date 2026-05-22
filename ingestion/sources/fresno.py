"""
Fresno, CA — Phase 3 expansion.

Fresno's Buddhist scene is anchored by two active centers offering regular
public sits: the Zen Center of Fresno (Soto Zen, Central Valley Zen Foundation)
holds Saturday morning zazen, and Fresno Buddhist Temple (Jodo Shinshu) offers
Sunday morning and Thursday evening meditation open to all.

Centers included:
  - Zen Center of Fresno (zen_center_fresno) — Zen (Soto)
    371 E. Bullard Ave., Suite 102, Fresno CA 93710. zenfresno.org
    Sat 9am (zazen + kinhin + dharma talk). No iCal; seeded recurring.

  - Fresno Buddhist Temple / Fresno Betsuin (fresno_buddhist_temple) — Other (Jodo Shinshu)
    2690 E. Alluvial Ave., Fresno CA 93720. fresnobuddhisttemple.org
    Sun 8:30am (Sunday Meditation Class) + Thu 7pm (Evening Meditation, hybrid).
    No iCal; seeded recurring.

Research notes (2026-05-22):
  - No Kadampa/NKT center in Fresno or Central Valley.
  - No Shambhala center in Fresno.
  - No Insight Meditation / Vipassana weekly sangha found.
  - Fresno River Zen / Empty Nest Zendo: historical listing; address now a Catholic
    church; appears absorbed into Zen Center of Fresno. Not added.
  - Mrauk Oo Dhamma Center (Burmese Theravada, 1340 Kern St): primarily serves
    Myanmar community; public accessibility unclear. Deferred.
  - California Vipassana Center (North Fork, 1 hr north): 10-day residential
    Goenka courses only, no drop-in sits. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "zen_center_fresno": Center(
        id="zen_center_fresno",
        name="Zen Center of Fresno",
        url="https://zenfresno.org",
        address="371 E. Bullard Ave., Suite 102",
        city="Fresno",
        state="CA",
        zip_code="93710",
        lat=36.8240,
        lng=-119.7965,
        neighborhood="Central Fresno",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Center of Fresno is part of the Central Valley Zen Foundation, "
            "in the Soto Zen lineage of Suzuki Roshi and Eihei Dogen. Saturday "
            "mornings (9–11 AM): two 25-minute zazen periods with kinhin, "
            "followed by a dharma talk at 10 AM and closing vows at 11 AM. "
            "Drop-in welcome; no reservation required. Teacher: Soshin Bruce "
            "Jewell (transmitted Soto teacher). Abbess: Myoan Grace Schireson."
        ),
    ),
    "fresno_buddhist_temple": Center(
        id="fresno_buddhist_temple",
        name="Fresno Buddhist Temple",
        url="https://fresnobuddhisttemple.org",
        address="2690 E. Alluvial Ave.",
        city="Fresno",
        state="CA",
        zip_code="93720",
        lat=36.8776,
        lng=-119.7590,
        neighborhood="Northeast Fresno",
        tradition=Tradition.OTHER,
        notes=(
            "Fresno Buddhist Temple (Fresno Betsuin) is a Jodo Shinshu "
            "(Pure Land) temple of the Buddhist Churches of America, offering "
            "structured public meditation sits. Sunday Meditation Class "
            "(8:30–9:15 AM): sitting and walking meditation in the Hondo, "
            "open to all. Thursday Evening Meditation with Rev. Kaz "
            "(7–7:45 PM): hybrid in-person + Zoom; email temple for Zoom "
            "link. No reservation required; donations welcome."
        ),
    ),
}

# No live iCal feeds for Fresno centers — all sits seeded as recurring.
ICAL_FEEDS: dict = {}
