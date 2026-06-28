"""
Dallas / Fort Worth, Texas — Phase 3 expansion (heartbeat 82).

Dallas–Fort Worth (pop. ~1.3M city / ~7.8M metro) is the fourth-largest
metro in the US. Its Buddhist community spans NKT Tibetan, Zen, Kagyu
Tibetan, Shambhala, and Plum Village traditions spread across Dallas,
Irving, and Richardson.

Centers included:
  - KMC Texas / Kadampa Meditation Center Texas (kmc_texas)
    NKT Tibetan (New Kadampa Tradition)
    1875 Laws St, Dallas TX 75207 (West End / near Dallas Aquarium)
    meditationintexas.org · Sun 11am, Tue 7pm, Thu 7pm
    Squarespace site — no iCal. Seeded as recurring.

  - Maria Kannon Zen Center (maria_kannon_zen_dallas)
    Soto Zen (ecumenical)
    1450 Old Gate Lane (White Rock UMC, 2nd floor), Dallas TX 75218
    mkzc.org · Mon 12pm + Mon 7:30pm + Wed 7:30pm + Sat 10:30am (hybrid)
    Squarespace site — no iCal. Seeded as recurring.

  - Dallas Shambhala Meditation Center (shambhala_dallas)
    Shambhala (Kagyu/Nyingma-influenced contemplative tradition)
    13140 Coit Rd Suite 117, Dallas TX 75240 (Far North Dallas)
    dallas.shambhala.org · Sun 10am + Tue 7pm in-person
    No iCal (Cologne server offline). Seeded as recurring.

  - Dallas Karma Thegsum Choling / KTC Dallas (ktc_dallas)
    Kagyu Tibetan (Karma Triyana Dharmachakra lineage)
    1000 Armeda Ave, Irving TX 75061
    ktcdallas.org · Sun 9:30am–1pm in-person (free intro meditation 9:30–10:30am)
    No iCal — seeded as recurring.

  - Dallas Meditation Center (dallas_meditation_center)
    Plum Village / Thich Nhat Hanh tradition
    810 W. Arapaho Rd Suite 98, Richardson TX 75080
    dallasmeditationcenter.com · Mon–Thu 12pm in-person (Zen-to-Go, 45 min)
    No iCal — seeded as recurring.

Research notes (2026-06-28):
  - KMC Texas: Major NKT center in downtown Dallas (West End neighborhood, 8,500 sq ft
    Temple). Drop-in classes suitable for beginners and experienced practitioners.
    Sun 11am (English + Spanish), Tue 7pm, Thu 7pm. Also runs satellite classes Mon
    (Fort Worth + Plano), Tue (McKinney), Wed (Denton). meditationintexas.org.
  - Maria Kannon Zen Center: Soto Zen center at White Rock UMC, NE Dallas.
    Describes itself as an "ecumenical haven of diverse meditation forms."
    In-person zendo sessions: Mon 12pm (lunch sit), Mon 7:30pm, Wed 7:30pm, Sat 10:30am.
    All hybrid (zendo + Zoom). Tue/Thu 6am Zoom-only — skipped (online only). mkzc.org.
  - Dallas Shambhala: Located at 13140 Coit Rd Suite 117 in Far North Dallas.
    Weekly public meditation Sun mornings (meditation instruction + dharma talk)
    and Tue evenings. Shambhala Cologne server offline (503) for Dallas. Manual seed.
    dallas.shambhala.org.
  - KTC Dallas: Karma Kagyu Tibetan center in Irving (Dallas suburb). Founded 1984
    by Khenpo Karthar Rinpoche. Open Sundays 9:30am–1pm: free intro meditation class
    9:30–10:30am, then dharma teachings. Led by Lama Dudjom Dorjee. ktcdallas.org.
  - Dallas Meditation Center: Plum Village-inspired mindfulness center in Richardson
    (north Dallas suburb). "Zen-to-Go" weekday noon sits (Mon–Thu 12–12:45pm in-person
    at their studio). Also Mon 7:30pm online. dallasmeditationcenter.com.
  - Fort Worth Zendo: Affiliated with Maria Kannon Zen Center; email-required for
    first visit (admin@fortworthzendo.org). No confirmed public address or schedule
    online. Deferred.
  - 3 Jewels Sangha (Fort Worth): Early-stage group, primarily Zoom. Deferred.
  - DFW Buddhist Vihara (Fort Worth): Sri Lankan Theravada temple, monthly retreats
    only — not drop-in. Skip.
  - Dallas Insight Sangha: In transition (no permanent physical location as of 2026).
    Online-only (Thu 7pm + Sun 9am). Deferred until they find a physical home.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_texas": Center(
        id="kmc_texas",
        name="Kadampa Meditation Center Texas",
        url="https://www.meditationintexas.org",
        address="1875 Laws St",
        city="Dallas",
        state="TX",
        zip_code="75207",
        lat=32.7820,
        lng=-96.8093,
        neighborhood="West End",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Texas (KMC Texas) is a major New Kadampa "
            "Tradition (NKT) center in the heart of downtown Dallas, housed in an "
            "8,500 sq ft Temple near the Dallas Aquarium. Classes include guided "
            "meditation and Buddhist teachings designed for all experience levels — "
            "each class stands alone, making drop-in easy. Weekly public sits: "
            "Sunday 11am (in English and Spanish), Tuesday 7pm, and Thursday 7pm. "
            "Also runs satellite classes Mon (Fort Worth + Plano), Tue (McKinney), "
            "Wed (Denton). Free introductory sessions available. "
            "1875 Laws St, Dallas TX 75207. meditationintexas.org."
        ),
    ),
    "maria_kannon_zen_dallas": Center(
        id="maria_kannon_zen_dallas",
        name="Maria Kannon Zen Center",
        url="https://www.mkzc.org",
        address="1450 Old Gate Lane",
        city="Dallas",
        state="TX",
        zip_code="75218",
        lat=32.8333,
        lng=-96.7108,
        neighborhood="White Rock",
        tradition=Tradition.ZEN,
        notes=(
            "Maria Kannon Zen Center is a Soto Zen center in northeast Dallas, "
            "meeting on the second floor of White Rock United Methodist Church. "
            "The center's primary commitment is offering Zen meditation practice "
            "while welcoming diverse meditation traditions. Weekly in-person/hybrid "
            "sessions: Monday noon zazen (12–1pm), Monday evening (7:30–9pm), "
            "Wednesday evening (7:30–9pm), and Saturday morning (10:30am–noon). "
            "Tuesday and Thursday 6am sessions are Zoom-only. "
            "1450 Old Gate Lane, Rooms 200–201, Dallas TX 75218. "
            "214-388-1122 · mkzc.org."
        ),
    ),
    "shambhala_dallas": Center(
        id="shambhala_dallas",
        name="Dallas Shambhala Meditation Center",
        url="https://dallas.shambhala.org",
        address="13140 Coit Rd Suite 117",
        city="Dallas",
        state="TX",
        zip_code="75240",
        lat=32.9344,
        lng=-96.7818,
        neighborhood="Far North Dallas",
        tradition=Tradition.TIBETAN,
        notes=(
            "Dallas Shambhala Meditation Center offers weekly public meditation "
            "rooted in the Chögyam Trungpa Rinpoche lineage and the Kagyu and "
            "Nyingma Buddhist traditions. Meditation instruction is available free "
            "of charge every Sunday morning (meditation + dharma talk) and Tuesday "
            "evening. Programs focus on making meditation a practical path for daily "
            "life and social transformation. "
            "13140 Coit Rd Suite 117, Dallas TX 75240. dallas.shambhala.org."
        ),
    ),
    "ktc_dallas": Center(
        id="ktc_dallas",
        name="KTC Dallas — Karma Thegsum Choling",
        url="https://www.ktcdallas.org",
        address="1000 Armeda Ave",
        city="Irving",
        state="TX",
        zip_code="75061",
        lat=32.8187,
        lng=-96.9625,
        neighborhood="Irving",
        tradition=Tradition.TIBETAN,
        notes=(
            "Dallas Karma Thegsum Choling (KTC Dallas) is a Kagyu Tibetan Buddhist "
            "center in Irving, Texas (Dallas suburb), founded in 1984 by the late "
            "Khenpo Karthar Rinpoche, abbot of Karma Triyana Dharmachakra (KTD) "
            "in Woodstock, NY. Open every Sunday 9:30am–1pm: free introduction to "
            "Buddhism and meditation class (9:30–10:30am) taught by Lama Dudjom "
            "Dorjee, followed by dharma teachings. Third Saturday of each month: "
            "Introduction to Buddhism class with meditation instructions. "
            "1000 Armeda Ave, Irving TX 75061. ktcdallas.org."
        ),
    ),
    "dallas_meditation_center": Center(
        id="dallas_meditation_center",
        name="Dallas Meditation Center",
        url="https://dallasmeditationcenter.com",
        address="810 W Arapaho Rd Suite 98",
        city="Richardson",
        state="TX",
        zip_code="75080",
        lat=32.9777,
        lng=-96.7303,
        neighborhood="Richardson",
        tradition=Tradition.ZEN,
        notes=(
            "Dallas Meditation Center is a mindfulness community in Richardson "
            "(north Dallas suburb) inspired by Thich Nhat Hanh's Plum Village "
            "tradition. Offers 'Zen-to-Go,' a gentle weekday noon sit "
            "(Monday–Thursday 12:00–12:45pm in-person) as a midday pause open to "
            "all levels. Monday evening 7:30–9pm session is online. Practice "
            "includes sitting meditation, walking meditation, dharma discussion, "
            "and Plum Village chanting. Drop-in, pay-what-you-can. "
            "810 W. Arapaho Rd Suite 98, Richardson TX 75080. "
            "dallasmeditationcenter.com."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------
# All Dallas/Fort Worth centers use recurring sits seeded via
# scripts/sangha-seed-recurring.js — no live iCal feeds available.

ICAL_FEEDS: dict = {}
