"""
Chattanooga, TN — Phase 3 expansion (heartbeat 67).

Chattanooga (pop. ~185k; metro ~580k), Tennessee's fourth-largest city, sits at
the foot of Lookout Mountain on the Tennessee River. Its Buddhist community spans
Insight/Vipassana, Soto Zen, and Tibetan Gelug traditions.

Centers included:
  - Chattanooga Insight Group (chattanooga_insight_group)
    Insight/Vipassana tradition; continues the CIMC community (closed Dec 2025)
    Center for Mindful Living, 400 E Main St Ste 150, Chattanooga TN 37408
    chattanoogainsight.com · Weekly Thursday 6:30–7:45pm (in-person)

  - Zen Group of Chattanooga (zen_group_chattanooga)
    Soto Zen — Silent Thunder Order / Soyu Matsuoka Roshi lineage
    335 Crestway Drive, Chattanooga TN 37411
    storder.org/portfolio/chattanooga-zen-group/ · Sunday 7:30–9:00am
    Format: 3×20–25 min zazen + 2×5 min kinhin; newcomers welcome

  - Paramita Center Southeast (paramita_center_southeast)
    Tibetan Gelug (Paramita Centre lineage, Québec/India); led by Lama Samten
    St Andrews Center, 1918 Union Ave, Chattanooga TN 37405
    buddhismsoutheast.org · Tuesday "Happy Hour" meditation 5:30–6:30pm
    All traditions welcome; brief intro teaching + group practice + discussion

Research notes (2026-05-26):
  - Chattanooga Insight Meditation Community (CIMC) closed Dec 2025. The
    Chattanooga Insight Group continues independently through breathingbody.net
    (Center for Mindful Living, janka@breathingbody.net). iCal feed at
    breathingbody.net/?method=ical&id=941 is malformed (DTEND spans full year;
    TZID=UTC but times are local Eastern). Seeded as recurring Thursday sit instead.
  - Zen Group of Chattanooga: confirmed weekly Sunday 7:30–9:00am at 335 Crestway
    Dr, Chattanooga TN 37411. Silent Thunder Order (Soyu Matsuoka Roshi lineage,
    one of first Soto Zen teachers in North America). Free, donations welcome.
    Contact: tlrieth@comcast.net.
  - Paramita Center Southeast: Tibetan Gelug center at St Andrews Center (1918
    Union Ave, Chattanooga TN 37405). Spiritual director Lama Samten; senior
    teacher Tenzin Gawa (Jason Simard). Regular "Happy Hour" meditation Tuesdays
    5:30–6:30pm. Offers full lamrim courses and retreats. All traditions welcome.
    5 Crescent Park, Ridgeside TN is their office; St Andrews Center is program
    venue for regular classes.
  - Tara Mandala Chattanooga Sangha (ChattaBuddha): meets virtually on Wednesday
    6–7:15pm — Zoom-only, no physical address. Skipped (online-only).
  - Mindfulness Sangha of Chattanooga (4418 Seneca Ave, Plum Village): appears
    dormant or Zoom-only — no confirmed active in-person schedule. Deferred.
  - Bodhi Center (4220 Dayton Blvd Ste E, Tibetan Gelug): website "coming soon" as
    of May 2026. Deferred pending relaunch.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "chattanooga_insight_group": Center(
        id="chattanooga_insight_group",
        name="Chattanooga Insight Group",
        url="https://chattanoogainsight.com",
        address="400 E Main St Ste 150",
        city="Chattanooga",
        state="TN",
        zip_code="37408",
        lat=35.0484,
        lng=-85.3087,
        neighborhood="Downtown Chattanooga",
        tradition=Tradition.THERAVADA,
        notes=(
            "Chattanooga Insight Group continues the practice community that grew "
            "from the Chattanooga Insight Meditation Community (CIMC, closed Dec 2025). "
            "The group is dedicated to the teaching and practice of meditation and "
            "mindfulness in the Insight/Vipassana tradition, exploring themes of "
            "mindfulness, insight, daily life practice, and the transformative power "
            "of presence. Weekly Thursday evenings, 6:30–7:45pm, at the Center for "
            "Mindful Living (400 E Main St Ste 150, downtown Chattanooga). Sessions "
            "begin with 30 minutes of silent meditation, followed by a talk or "
            "dharma sharing and Q&A. In-person. Free. "
            "Info: chattanoogainsight.com or breathingbody.net."
        ),
    ),
    "zen_group_chattanooga": Center(
        id="zen_group_chattanooga",
        name="Zen Group of Chattanooga",
        url="https://storder.org/portfolio/chattanooga-zen-group/",
        address="335 Crestway Drive",
        city="Chattanooga",
        state="TN",
        zip_code="37411",
        lat=35.0203,
        lng=-85.2395,
        neighborhood="Eastdale",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Group of Chattanooga is an affiliate of the Silent Thunder Order, "
            "which carries the Soto Zen lineage of Soyu Matsuoka Roshi — one of the "
            "first Japanese teachers to bring Soto Zen to North America. Sunday "
            "morning sitting from 7:30–9:00am at 335 Crestway Drive, Chattanooga. "
            "Format: three 20–25 minute zazen (seated meditation) periods, "
            "alternating with kinhin (walking meditation). Newcomers welcome and "
            "instruction available. No fee; donations appreciated. "
            "Contact: tlrieth@comcast.net."
        ),
    ),
    "paramita_center_southeast": Center(
        id="paramita_center_southeast",
        name="Paramita Center Southeast",
        url="https://buddhismsoutheast.org",
        address="1918 Union Ave",
        city="Chattanooga",
        state="TN",
        zip_code="37405",
        lat=35.0713,
        lng=-85.3128,
        neighborhood="North Chattanooga",
        tradition=Tradition.TIBETAN,
        notes=(
            "Paramita Center Southeast is a teaching center for meditation and "
            "Tibetan Buddhism in Chattanooga, affiliated with the Paramita Centres "
            "of Québec, Toronto, France, and India. Spiritual director is Lama "
            "Samten; senior teacher is Tibetan monk Tenzin Gawa (Jason Simard). "
            "Regular 'Happy Hour' meditation every Tuesday, 5:30–6:30pm, at "
            "St Andrews Center (1918 Union Ave, North Chattanooga). Includes a "
            "brief introductory teaching, followed by group practice and discussion. "
            "All traditions and levels welcome. The center also offers in-depth "
            "lamrim courses, multi-day urban retreats, and special teachings "
            "throughout the year. buddhismsoutheast.org."
        ),
    ),
}

# No live iCal feeds available — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
