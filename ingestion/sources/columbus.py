"""
Columbus, OH meditation center sources — Phase 3 expansion.

Columbus has a modest but solid Buddhist scene spread across the city.
The most notable feature: Columbus KTC has a confirmed working iCal feed.

Centers included:
  - Columbus Karma Thegsum Choling (KTC) — Tibetan Kagyu, iCal feed ✅
    645 W. Rich St. (Franklinton), weekly Sunday sits + Tue/Wed virtual
  - Mud Lotus Sangha — Soto Zen (White Plum lineage), 3 weekly in-person sits
    17 E. Tulane Rd. (Clintonville area / ILLIO Studios)
  - Zen Columbus Sangha — Soto Zen, Tue + Sat hybrid zazen
    93 W. Weisheimer Rd. (First UU Church, Clintonville)
  - Central Ohio Center for Pragmatic Buddhism (COCPB) — Zen/Pragmatist
    77 N. Brinker Ave. (West Side, private zendo), Sunday sits
  - Bliss Run Sangha — Plum Village / Thich Nhat Hanh lineage, Thu evenings
    4211 Maize Rd. (Unity Church, North Linden)

Research notes (2026-05-16):
  - Columbus KTC (columbusktc.org): 645 W. Rich St., Columbus OH 43215.
    Karma Kagyu lineage (affiliated with Karma Triyana Dharmachakra, Woodstock NY).
    Founded 1977. iCal feed confirmed at `columbusktc.org/events/?ical=1`.
    Sunday 10am Intro to Meditation (hybrid), 11:30am Dharma Talk (hybrid).
    Tuesday 7pm Chenrezig Puja (virtual only), Wed 12:15pm Midday Meditation (virtual).
  - Mud Lotus Sangha (mudlotussangha.org): 17 E. Tulane Rd., Columbus OH 43202
    (ILLIO Studios). Soto Zen, White Plum lineage with engaged Buddhism influence.
    Tue 7:30–8am Morning Sit (in-person), Wed 7–9pm Evening Zen + dharma discussion
    (in-person), Thu 9–10am Morning Meditation (hybrid, OSU Zoom). No iCal.
  - Zen Columbus Sangha (zencolumbus.org): 93 W. Weisheimer Rd., Columbus OH 43214
    (First Unitarian Universalist Church). Independent Soto Zen community.
    Tue 7–8:15pm two 25-min zazen periods + kinhin (hybrid), Sat 8:30–9:45am (hybrid).
    2nd Sat + 4th Tue monthly intro to zazen. No iCal.
  - COCPB (cocpb.com): 77 N. Brinker Ave., Columbus OH 43204 (private residence zendo,
    2nd floor entrance at back). Pragmatic Buddhism: Nikayan/Chan/Zen/Pragmatist synthesis.
    Teacher: Sensei Manny Shinshim. Sun 9:30am–noon zazen + dharma talk (in-person). No iCal.
  - Bliss Run Sangha (blissrun.org): Unity Church, 4211 Maize Rd., Columbus OH 43224
    (North Linden). Plum Village (Thich Nhat Hanh / Order of Interbeing).
    Thu 6:45pm newcomer orientation + 7–9pm walking meditation, sitting, dharma discussion
    (in-person). No iCal.
  - Columbus Shambhala (columbus.shambhala.org): 1271 E. Cooke Rd., Columbus OH 43224.
    Calendar shows no active events as of May 2026 — skip for now; monitor for revival.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "columbus_ktc": Center(
        id="columbus_ktc",
        name="Columbus Karma Thegsum Choling",
        url="https://columbusktc.org",
        address="645 W. Rich Street",
        city="Columbus",
        state="OH",
        zip_code="43215",
        lat=39.9553,
        lng=-83.0057,
        neighborhood="Franklinton",
        tradition=Tradition.TIBETAN,
        notes=(
            "Columbus Karma Thegsum Choling (KTC) is a Tibetan Buddhist meditation center "
            "in the Karma Kagyu lineage, affiliated with Karma Triyana Dharmachakra "
            "monastery in Woodstock, NY. Founded in 1977, it is one of the oldest "
            "Tibetan Buddhist centers in the Midwest. Weekly program includes Sunday "
            "Introduction to Meditation (10am, hybrid in-person + virtual) followed "
            "by Dharma Talk (11:30am), Tuesday evening Chenrezig Puja (7pm, virtual), "
            "and Wednesday Midday Meditation (12:15–1:30pm, virtual). All programs are "
            "free and open to the public; no experience required."
        ),
    ),
    "mud_lotus_sangha": Center(
        id="mud_lotus_sangha",
        name="Mud Lotus Sangha",
        url="https://www.mudlotussangha.org",
        address="17 E. Tulane Road",
        city="Columbus",
        state="OH",
        zip_code="43202",
        lat=40.0135,
        lng=-82.9975,
        neighborhood="Clintonville (at ILLIO Studios)",
        tradition=Tradition.ZEN,
        notes=(
            "Mud Lotus Sangha is Columbus's most active Zen community, practicing in "
            "the Soto Zen tradition (White Plum lineage) with engaged Buddhism and "
            "Order of Interbeing influences. Meets at ILLIO Studios in the Clintonville "
            "neighborhood. Weekly schedule: Tuesday 7:30–8am Morning Meditation "
            "(in-person); Wednesday 7–9pm Evening Zen Meditation with dharma discussion "
            "(in-person); Thursday 9–10am Morning Meditation (hybrid — in-person at "
            "ILLIO + Zoom). Monthly sesshins and day retreats. Drop-in welcome; free."
        ),
    ),
    "zen_columbus": Center(
        id="zen_columbus",
        name="Zen Columbus Sangha",
        url="http://zencolumbus.org",
        address="93 W. Weisheimer Road",
        city="Columbus",
        state="OH",
        zip_code="43214",
        lat=40.0569,
        lng=-83.0201,
        neighborhood="Clintonville (at First UU Church)",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Columbus Sangha is an independent Soto Zen community offering "
            "weekly zazen practice at the First Unitarian Universalist Church in "
            "Clintonville. Tuesday evenings 7–8:15pm: two 25-minute zazen periods "
            "with kinhin (walking meditation) and a brief service. Saturday mornings "
            "8:30–9:45am: same format. Both sessions are hybrid (in-person + Zoom). "
            "Introduction to Zazen offered on the 2nd Saturday and 4th Tuesday each "
            "month. All welcome; free."
        ),
    ),
    "cocpb_columbus": Center(
        id="cocpb_columbus",
        name="Central Ohio Center for Pragmatic Buddhism",
        url="https://www.cocpb.com",
        address="77 N. Brinker Avenue",
        city="Columbus",
        state="OH",
        zip_code="43204",
        lat=39.9706,
        lng=-83.0453,
        neighborhood="West Side",
        tradition=Tradition.ZEN,
        notes=(
            "The Central Ohio Center for Pragmatic Buddhism (COCPB) practices a "
            "synthesis of early Nikayan Buddhism, Chan, Japanese Zen, and American "
            "Pragmatist philosophy. Sensei Manny Shinshim leads weekly Sunday zazen "
            "(9:30am–noon) with dharma talk in a second-floor private zendo on the "
            "West Side. Entrance at the back of the house, then upstairs. In-person; "
            "small intimate community. All welcome; donations appreciated."
        ),
    ),
    "bliss_run_sangha": Center(
        id="bliss_run_sangha",
        name="Bliss Run Sangha",
        url="https://www.blissrun.org",
        address="4211 Maize Road",
        city="Columbus",
        state="OH",
        zip_code="43224",
        lat=40.0762,
        lng=-82.9981,
        neighborhood="North Linden (at Unity Church)",
        tradition=Tradition.OTHER,
        notes=(
            "Bliss Run Sangha is a Plum Village (Thich Nhat Hanh / Order of Interbeing) "
            "practice community meeting weekly at Unity Church in Columbus's North Linden "
            "neighborhood. Thursday evenings: 6:45pm newcomer orientation, then 7–9pm "
            "walking meditation, sitting meditation, and dharma discussion. In-person. "
            "All welcome; free."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

# Columbus KTC uses The Events Calendar WordPress plugin with a confirmed working iCal feed.
ICAL_FEEDS = {
    "columbus_ktc_ical": {
        "center_id": "columbus_ktc",
        "url": "https://columbusktc.org/events/?ical=1",
        "filter_to_sits": True,
    },
}
