"""
Virginia Beach / Hampton Roads, VA — Phase 3 expansion (heartbeat 88).

Hampton Roads (pop. ~1.8M metro) encompasses Virginia Beach, Norfolk, Chesapeake,
Newport News, Hampton, and surrounding cities. The area is home to a small but
diverse Buddhist community spanning Theravada, Vietnamese Mahayana, and
Plum Village lineages.

Centers included:
  - Shakyamuni Buddhist Meditation Monastery (shakyamuni_vb)
    Theravada (Sri Lankan lineage)
    3285 Dam Neck Road, Virginia Beach, VA 23453
    vbmeditation.org · Wednesday 7pm English public sit

  - Mindfulness Community of Hampton Roads (mindfulness_community_hr)
    Plum Village / Thich Nhat Hanh lineage (Order of Interbeing)
    612 Westover Avenue, Norfolk, VA 23507
    mindfulnesscommunityofhamptonroads.com · 1st & 3rd Sunday 10:30am

  - Dong Hung Temple / Buddhist Education Center of America (dong_hung_vb)
    Vietnamese Mahayana / Pureland-Zen
    423 Davis Street, Virginia Beach, VA 23462
    buddhistedu.org · Sunday 7:45am English service + 2nd Saturday 10am

Research notes (2026-07-16):
  - Shakyamuni Buddhist Meditation Monastery: Founded 2019. Resident monk at 3285 Dam
    Neck Road, Virginia Beach VA 23453. Two main public programs: Wednesday 7–8:30pm
    (English-language: chanting, breathing meditation, insight meditation, dharma talk;
    free, open to all) and Saturday 6–8:30pm (Sinhalese/Pali language). Contact:
    info@vbmeditation.org / (301) 691-8899. No iCal feed; static HTML site. Seeded
    Wednesday English sit as recurring.
  - Mindfulness Community of Hampton Roads: Founded 1992. Plum Village / Thich Nhat
    Hanh sangha at 612 Westover Avenue, Norfolk VA 23507 (private home in Ghent
    neighborhood, rear door). 1st and 3rd Sunday monthly 10:30am–12:30pm: sitting
    meditation, walking meditation, dharma talk video, dharma sharing, sutra reading.
    Contact Allen Sandler: asandler@odu.edu / (757) 333-1501. No iCal; seeded as
    recurring (1st/3rd Sunday).
  - Dong Hung Temple: Founded 1998 by Ven. Thich Thong Kinh. 423 Davis Street, Virginia
    Beach VA 23462. English sangha: Sunday morning services 7:45–8:45am in Buddha Hall
    (chanting, meditation, dharma sharing). 2nd Saturday 10–11am Meditation Hour.
    Contact English sangha: dhtenglishsangha@gmail.com / (757) 689-3408. No iCal;
    seeded Sunday English service + 2nd Saturday meditation as recurring.
  - Keajra Kadampa / Meditation in Coastal VA (156 Newtown Road, Virginia Beach): website
    possibly compromised (spam-injected pages in search results). Now a branch of KMC-DC
    (meditation-dc.org). Deferred until status clarified.
  - Ratnashri Sangha Circle (Drikung Kagyu, Norfolk): website down (ECONNREFUSED).
    Likely dormant. Skipped.
  - Deep Ocean Zendo (Soto Zen, Virginia Beach): Explicitly closed per Facebook page.
    Skipped.
  - Zen Group of Virginia Beach (Chapel Hill Zen Center affiliate): No current address
    confirmed; schedule unverified. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shakyamuni_vb": Center(
        id="shakyamuni_vb",
        name="Shakyamuni Buddhist Meditation Monastery",
        url="https://www.vbmeditation.org",
        address="3285 Dam Neck Road",
        city="Virginia Beach",
        state="VA",
        zip_code="23453",
        lat=36.7619,
        lng=-76.0590,
        neighborhood="Dam Neck",
        tradition=Tradition.THERAVADA,
        notes=(
            "Shakyamuni Buddhist Meditation Monastery is a Theravada Buddhist center "
            "with resident monk at 3285 Dam Neck Road, Virginia Beach VA 23453. "
            "Founded in 2019. Primary English-language public sit: Wednesday 7–8:30pm "
            "(chanting, breathing meditation, insight meditation, music meditation, "
            "dharma talk; free, open to all). Saturday 6–8:30pm is conducted in "
            "Sinhalese/Pali for the Sri Lankan community. All activities free. "
            "Contact: info@vbmeditation.org / (301) 691-8899. vbmeditation.org."
        ),
    ),
    "mindfulness_community_hr": Center(
        id="mindfulness_community_hr",
        name="Mindfulness Community of Hampton Roads",
        url="https://mindfulnesscommunityofhamptonroads.com",
        address="612 Westover Avenue",
        city="Norfolk",
        state="VA",
        zip_code="23507",
        lat=36.8591,
        lng=-76.3000,
        neighborhood="Ghent",
        tradition=Tradition.ZEN,
        notes=(
            "Mindfulness Community of Hampton Roads is a Plum Village / Thich Nhat "
            "Hanh sangha practicing in the Order of Interbeing tradition. Founded 1992. "
            "Meets the 1st and 3rd Sunday of each month, 10:30am–12:30pm, at a private "
            "home in Norfolk's Ghent neighborhood (612 Westover Avenue; enter at rear "
            "door). Program includes sitting meditation, walking meditation, a dharma "
            "talk video, dharma sharing, and sutra reading. All welcome; free. "
            "Contact: Allen Sandler, asandler@odu.edu / (757) 333-1501. "
            "mindfulnesscommunityofhamptonroads.com."
        ),
    ),
    "dong_hung_vb": Center(
        id="dong_hung_vb",
        name="Dong Hung Temple — Buddhist Education Center of America",
        url="https://www.buddhistedu.org",
        address="423 Davis Street",
        city="Virginia Beach",
        state="VA",
        zip_code="23462",
        lat=36.8184,
        lng=-76.1108,
        neighborhood="Kemps River",
        tradition=Tradition.MAHAYANA,
        notes=(
            "Dong Hung Temple (Đông Hưng Temple) / Buddhist Education Center of "
            "America is a Vietnamese Mahayana temple in Virginia Beach founded in "
            "1998 by Venerable Thich Thong Kinh. Offers English-language sangha "
            "programs including Sunday morning meditation services (7:45–8:45am in "
            "the Buddha Hall: chanting, meditation, dharma sharing, teaching) and a "
            "2nd Saturday Meditation Hour (10–11am). Vietnamese-language community "
            "services also held Sunday mornings. Contact English sangha: "
            "dhtenglishsangha@gmail.com / (757) 689-3408. buddhistedu.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

# No iCal feeds available for Hampton Roads centers. All sits seeded as recurring.
ICAL_FEEDS: dict = {}
