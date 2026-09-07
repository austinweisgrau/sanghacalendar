"""
Fort Wayne, IN — Phase 3 expansion.

Indiana's second-largest city (~280k) has a modest but genuine Buddhist
community, anchored by a Theravada/Insight lay sangha and a Sri Lankan
Theravada vihara in the nearby Hoagland township.

Centers included:
  - Insight Meditation Fort Wayne (imfw) — Theravada/Vipassana (lay)
    2332 Sandpoint Road, Fort Wayne IN 46809. imfw.org
    Tue 6pm hybrid (30 min guided + dharma talk), Sun 10am in-person
    No iCal (Squarespace site, static calendar pages); recurring sits seeded.

  - Indiana Buddhist Temple / Indiana Buddhist Vihara (indiana_buddhist_vihara)
    — Theravada (Sri Lankan)
    7528 Thompson Road, Hoagland IN 46745. indianabuddhistvihara.org
    Mon 6:30pm (Metta meditation), Thu 6:30pm (Anapanasati), Sat 2pm (sutta study)
    No iCal (static HTML events page); recurring sits seeded.
    ~15 miles SE of downtown Fort Wayne; functionally Fort Wayne metro.

Research notes (2026-09-07):
  - IMFW: Active lay sangha affiliated with Mid America Dharma. April 2026
    newsletter confirmed. Sangha House at 2332 Sandpoint Rd. Tue hybrid
    (in-person + Zoom), Sun in-person only. Squarespace site with static
    calendar at imfw.org/calendar.
  - Indiana Buddhist Vihara: Sri Lankan Theravada, founded 2003, Abbot Bhante
    Devananda. English-language, open to all. Events page (events.html) may
    be intermittently down; Facebook and Yelp active May 2026. Also livestreams
    on Facebook and YouTube.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "imfw": Center(
        id="imfw",
        name="Insight Meditation Fort Wayne",
        url="https://www.imfw.org",
        address="2332 Sandpoint Road",
        city="Fort Wayne",
        state="IN",
        zip_code="46809",
        lat=41.0485,
        lng=-85.2167,
        neighborhood="Southwest Fort Wayne",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Fort Wayne (IMFW) is a lay Theravada / Vipassana "
            "sangha affiliated with Mid America Dharma, meeting at its Sangha House "
            "on Sandpoint Road. Tuesday Evening Sits (6:00–7:00 PM) feature 30 "
            "minutes of guided meditation followed by a dharma talk — hybrid "
            "in-person and Zoom. Sunday Morning Sits (10:00 AM) are 40 minutes of "
            "silent sitting with optional walking meditation, in-person only. Second "
            "Tuesday of each month includes a Refuge Ceremony. Periodic multi-week "
            "Intro to Insight Meditation series. Free and open to all; no experience "
            "required. Contact: InsightMeditationFW@gmail.com. imfw.org."
        ),
    ),
    "indiana_buddhist_vihara": Center(
        id="indiana_buddhist_vihara",
        name="Indiana Buddhist Temple",
        url="https://www.indianabuddhistvihara.org",
        address="7528 Thompson Road",
        city="Hoagland",
        state="IN",
        zip_code="46745",
        lat=40.9892,
        lng=-84.9969,
        neighborhood="Hoagland (Fort Wayne metro)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Indiana Buddhist Temple (Indiana Buddhist Vihara) is a Sri Lankan "
            "Theravada community in Hoagland, about 15 miles southeast of downtown "
            "Fort Wayne. Founded June 2003, led by Abbot Venerable Thalangama "
            "Devananda (Bhante Devananda). Three weekly English-language programs "
            "open to all: Monday Loving-Kindness Meditation (Metta Bhavana, 6:30 PM), "
            "Thursday Mindfulness of Breathing (Anapanasati Bhavana, 6:30 PM), and "
            "Saturday Sutta Discussion & Meditation (2:00 PM, studying the Majjhima "
            "Nikaya). Services also livestreamed on Facebook and YouTube. Monthly "
            "retreats offered. Free. Phone: 260-447-5269. indianabuddhistvihara.org."
        ),
    ),
}

# No live iCal feeds available — all sits seeded as recurring in
# scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
