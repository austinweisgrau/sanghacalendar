"""
New Mexico meditation center sources — Phase 3 expansion.

Covers Albuquerque (the main metro) and Santa Fe (~60 miles north).

iCal feeds:
  - Albuquerque Shambhala Meditation Center (shambhala-koeln.de center=268)
    244 events: Sunday Public Sitting, Heart of Recovery, Nyinthün, etc.
  - Upaya Zen Center (upaya.org/events/?ical=1) — Santa Fe
    30 events: daily Morning Zazen (7am), Midday Zazen, Evening Zazen (5:30pm),
    Dharma talks, sesshins, and special programs.

Research notes (2026-05-10):
  - Kadampa Albuquerque (meditationinalbuquerque.org): 403/down — skip for now.
  - shenpen.org (Kagyu Shenpen Ösel Chöling): 403 on main site — skip for now.
  - Phoenix Shambhala: CLOSED Dec 31, 2025 — programming continues via ABQ Shambhala.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_albuquerque": Center(
        id="shambhala_albuquerque",
        name="Albuquerque Shambhala Meditation Center",
        url="https://albuquerque.shambhala.org",
        address="1102 Mountain Rd NW",
        city="Albuquerque",
        state="NM",
        zip_code="87102",
        lat=35.0912,
        lng=-106.6616,
        neighborhood="Old Town / Downtown",
        tradition=Tradition.TIBETAN,
        notes=(
            "Albuquerque Shambhala Meditation Center (ASMC) is a Tibetan Buddhist "
            "community in the Shambhala lineage of Chögyam Trungpa Rinpoche. Located "
            "in the Old Town/Downtown corridor of Albuquerque, NM. Offers Sunday Public "
            "Sitting (in-person and online), Heart of Recovery programs, Nyinthün (all-day "
            "group practice), Shambhala Training weekends, and book discussion groups. "
            "Also now hosts programming formerly offered by Phoenix Shambhala (closed "
            "Dec 31, 2025). Free and open to all; donations welcome."
        ),
    ),
    "upaya_zen_center": Center(
        id="upaya_zen_center",
        name="Upaya Zen Center",
        url="https://www.upaya.org",
        address="1404 Cerro Gordo Rd",
        city="Santa Fe",
        state="NM",
        zip_code="87501",
        lat=35.6870,
        lng=-105.9393,
        neighborhood="Canyon Road / Arts District",
        tradition=Tradition.ZEN,
        notes=(
            "Upaya Zen Center is one of the most prominent Soto Zen communities in the "
            "American Southwest, founded by Roshi Joan Halifax in 1990 and located on a "
            "five-acre campus in the foothills of Santa Fe, NM. Offers daily practice "
            "open to visitors: Morning Zazen (7am), Midday Zazen (12:20pm), and Evening "
            "Zazen (5:30pm) — all in the zendo and often available via Zoom. Weekly "
            "Dharma talks (Wed or Thu evenings), periodic sesshins, and transformative "
            "residential retreats including the renowned Being with Dying professional "
            "training. The Chaplaincy Training Program and Socially Engaged Buddhism "
            "initiatives draw practitioners nationwide."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "shambhala_albuquerque": {
        "url": "https://shambhala-koeln.de/ical.php?center=268",
        "filter_to_sits": True,
    },
    "upaya_zen_center": {
        "url": "https://www.upaya.org/events/?ical=1",
        "filter_to_sits": True,
    },
}
