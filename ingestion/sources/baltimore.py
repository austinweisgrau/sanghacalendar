"""
Baltimore, MD meditation center sources — Phase 3 expansion.

iCal feeds:
  None confirmed for Baltimore metro — Shambhala central iCal server (shambhala-koeln.de)
  returns 522 (connection timeout) for center=201, same as other Shambhala centers.
  KMC Maryland uses Squarespace with no site-wide iCal feed.
  Baltimore Dharma Group uses Wix with no iCal.

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - Baltimore Shambhala Centre — Sat (2nd & 4th) 9am hybrid in-person + Zoom
    33 W 33rd St (YMCA), Baltimore, MD 21218. Shambhala / Tibetan.
  - Baltimore Shambhala Centre — Mon–Fri 7am Morning Sitting (Zoom only)
    Shambhala / Tibetan.
  - KMC Maryland — Wed 11am, Wed 6pm, Thu 6:30pm, Sun 10:30am (in-person)
    901 Dartmouth Road, Baltimore, MD 21212. Tibetan (Kadampa/NKT).
  - KMC Maryland Canton — Tue 7pm (in-person)
    Church on the Square, 1025 S Potomac St, Baltimore, MD 21224.
  - Baltimore Dharma Group — Sun 8am zazen (in-person)
    3107 N Charles St (Homewood Friends Meeting), Baltimore, MD 21218. Soto Zen.
  - Baltimore Dharma Group — Thu 7pm zazen / dharma (in-person)
    3107 N Charles St, Baltimore, MD 21218. Soto Zen.

Research notes (2026-05-13):
  - Baltimore Shambhala Centre: shambhala-koeln.de/ical.php?center=201 returns
    522 error (same as DC 205, Boulder 191, Denver 218). Shambhala central server
    appears offline for most centers. Seeded biweekly Saturday sit (2nd/4th Sat 9am)
    from website schedule. Meets at 33rd Street YMCA, Baltimore MD 21218.
    Schedule also includes Mon-Fri 7-8am morning sit (Zoom), Sun 9-9:30am (Zoom),
    Tue Heart of Recovery (Zoom), Thu Lojong Study (Zoom). Only hybrid/in-person
    sits seeded; pure Zoom sits noted for future.
  - KMC Maryland (meditationmd.org): Squarespace site. 901 Dartmouth Rd, Roland Park,
    Baltimore MD 21212. Active multi-session schedule: Wed 11am + 6pm, Thu 6:30pm,
    Sun 10:30am. Also branch at Canton (1025 S Potomac St, Tue 7pm) and Columbia
    (Owen Brown Interfaith Center, Tue 7:30pm). $12/class or first class free;
    no experience required. Classes have "Meditations for X" style names.
  - Baltimore Dharma Group (baltimoredharmagroup.org): Wix site. Meets at Homewood
    Friends Meeting House, 3107 N Charles St, Baltimore MD 21218. Small lay Soto Zen
    community. Sun 8am (two 30-min zazen periods + kinhin, arrive 7:55). Thu evenings
    alternating dharma class and open zazen (~7pm). Free, all welcome.
  - Gampopa Center (Annapolis, 30 mi south): Kagyu Tibetan center at 918 Chesapeake
    Ave, Annapolis MD 21401. Deferred to future Annapolis expansion.
  - Columbia Insight Meditation Group (Ellicott City, 25 mi SW): IMCW affiliate at
    Centennial High School, Wed 7pm. School-year dependent. Deferred.
  - Burning House Zendo (Westminster, 40 mi): Friday in-person sits canceled until
    July 2026. Deferred; monitor for resumption.
  - Clare Sangha (Reisterstown, MD): Primarily online Zen community. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "baltimore_shambhala": Center(
        id="baltimore_shambhala",
        name="Baltimore Shambhala Centre",
        url="https://baltimore.shambhala.org",
        address="33 W 33rd St",
        city="Baltimore",
        state="MD",
        zip_code="21218",
        lat=39.3277,
        lng=-76.6093,
        neighborhood="Charles Village (33rd Street YMCA)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Baltimore Shambhala Centre is a community in the Shambhala lineage of "
            "Chögyam Trungpa Rinpoche and Sakyong Mipham Rinpoche, meeting at the "
            "YMCA on 33rd Street in the Charles Village neighborhood. Regular public "
            "offerings include biweekly in-person meditation (2nd & 4th Saturdays, "
            "9–10am, hybrid in-person + Zoom) and weekday morning sittings (Mon–Fri "
            "7–8am, Zoom). Sunday morning sitting (9–9:30am, Zoom) and Thursday "
            "Lojong Study Group also offered. Free and open to all."
        ),
    ),
    "kmc_maryland": Center(
        id="kmc_maryland",
        name="Kadampa Meditation Center Maryland",
        url="https://www.meditationmd.org",
        address="901 Dartmouth Road",
        city="Baltimore",
        state="MD",
        zip_code="21212",
        lat=39.3562,
        lng=-76.6383,
        neighborhood="Roland Park",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Maryland (KMC Maryland) is a New Kadampa "
            "Tradition center in Roland Park, north Baltimore. Offers multiple weekly "
            "drop-in classes: Sunday Meditations for Modern Life (10:30–11:45am), "
            "Wednesday Meditations for Modern Life (11am–noon) and World Peace "
            "Meditation (6–7pm), Thursday Meditations for Modern Life (6:30–7:45pm). "
            "Also Canton branch (1025 S Potomac St) Tuesdays 7–8pm. No Buddhist "
            "background required; first class free, $12 thereafter. Part of the "
            "Kadampa (NKT) international network."
        ),
    ),
    "kmc_maryland_canton": Center(
        id="kmc_maryland_canton",
        name="Kadampa Meditation Center Maryland — Canton",
        url="https://www.meditationmd.org",
        address="1025 S Potomac St",
        city="Baltimore",
        state="MD",
        zip_code="21224",
        lat=39.2848,
        lng=-76.5758,
        neighborhood="Canton",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Maryland Canton branch, meeting at Church on "
            "the Square (1025 S Potomac St) in the Canton neighborhood of southeast "
            "Baltimore. Weekly Tuesday meditation class (7–8pm), open to all levels. "
            "No Buddhist background required; first class free, $12 thereafter. "
            "Affiliated with KMC Maryland (meditationmd.org)."
        ),
    ),
    "baltimore_dharma_group": Center(
        id="baltimore_dharma_group",
        name="Baltimore Dharma Group",
        url="https://www.baltimoredharmagroup.org",
        address="3107 N Charles St",
        city="Baltimore",
        state="MD",
        zip_code="21218",
        lat=39.3262,
        lng=-76.6202,
        neighborhood="Guilford / Charles Village (Homewood Friends Meeting)",
        tradition=Tradition.ZEN,
        notes=(
            "Baltimore Dharma Group is a small lay Soto Zen sangha meeting at "
            "Homewood Friends Meeting House (3107 N Charles St, Baltimore). "
            "Weekly Sunday morning zazen (8–9:30am): two thirty-minute zazen "
            "periods with kinhin walking meditation — arrive by 7:55am. Thursday "
            "evening alternates between dharma class and open zazen (two 30-min "
            "periods + kinhin, or a 30-min sit with discussion). Shikantaza "
            "(just sitting) style. All levels welcome; free."
        ),
    ),
}

# No accessible iCal feeds for Baltimore-area centers
ICAL_FEEDS: dict = {}
