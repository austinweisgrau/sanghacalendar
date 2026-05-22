"""
Spokane, WA — Phase 3 expansion.

Spokane's Buddhist scene is anchored by several distinct lineages: the Zen
Center of Spokane (Diamond Sangha lineage, blending Soto and Rinzai) offers
three weekly sits with a live iCal feed; the Buddhist Institute of Universal
Compassion (BIUC) is an active Gelug Tibetan center running weekly Saturday
and Sunday programs with Zoom; and Chagdud Gonpa Padma Ling is a Nyingma
Tibetan center active since 1990.

Centers included:
  - Zen Center of Spokane (zen_center_spokane) — Zen (Diamond Sangha)
    25 W Main Ave (Saranac Building, 2nd fl), Spokane WA 99201. zencenterspokane.org
    Mon 7am, Wed 7:15pm, Sat 8am. In-person + Zoom. Live iCal feed.

  - Buddhist Institute of Universal Compassion (biuc_spokane) — Tibetan (Gelug)
    728 E Rich Ave, Spokane WA 99207. universalcompassion.org
    Sun 10am–12pm, Sat 9:30am–12pm. In-person + Zoom. No iCal; seeded recurring.

  - Chagdud Gonpa Padma Ling (padma_ling_spokane) — Tibetan (Nyingma)
    1014 W 7th Ave, Spokane WA 99204. chagdudgonpa.org/centers/padma-ling
    Teaches twice a week (days/times not publicly listed). Center since 1990.
    No iCal; seeded recurring once schedule is confirmed — not currently seeded.

Research notes (2026-05-22):
  - Zen Center of Spokane: Diamond Sangha lineage (blends Soto and Rinzai),
    located in the Saranac Building, 25 W Main Ave, 2nd floor, Downtown Spokane.
    Mon 7–7:50am: two 25-min sitting periods + kinhin + sutra recitation.
    Wed 7:15–8:15pm: same format. Sat 8–9:30am: same + dharma reading.
    In-person + Zoom (contact for Zoom link). The Events Calendar iCal feed
    (Tribe Events plugin) is verified working.
  - Buddhist Institute of Universal Compassion: Gelug Tibetan Buddhist center
    opened 2017, led by Venerable Geshe Thupten Phelgye. Located at 728 E Rich
    Ave, Spokane WA 99207. Saturday 9:30am–12pm and Sunday 10am–12pm: meditation
    and teachings. Both sessions available in-person and on Zoom
    (ID: 890 7744 2439). No iCal; seeded as recurring.
  - Chagdud Gonpa Padma Ling: Nyingma Tibetan Buddhist center founded 1990,
    resident Lama Inge Zangmo. At 1014 W 7th Ave. Schedule not published online
    ("being updated, check back soon"). Yelp shows activity September 2025.
    Skip seeding until schedule is confirmed via direct contact.
  - Tsinta Mani Choling: Nyingma Tibetan center, Lama Lakshey Zangpo, Rinpoche.
    2902 N East Oval Ave. Schedule unconfirmed; not added.
  - Spokane Buddhist Temple: Jodo Shinshu (Pure Land) — devotional tradition,
    not meditation-sit focused; not added.
  - Sravasti Abbey Monday sits: online-only (Zoom); no physical Spokane location.
  - Kadampa: nearest branch is in Coeur d'Alene, ID (30 min away); not Spokane.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "zen_center_spokane": Center(
        id="zen_center_spokane",
        name="Zen Center of Spokane",
        url="https://zencenterspokane.org",
        address="25 W Main Ave, Suite 200",
        city="Spokane",
        state="WA",
        zip_code="99201",
        lat=47.6590,
        lng=-117.4260,
        neighborhood="Downtown Spokane",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Center of Spokane is a Diamond Sangha community (blending Soto "
            "and Rinzai Zen), located in the Saranac Building, 25 W Main Ave, 2nd "
            "floor. Monday Morning (7–7:50 AM): two 25-min sitting periods, kinhin, "
            "and sutra recitation. Wednesday Evening (7:15–8:15 PM): same format. "
            "Saturday Morning (8–9:30 AM): sitting, kinhin, sutra, and dharma "
            "reading. All sessions in-person + Zoom. Drop-in welcome."
        ),
    ),
    "biuc_spokane": Center(
        id="biuc_spokane",
        name="Buddhist Institute of Universal Compassion",
        url="https://www.universalcompassion.org",
        address="728 E Rich Ave",
        city="Spokane",
        state="WA",
        zip_code="99207",
        lat=47.6608,
        lng=-117.3812,
        neighborhood="East Spokane",
        tradition=Tradition.TIBETAN,
        notes=(
            "Buddhist Institute of Universal Compassion (BIUC) is a Gelug Tibetan "
            "Buddhist center in Spokane, founded 2017 and led by Venerable Geshe "
            "Thupten Phelgye. Located at 728 E Rich Ave. Saturday (9:30 AM–12 PM): "
            "meditation and teachings. Sunday (10 AM–12 PM): meditation and teachings. "
            "Both sessions offered in-person and on Zoom (ID: 890 7744 2439). "
            "Open to all; dana-based."
        ),
    ),
    "padma_ling_spokane": Center(
        id="padma_ling_spokane",
        name="Chagdud Gonpa Padma Ling",
        url="https://www.chagdudgonpa.org/centers/padma-ling",
        address="1014 W 7th Ave",
        city="Spokane",
        state="WA",
        zip_code="99204",
        lat=47.6496,
        lng=-117.4273,
        neighborhood="South Hill",
        tradition=Tradition.TIBETAN,
        notes=(
            "Chagdud Gonpa Padma Ling is a Nyingma Tibetan Buddhist center in "
            "Spokane, active since 1990. Resident Lama Inge Zangmo offers "
            "teachings twice weekly; specific schedule available via direct "
            "contact at padmaling21@gmail.com or (509) 747-1559. Part of the "
            "Chagdud Gonpa Foundation."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "zen_center_spokane": {
        "url": "https://zencenterspokane.org/?post_type=tribe_events&ical=1&eventDisplay=list",
        "filter_to_sits": True,
    },
}
