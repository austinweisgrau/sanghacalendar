"""
New Orleans, LA — Phase 3 expansion.

New Orleans has a small but vibrant Buddhist community, shaped by the city's
syncretic spiritual culture. Two primary Zen centers anchor the scene.

Centers included:
  - New Orleans Zen Temple (American Zen Association) — Soto Zen, recurring sits
    8338 Oak Street, 2nd Floor, New Orleans LA 70118 (Riverbend / Carrollton)
  - Mid City Zen — Soto Zen (Suzuki Roshi / SFZC lineage), iCal + recurring sits
    3248 Castiglione St, New Orleans LA 70119 (Mid-City)

Research notes (2026-05-17):
  - New Orleans Zen Temple (neworleanszentemple.org): Founded 1983 by Robert
    Livingston Roshi; now led by Richard Collins. Lineage of Master Taisen
    Deshimaru / Association Zen Internationale. Moved to Oak Street in Jan 2023
    (formerly at 748 Camp Street for 30 years). Basic Squarespace site, no iCal
    or calendar plugin. Confirmed weekly schedule:
      Tue 7:00pm: zazen (in-person + Zoom)
      Thu 6:30am: zazen (in-person)
      Sun 10:00am: zazen (in-person)
    New practitioners must register via noztinfo@gmail.com for intro session.

  - Mid City Zen (midcityzen.org): Founded 2011; permanent location since 2014.
    Soto Zen in the Suzuki Roshi / San Francisco Zen Center lineage; peer-led.
    WordPress site with Google Calendar embed. Google Calendar ID extracted from
    iframe src (base64-encoded). Calendar contains special events (dharma talks,
    retreats, one-day sits, queer zen, sober zen, half-day sits). Regular
    weekday morning zazen and Sunday program seeded as recurring.
    Confirmed schedule:
      Mon, Wed, Fri 8:00am: Morning Zazen (in-person + Zoom)
      Sun 9:30am: Sunday Program — zazen, chanting, dharma talk (in-person + Zoom)
      2nd/4th Sun 8:45am: Beginner's Instruction
      1st Sun: half-day sit
    Google Calendar feed active and returning events (special events only).

  Skipped for now:
  - New Orleans Insight Meditation Group (NOIMG, noimg.org): Domain offline as
    of 2026-05-17. Meets at Aikido of New Orleans, 3124 Magazine St. Theravada
    tradition. Monitor for site recovery.
  - Sangha House NOLA (sanghahousenola.org): Newer center (2024), Tremé
    neighborhood. Multi-tradition, community-focused. Wix site, no iCal.
    Weekly schedule unclear online. Monitor for confirmed schedule.
  - Samten Choling (samtenchoeling.org): Tibetan (Gelugpa), Nelson St.
    Founded 2020. Calendar is dynamic/Wix — no extractable iCal. Monitor.
  - Mindfulness Community of Greater New Orleans (mcgno.org): Plum Village
    tradition. Announced dissolution of weekly practice group in late 2024.
    Skip for now; check for revival.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "nozt": Center(
        id="nozt",
        name="New Orleans Zen Temple",
        url="https://www.neworleanszentemple.org",
        address="8338 Oak Street, 2nd Floor",
        city="New Orleans",
        state="LA",
        zip_code="70118",
        lat=29.9370,
        lng=-90.1195,
        neighborhood="Riverbend / Carrollton",
        tradition=Tradition.ZEN,
        notes=(
            "New Orleans Zen Temple (American Zen Association) is the oldest Zen center "
            "in New Orleans, founded in 1983 by Robert Livingston Roshi in the lineage of "
            "Master Taisen Deshimaru and the Association Zen Internationale. The temple "
            "moved to its current Oak Street location in January 2023 (above Yes, Yoga). "
            "Weekly zazen: Tuesday evenings at 7pm, Thursday mornings at 6:30am, and "
            "Sunday mornings at 10am. New practitioners should contact noztinfo@gmail.com "
            "to register for an introductory session before attending. Some sessions "
            "also available via Zoom. Donation-based; all welcome."
        ),
    ),
    "mid_city_zen": Center(
        id="mid_city_zen",
        name="Mid City Zen",
        url="https://midcityzen.org",
        address="3248 Castiglione St",
        city="New Orleans",
        state="LA",
        zip_code="70119",
        lat=29.9634,
        lng=-90.0888,
        neighborhood="Mid-City",
        tradition=Tradition.ZEN,
        notes=(
            "Mid City Zen is a peer-led Soto Zen community in New Orleans's Mid-City "
            "neighborhood, founded in 2011 in the lineage of Shunryu Suzuki Roshi and "
            "the San Francisco Zen Center. The center has been at its Castiglione Street "
            "location since 2014. Regular practice: Monday, Wednesday, and Friday morning "
            "zazen at 8:00am (in-person and Zoom); Sunday Program at 9:30am including "
            "chanting, zazen, and dharma study (in-person and Zoom); Beginner's "
            "Instruction on 2nd and 4th Sundays at 8:45am; first-Sunday half-day sits. "
            "Special programs include Queer Zen (virtual), Sober Zen, and seasonal "
            "retreats. Drop-in welcome; dana (generosity) basis."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Phase 3 New Orleans — iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "mid_city_zen": {
        # Google Calendar public ICS — decoded from base64 iframe src on midcityzen.org
        # Contains special events: dharma talks, retreats, one-day sits, identity sits
        # Confirmed working 2026-05-17
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "c_7cdva7r4be3n2i2c3f4ivjqdqg%40group.calendar.google.com/public/basic.ics"
        ),
        "filter_to_sits": True,
    },
}
