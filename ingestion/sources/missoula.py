"""
Missoula, MT — Phase 3 expansion.

Missoula (~80k city, ~120k metro) is a university town in western Montana,
home to the University of Montana. Despite its modest size, it supports a
surprisingly active Buddhist community spanning Zen, Tibetan, and non-sectarian
traditions — reflecting Montana's contemplative culture and academic environment.

Centers included:
  - Open Way Sangha (open_way_sangha) — Vietnamese Zen / Plum Village (Thich Nhat Hanh)
    702 Brooks St, Missoula MT 59801. openway.org
    Tue 7–9pm + Sat 10am–noon. No iCal (Squarespace); seeded recurring sits.

  - Osel Shen Phen Ling (osel_shen_phen_ling) — Tibetan Buddhist, Gelug (FPMT)
    500 N Higgins Ave, Suite 208A, Missoula MT 59802. fpmtosel.wordpress.com
    Mon 7pm (~1h guided meditation). No iCal; seeded recurring sits.

  - Rocky Mountain Buddhist Center (rocky_mountain_bc) — Triratna Buddhist Community
    540 South 2nd West, Missoula MT 59801. rockymountainbuddhistcenter.org
    Wed 7–9pm Sangha Night. Note: Sangha Night requires completing their
    5-week Intro to Meditation and Buddhism course first. No iCal; seeded.

Research notes (2026-05-24):
  - Open Way Sangha: Plum Village lineage (Thich Nhat Hanh). Founded in Missoula
    in the 1990s. Rotating monthly format: dharma talk + sharing, sutra service,
    Mindfulness Trainings recitation, tea ceremony, special programs. Drop-in welcome.
  - Osel Shen Phen Ling: FPMT center established 1986, one of Montana's oldest
    Buddhist organizations. Monday 7pm guided meditation (~30 min shamatha +
    brief prayers/motivations). Free intro course on Tuesdays (fall). Drop-in
    Mondays require no experience.
  - Rocky Mountain Buddhist Center: Triratna lineage (founded by Sangharakshita).
    Located near UM campus. Sangha Night (Wed 7–9pm) teaches Mindfulness of
    Breathing and Metta Bhavana practices. Requires 5-week intro course first.
  - Big Sky Mind (Kagyu): 1st Monday monthly + weekly group requires email signup
    for Zoom link; schedule unconfirmed. Deferred.
  - Ewam Sang-ngag Ling (Nyingma): JS-rendered calendar, structured courses only;
    no confirmed drop-in sit schedule. Deferred.
  - Vipassana Montana: Bozeman-based, Zoom-only for Missoula. Skip.
  - No active Shambhala center found in Missoula.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "open_way_sangha": Center(
        id="open_way_sangha",
        name="Open Way Sangha",
        url="https://www.openway.org",
        address="702 Brooks St",
        city="Missoula",
        state="MT",
        zip_code="59801",
        lat=46.8533,
        lng=-114.0078,
        neighborhood="South Missoula",
        tradition=Tradition.ZEN,
        notes=(
            "Open Way Sangha is a Vietnamese Zen / Plum Village community (Thich Nhat Hanh "
            "lineage) meeting at 702 Brooks St, Missoula MT. Founded in the 1990s. Regular "
            "schedule: Tuesdays 7:00–9:00pm and Saturdays 10:00am–12:00pm. Monthly format "
            "rotates: dharma talk + sharing; meditation + sutra service; Mindfulness "
            "Trainings recitation; tea ceremony; special programs. All are welcome — 'new "
            "people are always welcome.' Dana-based. Contact openwaysangha@gmail.com."
        ),
    ),
    "osel_shen_phen_ling": Center(
        id="osel_shen_phen_ling",
        name="Osel Shen Phen Ling",
        url="https://fpmtosel.wordpress.com",
        address="500 N Higgins Ave, Suite 208A",
        city="Missoula",
        state="MT",
        zip_code="59802",
        lat=46.8723,
        lng=-113.9940,
        neighborhood="Downtown Missoula",
        tradition=Tradition.TIBETAN,
        notes=(
            "Osel Shen Phen Ling is an FPMT (Foundation for the Preservation of the "
            "Mahayana Tradition) Gelug Tibetan Buddhist center established in Missoula "
            "in 1986 — one of Montana's oldest Buddhist organizations. Located at 500 N "
            "Higgins Ave, Suite 208A (gompa on Higgins Ave). Monday 7:00pm: weekly group "
            "guided meditation (~30 minutes shamatha stabilizing meditation with brief "
            "prayers and motivations). No experience necessary; drop-in welcome. Free. "
            "Contact oselshenphenling@gmail.com or 406-327-1204."
        ),
    ),
    "rocky_mountain_bc": Center(
        id="rocky_mountain_bc",
        name="Rocky Mountain Buddhist Center",
        url="http://rockymountainbuddhistcenter.org",
        address="540 South 2nd West",
        city="Missoula",
        state="MT",
        zip_code="59801",
        lat=46.8645,
        lng=-114.0120,
        neighborhood="University District",
        tradition=Tradition.OTHER,
        notes=(
            "Rocky Mountain Buddhist Center is part of the Triratna Buddhist Community "
            "(formerly Friends of the Western Buddhist Order / FWBO), located near the "
            "University of Montana campus. Founded by UM Asian Studies professor Alan "
            "Sponburg. Wednesday Sangha Night 7:00–9:00pm: teaches Mindfulness of "
            "Breathing and Metta Bhavana practices. Note: Sangha Night is open to those "
            "who have completed their 5-week Introduction to Meditation and Buddhism "
            "course first. The intro course runs periodically. Contact: "
            "fwbomissoula@gmail.com."
        ),
    ),
}

# No live iCal feeds available for Missoula centers — all seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
