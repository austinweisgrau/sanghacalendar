"""
Lubbock, Texas — Phase 3 expansion.

Lubbock is a mid-sized West Texas city (~260k metro) anchored by Texas Tech
University. The Buddhist scene is modest but has one well-established center.

Centers included:
  - bodhichitta_kadampa_lubbock — New Kadampa Tradition (NKT) Tibetan
    6701 Aberdeen Avenue Suite 3, Lubbock TX 79424
    meditationinlubbock.org
    Mon 6:30pm, Tue 6:30pm evening classes; Mon/Wed/Fri 7:20am morning meditation.
    No iCal (Cloudflare-blocked site); recurring sits seeded.

Research notes (2026-09-16):
  - Bodhichitta Kadampa: Founded ~2010 as branch class of KMC Texas (Arlington).
    Resident teacher Erica Richardson. Full weekly drop-in schedule open to all.
    Website (meditationinlubbock.org) returns 403 Cloudflare challenge — no iCal
    accessible. Schedule reconstructed from search snippets + parent site.
  - Empty Plains Zen Center: Sanbo Zen, contact Robby Duncan (806-577-3511).
    Previously met at St. Johns UMC (1501 University Ave). Page now 404; status
    uncertain. Skip pending confirmation.
  - No Shambhala, Theravada, Insight Meditation, or independent Zen center found.
  - "Buddhist Center Lubbock Texas" Facebook page (~4,465 likes) unidentified;
    may be ethnic temple or general page. Investigate if accessible.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "bodhichitta_kadampa_lubbock": Center(
        id="bodhichitta_kadampa_lubbock",
        name="Bodhichitta Kadampa Buddhist Center",
        url="https://meditationinlubbock.org",
        address="6701 Aberdeen Avenue, Suite 3",
        city="Lubbock",
        state="TX",
        zip_code="79424",
        lat=33.5410,
        lng=-101.9095,
        neighborhood="SW Lubbock",
        tradition=Tradition.TIBETAN,
        notes=(
            "Bodhichitta Kadampa Buddhist Center (BKBC) is a New Kadampa Tradition "
            "(NKT) Tibetan Buddhist center in SW Lubbock, TX. Founded around 2010 as "
            "a branch class of KMC Texas (Arlington) and now an independent center "
            "with resident teacher Erica Richardson. Drop-in classes are open to all, "
            "no experience necessary. "
            "Monday evenings 6:30–7:45 PM: General Program (meditation and dharma "
            "class on modern Buddhist teachings). "
            "Tuesday evenings 6:30–7:45 PM: Tuesday Evening Meditation. "
            "Monday, Wednesday, Friday mornings 7:20–8:40 AM: Morning Meditation "
            "with Heart Jewel Prayers (devotional meditation). "
            "Thursday evenings 6:30–7:30 PM: Prayers for World Peace. "
            "Class fees typically $15 (members free). Also offers retreats and "
            "a Foundation Program for deeper study. Monthly outreach class in "
            "Midland TX. meditationinlubbock.org. Phone: (806) 787-2499."
        ),
    ),
}

# No live iCal feeds — site Cloudflare-blocked. All sits seeded as recurring
# in scripts/sangha-seed-recurring.js.
ICAL_FEEDS: dict = {}
