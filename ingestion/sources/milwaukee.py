"""
Milwaukee, Wisconsin — Phase 3 expansion (heartbeat 83).

Milwaukee (pop. ~590K city / ~1.6M metro) is the largest city in Wisconsin.
Its Buddhist community is anchored by the Milwaukee Zen Center (Soto Zen, one
of the oldest and most active Zen centers in the Midwest) and the Shambhala
Meditation Center.

Centers included:
  - Milwaukee Shambhala Meditation Center (shambhala_milwaukee)
    Shambhala (Chögyam Trungpa lineage)
    2344 N. Oakland Avenue, Milwaukee WI 53211 (East Side)
    milwaukee.shambhala.org · Live iCal feed (center=207, 428 events)

  - Milwaukee Zen Center (milwaukee_zen_center)
    Soto Zen (Suzuki/Katagiri lineage)
    2825 N. Stowell Avenue, Milwaukee WI 53211 (East Side)
    milwaukeezencenter.org
    Wed 6:30pm, Sat 7:30am, Sun 9:30am — seeded as recurring sits
    Also weekday mornings M-F 6:15am (very early; seeded as weekday sit)

Research notes (2026-07-01):
  - Milwaukee Shambhala: 2344 N. Oakland Ave, East Side neighborhood.
    Shambhala Cologne iCal server center=207 verified working (428 events).
    Public sits include: Café Shambhala (weekly Sunday morning), Tuesday evening
    meditation, Shambhala Training weekends, and special programs.
    milwaukee.shambhala.org.
  - Milwaukee Zen Center: 2825 N. Stowell Ave, Milwaukee WI 53211-3775.
    Soto Zen in the tradition of Tozen Akiyama, Tonen O'Connor, and Hoko Karnegis.
    Resident teacher: Reirin Alheidis Gumbel. 414-963-0526.
    Full schedule: weekday mornings M-F 6:15am zazen; Wed 6:30pm (drop-in, beginner
    instruction available); Sat 7:30am–10:15am (zazen + service + reading group);
    Sun 8:20am intro to zazen, 9:30am zazen + dharma talk. No iCal feed detected —
    milwaukeezencenter.org is a static HTML site. Seeded as recurring sits.
    milwaukeezencenter.org.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_milwaukee": Center(
        id="shambhala_milwaukee",
        name="Shambhala Meditation Center of Milwaukee",
        url="https://milwaukee.shambhala.org",
        address="2344 N. Oakland Avenue",
        city="Milwaukee",
        state="WI",
        zip_code="53211",
        lat=43.0693,
        lng=-87.8900,
        neighborhood="East Side",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Center of Milwaukee offers weekly meditation "
            "and dharma study rooted in the Shambhala Buddhist tradition of "
            "Chögyam Trungpa Rinpoche. Programs include Café Shambhala (drop-in "
            "Sunday morning meditation and community), Tuesday evening meditation, "
            "Shambhala Training weekends, and special programs. Open to all — "
            "no experience required. 2344 N. Oakland Avenue, Milwaukee WI 53211. "
            "milwaukee.shambhala.org."
        ),
    ),
    "milwaukee_zen_center": Center(
        id="milwaukee_zen_center",
        name="Milwaukee Zen Center",
        url="https://www.milwaukeezencenter.org",
        address="2825 N. Stowell Avenue",
        city="Milwaukee",
        state="WI",
        zip_code="53211",
        lat=43.0748,
        lng=-87.8935,
        neighborhood="East Side",
        tradition=Tradition.ZEN,
        notes=(
            "Milwaukee Zen Center is a Soto Zen center offering shikantaza ('just "
            "sitting') in the tradition of Tozen Akiyama, Tonen O'Connor, Hoko "
            "Karnegis, and the broader Soto Zen lineage. Resident teacher: Reirin "
            "Alheidis Gumbel. Weekly public schedule: weekday mornings M–F 6:15am "
            "zazen; Wednesday 6:30pm drop-in zazen (beginner instruction first 10 "
            "min); Saturday 7:30am zazen + service + reading group through 10:15am; "
            "Sunday 8:20am Intro to Zazen (free) + 9:30am zazen and dharma talk. "
            "No preregistration required; no charge (donations welcome). "
            "2825 N. Stowell Avenue, Milwaukee WI 53211. 414-963-0526. "
            "milwaukeezencenter.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "shambhala_milwaukee": {
        # Shambhala central iCal server (shambhala-koeln.de), center=207.
        # Verified working 2026-07-01: 428 events.
        # Events include Café Shambhala, Tuesday evening meditation, training weekends.
        "url": "https://shambhala-koeln.de/ical.php?center=207",
        "filter_to_sits": False,
    },
}
