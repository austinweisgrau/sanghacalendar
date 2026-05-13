"""
Sacramento, CA meditation center sources — Phase 3 expansion.

The Sacramento meditation scene is anchored by Sacramento Dharma Center (SDC),
a shared nonprofit campus at 3111 Wissemann Drive hosting three distinct sanghas.
Lion's Roar Dharma Center is a separate Tibetan Buddhist center downtown.

iCal feeds:
  - Sacramento Buddhist Meditation Group (SBMG)
    WordPress Events Calendar: https://sbmg.org/events/?ical=1
    Sunday 10am sits with rotating teachers, Tuesday 7am online meditation,
    BIPOC Sangha (4th Sunday), Family Sangha, and garden sits.
  - Valley Streams Zen Sangha (VSZS)
    WordPress Events Calendar: https://valleystreamszen.org/events/?ical=1
    Thursday 6am Morning Zazen + Service (hybrid), Monday 7pm Evening Program,
    Study groups, and occasional dharma talks.
  - Lion's Roar Dharma Center (LRDC)
    Google Calendar: 9ohgorq8dhupc1u8b0hhtiafbc@group.calendar.google.com
    Monthly Vajrayana practices on moon phases, Sunday services, special teachings.

Recurring sits (seeded in sangha-seed-recurring.js):
  - Sacramento Insight Meditation (SIM) — Thu 7pm Meditation & Dharma Talk (hybrid)
    3111 Wissemann Drive, Sacramento CA 95826. Theravada/Insight.
  - Sacramento Insight Meditation — Tue 6:30pm Dharma Recovery Sangha (in-person)
    3111 Wissemann Drive. Open to all, especially those in recovery.

Research notes (2026-05-13):
  - Sacramento Dharma Center (sacdharma.org): 3111 Wissemann Drive, Sacramento CA 95826.
    Shared campus with meditation hall, meeting rooms, library, kitchen on 1.7 acres.
    Hosts SBMG (since 1977), Valley Streams Zen Sangha, and Sacramento Insight Meditation.
  - SBMG (sbmg.org): Oldest/largest pluralist meditation sangha in Sacramento. Active
    WordPress Events Calendar iCal confirmed working. Sunday sits (10am–12pm, hybrid)
    with rotating teachers (Zen, Vipassana, Tibetan, eclectic). Tuesday 7am online.
    BIPOC Sangha 4th Sunday. Family Sangha 4th Sunday 10am. By donation.
  - Valley Streams Zen Sangha (valleystreamszen.org): Ordinary Mind Zen / Soto Zen
    (Charlotte Joko Beck lineage). Active WordPress Events Calendar iCal confirmed.
    Thursday 6am Morning Zazen + Service (hybrid). Monday 7pm Evening Program (hybrid).
    Also monthly Intro to Zen (2nd Monday 6pm, in-person).
  - Sacramento Insight Meditation (sactoinsight.org): Incapsula blocks all HTTP access —
    iCal not fetchable. Thu 7pm Meditation & Dharma Talk (hybrid) confirmed from web.
    Tue 6:30pm Dharma Recovery Sangha (in-person). Wed 7pm Young Persons Sangha (hybrid,
    bi-weekly). Seeded as recurring sits.
  - Lion's Roar Dharma Center (lionsroardharmacenter.org): 3240 B Street, Sacramento CA
    95816 (between 32nd and 33rd Street, Midtown). Google Calendar active and public.
    Tibetan Buddhist (Gelugpa / Kadampa orientation). Offers monthly Vajrayana practices
    on moon phases (in-person + online), Sunday services, occasional visiting teacher
    programs. Teaching lineage centers on Lama Yeshe Jinpa.
  - Sacramento Shambhala: No independent Sacramento center listed — covered under
    Northern California Shambhala network (Berkeley, SF, Davis, Silicon Valley, Sonoma).
  - KMC Sacramento (meditationinsacramento.org): Domain not resolving — appears defunct.
  - Sacramento Zen (sacramentozen.com): Ordinary Mind Zen group meeting in private Elmhurst-
    area zendo (near UC Davis Medical Center). Address not publicly listed (contact required).
    Mon 7am + Tue 7pm sits. Deferred due to private location and no iCal.
  - Davis Shambhala (25 mi west): Part of NorCal Shambhala network. Separate metro — deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "sbmg_sacramento": Center(
        id="sbmg_sacramento",
        name="Sacramento Buddhist Meditation Group",
        url="https://sbmg.org",
        address="3111 Wissemann Drive",
        city="Sacramento",
        state="CA",
        zip_code="95826",
        lat=38.5516,
        lng=-121.3810,
        neighborhood="Florin / Meadowview (Sacramento Dharma Center)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Sacramento Buddhist Meditation Group (SBMG) is the oldest and largest pluralist "
            "meditation sangha in Sacramento, founded in the 1970s. Located at Sacramento Dharma "
            "Center, a shared nonprofit campus at 3111 Wissemann Drive. Weekly Sunday Meditation "
            "& Dharma Talk (10am–12pm, hybrid): 40-minute silent sit followed by talk from a "
            "rotating teacher (Zen, Vipassana, Tibetan, secular, eclectic traditions). Tuesday "
            "Online Morning Meditation (7–8:15am via Zoom). First Sundays: Introduction to "
            "Meditation (9–9:30am, free). BIPOC Sangha (4th Sunday 1:15pm) and Family Sangha "
            "(4th Sunday 10am) also offered. All programs dana (donation) based; all welcome."
        ),
    ),
    "valley_streams_zen": Center(
        id="valley_streams_zen",
        name="Valley Streams Zen Sangha",
        url="https://valleystreamszen.org",
        address="3111 Wissemann Drive",
        city="Sacramento",
        state="CA",
        zip_code="95826",
        lat=38.5516,
        lng=-121.3810,
        neighborhood="Florin / Meadowview (Sacramento Dharma Center)",
        tradition=Tradition.ZEN,
        notes=(
            "Valley Streams Zen Sangha is a Soto Zen community in the Ordinary Mind Zen school "
            "— the lineage of Charlotte Joko Beck (Dharma successors adapting Zen practice for "
            "Western temperaments while maintaining traditional rigor). Based at Sacramento Dharma "
            "Center, 3111 Wissemann Drive. Weekly Morning Zazen & Service (Thursdays 6–7:30am, "
            "hybrid): zazen, kinhin, service, and informal tea. Monday Evening Program (7–9pm, "
            "hybrid): dharma talks, study, and sitting. Introduction to Zen Meditation (2nd Monday, "
            "6pm, in-person) for newcomers. Drop-in welcome; free."
        ),
    ),
    "sacramento_insight_meditation": Center(
        id="sacramento_insight_meditation",
        name="Sacramento Insight Meditation",
        url="https://sactoinsight.org",
        address="3111 Wissemann Drive",
        city="Sacramento",
        state="CA",
        zip_code="95826",
        lat=38.5516,
        lng=-121.3810,
        neighborhood="Florin / Meadowview (Sacramento Dharma Center)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Sacramento Insight Meditation (SIM) is a Theravada/Vipassana sangha meeting at "
            "Sacramento Dharma Center, 3111 Wissemann Drive. Weekly Thursday Meditation & "
            "Dharma Talk (7–9pm, hybrid): guided sitting meditation, dharma talk, and "
            "discussion — open to all levels. Also Tuesday Dharma Recovery Sangha (6:30–8pm, "
            "in-person): meditation and discussion for people seeking recovery, open to all. "
            "Monthly one-day retreats offered on donation basis. Young Persons Sangha "
            "(bi-weekly Wednesdays 7pm) for adults in 20s–40s. All programs dana-based."
        ),
    ),
    "lions_roar_dharma_center": Center(
        id="lions_roar_dharma_center",
        name="Lion's Roar Dharma Center",
        url="https://lionsroardharmacenter.org",
        address="3240 B Street",
        city="Sacramento",
        state="CA",
        zip_code="95816",
        lat=38.5768,
        lng=-121.4545,
        neighborhood="Midtown Sacramento",
        tradition=Tradition.TIBETAN,
        notes=(
            "Lion's Roar Dharma Center (LRDC) is a Tibetan Buddhist center in Midtown Sacramento, "
            "located at the Do Nga Dargey Temple (3240 B Street, between 32nd and 33rd). The "
            "resident teacher is Lama Yeshe Jinpa. Offers monthly in-person Vajrayana Buddhist "
            "practices on the phases of the moon (waxing, full, waning, new), Sunday services "
            "including the Shambhala Journey practice, and occasional visiting teacher programs "
            "and special teachings. Also hosts the Sustainable Service Program (quarterly "
            "half-day retreats) and Delek/Service Group meetings. All programs are hybrid "
            "(in-person and online). Dana-based; all welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "sbmg_sacramento": {
        "url": "https://sbmg.org/events/?ical=1",
        "center_id": "sbmg_sacramento",
        "filter_to_sits": True,
    },
    "valley_streams_zen": {
        "url": "https://valleystreamszen.org/events/?ical=1",
        "center_id": "valley_streams_zen",
        "filter_to_sits": True,
    },
    "lions_roar_gcal": {
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "9ohgorq8dhupc1u8b0hhtiafbc%40group.calendar.google.com"
            "/public/basic.ics"
        ),
        "center_id": "lions_roar_dharma_center",
        "filter_to_sits": True,
    },
}
