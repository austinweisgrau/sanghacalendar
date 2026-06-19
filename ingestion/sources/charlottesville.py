"""
Charlottesville, Virginia — Phase 3 expansion (heartbeat 80).

Charlottesville (pop. ~50k city; ~250k Albemarle County metro) is a university
town (UVA, ~24k students) with a well-developed meditation scene. The Buddhist
community is small but spans Insight, Zen, and Rinzai traditions, anchored by
centers that have operated for decades.

Centers included:
  - Insight Meditation Community of Charlottesville (insight_meditation_charlottesville)
    Theravada / Insight Meditation (Vipassana), founded 1996
    717 Rugby Road (UU Church), Charlottesville VA 22903
    imeditation.org · Tuesday 7:00–8:30pm hybrid (in-person + Zoom), ~50–60 attendees

  - Clear Spring Zen (clear_spring_zen_charlottesville)
    Zen (Diamond Sangha lineage — Robert Aitken); teacher Marian Morgan
    717 Rugby Road (UU Church), Charlottesville VA 22903
    clearspringzen.org · Wednesday 7:00–8:00pm in-person; Sunday 9:00–10:30am online

  - Blue Ridge Zen Group (blue_ridge_zen)
    Rinzai Zen (Myoshin-ji temple lineage); teacher Teido (Bill) Stephens, founded 1975
    4425 Advance Mills Road, Earlysville VA 22936 (Albemarle County, ~10 miles north)
    brzen.org · Tuesday 5:30–6:00pm + Sunday 9:00–10:15am (private zendo; contact first)

Research notes (2026-06-19):
  - IMCC: Active since 1996, ~175 members. Tuesday evenings at UU Church of Charlottesville
    (717 Rugby Rd). 7pm hybrid: guided meditation (~35 min) + dharma talk. Also has two
    additional weekly sits (details on website). Wild Apricot calendar, no iCal feed.
  - Clear Spring Zen: Diamond Sangha lineage teacher Marian Morgan. Two public sits:
    Wednesday 7pm at UU Church (in-person), Sunday 9am Zoom. Crozet Zendo has additional
    private sits (weekday mornings/evenings, Saturdays) — address by inquiry only.
    WordPress My Calendar, no iCal subscription URL exposed.
  - Blue Ridge Zen Group: Rinzai Zen since 1975, affiliated with Rinzai-ji. Teacher Teido
    (Bill) Stephens, Myoshin-ji lineage. Meetings at private zendo in Earlysville
    (~10 miles north of Charlottesville). Tuesday zazen 5:30pm and Sunday 9am sit.
    Mailing address publicly listed; zendo address by inquiry. No iCal feed.
  - Jefferson Tibetan Society: Sporadic events in 2026 (Gelug, Drepung Loseling affil.).
    No regular drop-in program confirmed — deferred.
  - White Hall Meditation (Insight, Crozet Library): ~2x/month alternating Wed/Sat.
    Too infrequent and irregular pattern for recurring seed — deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "insight_meditation_charlottesville": Center(
        id="insight_meditation_charlottesville",
        name="Insight Meditation Community of Charlottesville",
        url="https://www.imeditation.org",
        address="717 Rugby Road",
        city="Charlottesville",
        state="VA",
        zip_code="22903",
        lat=38.0517,
        lng=-78.4968,
        neighborhood="Rugby Road / UVA",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Community of Charlottesville (IMCC) is a Theravada/Vipassana "
            "sangha founded in 1996, with ~175 members. Meets at the Unitarian Universalist "
            "Church of Charlottesville (717 Rugby Road). Tuesday evenings 7:00–8:30pm: "
            "hybrid sit (in-person + Zoom) — guided meditation followed by dharma talk. "
            "Typical attendance ~50–60. Additional weekly sits listed on website. "
            "Free, open to all. imeditation.org."
        ),
    ),
    "clear_spring_zen_charlottesville": Center(
        id="clear_spring_zen_charlottesville",
        name="Clear Spring Zen",
        url="https://clearspringzen.org",
        address="717 Rugby Road",
        city="Charlottesville",
        state="VA",
        zip_code="22903",
        lat=38.0517,
        lng=-78.4968,
        neighborhood="Rugby Road / UVA",
        tradition=Tradition.ZEN,
        notes=(
            "Clear Spring Zen is a Diamond Sangha lineage Zen community led by teacher "
            "Marian Morgan (Robert Aitken lineage). Two public sits: Wednesday 7–8pm "
            "in-person at UU Church, 717 Rugby Road, Charlottesville; and Sunday 9–10:30am "
            "via Zoom. The Crozet Zendo also holds additional sits (weekday mornings/evenings "
            "and Saturdays) — contact teacher for address and details. "
            "Free, all welcome. clearspringzen.org."
        ),
    ),
    "blue_ridge_zen": Center(
        id="blue_ridge_zen",
        name="Blue Ridge Zen Group",
        url="https://www.brzen.org",
        address="4425 Advance Mills Road",
        city="Earlysville",
        state="VA",
        zip_code="22936",
        lat=38.1547,
        lng=-78.4697,
        neighborhood="Earlysville (Albemarle County)",
        tradition=Tradition.ZEN,
        notes=(
            "Blue Ridge Zen Group is a Rinzai Zen community in the Myoshin-ji temple "
            "lineage, led by teacher Teido (Bill) Stephens. Founded 1975; affiliated with "
            "Rinzai-ji. Meets at a private zendo in Earlysville, Albemarle County (~10 miles "
            "north of Charlottesville). Tuesday zazen 5:30–6pm and Sunday sitting 9–10:15am. "
            "Zendo address provided by inquiry — contact via brzen.org before visiting. "
            "One of the oldest Rinzai Zen communities on the East Coast. brzen.org."
        ),
    ),
}

# No live iCal feeds available — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
