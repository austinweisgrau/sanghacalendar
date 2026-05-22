"""
Boise, ID — Phase 3 expansion.

Boise has a small but genuine Buddhist scene anchored by the Boise Institute
for Buddhist Studies (BIBS), a multi-tradition umbrella center that hosts
several independent sanghas under one roof. The Boise Zen Center is a
standalone Soto Zen community, and Heart of the Dharma is an active Nyingma
Tibetan center.

No live iCal feeds are accessible: all centers either have JS-rendered
calendars, Squarespace sites without iCal export, or no machine-readable
calendar at all. All sits are seeded as recurring instances via
scripts/sangha-seed-recurring.js.

Centers included:
  - Boise Zen Center (boise_zen_center) — Soto Zen (SZBA)
    1524 W. Hays Street, Suite 101a, Boise ID 83702. boisezencenter.org
    Wed 7am (hybrid), Thu 6pm (in-person), Sat 8am (hybrid).

  - Empty Gate Zen Center Boise (empty_gate_zen_boise) — Korean Zen (Kwan Um)
    at BIBS, 901 N. 15th Street, Boise ID 83702. bibscenter.org
    Mon–Thu 6:30am (hybrid), Thu 7pm (hybrid).

  - Boise Insight Sangha (boise_insight_sangha) — Insight Meditation
    at BIBS, 901 N. 15th Street, Boise ID 83702. boiseinsightsangha.wordpress.com
    Tue 6pm (in-person).

  - Beginner's Mind Sangha (beginners_mind_sangha_boise) — Plum Village
    at BIBS, 901 N. 15th Street, Boise ID 83702. beginnersmindsangha.org
    Wed 7pm (in-person), Sun 10:15am (hybrid).

  - Heart of the Dharma (heart_of_the_dharma_boise) — Nyingma Tibetan
    1627 S. Orchard St., Suite 200, Boise ID 83705. heartofdharma.org
    Sun 11am (hybrid), Tue 7pm (online).

Research notes (2026-05-22):
  - Boise Zen Center: Soto Zen (SZBA member), teacher Jisen Coghlan. At 1524
    W. Hays Street. Wednesday morning zazen (7–8:30am): in-person + Zoom.
    Thursday evening (6–7:10pm): two sitting periods in-person. Saturday
    morning (8–9:30am): in-person + Zoom. Drop-in; donation-based.
  - Empty Gate Zen Center Boise: Kwan Um School of Zen (Korean Zen), teacher
    Jeff Kitzes (Zen Master Bon Soeng). Hosted at BIBS (901 N. 15th Street).
    Mon–Thu 6:30–7:30am: sitting + kinhin, in-person + Zoom. Thu 7pm: evening
    sitting, in-person + Zoom.
  - Boise Insight Sangha: Non-sectarian Insight Meditation group, hosted at
    BIBS. Tuesday evenings 6–7:30pm: sitting + dharma discussion. Drop-in,
    open to all.
  - Beginner's Mind Sangha: Plum Village tradition (Order of Interbeing,
    Thich Nhat Hanh lineage), hosted at BIBS. Wednesday 7–8:15pm: sitting +
    walking meditation + dharma sharing. Sunday 10:15–11:45am: sitting +
    dharma discussion; third Sunday includes Three Jewels ceremony; fifth
    Sunday is a Day of Mindfulness (10:15am–2:30pm). Hybrid (in-person + Zoom).
  - Heart of the Dharma: Nyingma Tibetan Buddhist center, teacher Dana Marsh
    (ordained by Anam Thubten). At 1627 S. Orchard Street, Suite 200.
    Sunday 11am–12:15pm: public practice, in-person + livestream. Tuesday 7pm:
    online/livestream only. Active Meetup group. Squarespace site; no iCal.
  - Dzogchen Shen Pan Choling (Boise): website down, last active ~2013; skip.
  - Recovery Dharma Boise: recovery-focused, not general public sits; skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "boise_zen_center": Center(
        id="boise_zen_center",
        name="Boise Zen Center",
        url="https://www.boisezencenter.org",
        address="1524 W. Hays Street, Suite 101a",
        city="Boise",
        state="ID",
        zip_code="83702",
        lat=43.6194,
        lng=-116.2052,
        neighborhood="Downtown Boise",
        tradition=Tradition.ZEN,
        notes=(
            "Boise Zen Center is a Soto Zen community (SZBA member) in downtown "
            "Boise, guided by teacher Jisen Coghlan. Wednesday Morning (7–8:30 AM): "
            "zazen and kinhin, in-person and Zoom. Thursday Evening (6–7:10 PM): "
            "two sitting periods with kinhin, in-person. Saturday Morning (8–9:30 AM): "
            "zazen and kinhin, in-person and Zoom. First Saturday monthly includes "
            "Introduction to Meditation. Drop-in welcome; donation-based. "
            "501(c)(3) non-profit."
        ),
    ),
    "empty_gate_zen_boise": Center(
        id="empty_gate_zen_boise",
        name="Empty Gate Zen Center Boise",
        url="https://bibscenter.org",
        address="901 N. 15th Street",
        city="Boise",
        state="ID",
        zip_code="83702",
        lat=43.6218,
        lng=-116.2118,
        neighborhood="North End Boise",
        tradition=Tradition.ZEN,
        notes=(
            "Empty Gate Zen Center Boise is a Kwan Um School of Zen community "
            "(Korean Zen), hosted at the Boise Institute for Buddhist Studies "
            "(BIBS), 901 N. 15th Street. Guiding teacher Jeff Kitzes (Zen Master "
            "Bon Soeng). Mon–Thu Morning (6:30–7:30 AM): sitting and kinhin, "
            "in-person and Zoom. Thursday Evening (7 PM): evening sitting, "
            "in-person and Zoom. Drop-in welcome."
        ),
    ),
    "boise_insight_sangha": Center(
        id="boise_insight_sangha",
        name="Boise Insight Sangha",
        url="https://boiseinsightsangha.wordpress.com",
        address="901 N. 15th Street",
        city="Boise",
        state="ID",
        zip_code="83702",
        lat=43.6218,
        lng=-116.2118,
        neighborhood="North End Boise",
        tradition=Tradition.THERAVADA,
        notes=(
            "Boise Insight Sangha is an Insight Meditation group hosted at the "
            "Boise Institute for Buddhist Studies (BIBS), 901 N. 15th Street. "
            "Tuesday Evening (6–7:30 PM): sitting meditation and dharma discussion. "
            "First Saturday monthly: half-day sitting (9 AM–12:30 PM). "
            "Drop-in welcome; open to all levels."
        ),
    ),
    "beginners_mind_sangha_boise": Center(
        id="beginners_mind_sangha_boise",
        name="Beginner's Mind Sangha",
        url="https://www.beginnersmindsangha.org",
        address="901 N. 15th Street",
        city="Boise",
        state="ID",
        zip_code="83702",
        lat=43.6218,
        lng=-116.2118,
        neighborhood="North End Boise",
        tradition=Tradition.PLURALIST,
        notes=(
            "Beginner's Mind Sangha is Boise's Plum Village community, practicing "
            "in the tradition of Thich Nhat Hanh and the Order of Interbeing. "
            "Hosted at BIBS, 901 N. 15th Street. Wednesday Evening (7–8:15 PM): "
            "sitting meditation, walking meditation, and dharma sharing. Sunday "
            "Morning (10:15–11:45 AM): sitting and dharma discussion, hybrid "
            "(in-person + Zoom). Third Sunday includes Three Jewels ceremony; "
            "fifth Sunday is a Day of Mindfulness (10:15 AM–2:30 PM). Free; "
            "open to all."
        ),
    ),
    "heart_of_the_dharma_boise": Center(
        id="heart_of_the_dharma_boise",
        name="Heart of the Dharma",
        url="https://heartofdharma.org",
        address="1627 S. Orchard Street, Suite 200",
        city="Boise",
        state="ID",
        zip_code="83705",
        lat=43.5935,
        lng=-116.2210,
        neighborhood="South Boise",
        tradition=Tradition.TIBETAN,
        notes=(
            "Heart of the Dharma is a Nyingma Tibetan Buddhist center in Boise, "
            "guided by teacher Dana Marsh (ordained by Anam Thubten). Located at "
            "1627 S. Orchard Street, Suite 200. Sunday Practice (11 AM–12:15 PM): "
            "in-person and livestream. Tuesday Evening (7 PM): online/livestream. "
            "Also offers day-long retreats and residential retreats throughout "
            "the year. Active Meetup group. Dana-based; open to all."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds — none accessible for Boise centers
# ---------------------------------------------------------------------------

ICAL_FEEDS: dict = {}
