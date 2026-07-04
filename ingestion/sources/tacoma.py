"""
Tacoma / South Sound, Washington — Phase 3 expansion (heartbeat 84).

Tacoma (pop. ~225K city / ~900K metro) is the third-largest city in Washington,
45 miles south of Seattle. The South Sound area also includes Olympia, the state
capital (~50K city / ~275K metro), 30 miles further south.

All centers in this module use seeded recurring sits — no live iCal feeds found.

Centers included:
  - Trikaya Zen Center (trikaya_zen)
    Soto Zen (White Plum Asanga lineage)
    2710 N. Madison St, Tacoma WA 98406 (North End)
    trikayazencenter.org · Sat 10am, Sun 10am

  - Tacoma Buddhist Center (tacoma_buddhist_center)
    Triratna Buddhist Community (non-sectarian Western Buddhism)
    Kliworth Chapel, University of Puget Sound, 3410 N 18th St, Tacoma WA 98416
    tacomabuddhistcenter.org · Wed 7:30pm

  - Tacoma Shambhala Meditation Group (tacoma_shambhala)
    Shambhala (Chögyam Trungpa lineage) — satellite group of Seattle Shambhala
    Good Karma Center for Joy, 711 St Helens Ave #103, Tacoma WA 98402
    seattle.shambhala.org · Tue 6:45pm

  - Tushita Kadampa Buddhist Center (tushita_kadampa)
    New Kadampa Tradition (NKT-IKBU, Geshe Kelsang Gyatso lineage)
    211 Legion Way SW, Olympia WA 98501
    meditateinolympia.org · Sun 10am, Wed noon

  - Nalanda Institute for Buddhist Studies and Meditation (nalanda_olympia)
    Tibetan / non-sectarian (Lama Lungrik)
    1620 4th Ave E, Olympia WA 98506
    nalandaolywa.org · MWF 12:15pm, Thu 7pm, Sat 10am

Research notes (2026-07-04):
  - Trikaya Zen Center: Teacher Sensei Rich Taido Christofferson, White Plum Asanga
    member (Maezumi Roshi lineage). Drop-in zazen Sat 10am and Sun 10am. Both days
    include dharma talk. No iCal feed; Squarespace site.
  - Tacoma Buddhist Center: Triratna Buddhist Community, formerly FWBO. Meets in
    Kliworth Chapel basement at UPS campus. Wed 7:30–9:15pm drop-in meditation +
    dharma discussion. Suggested donation $10. No iCal found.
  - Tacoma Shambhala: Satellite group of Shambhala Meditation Center of Seattle,
    meeting Tue 6:45–8:45pm at Good Karma Center for Joy (711 St Helens Ave #103).
    No standalone iCal. Confirm active status via seattle.shambhala.org.
  - Tushita Kadampa: NKT center at 211 Legion Way SW, downtown Olympia. Drop-in
    classes: Sun 10–11:15am, Wed noon–1pm. Wix site, no iCal endpoint detected.
  - Nalanda Institute: Non-sectarian center (Tibetan-informed) at 1620 4th Ave E.
    Lunchtime MWF 12:15–12:50pm, Thursday dharma talk 7–8:30pm (in-person/Zoom),
    Saturday Chenrezig 10–11:30am. PHP-based site, no iCal export. nalandaolywa.org.
  - Olympia Zen Center (Ryoko-an, 3248 39th Way NE): Residential Soto Zen training
    center, Teacher Eido Frances Carney. Public access unclear — primarily for
    resident practitioners. Deferred pending schedule clarification.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "trikaya_zen": Center(
        id="trikaya_zen",
        name="Trikaya Zen Center",
        url="https://trikayazencenter.org",
        address="2710 N. Madison St",
        city="Tacoma",
        state="WA",
        zip_code="98406",
        lat=47.2668,
        lng=-122.4695,
        neighborhood="North End",
        tradition=Tradition.ZEN,
        notes=(
            "Trikaya Zen Center is a Soto Zen center in the White Plum Asanga lineage "
            "of Taizan Maezumi Roshi. Teacher: Sensei Rich Taido Christofferson. "
            "Weekly public programs: Saturday 10–11:30am (zazen + dharma talk/Q&A) "
            "and Sunday 10am (zazen + private teacher interviews / daisan). "
            "Both koan practice and shikantaza. Drop-in welcome. "
            "2710 N. Madison St, Tacoma WA 98406. trikayazencenter.org."
        ),
    ),
    "tacoma_buddhist_center": Center(
        id="tacoma_buddhist_center",
        name="Tacoma Buddhist Center",
        url="https://tacomabuddhistcenter.org",
        address="3410 N 18th St",
        city="Tacoma",
        state="WA",
        zip_code="98416",
        lat=47.2683,
        lng=-122.4572,
        neighborhood="North End / UPS Campus",
        tradition=Tradition.PLURALIST,
        notes=(
            "Tacoma Buddhist Center is part of the Triratna Buddhist Community "
            "(formerly Friends of the Western Buddhist Order), drawing on Theravada, "
            "Mahayana, and Vajrayana traditions. Meets in Kliworth Chapel basement "
            "at the University of Puget Sound campus. Weekly drop-in: Wednesday "
            "7:30–9:15pm, guided meditation + dharma discussion. All welcome; "
            "suggested donation $10. 3410 N 18th St, Tacoma WA 98416. "
            "tacomabuddhistcenter.org."
        ),
    ),
    "tacoma_shambhala": Center(
        id="tacoma_shambhala",
        name="Tacoma Shambhala Meditation Group",
        url="https://seattle.shambhala.org",
        address="711 St Helens Ave #103",
        city="Tacoma",
        state="WA",
        zip_code="98402",
        lat=47.2534,
        lng=-122.4433,
        neighborhood="Downtown Tacoma",
        tradition=Tradition.TIBETAN,
        notes=(
            "Tacoma Shambhala Meditation Group is a satellite group of the Shambhala "
            "Meditation Center of Seattle, meeting at Good Karma Center for Joy in "
            "downtown Tacoma. Weekly sit: Tuesday 6:45–8:45pm, in-person. Shambhala "
            "Buddhist tradition (Chögyam Trungpa Rinpoche lineage). All welcome; "
            "free introductory instruction available. 711 St Helens Ave #103, "
            "Tacoma WA 98402. seattle.shambhala.org."
        ),
    ),
    "tushita_kadampa": Center(
        id="tushita_kadampa",
        name="Tushita Kadampa Buddhist Center",
        url="https://meditateinolympia.org",
        address="211 Legion Way SW",
        city="Olympia",
        state="WA",
        zip_code="98501",
        lat=47.0436,
        lng=-122.9012,
        neighborhood="Downtown Olympia",
        tradition=Tradition.TIBETAN,
        notes=(
            "Tushita Kadampa Buddhist Center offers Tibetan Buddhist meditation "
            "classes in the New Kadampa Tradition (NKT-IKBU) founded by Geshe "
            "Kelsang Gyatso. Drop-in classes in downtown Olympia: Sunday 10–11:15am "
            "'The Happiness Formula' and Wednesday noon–1pm 'Clear, Calm, "
            "Compassionate'. Beginners welcome; no experience needed. "
            "211 Legion Way SW, Olympia WA 98501. meditateinolympia.org."
        ),
    ),
    "nalanda_olympia": Center(
        id="nalanda_olympia",
        name="Nalanda Institute for Buddhist Studies and Meditation",
        url="https://nalandaolywa.org",
        address="1620 4th Ave E",
        city="Olympia",
        state="WA",
        zip_code="98506",
        lat=47.0560,
        lng=-122.8801,
        neighborhood="East Olympia",
        tradition=Tradition.TIBETAN,
        notes=(
            "Nalanda Institute for Buddhist Studies and Meditation offers a rich "
            "schedule of non-sectarian and Tibetan-informed meditation in Olympia. "
            "Public programs: Lunchtime Mindfulness Meditation Mon/Wed/Fri 12:15pm "
            "(in-person); Thursday Dharma Talk & Meditation 7pm (in-person + Zoom); "
            "Saturday Chenrezig Meditation 10am (most Saturdays, in-person); "
            "2nd and 4th Sunday 10am longer meditation session. "
            "Founded in the Tibetan tradition; teacher Lama Lungrik. "
            "1620 4th Ave E, Olympia WA 98506. nalandaolywa.org."
        ),
    ),
}
