"""
Houston, TX meditation center sources — Phase 3 expansion.

iCal feeds:
  - Chung Tai Zen Center of Houston (cthouston.org/events/?ical=1) — Chan (Taiwanese)
  - Dawn Mountain Center for Tibetan Buddhism (Google Calendar public ICS)

Recurring sits (no accessible iCal):
  - Insight Meditation Houston — Monday 7pm at 4949 Caroline St (Theravada/Vipassana)
  - Diamond Way Buddhist Center Houston — Wednesday 7:30pm at 5102 Center St (Tibetan)
"""

import logging

from data.schemas.event import Center, Tradition

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "chung_tai_houston": Center(
        id="chung_tai_houston",
        name="Chung Tai Zen Center of Houston",
        url="https://cthouston.org",
        address="12129 Bellaire Blvd",
        city="Houston",
        state="TX",
        zip_code="77072",
        lat=29.7122,
        lng=-95.5832,
        neighborhood="Westchase / Bellaire",
        tradition=Tradition.ZEN,
        notes=(
            "Chung Tai Zen Center of Houston (普德精舍) is a Chan (Zen) Buddhist center "
            "affiliated with Chung Tai Chan Monastery in Taiwan. Located in the Bellaire/Westchase "
            "area of southwest Houston. Offers structured meditation programs at multiple skill "
            "levels: Level 1 (Beginner) on Monday evenings 7:30pm and Saturday mornings 10am; "
            "Level 2 (Intermediate) and Level 3 (Advanced) on Wednesday evenings 7:30pm; "
            "Sutra Study on Thursday evenings 7pm; Youth and Children's Meditation on Saturday "
            "afternoons 4:30pm. Monthly half-day retreats. All are welcome; no experience needed."
        ),
    ),
    "dawn_mountain_houston": Center(
        id="dawn_mountain_houston",
        name="Dawn Mountain Center for Tibetan Buddhism",
        url="https://dawnmountain.org",
        address="4803 San Felipe St",
        city="Houston",
        state="TX",
        zip_code="77056",
        lat=29.7562,
        lng=-95.4643,
        neighborhood="Galleria / Uptown",
        tradition=Tradition.TIBETAN,
        notes=(
            "Dawn Mountain Center for Tibetan Buddhism is an ecumenical Tibetan Buddhist center "
            "in Houston's Galleria area, founded in 1996 by Anne C. Klein (Rigzin Drolma) and "
            "Harvey B. Aronson. One of the few Tibetan Buddhist centers in the US that actively "
            "bridges academic Buddhist studies and contemplative practice. Offers free Sunday "
            "guided meditations, Teaching Tuesdays, weekend retreats, and an in-depth study "
            "program in Tibetan texts and practice. The New Day curriculum offers structured "
            "training in Dzogchen, Ngondro, and related practices. Open to all levels."
        ),
    ),
    "insight_meditation_houston": Center(
        id="insight_meditation_houston",
        name="Insight Meditation Houston",
        url="https://insighthouston.org",
        address="4949 Caroline St",
        city="Houston",
        state="TX",
        zip_code="77004",
        lat=29.7268,
        lng=-95.3836,
        neighborhood="Museum District / Midtown",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Houston (IMH) teaches in the Theravada Vipassana / Insight "
            "Meditation tradition (Spirit Rock / IMS lineage). Weekly Monday evening sits "
            "(7–8:30pm) with meditation and dharma talk at Covenant Church, Building B "
            "(Huff Fellowship Hall), 4949 Caroline St, Museum District. Also available via "
            "Zoom. Free; donations welcome. Annual 2-day 'Deepening the Dharma' retreat. "
            "Sits are held most Mondays except federal holidays."
        ),
    ),
    "diamond_way_houston": Center(
        id="diamond_way_houston",
        name="Diamond Way Buddhist Center Houston",
        url="https://diamondway.org/houston/",
        address="5102 Center St",
        city="Houston",
        state="TX",
        zip_code="77007",
        lat=29.7653,
        lng=-95.3987,
        neighborhood="Heights / Washington Corridor",
        tradition=Tradition.TIBETAN,
        notes=(
            "Diamond Way Buddhist Center Houston is part of the worldwide Diamond Way Buddhist "
            "network (Karma Kagyu lineage, Lama Ole Nydahl). Weekly Wednesday evening program "
            "at 7:30pm — a short Buddhist teaching followed by guided Guru Yoga meditation "
            "(~30 minutes). Free; donations welcome. Located near the Heights/Washington "
            "Corridor area. All are welcome, no experience needed."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Phase 3 Houston — iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "chung_tai_houston": {
        # WordPress The Events Calendar (ECPv6) — confirmed working 2026-05-09
        "url": "https://cthouston.org/events/?ical=1",
        "filter_to_sits": True,
    },
    "dawn_mountain_houston": {
        # Google Calendar public ICS — confirmed working 2026-05-09
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "dawnmountain.org_98i9a9njars99imv86omhfmebs%40group.calendar.google.com"
            "/public/basic.ics"
        ),
        "filter_to_sits": True,
    },
}
