"""
Boston/Cambridge meditation center sources — Phase 3 Boston expansion.
Defines known Boston-area centers and their ingestion strategies.
"""

import logging

from data.schemas.event import Center, Tradition

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_boston": Center(
        id="shambhala_boston",
        name="Boston Shambhala Meditation Center",
        url="https://boston.shambhala.org",
        address="646 Brookline Ave",
        city="Brookline",
        state="MA",
        zip_code="02445",
        lat=42.3435,
        lng=-71.1286,
        neighborhood="Brookline Village",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Buddhist center (Chögyam Trungpa lineage). "
            "Nyinthün Sunday morning meditation 9am–12pm; Wednesday Open Dharma Gathering 7–8:30pm; "
            "Heart of Recovery (Mondays 7:30–9pm); LGBTQ+ Meditation Group 1st/3rd Tuesdays 7–8:30pm; "
            "Sangha Sunday 2nd Sundays; Learn to Meditate 1st Sundays 12:30pm."
        ),
    ),
    "gbzc": Center(
        id="gbzc",
        name="Greater Boston Zen Center",
        url="https://bostonzen.org",
        address="552 Massachusetts Ave, Suite 208",
        city="Cambridge",
        state="MA",
        zip_code="02139",
        lat=42.3638,
        lng=-71.1059,
        neighborhood="Central Square",
        tradition=Tradition.ZEN,
        notes=(
            "Greater Boston Zen Center (GBZC) — non-residential urban Zen community in Cambridge's "
            "Central Square. Soto/Rinzai Zen teachers from multiple lineages. Tuesday Evening Program "
            "7–9pm (hybrid in-person + Zoom); Saturday Morning Program 9–9:50am (online); "
            "monthly all-day zazenkai. Dana-based (pay what you can)."
        ),
    ),
    "cimc": Center(
        id="cimc",
        name="Cambridge Insight Meditation Center",
        url="https://cambridgeinsight.org",
        address="331 Broadway",
        city="Cambridge",
        state="MA",
        zip_code="02139",
        lat=42.3652,
        lng=-71.1107,
        neighborhood="MIT/Cambridgeport",
        tradition=Tradition.THERAVADA,
        notes=(
            "CIMC is one of the most respected urban Vipassana centers in North America, founded by "
            "Larry Rosenberg and part of the IMS/Spirit Rock lineage. Offers drop-in evening sits "
            "Mon/Tue/Thu/Fri 6–6:45pm, Monday Sitting & Sangha 6–7:15pm, Wednesday Evening Dharma "
            "6:30–8:45pm, Thursday Morning Retreat 9am–1pm, and Sunday Extended Practice 2–5:15pm. "
            "All events by donation. Strong community of experienced practitioners."
        ),
    ),
    "cambridge_zen": Center(
        id="cambridge_zen",
        name="Cambridge Zen Center",
        url="https://cambridgezen.org",
        address="199 Auburn St",
        city="Cambridge",
        state="MA",
        zip_code="02139",
        lat=42.3620,
        lng=-71.1176,
        neighborhood="Cambridgeport",
        tradition=Tradition.ZEN,
        notes=(
            "Cambridge Zen Center — residential Zen community in the Kwan Um School of Zen lineage "
            "(Korean Soto Zen). Tuesday Evening Zazen 7:30–8:40pm (hybrid in-person + Zoom); "
            "Thursday Evening 6:45pm instruction + 7:30pm Zoom sit; "
            "Sunday Morning Zazen 9am (4 x 30-min sits, hybrid). Monthly weekend retreats. "
            "Daily practice schedule for residents. Drop-in welcome."
        ),
    ),
    "kadampa_boston": Center(
        id="kadampa_boston",
        name="Kadampa Meditation Center Boston",
        url="https://meditationinboston.org",
        address="2298 Massachusetts Ave",
        city="Cambridge",
        state="MA",
        zip_code="02140",
        lat=42.3852,
        lng=-71.1248,
        neighborhood="North Cambridge",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Boston (KMCB) — New Kadampa Tradition (NKT-IKBU). "
            "Wednesday Evening Meditation classes; Sunday meditation sessions; "
            "study programs and workshops. Resident Teacher: Gen Kelsang Khedrub. "
            "Drop-in meditation classes welcome, beginners especially encouraged."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Phase 3 Boston — iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "shambhala_boston": {
        # Shambhala central iCal server (shambhala-koeln.de), center=204
        # Verified working 2026-05-06 — returns valid VCALENDAR with current events
        "url": "https://shambhala-koeln.de/ical.php?center=204",
        "filter_to_sits": True,
    },
}
