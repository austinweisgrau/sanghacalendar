"""
Colorado Springs, CO — Phase 3 expansion (heartbeat 68).

Colorado Springs (pop. ~480k; metro ~760k), Colorado's second-largest city, sits
at the foot of Pikes Peak on the eastern edge of the Rocky Mountains. The city's
Buddhist community spans Zen, Vipassana/Insight, and multiple Tibetan traditions.

Centers included:
  - Springs Mountain Sangha (springs_mountain_sangha)
    Zen — Pacific Zen School / Open Source Zen (Sanbo Kyodan lineage)
    Shove Chapel, Colorado College, Colorado Springs CO 80903
    smszen.org · Mon 6–8pm, Wed 6:30–7:30am, Sat 6:30–8:30am

  - Rocky Mountain Insight (rocky_mountain_insight_cs)
    Theravada / Vipassana (Insight Meditation)
    2525 W. Pikes Peak Ave. Suite A, Colorado Springs CO 80904
    rockymountaininsight.org · Sun 9–10am, Wed 6–7pm

  - BodhiMind Center (bodhimind_center_cs)
    Nonsectarian Buddhist rooted in Tibetan tradition
    2955 Professional Place Suite 101, Colorado Springs CO 80904
    bodhimindcenter.org · Tue & Thu 6–8pm

  - Kadampa Meditation Center — Colorado Springs (kadampa_cs)
    New Kadampa Tradition (Tibetan/Gelug, Geshe Kelsang Gyatso)
    Edenology Holistic Wellness, 2611 W. Colorado Ave. Studio B, Colorado Springs CO 80904
    meditationincolorado.org/colorado-springs/ · Mon 6:30–7:45pm

  - Tibetan Meditation Center Colorado (tibetan_meditation_center_cs)
    Tibetan Buddhism (teacher Geshe Wangden Tashi)
    3560 Hartsock Lane, Colorado Springs CO 80917
    tibetanmeditationcentercolorado.com · Sun 10–11am

Research notes (2026-05-26):
  - Springs Mountain Sangha: Pacific Zen School lineage through Sanbo Kyodan. Holds
    the most intensive schedule in Colorado Springs (3 sits/week). Monday dharma talks
    also available via Zoom. "No membership dues or sign-up requirements." Free.
    smszen.org uses All-in-One Event Calendar plugin; ?ical=1 returns HTML, not iCal.
    Seeded as recurring.
  - Rocky Mountain Insight: Active Vipassana community since ~2006, Old Colorado City
    neighborhood. Sunday 9am: sitting practice + dharma reading. Wednesday 6pm: Sangha
    Night (walking meditation, sitting, dharma, community). Both in-person + Zoom.
    Cloudflare blocks iCal at rockymountaininsight.org/classes/?ical=1. Seeded as
    recurring. First + third Wednesdays add 5:15pm new-student orientation.
  - BodhiMind Center: Founded with support from Khen Rinpoche Lobzang Tsetan. Non-
    sectarian but rooted in Tibetan tradition. Two 20-min sits + teaching + discussion
    per session (Tue/Thu 6–8pm). Drop-in, free, both in-person + Zoom.
    bodhimindcenter.org event calendar returns 404 on ?ical=1. Seeded as recurring.
  - Kadampa CS: Branch of KMC Colorado (Denver). Class at Edenology Holistic Wellness,
    2611 W. Colorado Ave. Studio B. Monday 6:30pm. $15/class, drop-in, no registration.
    meditationincolorado.org iCal feed is site-wide (Denver/Evergreen/Golden) and does
    not include Colorado Springs branch events. Seeded as recurring.
  - Tibetan Meditation Center: Led by Geshe Wangden Tashi, trained 20+ years in
    Sera Je Monastery (Gelug). Sunday 10–11am. Compassion teaching + silent meditation
    + mantra recitation + discussion. Free, all welcome, drop-in. Schedule confirmed
    via Meetup (tibetan-meditation-center) where updates posted.
  - Shambhala Colorado Springs: No location found; nearest are Boulder + Denver.
  - Dhamma Sela (Goenka Vipassana, Elbert CO, 40 miles east): retreat center only.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "springs_mountain_sangha": Center(
        id="springs_mountain_sangha",
        name="Springs Mountain Sangha",
        url="https://www.smszen.org",
        address="1010 N Nevada Ave",
        city="Colorado Springs",
        state="CO",
        zip_code="80903",
        lat=38.8433,
        lng=-104.8225,
        neighborhood="Colorado College",
        tradition=Tradition.ZEN,
        notes=(
            "Springs Mountain Sangha is a Zen community in the Pacific Zen School "
            "lineage (Open Source Zen), rooted in the Sanbo Kyodan tradition. Meets "
            "three times weekly at Shove Chapel on the Colorado College campus. "
            "Monday evenings 6:00–8:00pm (two sitting periods + dharma talk; also "
            "available via Zoom). Wednesday mornings 6:30–7:30am (two sitting periods "
            "with walking meditation). Saturday mornings 6:30–8:30am (four sitting "
            "periods with walking meditation). All sits are drop-in — 'We consider a "
            "member anyone who wishes to be considered a member. There are no membership "
            "dues or sign-up requirements.' Instruction available for beginners. Free. "
            "smszen.org."
        ),
    ),
    "rocky_mountain_insight_cs": Center(
        id="rocky_mountain_insight_cs",
        name="Rocky Mountain Insight",
        url="https://rockymountaininsight.org",
        address="2525 W Pikes Peak Ave Suite A",
        city="Colorado Springs",
        state="CO",
        zip_code="80904",
        lat=38.8673,
        lng=-104.8806,
        neighborhood="Old Colorado City",
        tradition=Tradition.THERAVADA,
        notes=(
            "Rocky Mountain Insight is a Vipassana/Insight Meditation community in "
            "the Theravada tradition, located in the Old Colorado City neighborhood of "
            "Colorado Springs. Sunday mornings 9:00–10:00am: sitting practice and "
            "dharma reading. Wednesday evenings 6:00–7:00pm: Sangha Night (walking "
            "meditation, sitting, dharma discussion, and community — open to all). "
            "Both sessions are drop-in and available in-person and via Zoom. "
            "First and third Wednesdays include a 5:15pm new-student orientation. "
            "Free; donations welcome. rockymountaininsight.org."
        ),
    ),
    "bodhimind_center_cs": Center(
        id="bodhimind_center_cs",
        name="BodhiMind Center",
        url="https://bodhimindcenter.org",
        address="2955 Professional Place Suite 101",
        city="Colorado Springs",
        state="CO",
        zip_code="80904",
        lat=38.8670,
        lng=-104.8731,
        neighborhood="Old Colorado City",
        tradition=Tradition.TIBETAN,
        notes=(
            "BodhiMind Center is a nonsectarian Buddhist center rooted in the Tibetan "
            "tradition, founded with the guidance of Khen Rinpoche Lobzang Tsetan. "
            "Tuesday and Thursday evenings, 6:00–8:00pm. Each session includes two "
            "20-minute sitting meditation periods, a teaching, and group discussion. "
            "Drop-in welcome; both in-person and Zoom available. No membership fees. "
            "2955 Professional Place Suite 101, Colorado Springs CO 80904. "
            "Contact: bodhimindcenter@gmail.com / 719-822-1999. bodhimindcenter.org."
        ),
    ),
    "kadampa_cs": Center(
        id="kadampa_cs",
        name="Kadampa Meditation Center — Colorado Springs",
        url="https://meditationincolorado.org/colorado-springs/",
        address="2611 W Colorado Ave Studio B",
        city="Colorado Springs",
        state="CO",
        zip_code="80904",
        lat=38.8590,
        lng=-104.8780,
        neighborhood="Old Colorado City",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Colorado Springs is a branch of KMC Colorado "
            "(Denver). Part of the New Kadampa Tradition (Gelug lineage, Geshe Kelsang "
            "Gyatso). Monday evening drop-in meditation class, 6:30–7:45pm, at "
            "Edenology Holistic Wellness (2611 W. Colorado Ave., Studio B, Colorado "
            "Springs CO 80904). $15/class; low-income accommodations available; no one "
            "turned away. No registration required. meditationincolorado.org."
        ),
    ),
    "tibetan_meditation_center_cs": Center(
        id="tibetan_meditation_center_cs",
        name="Tibetan Meditation Center Colorado",
        url="https://www.tibetanmeditationcentercolorado.com",
        address="3560 Hartsock Lane",
        city="Colorado Springs",
        state="CO",
        zip_code="80917",
        lat=38.9017,
        lng=-104.7558,
        neighborhood="Northeast Colorado Springs",
        tradition=Tradition.TIBETAN,
        notes=(
            "Tibetan Meditation Center Colorado is led by Geshe Wangden Tashi, who "
            "trained for over 20 years at Sera Je Monastery in India (Gelug lineage). "
            "Sunday mornings 10:00–11:00am: compassion teaching, silent meditation, "
            "mantra recitation, and group discussion. Drop-in; all are welcome. "
            "Free. 3560 Hartsock Lane, Colorado Springs CO 80917. "
            "tibetanmeditationcentercolorado.com."
        ),
    ),
}

# No live iCal feeds available — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
