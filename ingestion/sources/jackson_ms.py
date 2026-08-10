"""
Jackson, Mississippi — Phase 3 expansion (heartbeat 97).

Jackson (pop. ~150k city, ~590k metro) is the capital of Mississippi. The Buddhist
community is small but active, anchored at the Wolfe Fine Art Studio Dojo at 4308 Old
Canton Rd — home to both the Jackson Zen Group (Shorinji Zen Association) and the
Jackson Insight Meditation Group. Both traditions share the same practice space,
making this a genuine multi-tradition community hub.

Centers included:
  - Jackson Zen Group (jackson_zen_group)
    Zen (Shorinji Zen Association — Soto-influenced)
    4308 Old Canton Rd, Jackson MS 39211 (Wolfe Fine Art Studio Dojo)
    zeninmississippi.org · Wed 7am (30 min), Sun 8:30am (two 30-min sits + kinhin)
    One-time orientation required. Drop-in after orientation.

  - Jackson Insight Meditation Group (jackson_insight)
    Theravada / Vipassana / Insight Meditation
    4308 Old Canton Rd, Jackson MS 39211 (Wolfe Fine Art Studio Dojo)
    dharmainmississippi.com · Mon evenings (guided Metta, drop-in), Sat mornings (sit + discussion)

Research notes (2026-08-10):
  - Both groups meet at the Wolfe Fine Art Studio Dojo, 4308 Old Canton Rd, near I-55
    and Northside Drive in north Jackson. Contact: Bebe Wolfe (601) 201-4228.
  - Jackson Zen Group: Shorinji Zen Association lineage. Wed 7:00am (30 min zazen),
    Sun 8:30am (two 30-min periods with kinhin and ceremony). One-time orientation
    required before first visit (jacksonzengroup@gmail.com). Open to all after orientation.
    zeninmississippi.org/schedule/schedule.php — static HTML, no iCal.
  - Jackson Insight Meditation Group: Theravada / Vipassana. Monday evenings: guided
    Metta (loving-kindness) practice, beginner-friendly, drop-in. Saturday mornings:
    30-min silent sit + discussion based on dharma talk recording or book study. Free
    and open regardless of financial ability. Contact: bebewolfe@gmail.com.
    dharmainmississippi.com — static HTML, no iCal.
  - Moments of Joy Sangha (Plum Village, informal): meets at same dojo, schedule
    unconfirmed. Deferred until schedule is verified.
  - Metta Buddhist Center (about.me/mettacenterjxn): Schedule not documented publicly.
    Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "jackson_zen_group": Center(
        id="jackson_zen_group",
        name="Jackson Zen Group",
        url="https://zeninmississippi.org",
        address="4308 Old Canton Rd",
        city="Jackson",
        state="MS",
        zip_code="39211",
        lat=32.3780,
        lng=-90.1270,
        neighborhood="North Jackson",
        tradition=Tradition.ZEN,
        notes=(
            "Jackson Zen Group (Shorinji Zen Association) is a Soto-influenced Zen "
            "group meeting at the Wolfe Fine Art Studio Dojo, 4308 Old Canton Rd, "
            "North Jackson MS 39211. Regular schedule: Wednesday 7:00am (30-min zazen) "
            "and Sunday 8:30am (two 30-min sittings with kinhin and ceremony). "
            "A one-time orientation is required before your first sit — contact "
            "jacksonzengroup@gmail.com to arrange. Open to all after orientation. "
            "zeninmississippi.org · (601) 201-4228."
        ),
    ),
    "jackson_insight": Center(
        id="jackson_insight",
        name="Jackson Insight Meditation Group",
        url="https://dharmainmississippi.com/opportunities-to-practice/jackson-insight-meditation-group",
        address="4308 Old Canton Rd",
        city="Jackson",
        state="MS",
        zip_code="39211",
        lat=32.3780,
        lng=-90.1270,
        neighborhood="North Jackson",
        tradition=Tradition.THERAVADA,
        notes=(
            "Jackson Insight Meditation Group is a Theravada / Vipassana community "
            "meeting at the Wolfe Fine Art Studio Dojo, 4308 Old Canton Rd, "
            "North Jackson MS 39211. Monday evenings: guided Metta (loving-kindness) "
            "practice — beginner-friendly, drop-in. Saturday mornings: 30-min silent sit "
            "followed by discussion of a recorded dharma talk or book study. Free and open "
            "to all regardless of financial ability. Contact: bebewolfe@gmail.com or "
            "(601) 201-4228. dharmainmississippi.com."
        ),
    ),
}

# No live iCal feeds — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
