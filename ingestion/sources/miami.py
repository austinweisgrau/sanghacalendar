"""
Miami / South Florida meditation center sources — Phase 3 expansion.

Covers Coral Gables/Miami (KMC Miami) and Fort Lauderdale (KMC Fort Lauderdale).

iCal feeds:
  - KMC Fort Lauderdale — 2 public Google Calendar feeds:
    - GP Classes (41d28hqqp6v7lmfohaicb9ah20): weekly sits (Sun/Wed/Thu)
    - Free Activities (da0mpko7l6cr8a2jvus265mb18): pujas, Tsog, monthly events

Recurring sits (no accessible iCal):
  - KMC Miami (Coral Gables) — Wix-based site, no iCal; schedule seeded.
    Sun 11am, Mon 7:30pm, Tue 7:30pm (Spanish), Thu 7:30pm, Fri 12:15pm.
    316 Miracle Mile, Coral Gables, FL 33134.

Research notes (2026-05-10):
  - Miami Shambhala: no active center found (miami.shambhala.org redirects to main site).
  - Insight Miami (insightmiami.org): small private sangha, email-based locations — skip.
  - Southern Palm Zen (Boca Raton, floridazen.com): ~45 miles from Miami; deferred.
  - KMC Florida (Sarasota): 65 miles from Miami; different metro — skip.
  - No Vipassana centers with public calendars found in Miami metro.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_miami": Center(
        id="kmc_miami",
        name="Kadampa Meditation Center Miami",
        url="https://meditationinmiami.org",
        address="316 Miracle Mile",
        city="Coral Gables",
        state="FL",
        zip_code="33134",
        lat=25.7474,
        lng=-80.2575,
        neighborhood="Coral Gables / Downtown Miami",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Miami (KMC Miami) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located on Miracle Mile in Coral Gables, FL. "
            "Offers regular General Program meditation classes open to all — no experience needed. "
            "Weekly sits: Sunday 11am, Monday 7:30pm, Tuesday 7:30pm (Meditación en español), "
            "Thursday 7:30pm, and a Friday lunchtime sit. Branch of KMC Florida (Sarasota). "
            "Special programs, empowerments, and Tsog days offered monthly. "
            "Free to attend; donations welcome."
        ),
    ),
    "kmc_fort_lauderdale": Center(
        id="kmc_fort_lauderdale",
        name="Kadampa Meditation Center Fort Lauderdale",
        url="https://meditateinfortlauderdale.org",
        address="4342 E Tradewinds Ave",
        city="Lauderdale-by-the-Sea",
        state="FL",
        zip_code="33308",
        lat=26.1904,
        lng=-80.0978,
        neighborhood="Fort Lauderdale / Lauderdale-by-the-Sea",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Fort Lauderdale is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located in Lauderdale-by-the-Sea, FL "
            "(Broward County, approx. 30 miles north of Miami). Offers weekly General Program "
            "meditation classes on Sundays (11am, 90 min) and Thursdays (7pm), plus a Wednesday "
            "lunchtime sit and satellite groups in Delray Beach (2nd Wed) and Hollywood (1st Fri). "
            "Special events, empowerments, and Tsog pujas held monthly. Free to attend; "
            "donations welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

# KMC Fort Lauderdale uses public Google Calendar feeds.
# GP Classes = regular weekly sits; Free Activities = pujas, tsog, monthly events.
ICAL_FEEDS = {
    "kmc_fort_lauderdale_gp": {
        "url": "https://calendar.google.com/calendar/ical/41d28hqqp6v7lmfohaicb9ah20%40group.calendar.google.com/public/basic.ics",
        "center_id": "kmc_fort_lauderdale",
        "filter_to_sits": True,
    },
    "kmc_fort_lauderdale_free": {
        "url": "https://calendar.google.com/calendar/ical/da0mpko7l6cr8a2jvus265mb18%40group.calendar.google.com/public/basic.ics",
        "center_id": "kmc_fort_lauderdale",
        "filter_to_sits": True,
    },
}
