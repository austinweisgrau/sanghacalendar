"""
Huntsville, Alabama — Phase 3 expansion (heartbeat 74).

Huntsville (pop. ~215k; metro ~500k) is Alabama's second-largest city and
home to NASA's Marshall Space Flight Center and a significant tech/research
community. The Buddhist meditation scene is small but active, anchored by
Green Mountain Zen Center on the city's south side.

Centers included:
  - Green Mountain Zen Center (green_mountain_zen)
    Korean/Rinzai Zen (Single Flower Sangha / Kwan Um lineage)
    12035 Mountcrest Rd SE, Huntsville AL 35803 (Green Mountain neighborhood)
    gmzc.us · Sun 6pm in-person + virtual
    No iCal — seeded as recurring.

Research notes (2026-06-01):
  - Green Mountain Zen Center: founded 1993. Guiding teacher George Bowman
    (BoMun), Zen Master, Single Flower Sangha. Local teachers: Gary Beard
    (Bodhin) and Jim Gordon (Shogen). Sunday Meditation: 6:00–7:30pm (brief
    chanting + two zazen periods + kinhin; newcomers welcome). Wednesday Night
    Discussion: 7:00–8:30pm (dharma study group, not a formal sit). Both
    sessions in-person + Zoom. Website requires email/call before first visit.
    12035 Mountcrest Rd SE, Huntsville AL 35803.
  - Huntsville Shambhala Group: Shambhala satellite (meets at UU Church, 3921
    Broadmor Rd SW). Calendar shows "No events to display." Programming is
    irregular/sparse. Deferred pending schedule confirmation.
  - Kadampa N. Alabama Study Group: NKT, but classes are now in Florence AL
    (~90 miles NW, Shoals area). Not Huntsville coverage — deferred.
  - Bodhi Center of Huntsville (huntsvillebodhicenter.org): website down
    (ECONNREFUSED). Status unknown — deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "green_mountain_zen": Center(
        id="green_mountain_zen",
        name="Green Mountain Zen Center",
        url="https://www.gmzc.us",
        address="12035 Mountcrest Rd SE",
        city="Huntsville",
        state="AL",
        zip_code="35803",
        lat=34.6279,
        lng=-86.5183,
        neighborhood="Green Mountain",
        tradition=Tradition.ZEN,
        notes=(
            "Green Mountain Zen Center (GMZC) has served Huntsville since 1993, "
            "making it one of the oldest Zen communities in Alabama. Rooted in the "
            "Kwan Um School of Zen (Korean Zen, Seung Sahn lineage) through the "
            "Single Flower Sangha of Zen Master George Bowman (BoMun). Local "
            "teachers are Gary Beard (Bodhin) and Jim Gordon (Shogen). Located on "
            "Green Mountain in south Huntsville at 12035 Mountcrest Rd SE. "
            "Sunday Meditation: 6:00–7:30pm — brief chanting, two zazen periods "
            "with kinhin (walking meditation), and optional social gathering "
            "afterward. Wednesday Night Discussion Group: 7:00–8:30pm — dharma "
            "study and discussion. Both sessions are in-person with Zoom "
            "available. Newcomers welcome; please email before attending. "
            "greenmountainzenhsv@gmail.com · (256) 426-3344 · gmzc.us."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — center seeded via scripts/sangha-seed-recurring.js
