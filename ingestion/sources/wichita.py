"""
Wichita, KS — Phase 3 expansion.

Wichita (~400k city, ~650k metro) is Kansas' largest city, situated in the
south-central plains. Despite its location in the heartland, it supports a
genuine Buddhist community spanning Zen, Tibetan Karma Kagyu, and Theravada
traditions.

Centers included:
  - Southwind Sangha (southwind_sangha) — Soto Zen (SZBA)
    Meets at Pine Valley Christian Church, 5620 E 21st St N, Wichita KS 67208.
    southwindsangha.org. Sun 9–10:30am + Wed 7–8pm + 3rd Sat 8am–noon.
    No iCal; seeded recurring sits.

  - Wichita KTC (wichita_ktc) — Karma Kagyu Tibetan
    425 S Yale Ave, Wichita KS 67218. wichitaktc.org
    1st/3rd Sunday 10am Chenrezik Sadhana; 2nd/4th Sunday 10am Sitting Meditation.
    No iCal; seeded recurring sits (every Sunday 10am).

  - Dhammakaya Meditation Center Kansas (dmck) — Thai Theravada
    1650 S Water St, Wichita KS 67213. meditationkansas.org
    Saturday 3:30–5pm public meditation class. No iCal; seeded.

Research notes (2026-05-24):
  - Southwind Sangha: meets at Pine Valley Christian Church. Contact via
    harold.sanki@gmail.com or Facebook for Zoom link. Soto Zen Buddhist
    Association (SZBA) member. First Wednesday = Intro to Zen.
    Third Wednesday = single 30-min sit + dharma discussion. Third Saturday
    = half-day silent retreat 8am–noon. Very welcoming to beginners.
  - Wichita KTC: Karma Thegsum Chöling (KTC) in the Karma Kagyu lineage.
    1st/3rd Sunday 10am includes Chenrezik Sadhana (medicine Buddha mantra,
    sitting meditation, dharma talk). 2nd/4th Sunday is explicit sitting
    meditation + discussion/book study. Seeding all Sundays 10am.
  - Dhammakaya Meditation Center Kansas: Thai Theravada (Dhammakaya lineage),
    at 1650 S Water St. Saturday 3:30–5pm public meditation class; no
    experience required. First Saturday of each month is off (special holidays).
  - Kansas Meditation Center (kansasmeditationcenter.com): Theravada Buddhist
    monastery; offers weekly classes but schedule not publicly confirmed for
    2026 — deferred.
  - Mindfulness Practice Group of Kansas (Plum Village/TNH): meets at Wat
    Wichitaram (5327 N Broadway); schedule unconfirmed — deferred.
  - Zen Friends of Wichita: meets at First UU Church; schedule unconfirmed — deferred.
  - No Shambhala center found in Wichita (phoenix.shambhala.org redirects;
    nearest active centers are Kansas City and Albuquerque).
  - No KMC/NKT center found in Wichita.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "southwind_sangha": Center(
        id="southwind_sangha",
        name="Southwind Sangha",
        url="https://southwindsangha.org",
        address="5620 E 21st St N",
        city="Wichita",
        state="KS",
        zip_code="67208",
        lat=37.7220,
        lng=-97.2520,
        neighborhood="Northeast Wichita",
        tradition=Tradition.ZEN,
        notes=(
            "Southwind Sangha is a Soto Zen Buddhist community (Soto Zen Buddhist "
            "Association / SZBA member) meeting at Pine Valley Christian Church in "
            "northeast Wichita. Regular schedule: Sunday 9:00–10:30am (zazen, kinhin, "
            "Heart Sutra chanting; two rounds of seated meditation separated by walking "
            "meditation); Wednesday 7:00–8:00pm (first Wednesday = Introduction to Zen; "
            "third Wednesday = single 30-min sit + dharma discussion). Third Saturday of "
            "each month: 8:00am–12:00pm silent half-day retreat. Drop-in welcome. "
            "Contact harold.sanki@gmail.com or their Facebook page for Zoom link and "
            "to be added to the mailing list. Dana-based."
        ),
    ),
    "wichita_ktc": Center(
        id="wichita_ktc",
        name="Wichita KTC",
        url="https://wichitaktc.org",
        address="425 S Yale Ave",
        city="Wichita",
        state="KS",
        zip_code="67218",
        lat=37.6810,
        lng=-97.2680,
        neighborhood="East Wichita",
        tradition=Tradition.TIBETAN,
        notes=(
            "Wichita KTC (Karma Thegsum Chöling) is a Tibetan Buddhist meditation center "
            "in the Karma Kagyu lineage, located at 425 S Yale Ave in east Wichita. "
            "Sunday program 10:00–11:45am: 1st and 3rd Sundays feature the Chenrezik "
            "Sadhana (compassion practice, mantra, sitting meditation) followed by a "
            "dharma talk; 2nd and 4th Sundays offer explicit sitting meditation (10:00am) "
            "followed by discussion and book study (10:40–11:45am). All are welcome; "
            "check their Facebook page (KTCWichita) for cancellations or updates. "
            "Contact: ktcwichita@yahoo.com."
        ),
    ),
    "dmck": Center(
        id="dmck",
        name="Dhammakaya Meditation Center Kansas",
        url="https://www.meditationkansas.org",
        address="1650 S Water St",
        city="Wichita",
        state="KS",
        zip_code="67213",
        lat=37.6635,
        lng=-97.3305,
        neighborhood="South Wichita",
        tradition=Tradition.THERAVADA,
        notes=(
            "Dhammakaya Meditation Center Kansas (DMCK) is a Thai Theravada Buddhist "
            "center offering public meditation classes in Wichita. Saturday public "
            "meditation class: 3:30–5:00pm at 1650 S Water St (most Saturdays; first "
            "Saturday of month and special holidays are off). No experience necessary; "
            "open to all. The Dhammakaya tradition emphasizes samadhi (concentration) "
            "meditation and the Middle Way of inner stillness. All are welcome."
        ),
    ),
}

# No live iCal feeds available for Wichita centers — all seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
