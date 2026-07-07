"""
Santa Barbara, California — Phase 3 expansion (heartbeat 85).

Santa Barbara (pop. ~88K city / ~440K metro) is a coastal city on the California
Riviera, home to UCSB and a well-established Buddhist community. The Santa Barbara
Dharma Circle (sbdharmacircle.net) lists 15+ centers and groups.

Centers included:
  - Mahakankala Kadampa Buddhist Center (kmc_santa_barbara)
    New Kadampa Tradition (NKT-IKBU, Geshe Kelsang Gyatso lineage)
    1825 State Street Suite 202, Santa Barbara CA 93101
    meditationinsantabarbara.org · Live iCal feed (WordPress ECPv6)
    Sun 11am, Mon 6:30pm, Sun Foundation Program 1:30pm

  - Open Door Sangha (open_door_sangha_sb)
    Theravada / Vipassana / Insight (IMC-affiliated)
    Unity Church, 227 East Arrellaga Street, Santa Barbara CA 93101
    insightmeditationsb.org · Mon/Wed/Thu evenings 7pm (seeded recurring)

  - Santa Barbara Zen Center (santa_barbara_zen_center)
    Soto Zen
    2050 Alameda Padre Serra Unit 100, Santa Barbara CA 93103
    santabarbarazencenter.org · 2nd & 4th Sunday 9:45am (seeded monthly)

  - Bodhi Path Buddhist Center of Santa Barbara (bodhi_path_sb)
    Karma Kagyu / Tibetan (founded by Shamar Rinpoche, 1997)
    3815 State Street Suite G129, Santa Barbara CA 93101
    bodhipath.org/centers/sb · Tue 6pm, Thu 7pm (seeded recurring)

Research notes (2026-07-07):
  - KMC Santa Barbara: 1825 State Street Suite 202, downtown SB.
    WordPress ECPv6 iCal feed confirmed at meditationinsantabarbara.org/?ical=1.
    Active calendar: Sun 11am meditation class, Mon 6:30pm Lamrim, Sun 1:30pm
    Foundation Program, plus prayers and special events. (805) 563-6000.
  - Open Door Sangha: Theravada / Vipassana community affiliated with IMC tradition.
    Meets at Unity Church, 227 E Arrellaga St. Weekly: Mon 7–8pm (in-person),
    Wed 7–8pm (in-person), Thu 7–8:30pm (hybrid Zoom + in-person). Also Thu
    noon at UCSB (online). insightmeditationsb.org = opendoorsangha.org.
  - Santa Barbara Zen Center: Small Soto Zen group meeting 2nd & 4th Sunday
    at Santa Barbara Hospice (2050 Alameda Padre Serra Unit 100), 9:45am,
    in-person + Zoom. santabarbarazencenter@gmail.com. No iCal subscription feed;
    individual event ICS downloads only. Seeded as monthly recurring.
  - Bodhi Path Santa Barbara: Karma Kagyu center founded in 1997 at Shamar
    Rinpoche's direction. 3815 State St Suite G129 (near the 101/upper State area).
    Weekly meditation: Tue 6–7pm (in-person + Zoom). Weekly dharma teaching:
    Thu 7–9pm (in-person + Zoom). Monthly Joy of Practice (longer sitting).
    bodhipath.org was returning 403 during research — site may have Cloudflare;
    schedule confirmed via Yelp and secondary sources. (805) 284-2704.
  - Other Santa Barbara centers researched (not added):
    Odiyana Institute (odiyanainstitute.org) — Nyingma Tibetan, private residential
    retreat center, not a public meditation sitting venue.
    Pine Mountain Buddhist Temple — Soto Zen, Carpinteria (10mi south); small group.
    Mahakankala is the Kadampa center; also a separate Rigpa group exists.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_santa_barbara": Center(
        id="kmc_santa_barbara",
        name="Mahakankala Kadampa Buddhist Center",
        url="https://meditationinsantabarbara.org",
        address="1825 State Street Suite 202",
        city="Santa Barbara",
        state="CA",
        zip_code="93101",
        lat=34.4251,
        lng=-119.7031,
        neighborhood="Downtown Santa Barbara",
        tradition=Tradition.TIBETAN,
        notes=(
            "Mahakankala Kadampa Buddhist Center offers Tibetan Buddhist meditation "
            "in the New Kadampa Tradition (NKT-IKBU), founded by Geshe Kelsang Gyatso. "
            "Drop-in meditation classes: Sunday 11am, Monday 6:30pm. Also Foundation "
            "Program (advanced study), lunchtime meditation, and Wishfulfilling Jewel "
            "prayers. All levels welcome; no experience required. "
            "1825 State Street Suite 202, Santa Barbara CA 93101. "
            "(805) 563-6000. meditationinsantabarbara.org."
        ),
    ),
    "open_door_sangha_sb": Center(
        id="open_door_sangha_sb",
        name="Open Door Sangha",
        url="https://www.insightmeditationsb.org",
        address="227 East Arrellaga Street",
        city="Santa Barbara",
        state="CA",
        zip_code="93101",
        lat=34.4218,
        lng=-119.6912,
        neighborhood="Downtown Santa Barbara",
        tradition=Tradition.THERAVADA,
        notes=(
            "Open Door Sangha is a Theravada / Insight Meditation community in Santa "
            "Barbara, offering weekly sitting groups for all levels. Regular programs: "
            "Monday Evening Sitting Group 7–8pm, Wednesday Evening Sit & Discussion "
            "7–8pm, Thursday Evening Sitting Group 7–8:30pm (hybrid Zoom + in-person) "
            "— all held at Unity Church, 227 East Arrellaga Street. Also Thursday Noon "
            "Meditation 12:10–12:50pm online. Drop-in welcome; free. "
            "insightmeditationsb.org."
        ),
    ),
    "santa_barbara_zen_center": Center(
        id="santa_barbara_zen_center",
        name="Santa Barbara Zen Center",
        url="https://www.santabarbarazencenter.org",
        address="2050 Alameda Padre Serra Unit 100",
        city="Santa Barbara",
        state="CA",
        zip_code="93103",
        lat=34.4313,
        lng=-119.6844,
        neighborhood="Riviera / Mission Canyon",
        tradition=Tradition.ZEN,
        notes=(
            "Santa Barbara Zen Center is a small Soto Zen community meeting twice "
            "monthly on the 2nd and 4th Sunday at 9:45am, in-person and via Zoom. "
            "Located at Santa Barbara Hospice, 2050 Alameda Padre Serra Unit 100, "
            "on the Riviera hillside above the mission. All are welcome. "
            "santabarbarazencenter@gmail.com. santabarbarazencenter.org."
        ),
    ),
    "bodhi_path_sb": Center(
        id="bodhi_path_sb",
        name="Bodhi Path Buddhist Center of Santa Barbara",
        url="https://bodhipath.org/centers/sb/",
        address="3815 State Street Suite G129",
        city="Santa Barbara",
        state="CA",
        zip_code="93101",
        lat=34.4452,
        lng=-119.7404,
        neighborhood="Upper State",
        tradition=Tradition.TIBETAN,
        notes=(
            "Bodhi Path Buddhist Center of Santa Barbara offers Karma Kagyu Tibetan "
            "Buddhist practice and study, founded in 1997 at the direction of Shamar "
            "Rinpoche. Weekly meditation: Tuesday 6–7pm (in-person + Zoom). Weekly "
            "dharma teaching: Thursday 7–9pm (in-person + Zoom). Monthly 'Joy of "
            "Practice' sessions for extended sitting and walking meditation. "
            "3815 State Street Suite G129, Santa Barbara CA 93101. "
            "(805) 284-2704. bodhipath.org/centers/sb/."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "kmc_santa_barbara": {
        # WordPress Events Calendar (ECPv6.16.5.1) iCal export.
        # Verified working 2026-07-07: valid VCALENDAR response with Sun/Mon classes,
        # Foundation Program, prayers, and special events.
        "url": "https://meditationinsantabarbara.org/?ical=1",
        "filter_to_sits": True,
    },
}
