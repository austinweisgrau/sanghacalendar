"""
St. Louis, MO meditation center sources — Phase 3 expansion.

St. Louis has a modest but established Buddhist scene spanning several traditions,
centered in the neighborhoods of Maplewood, Brentwood, and the Central West End.

iCal feeds:
  - Confluence Zen Center STL (Soto Zen): WordPress All-in-One Event Calendar plugin
    at 3544 Oxford Ave, Maplewood, MO. Recurring zazen + sesshin + special events.

Recurring sits (seeded in sangha-seed-recurring.js):
  - Sunday Sangha STL (Insight Meditation) — Sun 11am hybrid, Brentwood MO.
  - Center for Pragmatic Buddhism STL — Thu 7pm in-person, First Unitarian Church.

Research notes (2026-05-14):
  - Confluence Zen Center STL (confluencezen.org): Soto Zen lay community in Maplewood.
    Founded and led by Daigaku Rumme, SZBA-authorized teacher. Address: 3544 Oxford Ave
    (also shown as 7112 St. James Square in older events — same building, corner address).
    Regular schedule: Morning Zazen Mon/Tue/Thu 6:20–7:15am, Evening Zazen Mon 7–8pm,
    Beginner's Night 1st Tue monthly 6:30pm, Sunday Zazen 2nd/3rd/4th/5th Sundays 9am.
    Active WordPress All-in-One Event Calendar (ai1ec) iCal feed with RRULE support.
  - Sunday Sangha St. Louis (sundaysangha-stl.org): Theravada/Insight Meditation community
    in Brentwood MO. Meets every Sunday 11am–12:30pm hybrid (in-person + Zoom). Specific
    venue address not published publicly (shared on email list signup). Multi-teacher.
    Free, donation-based.
  - Center for Pragmatic Buddhism — St. Louis (pragmaticbuddhism.org/stlouis): Eclectic
    Chan/Zen/Pragmatist synthesis. Weekly practice Thu 7–8:30pm Central at First Unitarian
    Church of St. Louis (5007 Waterman Blvd at Kingshighway, St. Louis MO 63108). Enter
    through north/back garden door. Free, open to all.
  - Missouri Zen Center (missourizencenter.org): 220 Spring Ave, Webster Groves MO 63119.
    Soto Zen. Site has 500 errors on iCal endpoint. Schedule not readily confirmed online.
    Deferred — monitor for accessible calendar.
  - Mid-America Buddhist Association (maba-usa.org): Chinese Chan. Open Fri/Sat/Sun.
    Devotional focus; schedule not clearly accessible. Deferred.
  - St. Louis Shambhala: stlouis.shambhala.org redirects to main shambhala.org — likely
    closed or no independent center. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "confluence_zen_stl": Center(
        id="confluence_zen_stl",
        name="Confluence Zen Center STL",
        url="https://www.confluencezen.org",
        address="3544 Oxford Avenue",
        city="Maplewood",
        state="MO",
        zip_code="63143",
        lat=38.5981,
        lng=-90.3287,
        neighborhood="Maplewood (St. Louis suburb)",
        tradition=Tradition.ZEN,
        notes=(
            "Confluence Zen Center STL is a Soto Zen lay community in Maplewood, "
            "MO, led by Daigaku Rumme (SZBA-authorized teacher). Regular schedule: "
            "Morning Zazen Mon/Tue/Thu 6:20–7:15am in-person; Evening Zazen Mon "
            "7–8pm in-person; Sunday Zazen 9–11am (2nd, 3rd, 4th, and 5th Sundays); "
            "Beginner's Night 1st Tuesday monthly 6:30pm (introduction to Zen "
            "practice and zendo protocol). Periodic sesshins, one-day sittings, "
            "and dharma study groups. Drop-in welcome for zazen; beginners encouraged "
            "to attend Beginner's Night first. Free, dana-based."
        ),
    ),
    "sunday_sangha_stl": Center(
        id="sunday_sangha_stl",
        name="Sunday Sangha St. Louis",
        url="https://sundaysangha-stl.org",
        address="",
        city="Brentwood",
        state="MO",
        zip_code="63144",
        lat=38.6107,
        lng=-90.3494,
        neighborhood="Brentwood (St. Louis suburb)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Sunday Sangha St. Louis is a Theravada/Insight Meditation community "
            "meeting every Sunday 11am–12:30pm in Brentwood, MO. Hybrid format: "
            "in-person attendance plus Zoom. Sessions begin with ~40 minutes of "
            "silent meditation, followed by brief instruction in the Insight "
            "tradition (mindfulness of breath, sound, body, and mind), facilitator "
            "sharing, and open discussion. All spiritual backgrounds welcome. "
            "Free (donations cover $35/week space rental — cash only)."
        ),
    ),
    "center_pragmatic_buddhism_stl": Center(
        id="center_pragmatic_buddhism_stl",
        name="Center for Pragmatic Buddhism — St. Louis",
        url="https://www.pragmaticbuddhism.org/stlouis",
        address="5007 Waterman Boulevard",
        city="St. Louis",
        state="MO",
        zip_code="63108",
        lat=38.6428,
        lng=-90.2724,
        neighborhood="Central West End (at First Unitarian Church)",
        tradition=Tradition.ZEN,
        notes=(
            "The Center for Pragmatic Buddhism (CPB) St. Louis chapter holds weekly "
            "Thursday practice 7–8:30pm Central at First Unitarian Church of St. "
            "Louis (5007 Waterman Blvd at Kingshighway, St. Louis MO 63108). Enter "
            "through the north/back of the building — garden walkway to glass doors "
            "on the left. CPB synthesizes early Indian Buddhist teachings (Nikayan), "
            "Chinese Chan and Japanese Zen, and American Pragmatism. Practice "
            "combines zazen, dharma talks, and group discussion. Open to all, "
            "free. Also offers online weekday morning sits (6am ET) via the "
            "national CPB community."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "confluence_zen_stl_ical": {
        "url": (
            "https://www.confluencezen.org/"
            "?plugin=all-in-one-event-calendar"
            "&controller=ai1ec_exporter_controller"
            "&action=export_events"
            "&no_html=true"
        ),
        "center_id": "confluence_zen_stl",
        "filter_to_sits": True,
    },
}
