"""
Tallahassee, Florida — Phase 3 expansion (heartbeat 81).

Tallahassee (pop. ~200k; metro ~380k) is Florida's state capital and home to
Florida State University and Florida A&M University. Its Buddhist community
spans Chan, Zen, and Shambhala traditions anchored by three active centers.

Centers included:
  - Tallahassee Chan Center (tallahassee_chan_center)
    Chan Buddhism (Dharma Drum lineage of Master Sheng Yen)
    1310 N Paul Russell Rd, Tallahassee FL 32301
    tallahasseechan.org · Sun 9:30am + Mon 6:30pm in-person + various monthly
    LIVE iCal feed: tallahasseechan.org/events/?ical=1

  - Cypress Tree Zen Group (cypress_tree_zen_tallahassee)
    Kwan Um School of Zen (Korean Chogye Zen, founded by Seung Sahn)
    1819 Doric Dr, Tallahassee FL 32303
    webdharma.com/ctzg/ · Sun 8:30–11am in-person
    No iCal — seeded as recurring.

  - Tallahassee Shambhala Meditation Group (shambhala_tallahassee)
    Shambhala (Tibetan-influenced contemplative tradition)
    2700 Apalachee Pkwy Suite A, Tallahassee FL 32301
    tallahassee.shambhala.org · Tue 7–8pm in-person
    No iCal — seeded as recurring.

Research notes (2026-06-25):
  - Tallahassee Chan Center: Active community led by Guo Gu (Jimmy Yu), a
    Dharma Drum Chan lineage teacher and FSU religion professor. Weekly Sunday
    Morning Meditation (9:30–11am), Monday Night Meditation (6:30–8pm),
    first-Thursday Short Meditation Instructions (6:30–8pm), third-Friday
    Bodhisattva Precepts Recitation (6–8pm). Also weekly Meditation on Recovery
    (Sun 11am) at the center's yoga building. All in-person events free.
    Live iCal feed confirmed at tallahasseechan.org/events/?ical=1.
  - Cypress Tree Zen Group: Kwan Um School of Zen, established community.
    Meets at 1819 Doric Dr (private house) Sunday mornings: bows, chanting,
    seated meditation, dharma discussion (8:30–11am in-person). Also offers
    Zoom sessions. webdharma.com/ctzg/
  - Tallahassee Shambhala: Part of the Shambhala Florida network. Meets
    Tuesdays 7–8pm for meditation and chanting at 2700 Apalachee Pkwy Suite A.
    Contact: Jo Schaden / Mary Beth McBride, (850) 219-1223.
  - Florida Drikung Dzogchen Community: appears to be a private study group,
    no confirmed public sitting schedule. Deferred.
  - Pema Tallahassee (Padmasambhava Buddhist Center affiliate): Nyingma
    tradition; schedule unclear from online sources. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "tallahassee_chan_center": Center(
        id="tallahassee_chan_center",
        name="Tallahassee Chan Center",
        url="https://tallahasseechan.org",
        address="1310 N Paul Russell Rd",
        city="Tallahassee",
        state="FL",
        zip_code="32301",
        lat=30.4134,
        lng=-84.2426,
        neighborhood="Southwood",
        tradition=Tradition.ZEN,
        notes=(
            "Tallahassee Chan Center (TCC) is the home base of Guo Gu (Jimmy Yu), "
            "a Dharma Drum Chan lineage teacher and professor of religion at Florida "
            "State University. Founded in the lineage of Master Sheng Yen (1930–2009), "
            "TCC is one of the most active English-language Chan centers in the United "
            "States. Regular public programs include: Sunday Morning Meditation "
            "(9:30–11am, in-person + Zoom, free); Monday Night Meditation (6:30–8pm, "
            "in-person, free); first-Thursday Short Meditation Instructions "
            "(6:30–8pm, in-person, free); third-Friday Group Bodhisattva Precepts "
            "Recitation (6–8pm, in-person, free); and weekly Sunday Meditation on "
            "Recovery (11am–noon, free, open to all regardless of background). "
            "1310 N Paul Russell Rd, Tallahassee FL 32301. tallahasseechan.org."
        ),
    ),
    "cypress_tree_zen_tallahassee": Center(
        id="cypress_tree_zen_tallahassee",
        name="Cypress Tree Zen Group",
        url="https://webdharma.com/ctzg/",
        address="1819 Doric Dr",
        city="Tallahassee",
        state="FL",
        zip_code="32303",
        lat=30.4777,
        lng=-84.3015,
        neighborhood="Northwest Tallahassee",
        tradition=Tradition.ZEN,
        notes=(
            "Cypress Tree Zen Group is a sitting community affiliated with the Kwan Um "
            "School of Zen, founded by the Korean Zen Master Seung Sahn. Meets at a "
            "private house at 1819 Doric Dr in northwest Tallahassee. Sunday morning "
            "program (8:30–11am): bows, chanting, seated meditation, and dharma "
            "discussion. Drop-in welcome; free. Zoom practice sessions also available. "
            "webdharma.com/ctzg/."
        ),
    ),
    "shambhala_tallahassee": Center(
        id="shambhala_tallahassee",
        name="Tallahassee Shambhala Meditation Group",
        url="https://tallahassee.shambhala.org",
        address="2700 Apalachee Pkwy Suite A",
        city="Tallahassee",
        state="FL",
        zip_code="32301",
        lat=30.4248,
        lng=-84.2565,
        neighborhood="Apalachee Parkway",
        tradition=Tradition.TIBETAN,
        notes=(
            "Tallahassee Shambhala Meditation Group offers weekly Tuesday evening "
            "meditation and chanting (7:00–8:00pm) at 2700 Apalachee Pkwy Suite A. "
            "Part of the Shambhala community, a global network presenting "
            "meditation as a practice for daily life and social transformation. "
            "Drop-in welcome. (850) 219-1223 · tallahassee.shambhala.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "tallahassee_chan_center": {
        "url": "https://tallahasseechan.org/events/?ical=1",
        "filter_to_sits": True,
    },
}
