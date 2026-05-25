"""
Cleveland, OH — Phase 3 expansion.

Northeast Ohio's Buddhist community spans several suburbs and traditions. Centers
included range from a 40-year-old Kapleau-lineage Zen group to Shambhala, Soto Zen,
Chan/Pure Land, and Insight Meditation groups dispersed across the metro area.

Centers included:
  - Cleveland Shambhala (cleveland_shambhala) — Tibetan/Shambhala
    17309 Madison Ave, Lakewood OH 44107. cleveland.shambhala.org
    Sun 10am, Tue 7pm, Wed 10am. No iCal (shambhala-koeln.de server down); recurring seeded.

  - Insight Meditation Cleveland — Shaker Heights (imc_cleveland) — Vipassana
    First Unitarian Church of Cleveland, 21600 Shaker Blvd, Shaker Heights OH 44122
    Thu 7–8:30pm weekly. No iCal; recurring seeded.

  - Crooked River Zen Center (crooked_river_zen) — Soto Zen
    1813 Wilton Road, Cleveland Heights OH 44118. crookedriverzen.org
    Tue 6pm, Thu 7pm, Sun 9:30am. No iCal (site suspended); recurring seeded.

  - Cleveland Zazen Group (cleveland_zazen_group) — Zen (Kapleau/Rochester lineage)
    1813 Wilton Road, Cleveland Heights OH 44118. zencleveland.com
    Tue 7:30pm, Sun 9am. Per-event ICS only (Squarespace); recurring seeded.

  - CloudWater Zendo (cloudwater_zendo) — Chan/Zen
    4388 W Pleasant Valley Rd, Parma OH 44134. cloudwater.org
    Tue 7pm, Sun 9:30am. No iCal; recurring seeded.

Research notes (2026-05-20):
  - Cleveland Shambhala: Located in Lakewood, west of Cleveland. Three weekly sits
    confirmed via ongoing-offerings page. shambhala-koeln.de iCal (center=240) returns
    522 error — server down again. Seeding recurring sits.
  - IMC Cleveland: Multiple sitting groups across NE Ohio. Shaker Heights (Thu 7pm)
    is the main weekly group, meeting at First Unitarian Church of Cleveland. All groups
    are drop-in, no registration, no cost.
  - Crooked River Zen Center: Shares building at 1813 Wilton Rd with Cleveland Zazen
    Group — two distinct organizations at same address. Schedule confirmed via Soto Zen
    Buddhist Association directory. Main site on Bluehost suspended; Google Sites mirror
    active. Tue 6pm (two 15-min periods), Thu 7pm (two 25-min periods), Sun 9:30am (two
    30-min periods). All hybrid in-person + Google Meet.
  - Cleveland Zazen Group: 40+ year established group, Kapleau/Rochester Zen lineage.
    Tue 7:30–8:45pm and Sun 9am–11am. Squarespace site; per-event ICS only.
  - CloudWater Zendo: Chan Buddhist and Pure Land (Dragon Flower Ch'an Temples). Has
    moved locations several times; current address 4388 W Pleasant Valley Rd per Yelp
    (March 2026). Tue 7pm two periods of seated meditation; Sun 9:30am group Zen sit.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "cleveland_shambhala": Center(
        id="cleveland_shambhala",
        name="Cleveland Shambhala Meditation Center",
        url="https://cleveland.shambhala.org",
        address="17309 Madison Avenue",
        city="Cleveland",
        state="OH",
        zip_code="44107",
        lat=41.4815,
        lng=-81.8025,
        neighborhood="Lakewood",
        tradition=Tradition.TIBETAN,
        notes=(
            "The Cleveland Shambhala Meditation Center offers authentic meditation "
            "instruction rooted in the Tibetan Buddhist tradition brought to the West "
            "by Chögyam Trungpa Rinpoche. Located in the Lakewood neighborhood west of "
            "Cleveland, the center hosts three weekly open sits: Sunday Morning Sit "
            "(10–11 AM), Tuesday Evening Sit (7–8 PM), and Wednesday Morning Sit "
            "(10–11 AM). All sessions include alternating sitting and walking meditation "
            "periods. No experience required; walk-in welcome. Part of the "
            "international Shambhala community."
        ),
    ),
    "imc_cleveland": Center(
        id="imc_cleveland",
        name="Insight Meditation Cleveland",
        url="https://imcleveland.org",
        address="21600 Shaker Boulevard",
        city="Cleveland",
        state="OH",
        zip_code="44122",
        lat=41.4726,
        lng=-81.5575,
        neighborhood="Shaker Heights / First Unitarian Church",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Cleveland (IMC) offers a network of drop-in sitting "
            "groups throughout Northeast Ohio, rooted in the Theravada/Vipassana "
            "tradition. The flagship Shaker Heights group meets weekly at the First "
            "Unitarian Church of Cleveland (21600 Shaker Blvd) every Thursday "
            "7–8:30 PM. Sessions include guided sitting meditation, walking "
            "meditation, and dharma discussion. No registration required; dana "
            "(donation) based. All levels welcome."
        ),
    ),
    "crooked_river_zen": Center(
        id="crooked_river_zen",
        name="Crooked River Zen Center",
        url="https://www.crookedriverzen.org",
        address="1813 Wilton Road",
        city="Cleveland",
        state="OH",
        zip_code="44118",
        lat=41.5095,
        lng=-81.5695,
        neighborhood="Cleveland Heights",
        tradition=Tradition.ZEN,
        notes=(
            "Crooked River Zen Center is a Soto Zen community in Cleveland Heights, "
            "affiliated with the Soto Zen Buddhist Association. Teacher Sensei Dean "
            "Williams leads three weekly sits open to all: Tuesday Evening (6–7 PM, "
            "two 15-minute periods with kinhin and chanting), Thursday Evening "
            "(7–8:30 PM, two 25-minute periods with kinhin, chanting, and dharma "
            "talk), and Sunday Morning (9:30–11 AM, two 30-minute periods with "
            "kinhin, chanting, and dharma talk). All sessions available in-person "
            "and via Google Meet. No experience required; drop-in welcome."
        ),
    ),
    "cleveland_zazen_group": Center(
        id="cleveland_zazen_group",
        name="Cleveland Zazen Group",
        url="https://www.zencleveland.com",
        address="1813 Wilton Road",
        city="Cleveland",
        state="OH",
        zip_code="44118",
        lat=41.5097,
        lng=-81.5697,
        neighborhood="Cleveland Heights",
        tradition=Tradition.ZEN,
        notes=(
            "The Cleveland Zazen Group is one of Northeast Ohio's longest-standing "
            "Zen communities, with over 40 years of continuous practice. Rooted in "
            "the Rinzai–Soto lineage of Philip Kapleau and the Rochester Zen Center, "
            "the group meets twice weekly in Cleveland Heights: Tuesday Evening "
            "(7:30–8:45 PM, two rounds of zazen and kinhin, occasional chanting) and "
            "Sunday Morning (9 AM–11 AM or longer, with group instruction, dharma "
            "talks, teisho, and work practice). The group shares its space at 1813 "
            "Wilton Road with Crooked River Zen Center. Drop-in welcome; no prior "
            "experience necessary."
        ),
    ),
    "cloudwater_zendo": Center(
        id="cloudwater_zendo",
        name="CloudWater Zendo",
        url="https://cloudwater.org",
        address="4388 W Pleasant Valley Road",
        city="Cleveland",
        state="OH",
        zip_code="44134",
        lat=41.3738,
        lng=-81.7645,
        neighborhood="Parma",
        tradition=Tradition.ZEN,
        notes=(
            "CloudWater Zendo is a Chan Buddhist and Pure Land community affiliated "
            "with the Dragon Flower Ch'an Temples lineage. The zendo hosts weekly "
            "practice sessions open to all: Tuesday Evening (7 PM, two periods of "
            "seated meditation, walking meditation, chanting, and dharma talk) and "
            "Sunday Morning (9:30 AM, group Zen meditation). An introductory class "
            "is offered on the 1st and 3rd Saturday at 11 AM. All are welcome; "
            "no experience required."
        ),
    ),
}

# No live iCal feeds available for Cleveland centers (shambhala-koeln.de down;
# other sites lack machine-readable feeds). All sits seeded as recurring.
ICAL_FEEDS: dict = {}
