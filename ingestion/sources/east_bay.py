"""
East Bay meditation center sources — Phase 1 prototype.
Defines all known centers and their ingestion strategies.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Phase 1 — Direct iCal subscribe
# ---------------------------------------------------------------------------

CENTERS = {
    "imc_berkeley": Center(
        id="imc_berkeley",
        name="Insight Meditation Center",
        url="https://www.insightmeditationcenter.org",
        address="1205 Hopkins St",
        city="Berkeley",
        state="CA",
        zip_code="94702",
        lat=37.8789,
        lng=-122.2865,
        neighborhood="West Berkeley",
        tradition=Tradition.THERAVADA,
    ),
    "ebmc": Center(
        id="ebmc",
        name="East Bay Meditation Center",
        url="https://eastbaymeditation.org",
        address="285 17th St",
        city="Oakland",
        state="CA",
        zip_code="94612",
        lat=37.8076,
        lng=-122.2697,
        neighborhood="Uptown Oakland",
        tradition=Tradition.PLURALIST,
        notes="Focus on diversity, equity, and inclusion. Many identity-specific sanghas.",
    ),
    "shambhala_berkeley": Center(
        id="shambhala_berkeley",
        name="Berkeley Shambhala Center",
        url="https://berkeley.shambhala.org",
        address="2288 Fulton St",
        city="Berkeley",
        state="CA",
        zip_code="94704",
        lat=37.8696,
        lng=-122.2677,
        neighborhood="South Campus Berkeley",
        tradition=Tradition.TIBETAN,
    ),

    # Phase 2 — Eventbrite / light scrape
    "nyingma_institute": Center(
        id="nyingma_institute",
        name="Nyingma Institute",
        url="https://www.nyingmainstitute.com",
        address="1815 Highland Pl",
        city="Berkeley",
        state="CA",
        zip_code="94709",
        lat=37.8781,
        lng=-122.2607,
        neighborhood="North Berkeley",
        tradition=Tradition.TIBETAN,
        notes="Tibetan Buddhist institute. Daily Kum Nye, Women's Meditation Group, Sunday Dharma Talks. Events on Eventbrite (organizer_id: 336367203).",
    ),
    "empty_gate_zen": Center(
        id="empty_gate_zen",
        name="Empty Gate Zen Center",
        url="https://emptygatezen.com",
        address="2200 Parker St",
        city="Berkeley",
        state="CA",
        zip_code="94704",
        lat=37.8634,
        lng=-122.2597,
        neighborhood="South Berkeley",
        tradition=Tradition.ZEN,
        notes="Korean Zen (Kwan Um lineage). Dense daily schedule of zazen + chanting.",
    ),
    "insight_berkeley": Center(
        id="insight_berkeley",
        name="Insight Meditation Community of Berkeley",
        url="https://www.insightberkeley.org",
        address="2304 McKinley Ave",  # meets at Berkeley Buddhist Monastery
        city="Berkeley",
        state="CA",
        zip_code="94703",
        lat=37.8758,
        lng=-122.2637,
        neighborhood="North Berkeley",
        tradition=Tradition.THERAVADA,
        notes="Theravada/Vipassana community. Weekly Thursday sits at Berkeley Buddhist Monastery (hybrid). Events on insightberkeley.org/events (static HTML) + Eventbrite (organizer_id: 32673197525) for day-long retreats.",
    ),
    "metta_dharma": Center(
        id="metta_dharma",
        name="Metta Dharma Foundation",
        url="https://www.mettadharma.org",
        address="2837 Claremont Blvd",
        city="Berkeley",
        state="CA",
        zip_code="94705",
        lat=37.8579,
        lng=-122.2432,
        neighborhood="Claremont",
        tradition=Tradition.THERAVADA,
        notes="Wednesday evening sits with Richard Shankman.",
    ),
    "oakland_zen": Center(
        id="oakland_zen",
        name="Oakland Zen Center / Kojin-an",
        url="https://oaklandzencenter.org",
        address="6140 Chabot Rd",
        city="Oakland",
        state="CA",
        zip_code="94618",
        lat=37.8397,
        lng=-122.2278,
        neighborhood="Rockridge",
        tradition=Tradition.ZEN,
        notes="Small family-run Soto Zen zendo.",
    ),
    "bay_zen": Center(
        id="bay_zen",
        name="Bay Zen Center",
        url="https://bayzen.org",
        address="3824 Grand Ave",
        city="Oakland",
        state="CA",
        zip_code="94610",
        lat=37.8145,
        lng=-122.2286,
        neighborhood="Grand Lake",
        tradition=Tradition.ZEN,
        notes="Ordinary Mind Zen School lineage. Weekly zazen: Mon 7am Zoom, Wed 6:30pm hybrid, Sat 8:30am hybrid. Special events on Squarespace calendar.",
    ),
    "berkeley_priory": Center(
        id="berkeley_priory",
        name="Berkeley Buddhist Priory",
        url="https://berkeleybuddhistpriory.org",
        address="1358 Marin Ave",
        city="Berkeley",
        state="CA",
        zip_code="94707",
        lat=37.8896,
        lng=-122.2714,
        neighborhood="North Berkeley",
        tradition=Tradition.ZEN,
        notes="Order of Buddhist Contemplatives (Soto Zen). Daily schedule of sits + services Tue–Sun. Monthly meditation retreats and special ceremonies. Events on WordPress calendar.",
    ),
    "spirit_rock": Center(
        id="spirit_rock",
        name="Spirit Rock Meditation Center",
        url="https://www.spiritrock.org",
        address="5000 Sir Francis Drake Blvd",
        city="Woodacre",
        state="CA",
        zip_code="94973",
        lat=37.9878,
        lng=-122.6318,
        neighborhood="West Marin",
        tradition=Tradition.THERAVADA,
        notes="Weekly drop-in meditation groups. Slightly outside East Bay.",
    ),
    "everyday_zen": Center(
        id="everyday_zen",
        name="Everyday Zen Foundation",
        url="https://everydayzen.org",
        address="145 Rock Hill Rd",
        city="Tiburon",
        state="CA",
        zip_code="94920",
        lat=37.8816,
        lng=-122.4577,
        neighborhood="Tiburon / Marin",
        tradition=Tradition.ZEN,
        notes="Soto Zen lineage (Norman Fischer). Weekly Metta Sittings, sutra recitation, all-day sittings. Meets at Community Congregational Church in Tiburon; many events hybrid or online.",
    ),
}


# Eventbrite organizer configs for Phase 2 scrapers
EVENTBRITE_FEEDS = {
    "nyingma_institute": {
        "organizer_id": "336367203",
        "filter_to_sits": False,  # Include all events (Dharma talks, classes, sittings)
    },
    "insight_berkeley": {
        "organizer_id": "32673197525",
        "filter_to_sits": True,  # Primarily day-long retreats — filter to actual sits
    },
}


# Static HTML calendar configs for Phase 2 LLM-assisted scrapers
STATIC_HTML_FEEDS = {
    "bay_zen": {
        "url": "https://bayzen.org/calendar",
        "filter_to_sits": False,  # Include sesshin and zazenkai (extended sitting retreats)
    },
    "berkeley_priory": {
        "url": "https://berkeleybuddhistpriory.org/calendar/",
        "filter_to_sits": False,  # Include meditation retreats and ceremonies
    },
    "insight_berkeley": {
        "url": "https://www.insightberkeley.org/events",
        "filter_to_sits": False,  # Include weekly sits + special class series
    },
}


# Feed configurations for Phase 1 direct-subscribe centers
ICAL_FEEDS = {
    "imc_berkeley": {
        "url": "https://calendar.google.com/calendar/ical/f2671ba813e15027485f84235a37074c4d3a113cc0135f83f46212744f55dc09%40group.calendar.google.com/public/basic.ics",
        "filter_to_sits": True,
    },
    "ebmc": {
        "url": "https://eastbaymeditation.org/?ical=1&eventDisplay=list",
        "filter_to_sits": True,
    },
    # shambhala_berkeley: removed — shambhala-koeln.de feed consistently times out.
    # Berkeley Shambhala events are covered by manual recurring sits already in the DB.
    "everyday_zen": {
        "url": "https://everydayzen.org/?ical=1",
        "filter_to_sits": True,
    },
}
