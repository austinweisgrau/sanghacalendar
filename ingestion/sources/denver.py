"""
Denver / Boulder meditation center sources — Phase 3 expansion.

iCal feeds:
  - Zen Center of Denver (zencenterofdenver.org/events/?ical=1)
  - Boulder Zen Center (Google Calendar ICS)
  - Orgyen Khandroling Denver (Google Calendar ICS)

Recurring sits (no accessible iCal — Shambhala Cologne server down):
  - Boulder Shambhala Center — Thu 7pm Open Class, Sun 9am Sitting Practice
  - Denver Shambhala Center  — Sun 10am Group Meditation
"""

import logging

from data.schemas.event import Center, Tradition

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "zen_center_denver": Center(
        id="zen_center_denver",
        name="Zen Center of Denver",
        url="https://zencenterofdenver.org",
        address="1856 S Columbine St",
        city="Denver",
        state="CO",
        zip_code="80210",
        lat=39.6956,
        lng=-104.9614,
        neighborhood="Washington Park East",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Center of Denver is one of the most active Zen communities in the Rocky Mountain "
            "region, led by Roshi Enkyo O'Hara (Village Zendo lineage) and resident teacher Peggy "
            "Metta Roshi. Weekly program includes Zoom Zen (daily online zazen), Tuesday morning "
            "and evening zazen, Thursday morning zazen 6:30am and evening zazen 7pm, and Saturday "
            "Zazenkai. Queer Dharma monthly, Zen of Recovery, MBSR, Cha Dao (tea ceremony). "
            "Livestreamed sessions available for all sittings. Dana-based (pay what you can)."
        ),
    ),
    "boulder_zen": Center(
        id="boulder_zen",
        name="Boulder Zen Center",
        url="https://www.boulderzen.org",
        address="2151 Arapahoe Ave",
        city="Boulder",
        state="CO",
        zip_code="80302",
        lat=40.0106,
        lng=-105.2541,
        neighborhood="Central Boulder",
        tradition=Tradition.ZEN,
        notes=(
            "Boulder Zen Center is a residential Zen practice community in Boulder's central "
            "neighborhood, led by Zenki Roshi in the Soto Zen tradition (White Plum Asanga lineage). "
            "Regular public sittings include weekly zazen, dharma talks, and sesshins. "
            "The center also offers individual dokusan (interview) and retreats. "
            "Located near the Pearl Street Mall."
        ),
    ),
    "orgyen_khandroling": Center(
        id="orgyen_khandroling",
        name="Orgyen Khandroling",
        url="https://orgyenkhandroling.org",
        address="3300 Josephine St",
        city="Denver",
        state="CO",
        zip_code="80205",
        lat=39.7629,
        lng=-104.9600,
        neighborhood="Cole / Northeast Denver",
        tradition=Tradition.TIBETAN,
        notes=(
            "Orgyen Khandroling is a Longchen Nyingthig / Dzogchen center in Northeast Denver, "
            "the seat of Anyen Rinpoche's international organization. The center offers regular "
            "Open Meditation sessions (Wednesday evenings, Sunday mornings), Tara Recitation, "
            "Tsok practice on auspicious lunar days, and periodic retreats. The teaching "
            "lineage is Nyingma Dzogchen — a direct transmission from Khenchen Tsewang Rigdzin "
            "and Dilgo Khyentse Rinpoche. Open to all levels; no prior Buddhist knowledge required."
        ),
    ),
    "shambhala_boulder": Center(
        id="shambhala_boulder",
        name="Boulder Shambhala Center",
        url="https://boulder.shambhala.org",
        address="1345 Spruce St",
        city="Boulder",
        state="CO",
        zip_code="80302",
        lat=40.0150,
        lng=-105.2705,
        neighborhood="Central Boulder",
        tradition=Tradition.TIBETAN,
        notes=(
            "Boulder Shambhala Center offers meditation in the Shambhala Buddhist tradition "
            "(Chögyam Trungpa lineage) from their central Boulder location near the Pearl Street "
            "Mall. Regular public programs: Thursday Night Open Class 7–8:45pm (in-person, "
            "all welcome), and Young Meditators 1st & 3rd Wednesdays 6:30–8pm. Meditation "
            "instruction available. Free introductory classes. Generosity policy — no one turned "
            "away for lack of funds. Calendar at boulder.shambhala.org."
        ),
    ),
    "shambhala_denver": Center(
        id="shambhala_denver",
        name="Shambhala Meditation Center of Denver",
        url="https://denver.shambhala.org",
        address="2305 S Syracuse Way, Suite 214",
        city="Denver",
        state="CO",
        zip_code="80231",
        lat=39.6519,
        lng=-104.8822,
        neighborhood="Hampden South / Tamarac Square",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Center of Denver offers meditation in the Shambhala Buddhist "
            "tradition (Chögyam Trungpa lineage) from their southeast Denver location in the "
            "Tamarac Square area. Weekly Sunday morning group meditation session at 10:00 AM "
            "(in-person); Open House and Meditation Instruction monthly (4th Sunday 10am, free). "
            "Heart of Recovery, Death and Dying sangha, and other programs. Free introductory "
            "meditation instruction at the start of the Sunday session."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Phase 3 Denver/Boulder — iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "zen_center_denver": {
        # WordPress The Events Calendar — confirmed working 2026-05-07
        "url": "https://zencenterofdenver.org/events/?ical=1",
        "filter_to_sits": True,
    },
    "boulder_zen": {
        # Google Calendar public ICS — confirmed working 2026-05-07
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "c_4q7en2flnpgd2vejquq61deiuk%40group.calendar.google.com/public/basic.ics"
        ),
        "filter_to_sits": True,
    },
    "orgyen_khandroling": {
        # Google Calendar public ICS — confirmed working 2026-05-07
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "orgyenkhamdroling.org_naq1onh8q4o6pl9bpvmi2fuqs8%40group.calendar.google.com/public/basic.ics"
        ),
        "filter_to_sits": True,
    },
}
