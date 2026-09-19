"""
Dayton, Ohio — Phase 3 expansion.

Dayton is a mid-sized Ohio metro (~800k metro, 140k city) in the Miami Valley.
The Buddhist scene is modest but includes a well-established Tibetan center
with a live iCal feed, an active non-sectarian daily-sitting center in nearby
Yellow Springs, and a Korean Zen group in Centerville.

Centers included:
  - gar_drolma — Drikung Kagyu Tibetan (Garchen Rinpoche lineage)
    1329 Creighton Ave, Dayton OH 45420
    gardrolma.org · live iCal feed (Tribe Events / The Events Calendar WP plugin)

  - zen_fellowship_dayton — Kwan Um Zen (Furnace Mountain / Cincinnati ZC affiliate)
    61-B South Main Street, Centerville OH 45458
    zenfellowshipdayton.com · no iCal (Wix); recurring sits seeded.

  - yellow_springs_dharma — non-sectarian (Vipassana + Zen + Vajrayana)
    502 Livermore Street, Yellow Springs OH 45387 (~20 mi east of Dayton)
    ysdharma.org · no iCal; recurring sits seeded.

Research notes (2026-09-19):
  - Gar Drolma: founded 2002/incorporated 2003. Full address 1329 Creighton Ave,
    Dayton OH 45420 (Belmont neighborhood). Khenpo Samdup Rinpoche is Spiritual
    Director; weekly schedule posted at gardrolma.org/schedule-events/. The
    Events Calendar WP plugin provides a working ?ical=1 feed with ~15-20 events.
  - Zen Fellowship of Dayton: Wix site, no iCal. Affiliated with Cincinnati ZC
    and Furnace Mountain (Zen Master Dae Gak / Seung Sahn lineage). Meets
    Tuesdays 7pm + Sundays 8am in Centerville (61-B S Main St, Suite B).
    Teacher: Abbot Hae Cho (Connie Klayko). Drop-in; free.
  - Yellow Springs Dharma Center: robust daily schedule across Vipassana, Zen,
    and Vajrayana. Located in Yellow Springs, a small college town (Antioch
    College) ~20 mi from Dayton. Mon-Fri 8-8:40am morning open sit; Mon-Thu
    7-7:30pm evening open sit; Sat 7:30-9:30am Zen (Zoom too); Sun 8-10am
    Vipassana; Sun 11am-noon Vajrayana (2nd/3rd/4th). Orientation 2nd+4th Mon
    7:30pm. No iCal.
  - RK Dharma Center (1214 Creighton Ave): Rissho Kosei-kai — primarily Lotus
    Sutra study/liturgy, not meditation-focused. Skip.
  - Blue Lotus Assembly (6236 Far Hills Ave): ninjutsu school with monthly
    Buddhist meditation (full moon Wed). Monthly only; skip.
  - Springfield Zen Center (600 S Douglas Ave, Springfield OH): small group,
    no website, Mon 7pm only. Status uncertain; skip pending confirmation.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "gar_drolma": Center(
        id="gar_drolma",
        name="Gar Drolma Buddhist Learning and Meditation Center",
        url="https://gardrolma.org",
        address="1329 Creighton Avenue",
        city="Dayton",
        state="OH",
        zip_code="45420",
        lat=39.7412,
        lng=-84.1542,
        neighborhood="Belmont",
        tradition=Tradition.TIBETAN,
        notes=(
            "Gar Drolma is a Drikung Kagyu Tibetan Buddhist learning and meditation "
            "center in Dayton's Belmont neighborhood. Founded 2002/incorporated 2003 "
            "under the guidance of His Eminence Garchen Rinpoche. Spiritual Director: "
            "Khenpo Samdup Rinpoche. Offers a rich weekly schedule of meditation, "
            "dharma teachings, and Vajrayana practices including Achi (Drikung protector) "
            "practice, Parnashavari, and Chenrezig. Weekly 'Meditation & Learning "
            "Buddhism Program' open to the public on select evenings — see calendar. "
            "Weekend sessions with Khenpo Samdup both in-person and online. "
            "Phone: (937) 252-2220. gardrolma.org."
        ),
    ),
    "zen_fellowship_dayton": Center(
        id="zen_fellowship_dayton",
        name="Zen Fellowship of Dayton",
        url="https://www.zenfellowshipdayton.com",
        address="61-B South Main Street",
        city="Centerville",
        state="OH",
        zip_code="45458",
        lat=39.6292,
        lng=-84.1313,
        neighborhood="Centerville",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Fellowship of Dayton is a Korean Zen (Kwan Um School) sitting group "
            "in Centerville, a suburb south of Dayton. Affiliated with Cincinnati Zen "
            "Center and Furnace Mountain Zen Center. Lineage: Zen Master Dae Gak, who "
            "received Dharma transmission from Zen Master Seung Sahn in 1994. Abbot: "
            "Hae Cho (Connie Klayko). Regular resident teacher: Myo Wol Soen-sa "
            "(Mark Davis). Tuesday evenings 7:00 PM and Sunday mornings 8:00 AM. "
            "Drop-in welcome, free. Also offers occasional tea ceremonies, Five Bowls "
            "Eating Practice, and retreats. zenfellowshipdayton.com."
        ),
    ),
    "yellow_springs_dharma": Center(
        id="yellow_springs_dharma",
        name="Yellow Springs Dharma Center",
        url="https://www.ysdharma.org",
        address="502 Livermore Street",
        city="Yellow Springs",
        state="OH",
        zip_code="45387",
        lat=39.8014,
        lng=-83.8911,
        neighborhood="Yellow Springs",
        tradition=Tradition.PLURALIST,
        notes=(
            "Yellow Springs Dharma Center (YSDC) is a non-sectarian Buddhist practice "
            "center in Yellow Springs, Ohio (~20 miles east of Dayton in the Dayton "
            "metro area). Supports three traditions: Vipassana, Zen, and Vajrayana. "
            "Robust daily schedule: weekday morning open meditation Mon–Fri 8:00–8:40 AM; "
            "weekday evening open meditation Mon–Thu 7:00–7:30 PM; Zen practice "
            "Saturdays 7:30–9:30 AM (Zoom available); Vipassana practice Sundays "
            "8:00–10:00 AM; Vajrayana practice 2nd, 3rd, and 4th Sundays 11:00 AM–noon. "
            "Orientation sessions 2nd and 4th Mondays 7:30 PM. Phone: (937) 767-9919. "
            "ysdharma.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "gar_drolma": {
        "url": "https://gardrolma.org/?ical=1",
        "filter_to_sits": True,
    },
}

# No Eventbrite or static HTML scrapers for this metro.
EVENTBRITE_FEEDS: dict = {}
STATIC_HTML_FEEDS: dict = {}
