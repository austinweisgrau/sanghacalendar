"""
Nashville, TN meditation center sources — Phase 3 expansion.

iCal feeds:
  - One Dharma Nashville: WordPress Events Calendar feed exists but contains only
    multi-day retreats (Southern Dharma, Whistler BC, etc.) — all filtered out
    by filter_to_sits. Regular Monday evening sits seeded as recurring instead.

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - One Dharma Nashville — Mon 7pm (hybrid in-person + online)
    530 26th Ave N, Nashville TN 37209. Insight/Vipassana (Lisa Ernst).
  - Wild Heart Meditation Center — Wed 7pm, Fri 7pm, Sun 9am (in-person + Zoom)
    3123 Gallatin Pike, Nashville TN 37216. Secular/multi-tradition.
  - Nashville Zen Center — Tue 7pm, Sat 7am (zazen, in-person)
    3123 Gallatin Pike, Nashville TN 37216. Soto Zen (Silent Thunder Order).
  - Padmasambhava Buddhist Center of Tennessee — Sun 9:30am (in-person)
    419 East Iris Drive, Nashville TN 37204. Tibetan (Nyingma/Dzogchen).

Research notes (2026-05-12):
  - One Dharma Nashville: onedharmanashville.com — WordPress + The Events Calendar.
    iCal at /events/?ical=1 confirmed working but only retreat events (multi-day,
    out of state). Monday 7pm sits not published in iCal. Seed as recurring.
  - Wild Heart Meditation Center: wildheartmeditationcenter.org — Squarespace.
    Per-event ICS links only; no site-wide iCal. Rich weekly schedule. Seed recurring.
    Co-located with Nashville Zen Center at 3123 Gallatin Pike (East Nashville).
  - Nashville Zen Center: nashvillezencenter.org — Squarespace. Static schedule page,
    no iCal. Tue 7pm + Sat 7am zazen. Soto Zen, Silent Thunder Order lineage.
  - PBC-TN: pbc-tn.org — Wix. No iCal. Sunday 9:30–11am Calm Abiding Meditation.
    Oldest Tibetan dharma center in the region (founded 1990, Nyingma/Dzogchen).
  - Snow Lion Nashville: nashvillemeditates.org — site down/unreachable as of 2026-05-12.
    Was Shambhala but now independent. Sun 10am, Wed 7pm reported schedule — deferred
    until site recovery confirmed.
  - Sitagu Buddhist Monastery (99 Lyle Lane): Burmese Theravada monastery — primarily
    devotional/community functions. No structured public sit calendar. Skip for now.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "one_dharma_nashville": Center(
        id="one_dharma_nashville",
        name="One Dharma Nashville",
        url="https://onedharmanashville.com",
        address="530 26th Ave N",
        city="Nashville",
        state="TN",
        zip_code="37209",
        lat=36.1650,
        lng=-86.8149,
        neighborhood="Germantown / Midtown",
        tradition=Tradition.THERAVADA,
        notes=(
            "One Dharma Nashville is an Insight Meditation community led by guiding teacher "
            "Lisa Ernst. Located in Germantown/Midtown Nashville. Offers weekly Monday "
            "Evening Meditation (7–8:30pm, hybrid in-person + online) featuring guided "
            "meditation, dharma talk, and discussion. Also Friday morning online sit "
            "(7:30–8am via Zoom). 1st and 3rd Thursday evening sits in Franklin, TN "
            "(at The Factory at Franklin). Donation-based, all welcome."
        ),
    ),
    "wild_heart_meditation": Center(
        id="wild_heart_meditation",
        name="Wild Heart Meditation Center",
        url="https://www.wildheartmeditationcenter.org",
        address="3123 Gallatin Pike",
        city="Nashville",
        state="TN",
        zip_code="37216",
        lat=36.2038,
        lng=-86.7178,
        neighborhood="East Nashville / McFerrin Park",
        tradition=Tradition.THERAVADA,
        notes=(
            "Wild Heart Meditation Center is a secular, multi-tradition meditation center "
            "in East Nashville, co-located with Nashville Zen Center. Rooted in Against the "
            "Stream and Dharma Punx lineage; welcoming and inclusive community. Offers "
            "multiple weekly in-person sessions: Wednesday Dharma & Discussion (7–8:30pm), "
            "Friday Dharma & Discussion (7–8:30pm), Sunday Dharma & Discussion (9–10:30am). "
            "Also Monday Recovery Dharma (7pm), Tuesday POC Sangha (1st/3rd Tue), Thursday "
            "Queer Sangha (7pm), and daily morning online sits. All drop-in, no registration."
        ),
    ),
    "nashville_zen_center": Center(
        id="nashville_zen_center",
        name="Nashville Zen Center",
        url="https://nashvillezencenter.org",
        address="3123 Gallatin Pike",
        city="Nashville",
        state="TN",
        zip_code="37216",
        lat=36.2038,
        lng=-86.7178,
        neighborhood="East Nashville / McFerrin Park",
        tradition=Tradition.ZEN,
        notes=(
            "Nashville Zen Center is a Soto Zen community in the Silent Thunder Order, "
            "the lineage of Zengaku Soyu Matsuoka. Located in East Nashville, sharing "
            "space with Wild Heart Meditation Center. Weekly zazen: Tuesday 7pm (newcomers "
            "welcome — arrive at 6:30pm for orientation) and Saturday 7am. Open to all "
            "levels; no experience required. Part of the national Silent Thunder Order "
            "sangha (affiliated with Atlanta Soto Zen Center)."
        ),
    ),
    "pbc_tennessee": Center(
        id="pbc_tennessee",
        name="Padmasambhava Buddhist Center of Tennessee",
        url="https://www.pbc-tn.org",
        address="419 East Iris Drive",
        city="Nashville",
        state="TN",
        zip_code="37204",
        lat=36.1388,
        lng=-86.7903,
        neighborhood="12South / Waverly-Belmont",
        tradition=Tradition.TIBETAN,
        notes=(
            "Padmasambhava Buddhist Center of Tennessee (PBC-TN) is a Tibetan Buddhist "
            "center in the Nyingma tradition (Dzogchen), part of the international PBC "
            "network founded by Venerable Khenchen Palden Sherab Rinpoche. One of the "
            "largest Tibetan dharma groups in the South, established in 1990. Yeshe "
            "Tsogyal Temple is their practice home in the 12South neighborhood of Nashville. "
            "Offers weekly Sunday Calm Abiding Meditation (9:30–11am), open to all — no "
            "Buddhist background required. Also 'Discovering Tibetan Buddhism' classes and "
            "seasonal retreats."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

# One Dharma Nashville iCal exists (WordPress Events Calendar) but contains only
# out-of-area retreat events — all filtered out by filter_to_sits. Regular sits
# are seeded as recurring in sangha-seed-recurring.js instead.
ICAL_FEEDS: dict = {}
