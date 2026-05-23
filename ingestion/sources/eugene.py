"""
Eugene, OR — Phase 3 expansion.

Eugene is Oregon's second-largest city (~180k, ~380k metro), home to the
University of Oregon. Its progressive culture and proximity to Portland's Zen
network supports a rich Buddhist community with strong Zen, Insight, and
Tibetan representation.

Centers included:
  - Buddha Eye Temple (buddha_eye_temple) — Soto Zen (Japanese)
    2190 Garfield St, Eugene OR 97405. buddhaeye.org
    Sunday public program 8:45am–~10:30am (intro + zazen + service).
    No iCal; seeded recurring Sunday program.

  - Blue Cliff Zen Center (blue_cliff_zen_eugene) — Western Zen (Soto/Rinzai)
    352 W 12th Ave, Eugene OR 97401 (Everyday People Yoga studio).
    bluecliffzen.org. Tue/Thu 7–8am in-person + online; Sun 4:30–6pm.
    No iCal; seeded.

  - Zen West Eugene (zen_west_eugene) — Soto Zen (Dharma Rain affiliate)
    1685 W 13th Ave, Eugene OR 97402 (UUCE). zenwesteugene.org
    Thursday 7–8:45pm. No iCal; seeded.

  - River Wisdom Insight Meditation (river_wisdom_insight) — Insight/Theravada
    UUCE (1st Sat) + Buddha Eye Temple (3rd Sat). riverwisdominsight.com
    1st Saturday 10:30am–12pm, 3rd Saturday 10:30–11:30am.
    No iCal; seeded.

Research notes (2026-05-23):
  - Buddha Eye Temple: oldest Soto Zen temple in Eugene area (2002). Full
    monastic schedule; Sunday morning program is the main public entry point.
    Intro to Meditation 8:45–9:50am, then Zazen 9am, Assembly 10am (~10:30 end).
  - Blue Cliff Zen: meets at yoga studio, teacher Matt Shinkai Kane. Mon/Wed/Fri
    7–7:30am are Zoom-only; Tue/Thu 7–8am and Sunday 4:30–6pm are hybrid.
  - Zen West Eugene: Dharma Rain satellite, led by Debra Seido Martin (transmitted
    Soto Zen lay teacher). Full program: zazen, kinhin, recitation, dharma talk.
  - River Wisdom Insight: led by Linda Rose (under Howie Cohn / Spirit Rock lineage).
    Wednesday Zoom-only sits not seeded (online only).
  - Mahasiddha Kadampa (144 E 14th Ave, NKT): schedule not publicly confirmed;
    meditationinoregon.org uses JS verification blocking. Skip until verifiable.
  - Open Sky Shambhala Eugene: shambhala.org redirect suggests dormant/reorganized.
  - Eugene Buddhist Priory (OBC Soto Zen, 85415 Teague Loop): rural location ~5 miles
    south of Eugene; early AM schedule; primary access by appointment. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "buddha_eye_temple": Center(
        id="buddha_eye_temple",
        name="Buddha Eye Temple",
        url="https://www.buddhaeye.org",
        address="2190 Garfield St",
        city="Eugene",
        state="OR",
        zip_code="97405",
        lat=44.0268,
        lng=-123.0978,
        neighborhood="South Eugene",
        tradition=Tradition.ZEN,
        notes=(
            "Buddha Eye Temple is a Soto Zen temple (registered Soto Zen School, Japanese "
            "denomination) in South Eugene, founded 2002. The Sunday morning program is the "
            "main public entry point: Introduction to Meditation 8:45–9:50am (open to all), "
            "then Zazen 9:00am, Assembly/ceremony 10:00am. Weekday zazen at 5:00am (Sep–Jun) "
            "or 5:30am (summer) followed by morning service. Thursday evening teisho on "
            "select dates 6:30–8:30pm. Sesshin several times per year. Teacher: Kogen Czarnik."
        ),
    ),
    "blue_cliff_zen_eugene": Center(
        id="blue_cliff_zen_eugene",
        name="Blue Cliff Zen Center",
        url="https://www.bluecliffzen.org",
        address="352 W 12th Ave",
        city="Eugene",
        state="OR",
        zip_code="97401",
        lat=44.0477,
        lng=-123.0888,
        neighborhood="West University / Downtown Eugene",
        tradition=Tradition.ZEN,
        notes=(
            "Blue Cliff Zen Center is a Western Zen community (Soto/Rinzai hybrid) meeting "
            "inside Everyday People Yoga studio in Eugene. Teacher: Matt Shinkai Kane. "
            "Public in-person programs: Tuesday and Thursday 7:00–8:00am (zazen + optional "
            "instruction; in-person + online hybrid), Sunday 4:30–6:00pm (zazen + dharma "
            "discussion; in-person + online). Monday/Wednesday/Friday 7:00–7:30am are "
            "Zoom-only. Intensive retreats offered periodically. Drop-in welcome; dana-based."
        ),
    ),
    "zen_west_eugene": Center(
        id="zen_west_eugene",
        name="Zen West Eugene",
        url="https://www.zenwesteugene.org",
        address="1685 W 13th Ave",
        city="Eugene",
        state="OR",
        zip_code="97402",
        lat=44.0456,
        lng=-123.1172,
        neighborhood="Jefferson Westside / West Eugene",
        tradition=Tradition.ZEN,
        notes=(
            "Zen West Eugene is a Soto Zen community affiliated with Dharma Rain Zen Center "
            "in Portland, led by Debra Seido Martin (transmitted Soto Zen lay teacher). "
            "Thursday evening program (7:00–8:45pm) at the Unitarian Universalist Church of "
            "Eugene (UUCE): 7:00pm zazen, 7:20pm kinhin (walking), 7:30pm zazen, 7:45pm "
            "chanting/recitation, 7:55pm dharma talk/discussion, 8:45pm close. Monthly "
            "zazenkai (all-day sitting). Sesshin 4x/year (Dec, Mar, Jun, Aug). Drop-in welcome."
        ),
    ),
    "river_wisdom_insight": Center(
        id="river_wisdom_insight",
        name="River Wisdom Insight Meditation Community",
        url="https://riverwisdominsight.com",
        address="1685 W 13th Ave",
        city="Eugene",
        state="OR",
        zip_code="97402",
        lat=44.0456,
        lng=-123.1172,
        neighborhood="Jefferson Westside / West Eugene",
        tradition=Tradition.THERAVADA,
        notes=(
            "River Wisdom Insight Meditation Community offers Insight Meditation in the "
            "Theravada tradition, led by Linda Rose (student of Howie Cohn / Spirit Rock "
            "lineage). 1st Saturday of month: 10:30am–12:00pm at UUCE (1685 W 13th Ave, "
            "Eugene) — sitting meditation, dharma talk, discussion. 3rd Saturday of month: "
            "10:30–11:30am at Buddha Eye Temple (2190 Garfield St, Eugene). Wednesday "
            "10:00–11:15am sits are Zoom-only. Annual retreats and immersions offered. "
            "Drop-in welcome; dana-based."
        ),
    ),
}

# No live iCal feeds available for Eugene centers — all seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
