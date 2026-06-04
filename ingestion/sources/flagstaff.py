"""
Flagstaff, Arizona — Phase 3 expansion (heartbeat 75).

Flagstaff (pop. ~75k; metro ~145k) is a university city (Northern Arizona
University) at 7,000 ft elevation in the Colorado Plateau. The Buddhist
scene is small but diverse: Theravada insight, Zen, and NKT Tibetan all
represented with regular drop-in programming.

Centers included:
  - Flagstaff Insight Meditation Community (fimc_flagstaff)
    Theravada/Vipassana, founded ~2006
    510 N Leroux St (Beacon UU), Flagstaff AZ 86001
    flagstaffinsight.org · Mon 6:30pm hybrid
    No iCal — seeded as recurring.

  - Flagstaff Zen Sangha (flagstaff_zen_sangha)
    Diamond Sangha lineage Zen (Robert Aitken)
    2 South Beaver St Suite 150 (Human Nature Studio), Flagstaff AZ 86001
    Sun 8:30am in-person
    No iCal — seeded as recurring.

  - IKRC Grand Canyon — Flagstaff Class (ikrc_flagstaff)
    New Kadampa Tradition (NKT), outreach from IKRC Grand Canyon (Williams AZ)
    510 N Leroux St (Beacon UU), Flagstaff AZ 86001
    meditationinnorthernarizona.org · Tue 6:30pm in-person, $10/$5
    No separate iCal — seeded as recurring.

Research notes (2026-06-04):
  - FIMC: Monday evenings at Beacon UU confirmed at 6:30pm MST. Google Calendar
    embed on site; no WordPress iCal feed available. Hybrid in-person + Zoom.
    Active Dharma Seed teachers page. Free, dana-based.
  - Flagstaff Zen Sangha: Sunday 8:30am at Human Nature Studio (2 S Beaver St
    Suite 150, downtown). Diamond Sangha / Robert Aitken lineage. First-timers
    arrive at 8:00am for brief orientation. In-person only. Free, drop-in.
    Confirmed via flagstaff365.com listing.
  - IKRC Grand Canyon Flagstaff class: Tuesday 6:30–7:45pm confirmed directly
    from meditationinnorthernarizona.org/flagstaff/ page. At Beacon UU (same
    building as FIMC). Cost $10 / $5 students/seniors / free for members.
    The parent retreat center iCal (meditationinnorthernarizona.org/?ical=1)
    covers the Williams campus only; Flagstaff outreach not in that feed.
  - Katog Jampel Sungling (2708 N 4th St Suite D-4): website unreachable;
    schedule unclear. Deferred.
  - Bell Garden Buddhist Center (same address as Katog): website unreachable;
    possibly same organization. Deferred.
  - Flagstaff Shambhala: formerly met at Flagstaff Middle School (755 N Bonito
    St). Status uncertain post-2019 Shambhala reorganization; no active website
    found. Deferred pending confirmation.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "fimc_flagstaff": Center(
        id="fimc_flagstaff",
        name="Flagstaff Insight Meditation Community",
        url="https://flagstaffinsight.org",
        address="510 N Leroux St",
        city="Flagstaff",
        state="AZ",
        zip_code="86001",
        lat=35.2004,
        lng=-111.6519,
        neighborhood="Downtown Flagstaff",
        tradition=Tradition.THERAVADA,
        notes=(
            "Flagstaff Insight Meditation Community (FIMC) brings Theravada/Vipassana "
            "practice to the Colorado Plateau. Monday Evening Meditation: 6:30pm at "
            "Beacon Unitarian Universalist Congregation (510 N Leroux St, downtown "
            "Flagstaff) — guided sitting meditation followed by a dharma talk and "
            "optional discussion. Hybrid in-person + Zoom. Daily online sits also "
            "offered every morning at 5:00–5:30am and 7:30–8:00am via Zoom. "
            "Free, dana-based; drop-in welcome. FIMC teachers are listed on Dharma "
            "Seed. flagstaffinsight.org."
        ),
    ),
    "flagstaff_zen_sangha": Center(
        id="flagstaff_zen_sangha",
        name="Flagstaff Zen Sangha",
        url="https://flagstaff365.com/organization/flagstaff-zen-sangha/",
        address="2 S Beaver St, Suite 150",
        city="Flagstaff",
        state="AZ",
        zip_code="86001",
        lat=35.1988,
        lng=-111.6510,
        neighborhood="Downtown Flagstaff",
        tradition=Tradition.ZEN,
        notes=(
            "Flagstaff Zen Sangha practices in the Diamond Sangha lineage of "
            "Robert Aitken Roshi. Sunday Morning: 8:30am at Human Nature Studio "
            "(2 South Beaver St, Suite 150, downtown Flagstaff). The program "
            "includes sutra service, kinhin (walking meditation), and two 25-minute "
            "zazen periods. First-time visitors are welcome to arrive at 8:00am "
            "for a brief orientation. In-person only. Free, drop-in. "
            "(928) 699-6651."
        ),
    ),
    "ikrc_flagstaff": Center(
        id="ikrc_flagstaff",
        name="Kadampa Meditation — Flagstaff Class",
        url="https://meditationinnorthernarizona.org/flagstaff/",
        address="510 N Leroux St",
        city="Flagstaff",
        state="AZ",
        zip_code="86001",
        lat=35.2004,
        lng=-111.6519,
        neighborhood="Downtown Flagstaff",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Flagstaff is a weekly outreach class from the "
            "International Kadampa Retreat Center Grand Canyon (IKRC GC) in "
            "Williams, AZ — home to the fifth Kadampa World Peace Temple. "
            "Tuesday Evening Class: 6:30–7:45pm at Beacon Unitarian Universalist "
            "Congregation (510 N Leroux St, downtown Flagstaff). Beginner-friendly "
            "guided meditation and Buddhist teaching; no prior experience needed. "
            "Cost: $10 / $5 students and seniors / free for members. New Kadampa "
            "Tradition (NKT). meditationinnorthernarizona.org/flagstaff/."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — all centers seeded via scripts/sangha-seed-recurring.js
