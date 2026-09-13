"""
Fargo-Moorhead metro — Phase 3 expansion.

The Fargo-Moorhead metro straddles the ND/MN border (~240k combined).
Buddhist activity centers on Open Land Sangha, a lay Soto Zen community
in Downtown Moorhead, MN.

Centers included:
  - open_land_sangha — Soto Zen (lay-led, Mt. Equity Sangha affiliation)
    Downtown Moorhead, MN. openlandsangha.org.
    Mon 7–8:30pm CT (Zoom only), Wed 7–8:30pm CT (hybrid in-person + Zoom)
    No iCal (Wix site); recurring sits seeded.

Research notes (2026-09-13):
  - Open Land Sangha: Founded February 2018 by Nancy Nanshin White, a lay
    teacher authorized in the Soto Zen lineage of Rev. Patricia Dai-En
    Bennage Roshi (Mt. Equity Zendo, Pennsdale PA). The Fargo-Moorhead group
    IS the local Mt. Equity Sangha chapter. Meets in-person Wednesday evenings
    in Downtown Moorhead + Zoom; Monday evenings Zoom only; 2nd+4th Friday
    mornings Zoom only. Before joining, contact for a short intro session.
    Website: openlandsangha.org (Wix, JS-heavy, no iCal endpoint).
  - North Dakota Buddhist Vihara: Theravada, P.O. Box 5152 Fargo ND 58105.
    Website (ndbv.org) was unreachable in Sept 2026. Monthly events only
    (not a regular weekly sit schedule). Skip pending website recovery.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "open_land_sangha": Center(
        id="open_land_sangha",
        name="Open Land Sangha",
        url="https://www.openlandsangha.org",
        address="Downtown Moorhead",
        city="Moorhead",
        state="MN",
        zip_code="56560",
        lat=46.8738,
        lng=-96.7678,
        neighborhood="Downtown Moorhead (Fargo-Moorhead metro)",
        tradition=Tradition.ZEN,
        notes=(
            "Open Land Sangha is a lay Soto Zen community in Downtown Moorhead, MN, "
            "serving the Fargo-Moorhead metro area. Founded in February 2018 by lay "
            "teacher Nancy Nanshin White, authorized in the lineage of Rev. Patricia "
            "Dai-En Bennage Roshi (Mt. Equity Zendo / Soto Zen). The practice is "
            "shikantaza (just sitting). "
            "Monday evenings 7:00–8:30 PM CT: one 30-minute period of zazen followed "
            "by a shared reading and discussion — Zoom only. "
            "Wednesday evenings 7:00–8:30 PM CT: zazen and reading/discussion (formats "
            "vary: 1st Wed one 30-min period + reading; 2nd Wed two 20-min periods + "
            "kinhin + service; 3rd Wed one 30-min + dharma talk; 4th Wed two 30-min + "
            "kinhin + precepts recitation) — hybrid in-person Downtown Moorhead and Zoom. "
            "2nd and 4th Friday mornings 7:00–8:00 AM CT: one period of zazen via Zoom. "
            "Prior to joining, contact them to schedule a short introductory session "
            "(in-person or Zoom). Free, open to all. openlandsangha.org."
        ),
    ),
}

# No live iCal feeds — all sits seeded as recurring in
# scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
