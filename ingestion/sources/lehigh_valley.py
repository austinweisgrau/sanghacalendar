"""
Lehigh Valley, PA — Phase 3 expansion (heartbeat 65; expanded heartbeat 113).

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

  - Christmas City Sangha (christmas_city_sangha) — Plum Village / TNH Zen
    Cathedral Church of the Nativity, 321 Wyandotte St, Bethlehem PA 18015
    pa-community-of-mindful-living.org · Weekly Wednesday 7pm sit (in-person)

  - Mountain Lotus Sangha (mountain_lotus_sangha) — Plum Village / TNH Zen
    Jim Thorpe Yoga, 434 Center St, Jim Thorpe PA 18229
    mountainlotussangha.weebly.com · Weekly Sunday 10am sit (in-person)

Research notes (2026-05-25 / updated 2026-10-13):
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
  - Christmas City Sangha: Plum Village / TNH, affiliated with PA Community of
    Mindful Living. Meets at Cathedral Church of the Nativity (historic Episcopal
    church), 321 Wyandotte St, Bethlehem. Wed 7–8:30pm (doors 6:30pm): 20-min
    guided meditation, walking meditation, silent sitting. Contact Kevin Siddons,
    kevinsiddons@yahoo.com. No iCal. Free.
  - Mountain Lotus Sangha: Plum Village / TNH, affiliated with PA Community of
    Mindful Living. Meets at Jim Thorpe Yoga, 434 Center St, Jim Thorpe PA
    (~35 mi NW of Allentown). Weekly Sunday 10am–noon. No iCal.
    mountainlotussangha.weebly.com (may be outdated).
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
    "christmas_city_sangha": Center(
        id="christmas_city_sangha",
        name="Christmas City Sangha",
        url="https://www.pa-community-of-mindful-living.org/christmas-city-sangha.html",
        address="321 Wyandotte St",
        city="Bethlehem",
        state="PA",
        zip_code="18015",
        lat=40.6192,
        lng=-75.3736,
        neighborhood="Bethlehem",
        tradition=Tradition.ZEN,
        notes=(
            "Christmas City Sangha is a Plum Village / Thich Nhat Hanh community "
            "affiliated with the PA Community of Mindful Living. They meet every "
            "Wednesday 7:00–8:30pm (doors open 6:30pm) at the Cathedral Church of "
            "the Nativity, 321 Wyandotte St, Bethlehem. Practice includes 20 minutes "
            "of guided meditation, walking meditation, and silent sitting. Free, all "
            "welcome. Contact Kevin Siddons at kevinsiddons@yahoo.com."
        ),
    ),
    "mountain_lotus_sangha": Center(
        id="mountain_lotus_sangha",
        name="Mountain Lotus Sangha",
        url="http://mountainlotussangha.weebly.com",
        address="434 Center St",
        city="Jim Thorpe",
        state="PA",
        zip_code="18229",
        lat=40.8768,
        lng=-75.7355,
        neighborhood="Jim Thorpe",
        tradition=Tradition.ZEN,
        notes=(
            "Mountain Lotus Sangha is a Plum Village / Thich Nhat Hanh community "
            "affiliated with the PA Community of Mindful Living. They meet every "
            "Sunday 10:00am–noon at Jim Thorpe Yoga (434 Center St, Jim Thorpe PA), "
            "approximately 35 miles northwest of Allentown in the Pocono foothills. "
            "Free, all welcome."
        ),
    ),
}

# No live iCal feeds available — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
