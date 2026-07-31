"""
Savannah, Georgia — Phase 3 expansion (heartbeat 93).

Savannah (pop. ~390k metro, oldest city in Georgia) has a small but genuine
Buddhist meditation community anchored by two active Zen centers and a
Vietnamese Mahayana temple offering English-language sits.

Centers included:
  - Ancient Oaks Zen Community (ancient_oaks_zen)
    Soto Zen (International Zen Garland Order — Maezumi Roshi lineage)
    4501 Montgomery Street D, Savannah GA 31405
    ancientoakszen.org · Thu 7–8pm + Sun 9–11:30am (in-person)
    → No iCal (Modern Events Calendar, JS-rendered); seeded as recurring

  - Flying Cloud Zen (flying_cloud_zen)
    Soto Zen (Silent Thunder Order — SFZC / Shunryu Suzuki lineage)
    2132 E Victory Drive, Savannah GA 31404
    flyingcloudzen.org · Thu 8–8:30am + Sat 8:30–9:30am (in-person)
    → No iCal; seeded as recurring

  - Vietnamese Buddhist Association of Savannah / Chua Cat Tuong (chua_cat_tuong_savannah)
    Vietnamese Mahayana / Pure Land
    2619 US Highway 80 W, Garden City GA 31408 (~8 miles west of downtown)
    savannahbuddhist.org · Thu 7–8pm English-language meditation (in-person)
    → No iCal (Squarespace); seeded as recurring

Research notes (2026-07-31):
  - Ancient Oaks Zen Community: Founded 2012 by Roshi Paul Genki Kahn and
    Roshi Monika Genmitsu Kahn. Affiliated with the International Zen Garland
    Order (IZGO), in the lineage of Taizan Maezumi Roshi. Address: 4501
    Montgomery Street D, Savannah GA 31405. Thursday 7–8pm: zazen with Roshi
    Genmitsu (in-person, drop-in). Sunday 9–11:30am: Zen Liturgy, zazen,
    dokusan (individual student/teacher interview), and Dharma Talk (in-person).
    Tuesday 6–7pm: Introduction to Zen (by appointment only — excluded).
    Also runs Ango (3-month intensive) and sesshins. ancientoakszen.org.
    Phone: 201-616-9263.
  - Flying Cloud Zen: Lay-led Soto Zen group led by Un Shin Cindy Beach, Sensei
    (Silent Thunder Order, SFZC/Suzuki lineage). Formerly "Savannah Zen Center"
    and "Floating Cloud Zen." Address: 2132 E Victory Drive, Savannah GA 31404.
    Thursday 8–8:30am: zazen (in-person). Saturday 8:30–9:30am: shared silent
    sitting, metta/Heart Sutra chant, informal Q&A (in-person; explicitly open
    to newcomers). Small community, welcoming to beginners. flyingcloudzen.org.
  - Chua Cat Tuong (Vietnamese Buddhist Association of Savannah): Vietnamese
    Mahayana / Pure Land temple at 2619 US Highway 80 W, Garden City GA 31408
    (~8 miles west of downtown Savannah). Thursday 7–8pm English-language
    meditation and Dhamma Talk: explicitly drop-in, no appointment needed, open
    to all backgrounds. Sunday 10am–12pm: Vietnamese-language service (All are
    welcome but primarily cultural). Seeding Thursday English-language session
    only. savannahbuddhist.org. Phone: 912-657-1876.
  - Lotus Templar (Theravada nonprofit, founded 2023): website down/inaccessible
    at time of research; no public schedule found. Deferred — monitor.
  - No Shambhala, Kadampa/KMC, or Plum Village group confirmed in Savannah.
    Nearest Kadampa is Atlanta (741 Edgewood Ave); nearest Shambhala is Decatur.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "ancient_oaks_zen": Center(
        id="ancient_oaks_zen",
        name="Ancient Oaks Zen Community",
        url="https://ancientoakszen.org",
        address="4501 Montgomery Street D",
        city="Savannah",
        state="GA",
        zip_code="31405",
        lat=32.0850,
        lng=-81.1061,
        neighborhood="Midtown Savannah",
        tradition=Tradition.ZEN,
        notes=(
            "Ancient Oaks Zen Community is a Soto Zen center in Savannah, Georgia, "
            "founded in 2012 by Roshi Paul Genki Kahn and Roshi Monika Genmitsu Kahn. "
            "Affiliated with the International Zen Garland Order (IZGO) in the lineage "
            "of Taizan Maezumi Roshi. Address: 4501 Montgomery Street D, Savannah GA "
            "31405. Public sitting schedule: Thursday 7–8pm zazen with Roshi Genmitsu "
            "(in-person, drop-in); Sunday 9–11:30am full Zen morning program (liturgy, "
            "zazen, dokusan, and Dharma Talk, in-person). Also runs Ango (3-month "
            "intensive training) and sesshins. The most established Buddhist meditation "
            "center in Savannah. ancientoakszen.org. Phone: 201-616-9263."
        ),
    ),
    "flying_cloud_zen": Center(
        id="flying_cloud_zen",
        name="Flying Cloud Zen",
        url="https://flyingcloudzen.org",
        address="2132 E Victory Drive",
        city="Savannah",
        state="GA",
        zip_code="31404",
        lat=32.0567,
        lng=-81.0627,
        neighborhood="Midtown Savannah",
        tradition=Tradition.ZEN,
        notes=(
            "Flying Cloud Zen (formerly Savannah Zen Center / Floating Cloud Zen) is "
            "a lay-led Soto Zen community in the lineage of Shunryu Suzuki Roshi and "
            "the San Francisco Zen Center (Silent Thunder Order). Teacher: Un Shin "
            "Cindy Beach, Sensei. Address: 2132 E Victory Drive, Savannah GA 31404. "
            "Regular schedule: Thursday 8:00–8:30am zazen (in-person); Saturday "
            "8:30–9:30am Saturday Morning Meditation Community — 25 minutes of shared "
            "silent sitting, brief sutra chant, then 30 minutes of informal practice "
            "Q&A welcoming to beginners (in-person). Free, drop-in. "
            "flyingcloudzen.org."
        ),
    ),
    "chua_cat_tuong_savannah": Center(
        id="chua_cat_tuong_savannah",
        name="Vietnamese Buddhist Association of Savannah — Chùa Cát Tường",
        url="https://savannahbuddhist.org",
        address="2619 US Highway 80 W",
        city="Garden City",
        state="GA",
        zip_code="31408",
        lat=32.0889,
        lng=-81.1975,
        neighborhood="Garden City",
        tradition=Tradition.OTHER,
        notes=(
            "Vietnamese Buddhist Association of Savannah / Chùa Cát Tường is a "
            "Vietnamese Mahayana temple (Pure Land tradition) at 2619 US Highway 80 W, "
            "Garden City GA 31408 (~8 miles west of downtown Savannah). "
            "English-language meditation and Dhamma Talk: Thursday 7–8pm, in-person, "
            "no appointment needed, open to all backgrounds. Sunday 10am–12pm: "
            "Vietnamese-language service, vegetarian meal follows (all welcome). "
            "Free. Phone: 912-657-1876. Email: thienhanhus@gmail.com. "
            "savannahbuddhist.org."
        ),
    ),
}

# No live iCal feeds — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
