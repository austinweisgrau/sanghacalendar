"""
Tucson, AZ — Phase 3 expansion.

Tucson has a modest Buddhist community. The most accessible center with a
stable, confirmable schedule is KMC Arizona (meditationintucson.org).

Centers included:
  - Kadampa Meditation Center Arizona (kmc_arizona_tucson) — NKT Tibetan
    5326 E. Pima Street, Tucson AZ 85712
    Recurring sits: Sun 10am, Tue 6:30pm, Sat 10am
    Wix site — no accessible iCal; sits seeded as recurring.

Research notes (2026-05-18):
  - KMC Arizona (meditationintucson.org): Wix site, no ?ical=1 feed.
    Confirmed schedule from /gp page: Sun 10am "New Mind, New World" (75 min),
    Tue 6:30pm "Transforming Immobilizing Minds" (75 min),
    Sat 10am "Simply Meditate" (30 min). 5326 E. Pima St, Tucson AZ 85712.
  - Tucson Shambhala (tucson.shambhala.org): redirects to main shambhala.org —
    appears inactive or closed.
  - Rincon Mountain Insight Meditation / Tucson Insight: domains dead — dormant.
  - Old Pueblo Zen: domain dead — no active web presence found.
  - Diamond Way Tucson: domain dead; no AZ centers in global Diamond Way directory.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_arizona_tucson": Center(
        id="kmc_arizona_tucson",
        name="Kadampa Meditation Center Arizona",
        url="https://www.meditationintucson.org",
        address="5326 East Pima Street",
        city="Tucson",
        state="AZ",
        zip_code="85712",
        lat=32.2432,
        lng=-110.8789,
        neighborhood="Midtown / East Tucson",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Arizona (KMC Arizona) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located in Midtown Tucson. Offers weekly "
            "General Program meditation classes open to all: Sunday morning, Tuesday evening, "
            "and a brief Saturday morning drop-in. Classes include guided meditation and "
            "dharma teaching on modern Kadampa Buddhism. No experience necessary; "
            "all are welcome."
        ),
    ),
}

# No iCal feeds — Wix site, not accessible via ?ical=1
ICAL_FEEDS = {}
