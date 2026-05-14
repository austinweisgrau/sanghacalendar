"""
Pittsburgh, PA meditation center sources — Phase 3 expansion.

iCal feeds:
  None confirmed for Pittsburgh metro. No centers with accessible iCal endpoints found.
  Stillpoint Zen uses WordPress but no Events Calendar plugin.
  Pittsburgh Buddhist Center uses WordPress but no ?ical=1 feed.
  Olmo Ling and Three Rivers Tibetan CC use Wix / static HTML.

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - Stillpoint Zen — Sun 9:30am, Wed 7pm zazen (in-person)
    137 41st St, Lawrenceville, Pittsburgh, PA 15201. Zen (lay community).
  - Pittsburgh Buddhist Center — Wed 7pm (main, Allison Park), Tue 6pm (Oakmont)
    58 QSI Lane, Allison Park, PA 15101. Theravada (resident monks).
  - Olmo Ling Bon Center — Sun 4pm Dzogchen Practice Group (1st & 3rd Sundays, in-person + Zoom)
    1101 Greenfield Ave, Pittsburgh, PA 15217. Tibetan Bon (pre-Buddhist Tibetan).
  - Three Rivers Tibetan Cultural Center — Wed 7pm, Sun 10am (in-person + Zoom)
    1660 Lincoln Way, White Oak, PA 15131. Tibetan (Drikung Kagyu).

Research notes (2026-05-14):
  - Stillpoint Zen (stillpointzen.org): Active lay Zen community in Lawrenceville.
    WordPress site, no iCal. Sunday zazen 9:30–10:40am, Wednesday 7–8pm.
    Fourth Saturday zazenkai (8:30am–8:10pm) — all-day sit, not seeded as weekly.
    Walk-in welcome; private intro to zazen on request.
  - Pittsburgh Buddhist Center (pittsburghbuddhistcenter.org): Theravada monastery
    in Allison Park with resident Burmese monks. Weekly Wed sit 7–9:30pm (beginners
    6:30pm for private instruction). Also outreach sits at Oakmont Carnegie Library
    (Tue 6pm), East Liberty Library (Mon 6pm), Fox Chapel Library (Thu 6pm). Free.
    WordPress site, no iCal.
  - Olmo Ling Bon Center (olmoling.org): Bon Buddhism (pre-Buddhist Tibetan tradition).
    1101 Greenfield Ave, Pittsburgh. Sunday Dzogchen Practice Group 4–6pm (1st/3rd
    Sundays: guided meditation; 2nd/4th: reading + discussion — all open to the public).
    Wednesday Wed Ngondro + Silent Meditation temporarily cancelled. Sat 8:30am Zoom
    (registration required). No iCal.
  - Three Rivers Tibetan Cultural Center (threeriverstibetancc.org): Drikung Kagyu
    lineage with resident teachers (Ven. Khenpo Choephel + Ven. Lama Kalsang).
    White Oak PA 15131, ~12 miles SE of Pittsburgh. Weekly practices (rotating
    Chenrezig, Manjushri, Medicine Buddha, Green Tara) Wed 7pm hybrid; Vajrasattva
    practice Sun 10am hybrid; Sat 10–10:30am Dharma Discussion. All levels welcome.
    No iCal; email list distribution.
  - Pittsburgh Shambhala (pittsburgh.shambhala.org): Redirects to main shambhala.org —
    center appears to have disaffiliated from Shambhala International in 2019.
    Skip; treat as inactive.
  - Deep Spring Zen Temple (deepspringzen.org): Soto Zen, SZBA-recognized, in Sewickley
    (~20 mi north). Strong lineage but orientation required before attending — deferred
    for now; seeding would require verification of drop-in policy. Monitor for future add.
  - Neighborhood Zen (neighborhoodzen.substack.com): Soto Zen, private Greenfield
    location, requires pre-registration. Google Calendar available but semi-private
    community. Deferred.
  - Zen Group of Pittsburgh (Kwan Um): Small Korean Zen group, 718 Franklin Ave,
    Wilkinsburg. Wed 7pm. Deferred (very small, verify still active before adding).
  - Insight Meditation Community of Pittsburgh: Zoom-only, Facebook-only presence.
    Deferred until they have a stable website.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "stillpoint_zen_pittsburgh": Center(
        id="stillpoint_zen_pittsburgh",
        name="Stillpoint — A Pittsburgh Zen Community",
        url="https://www.stillpointzen.org",
        address="137 41st St",
        city="Pittsburgh",
        state="PA",
        zip_code="15201",
        lat=40.4646,
        lng=-79.9644,
        neighborhood="Lawrenceville",
        tradition=Tradition.ZEN,
        notes=(
            "Stillpoint is a lay Zen community in the Lawrenceville neighborhood of Pittsburgh, "
            "offering drop-in zazen twice a week: Sunday morning (9:30–10:40am) and Wednesday "
            "evening (7–8pm), plus a monthly all-day zazenkai (fourth Saturday, 8:30am–8:10pm). "
            "Newcomers are explicitly welcome; a private introduction to zazen is offered to "
            "those new to the practice. No experience or membership required. Free, donation "
            "welcome. Contact: sit@stillpointzen.org."
        ),
    ),
    "pittsburgh_buddhist_center": Center(
        id="pittsburgh_buddhist_center",
        name="Pittsburgh Buddhist Center",
        url="https://www.pittsburghbuddhistcenter.org",
        address="58 QSI Lane",
        city="Allison Park",
        state="PA",
        zip_code="15101",
        lat=40.5760,
        lng=-79.9576,
        neighborhood="Allison Park (Hampton Township)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Pittsburgh Buddhist Center is a Theravada community with resident Burmese "
            "monks offering free, public weekly sits. Main center sits are Wednesday evenings "
            "(7–9:30pm at 58 QSI Lane, Allison Park; beginners welcome 6:30pm for private "
            "instruction). Community outreach sits at Oakmont Carnegie Library (Tuesday 6pm) "
            "and East Liberty Carnegie Library (Monday 6pm). Monks are available for dharma "
            "conversation after sits. All programs free; lay practitioners and newcomers welcome. "
            "Livestream: youtube.com/pbclive."
        ),
    ),
    "pittsburgh_buddhist_center_oakmont": Center(
        id="pittsburgh_buddhist_center_oakmont",
        name="Pittsburgh Buddhist Center — Oakmont",
        url="https://www.pittsburghbuddhistcenter.org",
        address="700 Allegheny River Blvd",
        city="Oakmont",
        state="PA",
        zip_code="15139",
        lat=40.5209,
        lng=-79.8362,
        neighborhood="Oakmont Carnegie Library",
        tradition=Tradition.THERAVADA,
        notes=(
            "Pittsburgh Buddhist Center outreach sit at Oakmont Carnegie Library (700 Allegheny "
            "River Blvd, Oakmont PA 15139). Weekly Tuesday evenings, 6pm. Led by resident monks "
            "from the main Pittsburgh Buddhist Center in Allison Park. Free and open to the public; "
            "all experience levels welcome. Monks available for dharma Q&A after sits."
        ),
    ),
    "olmo_ling_pittsburgh": Center(
        id="olmo_ling_pittsburgh",
        name="Olmo Ling Bon Center and Institute",
        url="https://www.olmoling.org",
        address="1101 Greenfield Ave",
        city="Pittsburgh",
        state="PA",
        zip_code="15217",
        lat=40.4180,
        lng=-79.9449,
        neighborhood="Greenfield",
        tradition=Tradition.TIBETAN,
        notes=(
            "Olmo Ling Bon Center and Institute is a center for Tibetan Bon Buddhism — the "
            "pre-Buddhist indigenous spiritual tradition of Tibet, closely related to but "
            "distinct from Tibetan Buddhism. Located in the Greenfield neighborhood of Pittsburgh. "
            "Sunday Dzogchen Practice Group (4–6pm) meets 1st and 3rd Sundays in-person with Zoom; "
            "1st/3rd Sundays are guided meditation practice, 2nd/4th Sundays are reading and "
            "discussion. Open to all; free. Monthly Family Sangha (Friday evenings 7–8pm) and "
            "Saturday Calm Abiding meditation via Zoom (8:30am, registration required). "
            "Director: Geshe Tenzin Wangyal Rinpoche's lineage. Contact: bon@olmoling.org."
        ),
    ),
    "three_rivers_tibetan_pittsburgh": Center(
        id="three_rivers_tibetan_pittsburgh",
        name="Three Rivers Tibetan Cultural Center",
        url="https://www.threeriverstibetancc.org",
        address="1660 Lincoln Way",
        city="White Oak",
        state="PA",
        zip_code="15131",
        lat=40.3407,
        lng=-79.8289,
        neighborhood="White Oak (SE Pittsburgh metro)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Three Rivers Tibetan Cultural Center (TRTCC) is a Drikung Kagyu lineage Tibetan "
            "Buddhist center in White Oak, PA (~12 miles southeast of Pittsburgh), with resident "
            "teachers Ven. Khenpo Choephel and Ven. Lama Kalsang. Weekly practices include "
            "rotating Chenrezig, Manjushri, Medicine Buddha, and Green Tara pujas — Wednesdays "
            "7pm hybrid in-person + Zoom; Vajrasattva practice Sundays 10am hybrid; Saturday "
            "10–10:30am Dharma Discussion / Basic Buddhism hybrid. Tuesday 7pm online Beginner "
            "Buddhism teaching. All levels of practitioners welcome; free. Practice schedule "
            "distributed via email list."
        ),
    ),
}

# No accessible iCal feeds for Pittsburgh-area centers
ICAL_FEEDS: dict = {}
