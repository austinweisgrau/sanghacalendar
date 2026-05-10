"""
Houston, TX meditation center sources — Phase 3 expansion.

iCal feeds:
  - Chung Tai Zen Center of Houston (cthouston.org/events/?ical=1) — Chan (Taiwanese)
  - Dawn Mountain Center for Tibetan Buddhism (Google Calendar public ICS)

Squarespace JSON:
  - Houston Zen Center (houstonzen.org/events-calendar?format=json) — Soto Zen

Recurring sits (no accessible iCal):
  - Insight Meditation Houston — Monday 7pm at 4949 Caroline St (Theravada/Vipassana)
  - Diamond Way Buddhist Center Houston — Wednesday 7:30pm at 5102 Center St (Tibetan)
  - Houston Zen Center — daily zazen seeded as recurring sits
  - Drepung Loseling Institute of Texas — Thu 7-9am + Sun 10am-noon + Sun 3-7pm (Gelugpa Tibetan)
"""

import logging

from data.schemas.event import Center, Tradition

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "houston_zen": Center(
        id="houston_zen",
        name="Houston Zen Center",
        url="https://houstonzen.org",
        address="1605 Heights Blvd",
        city="Houston",
        state="TX",
        zip_code="77008",
        lat=29.8004,
        lng=-95.3984,
        neighborhood="The Heights",
        tradition=Tradition.ZEN,
        notes=(
            "Houston Zen Center (HZC) is a Soto Zen community in The Heights neighborhood, "
            "offering one of the most active daily practice schedules in Texas. Morning zazen "
            "(Mon–Thu 5:50am and 6:40am, Sat 8:20am) and evening zazen (Mon–Thu 5:30pm) are "
            "open to all via Zoom and in-person. The full Sunday program (8:20am–noon) includes "
            "chanting, zazen, dharma talks, and newcomer orientation. Weekly dharma talks by the "
            "Abbot Gaelyn Godwin and visiting teachers. Free; donations welcome. Drop-in always "
            "welcome."
        ),
    ),
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
    "drepung_loseling_texas": Center(
        id="drepung_loseling_texas",
        name="Drepung Loseling Institute of Texas",
        url="https://www.drepungloselinginstitute.org",
        address="11510 S Garden St",
        city="Houston",
        state="TX",
        zip_code="77071",
        lat=29.6620,
        lng=-95.4908,
        neighborhood="Westbury / Southwest Houston",
        tradition=Tradition.TIBETAN,
        notes=(
            "Drepung Loseling Institute of Texas is a Tibetan Buddhist temple and meditation "
            "center in the Westbury area of southwest Houston, affiliated with Drepung Loseling "
            "Monastery in India under the patronage of His Holiness the 14th Dalai Lama "
            "(Gelugpa lineage). Offers weekly Thursday morning practice (7–9am) and Sunday "
            "programs: morning session (10am–noon) and afternoon program (3–7pm) that includes "
            "meditation, teachings, and Tibetan Buddhist ritual practice. All are welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Phase 3 Houston — iCal feeds
# ---------------------------------------------------------------------------

SQUARESPACE_FEEDS = {
    "houston_zen": {
        # Squarespace events JSON API — confirmed working 2026-05-09
        # Returns dharma talks, classes, retreats, ceremonies (~10 events per page)
        "url": "https://houstonzen.org/events-calendar",
        "filter_to_sits": False,  # include dharma talks and classes too
    },
}

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
