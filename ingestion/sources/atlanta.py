"""
Atlanta, GA meditation center sources — Phase 3 expansion.

iCal feeds:
  - Atlanta Shambhala Meditation Center (shambhala_atlanta)
    Cologne iCal server: shambhala-koeln.de/ical.php?center=196 — 372 events.
    Drop-in sits: Fri 12pm, Sun 10am, Tue 7pm. One Breath Group Mon/Wed/Thu.
    Also: BIPOC Sangha, Queer Dharma, Shambhala Training weekends.
    Address: 1447 Church St, Decatur GA 30030 (unincorporated DeKalb, in Atlanta metro)

RSS feeds:
  - Red Clay Sangha (red_clay_sangha)
    Wild Apricot RSS: redclaysangha.org/Calendar/RSS — 243 items.
    Multi-tradition (Theravada / Plum Village / Chan-Zen), 3315 Chamblee Dunwoody Rd, Chamblee GA.
    Key sits: Sunday Morning Meditation 9am, Mindfulness Practice in Plum Village Tradition 5pm,
    RCS Insight Dialog Practice Group (3rd Monday 7pm monthly).

Static HTML scrapers:
  - Drepung Loseling Institute Atlanta (drepung_loseling_atlanta)
    Monthly HTML calendar at drepung.org/changing/calendar/current.htm.
    Major Gelugpa Tibetan institution connected to Emory CBCT.
    1781 Dresden Dr NE, Brookhaven / Lynwood Hills, Atlanta GA 30319.
    Public sits: Sunday 11am Open Meditation (in-person + livestream),
    Tuesday 7pm Public Talk by resident geshe (in-person + livestream).

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - Atlanta Soto Zen Center (aszc): daily 6am, Wed 7pm, Sun 9am
    (Squarespace site, no iCal — schedule from aszc.org)
  - Kadampa Meditation Center Georgia (kmc_georgia): Sun 10:30am, Tue 7pm, Wed 7pm
    (Squarespace site, no iCal — schedule from meditationingeorgia.org)
  - Drepung Loseling Atlanta (drepung_loseling_atlanta): Sun 11am
    (backup recurring sit for static HTML scraper gaps)

Research notes (2026-05-11):
  - Atlanta Insight Meditation Community (atlinsight.org): small Squarespace community.
    Tue 6:30pm + Thu 8am (Zoom-only satsang). Low priority.
  - Diamond Way Atlanta: no active center found.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_atlanta": Center(
        id="shambhala_atlanta",
        name="Atlanta Shambhala Meditation Center",
        url="https://atlanta.shambhala.org",
        address="1447 Church St",
        city="Decatur",
        state="GA",
        zip_code="30030",
        lat=33.7763,
        lng=-84.2960,
        neighborhood="Decatur / Atlanta metro",
        tradition=Tradition.TIBETAN,
        notes=(
            "Atlanta Shambhala Meditation Center is a contemplative community in the Shambhala "
            "lineage of Chögyam Trungpa Rinpoche, located in a charming bungalow in Decatur "
            "(just east of Atlanta proper). Offers drop-in public meditation on Sundays "
            "(10am–noon), Tuesdays (7–8:30pm), and Fridays (noon–1pm). Also hosts the One "
            "Breath Group (Mon/Wed/Thu), monthly BIPOC Sangha, monthly Queer Dharma group, "
            "and Shambhala Training weekends. Open to all; drop-in welcome."
        ),
    ),
    "aszc": Center(
        id="aszc",
        name="Atlanta Soto Zen Center",
        url="https://www.aszc.org",
        address="1167 Zonolite Pl NE, Suite C",
        city="Atlanta",
        state="GA",
        zip_code="30306",
        lat=33.8060,
        lng=-84.3420,
        neighborhood="Morningside / Lenox",
        tradition=Tradition.ZEN,
        notes=(
            "Atlanta Soto Zen Center (ASZC) is one of Atlanta's longest-running Zen centers, "
            "founded in 1977 in the Soto Zen tradition. Offers daily zazen including a morning "
            "Sunrise Sangha (6am, hybrid in-person + Zoom), Wednesday evening Introduction to "
            "Zen Meditation (7–8:30pm, in-person drop-in), and Sunday Morning Service (9am–noon, "
            "hybrid). Monthly Just Sit Saturdays and Roshi seminars. Located in Morningside "
            "near Piedmont Park. Drop-in welcome; newcomers' orientation offered monthly."
        ),
    ),
    "kmc_georgia": Center(
        id="kmc_georgia",
        name="Kadampa Meditation Center Georgia",
        url="https://www.meditationingeorgia.org",
        address="741 Edgewood Ave NE",
        city="Atlanta",
        state="GA",
        zip_code="30307",
        lat=33.7565,
        lng=-84.3560,
        neighborhood="Inman Park / Old Fourth Ward",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Georgia (KMC Georgia) is a Tibetan Buddhist center in the "
            "New Kadampa Tradition (NKT-IKBU), located in the Inman Park neighborhood near "
            "BeltLine access. Offers weekly drop-in General Program classes: Sunday 'Advice for "
            "a Happy Life' (10:30–11:45am), Tuesday 'Meditation for Beginners' (7–8pm), and "
            "Wednesday 'Modern Buddhism and Meditation' (7–8:15pm). All sessions include guided "
            "meditation and Buddhist teachings. Drop-in fee: $15 general, $5 students/seniors, "
            "free for members."
        ),
    ),
    "red_clay_sangha": Center(
        id="red_clay_sangha",
        name="Red Clay Sangha",
        url="https://www.redclaysangha.org",
        address="3315 Chamblee Dunwoody Rd",
        city="Chamblee",
        state="GA",
        zip_code="30341",
        lat=33.8895,
        lng=-84.2984,
        neighborhood="Chamblee / Atlanta metro",
        tradition=Tradition.PLURALIST,
        notes=(
            "Red Clay Sangha is a vibrant multi-tradition Buddhist community in Chamblee (NE Atlanta "
            "metro), drawing from Theravada, Chan/Zen, and Plum Village (Thich Nhat Hanh) lineages. "
            "Weekly events include Sunday Morning Meditation, Talk and Service (9am, hybrid in-person "
            "+ Zoom) and the Peach Blossom Sangha's Mindfulness Practice in the Plum Village "
            "Tradition (Sundays 5pm, hybrid). Also hosts monthly Insight Dialog Practice Group "
            "(3rd Monday 7pm, Zoom), day retreats, and community events. Drop-in welcome at all "
            "sitting sessions."
        ),
    ),
    "drepung_loseling_atlanta": Center(
        id="drepung_loseling_atlanta",
        name="Drepung Loseling Institute",
        url="https://www.drepung.org",
        address="1781 Dresden Dr NE",
        city="Atlanta",
        state="GA",
        zip_code="30319",
        lat=33.8505,
        lng=-84.3247,
        neighborhood="Brookhaven / Lynwood Hills",
        tradition=Tradition.TIBETAN,
        notes=(
            "Drepung Loseling Institute is one of the foremost Tibetan Buddhist institutions in "
            "North America, established in Atlanta in 1988 by His Holiness the Dalai Lama. The "
            "center is home to resident Gelugpa monks and is a partner institution with Emory "
            "University's Contemplative Studies and Mind & Life Institute. Open public programs "
            "include Sunday 11am Meditation (in-person + livestream) and Tuesday 7pm Public Talk "
            "series by resident geshe Ngawang Phende (in-person + livestream). Monthly Tsog "
            "ceremonies, retreats, and visiting teacher programs also offered."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "shambhala_atlanta": {
        "url": "https://shambhala-koeln.de/ical.php?center=196",
        "center_id": "shambhala_atlanta",
        "filter_to_sits": True,
    },
}

# ---------------------------------------------------------------------------
# Wild Apricot RSS feeds
# ---------------------------------------------------------------------------

RSS_FEEDS = {
    "red_clay_sangha": {
        "url": "https://redclaysangha.org/Calendar/RSS",
        "center_id": "red_clay_sangha",
        # Keywords that identify meditation sits in the title
        "title_keywords": [
            "Sunday Morning Meditation",
            "Mindfulness Practice in the Plum Village",
            "Insight Dialog",
            "Day Retreat",
            "Vesak",
        ],
        "filter_to_sits": True,
        "duration_min": 90,
    },
}

# ---------------------------------------------------------------------------
# Static HTML scrapers (LLM-assisted)
# ---------------------------------------------------------------------------

STATIC_HTML_FEEDS = {
    "drepung_loseling_atlanta": {
        "url": "https://www.drepung.org/changing/calendar/current.htm",
        "center_id": "drepung_loseling_atlanta",
        "filter_to_sits": True,
    },
}
