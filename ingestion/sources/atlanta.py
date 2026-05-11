"""
Atlanta, GA meditation center sources — Phase 3 expansion.

iCal feeds:
  - Atlanta Shambhala Meditation Center (shambhala_atlanta)
    Cologne iCal server: shambhala-koeln.de/ical.php?center=196 — 372 events.
    Drop-in sits: Fri 12pm, Sun 10am, Tue 7pm. One Breath Group Mon/Wed/Thu.
    Also: BIPOC Sangha, Queer Dharma, Shambhala Training weekends.
    Address: 1447 Church St, Decatur GA 30030 (unincorporated DeKalb, in Atlanta metro)

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - Atlanta Soto Zen Center (aszc): daily 6am, Wed 7pm, Sun 9am
    (Squarespace site, no iCal — schedule from aszc.org)
  - Kadampa Meditation Center Georgia (kmc_georgia): Sun 10:30am, Tue 7pm, Wed 7pm
    (Squarespace site, no iCal — schedule from meditationingeorgia.org)

Research notes (2026-05-11):
  - Drepung Loseling Institute (1781 Dresden Dr, Atlanta GA 30319): major Tibetan Buddhist
    institution. Static HTML table calendar at drepung.org/changing/calendar/current.htm.
    Drop-in sits: Sun 11am (Beginner's Meditation), Thu 7pm (public talk + practice).
    Deferred — needs monthly HTML scraper. High priority for heartbeat 24.
  - Red Clay Sangha (Chamblee, GA): multi-tradition, active, RSS feed exists but no confirmed
    iCal. Worth investigating.
  - Atlanta Insight Meditation Community (atlinsight.org): small Squarespace community.
    Tue 6:30pm + Thu 8am (Zoom-only satsang). Low priority.
  - Diamond Way Atlanta: no active center found.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_atlanta": Center(
        id="shambhala_atlanta",
        name="Atlanta Shambhala Meditation Center",
        url="https://atlanta.shambhala.org",
        address="1447 Church St",
        city="Decatur",
        state="GA",
        zip_code="30030",
        lat=33.7763,
        lng=-84.2960,
        neighborhood="Decatur / Atlanta metro",
        tradition=Tradition.TIBETAN,
        notes=(
            "Atlanta Shambhala Meditation Center is a contemplative community in the Shambhala "
            "lineage of Chögyam Trungpa Rinpoche, located in a charming bungalow in Decatur "
            "(just east of Atlanta proper). Offers drop-in public meditation on Sundays "
            "(10am–noon), Tuesdays (7–8:30pm), and Fridays (noon–1pm). Also hosts the One "
            "Breath Group (Mon/Wed/Thu), monthly BIPOC Sangha, monthly Queer Dharma group, "
            "and Shambhala Training weekends. Open to all; drop-in welcome."
        ),
    ),
    "aszc": Center(
        id="aszc",
        name="Atlanta Soto Zen Center",
        url="https://www.aszc.org",
        address="1167 Zonolite Pl NE, Suite C",
        city="Atlanta",
        state="GA",
        zip_code="30306",
        lat=33.8060,
        lng=-84.3420,
        neighborhood="Morningside / Lenox",
        tradition=Tradition.ZEN,
        notes=(
            "Atlanta Soto Zen Center (ASZC) is one of Atlanta's longest-running Zen centers, "
            "founded in 1977 in the Soto Zen tradition. Offers daily zazen including a morning "
            "Sunrise Sangha (6am, hybrid in-person + Zoom), Wednesday evening Introduction to "
            "Zen Meditation (7–8:30pm, in-person drop-in), and Sunday Morning Service (9am–noon, "
            "hybrid). Monthly Just Sit Saturdays and Roshi seminars. Located in Morningside "
            "near Piedmont Park. Drop-in welcome; newcomers' orientation offered monthly."
        ),
    ),
    "kmc_georgia": Center(
        id="kmc_georgia",
        name="Kadampa Meditation Center Georgia",
        url="https://www.meditationingeorgia.org",
        address="741 Edgewood Ave NE",
        city="Atlanta",
        state="GA",
        zip_code="30307",
        lat=33.7565,
        lng=-84.3560,
        neighborhood="Inman Park / Old Fourth Ward",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Georgia (KMC Georgia) is a Tibetan Buddhist center in the "
            "New Kadampa Tradition (NKT-IKBU), located in the Inman Park neighborhood near "
            "BeltLine access. Offers weekly drop-in General Program classes: Sunday 'Advice for "
            "a Happy Life' (10:30–11:45am), Tuesday 'Meditation for Beginners' (7–8pm), and "
            "Wednesday 'Modern Buddhism and Meditation' (7–8:15pm). All sessions include guided "
            "meditation and Buddhist teachings. Drop-in fee: $15 general, $5 students/seniors, "
            "free for members."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "shambhala_atlanta": {
        "url": "https://shambhala-koeln.de/ical.php?center=196",
        "center_id": "shambhala_atlanta",
        "filter_to_sits": True,
    },
}
