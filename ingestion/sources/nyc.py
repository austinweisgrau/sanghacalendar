"""
NYC meditation center sources — Phase 3a.
Defines all known NYC centers and their ingestion strategies.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Phase 3a — Direct iCal subscribe (easy wins)
# ---------------------------------------------------------------------------

CENTERS = {
    "nyimc": Center(
        id="nyimc",
        name="New York Insight Meditation Center",
        url="https://www.nyimc.org",
        address="115 West 29th Street, 12th Floor",
        city="Manhattan",
        state="NY",
        zip_code="10001",
        lat=40.7473,
        lng=-73.9932,
        neighborhood="Midtown South",
        tradition=Tradition.THERAVADA,
        notes="Theravada / Secular Vipassana. Weekly Community Sit (Thursdays, co-presented with Rubin Museum), Wednesday Community Meditation Gathering, monthly Sitting on Sunday. MBSR courses and retreats.",
    ),
    "brooklyn_zen_center": Center(
        id="brooklyn_zen_center",
        name="Brooklyn Zen Center",
        url="https://brooklynzen.org",
        address="326 Clinton St",
        city="Brooklyn",
        state="NY",
        zip_code="11231",
        lat=40.6820,
        lng=-73.9984,
        neighborhood="Carroll Gardens",
        tradition=Tradition.ZEN,
        notes="Soto Zen, socially-engaged and progressive. Daily online morning meditation Mon–Fri 7:30am ET; Wednesday Dharma Share 7pm (in-person); Saturday Morning Program 9am–12:40pm (most Saturdays, in-person). Monthly zazenkai one-day sits.",
    ),
    "kadampa_nyc": Center(
        id="kadampa_nyc",
        name="Kadampa Meditation Center New York",
        url="https://meditationinnewyork.org",
        address="127 W 24th St",
        city="Manhattan",
        state="NY",
        zip_code="10011",
        lat=40.7455,
        lng=-73.9960,
        neighborhood="Chelsea",
        tradition=Tradition.TIBETAN,
        notes="New Kadampa Tradition (NKT-IKBU) Tibetan Buddhist center. 30+ drop-in classes per week. Mon/Wed evenings 7pm; Tue lunchtime 11:15am; Tue/Fri evenings 5:30pm; Sun 11am.",
    ),
}


# Feed configurations for Phase 3a direct-subscribe centers
ICAL_FEEDS = {
    "nyimc": {
        # WordPress + The Events Calendar Pro
        # Returns 403 without browser User-Agent — ical_feed.py already sets headers
        "url": "https://www.nyimc.org/events/?ical=1",
        "filter_to_sits": True,
    },
    "brooklyn_zen_center": {
        # WordPress + Event Organiser plugin
        # PRODID:-//Brooklyn Zen Center//NONSGML Events//EN
        "url": "https://brooklynzen.org/?ical=1",
        "filter_to_sits": True,
    },
    "kadampa_nyc": {
        # WordPress + The Events Calendar (meditationinnewyork.org — NYC branch site)
        # filter_to_sits=False to include classes and programs (not just sits)
        "url": "https://meditationinnewyork.org/events/?ical=1",
        "filter_to_sits": False,
    },
}
