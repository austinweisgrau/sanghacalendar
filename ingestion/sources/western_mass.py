"""
Western Massachusetts (Pioneer Valley) — Phase 3 expansion.

The Pioneer Valley — Northampton, Amherst, Easthampton, Springfield, Greenfield —
hosts one of New England's densest dharma communities outside Boston. Anchor
institutions span Theravada, Zen, and Tibetan traditions, and the region's
progressive college-town culture keeps attendance strong.

Centers included:
  - Insight Meditation Western MA (insight_wma) — Theravada (Vipassana)
    Eastworks, 116 Pleasant Street Suite 242, Easthampton MA 01027. insightwma.org
    Live iCal feed (WordPress Events Calendar plugin, insightwma.org/events/?ical=1).
    Weekly in-person sits: Saturday Sangha 8:45–10am + Tuesday Sangha 5:30–7pm +
    affinity groups. Very active; founded as Insight Meditation Center of Pioneer Valley.
    Guiding Teacher Emerita: Rebecca Bradshaw.

  - Pioneer Valley Shambhala Meditation Center (pioneer_valley_shambhala)
    — Tibetan (Shambhala)
    191 Main Street, 3rd Floor, Northampton MA 01060. pioneervalley.shambhala.org
    Mon 6:30–8pm open sitting, Thu 7–8:30pm open sitting. No iCal (403); seeded.

  - Oxbow Zen (oxbow_zen) — Zen (Village Zendo lineage / Enkyo O'Hara)
    First Churches of Northampton (enter Center St side), Northampton MA 01060.
    oxbowzen.org
    Sun 8–9:30am zazen + kinhin + service, Thu 5:30–6:40pm zazen. No iCal; seeded.

  - Boundless Way Zen — Northampton (boundless_way_northampton) — Zen (Boundless Way)
    Unitarian Society of Northampton & Florence, 220 Main Street, Northampton MA 01060.
    boundlessway.org / northamptonzen.org
    Wed 7:30–8:30pm drop-in zazen + walking meditation. No iCal; seeded.

Research notes (2026-10-16):
  - insightwma.org/events/?ical=1 confirmed live (HTTP 200, content-type text/calendar).
    Mix of in-person (Eastworks) and Zoom events; filter_to_sits=True will handle
    classification. Active events: Saturday Sangha, Tuesday Sangha, BIPOC Affinity,
    courses, and retreats.
  - Pioneer Valley Shambhala: shambhala-koeln.de feed for this center returns 403
    (Cloudflare). Recurring sits seeded from website (Mon 6:30pm, Thu 7pm).
  - Oxbow Zen: WordPress site, oxbowzen.org/events/?ical=1 returns 503. Recurring
    sits seeded (Sun 8am, Thu 5:30pm). Village Zendo lineage (Roshi Enkyo O'Hara).
  - Boundless Way Northampton: No persistent iCal on boundlessway.org for this group.
    Wednesday evening drop-in seeded. Affiliated with Boundless Way Worcester temple.
  - Green River Zen (Deerfield/Montague): Saturday 8:30am in-person at Windhorse Hill
    Retreat Center (595B River Rd, Deerfield). Verified active via greenriverzen.org.
    Not wired this round — remote rural location; may add in future heartbeat.
  - Living Dharma Center (Northampton, Tue 7pm): website active but schedule info
    sparse; deferred pending schedule verification.
  - Dhamma Dhara (Shelburne): Goenka 10-day courses only — not a drop-in sit.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "insight_wma": Center(
        id="insight_wma",
        name="Insight Meditation Western MA",
        url="https://insightwma.org",
        address="116 Pleasant Street, Suite 242",
        city="Easthampton",
        state="MA",
        zip_code="01027",
        lat=42.2669,
        lng=-72.6697,
        neighborhood="Eastworks Mill Building, Easthampton",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Western MA (IWM) is a non-residential urban dharma "
            "center in the Theravada / Insight Meditation tradition, located in the "
            "Eastworks mill building in Easthampton. Guiding Teacher Emerita: Rebecca "
            "Bradshaw; active teaching team includes Jaya Karlson and others. Weekly "
            "programs include Saturday Sangha (8:45–10am in-person, newcomer-friendly), "
            "Tuesday Sangha (5:30–7pm in-person, sitting + dharma talk), and various "
            "affinity groups (BIPOC, Queer & Trans, Elders). Classes, half-day and "
            "one-day retreats throughout the year. (413) 527-0388. insightwma.org."
        ),
    ),
    "pioneer_valley_shambhala": Center(
        id="pioneer_valley_shambhala",
        name="Pioneer Valley Shambhala Meditation Center",
        url="https://pioneervalley.shambhala.org",
        address="191 Main Street, 3rd Floor",
        city="Northampton",
        state="MA",
        zip_code="01060",
        lat=42.3229,
        lng=-72.6414,
        neighborhood="Downtown Northampton",
        tradition=Tradition.TIBETAN,
        notes=(
            "Pioneer Valley Shambhala Meditation Center is one of western New England's "
            "most established Tibetan Buddhist centers, located on the 3rd floor of 191 "
            "Main Street in downtown Northampton (elevator available). Shambhala "
            "International / Chogyam Trungpa Rinpoche lineage. Two weekly open drop-in "
            "sittings: Monday 6:30–8pm and Thursday 7–8:30pm — sitting meditation, "
            "optional instruction, and community. Shambhala Training weekends, "
            "meditation courses, Heart of Recovery, and programs for younger adults "
            "offered throughout the year. (413) 585-9848. pioneervalley.shambhala.org."
        ),
    ),
    "oxbow_zen": Center(
        id="oxbow_zen",
        name="Oxbow Zen",
        url="https://oxbowzen.org",
        address="129 Main Street (enter from Center Street)",
        city="Northampton",
        state="MA",
        zip_code="01060",
        lat=42.3257,
        lng=-72.6397,
        neighborhood="Downtown Northampton (First Churches)",
        tradition=Tradition.ZEN,
        notes=(
            "Oxbow Zen is a Northampton sitting community in the Village Zendo lineage "
            "(Roshi Enkyo O'Hara, New York). Meets upstairs in the First Churches of "
            "Northampton building — enter from Center Street behind the garden (be "
            "seated by 7:55am for Sunday, by 5:25pm for Thursday). Sunday Morning "
            "Zazen (8–9:30am): two 30-min sits, kinhin, chanting service; 3rd Sunday "
            "adds a dharma study group. Thursday Evening Zazen (5:30–6:40pm): two "
            "rounds of zazen and kinhin. All experience levels welcome. Online option "
            "available. Zazenkai (all-day sits) offered seasonally. oxbowzen.org."
        ),
    ),
    "boundless_way_northampton": Center(
        id="boundless_way_northampton",
        name="Boundless Way Zen — Northampton",
        url="https://boundlessway.org",
        address="220 Main Street",
        city="Northampton",
        state="MA",
        zip_code="01060",
        lat=42.3234,
        lng=-72.6362,
        neighborhood="Downtown Northampton (Unitarian Society)",
        tradition=Tradition.ZEN,
        notes=(
            "Boundless Way Zen — Northampton is a free, drop-in Zen sitting group "
            "affiliated with Boundless Way Zen Temple (Worcester, MA). Meets in the "
            "Parlor of the Unitarian Society of Northampton & Florence, 220 Main "
            "Street (enter via the side door near the back, up a half-flight of "
            "stairs). Wednesday evenings 7:30–8:30pm: brief chanting, two 25-minute "
            "zazen periods, walking meditation; 1st and 3rd Wednesdays include a "
            "dharma talk. Boundless Way blends Soto and Rinzai Zen (James Ishmael "
            "Ford Roshi lineage). No experience required; all welcome. Free. "
            "northamptonzen.org / boundlessway.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "insight_wma": {
        "url": "https://insightwma.org/events/?ical=1",
        "filter_to_sits": True,
    },
}
