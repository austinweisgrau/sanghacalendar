"""
Iowa City, Iowa — Phase 3 expansion (heartbeat 117).

Iowa City (pop. ~74k; metro ~170k) is home to the University of Iowa and
hosts a small but active Buddhist scene. Two distinct traditions are
represented with regular public sits.

Centers included:
  - Iowa City Zen Center (iowa_city_zen)
    Soto Zen — Rev. Daiken Nelson Roshi
    1025 E Fairchild St, Iowa City IA 52245
    iowacityzencenter.org
    Mon–Fri 7–8am + Tue 7–8pm + Sun 9am in-person + Zoom hybrid
    No iCal — seeded as recurring.

  - Garchen Mila Buddhist Center (garchen_mila_iowa_city)
    Tibetan Vajrayana (Drikung Kagyu / Garchen Rinpoche lineage)
    209 E Washington St Suite 200, Iowa City IA 52240
    milarepaiowa.org
    Sun 10–11:15am in-person (drop-in)
    No iCal — seeded as recurring.

Research notes (2026-10-25):
  - Iowa City Zen Center: Founded mid-20th century, one of Iowa's oldest Zen
    sanghas. Resident teacher Rev. Daiken Nelson Roshi (Soto lineage). Weekly
    schedule: Mon–Fri 7:00–8:00am zazen (in-person + Zoom); Tue 6:30pm
    instruction + 7:00–8:00pm zazen (in-person + Zoom); Mon 7:00–8:15pm
    "Sitting with Impermanence" (collaboration with Death Collective of Eastern
    Iowa); Sun 8:30am instruction + 9:00am zazen + 10:00am dharma talk (2nd/4th
    Sundays). Zoom: https://us02web.zoom.us/j/83767296520. iowacityzencenter.org.
  - Garchen Mila Buddhist Center: Affiliated with Garchen Rinpoche (Drikung Kagyu).
    Located in downtown Iowa City at The Paul Helen Building. Sunday morning
    practice: dharma reading (rotating: Shantideva's Way of the Bodhisattva, 37
    Practices, Kuntuzangpo prayer), silent contemplation, guided compassion
    meditation with "Om Ah Hung" mantra. 10:00–11:15am through Dec 2026; likely
    to continue. Free / dana. Contact: sangha@milarepaiowa.org. milarepaiowa.org.
  - Lamrim Kadampa Buddhist Center: Actually located in Davenport IA (Quad
    Cities), ~65 mi east of Iowa City — out of scope for Iowa City metro.
  - No Shambhala center found in Iowa City metro (nearest is Minneapolis or Chicago).
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "iowa_city_zen": Center(
        id="iowa_city_zen",
        name="Iowa City Zen Center",
        url="https://www.iowacityzencenter.org",
        address="1025 E Fairchild St",
        city="Iowa City",
        state="IA",
        zip_code="52245",
        lat=41.6674,
        lng=-91.5240,
        neighborhood="Near East Side",
        tradition=Tradition.ZEN,
        notes=(
            "Iowa City Zen Center is a Soto Zen practice community at 1025 E "
            "Fairchild St, Iowa City IA. Resident teacher: Rev. Daiken Nelson Roshi "
            "(Soto lineage). Regular schedule: Monday–Friday 7:00–8:00am zazen "
            "(in-person + Zoom); Tuesday 7:00–8:00pm zazen with beginning instruction "
            "at 6:30pm (in-person + Zoom); Monday 7:00–8:15pm 'Sitting with "
            "Impermanence' in collaboration with the Death Collective of Eastern Iowa; "
            "Sunday 9:00am zazen (instruction 8:30am) with dharma talk at 10am on "
            "2nd and 4th Sundays (in-person + Zoom). Open to all; drop-in welcome. "
            "iowacityzencenter.org."
        ),
    ),
    "garchen_mila_iowa_city": Center(
        id="garchen_mila_iowa_city",
        name="Garchen Mila Buddhist Center",
        url="https://milarepaiowa.org",
        address="209 E Washington St Suite 200",
        city="Iowa City",
        state="IA",
        zip_code="52240",
        lat=41.6601,
        lng=-91.5351,
        neighborhood="Downtown Iowa City",
        tradition=Tradition.TIBETAN,
        notes=(
            "Garchen Mila Buddhist Center is a Tibetan Vajrayana community in the "
            "Drikung Kagyu lineage of Garchen Rinpoche, located at The Paul Helen "
            "Building, 209 E Washington St Suite 200, Iowa City IA. Sunday morning "
            "practice (10:00–11:15am) follows the Three Activities: group dharma "
            "reading (rotating among Shantideva's Way of the Bodhisattva, 37 Practices "
            "of a Bodhisattva, and the Kuntuzangpo prayer), silent contemplation, and "
            "guided compassion meditation with the 'Om Ah Hung' mantra. Drop-in "
            "welcome; offered freely in the tradition of generosity. "
            "sangha@milarepaiowa.org · milarepaiowa.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — all centers seeded via scripts/sangha-seed-recurring.js
