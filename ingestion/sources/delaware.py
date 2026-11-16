"""
Delaware — Phase 3 expansion (heartbeat 123).

Delaware has a small but active Buddhist community concentrated near Wilmington
(Newark DE) and in coastal Lewes (Sussex County).

Centers included:
  - dvzc
    Kwan Um School of Zen (Korean Zen)
    New Ark UCC, 300 E Main St, Newark DE 19711
    Wednesday 6:30–8:00pm in-person
    dvzc.com — no iCal; seeded as recurring.

  - imc_lewes
    Insight Meditation (Theravada / Vipassana)
    St. Peter's Community Hall, 211 Mulberry St, Lewes DE 19958
    2nd and 4th Monday 4:00–5:30pm hybrid (in-person + Zoom)
    1st and 3rd Monday 5:00–6:00pm Dharma Study (Zoom + hybrid)
    imc-lewes.org — no iCal; seeded as recurring.

  - open_heart_zen_wilmington
    Zen Buddhism (independent, lay-led)
    Online via Zoom (formerly at First UU Wilmington, 730 Halstead Rd)
    Wednesday 7:00–8:30pm online
    openheartzen.org — online only; seeded as recurring.

Research notes (2026-11-16):
  - Delaware Valley Zen Center (DVZC): Founded 1999, one of 60+ centers in the
    worldwide Kwan Um School of Zen network. Guiding teacher: Zen Master Tang
    Gong (José Ramírez). Weekly Wednesday 6:30–8:00pm: chanting + 2x 25-min
    sitting + 10-min walking. 3rd Wednesday includes kong-an interviews via Zoom.
    4th Wednesday 5:30pm newcomer instruction. Quarterly retreats. Free,
    drop-in welcome. DVZCinfo@gmail.com | (302) 533-8819. dvzc.com.
  - IMC Lewes: Insight Meditation Community of Lewes. Well-organized community
    in coastal Lewes (Sussex County), ~1.5 hrs south of Wilmington. Weekly
    Monday practice: 2nd and 4th Mondays 4–5:30pm hybrid at St. Peter's
    Community Hall (211 Mulberry St); 1st and 3rd Mondays 5pm Dharma Study
    Group. Periodic dharma talks and daylong retreats. No iCal feed (Event
    Organiser WP plugin returns HTML). info@imc-lewes.org. imc-lewes.org.
  - Open Heart Zen Sangha: Founded 2010 at First UU Wilmington. Currently fully
    online via Zoom. Wednesday evenings 7–8:30pm: 30-min zazen + dharma talk +
    discussion. Contact openheartzen@gmail.com for Zoom link. openheartzen.org.
  - Dhamma Pubbananda (Claymont DE, near PA border): S.N. Goenka 10-day
    residential courses only; no drop-in sits; not suitable for calendar.
  - No Shambhala, Kadampa, or Plum Village centers found in Delaware.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "dvzc": Center(
        id="dvzc",
        name="Delaware Valley Zen Center",
        url="https://dvzc.com",
        address="300 E Main St",
        city="Newark",
        state="DE",
        zip_code="19711",
        lat=39.6837,
        lng=-75.7497,
        neighborhood="Downtown Newark",
        tradition=Tradition.ZEN,
        notes=(
            "Delaware Valley Zen Center (DVZC) is a Kwan Um School of Zen center "
            "in Newark, DE, founded in 1999. Guiding teacher: Zen Master Tang Gong "
            "(José Ramírez). Weekly Wednesday sit at New Ark United Church of Christ "
            "(300 E Main St): 6:30–8:00pm, with chanting, two 25-minute sitting "
            "periods, and walking meditation. 3rd Wednesday includes kong-an "
            "interviews via Zoom; 4th Wednesday offers newcomer instruction at 5:30pm. "
            "Quarterly one-day retreats. Free, drop-in welcome. No registration "
            "required. DVZCinfo@gmail.com | (302) 533-8819. dvzc.com."
        ),
    ),
    "imc_lewes": Center(
        id="imc_lewes",
        name="Insight Meditation Community of Lewes",
        url="https://imc-lewes.org",
        address="211 Mulberry St",
        city="Lewes",
        state="DE",
        zip_code="19958",
        lat=38.7748,
        lng=-75.1397,
        neighborhood="Lewes (Sussex County)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Community of Lewes (IMC-Lewes) is a Vipassana / "
            "Insight Meditation community on Delaware's coast, in the Theravada "
            "tradition. Weekly Monday practice at St. Peter's Community Hall "
            "(211 Mulberry St, Lewes): 2nd and 4th Mondays 4:00–5:30pm, hybrid "
            "in-person + Zoom; 1st and 3rd Mondays 5:00pm Dharma Study Group. "
            "Also periodic daylong retreats and dharma talks. Free, open to all "
            "experience levels. info@imc-lewes.org. imc-lewes.org."
        ),
    ),
    "open_heart_zen_wilmington": Center(
        id="open_heart_zen_wilmington",
        name="Open Heart Zen Sangha",
        url="https://www.openheartzen.org",
        address="730 Halstead Rd",
        city="Wilmington",
        state="DE",
        zip_code="19803",
        lat=39.7447,
        lng=-75.5597,
        neighborhood="Sharpley / North Wilmington",
        tradition=Tradition.ZEN,
        notes=(
            "Open Heart Zen Sangha is an independent lay Zen community based in "
            "the Wilmington, DE area, founded in 2010 at First Unitarian Church "
            "(730 Halstead Rd, Sharpley). Currently practicing online via Zoom. "
            "Weekly Wednesday evenings 7:00–8:30pm: 30 minutes of zazen + dharma "
            "talk + discussion. Monthly open discussion on the last Wednesday. "
            "Contact openheartzen@gmail.com for the Zoom link. openheartzen.org."
        ),
    ),
}

# No live iCal, Eventbrite, or static HTML feeds for Delaware.
ICAL_FEEDS: dict = {}
EVENTBRITE_FEEDS: dict = {}
STATIC_HTML_FEEDS: dict = {}
