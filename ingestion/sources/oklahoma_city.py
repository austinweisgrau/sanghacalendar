"""
Oklahoma City, OK — Phase 3 expansion.

OKC has a small but active meditation community spanning Theravada and
Chinese Zen traditions. The city's longest-running public meditation
program is the Oklahoma Buddhist Vihara, a Theravada monastery offering
free weekly sits since the 1990s.

Centers included:
  - Oklahoma Buddhist Vihara (okbv) — Theravada
    4820 N Portland Ave, Oklahoma City OK 73112 (Nichols Hills area)
    okbv.org — Wed 6pm (Silent Meditation), Sat 6pm (Pali Chanting+Sit),
    Sun 5pm (Guided Meditation + Discussion)
    No iCal; recurring sits seeded.

  - Buddha Mind Monastery OKC (buddha_mind_okc) — Chinese Mahayana/Zen
    5800 S Anderson Rd, Oklahoma City OK 73150 (SE Oklahoma City)
    ctbuddhamind.org — Sun 3pm (One-Hour Guided Meditation)
    No iCal; recurring sit seeded.

Research notes (2026-05-20):
  - Oklahoma Buddhist Vihara (OKBV): Theravada monastery at 4820 N Portland Ave.
    Founded with resident monks trained in the Theravada tradition; open to all
    traditions. Confirmed schedule (okbv.org): Wed 6–7pm silent meditation,
    Sat 6–7pm Pali chanting + silent reflection, Sun 5–6pm guided meditation +
    30-min discussion. Hybrid Google Meet. Free; donations welcome.
  - Buddha Mind Monastery OKC: Chinese Mahayana/Zen at 5800 S Anderson Rd.
    Founded 2004. Free weekly guided meditation: Sun 3–4pm. Monthly half-day
    retreats and dharma ceremonies. No iCal (WordPress events page).
  - Ganden Ling Buddhist Center (NKT/Kadampa): 4813 N MacArthur Blvd — website
    (meditationinoklahoma.org) is offline. Status unclear; deferred.
  - Rissho Kosei-kai Dharma Center (2745 NW 40th St): Nichiren-influenced; primary
    activities are chanting services and Hoza circles rather than sitting
    meditation. Skipped — not a fit for sit-focused calendar.
  - No Shambhala center found in OKC (nearest is Tulsa or Kansas City).
  - Memphis Zen Community (memphiszen.org): domain dead as of 2026 — not OKC but
    noted for future investigation if domain revives.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "okbv": Center(
        id="okbv",
        name="Oklahoma Buddhist Vihara",
        url="https://okbv.org",
        address="4820 N Portland Ave",
        city="Oklahoma City",
        state="OK",
        zip_code="73112",
        lat=35.5005,
        lng=-97.5263,
        neighborhood="Nichols Hills area / Uptown OKC",
        tradition=Tradition.THERAVADA,
        notes=(
            "The Oklahoma Buddhist Vihara (OKBV) is a Theravada monastery in "
            "central Oklahoma City, guided by resident monastics trained in the "
            "Theravada tradition but welcoming practitioners of all backgrounds "
            "and traditions. Weekly public sits: Wednesday Silent Meditation "
            "(6–7 PM in-person), Saturday Pali Chanting and Meditation (6–7 PM "
            "in-person), and Sunday Guided Meditation and Discussion (5–6 PM, "
            "hybrid in-person + Google Meet — 30 min guided sit followed by "
            "30 min dharma discussion). Free; donations welcome."
        ),
    ),
    "buddha_mind_okc": Center(
        id="buddha_mind_okc",
        name="Buddha Mind Monastery",
        url="https://www.ctbuddhamind.org",
        address="5800 S Anderson Rd",
        city="Oklahoma City",
        state="OK",
        zip_code="73150",
        lat=35.3908,
        lng=-97.4218,
        neighborhood="SE Oklahoma City",
        tradition=Tradition.ZEN,
        notes=(
            "Buddha Mind Monastery (佛心禪寺) is a Chinese Mahayana Zen "
            "monastery in southeast Oklahoma City, founded in 2004. It offers "
            "free one-hour guided meditation every Sunday from 3–4 PM, open to "
            "all regardless of background or experience. The monastery also "
            "hosts monthly dharma ceremonies (Medicine Buddha, Amitabha, etc.) "
            "and half-day meditation retreats. Eleven acres; open daily "
            "2–5 PM for visits."
        ),
    ),
}

# No live iCal feeds extractable for Oklahoma City centers —
# all sits seeded as recurring in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
