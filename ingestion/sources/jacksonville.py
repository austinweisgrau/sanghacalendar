"""
Jacksonville, FL — Phase 3 expansion (heartbeat 111).

Jacksonville (pop. ~975k; metro ~1.6M) is Florida's largest city and one of
the largest by area in the contiguous US. Its Buddhist scene is modest but
geographically spread across distinct neighborhoods.

Centers included:
  - Maitreya Kadampa Buddhist Center Jacksonville (maitreya_kadampa_jax)
    NKT/Kadampa Tibetan, teacher Kadam Carol Lutker
    8400 Baymeadows Way Suite 7, Jacksonville FL 32256
    Recurring sits: Sun 10am, Thu 6pm (main center) + Wed 5pm at San Marco Library
    No iCal (WordPress Events Calendar plugin, no public feed confirmed); sits seeded.

  - Jacksonville Great Cloud Sangha (great_cloud_sangha_jax)
    Soto Zen / Silent Thunder Order (Matsuoka-Roshi lineage), Sensei Ungan Bill Mayhew
    7405 Arlington Expressway, Jacksonville FL 32211 (Unitarian Universalist Church)
    Recurring sits: Mon 7pm hybrid + Sat 1:30pm hybrid
    No persistent iCal; seeded from confirmed schedule.

  - Karma Thegsum Choling Jacksonville (ktc_jacksonville)
    Tibetan Buddhism, Karma Kagyu lineage (KTD affiliate), est. ~1987
    4168 Herschel St, Jacksonville FL 32210
    Recurring sits: Sat 9am silent meditation (hybrid) + Tue 6pm Medicine Buddha (hybrid)
    No iCal; sits seeded from website schedule.

Research notes (2026-10-07):
  - Maitreya Kadampa (meditationinjacksonville.org): Wix/WP site with Events Calendar
    plugin. Schedule confirmed: Sun 10–11:15am in-person teachings + guided meditation
    with Kadam Carol Lutker; Thu 6–7:15pm in-person General Program with teacher John
    Jones; Wed 5–5:40pm in-person at San Marco Library branch. Also Tue 6pm online-only
    (skipped). Foundation Program Sun noon–2pm (advanced members only; skipped).
    Also has Meetup.com group (exports iCal) but schedule reliability lower.
  - Great Cloud Sangha (storder.org): Soto Zen group affiliated with Silent Thunder
    Order (Matsuoka Roshi lineage; same lineage as Midwest Zen centers). Sensei Ungan
    Bill Mayhew leads. Meets at UU Church of Jacksonville, 7405 Arlington Expressway
    (Susan B. Anthony Room). Mon 7–8:30pm (2× 25-min sits, kinhin, Heart Sutra,
    dharma discussion; Zoom also available). Sat 1:30–3pm open sitting (Zoom also
    available). Newcomers: arrive by 6pm Mon or 12:30pm Sat for orientation.
    Events listed on storder.org with iCal/GCal export — Silent Thunder Order
    aggregate calendar.
  - KTC Jacksonville (ktcjax.org): Karma Kagyu lineage, affiliated with Karma Triyana
    Dharmachakra. Est. ~1987. 4168 Herschel St (Murray Hill/Avondale area).
    Sat: 9–10am Silent Sitting Meditation + 10–10:30am Book Study + 10:30–11:30am
    Chenrezig/Amitabha sadhana (1st Sat: Green Tara) — seeded the meditation sit only.
    Tue: 6–7pm Medicine Buddha practice (hybrid) + 7–8pm Buddhism Basics Study Group
    (2nd Tue: Lama Losang via Zoom) — seeded Medicine Buddha as a practice sit.
  - Jacksonville Zen Sangha (jaxzensangha.org, 2014 Perry Place): Rinzai Zen
    (Dai Bosatsu lineage). Schedule uncertain — stale data risk; deferred pending
    confirmation. Contact: zenrin@bellsouth.net.
  - Bhavana Meditation Center (Vietnamese Buddhist, Meetup Fri 7pm): skipped for
    now — Meetup-only calendar, small group; revisit if schedule stabilizes.
  - SGI-USA Jacksonville: no confirmed public sit schedule; skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "maitreya_kadampa_jax": Center(
        id="maitreya_kadampa_jax",
        name="Maitreya Kadampa Buddhist Center",
        url="https://meditationinjacksonville.org",
        address="8400 Baymeadows Way Suite 7",
        city="Jacksonville",
        state="FL",
        zip_code="32256",
        lat=30.2089,
        lng=-81.5839,
        neighborhood="Baymeadows",
        tradition=Tradition.TIBETAN,
        notes=(
            "Maitreya Kadampa Buddhist Center is a New Kadampa Tradition (NKT-IKBU) "
            "Tibetan Buddhist center in the Baymeadows neighborhood of Jacksonville, "
            "led by resident teacher Kadam Carol Lutker. Regular drop-in classes "
            "include Sunday Meditations for World Peace (10:00–11:15am, in-person), "
            "Wednesday General Program at San Marco Library (5:00–5:40pm, in-person), "
            "and Thursday General Program (6:00–7:15pm, in-person with teacher John "
            "Jones). All sessions include guided meditation and Buddhist teachings "
            "in the Kadampa / Modern Buddhism tradition. No experience needed; "
            "donations welcome. Special events, retreats, and empowerments throughout "
            "the year. meditationinjacksonville.org. (904) 648-9994."
        ),
    ),
    "great_cloud_sangha_jax": Center(
        id="great_cloud_sangha_jax",
        name="Jacksonville Great Cloud Sangha",
        url="https://storder.org/portfolio/jacksonsville-soto-zen-group/",
        address="7405 Arlington Expressway",
        city="Jacksonville",
        state="FL",
        zip_code="32211",
        lat=30.3292,
        lng=-81.6076,
        neighborhood="Arlington",
        tradition=Tradition.ZEN,
        notes=(
            "Jacksonville Great Cloud Sangha is a Soto Zen sitting group in the "
            "Silent Thunder Order, the lineage of Matsuoka Roshi, led by Sensei "
            "Ungan Bill Mayhew. The group meets in the Susan B. Anthony Room at the "
            "Unitarian Universalist Church of Jacksonville (7405 Arlington Expressway). "
            "Monday Evening Zazen (7:00–8:30pm): two 25-minute periods of zazen, "
            "kinhin, Heart Sutra, and dharma discussion; newcomers arrive by 6:00pm "
            "for orientation. Saturday Open Sitting (1:30–3:00pm): open zazen and "
            "kinhin; newcomers arrive by 12:30pm. Both sessions available via Zoom. "
            "Drop-in welcome; all levels. Free. (904) 725-8133. "
            "storder.org/portfolio/jacksonsville-soto-zen-group/."
        ),
    ),
    "ktc_jacksonville": Center(
        id="ktc_jacksonville",
        name="Karma Thegsum Choling Jacksonville",
        url="https://ktcjax.org",
        address="4168 Herschel St",
        city="Jacksonville",
        state="FL",
        zip_code="32210",
        lat=30.3098,
        lng=-81.6853,
        neighborhood="Murray Hill / Avondale",
        tradition=Tradition.TIBETAN,
        notes=(
            "Karma Thegsum Choling (KTC) Jacksonville is a Tibetan Buddhist center "
            "in the Karma Kagyu lineage, affiliated with Karma Triyana Dharmachakra "
            "(KTD) in Woodstock, NY — the North American seat of His Holiness "
            "Gyalwang Karmapa. One of the oldest KTC centers in Florida, founded "
            "~1987. Located at 4168 Herschel St in the Murray Hill / Avondale "
            "neighborhood. Saturday Program: Silent Sitting Meditation (9:00–10:00am), "
            "Book Study (10:00–10:30am), and Chenrezig & Amitabha Sadhana "
            "(10:30am–noon; 1st Saturday: Green Tara Sadhana) — in-person and Zoom. "
            "Tuesday Evening: Medicine Buddha Practice (6:00–7:00pm) and Buddhism "
            "Basics Study Group (7:00–8:00pm; 2nd Tuesday: teachings from Lama "
            "Losang via Zoom). Open to all; drop-in welcome. ktcjax.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No confirmed live iCal feeds — all sits seeded via sangha-seed-recurring.js
