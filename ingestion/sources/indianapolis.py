"""
Indianapolis, IN — Phase 3 expansion.

Indianapolis has a compact but active practice community spanning Tibetan,
Korean Zen, and Theravada traditions. The city's Buddhist scene includes
the long-running Dromtonpa Kadampa center (NKT, est. 1998) and the
Indianapolis Zen Center (Kwan Um School of Zen, est. 1991).

Centers included:
  - KMC Indianapolis / Dromtonpa (kmc_indianapolis) — NKT Tibetan
    4010 W 86th St, Suite C, Indianapolis IN 46268 (NW Indianapolis)
    meditation-indianapolis.org — Sun 11am, Thu 6pm, Fri 10am
    No iCal (Squarespace, no JSON events API); recurring sits seeded.

  - Indianapolis Zen Center (indianapolis_zen_center) — Korean Zen (Kwan Um)
    3703 N. Washington Blvd, Indianapolis IN 46205 (Meridian-Kessler)
    indyzen.org — Mon/Wed 7pm evenings, Mon/Wed/Fri 6:45am mornings, Sat 9:30am
    No iCal (Wix site, JS-rendered calendar); recurring sits seeded.

Research notes (2026-05-19):
  - KMC Indianapolis (Dromtonpa): Founded 1998 by Tom Mitchell (IU professor).
    NKT center at 4010 W 86th St Ste C. Squarespace site; no iCal endpoint
    (?ical=1 returns homepage HTML, events-calendar?format=json returns HTML).
    Schedule confirmed: Sun 11am–12:15pm General Program, Thu 6–7pm Evening
    Meditation Class, Fri 10–11:15am Morning Meditation Class. Drop-in welcome;
    ~$12 suggested donation per class.
  - Indianapolis Zen Center (IZC): Member of Kwan Um School of Zen (Seung Sahn
    lineage, est. 1991). 3703 N. Washington Blvd. Wix site, no iCal.
    Schedule confirmed: Mon/Wed 7–8:30pm (two 25-min sits + walking meditation),
    Mon/Wed/Fri 6:45–7:15am morning practice (sit + reading/discussion),
    Sat 9:30–10:30am (chanting + sitting/walking). Hybrid in-person + Zoom
    (bit.ly/IndyZen). Monthly retreat 2nd Saturday. Drop-in, free.
  - Indiana Buddhist Center (IBC): 9260 E 10th St, Indianapolis (Gelugpa/Dalai
    Lama lineage). Wix site, JS-rendered, no iCal. Schedule unclear — events
    description says "currently in Greenwood" (suburb south of Indianapolis);
    Eventbrite shows 0 upcoming events. Deferred pending schedule confirmation.
  - Hoosier Heartland Shambhala Meditation Group: Based in Bloomington IN
    (Indiana University town, ~50 mi south of Indianapolis). Not Indianapolis
    metro; separate city. Deferred.
  - TMBCC (Tibetan Mongolian Buddhist Cultural Center): 3655 S Snoddy Rd,
    Bloomington IN. Dalai Lama's brother's center, 108 acres. Bloomington
    metro only; not Indianapolis. Deferred to future Bloomington expansion.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_indianapolis": Center(
        id="kmc_indianapolis",
        name="Kadampa Meditation Center Indianapolis",
        url="https://www.meditation-indianapolis.org",
        address="4010 W 86th Street, Suite C",
        city="Indianapolis",
        state="IN",
        zip_code="46268",
        lat=39.9080,
        lng=-86.2012,
        neighborhood="NW Indianapolis / North Willow",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Indianapolis (also known as Dromtonpa Kadampa "
            "Buddhist Center) is Indiana's New Kadampa Tradition (NKT) center, "
            "offering modern Tibetan Buddhist teachings in a welcoming, non-residential "
            "setting in northwest Indianapolis. Founded in 1998 by Indiana University "
            "professor Tom Mitchell, it is one of the oldest KMC centers in the US "
            "Midwest. Weekly public classes: Sunday General Program (11am–12:15pm), "
            "Thursday Evening Meditation (6–7pm), and Friday Morning Meditation "
            "(10–11:15am). All classes combine guided meditation with Buddhist "
            "teachings in the Kadampa style. Drop-in welcome; suggested donation ~$12. "
            "Foundation Program in-depth study course also offered Monday evenings."
        ),
    ),
    "indianapolis_zen_center": Center(
        id="indianapolis_zen_center",
        name="Indianapolis Zen Center",
        url="https://www.indyzen.org",
        address="3703 N. Washington Boulevard",
        city="Indianapolis",
        state="IN",
        zip_code="46205",
        lat=39.8373,
        lng=-86.1569,
        neighborhood="Meridian-Kessler",
        tradition=Tradition.ZEN,
        notes=(
            "The Indianapolis Zen Center (IZC) has been offering Korean Zen practice "
            "in central Indiana since 1991. A member of the Kwan Um School of Zen — "
            "founded by Korean master Seung Sahn Sunim, the same lineage as the "
            "Providence Zen Center — IZC holds regular weekly sits at its Meridian-"
            "Kessler location. Monday and Wednesday evening sittings (7–8:30pm) "
            "include two 25-minute periods of quiet meditation with walking in "
            "between. Monday, Wednesday, and Friday morning practice (6:45–7:15am) "
            "combines a 25–30 minute meditation with a short reading and discussion. "
            "Saturday morning gatherings (9:30–10:30am) include chanting and sitting "
            "or walking meditation. All sessions are hybrid in-person + Zoom "
            "(bit.ly/IndyZen). Monthly retreats held the 2nd Saturday. Drop-in "
            "welcome, no charge."
        ),
    ),
}

# No live iCal feeds extractable for Indianapolis centers —
# all sits seeded as recurring in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
