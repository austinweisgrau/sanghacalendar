"""
Rapid City, South Dakota — Phase 3 expansion (heartbeat 118).

Rapid City (pop. ~75k; metro ~140k) is South Dakota's second-largest city,
located near the Black Hills and Mount Rushmore. Small but active Buddhist
scene with two confirmed centers.

Centers included:
  - Laughing Teabowl Zendo (laughing_teabowl_zendo)
    Soto Zen — lay-led
    3326 Harmony Lane, Rapid City SD 57702
    Tuesday 7:00–9:00pm + Sunday 9:00–10:30am
    No iCal — seeded as recurring.

  - Mother of Wisdom Sangha (mother_of_wisdom_rapid_city)
    Tibetan Vajrayana
    907 Columbus Street, Rapid City SD 57701
    Schedule not confirmed — not seeded. Contact: (605) 341-2404.

Research notes (2026-10-28):
  - Laughing Teabowl Zendo: Soto Zen, lay-led community. 3326 Harmony Lane,
    Rapid City SD 57702. Regular schedule: Tuesday 7:00–9:00pm sit + dharma
    discussion; Sunday 9:00–10:30am zazen + dokusan. Contact: (605) 341-6378.
    No active website found; listed in BuddhaNet World Buddhist Directory.
  - Mother of Wisdom Sangha: Tibetan Vajrayana, 907 Columbus Street, Rapid City
    SD 57701. Phone: (605) 341-2404. Active listing in BuddhaNet. Schedule not
    confirmed from web sources; deferred pending contact.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "laughing_teabowl_zendo": Center(
        id="laughing_teabowl_zendo",
        name="Laughing Teabowl Zendo",
        url=None,
        address="3326 Harmony Lane",
        city="Rapid City",
        state="SD",
        zip_code="57702",
        lat=44.0720,
        lng=-103.2590,
        neighborhood="Rapid City",
        tradition=Tradition.ZEN,
        notes=(
            "Laughing Teabowl Zendo is a Soto Zen practice community at 3326 Harmony "
            "Lane, Rapid City SD 57702. Regular sits: Tuesday evening 7:00–9:00pm "
            "(zazen + dharma discussion) and Sunday morning 9:00–10:30am (zazen + "
            "dokusan). Lay-led community. Open to all; drop-in welcome. "
            "Contact: (605) 341-6378."
        ),
    ),
    "mother_of_wisdom_rapid_city": Center(
        id="mother_of_wisdom_rapid_city",
        name="Mother of Wisdom Sangha",
        url=None,
        address="907 Columbus Street",
        city="Rapid City",
        state="SD",
        zip_code="57701",
        lat=44.0810,
        lng=-103.2270,
        neighborhood="Rapid City",
        tradition=Tradition.TIBETAN,
        notes=(
            "Mother of Wisdom Sangha is a Tibetan Vajrayana Buddhist community at "
            "907 Columbus Street, Rapid City SD 57701. Contact: (605) 341-2404. "
            "Schedule not yet confirmed; contact for current sitting times."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — seeded via scripts/sangha-seed-recurring.js (Laughing Teabowl)
