"""
Bozeman, MT — Phase 3 expansion.

Bozeman (~55k city, ~130k metro) is home to Montana State University and sits
in the Gallatin Valley. Despite its modest size, it has a remarkably active
Buddhist community centered around the Bozeman Dharma Center (BDC), a
multi-tradition hub that hosts seven distinct groups.

Centers included:
  - Bozeman Dharma Center (bozeman_dharma_center) — multi-tradition hub
    206 E Griffin Dr, Bozeman MT 59715. bozemandharmacenter.org
    Live WordPress iCal feed: bozemandharmacenter.org/calendar/?ical=1
    Hosts: Bozeman Zen Group, Bozeman Insight Community, Joining Rivers Sangha
    (Plum Village), Tergar Bozeman, Palyul Tibetan Buddhist Sangha,
    MindSpace (young adults), Recovery Dharma, daily Noon Sit.

Research notes (2026-05-25):
  - Bozeman Dharma Center: NW Dharma Association member, founded around 2010s.
    Current meeting location is Fork & Spoon, 206 E Griffin Dr (a pay-what-you-can
    community restaurant that rents space). Website (bozemandharmacenter.org) still
    lists 3810 Valley Commons Dr as postal address but live iCal events all show
    Griffin St location. (406) 219-2140.
  - Bozeman Zen Group (boznzen@gmail.com): Soto Zen, Branching Streams / SFZC
    lineage (dharma heir of Berkeley Zen Center's Sojun Mel Weitsman Roshi). Teacher:
    Karen DeCotis. Daily online zazen M–F 6am + Sun 8am; in-person afternoon zazen
    M/Thu/Fri 5:30pm + Sun 5pm formal practice (dharma talk, tea).
  - Bozeman Insight Community (est. 1996): Vipassana/Insight. Thursday 6:30–8pm
    in-person + Zoom; Tuesday 10:30am Zoom only (Kindhearted Awareness metta practice).
  - Joining Rivers Sangha: Plum Village / Order of Interbeing. Monday 7–8:30pm
    in-person (sitting + walking + dharma sharing). bozemantnh@gmail.com.
  - Tergar Bozeman: Yongey Mingyur Rinpoche teachings. Wednesday 5:30–7pm
    in-person + Zoom; no prerequisites; freely offered. tergar.org/bozeman.
  - Palyul Tibetan Buddhist Sangha (Namdroling Montana): Nyingma Vajrayana
    (Palyul/Namdroling). 1st & 3rd Sundays 9–10:15am in-person + Zoom.
  - MindSpace: Buddhist young adults (18–40). Tuesday 6:30–7:45pm in-person.
  - Recovery Dharma: Monday 5:30pm in-person.
  - Noon Sit: M–F 12–1pm silent open sit.
  - All events flow through single BDC WordPress iCal feed (filter_to_sits=True).
  - No Shambhala, KMC/Kadampa, or standalone Zen center in Bozeman.
  - Vipassana Montana (10-day Goenka retreats): not in Bozeman metro; skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "bozeman_dharma_center": Center(
        id="bozeman_dharma_center",
        name="Bozeman Dharma Center",
        url="https://bozemandharmacenter.org",
        address="206 E Griffin Dr",
        city="Bozeman",
        state="MT",
        zip_code="59715",
        lat=45.6784,
        lng=-111.0346,
        neighborhood="Downtown Bozeman",
        tradition=Tradition.OTHER,
        notes=(
            "Bozeman Dharma Center is a multi-tradition Buddhist hub in Bozeman, MT, "
            "currently meeting at Fork & Spoon (206 E Griffin Dr). It hosts seven "
            "resident groups: Bozeman Zen Group (Soto Zen / Branching Streams), Bozeman "
            "Insight Community (Vipassana, est. 1996), Joining Rivers Sangha (Plum "
            "Village/TNH), Tergar Bozeman (Mingyur Rinpoche), Palyul Tibetan Buddhist "
            "Sangha (Nyingma/Namdroling), MindSpace (young adults 18–40), and Recovery "
            "Dharma. Also hosts daily Noon Sit (M–F 12–1pm). Northwest Dharma "
            "Association member. (406) 219-2140 / info@bozemandharmacenter.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "bozeman_dharma_center": {
        "url": "https://bozemandharmacenter.org/calendar/?ical=1",
        "filter_to_sits": True,
    },
}
