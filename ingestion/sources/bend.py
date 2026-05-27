"""
Bend/Central Oregon — Phase 3 expansion (heartbeat 71).

Bend (pop. ~100k; metro ~210k) is a fast-growing high-desert city in central
Oregon anchored by outdoor recreation and a vibrant wellness community. The
Buddhist scene is small but established across three traditions: a long-running
lay Zen group, a Nyingma Tibetan center founded in 1996, and a non-sectarian
Theravada/Vipassana center in nearby Redmond (~15 miles north).

Centers included:
  - Bend Zen (bend_zen)
    Non-affiliated lay Zen group (since 2003)
    Brooks Hall, Trinity Episcopal Church, 469 NW Wall St, Bend OR 97703
    bendzen.net · Mon 7–8pm in-person. Discussion group 8–8:30pm.
    No iCal — seeded as recurring.

  - Natural Mind Dharma Center (natural_mind_bend)
    Nyingma Tibetan Buddhist (Dudjom Tersar lineage), founded 1996
    345 SW Century Dr #2, Bend OR 97702
    naturalminddharma.org · Sun 8–9am (open to all) + Wed 7–8pm (experienced)
    Hybrid in-person + online. No iCal — seeded as recurring.

  - International Insight Meditation Center of Oregon (iimc_redmond)
    Non-sectarian Theravada/Vipassana, founded 2015
    805 NW 95th St, Redmond OR 97756 (~15 mi north of Bend)
    iimc-redmond.org · Sun 1–3pm in-person + monthly Peace Weekends
    No iCal — seeded as recurring.

Research notes (2026-05-27):
  - Bend Zen: Founded 2003 as a lay-led group. Uses Zen form (sitting, kinhin,
    dharma discussion) but welcomes all traditions. Monday evenings at Brooks
    Hall in Trinity Episcopal Church (469 NW Wall St, east entrance). Social
    tea starts 6:40pm; main sit 7–8pm; dharma discussion 8–8:30pm. Drop-in;
    no fee. Website: bendzen.net.
  - Bend Zendo (bendzendo.org): Appears dormant — website ECONNREFUSED. Listed
    at gosit.org but no current evidence of activity. Skip.
  - Natural Mind Dharma Center: Nyingma Tibetan center, Dudjom Tersar lineage.
    Teacher: Michael Scott Stevens (Pema Kunsang), vowed householder yogi.
    Founded 1996. 345 SW Century Dr #2, Bend OR 97702. Sunday 8–9am: Vajrayana
    practices + dharma talk, open to everyone (in-person + online). Wednesday
    7–8pm: focused practice + teachings (Vajrayana experience preferred,
    in-person + online). Online links via newsletter. No iCal feed.
  - IIMC Redmond: Non-sectarian Buddhist center focusing on Theravada suttas
    and Vipassana. Founded 2015. 805 NW 95th St, Redmond OR 97756. Sunday 1pm:
    community practice (walking meditation, sitting, metta). Third weekend of
    month: Peace Weekends. Saturday: online Dhamma talks group. No iCal feed.
  - Mahasiddha Kadampa (meditationinoregon.org): Blocked by security challenge
    (Cloudflare). Oregon NKT center; location unclear from search results.
    Monitor for future access.
  - SRF Bend Meditation Circle: Self-Realization Fellowship. Devotional/inspirational
    tradition (Paramahansa Yogananda), not a traditional Buddhist sit. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "bend_zen": Center(
        id="bend_zen",
        name="Bend Zen",
        url="https://www.bendzen.net",
        address="469 NW Wall St",
        city="Bend",
        state="OR",
        zip_code="97703",
        lat=44.0578,
        lng=-121.3155,
        neighborhood="Downtown Bend",
        tradition=Tradition.ZEN,
        notes=(
            "Bend Zen is a lay-led Zen sitting group that has practiced together "
            "since 2003. While welcoming all contemplative traditions, the group "
            "uses a distinctly Zen form: sitting meditation, kinhin (walking "
            "meditation), and dharma discussion. Monday evenings at Brooks Hall, "
            "Trinity Episcopal Church (469 NW Wall St, east entrance): tea and "
            "social 6:40pm; sit 7:00–8:00pm; dharma discussion 8:00–8:30pm. "
            "Drop-in welcome; no fee. bendzen.net."
        ),
    ),
    "natural_mind_bend": Center(
        id="natural_mind_bend",
        name="Natural Mind Dharma Center",
        url="https://naturalminddharma.org",
        address="345 SW Century Dr, Suite 2",
        city="Bend",
        state="OR",
        zip_code="97702",
        lat=44.0422,
        lng=-121.3358,
        neighborhood="Southwest Bend",
        tradition=Tradition.TIBETAN,
        notes=(
            "Natural Mind Dharma Center is a Nyingma Tibetan Buddhist center in "
            "Bend, founded in 1996 by Michael Scott Stevens (Pema Kunsang), a "
            "vowed householder yogi in the Dudjom Tersar lineage. Emphasizes "
            "Vajrayana meditation, visualization, mantra, and Dzogchen. "
            "Sunday 8–9am: Vajrayana Buddhist Practices and Dharma Talk — open "
            "to everyone; in-person and online. Wednesday 7–8pm: Practice and "
            "Focused Teachings — best for those with some Vajrayana experience; "
            "in-person and online. Online links via newsletter. 345 SW Century "
            "Dr #2, Bend OR 97702. (541) 388-3352. naturalminddharma.org."
        ),
    ),
    "iimc_redmond": Center(
        id="iimc_redmond",
        name="International Insight Meditation Center of Oregon",
        url="https://www.iimc-redmond.org",
        address="805 NW 95th St",
        city="Redmond",
        state="OR",
        zip_code="97756",
        lat=44.2780,
        lng=-121.1519,
        neighborhood="Redmond",
        tradition=Tradition.THERAVADA,
        notes=(
            "International Insight Meditation Center of Oregon (IIMC) is a "
            "non-sectarian Buddhist meditation center in Redmond (~15 miles north "
            "of Bend), founded in 2015. Dedicated to the study and practice of "
            "the Buddha's teachings as found in the Suttas, with a focus on "
            "Vipassana (insight meditation) and metta (loving-kindness). Sunday "
            "1:00–3:00pm: Community Practice — walking meditation, sitting "
            "meditation, and metta; in-person. Monthly: Peace Weekends on the "
            "third weekend. Saturday online group: Dhamma talks and Suttas study. "
            "805 NW 95th St, Redmond OR 97756. iimc-redmond.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — all centers seeded via sangha-seed-recurring.js
