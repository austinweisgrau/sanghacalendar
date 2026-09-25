"""
Worcester, MA — Phase 3 expansion.

Worcester is Massachusetts's second-largest city (~200k), about 40 miles west
of Boston. The Buddhist scene is modest but genuine, anchored by one of New
England's most active Zen temples.

Centers included:
  - Boundless Way Zen Temple / Mugendo-ji (boundless_way_worcester)
    — Soto/Rinzai Zen fusion
    1030 Pleasant Street, Worcester MA 01602. boundlessway.org
    Mon 7–8:30pm hybrid, Wed 7–8pm hybrid, Sun 7–8:30pm hybrid
    iCal blocked by Mod_Security; recurring sits seeded.

  - New England Buddhist Vihara / Boston Buddhist Vihara (new_england_buddhist_vihara)
    — Sri Lankan Theravada
    162 Old Upton Road, Grafton MA 01519. nebvmc.org
    Wed 7–8:30pm in-person English meditation + dharma talk
    No iCal; recurring sit seeded.

Research notes (2026-09-25):
  - Boundless Way: iCal blocked (Mod_Security 406). Home page calendar lists
    Monday and Wednesday evenings as hybrid in-person + Zoom, Sunday evening
    hybrid. Tuesday evenings listed as online-only. Morning practice (7am daily)
    also available but online-only per site. Only in-person/hybrid sessions seeded.
    Temple founded mid-1990s; Guiding Teachers Melissa Myozen Blacker Roshi +
    David Dae An Rynick Roshi. SZBA & AZA member. Active sesshin program.
  - NEBVM: Also known as Boston Buddhist Vihara. Sri Lankan Theravada, est. 2004.
    Led by Ven. Aluthgama Dhammajothi Thero. Wed 7–8:30pm English guided
    meditation + dharma talk. Full moon day-long celebrations. Grafton is ~10
    miles south of Worcester city center; functionally Worcester metro.
  - Atisha Kadampa Worcester class (Thu 6:30pm): Zoom-only branch of Atisha KBC
    Providence RI. Skipped — no in-person Worcester component.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "boundless_way_worcester": Center(
        id="boundless_way_worcester",
        name="Boundless Way Zen Temple",
        url="https://boundlessway.org",
        address="1030 Pleasant Street",
        city="Worcester",
        state="MA",
        zip_code="01602",
        lat=42.2568,
        lng=-71.8012,
        neighborhood="South Worcester",
        tradition=Tradition.ZEN,
        notes=(
            "Boundless Way Zen Temple (temple name Mugendo-ji) is one of New England's "
            "most active Zen practice centers, located in Worcester, MA. Guiding "
            "Teachers Melissa Myozen Blacker Roshi and David Dae An Rynick Roshi blend "
            "Soto and Rinzai Zen lineages. The temple offers daily practice including "
            "hybrid in-person + Zoom evening sittings on Monday (7:00–8:30 PM), "
            "Wednesday (7:00–8:00 PM), and Sunday (7:00–8:30 PM). Dharma talks and "
            "dokusan (individual teacher meetings) available regularly. 12–14 sesshins "
            "per year including residential intensives. Member of the Soto Zen Buddhist "
            "Association (SZBA) and American Zen Teachers Association (AZTA). All are "
            "welcome; no experience required. boundlessway.org."
        ),
    ),
    "new_england_buddhist_vihara": Center(
        id="new_england_buddhist_vihara",
        name="New England Buddhist Vihara",
        url="https://www.nebvmc.org",
        address="162 Old Upton Road",
        city="Grafton",
        state="MA",
        zip_code="01519",
        lat=42.1993,
        lng=-71.6748,
        neighborhood="Grafton (Worcester metro)",
        tradition=Tradition.THERAVADA,
        notes=(
            "New England Buddhist Vihara and Meditation Center (also known as Boston "
            "Buddhist Vihara) is a Sri Lankan Theravada temple in Grafton, MA, about "
            "10 miles south of Worcester. Founded in 2004 by Venerable Aluthgama "
            "Dhammajothi Thero. Serves over 100 families across New England. Weekly "
            "English-language Guided Meditation and Dharma Talk every Wednesday "
            "7:00–8:30 PM — open to all, no experience required. Full moon day-long "
            "celebrations (poya days) monthly. Free. Phone: (508) 839-5038. "
            "information@nebvmc.org. nebvmc.org."
        ),
    ),
}

# No live iCal feeds available — all sits seeded as recurring in
# scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
