"""
Fort Collins, CO — Phase 3 expansion (heartbeat 69).

Fort Collins (pop. ~170k; metro ~360k), home of Colorado State University, is
a vibrant Front Range city with a small but active Buddhist community spanning
the Tibetan, Zen, and Plum Village traditions.

Centers included:
  - Heruka Kadampa Meditation Center (heruka_kadampa_fc)
    New Kadampa Tradition (Tibetan/Gelug, Geshe Kelsang Gyatso)
    149 W Harvard St Suite 102, Fort Collins CO 80525
    meditateinfortcollins.org · Mon 6:30pm, Thu 12:15pm, Wed 7pm,
    Fri 5:30pm, Sun 11:30am + 1pm + 2pm (various drop-in classes)
    LIVE iCal feed: meditateinfortcollins.org/calendar/?ical=1

  - Prairie Mountain Zen Center — Fort Collins (prairie_mountain_zen_fc)
    Soto Zen (Dainin Katagiri / Soto Zen Buddhist Association lineage)
    Plymouth Congregational Church, 916 W Prospect Rd, Fort Collins CO 80526
    prairiemountain.org/fort-collins.html · Thu 6:30–8:00pm
    No iCal — seeded as recurring.

  - Zen Meditation at Iyengar Yoga of Fort Collins (zen_fc_wright)
    Harada-Yasutani Zen (Dharma transmission 2023 from Peggy Metta Roshi)
    Iyengar Yoga of Fort Collins, Fort Collins CO
    cwrightyoga.com/zen-meditation/ · Mon 5:30–6:30pm (resumed June 2026)
    No iCal — seeded as recurring.

Research notes (2026-05-26):
  - Heruka Kadampa: Founded 1999. Multiple weekly drop-in sits/classes with
    varying price points (some free, some $10-15). Confirmed iCal feed at
    meditateinfortcollins.org/calendar/?ical=1 (WordPress Events Calendar,
    Content-Type: text/calendar).
  - Prairie Mountain Zen: Soto Zen group led by teacher(s) trained under
    Dainin Katagiri Roshi at Minnesota Zen Center 1977-1989. Listed with the
    Soto Zen Buddhist Association (SZBA). Meets Thursdays at Plymouth
    Congregational Church. Drop-in welcome, no fee mentioned. Wix site has
    no iCal endpoint.
  - Cathy Wright Zen: Authorized teacher (Dharma transmission 2023 from
    Peggy Metta Roshi, Zen Center of Denver). Harada-Yasutani lineage.
    Monday evenings 5:30-6:30pm at Iyengar Yoga of Fort Collins.
    Note: "No Monday night zen until June 1, 2026" — resumes June 2026.
    Free, donations accepted.
  - Fort Collins Shambhala: CLOSED — "let go of its lease."
  - Fort Collins Zen Center (Kwan Um): likely dormant, website down.
  - Fort Collins Zen Group / Great Mountain: likely dormant, website down.
  - Peaceful Heart Sangha: Plum Village lineage, 2nd/4th Sundays, but
    bemindfulfortcollins.org is unreachable and schedule is via private
    Google Group email list. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "heruka_kadampa_fc": Center(
        id="heruka_kadampa_fc",
        name="Heruka Kadampa Meditation Center",
        url="https://www.meditateinfortcollins.org",
        address="149 W Harvard St Suite 102",
        city="Fort Collins",
        state="CO",
        zip_code="80525",
        lat=40.5542,
        lng=-105.0787,
        neighborhood="Midtown Fort Collins",
        tradition=Tradition.TIBETAN,
        notes=(
            "Heruka Kadampa Meditation Center is a New Kadampa Tradition (NKT) "
            "center in Fort Collins, founded in 1999. Part of the Gelug lineage "
            "as revived by Geshe Kelsang Gyatso. Offers multiple weekly drop-in "
            "meditation classes and sitting sessions, including Monday evening "
            "at FoCo Cafe (6:30–7:30pm, $10), Thursday lunchtime Simply Meditate "
            "(12:15–12:45pm), Wednesday evening class (7:00–8:30pm, $15), Friday "
            "after-work meditation (5:30–6:15pm), and Sunday morning class "
            "(11:30am–12:45pm, $15). Also Sunday Prayers for World Peace (2–3pm, "
            "free). No one turned away for lack of funds. "
            "149 W Harvard St, Suite 102, Fort Collins CO 80525. "
            "meditateinfortcollins.org."
        ),
    ),
    "prairie_mountain_zen_fc": Center(
        id="prairie_mountain_zen_fc",
        name="Prairie Mountain Zen Center — Fort Collins",
        url="https://www.prairiemountain.org/fort-collins.html",
        address="916 W Prospect Rd",
        city="Fort Collins",
        state="CO",
        zip_code="80526",
        lat=40.5684,
        lng=-105.0969,
        neighborhood="CSU Area",
        tradition=Tradition.ZEN,
        notes=(
            "Prairie Mountain Zen Center's Fort Collins group meets weekly at "
            "Plymouth Congregational Church (916 W Prospect Rd — enter from north "
            "parking lot door, follow signs to choir room). The teacher trained "
            "under Dainin Katagiri Roshi at Minnesota Zen Center from 1977 to 1989 "
            "and is listed with the Soto Zen Buddhist Association (SZBA). "
            "Thursday evenings 6:30–8:00pm: 30 minutes sitting, 10 minutes "
            "walking, tea and dharma discussion. Drop-in welcome; no fee. "
            "Occasional Saturday one-day sittings (9am–4pm) at the same location. "
            "Contact: cliff@prairiemountain.org or david.pavlacky@gmail.com. "
            "prairiemountain.org/fort-collins.html."
        ),
    ),
    "zen_fc_wright": Center(
        id="zen_fc_wright",
        name="Zen Meditation with Cathy Wright — Fort Collins",
        url="https://www.cwrightyoga.com/zen-meditation/",
        address="Fort Collins",
        city="Fort Collins",
        state="CO",
        zip_code="80521",
        lat=40.5853,
        lng=-105.0844,
        neighborhood="Fort Collins",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Meditation sits led by Cathy 'Seizan' Wright, an authorized "
            "teacher who received Dharma transmission in 2023 from Peggy Metta "
            "Roshi at the Zen Center of Denver (Harada-Yasutani lineage, training "
            "in both Soto and Rinzai styles). Monday evenings 5:30–6:30pm: one "
            "hour silent sitting at Iyengar Yoga of Fort Collins (Sunrise Room). "
            "Drop-in; free, donations accepted for space rental. "
            "cwrightyoga.com/zen-meditation/."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "heruka_kadampa_fc": {
        "url": "https://www.meditateinfortcollins.org/calendar/?ical=1",
        "filter_to_sits": True,
    },
}
