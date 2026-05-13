"""
Detroit, MI meditation center sources — Phase 3 expansion.

iCal feeds:
  None — all Detroit-area centers use Wix or static HTML sites without
  accessible iCal feeds.

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - Detroit Zen Center — Sun 10am Zen Workshop (in-person)
    3030 Casmere St, Hamtramck, MI 48212. Korean Zen (Sudeok-sa / Chogye Order).
  - Still Point Zen Buddhist Temple — Sun 8:30am Sunday Service (in-person + stream)
    4345 Trumbull Ave, Detroit, MI 48208. Korean Zen (Samu Sunim lineage).
  - Still Point Zen Buddhist Temple — Sat 10am Saturday Service (in-person + stream)
    4345 Trumbull Ave, Detroit, MI 48208. Korean Zen.
  - Field Temple — Sun 10am Meditation (in-person)
    5333 Elmwood Ave, Detroit, MI 48211. Zen (Korean tradition).
  - Dharma Gate Zen Center — Sun 10am Sunday Service (in-person)
    360 East Maple Suite K, Troy, MI 48083. Soto Zen.

Research notes (2026-05-13):
  - Detroit Zen Center (detroitzencenter.org): Wix site — no iCal. Founded 1990 by
    Abbot Hwalson Sunim; spiritual branch of Sudeok-sa Temple, Korea (Chogye Order).
    3030 Casmere St, Hamtramck MI (Hamtramck is a city encircled by Detroit).
    Sunday Zen Workshop: Meditation, Talk & Tea — 10am–12pm every Sunday.
    First Sunday: Beginners Workshop & Brunch 9am–12pm (instruction + group sit +
    Dharma talk + dialogue). Daily sittings for residents; Sunday workshop is primary
    public offering.
  - Still Point Zen Buddhist Temple (stillpointzenbuddhisttemple.org): Wix site — no
    iCal. 4345 Trumbull Ave, Detroit MI 48208 (Corktown/Woodbridge area). Founded by
    P'arang Geri Larkin, current teacher Koho Vince Anila. Korean Zen lineage through
    Venerable Samu Sunim. Sunday service 8:30–11:30am (in-person + livestream); also
    Saturday in-person service. Recovery Dharma meetings. Significant social justice
    presence. Sunday hours confirmed: 8:30am–11:30am.
  - Field Temple (fieldtemple.org): Simple website — no iCal. 5333 Elmwood Ave,
    Detroit MI 48211. Zen in the Korean tradition. Sunday meditation 10–11am: two
    20-min zazen periods, chanting three refuges (Pali then English), dharma talk,
    tea. Meeting "in the Field or under the trees." Free, all welcome.
  - Dharma Gate Zen Center (dharmagatezen.org): WordPress site — weekday sittings
    currently on hiatus. Sunday Service 10–11am in-person. Recovery Dharma Sat 10am
    and Wed noon. 360 East Maple Suite K, Troy MI 48083. Soto Zen lineage.
  - Detroit Zen Center (weebly legacy site detroitzencenter.weebly.com): old site,
    content migrated to current Wix site.
  - Southeast Michigan aggregator: beyondthecushion.com/southeast-michigan/ lists
    additional centers; Ann Arbor centers (45 mi west) deferred to separate metro.
  - Midwest Buddhist Meditation Center (Warren, MI): Thai Theravada (Maha Nikaya),
    29750 Ryan Rd, Warren MI — primarily temple/festival events, not clear drop-in
    sitting schedule. Deferred.
  - Great Lakes Buddhist Vihara (Southfield MI): Theravada monastery, mainly online
    courses and private guidance. No regular public drop-in sits. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "detroit_zen_center": Center(
        id="detroit_zen_center",
        name="Detroit Zen Center",
        url="https://www.detroitzencenter.org",
        address="3030 Casmere St",
        city="Hamtramck",
        state="MI",
        zip_code="48212",
        lat=42.3936,
        lng=-83.0566,
        neighborhood="Hamtramck (Detroit metro)",
        tradition=Tradition.ZEN,
        notes=(
            "Detroit Zen Center is a Korean Zen community in the Chogye Order, a "
            "spiritual branch of Sudeok-sa Temple in Korea (founded 6th century CE). "
            "Founded in 1990 by Abbot Hwalson Sunim in Hamtramck (a city encircled "
            "by Detroit). Sunday Zen Workshop (10am–12pm): guided meditation, dharma "
            "talk, and tea — open to all levels, drop-in welcome. First Sunday "
            "Beginners Workshop & Brunch (9am–12pm) includes instruction, group "
            "meditation, dharma talk, and dialogue. Gardens, plant-based meals, and "
            "guest retreat lodging available. By donation."
        ),
    ),
    "still_point_zen_detroit": Center(
        id="still_point_zen_detroit",
        name="Still Point Zen Buddhist Temple",
        url="https://www.stillpointzenbuddhisttemple.org",
        address="4345 Trumbull Ave",
        city="Detroit",
        state="MI",
        zip_code="48208",
        lat=42.3527,
        lng=-83.0731,
        neighborhood="Corktown / Woodbridge",
        tradition=Tradition.ZEN,
        notes=(
            "Still Point Zen Buddhist Temple is a Korean Zen community in Detroit's "
            "Corktown/Woodbridge area, in the lineage of Venerable Samu Sunim. "
            "Founded by P'arang Geri Larkin; current guiding teacher is Koho Vince "
            "Anila. Sunday service (8:30–11:30am): zazen, chanting, dharma talk — "
            "in-person and livestreamed. Saturday service also in-person with "
            "livestream. Recovery Dharma meetings and One Sangha outreach program. "
            "Known for strong social justice engagement in Detroit. Free and open to all."
        ),
    ),
    "field_temple_detroit": Center(
        id="field_temple_detroit",
        name="Field Temple",
        url="https://fieldtemple.org",
        address="5333 Elmwood Ave",
        city="Detroit",
        state="MI",
        zip_code="48211",
        lat=42.3699,
        lng=-83.0431,
        neighborhood="East Detroit / Poletown East",
        tradition=Tradition.ZEN,
        notes=(
            "Field Temple is a Zen community in Detroit's Poletown East neighborhood, "
            "practicing in the Korean Zen tradition. Sunday meditation (10–11am): "
            "two twenty-minute zazen periods separated by chanting the three refuges "
            "(first in Pali, then English), followed by a dharma talk and tea. "
            "Sessions held in the garden or under the trees at 5333 Elmwood. "
            "Open to all — no experience required. Free."
        ),
    ),
    "dharma_gate_zen_troy": Center(
        id="dharma_gate_zen_troy",
        name="Dharma Gate Zen Center",
        url="https://dharmagatezen.org",
        address="360 East Maple Suite K",
        city="Troy",
        state="MI",
        zip_code="48083",
        lat=42.5798,
        lng=-83.1446,
        neighborhood="Troy (Detroit suburb)",
        tradition=Tradition.ZEN,
        notes=(
            "Dharma Gate Zen Center is a Soto Zen community in Troy, Michigan (north "
            "Detroit suburb). Sunday service (10–11am) includes zazen and a dharma "
            "talk — open to all, beginners welcome. Also hosts Recovery Dharma "
            "meetings (Saturday 10am and Wednesday noon) and Shinrin-Yoku (forest "
            "bathing) practice on Saturdays. Weekday zazen currently on hiatus. "
            "Free to attend."
        ),
    ),
}

# No accessible iCal feeds for Detroit-area centers
ICAL_FEEDS: dict = {}
