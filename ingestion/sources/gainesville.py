"""
Gainesville, Florida — Phase 3 expansion (heartbeat 76).

Gainesville (pop. ~140k; metro ~330k) is home to the University of Florida
and a notably diverse Buddhist scene anchored by the Gainesville Buddhist
Alliance. The GBA coordinates monthly community sits and represents seven
member groups spanning Tibetan, Shambhala, Zen, Vipassana, and Plum Village
traditions.

Centers included:
  - Gainesville Karma Thegsum Choling (ktc_gainesville)
    Tibetan Buddhist (Karma Kagyu lineage), teacher Lama Losang (Dr. David Bole)
    1216 NW 9th Ave, Gainesville FL 32601
    ktcgainesville.org · Sun 9:30am in-person
    No iCal — seeded as recurring.

  - Shambhala Gainesville (shambhala_gainesville)
    Shambhala (Tibetan-influenced), meditation and study
    1899 NE 23rd Ave, Gainesville FL 32609
    gainesville.shambhala.org · Tue 6pm + Sun 10am in-person
    No iCal — seeded as recurring.

  - Vipassana Karuna Sangha (vipassana_karuna_gainesville)
    Theravada / Vipassana, teacher Nancy Lasseter
    Karuna Cottage, Gainesville FL (private residence, NW area)
    nancylasseter.com/vipassana-karuna-sangha/ · Thu 6pm in-person
    No iCal — seeded as recurring.

  - Florida Sanbo Zen (florida_sanbo_zen)
    Zen (Sanbo Zen lineage), teachers Shana Smith, Debi & Bob Kolb
    Karuna Cottage, Gainesville FL (private residence, NW area)
    nancylasseter.com/fl-sanbo-zen/ · Wed 6pm in-person + online
    No iCal — seeded as recurring.

Research notes (2026-06-07):
  - Gainesville KTC: founded by Lama Losang (Dr. David Bole), Karma Kagyu /
    Vajrayana. Sundays: Nejang & Qi Gong 9am, meditation 9:30am, Buddhist
    teachings 10am. Also 1st Saturday monthly 4pm Ngondro practice. Located
    at 1216 NW 9th Ave (near downtown, Duckpond neighborhood). ktcgainesville.org.
  - Shambhala Gainesville: meets at 1899 NE 23rd Ave. Tuesday 6:00–7:00pm
    in-person sitting (rotating instruction / compassion practice / chants).
    Sunday 9:30am beginner instruction + 10:00am–12:00pm sitting + walking +
    book discussion. Mon–Fri 6:45am online Zoom sits also offered but online-
    only sits excluded from seeding. Active community with Rainbow Dharma
    (LGBTQIA+-led, 2nd/4th Thu) and other programs.
  - Vipassana Karuna Sangha + Florida Sanbo Zen both meet at Karuna Cottage,
    a private residence in Gainesville (NW area, zip 32653). Address sent to
    attendees on registration/request. Nancy Lasseter hosts both groups.
  - Gateless Gate Zen (Kwan Um): Tuesday 6pm Zoom-only — skipped (online only).
  - Gainesville Vipassana Society (floridavipassana.org): Wednesday 7:30pm
    Zoom-only — skipped (online only).
  - Kadampa Gainesville (meditationingainesville.org): uncertain if still active;
    Tampa Bay page doesn't show Gainesville-specific schedule. Deferred.
  - Live Oak Sangha (Plum Village, meets at United Church of Gainesville,
    1801 NW 5th Ave): schedule not confirmed from public sources; deferred.
  - Gainesville Buddhist Alliance (gainesvillebuddhistalliance.org): umbrella
    org, last-Saturday-of-month community sit at Thomas Center — informal,
    deferred pending confirmed schedule.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "ktc_gainesville": Center(
        id="ktc_gainesville",
        name="Gainesville Karma Thegsum Choling",
        url="https://www.ktcgainesville.org",
        address="1216 NW 9th Ave",
        city="Gainesville",
        state="FL",
        zip_code="32601",
        lat=29.6592,
        lng=-82.3378,
        neighborhood="Duckpond",
        tradition=Tradition.TIBETAN,
        notes=(
            "Gainesville Karma Thegsum Choling (KTC) is a Tibetan Buddhist center "
            "in the Karma Kagyu lineage, led by Lama Losang (Dr. David Bole). "
            "Located at 1216 NW 9th Ave near downtown Gainesville. Sunday Program: "
            "Nejang & Qi Gong at 9:00am, sitting meditation at 9:30am, and Buddhist "
            "teachings at 10:00am — open to the public, drop-in welcome. "
            "Additional programming includes Monday Advanced Book Study (5:30pm), "
            "Tuesday Nejang Yoga/Tai Chi (11am and 6pm), and a monthly 1st Saturday "
            "Ngondro Practice Group (4pm). Member of the Gainesville Buddhist "
            "Alliance. (352) 335-1975 · ktcgainesville.org."
        ),
    ),
    "shambhala_gainesville": Center(
        id="shambhala_gainesville",
        name="Shambhala Gainesville",
        url="https://gainesville.shambhala.org",
        address="1899 NE 23rd Ave",
        city="Gainesville",
        state="FL",
        zip_code="32609",
        lat=29.6768,
        lng=-82.3028,
        neighborhood="Northeast Gainesville",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Gainesville offers a rich schedule of in-person and online "
            "meditation at its center at 1899 NE 23rd Ave. Tuesday Evening Sitting "
            "(6:00–7:00pm): in-person, rotating formats — meditation instruction, "
            "compassion practice, or chants; drop-in welcome. Sunday Morning Program "
            "(10:00am–12:00pm): sitting + walking meditation + book discussion; "
            "beginner instruction at 9:30am; drop-in welcome. Also hosts Rainbow "
            "Dharma (LGBTQIA+-led sits, 2nd & 4th Thursdays 6:30pm) and online "
            "weekday morning sits. Member of the Gainesville Buddhist Alliance. "
            "(352) 448-5870 · info@gainesville.shambhala.org · "
            "gainesville.shambhala.org."
        ),
    ),
    "vipassana_karuna_gainesville": Center(
        id="vipassana_karuna_gainesville",
        name="Vipassana Karuna Sangha",
        url="https://nancylasseter.com/vipassana-karuna-sangha/",
        address="Karuna Cottage",
        city="Gainesville",
        state="FL",
        zip_code="32653",
        lat=29.6950,
        lng=-82.3500,
        neighborhood="Northwest Gainesville",
        tradition=Tradition.THERAVADA,
        notes=(
            "Vipassana Karuna Sangha is a Theravada/Vipassana community led by "
            "Nancy Lasseter at Karuna Cottage — her private residence in northwest "
            "Gainesville. Thursday Evening Meditation (6:00–7:30pm): 30-minute "
            "guided meditation, 10-minute walking meditation, 20-minute silent sit, "
            "followed by a teaching and community sharing. In-person; arrive by "
            "5:50pm to settle in. All are welcome; free (donations suggested). "
            "Location sent on registration. Member of the Gainesville Buddhist "
            "Alliance. nancylasseter@gmail.com · "
            "nancylasseter.com/vipassana-karuna-sangha/."
        ),
    ),
    "florida_sanbo_zen": Center(
        id="florida_sanbo_zen",
        name="Florida Sanbo Zen",
        url="https://nancylasseter.com/fl-sanbo-zen/",
        address="Karuna Cottage",
        city="Gainesville",
        state="FL",
        zip_code="32653",
        lat=29.6950,
        lng=-82.3500,
        neighborhood="Northwest Gainesville",
        tradition=Tradition.ZEN,
        notes=(
            "Florida Sanbo Zen is a Zen sitting group in the Sanbo Zen lineage, "
            "meeting at Karuna Cottage (Nancy Lasseter's home) in northwest "
            "Gainesville. Teachers include Shana Smith and senior practitioners "
            "Debi and Bob Kolb. Wednesday Evening Zazen (6:00–7:45pm): zazen, "
            "kinhin (walking meditation), and tea; in-person with an online option "
            "available. All levels and traditions welcome; drop-in. Suggested "
            "donation $5–$20, sustaining membership $25/month. "
            "Member of the Gainesville Buddhist Alliance. "
            "floridasanbozen@gmail.com · nancylasseter.com/fl-sanbo-zen/."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — all centers seeded via scripts/sangha-seed-recurring.js
