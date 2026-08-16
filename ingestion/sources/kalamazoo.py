"""
Kalamazoo / Battle Creek, Michigan — Phase 3 expansion (heartbeat 99).

Kalamazoo (pop. ~72k city, ~270k metro) and Battle Creek (~50k city) together form
Southwest Michigan's main Buddhist hub. The region's most active center is SokukoJi
Buddhist Temple Monastery in Battle Creek — a daily-practice monastery in the Soto
Zen / Order of Immediate Light tradition led by Abbot Kyoun Sokuzan. Jewel Heart
West Michigan (Kalamazoo) offers Tuesday evening Tibetan Vajrayana study.

Centers included:
  - SokukoJi Buddhist Temple Monastery (sokukoji)
    Soto Zen + Order of Immediate Light (Soto/Kagyu blend)
    33 Anderson Ct, Battle Creek MI 49017
    sokukoji.org · Daily sits + Wednesday evening + Sunday morning service

  - Jewel Heart West Michigan (jewel_heart_west_michigan)
    Tibetan Vajrayana — Jewel Heart International (Gelek Rimpoche lineage)
    People's Church of Kalamazoo, 1758 N 10th St, Kalamazoo MI 49009
    jewelheart.org · Tuesday 7–8:30pm

Research notes (2026-08-16):
  - SokukoJi (sokukoji.org): Active Soto Zen monastery with rich daily schedule.
    Abbot Kyoun Sokuzan (Order of Immediate Light, Soto/Kagyu blend). Open to
    all — drop-in welcomed explicitly; chairs available; dark clothing requested.
    Online participation (Zoom) available for most sessions. No iCal feed —
    Wix Events calendar with no export. Sits seeded manually.
  - Jewel Heart West Michigan (jewelheart.org/chapters/west-michigan/):
    Tibetan Vajrayana, affiliated with Jewel Heart International (Ann Arbor).
    Founded by Kyabje Gelek Rimpoche; teachings also from Demo Rinpoche.
    Tuesday 7–8:30pm at People's Church of Kalamazoo, 1758 N 10th St N.
    All are welcome, donations appreciated, no registration.
  - Shambhala Portage (1611 W Centre Ave Ste 208, Portage MI): website defunct,
    localendar calendar empty. Activity migrated to DSG Kazoo (online only).
    Skipped — no verifiable current public schedule.
  - Dharma Study Group Kazoo (dsgroupkazoo.com): Active online, no public venue.
    Skipped — no fixed in-person location.
  - Lama Tsong Khapa Center (224 Rose Place, Kalamazoo): Ad-hoc only, contact
    required. Skipped — no public drop-in schedule.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "sokukoji": Center(
        id="sokukoji",
        name="SokukoJi Buddhist Temple Monastery",
        url="https://www.sokukoji.org",
        address="33 Anderson Ct",
        city="Battle Creek",
        state="MI",
        zip_code="49017",
        lat=42.3170,
        lng=-85.1813,
        neighborhood=None,
        tradition=Tradition.ZEN,
        notes=(
            "SokukoJi Buddhist Temple Monastery is a Soto Zen monastery in Battle Creek "
            "led by Abbot Kyoun Sokuzan. The Order of Immediate Light blends Soto Zen "
            "with Tibetan Kagyu elements. Daily sitting practice (morning and afternoon "
            "sessions), Wednesday evening service, and Sunday morning service — all open "
            "to the public. Chairs available; dark non-descript clothing requested. "
            "Online (Zoom) links available for most sessions. Free, donations welcome. "
            "sokukoji.org."
        ),
    ),
    "jewel_heart_west_michigan": Center(
        id="jewel_heart_west_michigan",
        name="Jewel Heart West Michigan",
        url="https://www.jewelheart.org/chapters/west-michigan/",
        address="1758 N 10th St",
        city="Kalamazoo",
        state="MI",
        zip_code="49009",
        lat=42.3091,
        lng=-85.5697,
        neighborhood=None,
        tradition=Tradition.TIBETAN,
        notes=(
            "Jewel Heart West Michigan is a Tibetan Vajrayana center affiliated with "
            "Jewel Heart International (founded by Kyabje Gelek Rimpoche, based in Ann Arbor). "
            "Teachings also offered by Demo Rinpoche. Tuesday evening 7–8:30pm at "
            "People's Church of Kalamazoo, 1758 N 10th St N, Kalamazoo MI 49009. "
            "All are welcome; donations appreciated; no registration required. "
            "jewelheart.org/chapters/west-michigan."
        ),
    ),
}

# No live iCal feeds — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
