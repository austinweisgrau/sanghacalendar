"""
Portland, OR meditation center sources — Phase 3 expansion.

iCal feeds:
  - Dharma Rain Zen Center (dharma-rain.org/events/?ical=1)
  - Kagyu Changchub Chuling (kcc.org/calendar/month/?ical=1)

Recurring sits (no accessible iCal):
  - Portland Insight Meditation Community (PIMC) — Wix site, no iCal
  - Portland Shambhala — dynamic FullCalendar, no static feed
"""

import logging

from data.schemas.event import Center, Tradition

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "dharma_rain": Center(
        id="dharma_rain",
        name="Dharma Rain Zen Center",
        url="https://dharma-rain.org",
        address="8500 NE Siskiyou St",
        city="Portland",
        state="OR",
        zip_code="97220",
        lat=45.5508,
        lng=-122.5946,
        neighborhood="Roseway / Northeast Portland",
        tradition=Tradition.ZEN,
        notes=(
            "Dharma Rain Zen Center is the oldest and largest Soto Zen temple in Oregon, founded "
            "in 1975. The center has two buildings (Sodo and Uji) and offers a full monastic and "
            "lay practice schedule. Regular public programs: Wednesday Evening Meditation 7–9pm "
            "(zazen, chanting, open Buddhism class; free, donations welcome), Sunday Morning "
            "Program 8:30–11:30am (two zazen periods, chanting service, Dharma talk). Early "
            "morning zazen Wed–Sat 6:30–7:30am. Sesshin, zazenkai, and dokusan offered. "
            "Drop-in welcome; no registration required for public sits."
        ),
    ),
    "kagyu_changchub_chuling": Center(
        id="kagyu_changchub_chuling",
        name="Kagyu Changchub Chuling",
        url="https://kcc.org",
        address="4936 NE Skidmore St",
        city="Portland",
        state="OR",
        zip_code="97218",
        lat=45.5579,
        lng=-122.6134,
        neighborhood="Beaumont-Wilshire / Northeast Portland",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kagyu Changchub Chuling (KCC) is a Karma Kagyu Tibetan Buddhist center in Northeast "
            "Portland, led by Lama Eric Yankovitch. One of the oldest Tibetan Buddhist centers in "
            "the Pacific Northwest. Regular public programs include Sunday Shamatha (9–11am in-person "
            "and 6:30–8pm hybrid), Wednesday Chenrezi Practice 7–8pm (hybrid), Thursday Silent Sit "
            "11am–12pm (in-person), and Daily Morning Meditation 7–7:45am online. "
            "Tibetan language and Dharma study classes offered. Drop-in welcome."
        ),
    ),
    "portland_insight": Center(
        id="portland_insight",
        name="Portland Insight Meditation Community",
        url="https://www.portlandinsight.org",
        address="6536 SE Duke St",
        city="Portland",
        state="OR",
        zip_code="97206",
        lat=45.4738,
        lng=-122.6186,
        neighborhood="Brentwood-Darlington / Southeast Portland",
        tradition=Tradition.THERAVADA,
        notes=(
            "Portland Insight Meditation Community (PIMC) teaches in the Theravada Vipassana "
            "tradition (Ruth Denison lineage). Weekly programs include Sunday morning meditation "
            "and Dharma talk (in-person + Zoom), Monday morning sit with poem and group discussion, "
            "Tuesday Evening Sangha 6:30–8pm (in-person), and Wednesday evening Heart of Freedom "
            "class (guided meditation, wisdom teachings, Q&A). Open to all levels; drop-in welcome. "
            "Located in Brentwood-Darlington, Southeast Portland."
        ),
    ),
    "shambhala_portland": Center(
        id="shambhala_portland",
        name="Portland Shambhala Meditation Center",
        url="https://portland.shambhala.org",
        address="1404 SE 25th Ave",
        city="Portland",
        state="OR",
        zip_code="97214",
        lat=45.5168,
        lng=-122.6434,
        neighborhood="Buckman / Richmond, Southeast Portland",
        tradition=Tradition.TIBETAN,
        notes=(
            "Portland Shambhala Meditation Center offers meditation in the Shambhala Buddhist "
            "tradition (Chögyam Trungpa lineage) from their Southeast Portland location near "
            "Hawthorne. Regular in-person programs: Monday and Friday evening 'Decompress + "
            "Connect' meditation at 1404 SE 25th Ave. Online programs include Monday morning "
            "meditation, Tuesday evening open house, Friday morning meditation, and Sunday "
            "community meditation. Monthly Laurelhurst Park sit (3rd Sunday 10–11:30am). "
            "Free introductory meditation instruction available."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Phase 3 Portland — iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "dharma_rain": {
        # WordPress The Events Calendar — confirmed working 2026-05-07
        "url": "https://dharma-rain.org/events/?ical=1",
        "filter_to_sits": True,
    },
    "kagyu_changchub_chuling": {
        # WordPress The Events Calendar — confirmed working 2026-05-07
        # Uses /calendar/month/ path instead of /events/
        "url": "https://kcc.org/calendar/month/?ical=1",
        "filter_to_sits": True,
    },
}
