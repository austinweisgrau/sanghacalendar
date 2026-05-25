"""
Knoxville, TN — Phase 3 expansion (heartbeat 66).

Knoxville (pop. ~200k; metro ~900k) is home to the University of Tennessee and a
modest but genuine Buddhist community spanning Plum Village Zen, NKT Kadampa,
multi-tradition vipassana, and a Tibetan Gelug center. No live iCal feeds found —
all ingested via seeded recurring sits.

Centers included:
  - Mountain Solid, Water Reflecting Sangha (mountain_solid_water_reflecting)
    Plum Village / Thich Nhat Hanh lineage
    West Knoxville Friends Meeting House, 1517 Meeting House Rd, Knoxville TN 37909
    knoxmindful.org · Weekly Sunday 4:00–5:30pm (in-person + Zoom)

  - Knoxville Community of Mindfulness (knoxville_community_mindfulness)
    Multi-tradition (Vipassana, Zen, Dzogchen); led by John Blackburn
    Meaningful Life Center, 116 Carr St, Knoxville TN
    knoxcomind.org · 1st & 3rd Thursday 6:30–8:00pm (in-person + Zoom)

  - Je Tsongkhapa Kadampa Buddhist Center – Knoxville (je_tsongkhapa_knoxville)
    NKT / New Kadampa Tradition (outreach from KMC Asheville)
    OASIS Institute, 4918 Homberg Dr, Knoxville TN
    meditationinasheville.org · Weekly Tuesday 7:15–8:30pm (in-person)

  - Lotus Light Contemplative Community Center (lotus_light_knoxville)
    Multi-tradition hub; home to Losel Shedrup Ling (Gelug Tibetan) + other groups
    501 Arthur St, Knoxville TN 37921
    lotuslightcenter.org · Insight Meditation Mon 7–8:30pm; Zazen Sun 4–5pm

Research notes (2026-05-25):
  - Mountain Solid, Water Reflecting Sangha: Active since 1998. Plum Village / Order of
    Interbeing. Weekly Sunday 4–5:30pm at the Quaker Meeting House, West Knoxville.
    1st Sundays: book discussion. 2nd Sundays: recitation of Mindfulness Trainings +
    mindful eating potluck. Hybrid in-person + Zoom (join.zoom.us/j/83488445440,
    passcode 800925). No iCal.
  - Knoxville Community of Mindfulness: Led by John Blackburn (50+ years practice,
    Vipassana/Zen/Dzogchen). Meets at Meaningful Life Center (116 Carr St, Knoxville TN).
    1st and 3rd Thursdays in-person + every Thursday on Zoom, 6:30–8pm. Courses offered
    on Four Noble Truths, Metta, Lojong, etc. No iCal; website only.
  - Je Tsongkhapa Kadampa Buddhist Center: NKT outreach from KMC Asheville (NC). Weekly
    Tuesday 7:15–8:30pm drop-in at OASIS Institute, 4918 Homberg Dr, Knoxville TN. Classes
    based on Kadampa Buddhist philosophy, open to all. No iCal; managed via Asheville KMC.
  - Lotus Light Contemplative Community Center: Community hub at 501 Arthur St, Knoxville
    TN 37921 (Mechanicsville, ~1 mi west of UT campus). Home to Losel Shedrup Ling (Gelug
    Tibetan Buddhist Center of Knoxville, lslk.org) and independent groups. Regular weekly
    groups include Insight Meditation (Mon 7pm), Zazen (Sun 4pm), Chenrezig practice
    (Wed 6pm), Recovery Dharma (multiple times). iCal feed exists but malformed (PHP errors).
  - Losel Shedrup Ling (lslk.org): Gelug Tibetan Buddhist center co-located with Lotus
    Light. Weekly meetings for meditation + Buddhist text discussion; schedule not published
    online — deferred pending contact.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "mountain_solid_water_reflecting": Center(
        id="mountain_solid_water_reflecting",
        name="Mountain Solid, Water Reflecting Sangha",
        url="https://www.knoxmindful.org",
        address="1517 Meeting House Rd",
        city="Knoxville",
        state="TN",
        zip_code="37909",
        lat=35.9388,
        lng=-84.0801,
        neighborhood="West Knoxville",
        tradition=Tradition.ZEN,
        notes=(
            "Mountain Solid, Water Reflecting Sangha is a Plum Village / Order of "
            "Interbeing community practicing in the tradition of Thich Nhat Hanh "
            "since 1998. Weekly Sunday 4:00–5:30pm at the West Knoxville Friends "
            "Meeting House. 1st Sundays include book discussion; 2nd Sundays feature "
            "recitation of the Mindfulness Trainings followed by mindful eating and "
            "potluck. All are welcome; no experience or reservation required. "
            "In-person + Zoom (join.zoom.us/j/83488445440, passcode 800925)."
        ),
    ),
    "knoxville_community_mindfulness": Center(
        id="knoxville_community_mindfulness",
        name="Knoxville Community of Mindfulness",
        url="https://www.knoxcomind.org",
        address="116 Carr St",
        city="Knoxville",
        state="TN",
        zip_code="37919",
        lat=35.9837,
        lng=-83.9424,
        neighborhood="Old North Knoxville",
        tradition=Tradition.OTHER,
        notes=(
            "Knoxville Community of Mindfulness is a multi-tradition sangha led by "
            "John Blackburn, who has practiced for over 50 years in the Vipassana, "
            "Zen, and Dzogchen traditions. Meets at the Meaningful Life Center "
            "(116 Carr St, Knoxville). 1st and 3rd Thursdays in-person, 6:30–8pm; "
            "weekly Thursdays also available on Zoom. Courses offered throughout "
            "the year on meditation, the Four Noble Truths, Metta, Lojong, and "
            "more. All traditions welcome; no charge to attend."
        ),
    ),
    "je_tsongkhapa_knoxville": Center(
        id="je_tsongkhapa_knoxville",
        name="Je Tsongkhapa Kadampa Buddhist Center – Knoxville",
        url="https://www.meditationinasheville.org/tuesday-evening-drop-in-meditation-class-knoxville-tn/",
        address="4918 Homberg Dr",
        city="Knoxville",
        state="TN",
        zip_code="37919",
        lat=35.9488,
        lng=-84.0165,
        neighborhood="Bearden",
        tradition=Tradition.TIBETAN,
        notes=(
            "Je Tsongkhapa Kadampa Buddhist Center holds a weekly Tuesday evening "
            "drop-in meditation class in Knoxville, an outreach program of KMC "
            "Asheville (NC). Classes run 7:15–8:30pm at the OASIS Institute "
            "(4918 Homberg Dr, Bearden). Teachings draw from the New Kadampa "
            "Tradition; no Buddhist background needed to attend. Part of the "
            "worldwide network of over 1,300 NKT-IKBU centers."
        ),
    ),
    "lotus_light_knoxville": Center(
        id="lotus_light_knoxville",
        name="Lotus Light Contemplative Community Center",
        url="https://lotuslightcenter.org",
        address="501 Arthur St",
        city="Knoxville",
        state="TN",
        zip_code="37921",
        lat=35.9764,
        lng=-83.9567,
        neighborhood="Mechanicsville",
        tradition=Tradition.OTHER,
        notes=(
            "Lotus Light Contemplative Community Center is a multi-tradition hub "
            "in Knoxville's Mechanicsville neighborhood (~1 mile west of UT campus). "
            "Home to Losel Shedrup Ling (Gelug Tibetan Buddhist Center of Knoxville) "
            "and several independent practice groups. Regular weekly offerings "
            "include Insight Meditation (Mondays 7pm), Zazen (Sundays 4pm), "
            "Chenrezig Compassion Practice (Wednesdays 6pm), and Recovery Dharma "
            "(multiple times weekly). Dharma talks, book groups, and visiting "
            "teachers throughout the year."
        ),
    ),
}

# No live iCal feeds available — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
