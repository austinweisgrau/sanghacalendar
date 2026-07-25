"""
Columbia, South Carolina — Phase 3 expansion (heartbeat 91).

Columbia (pop. ~840k metro, state capital, home of USC) has a modest but
steady Buddhist meditation scene spanning Kadampa, Soto Zen, and Tibetan
Gelug traditions.

Centers included:
  - KMC South Carolina (kmc_sc_columbia)
    Kadampa (New Kadampa Tradition / NKT-IKBU)
    2000 Park Street Suite 103, Columbia SC 29201
    meditationinsouthcarolina.org · Sun 10:30am, Wed 6:30pm
    → No iCal; seeded as recurring in sangha-seed-recurring.js

  - Columbia Zen Buddhist Priory (columbia_zen_priory)
    Soto Zen (Order of Buddhist Contemplatives / Shasta Abbey lineage)
    426 Arrowwood Road, Columbia SC 29210
    columbiazen.org · Sun 9:30am, Wed 6:30pm
    → No iCal; seeded as recurring in sangha-seed-recurring.js

  - SC Dharma Group (sc_dharma_group)
    Tibetan Buddhist (Gelug; endorsed by H.H. the Dalai Lama)
    3003 Columbia Ave, Columbia SC 29201
    scdharma.org · Sun 9:15am in-person + 10am Zoom teachings
    → No iCal; Sunday morning in-person sit seeded as recurring

Research notes (2026-07-25):
  - KMC South Carolina: NKT Kadampa center at 2000 Park St Suite 103 (enter
    and park from Calhoun Street). Founded 2002. Resident Teacher Kelsang
    Jangchen. Sunday 10:30–11:45am and Wednesday 6:30–7:45pm drop-in classes.
    Each class: guided breathing meditation, dharma teaching, second meditation.
    Drop-in $15; series $75; free for members. No Greenville branch conflicts —
    Greenville is a separate branch class at UU Fellowship; this is the main
    Columbia center. meditationinsouthcarolina.org / (803) 200-2115.
  - Columbia Zen Buddhist Priory: OBC (Order of Buddhist Contemplatives, Shasta
    Abbey lineage), Soto Zen. 426 Arrowwood Rd, Columbia SC 29210. Prior is
    Rev. Rokuzan Kroenke, Dharma Heir of Rev. Master Jiyu-Kennett. Sunday
    9:30am–~11:30am (two periods of meditation + morning service + Dharma talk);
    Wednesday 6:30–8:15pm (meditation + services + Dharma talk). Friday 6pm =
    newcomer orientation (required before attending regular sits). 2nd Saturday
    9am–noon Work Day. First-timers should call before visiting. columbiazen.org /
    (803) 772-7552.
  - SC Dharma Group: Tibetan Buddhist (Gelug tradition, H.H. Dalai Lama
    endorsed). Spiritual director Geshe Dakpa Topgyal based in Charleston.
    3003 Columbia Ave, Columbia SC 29201 (Earlewood neighborhood; meditation
    building behind main house). Sunday program: in-person meditation at 9:15am,
    followed by Zoom teachings at 10am with Geshe Dakpa Topgyal via TV/Zoom.
    Tuesday Zoom dharma discussion (contact-based). Drop-in, free, open to all.
    scdharma.org / (803) 467-7759 / scdharma@gmail.com.
  - Insight Meditation Community of Columbia (IMCC): website down
    (insightmeditationcolumbia.org returns ECONNREFUSED). Possibly dormant
    post-COVID. Deferred until site recovers.
  - No Shambhala center confirmed in Columbia SC.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kmc_sc_columbia": Center(
        id="kmc_sc_columbia",
        name="Kadampa Meditation Center South Carolina",
        url="https://meditationinsouthcarolina.org",
        address="2000 Park Street, Suite 103",
        city="Columbia",
        state="SC",
        zip_code="29201",
        lat=34.0019,
        lng=-81.0347,
        neighborhood="Five Points",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center South Carolina is a Tibetan Buddhist "
            "(New Kadampa Tradition / NKT-IKBU) center at 2000 Park Street "
            "Suite 103, Columbia SC 29201 (enter and park from Calhoun Street). "
            "Founded 2002. Resident Teacher: Kelsang Jangchen. "
            "Sunday 10:30–11:45am and Wednesday 6:30–7:45pm drop-in meditation "
            "classes. Each self-contained class includes guided breathing "
            "meditation, a dharma teaching, and a second meditation — suitable "
            "for complete beginners. Drop-in $15; series $75; free for members. "
            "meditationinsouthcarolina.org. (803) 200-2115."
        ),
    ),
    "columbia_zen_priory": Center(
        id="columbia_zen_priory",
        name="Columbia Zen Buddhist Priory",
        url="https://columbiazen.org",
        address="426 Arrowwood Road",
        city="Columbia",
        state="SC",
        zip_code="29210",
        lat=34.0264,
        lng=-81.0997,
        neighborhood="West Columbia",
        tradition=Tradition.ZEN,
        notes=(
            "Columbia Zen Buddhist Priory is a Soto Zen temple in the Order "
            "of Buddhist Contemplatives (Shasta Abbey lineage), 426 Arrowwood "
            "Road, Columbia SC 29210. Prior: Rev. Rokuzan Kroenke, Dharma Heir "
            "of Rev. Master Jiyu-Kennett. Sunday 9:30am–~11:30am (two periods "
            "of sitting meditation, morning service, and Dharma talk); "
            "Wednesday 6:30–8:15pm (meditation, services, Dharma talk). "
            "Friday 6pm newcomer orientation is required before attending "
            "regular sessions — please call ahead: (803) 772-7552. "
            "columbiazen.org."
        ),
    ),
    "sc_dharma_group": Center(
        id="sc_dharma_group",
        name="SC Dharma Group",
        url="https://www.scdharma.org",
        address="3003 Columbia Avenue",
        city="Columbia",
        state="SC",
        zip_code="29201",
        lat=34.0145,
        lng=-81.0478,
        neighborhood="Earlewood",
        tradition=Tradition.TIBETAN,
        notes=(
            "SC Dharma Group is a Tibetan Buddhist center (Gelug tradition, "
            "endorsed by H.H. the Dalai Lama) at 3003 Columbia Avenue, Columbia "
            "SC 29201 (Earlewood neighborhood; the meditation room is in the "
            "building behind the main house). Spiritual director: Geshe Dakpa "
            "Topgyal (based in Charleston). Sunday program: in-person sitting "
            "meditation 9:15am, followed by dharma teachings via Zoom/TV at "
            "10:00am with Geshe Dakpa Topgyal. Drop-in, free, open to all "
            "backgrounds. Tuesday Zoom dharma discussion available on request. "
            "scdharma.org. (803) 467-7759."
        ),
    ),
}

# No live iCal feeds — all centers seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
