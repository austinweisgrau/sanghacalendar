"""
New Hampshire — Phase 3 expansion (heartbeat 119).

New Hampshire's dharma scene is small but spans the full state — seacoast
Triratna hubs (Aryaloka + Portsmouth), a vibrant multi-sit Keene center,
a strong Theravada group in the Upper Valley, and a Zen sangha in the
quiet Canterbury hills.

Centers included:
  - Aryaloka Buddhist Center (aryaloka) — Other (Triratna)
    14 Heartwood Circle, Newmarket NH 03857. aryaloka.org
    Tue 6:45–8:45pm weekly (Friends' Evenings: meditation + dharma discussion).
    Flagship Triratna center for the region, founded early 1980s. No iCal seeded.

  - Portsmouth Buddhist Center (portsmouth_buddhist_center) — Other (Triratna)
    875 Islington St (at Gateway Taiji Studio), Portsmouth NH 03801.
    portsmouthbuddhistcenter.com
    Sun 10:00–11:45am (Sunday Gathering: meditation, dharma talk, discussion).
    Sister center to Aryaloka; founded ~2015. No iCal; seeded.

  - Monadnock Mindfulness Practice Center (monadnock_mindfulness)
    — Other (Non-sectarian / Plum Village)
    103 Roxbury Street Suite 301, Keene NH 03431. mindfulnesskeene.org
    Mon 6:30–7:30pm + Wed 6:00–7:30pm (Plum Village tradition) +
    Thu 8:00–9:00am + Fri 5:30–6:30pm. Most active NH center; founded 2002.
    No iCal; seeded.

  - Valley Insight Meditation Society (valley_insight_nh) — Theravada (Insight)
    14 Green Street, Lebanon NH 03766. valleyinsight.org
    Thu 11:00am–12:30pm hybrid in-person. Aligned with IMS and Spirit Rock.
    Monday + Tuesday also meet (mostly Zoom / monthly in-person). Seeded Thu only
    (most accessible regular NH in-person sit). No iCal; seeded.

  - Oxbow Zen Sangha (oxbow_zen_nh) — Zen (Mahayana / Vermont Zen Center affiliate)
    11 Oxbow Pond Road, Canterbury NH 03224. oxbowzen.org
    Sun 8:00–9:30am + Thu 5:30–6:40pm. Vermont Zen Center affiliate; rural
    Canterbury setting ~15 min north of Concord. No iCal; seeded.

Research notes (2026-10-31):
  - Aryaloka: CiviCRM iCal available at aryaloka.org/civicrm/event/ical?reset=1
    (confirmed live). Feed includes both Aryaloka and Portsmouth events, plus
    retreats and recovery meetings. Opted to seed manually to avoid geocoding
    ambiguity and recovery-event bleed-through; can wire iCal later.
  - Portsmouth Buddhist Center: portsmouthbuddhistcenter.com / thebuddhistcenter.com/
    portsmouth. Sister center to Aryaloka; events also appear on aryaloka.org/civicrm.
    Sunday Gathering runs hybrid (Zoom option). (603) 617-2285.
  - Monadnock Mindfulness Practice Center: mindfulnesskeene.org. ~1,200 participants/yr.
    4 sits/week: Mon 6:30pm (Tom), Wed 6pm (in-person, Plum Village), Thu 8am (Aylene),
    Fri 5:30pm (Eve, "Meditation & Movement"). Founded 2002. By donation. Suite 301,
    3rd floor, accessible building.
  - Valley Insight: valleyinsight.org. Theravada / Vipassana; teacher-led sits.
    Mon 5:30pm + Tue 5:30pm are mainly Zoom with one in-person/month; Thu 11am at
    14 Green St Lebanon is the most consistent NH in-person sit. (802) 649-7085.
    greetingsfromvalleyinsight@gmail.com. Norwich VT and Hanover NH communities.
  - Oxbow Zen Sangha: oxbowzen.org. Vermont Zen Center affiliate (Roshi Philip Kapleau /
    Bodhin Kjolhede lineage); sits in Canterbury ~15 min north of Concord. Sun 8–9:30am
    + Thu 5:30–6:40pm. All levels welcome. oxbowzensangha@gmail.com.
  - Not seeded: Portsmouth Zendo (South Berwick ME, ~15 min from Portsmouth, Monday 7pm;
    technically Maine), Wonderwell Mountain Refuge (Springfield NH, Wednesday 6pm;
    retreat center), Nashua Buddhist Meditation Group (Wednesday 7pm Shambhala at UU),
    Granite State Sangha (website down), Bear Tree Zen (no website, unconfirmed).
    These can be added in a follow-up heartbeat.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "aryaloka": Center(
        id="aryaloka",
        name="Aryaloka Buddhist Center",
        url="https://www.aryaloka.org",
        address="14 Heartwood Circle",
        city="Newmarket",
        state="NH",
        zip_code="03857",
        lat=43.0794,
        lng=-70.9431,
        neighborhood="Newmarket, NH Seacoast",
        tradition=Tradition.OTHER,
        notes=(
            "Aryaloka Buddhist Center is the flagship Triratna Buddhist Community "
            "center for New England, located at 14 Heartwood Circle in Newmarket, NH. "
            "Triratna (formerly Friends of the Western Buddhist Order) is a worldwide "
            "movement founded by Sangharakshita that emphasizes lay practice, "
            "accessibility, and depth across all major Buddhist traditions. Tuesday "
            "Friends' Evenings (6:45–8:45pm): weekly public sit combining guided "
            "meditation, dharma discussion, and community tea — the center's main "
            "ongoing practice event, open to all. Also hosts day retreats, weekend "
            "retreats, meditation courses, yoga programs, and full-moon pujas "
            "throughout the year. Residential retreat center with overnight "
            "accommodation on-site. (603) 659-5456. aryaloka.org."
        ),
    ),
    "portsmouth_buddhist_center": Center(
        id="portsmouth_buddhist_center",
        name="Portsmouth Buddhist Center",
        url="https://www.portsmouthbuddhistcenter.com",
        address="875 Islington Street",
        city="Portsmouth",
        state="NH",
        zip_code="03801",
        lat=43.0717,
        lng=-70.7861,
        neighborhood="Portsmouth Seacoast",
        tradition=Tradition.OTHER,
        notes=(
            "Portsmouth Buddhist Center is a Triratna Buddhist Community presence on "
            "the NH seacoast, sister center to Aryaloka Buddhist Center in Newmarket. "
            "Located at 875 Islington Street (Gateway Taiji Studio), Portsmouth NH. "
            "Sunday Gathering (10:00–11:45am): weekly public program combining guided "
            "meditation, a short dharma talk or reading, and open discussion. Hybrid "
            "format with Zoom option. All backgrounds welcome; drop-in. "
            "Also holds a Buddhist Recovery Group (Mondays 7:00–8:30pm at 73 Court "
            "Street, Portsmouth) for those in recovery programs. Founded ~2015. "
            "(603) 617-2285. portsmouthbuddhistcenter.com."
        ),
    ),
    "monadnock_mindfulness": Center(
        id="monadnock_mindfulness",
        name="Monadnock Mindfulness Practice Center",
        url="https://mindfulnesskeene.org",
        address="103 Roxbury Street, Suite 301",
        city="Keene",
        state="NH",
        zip_code="03431",
        lat=42.9367,
        lng=-72.2787,
        neighborhood="Downtown Keene",
        tradition=Tradition.OTHER,
        notes=(
            "Monadnock Mindfulness Practice Center is New Hampshire's most active "
            "meditation center, offering four public sits per week in Keene's "
            "Monadnock Region. Located at 103 Roxbury Street Suite 301 (3rd floor, "
            "accessible building) in downtown Keene. Founded 2002; serves ~1,200 "
            "participants annually. Monday Evening Sit (6:30–7:30pm): guided "
            "meditation and discussion. Wednesday Evening Sit (6:00–7:30pm): "
            "Plum Village / Thich Nhat Hanh tradition — walking meditation, sitting, "
            "dharma sharing. Thursday Morning Sit (8:00–9:00am): silent and guided "
            "sitting. Friday Evening Sit (5:30–6:30pm, 'Meditation & Movement'): "
            "gentle movement and sitting practice. All sits by donation; no "
            "experience needed. (603) 876-9318. mindfulnesskeene.org."
        ),
    ),
    "valley_insight_nh": Center(
        id="valley_insight_nh",
        name="Valley Insight Meditation Society",
        url="https://valleyinsight.org",
        address="14 Green Street",
        city="Lebanon",
        state="NH",
        zip_code="03766",
        lat=43.6424,
        lng=-72.2524,
        neighborhood="Lebanon, Upper Valley NH",
        tradition=Tradition.THERAVADA,
        notes=(
            "Valley Insight Meditation Society is the Upper Valley's Theravada / "
            "Vipassana sangha, serving the Hanover NH / Lebanon NH / Norwich VT "
            "region near Dartmouth College. Aligned with IMS (Barre MA) and Spirit "
            "Rock (CA). In-person Thursday Sit (11:00am–12:30pm) at 14 Green Street, "
            "Lebanon NH — teacher-led; includes guided meditation, dharma talk, and "
            "small-group discussion. Monday (5:30–7:00pm) and Tuesday (5:30–7:00pm) "
            "sits also offered — mainly Zoom with one in-person gathering per month. "
            "Open to all experience levels; dana-based. "
            "(802) 649-7085. greetingsfromvalleyinsight@gmail.com. valleyinsight.org."
        ),
    ),
    "oxbow_zen_nh": Center(
        id="oxbow_zen_nh",
        name="Oxbow Zen Sangha",
        url="https://oxbowzen.org",
        address="11 Oxbow Pond Road",
        city="Canterbury",
        state="NH",
        zip_code="03224",
        lat=43.3647,
        lng=-71.5656,
        neighborhood="Canterbury, NH (north of Concord)",
        tradition=Tradition.ZEN,
        notes=(
            "Oxbow Zen Sangha is a Mahayana Zen community affiliated with Vermont "
            "Zen Center (Rochester NY lineage; Roshi Philip Kapleau / Roshi Bodhin "
            "Kjolhede). Located at 11 Oxbow Pond Road in rural Canterbury, NH, "
            "about 15 minutes north of Concord. Sunday Morning Practice "
            "(8:00–9:30am): zazen, kinhin, liturgy, and dharma discussion — open "
            "to all levels. Thursday Evening Practice (5:30–6:40pm): zazen and "
            "kinhin — drop-in welcome. Both sits in-person at the Canterbury "
            "location. Retreats and special programs announced on website. "
            "oxbowzensangha@gmail.com. oxbowzen.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# Aryaloka CiviCRM iCal available at aryaloka.org/civicrm/event/ical?reset=1
# (confirmed live 2026-10-31). Opted for manual seeding to avoid recovery-event
# bleed-through and cross-location geocoding ambiguity. Can wire later.
