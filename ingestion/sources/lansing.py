"""
Lansing / East Lansing / Okemos, Michigan — Phase 3 expansion (heartbeat 102).

Michigan's state capital (~112k city, ~540k metro) has a modest but genuine
Buddhist community spanning Plum Village Zen, Japanese Zen, and Theravada.
Michigan State University (East Lansing) draws practitioners to the area.

Centers included:
  - Lansing Area Mindfulness Community / LAMC (lamc)
    Plum Village / Thich Nhat Hanh lineage
    Van Hanh Temple, 3015 S. Martin Luther King Jr. Blvd, Lansing MI 48910
    lamc.info · Wednesday 7–9pm (in-person + Zoom)

  - Michigan Zen Center (michigan_zen_center)
    Japanese Zen (lay-led, ordained priest Ryunen Don Davis since 2002)
    2254 Hamilton Road, Okemos MI 48864 (~5 mi from MSU campus)
    michiganzencenter.com · Sunday 9am

  - Dhammasala Forest Monastery (dhammasala_forest_monastery)
    Theravada / Thai Forest Tradition (Dhammayut order)
    14780 Beardslee Road, Perry MI 48872 (~20 mi northeast of Lansing)
    dhammasala.org · Saturday 5:30–6:30pm Dhamma class (public)

Research notes (2026-09-10):
  - LAMC (lamc.info): Active Plum Village sangha meeting at the Vietnamese
    American Buddhist Association's Van Hanh Temple. Wednesday 7–9pm: walking
    meditation, sitting, dharma discussion. Hybrid in-person + Zoom. No iCal
    feed — static HTML on lamc.info/weeklypractice. Most active beginner-
    friendly public group in Lansing.
  - Michigan Zen Center (michiganzencenter.com): Led by ordained Zen priest
    Ryunen Don Davis. Sunday 9am service (zazen, dharma talk). JS-heavy site,
    no iCal. Small community in Okemos township adjacent to East Lansing.
  - Dhammasala Forest Monastery (dhammasala.org): Thai Forest Theravada
    (Dhammayut order) on 28 acres in Perry MI, ~20 miles NE of Lansing.
    Saturday 5:30–6:30pm Dhamma class open to public. Available for individual/
    group retreats May–September. Genuine monastic community; static HTML
    calendar. Only traditional Theravada forest monastery in the Lansing region.
  - Ananda Michigan / SRF Lansing (Yogananda lineage): skipped — Hindu-derived,
    not Buddhist.
  - Dharma Drum Mountain Michigan (East Lansing): likely dormant, unverified.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "lamc": Center(
        id="lamc",
        name="Lansing Area Mindfulness Community",
        url="https://lamc.info",
        address="3015 S. Martin Luther King Jr. Blvd",
        city="Lansing",
        state="MI",
        zip_code="48910",
        lat=42.7025,
        lng=-84.5486,
        neighborhood=None,
        tradition=Tradition.ZEN,
        notes=(
            "Lansing Area Mindfulness Community (LAMC) is a Plum Village / Thich Nhat "
            "Hanh lineage sangha meeting at Van Hanh Temple (Chua Van Hanh), the Vietnamese "
            "American Buddhist Association's meditation hall in Lansing. Wednesday evenings "
            "7:00–9:00 PM: 15 minutes walking meditation, 30 minutes sitting, followed by "
            "dharma discussion. Hybrid in-person and Zoom. Beginner-friendly, drop-in "
            "welcome, no experience needed. Free. info@lamc.info. lamc.info."
        ),
    ),
    "michigan_zen_center": Center(
        id="michigan_zen_center",
        name="Michigan Zen Center",
        url="https://michiganzencenter.com",
        address="2254 Hamilton Road",
        city="Okemos",
        state="MI",
        zip_code="48864",
        lat=42.7083,
        lng=-84.4044,
        neighborhood="Okemos (East Lansing metro)",
        tradition=Tradition.ZEN,
        notes=(
            "Michigan Zen Center is a Japanese-lineage Zen community in Okemos, immediately "
            "adjacent to East Lansing (~5 miles from Michigan State University campus). Led "
            "by ordained Zen priest Ryunen Don Davis since 2002. Sunday morning service at "
            "9:00 AM: zazen, liturgy, dharma talk. Drop-in welcome. "
            "contact@michiganzencenter.com. michiganzencenter.com."
        ),
    ),
    "dhammasala_forest_monastery": Center(
        id="dhammasala_forest_monastery",
        name="Dhammasala Forest Monastery",
        url="https://dhammasala.org",
        address="14780 Beardslee Road",
        city="Perry",
        state="MI",
        zip_code="48872",
        lat=42.8190,
        lng=-84.3530,
        neighborhood="Perry (Lansing metro, ~20 mi NE)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Dhammasala Forest Monastery (Wat Dhammasala) is a Thai Forest Theravada "
            "monastery in the Dhammayut order, on 28 acres of forested land in Perry MI, "
            "about 20 miles northeast of Lansing. Saturday Dhamma Class (5:30–6:30 PM) is "
            "open to the public: guided meditation, Dhamma teaching, and informal discussion. "
            "Also open for individual and group retreats May–September. Resident monks "
            "present year-round. The only traditional Theravada forest monastery in the "
            "greater Lansing region. Phone: (517) 675-1010. "
            "dhammasala.forest.monastery@gmail.com. dhammasala.org."
        ),
    ),
}

# No live iCal feeds — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
