"""
Richmond, VA meditation center sources — Phase 3 expansion.

Richmond's Buddhist scene is anchored by Ekoji Buddhist Sangha (3411 Grove Ave,
Fan District) — a multi-tradition Buddhist community center that hosts several
distinct sangha groups under one roof. Nearly all public sits in Richmond
happen at Ekoji or via Zoom.

Centers included:
  - Insight Meditation Community of Richmond (IMCR) — Theravada/Insight, Tue+Fri weekly
    + monthly specials; WordPress TEC iCal feed (Chrome UA required)
  - Richmond Zen — Soto Zen (Shunryu Suzuki/Branching Streams lineage), Sun+Tue+Wed+Fri
  - Nyama Sangha — Shambhala-derived, Sat 10:30am
  - Palpung Shenpen Tharchin — Tibetan Kagyu (Palpung lineage), Thu 7pm

Regular weekly sits are seeded as recurring events in scripts/sangha-seed-recurring.js.
IMCR's iCal feed captures special events and retreats (off-site locations).

Research notes (2026-05-15):
  - Ekoji Buddhist Sangha (ekojirichmond.org): 3411 Grove Ave, Richmond VA 23221.
    Multi-tradition community hub in the Fan District. Hosts 7+ distinct sangha groups.
    All services open to public. No master iCal feed for the whole venue.
  - IMCR (imcrva.org): WordPress Events Calendar plugin. iCal feed requires Chrome UA
    (blocks default httpx UA with 406). Feed contains retreats and specials (not weekly sits).
    Weekly sits: Tue 7–9pm + Fri 5:45–7:30pm in-person at Ekoji + Zoom.
    Monthly: 1st Sun "Unplug" (9am + 3pm), 2nd Sat Early Sit (5:45am), 2nd Sat Engaged
    Buddhism (6:15pm).
  - Richmond Zen (richmondzen.org): Soto Zen, Branching Streams (Shunryu Suzuki Roshi
    lineage). Guiding teacher: Josho Phelan Roshi (abbess Chapel Hill Zen Center).
    Head priest: Eden Kevin Heffernan. No iCal; static WordPress. Schedule: Sun 9–11:30am,
    Tue 6:30–7:30am, Wed 7–8:30pm, Fri 6:30–7:30am. All at Ekoji in-person.
  - Nyama Sangha (ekojirichmond.org/richmond-shambhala/): Shambhala-derived community
    at Ekoji. Meets Saturdays 10:30am in-person + Zoom. No iCal.
  - Palpung Shenpen Tharchin (palpungrichmond.org): Tibetan Kagyu (Palpung lineage),
    teacher Lama Linda. Thu 7pm at Ekoji + Zoom. Rotating practices by week-of-month
    (Chenrezig, Green Tara, Medicine Buddha). 4th Sun 2–4pm teaching seeded monthly.
  - Integral Zen (at Ekoji): Mon 7–8:45pm. Eclectic/Ken Wilber-influenced — deferred,
    not clearly a traditional Buddhist sit.
  - Meditative Inquiry (at Ekoji): Sun 7–8:45pm at Ekoji + Wed 12:15pm Zoom. Not clearly
    Buddhist sits — deferred.
  - Pure Land (at Ekoji): Sat 2pm + 1st Sat 9:30am. Pure Land devotional — deferred.
  - Won Buddhism of Richmond (rvawonbuddhism.org): Mechanicsville, 20 miles north — separate
    metro; deferred.
  - Guhyasamaja Center (guhyasamaja.org): 10875 Main St, Fairfax VA 22030 — DC suburb,
    45 miles north; covered under DC metro if expanded.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "imcr": Center(
        id="imcr",
        name="Insight Meditation Community of Richmond",
        url="https://imcrva.org",
        address="3411 Grove Avenue",
        city="Richmond",
        state="VA",
        zip_code="23221",
        lat=37.5532,
        lng=-77.4774,
        neighborhood="Fan District (at Ekoji)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Community of Richmond (IMCR) is Richmond's primary "
            "Vipassana/Theravada community, meeting at Ekoji Buddhist Sangha in the "
            "Fan District. Weekly sits: Tuesdays 7–9pm (sit, walk, dharma talk + "
            "discussion) and Fridays 5:45–7:30pm (sit, walk, book reading + discussion) "
            "— both in-person at Ekoji and via Zoom. Monthly specials: 1st Sunday "
            "'Unplug' program (9am and 3pm sessions), 2nd Saturday Early Sit "
            "(5:45–9:30am), 2nd Saturday Engaged Buddhism (6:15–7:30pm). Also offers "
            "daylong and weekend retreats at off-site locations. Free; dana welcome."
        ),
    ),
    "richmond_zen": Center(
        id="richmond_zen",
        name="Richmond Zen",
        url="https://www.richmondzen.org",
        address="3411 Grove Avenue",
        city="Richmond",
        state="VA",
        zip_code="23221",
        lat=37.5532,
        lng=-77.4774,
        neighborhood="Fan District (at Ekoji)",
        tradition=Tradition.ZEN,
        notes=(
            "Richmond Zen practices in the Soto Zen lineage of Shunryu Suzuki Roshi, "
            "affiliated with Branching Streams. Guiding teacher: Josho Phelan Roshi "
            "(abbess of Chapel Hill Zen Center); head priest: Eden Kevin Heffernan. "
            "Meets at Ekoji Buddhist Sangha in Richmond's Fan District. Schedule: "
            "Sundays 9–11:30am, Tuesdays 6:30–7:30am, Wednesdays 7–8:30pm, Fridays "
            "6:30–7:30am. All sessions in-person. Drop-in welcome for all sits. "
            "Newcomer orientations offered regularly (see website). Free."
        ),
    ),
    "nyama_sangha": Center(
        id="nyama_sangha",
        name="Nyama Sangha",
        url="https://ekojirichmond.org/richmond-shambhala/",
        address="3411 Grove Avenue",
        city="Richmond",
        state="VA",
        zip_code="23221",
        lat=37.5532,
        lng=-77.4774,
        neighborhood="Fan District (at Ekoji)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Nyama Sangha is Richmond's Shambhala-lineage meditation community, "
            "meeting weekly at Ekoji Buddhist Sangha in the Fan District. Saturday "
            "morning sits at 10:30am in-person and via Zoom. Open to practitioners "
            "of all backgrounds; no experience necessary. Instruction available for "
            "newcomers. Free; donations appreciated."
        ),
    ),
    "palpung_richmond": Center(
        id="palpung_richmond",
        name="Palpung Shenpen Tharchin",
        url="https://palpungrichmond.org",
        address="3411 Grove Avenue",
        city="Richmond",
        state="VA",
        zip_code="23221",
        lat=37.5532,
        lng=-77.4774,
        neighborhood="Fan District (at Ekoji)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Palpung Shenpen Tharchin is a Tibetan Buddhist community in the Palpung "
            "Kagyu lineage, meeting weekly at Ekoji Buddhist Sangha. Teacher: Lama "
            "Linda. Thursday evenings 7pm in-person at Ekoji and via Zoom. Weekly "
            "practices rotate by week-of-month: 1st Thursday — teaching on The Six "
            "Perfections followed by Chenrezig chanting in English; 2nd Thursday — "
            "Chenrezig in Tibetan; 3rd Thursday — Green Tara in English; 4th Thursday "
            "— Green Tara in Tibetan; 5th Thursday — Medicine Buddha. 4th Sunday "
            "2–4pm teaching with Lama Linda (monthly). All open to the public; "
            "newcomers welcome. Free."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

# IMCR uses WordPress Events Calendar plugin. The default httpx UA gets a 406
# (blocked by Mod Security); the ical_feed.py fetch_feed() already sends a Chrome
# UA so this should work. Feed contains special events and retreats; regular weekly
# sits are seeded as recurring in sangha-seed-recurring.js.
ICAL_FEEDS = {
    "imcr_ical": {
        "center_id": "imcr",
        "url": "https://imcrva.org/?ical=1",
        "filter_to_sits": True,
    },
}
