"""
Lehigh Valley, PA — Phase 3 expansion (heartbeat 65).

The Lehigh Valley (Allentown / Bethlehem / Emmaus, PA; ~830k metro) is home
to a modest but real Buddhist community. Centers are small and mostly lack
iCal feeds — all ingested via seeded recurring sits.

Centers included:
  - Dharma Moon Sangha (dharma_moon_sangha) — Plum Village / Mahayana Zen
    Living Room Yoga, 1328 Chestnut St, Emmaus PA 18049
    dharmamoonsangha.com · Weekly Tuesday 7pm sit (in-person + Zoom)

  - Blue Mountain Zendo (blue_mountain_zendo) — Rinzai Zen
    Bethlehem, PA 18017 (exact address unpublished; call 484-735-0636)
    bluemountainzendo.org · Weekly Sunday 5pm full Zen service

  - Lehigh Valley Buddhist Group (lv_buddhist_group) — Non-sectarian / ecumenical
    Unity of Lehigh Valley, 26 N 3rd St, Emmaus PA 18049
    lvbuddhistgroup.org · Monthly Sunday 4pm dharma + meditation gathering

Research notes (2026-05-25):
  - Dharma Moon Sangha: active since 2009. Meets at Living Room Yoga, Emmaus.
    Weekly Tuesday 7pm (in-person + Zoom). 20-min zazen, kinhin, more zazen,
    dharma sharing. Free, drop-in welcome. emmaussangha@gmail.com.
    No iCal; no Eventbrite. Simple WordPress blog.
  - Blue Mountain Zendo (Koryu-ji): Rinzai Zen, Rev. Ryuun Joriki Baker.
    Bethlehem Zendo meets Sunday 5–7pm (full service: chanting, zazen, kinhin,
    formal eating, dharma talk, tea). Newcomers arrive 15 min early. Second
    location in Bushkill (Pocono Mts). Private address — call 484-735-0636.
    WordPress site with The Events Calendar plugin, but ?ical=1 returns empty.
  - Lehigh Valley Buddhist Group: Ecumenical; hosts guest teachers from multiple
    lineages. Monthly Sunday 4–5:30pm at Unity of Lehigh Valley church (Emmaus).
    2026 confirmed dates: Jun 21, Jul 12 (plus likely Aug–Oct). All welcome.
    No iCal; individual event ICS downloads only.
  - Saccananda Dhamma Center (5058 PA-378, Bethlehem): Burmese Theravada;
    primarily serves ethnic community, schedule unconfirmed — deferred.
  - New Leaf Meditation (131 S Main St, Nazareth): secular mindfulness, not
    explicitly Buddhist — skipped.
  - No Shambhala, KMC/NKT, or Diamond Way centers found in Lehigh Valley.
  - Nearest Tibetan/Zen centers are Philadelphia (~60 mi south).
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "dharma_moon_sangha": Center(
        id="dharma_moon_sangha",
        name="Dharma Moon Sangha",
        url="https://dharmamoonsangha.com",
        address="1328 Chestnut St",
        city="Emmaus",
        state="PA",
        zip_code="18049",
        lat=40.5380,
        lng=-75.4998,
        neighborhood="Emmaus",
        tradition=Tradition.ZEN,
        notes=(
            "Dharma Moon Sangha is a Plum Village / Order of Interbeing sangha "
            "meeting weekly at Living Room Yoga in Emmaus, PA. Founded 2009. "
            "Tuesday 7:00pm (in-person + Zoom): 20-min zazen, kinhin (walking "
            "meditation), more seated zazen, dharma sharing. Free, all welcome, "
            "no reservation required. Zoom link via emmaussangha@gmail.com."
        ),
    ),
    "blue_mountain_zendo": Center(
        id="blue_mountain_zendo",
        name="Blue Mountain Zendo",
        url="https://www.bluemountainzendo.org",
        address="Bethlehem, PA",
        city="Bethlehem",
        state="PA",
        zip_code="18017",
        lat=40.6259,
        lng=-75.3705,
        neighborhood="Bethlehem",
        tradition=Tradition.ZEN,
        notes=(
            "Blue Mountain Zendo (Koryu-ji) is a Rinzai Zen center led by "
            "Rev. Ryuun Joriki Baker. The Bethlehem Zendo holds a full Zen "
            "service every Sunday 5:00–7:00pm: chanting, zazen, kinhin (walking "
            "meditation), formal eating (oryoki), dharma talk, and tea fellowship. "
            "Newcomers welcome — arrive 15 minutes early. Private home address; "
            "call 484-735-0636 for directions. Second location in Bushkill PA "
            "(Pocono Mountains)."
        ),
    ),
    "lv_buddhist_group": Center(
        id="lv_buddhist_group",
        name="Lehigh Valley Buddhist Group",
        url="https://www.lvbuddhistgroup.org",
        address="26 N 3rd St",
        city="Emmaus",
        state="PA",
        zip_code="18049",
        lat=40.5378,
        lng=-75.4965,
        neighborhood="Emmaus",
        tradition=Tradition.OTHER,
        notes=(
            "Lehigh Valley Buddhist Group is a non-sectarian, ecumenical sangha "
            "hosting monthly gatherings at Unity of Lehigh Valley church in Emmaus. "
            "Monthly Sunday 4:00–5:30pm: guest teachers from Theravada, Tibetan, "
            "and Zen traditions lead meditation, dharma talks, and Q&A. Open to "
            "Buddhist and non-Buddhist alike. Free. Info@lvbuddhistgroup.org."
        ),
    ),
}

# No live iCal feeds available — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
