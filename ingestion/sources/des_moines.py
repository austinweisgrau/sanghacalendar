"""
Des Moines, Iowa — Phase 3 expansion (heartbeat 77).

Des Moines (pop. ~215k; metro ~700k) is Iowa's capital and largest city.
The Buddhist scene is small but active, anchored by a Soto Zen center and
a multi-tradition temple in the western suburb of Clive.

Centers included:
  - Des Moines Zen Center / Deep River Temple (des_moines_zen)
    Soto Zen (Deep River lineage)
    6901 SW 14th St, Des Moines IA 50315
    dsmzencenter.org · Sun 7:10am + Wed 6pm in-person
    No iCal — seeded as recurring.

  - Pure Land of Iowa (pure_land_iowa)
    Multi-tradition (Zen + Theravada teachers), temple in Clive IA
    8364 Hickman Rd, Clive IA 50325
    purelandofiowa.org · Wed 6:30pm (Theravada) + Thu 7pm (Zen) in-person
    No iCal — seeded as recurring.

Research notes (2026-06-10):
  - Des Moines Zen Center: Soto Zen, also known as Deep River Temple or Shinsenji.
    Weekly schedule: Sunday 7:10–8:50am (zazen, kinhin, dharma talk) and
    Wednesday 6:00–8:00pm (instruction 5:40pm, zazen 6pm, study group 2nd-4th Wed
    6:50pm). All practices open to all; drop-in. Located at 6901 SW 14th St in SW
    Des Moines. dsmzencenter.org.
  - Pure Land of Iowa: multi-tradition temple at 8364 Hickman Rd, Clive IA (western
    suburb). Teachers include Daishin Eric McCabe (Zen, morning and Thu meditation)
    and Bhante Dhammapala (Theravada monk, Wed 6:30pm). Wed evening sit: 6:30–8:15pm
    guided meditation + discussion (Theravada, in-person). Thu evening: 7:00–8:00pm
    guided meditation (Zen, in-person). Also offers Mon/Wed/Fri 5:30am morning sits
    (30 min, Zen). (515) 331-4144 · purelandofiowa.org.
  - Ariya Magga Buddhist Missionary Society (AMBMS): Theravada group led by Bhante
    Dhammapala, meets online via Google Meet — skipped (online only).
  - Awakening Heart Sangha (Plum Village / First Unitarian Church): Zoom-only Mondays
    — skipped (online only).
  - Ryumonji Zen Monastery: Northeast Iowa (not Des Moines metro) — out of scope.
  - No Shambhala, Kadampa, or Tibetan center found in Des Moines metro.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "des_moines_zen": Center(
        id="des_moines_zen",
        name="Des Moines Zen Center",
        url="https://www.dsmzencenter.org",
        address="6901 SW 14th St",
        city="Des Moines",
        state="IA",
        zip_code="50315",
        lat=41.5558,
        lng=-93.6480,
        neighborhood="Southwest Des Moines",
        tradition=Tradition.ZEN,
        notes=(
            "Des Moines Zen Center (Deep River Temple / Shinsenji) is a Soto Zen "
            "practice community at 6901 SW 14th St in southwest Des Moines. "
            "Committed to inclusivity and diversity, welcoming practitioners of all "
            "backgrounds. Weekly sitting schedule: Sunday Morning Program — "
            "zazen instruction 7:40am, zazen 7:10–8:40am, kinhin (walking), "
            "morning service, and dharma talk from 8:50am. Wednesday Evening — "
            "zazen instruction 5:40pm, zazen 6:00–6:40pm; Zen Study Group on 2nd, "
            "3rd, and 4th Wednesdays 6:50–8:00pm. All practices open to the public; "
            "drop-in welcome. dsmzencenter.org."
        ),
    ),
    "pure_land_iowa": Center(
        id="pure_land_iowa",
        name="Pure Land of Iowa",
        url="https://www.purelandofiowa.org",
        address="8364 Hickman Rd",
        city="Clive",
        state="IA",
        zip_code="50325",
        lat=41.5985,
        lng=-93.7729,
        neighborhood="Clive",
        tradition=Tradition.OTHER,
        notes=(
            "Pure Land of Iowa is a multi-tradition Buddhist temple at 8364 Hickman Rd "
            "in Clive, a western suburb of Des Moines. Teachers include Daishin Eric "
            "McCabe (Zen lineage) and Bhante Dhammapala (Theravada monk). The temple "
            "offers several weekly in-person sits: Wednesday Evening Meditation "
            "(6:30–8:15pm) with Bhante Dhammapala — guided meditation, group "
            "discussion, and silent sitting in the Theravada tradition; Thursday "
            "Evening Meditation (7:00–8:00pm) with Daishin Eric McCabe — guided "
            "sitting in the Zen tradition; and early morning sits Mon/Wed/Fri at "
            "5:30–6:00am (Zen). All are beginner-friendly and open to the public. "
            "(515) 331-4144 · purelandofiowa.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — all centers seeded via scripts/sangha-seed-recurring.js
