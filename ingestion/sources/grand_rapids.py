"""
Grand Rapids, Michigan — Phase 3 expansion (heartbeat 98).

Grand Rapids (pop. ~198k city, ~1.1M metro) is Michigan's second-largest city
and the largest city in West Michigan. The Buddhist community is anchored by
the Grand Rapids Buddhist Temple — a multi-tradition hub on S Division Ave
that hosts Soto Zen primary practice, a Sokukoji-affiliate Tuesday Zen group,
and Buddhist-based recovery sits.

Centers included:
  - Grand Rapids Buddhist Temple (grand_rapids_buddhist_temple)
    Multi-tradition: Soto Zen primary (also Tibetan Gelug, Heartside Mindfulness)
    451 S Division Ave, Grand Rapids MI 49503
    zengr.org · Sun 9:30am in-person + streaming, Mon 6:30pm recovery, Fri 10:05am recovery

  - Grand Rapids Zen (Sokukoji affiliate) (grand_rapids_zen)
    Soto Zen — affiliated with SokukoJi Monastery, Battle Creek
    451 S Division Ave, Grand Rapids MI 49503 (Grand Rapids Buddhist Temple, rear entrance)
    meetup.com/grandrapidszen · Tue 6–8pm (meditation + book study)

Research notes (2026-08-13):
  - Grand Rapids Buddhist Temple (zengr.org): Multi-tradition center rooted in
    Soto Zen Mahayana (also hosts Tibetan Gelug and Heartside Mindfulness programming).
    451 S Division Ave, Grand Rapids MI 49503. Sunday schedule: setup 9am, chants +
    silent meditation 9:30am, service 10am, social 11–11:30am (also on YouTube/Zoom).
    Monday: Buddhist-based recovery sit 6:30pm, meeting 7pm.
    Friday: Buddhist-based recovery meditation 10:05am.
    Google Sites calendar at zengr.org/temple-events/calendar — no iCal export.
  - Grand Rapids Buddhist Meetup (meetup.com/grandrapidszen): Sokukoji affiliate.
    Meets Tuesdays 6–8pm at the Buddhist Temple (rear entrance off Logan St).
    Meditation + book study. Occasionally Abbot Sokuzan gives talks 1st Tuesday.
    Free, open to all. Donations appreciated. No iCal feed.
  - SokukoJi Buddhist Temple Monastery (Battle Creek): 33 Anderson Ct, Battle Creek MI 49017.
    Mon/Tue/Wed/Fri 2:30–4:30pm sits, last Saturday sesshin 8am–4pm. Too far for
    Grand Rapids grouping; may add as separate Battle Creek entry later.
  - Just Sit Soto Zen (justsitsotozen.org): 2232 Woodcliff Ave SE, Grand Rapids MI 49546.
    Small private Soto Zen group; newcomers contact first. Schedule not publicly confirmed.
    Deferred until schedule verified.
  - Withered Tree Sangha (buddhistgr.com): Online-only, non-sectarian. Deferred — no in-person.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "grand_rapids_buddhist_temple": Center(
        id="grand_rapids_buddhist_temple",
        name="Grand Rapids Buddhist Temple",
        url="https://www.zengr.org",
        address="451 S Division Ave",
        city="Grand Rapids",
        state="MI",
        zip_code="49503",
        lat=42.9548,
        lng=-85.6679,
        neighborhood="Heartside",
        tradition=Tradition.ZEN,
        notes=(
            "Grand Rapids Buddhist Temple is a multi-tradition center rooted in Soto Zen "
            "Mahayana Buddhism, honoring the interconnection of all beings and the "
            "compassionate Bodhisattva path. Also hosts Tibetan Gelug instruction and "
            "Heartside Mindfulness School programming. 451 S Division Ave, Grand Rapids "
            "MI 49503. Sunday: chants + silent meditation 9:30am, full service 10am, "
            "social 11am — in-person and livestreamed on YouTube/Zoom. Children's Sangha "
            "School (resuming Sep 2026). Buddhist-based recovery sits: Mon 6:30pm, "
            "Fri 10:05am. Free and open to all. zengr.org."
        ),
    ),
    "grand_rapids_zen": Center(
        id="grand_rapids_zen",
        name="Grand Rapids Zen (Sokukoji Affiliate)",
        url="https://www.meetup.com/grandrapidszen/",
        address="451 S Division Ave",
        city="Grand Rapids",
        state="MI",
        zip_code="49503",
        lat=42.9548,
        lng=-85.6679,
        neighborhood="Heartside",
        tradition=Tradition.ZEN,
        notes=(
            "Grand Rapids Zen is a Soto Zen group affiliated with SokukoJi Buddhist "
            "Temple Monastery (Battle Creek, MI) and the Order of Immediate Light. "
            "Meets Tuesdays 6–8pm at the Grand Rapids Buddhist Temple, 451 S Division "
            "Ave (rear entrance off Logan St). Sessions include sitting meditation + "
            "dharma book study; Abbot Sokuzan occasionally joins for talks. Free and "
            "open to all; donations welcome. meetup.com/grandrapidszen."
        ),
    ),
}

# No live iCal feeds — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
