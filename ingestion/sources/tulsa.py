"""
Tulsa, OK — Phase 3 expansion.

Tulsa (~400k metro) has a small but active contemplative community anchored by
two long-running weekly groups at All Souls Unitarian Church plus a monthly Zen
day-retreat program at the Osage Forest of Peace retreat center in adjacent
Sand Springs.

Centers included:
  - Tulsa Zen Center (tulsa_zen_center)
    — Soto/Rinzai Zen
    5001 S Fulton Ave, Tulsa OK 74135 (All Souls Unitarian Church)
    tulsazencenter.com — Sunday 8:30–10:00 AM weekly sit
    No iCal (GoDaddy builder); recurring sit seeded.

  - Tulsa Shambhala Meditation Group (tulsa_shambhala)
    — Shambhala / Tibetan-influenced (Chogyam Trungpa lineage)
    tulsa.shambhala.org — Tue 6:30–7:30 PM in-person + 1st Sunday Open House
    iCal blocked (403 Cloudflare); recurring sits seeded.

  - Tulsa Zen Sangha (tulsa_zen_sangha)
    — Rinzai/Soto Zen; guiding teacher Helen Cortes (Maria Kannon Zen Center)
    Osage Forest of Peace, Sand Springs OK (just west of Tulsa)
    3rd Saturday monthly zazenkai (6:30am–3:30pm)
    2nd Sunday monthly afternoon sit (2:30–4:00pm)
    No iCal; recurring sits seeded.

Research notes (2026-10-01):
  - Tulsa Zen Center: GoDaddy website, no calendar plugin. Sunday public sit at
    All Souls UU Church (5001 S Fulton Ave). Newcomers arrive 8:15 AM. Instructors
    Patti Mitchell (Soto, Suzuki lineage) and Michael Mason (Harada-Yasutani).
    Free/donations. Confirmed active through 2026.
  - Tulsa Shambhala: WordPress Shambhala platform at tulsa.shambhala.org; iCal
    endpoint returns 403 (Cloudflare). Tuesday Open Meditation 6:30-7:30 PM
    in-person (Zoom available on 1hr notice). Wednesday noon is Zoom-only (skip).
    1st Sunday monthly Open House 10am-noon (in-person). 2nd Saturday monthly
    half-day Nyinthun 9am-1pm seeded as well.
  - Tulsa Zen Sangha: tulsazensangha.wordpress.com; affiliated with Maria Kannon
    Zen Center (Dallas). Holds all-day zazenkai (3rd Saturday) and afternoon sits
    (2nd Sunday) at Osage Forest of Peace retreat center, Sand Springs OK (~10 mi
    west of downtown Tulsa). $30 registration for day events; afternoon sit free.
  - Shining Window Zen: Living Vow Zen lineage, Zoom-only — skipped.
  - Bodhicharya Oklahoma (Karma Kagyu): website down, status uncertain — deferred.
  - Middle Path Group: website down, appears defunct — skipped.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "tulsa_zen_center": Center(
        id="tulsa_zen_center",
        name="Tulsa Zen Center",
        url="https://tulsazencenter.com",
        address="5001 S Fulton Ave",
        city="Tulsa",
        state="OK",
        zip_code="74135",
        lat=36.0900,
        lng=-95.9350,
        neighborhood="South Tulsa (All Souls Unitarian Church)",
        tradition=Tradition.ZEN,
        notes=(
            "Tulsa Zen Center is a lay-led Zen community that has gathered in Tulsa "
            "for many years. It draws from both Soto (Shunryu Suzuki lineage, Patti "
            "Mitchell) and Rinzai/Harada-Yasutani (Michael Mason) Zen traditions. "
            "Weekly Sunday morning sit 8:30–10:00 AM at All Souls Unitarian Church "
            "(5001 S Fulton Ave). Newcomers welcome — arrive 8:15 AM for brief "
            "orientation. Includes sitting meditation, walking meditation, and dharma "
            "discussion. Free; dana/donations appreciated. tulsazencenter.com."
        ),
    ),
    "tulsa_shambhala": Center(
        id="tulsa_shambhala",
        name="Tulsa Shambhala Meditation Group",
        url="https://tulsa.shambhala.org",
        address="5001 S Fulton Ave",
        city="Tulsa",
        state="OK",
        zip_code="74135",
        lat=36.0900,
        lng=-95.9350,
        neighborhood="South Tulsa (All Souls Unitarian Church)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Tulsa Shambhala Meditation Group is an affiliate of Shambhala "
            "International (Chogyam Trungpa Rinpoche lineage) offering secular "
            "mindfulness and Tibetan-inspired meditation practice in Tulsa. "
            "Weekly Tuesday Open Meditation 6:30–7:30 PM in-person (Zoom also "
            "available with 1-hour advance request). Monthly events include: "
            "1st Sunday Open House 10 AM–noon (meditation instruction + community "
            "tea) and 2nd Saturday half-day Nyinthun practice 9 AM–1 PM. All "
            "are welcome regardless of background or experience. "
            "shambhalatulsa@gmail.com. (918) 694-9233. tulsa.shambhala.org."
        ),
    ),
    "tulsa_zen_sangha": Center(
        id="tulsa_zen_sangha",
        name="Tulsa Zen Sangha",
        url="https://tulsazensangha.wordpress.com",
        address="18275 W Hwy 51",
        city="Sand Springs",
        state="OK",
        zip_code="74063",
        lat=36.1396,
        lng=-96.1096,
        neighborhood="Osage Forest of Peace, Sand Springs (west of Tulsa)",
        tradition=Tradition.ZEN,
        notes=(
            "Tulsa Zen Sangha is a Rinzai/Soto Zen group guided by Helen Cortes, "
            "a teacher in the Maria Kannon Zen Center lineage (Dallas). The sangha "
            "meets monthly at the Osage Forest of Peace retreat center in Sand "
            "Springs, about 10 miles west of downtown Tulsa. Third Saturday monthly "
            "all-day Zazenkai 6:30 AM–3:30 PM (registration $30). Second Sunday "
            "monthly afternoon Forest Sit 2:30–4:00 PM (free; beginner instruction "
            "available). Contact via tulsazensangha.wordpress.com for details and "
            "directions. forestofpeace.org."
        ),
    ),
}

# No live iCal feeds extractable for Tulsa centers —
# all sits seeded as recurring in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
