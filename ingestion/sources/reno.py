"""
Reno / Northern Nevada — Phase 3 expansion (heartbeat 89).

Reno (pop. ~500k metro, Washoe County) is Nevada's second-largest metro and home
to a small but diverse Buddhist community spanning Theravada/Insight, Zen, Tibetan
(FPMT), and non-sectarian/Pure Land lineages. The University of Nevada, Reno gives
the city a more academic and spiritually curious character than Las Vegas.

Centers included:
  - Dharma Zephyr Insight Meditation Community (dharma_zephyr_reno)
    Theravada / Insight Meditation (coalition of sitting groups)
    Reno group: St. John's Episcopal Church, 1070 West Plumb Lane, Reno NV 89509
    dharmazephyr.org · Monday 6:30–8:15pm

  - Reno Buddhist Center (reno_buddhist_center)
    Non-sectarian / Jodo Shinshu Pure Land
    820 Plumas Street, Reno, NV 89509
    renobuddhistcenter.org · Thursday 6–7pm Golden Light Meditation

  - Facing the Mountain Zen Group (facing_mountain_zen)
    Soto Zen / SFZC Branching Streams affiliate
    Reno, NV (address not published on website; JS-rendered site)
    facingthemountain.org · Tuesday evenings (zazen + dharma talk)

  - Dharmakaya Buddhist Center (dharmakaya_reno)
    Tibetan (FPMT / Gelug) study and meditation group
    140 Washington Street, Suite LL30, Reno, NV 89503
    dharmakayacenter.com · 1st/2nd/4th Sundays 9am

Research notes (2026-07-19):
  - Dharma Zephyr: Coalition of Vipassana sitting groups in Northern Nevada
    (Reno, Carson City, Minden/Gardnerville, Tahoe). Reno group meets Mondays
    6:30–8:15pm at St. John's Episcopal Church, 1070 West Plumb Lane, Reno NV 89509.
    Contact: Dionne, 775-771-3435. dharmazephyr.org.
  - Reno Buddhist Center: 29+ year old center at 820 Plumas St, Reno NV 89509.
    Non-sectarian with Jodo Shinshu roots. Thursday Golden Light Meditation 6–7pm
    (traditional sitting + walking meditation, clear intention). Also regular
    Buddhist services, chanting, sutra study. renobuddhistcenter.org.
  - Facing the Mountain Zen Group: Soto Zen sangha founded ~2014, SFZC Branching
    Streams affiliate. Led by Rev. Sekibu Alice Tulloch. Meets Tuesday evenings for
    zazen and dharma talk. Website is Next.js client-rendered; physical address not
    available via scraping. facingthemountain.org.
  - Dharmakaya Buddhist Center: FPMT (Foundation for the Preservation of the
    Mahayana Tradition) study group at 140 Washington St Suite LL30, Reno NV 89503.
    Tibetan Buddhist (Gelug). Drop-in meditation and Buddhist philosophy classes.
    1st, 2nd & 4th Sundays 9am (per Meetup). Monthly membership model ($50/month)
    but drop-in also offered. dharmakayacenter.com.
  - Tahoe-Reno Kapala Mandala (645 Sierra Rose Dr Suite 201, Reno): Tara Mandala /
    Chöd lineage (Lama Tsultrim Allione). Local study group for Kapala training;
    no regular public sits verified. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "dharma_zephyr_reno": Center(
        id="dharma_zephyr_reno",
        name="Dharma Zephyr Insight Meditation Community",
        url="https://dharmazephyr.org",
        address="1070 West Plumb Lane",
        city="Reno",
        state="NV",
        zip_code="89509",
        lat=39.5074,
        lng=-119.8273,
        neighborhood="Southwest Reno",
        tradition=Tradition.THERAVADA,
        notes=(
            "Dharma Zephyr Insight Meditation Community is a coalition of Vipassana "
            "(Insight Meditation) sitting groups in Northern Nevada, including groups "
            "in Reno, Carson City, Minden/Gardnerville, and Lake Tahoe. The Reno "
            "sitting group meets Monday evenings 6:30–8:15pm at St. John's Episcopal "
            "Church, 1070 West Plumb Lane, Reno NV 89509. Program includes guided "
            "and silent sitting meditation, walking meditation, and dharma discussion. "
            "All are welcome; dana-based. Contact: Dionne, 775-771-3435. "
            "dharmazephyr.org."
        ),
    ),
    "reno_buddhist_center": Center(
        id="reno_buddhist_center",
        name="Reno Buddhist Center",
        url="https://www.renobuddhistcenter.org",
        address="820 Plumas Street",
        city="Reno",
        state="NV",
        zip_code="89509",
        lat=39.5182,
        lng=-119.8195,
        neighborhood="Midtown Reno",
        tradition=Tradition.OTHER,
        notes=(
            "Reno Buddhist Center (RBC) is a 29-year-old non-sectarian Buddhist "
            "center at 820 Plumas Street, Reno NV 89509, with roots in Jodo Shinshu "
            "(Pure Land) tradition. Offers the Thursday Golden Light Meditation "
            "(6–7pm): traditional sitting and walking meditation with clear intention, "
            "open to all, free. Also holds twice-monthly Buddhist services, chanting, "
            "sutra study, and visiting teachers for yoga, Tai Chi, Qigong, and "
            "Feldenkrais. renobuddhistcenter.org."
        ),
    ),
    "facing_mountain_zen": Center(
        id="facing_mountain_zen",
        name="Facing the Mountain Zen Group",
        url="https://www.facingthemountain.org",
        address="Reno",
        city="Reno",
        state="NV",
        zip_code="89501",
        lat=39.5296,
        lng=-119.8138,
        neighborhood="Reno",
        tradition=Tradition.ZEN,
        notes=(
            "Facing the Mountain Zen Group is a Soto Zen sangha in Reno, Nevada, "
            "founded around 2014 and affiliated with San Francisco Zen Center's "
            "Branching Streams network. Led by Rev. Sekibu Alice Tulloch. Meets "
            "weekly on Tuesday evenings for zazen and a dharma talk/lecture. "
            "Physical meeting address available at facingthemountain.org. "
            "facingthemountain.org."
        ),
    ),
    "dharmakaya_reno": Center(
        id="dharmakaya_reno",
        name="Dharmakaya Buddhist Center",
        url="https://www.dharmakayacenter.com",
        address="140 Washington Street, Suite LL30",
        city="Reno",
        state="NV",
        zip_code="89503",
        lat=39.5247,
        lng=-119.8142,
        neighborhood="Downtown Reno",
        tradition=Tradition.TIBETAN,
        notes=(
            "Dharmakaya Buddhist Center is an FPMT (Foundation for the Preservation "
            "of the Mahayana Tradition) study and meditation group at 140 Washington "
            "Street, Suite LL30, Reno NV 89503. Tibetan Buddhist (Gelug lineage). "
            "Offers drop-in meditation and Buddhist philosophy classes including the "
            "Tonglen (giving and taking) practice; also hosts weekend retreats and "
            "Saturday workshops. Regular study group meets 1st, 2nd, and 4th Sundays "
            "at 9am. Monthly membership available ($50/month, all programs included) "
            "or drop-in. dharmakayacenter.com."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

# No iCal feeds verified for Reno centers. All sits seeded as recurring.
ICAL_FEEDS: dict = {}
