"""
Madison, WI — Phase 3 expansion.

Madison is a university city (UW-Madison) with a rich and eclectic Buddhist
community spanning Tibetan, Zen, Shambhala, Plum Village, and lay Karma Kagyu
traditions. The city has 5 confirmed centers offering regular public sits,
with one live iCal feed (Shambhala Madison via Shambhala Cologne server).

Centers included:
  - Shambhala Meditation Center of Madison (shambhala_madison) — Tibetan/Shambhala
    408 S. Baldwin St, Madison WI 53703. madison.shambhala.org
    Sun 10am, Thu 7pm in-person. Live iCal feed: shambhala-koeln.de center=226.

  - Kadampa Meditation Center Madison (kmc_madison) — NKT Tibetan
    1825 S. Park St, Madison WI 53713. meditationinmadison.org
    Sun 10am, Wed noon, Thu 6:30pm. No iCal (WordPress/MEC, feed broken); recurring seeded.

  - Madison Zen Center (madison_zen_center) — Zen (Kapleau lineage, Rochester lineage)
    1820 Jefferson St, Madison WI 53711. madisonzen.org
    Sun 8:30am, Mon 7pm, Tue 6:30am, Wed 6:30pm, Thu 6:30am, Fri 6:30am. No iCal; recurring seeded.

  - Snowflower Sangha (snowflower_sangha) — Plum Village / Thich Nhat Hanh
    Friends Meetinghouse, 1704 Roberts Court, Madison WI 53711. snowflower.org
    Tue 7pm hybrid, Sat 10am in-person. No iCal; recurring seeded.

  - Diamond Way Buddhist Center Madison (diamond_way_madison) — Karma Kagyu Tibetan
    104 King Street Suite 302, Madison WI 53703. diamondway.org/madison
    Sun 7:30pm, Wed 7:30pm in-person. No iCal; recurring seeded.

Research notes (2026-05-21):
  - Shambhala Madison: 408 S. Baldwin St (Isthmus neighborhood). iCal from
    shambhala-koeln.de/ical.php?center=226 confirmed working — returns valid
    VCALENDAR titled "Shambhala events Madison". Sun 10am + Thu 7pm public
    sits confirmed from madison.shambhala.org/calendar.
  - KMC Madison: 1825 S. Park St. WordPress + Modern Events Calendar plugin;
    /?ical=1 endpoint non-responsive. Four weekly drop-in classes; Fri 11am
    Lamrim study class less sit-focused — seeding Sun/Wed/Thu only.
  - Madison Zen Center: 1820 Jefferson St (UW campus area). Kapleau/Rochester
    lineage (teacher Sensei Rick Smith). Rich daily schedule; all 6 weekly
    recurring times seeded. Online Zoom available by request.
  - Snowflower Sangha: TNH/Plum Village. Multiple weekly meetings; seeding
    the two main in-person/hybrid sits (Tue evening hybrid, Sat morning in-person).
  - Diamond Way Madison: 104 King St, 3rd floor (downtown). Ole Nydahl /
    17th Karmapa lineage. Sun + Wed 7:30pm, free, no registration required.
  - Tergar Madison (Yongey Mingyur Rinpoche, Tue 7pm hybrid): Google Calendar
    ICS URL returned 404; deferred. Tue evening overlaps Snowflower anyway.
  - Madison Insight Meditation Group: Squarespace site, per-event ICS only;
    no master feed. Could be seeded as recurring if confirmed stable schedule.
    Currently deferred.
  - Midwest Soto Zen Community: All Zoom currently. Skipped.
  - Tomyoji Zen Temple / Ryugenji: Smaller supplemental groups; deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_madison": Center(
        id="shambhala_madison",
        name="Shambhala Meditation Center of Madison",
        url="https://madison.shambhala.org",
        address="408 S. Baldwin Street",
        city="Madison",
        state="WI",
        zip_code="53703",
        lat=43.0706,
        lng=-89.3887,
        neighborhood="Isthmus / Downtown Madison",
        tradition=Tradition.TIBETAN,
        notes=(
            "The Shambhala Meditation Center of Madison offers weekly open sits "
            "rooted in the Tibetan Buddhist tradition brought to the West by "
            "Chögyam Trungpa Rinpoche. Located on the Madison Isthmus near "
            "the Capitol, the center hosts Sunday Morning Public Meditation "
            "(10 AM–noon) and Thursday Evening Public Meditation (7–8:30 PM). "
            "Both sessions include alternating sitting and walking meditation "
            "periods with instruction available. No experience required; "
            "drop-in welcome. Part of the international Shambhala community."
        ),
    ),
    "kmc_madison": Center(
        id="kmc_madison",
        name="Kadampa Meditation Center Madison",
        url="https://www.meditationinmadison.org",
        address="1825 S. Park Street",
        city="Madison",
        state="WI",
        zip_code="53713",
        lat=43.0568,
        lng=-89.4019,
        neighborhood="South Madison",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Madison (KMC Madison) is Wisconsin's "
            "New Kadampa Tradition (NKT-IKBU) center, offering modern Tibetan "
            "Buddhist teachings and guided meditation at 1825 S. Park Street "
            "in South Madison. Three weekly drop-in public classes: Sunday "
            "Morning Meditation (10–11:15 AM), Wednesday Meditation at Noon "
            "(noon–12:30 PM, $5), and Thursday Buddhist Wisdom for Daily Life "
            "(6:30–7:30 PM). Classes combine guided meditation with Buddhist "
            "philosophy in the Kadampa style. Drop-in welcome; suggested $12/class."
        ),
    ),
    "madison_zen_center": Center(
        id="madison_zen_center",
        name="Madison Zen Center",
        url="https://www.madisonzen.org",
        address="1820 Jefferson Street",
        city="Madison",
        state="WI",
        zip_code="53711",
        lat=43.0617,
        lng=-89.3957,
        neighborhood="Regent / UW Campus Area",
        tradition=Tradition.ZEN,
        notes=(
            "The Madison Zen Center (MZC) is a lay Zen community affiliated "
            "with the Rochester Zen Center, practicing in the combined Rinzai–"
            "Soto lineage of Philip Kapleau Roshi. Under teacher Sensei Rick "
            "Smith, MZC offers an extensive daily schedule: early morning zazen "
            "Tuesday–Friday (6:30 AM), Monday Evening (7–8:30 PM, three 25-minute "
            "rounds with kinhin and instruction), Wednesday Evening (6:30–8:30 PM), "
            "and the main Sunday Program (8:30–10:30 AM with sitting, chanting, "
            "and dharma talk). Drop-in welcome; all levels. Online via Zoom "
            "available by contacting mzc@madisonzen.org."
        ),
    ),
    "snowflower_sangha": Center(
        id="snowflower_sangha",
        name="Snowflower Sangha",
        url="https://snowflower.org",
        address="1704 Roberts Court",
        city="Madison",
        state="WI",
        zip_code="53711",
        lat=43.0676,
        lng=-89.3780,
        neighborhood="Vilas / Friends Meetinghouse",
        tradition=Tradition.ZEN,
        notes=(
            "Snowflower Sangha is Madison's Plum Village community, practicing "
            "in the tradition of Thich Nhat Hanh. The sangha meets multiple "
            "times weekly across Madison. Tuesday Evening (7–8:30 PM) is held "
            "hybrid at the Friends Meetinghouse (1704 Roberts Court) + Zoom. "
            "Saturday Morning (10–11:30 AM) meets in-person at the Friends "
            "Meetinghouse. Practice includes sitting meditation, walking "
            "meditation, Dharma sharing, and chanting. Open to all; no "
            "experience required. Free; dana welcome."
        ),
    ),
    "diamond_way_madison": Center(
        id="diamond_way_madison",
        name="Diamond Way Buddhist Center Madison",
        url="https://diamondway.org/madison/",
        address="104 King Street, Suite 302",
        city="Madison",
        state="WI",
        zip_code="53703",
        lat=43.0740,
        lng=-89.3840,
        neighborhood="Downtown Madison",
        tradition=Tradition.TIBETAN,
        notes=(
            "Diamond Way Buddhist Center Madison is a lay Karma Kagyu Tibetan "
            "Buddhist center in downtown Madison, affiliated with Lama Ole "
            "Nydahl's Diamond Way Buddhist Union and the 17th Karmapa Trinley "
            "Thaye Dorje. Two weekly public meditation sessions open to all: "
            "Sunday Evening (7:30 PM) and Wednesday Evening (7:30 PM) — each "
            "featuring a short talk followed by a guided meditation. Located "
            "on the third floor at 104 King Street, near the Capitol Square. "
            "Free; no experience required; no registration needed."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "shambhala_madison": {
        "url": "https://shambhala-koeln.de/ical.php?center=226",
        "filter_to_sits": True,
    },
}
