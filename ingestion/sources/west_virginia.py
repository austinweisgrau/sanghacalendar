"""
West Virginia — Phase 3 expansion (heartbeat 122).

WV is thinly covered but has three notable Buddhist practice communities:
  - Bhavana Society, a significant Theravada forest monastery in the mountains
  - Morgantown Buddhist Meditation Group, a Korean Zen + Tibetan group near WVU
  - The Mindfulness Tree, a Plum Village community in Charleston

Centers included:
  - bhavana_society
    Theravada Forest Monastery (Bhante Gunaratana lineage)
    97 Meditation Trail, High View WV 26808
    Residential retreats (free) — no weekly public sits at the monastery.
    LIVE iCal feed: bhavanasociety.org/events/?ical=1 (WordPress Events Calendar)

  - morgantown_buddhist_meditation
    Korean Zen + Kagyu/Nyingma Tibetan (Pahok Jon Reed + Bhaddaka Rodger Dotson)
    429 Warrick St / Unitarian Universalist Fellowship, Morgantown WV 26505
    Wed 5:45–6:45pm + Thu 7–8:30pm + 3rd Sat 9am–noon
    No iCal (Wix site); recurring sits seeded.

  - mindfulness_tree_charleston
    Plum Village / Thich Nhat Hanh tradition (Dr. Christine Blice-Baum)
    1600 Kanawha Blvd E / Trinity Evangelical Lutheran Church, Charleston WV 25311
    Tue 10:00–11:00am (in-person + online)
    No iCal; recurring sit seeded.

Research notes (2026-11-13):
  - Bhavana Society: Founded 1985 by Bhante Henepola Gunaratana (author of
    "Mindfulness in Plain English"). One of the most significant Theravada
    forest monasteries in North America. Located at 97 Meditation Trail, High
    View WV 26808 (Hardy County, Appalachian Mountains, ~2.5 hrs from DC).
    Offers year-round residential retreats (free, dana-based), all-day sittings,
    and community events. No regular drop-in public sits. WordPress Events
    Calendar iCal confirmed at bhavanasociety.org/events/?ical=1 (200 OK,
    text/calendar). filter_to_sits=False — include all retreat events.
  - Morgantown Buddhist Meditation Group: Two lineages in one sangha.
    Pahok Jon Reed (Korean Zen, Kwan Um lineage) and Bhaddaka Rodger Dotson
    (Tibetan Kagyu/Nyingma, trained under Traleg Rinpoche). Thursday evening
    Study Group at Friends Meeting House, 648 E. Brockway Ave. Wednesday
    Evening Practice and 3rd Saturday Half-Day Retreats at UU Fellowship,
    429 Warrick St. Morgantown WV (pop. 32k, home of WVU).
    Website: morgantownbuddhism.wixsite.com/morgantownmeditation (Wix, no iCal).
  - The Mindfulness Tree: Plum Village / TNH tradition. Weekly sit Tuesdays
    10:00–11:00am (in-person + Zoom), at Trinity Evangelical Lutheran Church,
    1600 Kanawha Blvd E, Charleston WV 25311. Run by The Mindfulness Tree
    Charleston WV LLC. Formerly the Meditation Circle met here (closed 2022);
    Mindfulness Tree is the active group now. Website: themindfulnesstree.life.
  - The Meditation Circle (Charleston): CLOSED June 2022; skip.
  - Bhavana Society Saturday community sittings: occasional but not regular;
    retreats are the primary offering; iCal covers all events.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "bhavana_society": Center(
        id="bhavana_society",
        name="Bhāvanā Society",
        url="https://bhavanasociety.org",
        address="97 Meditation Trail",
        city="High View",
        state="WV",
        zip_code="26808",
        lat=39.1740,
        lng=-78.5780,
        neighborhood="Hardy County (Appalachian Mountains)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Bhāvanā Society is a Theravāda Buddhist forest monastery in the Appalachian "
            "Mountains of West Virginia, founded in 1985 by Bhante Henepola Gunaratana "
            "(author of 'Mindfulness in Plain English'). One of the most significant "
            "Theravada retreat centers in North America. Located at 97 Meditation Trail, "
            "High View WV 26808 (Hardy County, ~2.5 hours from Washington DC). "
            "Offers year-round residential retreats (all-inclusive, free / dana-based), "
            "day-long sittings, Vesak celebrations, and other community events. "
            "Retreats accommodate up to 50 participants (25 women, 25 men). "
            "No regular drop-in weekly sits; advance registration required for retreats. "
            "bhavanasociety.org."
        ),
    ),
    "morgantown_buddhist_meditation": Center(
        id="morgantown_buddhist_meditation",
        name="Morgantown Buddhist Meditation Group",
        url="https://morgantownbuddhism.wixsite.com/morgantownmeditation",
        address="429 Warrick St",
        city="Morgantown",
        state="WV",
        zip_code="26505",
        lat=39.6355,
        lng=-79.9557,
        neighborhood="WVU Area",
        tradition=Tradition.ZEN,
        notes=(
            "Morgantown Buddhist Meditation Group serves the Morgantown WV / WVU community "
            "with two lineages: Korean Zen under Pahok Jon Reed (Kwan Um lineage) and "
            "Kagyu/Nyingma Tibetan Buddhism under Bhaddaka Rodger Dotson (Traleg Rinpoche "
            "lineage). Wednesday Evening Practice (5:45–6:45pm) and 3rd Saturday Half-Day "
            "Retreats (9:00am–noon) are held at the Unitarian Universalist Fellowship, "
            "429 Warrick St. Thursday Study Group (7:00–8:30pm) meets at Friends Meeting "
            "House, 648 E. Brockway Ave. All sessions drop-in and free. "
            "morgantownbuddhism.wixsite.com/morgantownmeditation."
        ),
    ),
    "mindfulness_tree_charleston": Center(
        id="mindfulness_tree_charleston",
        name="The Mindfulness Tree",
        url="https://themindfulnesstree.life",
        address="1600 Kanawha Blvd E",
        city="Charleston",
        state="WV",
        zip_code="25311",
        lat=38.3493,
        lng=-81.6224,
        neighborhood="Kanawha City",
        tradition=Tradition.ZEN,
        notes=(
            "The Mindfulness Tree is a Plum Village / Thich Nhat Hanh tradition community "
            "in Charleston, WV (Kanawha City). Weekly sit at Trinity Evangelical Lutheran "
            "Church (1600 Kanawha Blvd E): Tuesdays 10:00–11:00am, in-person and online "
            "via Zoom. Format: inviting the bell, seated meditation, walking meditation, "
            "dharma talk, and dharma sharing. Also offers occasional online-only gatherings "
            "(1st Wednesday of month, 10:00–10:45am). MBSR classes and private instruction "
            "also available. Free / open to all. themindfulnesstree.life."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "bhavana_society": {
        "url": "https://bhavanasociety.org/events/?ical=1",
        "filter_to_sits": False,  # retreats — include all; enrichment will classify
    },
}

# No Eventbrite or static HTML scrapers for this state.
EVENTBRITE_FEEDS: dict = {}
STATIC_HTML_FEEDS: dict = {}
