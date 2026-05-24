"""
Santa Cruz, CA — Phase 3 expansion.

Santa Cruz (~65k city, ~275k county) sits on Monterey Bay, home to UC Santa Cruz.
Its progressive culture and proximity to Spirit Rock and SF Bay supports a rich
Buddhist community spanning Zen, Insight, and Tibetan lineages.

Centers included:
  - Ocean Gate Zen Center (ocean_gate_zen) — Soto Zen
    920 41st Ave Suite F, Santa Cruz CA 95062. oceangatezen.org
    Live Tockify ICS feed: tockify.com/api/feeds/ics/ocean.gate.google.calendar
    Tue/Thu/Fri AM zazen; Thu PM zazen + dharma; Sat 9am "Come As You Are" program.

  - Santa Cruz Zen Center / SCZC (sczc) — Soto Zen
    113 School St, Santa Cruz CA 95060. sczc.org
    No iCal (Squarespace); recurring sits seeded.
    Mon–Fri 6am zazen, Wed 6:30pm evening program, Sat 8:30am, Sun 6pm zazen.

  - Insight Santa Cruz (insight_santa_cruz) — Insight/Theravada
    740 Front Street Suite 240, Santa Cruz CA 95060. insightsantacruz.org
    No iCal; recurring sits seeded: Sun 9am, Tue 12pm, Wed 6pm.

  - Land of Medicine Buddha / LMB (land_of_medicine_buddha) — Tibetan (FPMT/Gelug)
    5800 Prescott Rd, Soquel CA 95073. landofmedicinebuddha.org
    No iCal; Sunday 9am in-person Drop-In Meditation seeded.

Research notes (2026-05-24):
  - Ocean Gate Zen: Tockify ICS confirmed live (ocean.gate.google.calendar).
    Founded ~2021 at 920 41st Ave (Capitola/Santa Cruz border area, Opal Cliffs
    neighborhood). Teacher: Eikei Susan O'Brien (transmitted Soto Zen teacher,
    dharma successor of Shohaku Okumura). Regular public programs: Tue/Thu AM
    zazen 6:45–8am (in-person + Zoom), Fri AM zazen 9–9:40am, Thu PM 6pm zazen
    + service + Q&A (in-person + Zoom), Sat 9am "Come As You Are" sit +
    dharma talk (in-person). Filter_to_sits=True handles the variety.
  - SCZC (sczc.org): Founded 1970. Oldest and largest Zen center in Santa Cruz.
    Squarespace site, no public ICS. Rich daily schedule: M–F 6am zazen (hybrid),
    M–F 6pm zazen + service (hybrid), Wed 6:30pm evening dharma talk (hybrid),
    Sat 8:30–9:10am zazen (hybrid), Sun 6–6:40pm zazen (hybrid). No iCal; seeded.
  - Insight Santa Cruz (insightsantacruz.org): downtown Santa Cruz, 740 Front St.
    MEC-Lite WordPress plugin, no ICS export. Key in-person/hybrid sits: Sun 9am
    volunteer-led sit, Tue 12pm All-Community Sit with teacher, Wed 6pm All-Community
    Sit. Mon All-Community Practice (7pm) is online-only; not seeded.
  - Land of Medicine Buddha (landofmedicinebuddha.org): FPMT/Gelug center in the
    hills above Soquel. Sunday 9–10am Drop-In Meditation at the Gompa (in-person).
    Weekday Zoom meditation sessions not seeded (online-only).
  - Kadampa / NKT: no center in Santa Cruz or Monterey area; nearest is SF/South Bay.
  - Shambhala Santa Cruz: no active public-facing center found.
  - Watsonville Buddhist Temple (Jodo Shinshu): devotional temple, not a sit-focused
    meditation center; skipped.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "ocean_gate_zen": Center(
        id="ocean_gate_zen",
        name="Ocean Gate Zen Center",
        url="https://oceangatezen.org",
        address="920 41st Ave Suite F",
        city="Santa Cruz",
        state="CA",
        zip_code="95062",
        lat=36.9719,
        lng=-121.9920,
        neighborhood="Opal Cliffs / 41st Ave District",
        tradition=Tradition.ZEN,
        notes=(
            "Ocean Gate Zen Center is a Soto Zen community founded ~2021 in Santa Cruz, "
            "led by Eikei Susan O'Brien (transmitted Soto Zen teacher, dharma successor "
            "of Shohaku Okumura). Located at 920 41st Ave Suite F (enter from back "
            "parking lot). Regular public programs: Tuesday and Thursday morning zazen "
            "6:45–7:25am + service 7:25–7:45am + community bow-in 7:45–8:00am "
            "(in-person + Zoom); Friday morning zazen 9:00–9:40am + service; Thursday "
            "evening 6:00pm zazen + service + Q&A (in-person + Zoom); Saturday 9:00am "
            '"Come As You Are" zazen + dharma talk/Q&A (in-person; 1st Saturday includes '
            "8:30am zazen instruction). Zoom: zoom.us/j/2757401596, pw: Dogen4all. "
            "Drop-in welcome; no registration required."
        ),
    ),
    "sczc": Center(
        id="sczc",
        name="Santa Cruz Zen Center",
        url="https://sczc.org",
        address="113 School St",
        city="Santa Cruz",
        state="CA",
        zip_code="95060",
        lat=36.9783,
        lng=-122.0278,
        neighborhood="Downtown Santa Cruz",
        tradition=Tradition.ZEN,
        notes=(
            "Santa Cruz Zen Center (SCZC, formally Jorinzan Gyokuon-ji) is the oldest "
            "and largest Zen center in Santa Cruz, founded 1970 in the Soto Zen lineage "
            "(SZBA member). Located at 113 School St in downtown Santa Cruz. Regular "
            "public schedule: Monday–Friday 6:00am zazen + 6:40am morning service "
            "(in-person + Zoom); Monday/Wednesday/Friday noon zazen (in-person only); "
            "Monday–Friday 6:00pm zazen + 6:30pm service (in-person + Zoom); Wednesday "
            "evenings 6:30pm kinhin + 6:40pm dharma lecture/discussion (in-person + "
            "Zoom); Saturday 8:30–9:10am zazen + optional instruction (in-person + "
            "Zoom); Sunday 6:00–6:40pm zazen (in-person + Zoom; no service). "
            "Introduction to Zen typically 3rd Saturday 1–2pm. Sesshin and "
            "intensive retreats offered throughout the year. Drop-in welcome."
        ),
    ),
    "insight_santa_cruz": Center(
        id="insight_santa_cruz",
        name="Insight Santa Cruz",
        url="https://www.insightsantacruz.org",
        address="740 Front Street, Suite 240",
        city="Santa Cruz",
        state="CA",
        zip_code="95060",
        lat=36.9742,
        lng=-122.0308,
        neighborhood="Downtown Santa Cruz",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Santa Cruz is a Vipassana/Insight Meditation community in downtown "
            "Santa Cruz (740 Front St, Suite 240), practicing in the Theravada-influenced "
            "tradition. Regular in-person/hybrid public sits: Sunday 9:00–9:45am "
            "volunteer-led sitting with short reading (in-center + online); 4th Sunday "
            "10:00–11:30am teacher-led sit with dharma talk; Tuesday 12:00–1:00pm "
            "All-Community Sit with teacher (in-center + online); Wednesday 6:00–7:15pm "
            "All-Community Sit (in-center + online). Also: Monday and Wednesday noon "
            "45-min sits with reading (in-center + online); 4th Tuesday 7–8:30pm Rainbow "
            "Sangha (in-center only, LGBTQ+ inclusive). Dana-based; all are welcome."
        ),
    ),
    "land_of_medicine_buddha": Center(
        id="land_of_medicine_buddha",
        name="Land of Medicine Buddha",
        url="https://www.landofmedicinebuddha.org",
        address="5800 Prescott Rd",
        city="Soquel",
        state="CA",
        zip_code="95073",
        lat=37.0061,
        lng=-121.9497,
        neighborhood="Santa Cruz Mountains / Soquel Hills",
        tradition=Tradition.TIBETAN,
        notes=(
            "Land of Medicine Buddha (LMB) is an FPMT (Foundation for the Preservation "
            "of the Mahayana Tradition) retreat and study center in the Gelug lineage, "
            "located at 5800 Prescott Rd in the hills above Soquel (near Santa Cruz). "
            "The main public sit is the weekly Sunday Drop-In Meditation (9:00–10:00am) "
            "at the Gompa, led by resident teacher Ven. Yangchen — sitting and walking "
            "meditation, suitable for all levels, no registration required. Online daily "
            "meditation sessions (6:30am Morning Express and 8pm Evening Vajrasattva) "
            "are available to all via Zoom. Retreats and teachings throughout the year; "
            "see website for current programs."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "ocean_gate_zen": {
        "url": "https://tockify.com/api/feeds/ics/ocean.gate.google.calendar",
        "filter_to_sits": True,
    },
}
