"""
Tucson, AZ — Phase 3 expansion (heartbeat 43 initial; heartbeat 70 expanded).

Tucson (pop. ~550k; metro ~1M), home of the University of Arizona, has a
surprisingly rich Buddhist community spanning Theravada, Zen, Tibetan, and
non-sectarian traditions.

Centers included:
  - Kadampa Meditation Center Arizona (kmc_arizona_tucson) — NKT Tibetan
    5326 E. Pima Street, Tucson AZ 85712
    Recurring sits: Sun 10am, Tue 6:30pm, Sat 10am
    Wix site — no accessible iCal; sits seeded as recurring.

  - Insight Meditation Tucson (insight_meditation_tucson) — Theravada/Vipassana
    Pima Friends Meeting House, 931 N Fifth Ave, Tucson AZ 85705
    Recurring sit: Thu 6pm (in-person + Zoom drop-in)
    Squarespace site — no iCal; sits seeded as recurring.

  - Tucson Community Meditation Center (tcmc_tucson) — Non-sectarian/Vipassana
    1147 N Howard Blvd, Tucson AZ 85705
    Recurring sits: Mon 6pm, Tue 5pm, Wed 6pm (all hybrid)
    Custom site — no iCal; sits seeded as recurring.

  - Zen Desert Sangha (zen_desert_sangha_tucson) — Zen (Diamond Sangha lineage)
    3226 N Martin Ave, Tucson AZ 85712
    Recurring sits: Mon/Wed 6:30pm, Sat 7:30am, Sun 5pm
    No iCal; sits seeded as recurring.

  - Awam Tibetan Buddhist Institute (awam_tbi_tucson) — Tibetan/Nyingma Dzogchen
    301B N Longfellow Ave, Tucson AZ 85711
    Recurring sits: Sun 9:30am (Zoom + YouTube), Wed 6pm
    Wix site — no iCal; sits seeded as recurring.

  - Desert Rain Zen (desert_rain_zen_tucson) — Zen
    Little Chapel of All Nations, 1401 E First Street, Tucson AZ 85719 (UA campus)
    Recurring sit: Thu 6:30pm (hybrid)
    No iCal; sits seeded as recurring.

Research notes (2026-05-27):
  - KMC Arizona: NKT-IKBU, Midtown Tucson. Wix site, no ?ical=1.
    Confirmed schedule: Sun 10am "New Mind, New World" (75 min),
    Tue 6:30pm class (75 min), Sat 10am "Simply Meditate" (30 min).
  - Insight Meditation Tucson (IMT): Theravada/Vipassana. Pima Friends Meeting House.
    Thu drop-in 6–7:45pm: guided meditation + dharma talk + discussion. Hybrid.
    Also 1st Monday 5:30pm beginner drop-in. Squarespace, no iCal.
    Contact: insightmeditationtucson@gmail.com
  - Tucson Community Meditation Center (TCMC): Non-sectarian vipassana, founded 1984.
    1147 N Howard Blvd. Mon 6pm "Meditating in Community" (hybrid), Tue 5pm
    peer-led silent sit (in-person), Wed 6pm Mindfulness & Loving Kindness (hybrid).
    Also Thu 6pm Heart of Recovery and 1st Sun 8:30am "Mindfulness for Everyone!"
  - Zen Desert Sangha: Diamond Sangha (Robert Aitken) lineage. 3226 N Martin Ave
    (north of Fort Lowell, west of Campbell). Mon & Wed 6:30–8pm zazen (in-person).
    Sat 7:30am–10:30am full sitting schedule. Sun 5–6:30pm. Very drop-in friendly.
    zds@zendesertsangha.org | (520) 319-6260.
  - Awam Tibetan Buddhist Institute: Nyingma Dzogchen. Founded by Venerable Lobsang
    Palden. 301B N Longfellow Ave. Sun 9:30am in-depth teachings (Zoom+YouTube),
    11am practices. Wed 6–6:30pm mindfulness. Active YouTube channel.
    info@AwamInstitute.org | 520-622-8460.
  - Desert Rain Zen: Harada-Yasutani Zen lineage. Meets at UA's Little Chapel of
    All Nations (1401 E First St). Thu 6:30–7:30pm guided meditation (hybrid).
    Sun 3:30–5pm zazen + koan (Zoom); Tue 5:30pm study group (Zoom).
    Contact: desertrainzen@gmail.com. Beginner-friendly.
  - Tucson Shambhala: redirects to main shambhala.org — appears inactive or closed.
  - Rincon Mountain Insight Meditation / Tucson Insight: domains dead — dormant.
  - Old Pueblo Zen: domain dead — no active web presence found.
  - Diamond Way Tucson: domain dead; no AZ centers in global Diamond Way directory.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_arizona_tucson": Center(
        id="kmc_arizona_tucson",
        name="Kadampa Meditation Center Arizona",
        url="https://www.meditationintucson.org",
        address="5326 East Pima Street",
        city="Tucson",
        state="AZ",
        zip_code="85712",
        lat=32.2432,
        lng=-110.8789,
        neighborhood="Midtown / East Tucson",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Arizona (KMC Arizona) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located in Midtown Tucson. Offers weekly "
            "General Program meditation classes open to all: Sunday morning, Tuesday evening, "
            "and a brief Saturday morning drop-in. Classes include guided meditation and "
            "dharma teaching on modern Kadampa Buddhism. No experience necessary; "
            "all are welcome."
        ),
    ),
    "insight_meditation_tucson": Center(
        id="insight_meditation_tucson",
        name="Insight Meditation Tucson",
        url="https://www.insightmeditationtucson.org",
        address="931 North Fifth Avenue",
        city="Tucson",
        state="AZ",
        zip_code="85705",
        lat=32.2282,
        lng=-110.9741,
        neighborhood="Armory Park / Barrio Historico",
        tradition=Tradition.THERAVADA,
        notes=(
            "Insight Meditation Tucson (IMT) is a Theravada/Vipassana community offering "
            "weekly drop-in sits at the Pima Friends Meeting House (931 N Fifth Ave). "
            "Thursday evenings 6:00–7:45pm: guided meditation, dharma talk, and group "
            "discussion — in-person and Zoom. Beginner-friendly; no registration needed. "
            "Also offers a 1st Monday beginner drop-in (5:30–6:30pm) and weekday morning "
            "Zoom sits (Mon–Fri 7:00–7:30am). insightmeditationtucson.org."
        ),
    ),
    "tcmc_tucson": Center(
        id="tcmc_tucson",
        name="Tucson Community Meditation Center",
        url="https://tucsonmeditation.org",
        address="1147 North Howard Boulevard",
        city="Tucson",
        state="AZ",
        zip_code="85705",
        lat=32.2337,
        lng=-110.9734,
        neighborhood="Midtown Tucson",
        tradition=Tradition.THERAVADA,
        notes=(
            "Tucson Community Meditation Center (TCMC) is a non-sectarian Vipassana "
            "community founded in 1984, one of the oldest meditation centers in Tucson. "
            "Offers multiple weekly sits at 1147 N Howard Blvd: Monday 6–7:20pm "
            "'Meditating in Community' (hybrid), Tuesday 5–5:55pm peer-led silent sit "
            "(in-person), and Wednesday 6–7pm Mindfulness & Loving Kindness (hybrid). "
            "Also Thursday 6pm Heart of Recovery, and 1st Sunday 8:30–9:30am drop-in. "
            "Drop-in welcome; dana-based. tucsonmeditation.org."
        ),
    ),
    "zen_desert_sangha_tucson": Center(
        id="zen_desert_sangha_tucson",
        name="Zen Desert Sangha",
        url="https://www.zendesertsangha.org",
        address="3226 North Martin Avenue",
        city="Tucson",
        state="AZ",
        zip_code="85712",
        lat=32.2591,
        lng=-110.9232,
        neighborhood="Richland Heights",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Desert Sangha is a Zen community in the Diamond Sangha lineage "
            "(Robert Aitken Roshi), practicing Rinzai-style koan Zen in Tucson. "
            "3226 N Martin Ave (half block north of Fort Lowell, one block west of "
            "Campbell). Monday and Wednesday evenings 6:30–8pm: zazen (sitting + "
            "walking), open to all. Saturday mornings: tea at 7:25am, zazen 7:30–8:30am, "
            "samu 8:30–9am, chanting 9–9:30am, zazen 9:30–10:30am (also on Zoom). "
            "Sunday 5–6:30pm sitting. All are welcome; no advance contact needed. "
            "zendesertsangha.org | zds@zendesertsangha.org."
        ),
    ),
    "awam_tbi_tucson": Center(
        id="awam_tbi_tucson",
        name="Awam Tibetan Buddhist Institute",
        url="https://www.awaminstitute.org",
        address="301B North Longfellow Avenue",
        city="Tucson",
        state="AZ",
        zip_code="85711",
        lat=32.2362,
        lng=-110.9042,
        neighborhood="Midtown Tucson",
        tradition=Tradition.TIBETAN,
        notes=(
            "Awam Tibetan Buddhist Institute is a Nyingma Dzogchen center in Tucson, "
            "founded by Venerable Khenchen Tsewang Rigdzin Rinpoche and directed by "
            "Lama Lobsang Palden. Offers regular public programs including Sunday morning "
            "in-depth teachings (9:30–10:30am, Zoom + YouTube) and Wednesday evening "
            "mindfulness practice (6:00–6:30pm). Active YouTube channel with hundreds of "
            "teachings. info@AwamInstitute.org | 520-622-8460. awaminstitute.org."
        ),
    ),
    "desert_rain_zen_tucson": Center(
        id="desert_rain_zen_tucson",
        name="Desert Rain Zen",
        url="https://www.desertrainzen.org",
        address="1401 East First Street",
        city="Tucson",
        state="AZ",
        zip_code="85719",
        lat=32.2253,
        lng=-110.9459,
        neighborhood="University of Arizona Campus",
        tradition=Tradition.ZEN,
        notes=(
            "Desert Rain Zen is a Zen meditation group meeting at the Little Chapel of "
            "All Nations on the University of Arizona campus (1401 E First St). "
            "Thursday evenings 6:30–7:30pm: guided meditation, hybrid in-person + Zoom. "
            "Sunday 3:30–5pm: zazen and koan conversation (Zoom). Beginner-friendly; "
            "all are welcome. Contact desertrainzen@gmail.com for Zoom links. "
            "Harada-Yasutani Zen lineage. desertrainzen.org."
        ),
    ),
}

# No iCal feeds — all Tucson centers use Wix, Squarespace, or no calendar system
ICAL_FEEDS = {}
