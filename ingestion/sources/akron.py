"""
Akron / Northeast Ohio — Phase 3 expansion.

Akron is a mid-sized Ohio metro (~700k metro, 190k city) in Summit County,
30 miles south of Cleveland. The Buddhist scene spans Theravada, Shambhala,
Soto Zen, and lay-Zen groups in the city and nearby Kent (12 mi SE) and
Cuyahoga Falls (adjacent north).

Centers included:
  - cleveland_buddhist_vihara_akron — Theravada (Sri Lankan)
    1695 Vernon Odom Blvd, Akron OH 44320
    clevelandbuddhistvihara.org · no iCal (different WP events plugin); Sunday sit seeded.
    Note: Despite "Cleveland" in the name, this center is physically located in Akron.

  - akron_canton_shambhala — Shambhala International (Vajrayana/Shambhala)
    1707 Front St, Cuyahoga Falls OH 44221 (adjacent to Akron, north)
    akron.shambhala.org · Cloudflare-blocked iCal; Tue/Wed sits seeded.

  - kent_zendo — Soto Zen (SZBA member)
    555 Franklin Ave, Kent OH 44240 (~12 mi SE of Akron)
    kentzendo.org · SSL cert expired; recurring sits seeded.

  - uu_akron_zen — Lay Zen (Steve Berg teacher)
    3300 Morewood Rd, Fairlawn OH 44333 (western Akron suburb)
    uuakron.org · UU calendar has mixed events; recurring sit seeded.

Research notes (2026-09-22):
  - Cleveland Buddhist Vihara is physically in Akron (Vernon Odom Blvd, west side).
    English-language Sunday 4–5pm guided meditation open to all. Active website,
    events page returns HTML not iCal. Weekly sit seeded as recurring.
  - Akron/Canton Shambhala: 1707 Front St, Cuyahoga Falls. Shambhala platform
    iCal blocked by Cloudflare. Tue 6:45pm + Wed 6:45pm open meditation; Sunday
    morning program also listed on site. Tue/Wed seeded.
  - Kent Zendo: kentzendo.org, SZBA member. Daily 6pm zazen Mon–Sat; Sunday
    11am instruction + zazen; last Sunday of month 9am zazenkai (half-day).
    SSL cert expired; ?ical=1 returns 301. All sits seeded as recurring.
  - UU Akron Zen Group: Steve Berg (15+ years leading weekly Zen sits), weekly
    Tuesdays 7–8:30pm in McKeeman room, 3300 Morewood Rd, Fairlawn OH.
    "No experience necessary. Anyone can come." UU calendar has mixed events;
    seeded as single recurring sit.
  - Portage Path Zendo (1150 McIntosh Ave, Akron): listed in gosit.org directory
    but no active website or current schedule found. Skipped.
  - Palyul Ohio (3750 W Streetsboro Rd, Richfield): Nyingma/Palyul Tibetan temple;
    weekly Wed/Sat/Sun sessions but schedule not publicly confirmed. Skipped.
  - It's Now Sangha (Canton): Plum Village, Wix site, no iCal, schedule unclear. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "cleveland_buddhist_vihara_akron": Center(
        id="cleveland_buddhist_vihara_akron",
        name="Cleveland Buddhist Vihara and Meditation Center",
        url="https://clevelandbuddhistvihara.org",
        address="1695 Vernon Odom Blvd",
        city="Akron",
        state="OH",
        zip_code="44320",
        lat=41.0730,
        lng=-81.5562,
        neighborhood="West Akron",
        tradition=Tradition.THERAVADA,
        notes=(
            "Cleveland Buddhist Vihara and Meditation Center is a Sri Lankan Theravada "
            "temple and practice center located in Akron's west side (despite the "
            "'Cleveland' in its name). Resident ordained monastics, regular dharma "
            "programs, and a public English-language guided meditation every Sunday "
            "4:00–5:00 PM. Open to practitioners of all backgrounds. Meditation "
            "instruction available. Free to attend. "
            "clebvihara@gmail.com. clevelandbuddhistvihara.org."
        ),
    ),
    "akron_canton_shambhala": Center(
        id="akron_canton_shambhala",
        name="Akron/Canton Shambhala Meditation Center",
        url="https://akron.shambhala.org",
        address="1707 Front Street",
        city="Cuyahoga Falls",
        state="OH",
        zip_code="44221",
        lat=41.1339,
        lng=-81.4826,
        neighborhood="Cuyahoga Falls",
        tradition=Tradition.TIBETAN,
        notes=(
            "Akron/Canton Shambhala Meditation Center is a Shambhala International "
            "center in Cuyahoga Falls, immediately north of Akron. Rooted in the "
            "Tibetan Kagyu/Nyingma lineage of Chögyam Trungpa Rinpoche. Offers open "
            "meditation Tuesday and Wednesday evenings at 6:45 PM — meditation "
            "instructor available for newcomers. All are welcome; no experience "
            "necessary. Phone: (330) 983-9019. akron.shambhala.org."
        ),
    ),
    "kent_zendo": Center(
        id="kent_zendo",
        name="Kent Zendo",
        url="http://kentzendo.org",
        address="555 Franklin Avenue",
        city="Kent",
        state="OH",
        zip_code="44240",
        lat=41.1531,
        lng=-81.3576,
        neighborhood="Kent",
        tradition=Tradition.ZEN,
        notes=(
            "Kent Zendo is a Soto Zen sitting group in Kent, Ohio (~12 miles southeast "
            "of Akron, near Kent State University). A member of the Soto Zen Buddhist "
            "Association (SZBA). Offers daily zazen Monday–Saturday evenings at 6 PM "
            "and Sunday mornings at 11 AM with sitting instruction. The last Sunday of "
            "each month is a half-day zazenkai (9 AM–3 PM). Drop-in welcome, free. "
            "kentzendo.org."
        ),
    ),
    "uu_akron_zen": Center(
        id="uu_akron_zen",
        name="Zen Meditation Group at UU Akron",
        url="https://uuakron.org/connection/zen-meditation/",
        address="3300 Morewood Road",
        city="Fairlawn",
        state="OH",
        zip_code="44333",
        lat=41.1126,
        lng=-81.6352,
        neighborhood="Fairlawn",
        tradition=Tradition.ZEN,
        notes=(
            "The Zen Meditation Group meets weekly at the Unitarian Universalist Church "
            "of Akron in Fairlawn (western Akron suburb). Led by Steve Berg, a Zen "
            "teacher with 15+ years of experience guiding weekly sits in the Akron area. "
            "Tuesdays 7:00–8:30 PM in the McKeeman room. No experience necessary — "
            "anyone is welcome. Free. uuakron.org."
        ),
    ),
}

# No live iCal feeds for this metro (all blocked or unavailable).
ICAL_FEEDS: dict = {}
EVENTBRITE_FEEDS: dict = {}
STATIC_HTML_FEEDS: dict = {}
