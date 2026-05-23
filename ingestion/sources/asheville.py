"""
Asheville, NC — Phase 3 expansion.

Asheville is a progressive mountain city (pop. ~95k city, ~500k metro) with a
strong spiritual community and a notable Buddhist presence across traditions.

Centers included:
  - Zen Center of Asheville (zen_center_asheville) — Zen (Soto)
    227 Edgewood Rd, Asheville NC 28804. zcasheville.org
    Mon/Wed/Fri 6am morning zazen; Sat 6am (extended); Tue 7pm evening zazen + talk.
    No iCal (FrontPage 3.0 static site); seeded recurring.

  - Mountain Mindfulness Sangha (mountain_mindfulness_asheville) — Other (Plum Village/TNH)
    227 Edgewood Road, Asheville NC 28804 (Asheville Friends Meeting).
    Thu 7pm weekly (4 rotating formats); 1st Sat 10am outdoor (seasonal, Weaverville).
    No iCal; seeded recurring.

  - Asheville Insight Meditation (asheville_insight_meditation) — Theravada
    85 Weaverville Road, Unit 5, Woodfin NC 28804. ashevillemeditation.com
    Thu 7pm in-person + Zoom. (Sun sits are Zoom-only.)
    No iCal; seeded recurring.

  - Anattasati Magga (anattasati_magga) — Zen (Soto)
    32 Mineral Dust Drive, Asheville NC 28806. anattasatimagga.org
    Sun 10am in-person + Zoom. Lay Soto Zen sangha on 7 quiet acres, West Asheville.
    No iCal; seeded recurring.

Research notes (2026-05-23):
  - Je Tsongkhapa Kadampa (meditationinasheville.org, 1070 Tunnel Rd): iCal shows all
    events at "Zen Rabbit Yoga, Travelers Rest, SC 29690" — not in Asheville. Classes
    appear to have moved to Travelers Rest SC satellite location. Skipped.
  - Southern Dharma Retreat Center (Hot Springs, NC): retreat-only, no drop-in. Skip.
  - Windhorse Zen Community: monastic residential center, not drop-in public sits. Skip.
  - Urban Dharma NC (udharmanc.com): Sri Lankan Theravada temple — community-focused,
    no confirmed public drop-in sits. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "zen_center_asheville": Center(
        id="zen_center_asheville",
        name="Zen Center of Asheville",
        url="https://zcasheville.org",
        address="227 Edgewood Rd",
        city="Asheville",
        state="NC",
        zip_code="28804",
        lat=35.6182,
        lng=-82.5564,
        neighborhood="North Asheville",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Center of Asheville (ZCA) offers regular zazen in the Soto Zen "
            "tradition. Morning zazen: Mon/Wed/Fri 6–6:50am (zazen 40 min). Saturday "
            "6–7:40am (extended: zazen, kinhin, zazen, Heart Sutra). Tuesday evening: "
            "7pm zazen (30 min) + 7:30–8:30pm dharma talk and discussion. New student "
            "instruction (1st Tuesday, 6pm) by registration. All sits drop-in; dana "
            "$10 for evening. Meets at the Asheville Friends Meeting building."
        ),
    ),
    "mountain_mindfulness_asheville": Center(
        id="mountain_mindfulness_asheville",
        name="Mountain Mindfulness Sangha of Asheville",
        url="https://www.mountainmindfulness.org",
        address="227 Edgewood Road",
        city="Asheville",
        state="NC",
        zip_code="28804",
        lat=35.6182,
        lng=-82.5564,
        neighborhood="North Asheville",
        tradition=Tradition.OTHER,
        notes=(
            "Mountain Mindfulness Sangha practices engaged Buddhism in the tradition of "
            "Thich Nhat Hanh (Plum Village). Thursday 7–8:30pm at Asheville Friends "
            "Meeting (227 Edgewood Road): four rotating formats — 1st Thu: Heart Sutra "
            "chanting; 2nd Thu: Plum Village book reading; 3rd Thu: silent sitting and "
            "walking; 4th Thu: Five Mindfulness Trainings recitation. First Saturday of "
            "month (warm season, ~Mar–Oct): 10–11:30am outdoor practice at Weaverville "
            "Main Street Nature Park. Drop-in welcome; free."
        ),
    ),
    "asheville_insight_meditation": Center(
        id="asheville_insight_meditation",
        name="Asheville Insight Meditation",
        url="https://www.ashevillemeditation.com",
        address="85 Weaverville Road, Unit 5",
        city="Woodfin",
        state="NC",
        zip_code="28804",
        lat=35.6481,
        lng=-82.5802,
        neighborhood="Woodfin (North Asheville metro)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Asheville Insight Meditation offers weekly Insight Meditation sits in the "
            "Vipassana tradition ('Dharma without the Dogma'). Thursday Evening "
            "Meditation 7–8:30pm: 30-min guided meditation, 30-min dharma talk, 30-min "
            "Q&A/discussion — in-person at 85 Weaverville Road, Unit 5, Woodfin, plus "
            "Zoom. Sunday morning sits are Zoom-only. Drop-in; free."
        ),
    ),
    "anattasati_magga": Center(
        id="anattasati_magga",
        name="Anattasati Magga",
        url="https://anattasatimagga.org",
        address="32 Mineral Dust Drive",
        city="Asheville",
        state="NC",
        zip_code="28806",
        lat=35.5668,
        lng=-82.6224,
        neighborhood="West Asheville",
        tradition=Tradition.ZEN,
        notes=(
            "Anattasati Magga is a lay Soto Zen Buddhist sangha set on 7 quiet acres in "
            "West Asheville. Sunday 10am–12pm: 30-min sitting meditation, chants and "
            "recitations, and a dharma class — in-person at 32 Mineral Dust Drive or "
            "via Zoom. Second Sunday includes new-student orientation. Teacher: Sujata "
            "(Nancy Hampton). Free; donations welcome. Contact: nancy@anattasatimagga.org."
        ),
    ),
}

# No live iCal feeds for Asheville centers — all sits seeded as recurring.
ICAL_FEEDS: dict = {}
