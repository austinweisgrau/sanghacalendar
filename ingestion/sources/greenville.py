"""
Greenville, South Carolina — Phase 3 expansion (heartbeat 90).

Greenville (pop. ~450k metro, Upstate SC) is one of the fastest-growing cities
in the Southeast, with a revitalized downtown and a small but active Buddhist
meditation community spanning Soto Zen, Theravada, and Kadampa traditions.

Centers included:
  - Greenville Zen Center (greenville_zen)
    Soto Zen (zazen, lay group)
    Cancer Survivors Park Center for Hope & Healing, 52 Cleveland St, Greenville SC 29601
    greenvillezen.org · 1st & 3rd Sundays 8:15–9:30am
    → Live iCal feed: greenvillezen.org/greenville-zen-sittings.ics

  - Carolina Buddhist Vihara (carolina_buddhist_vihara)
    Theravada (Sri Lankan lineage, Bhikkhuni-led)
    113 Woodridge Circle, Greenville SC 29607
    carolinabuddhist.org · Saturdays 9:00–11:30am (meditation + sutta study)
    → No iCal; seeded as recurring in sangha-seed-recurring.js

  - KMC SC — Greenville Branch (kmc_sc_greenville)
    Kadampa (New Kadampa Tradition)
    Greenville UU Fellowship, 1135 State Park Rd, Greenville SC 29609
    meditationinsouthcarolina.org/greenville/ · Mondays 6:30–7:45pm
    → No iCal; seeded as recurring in sangha-seed-recurring.js (resumes fall 2026)

Research notes (2026-07-22):
  - Greenville Zen Center: Registered 501(c)(3) lay Soto Zen group. Meets at Cancer
    Survivors Park Center for Hope & Healing, 52 Cleveland Street (parking at 44 Cleveland
    St). Two periods of zazen separated by kinhin, brief dharma reading. Newcomers arrive
    7:50am for orientation; bell rings at 8:15am strict start. Free, true drop-in. Also
    has a Luma calendar (luma.com/greenvillezen). Live iCal feed confirmed working.
    Upcoming 2026 dates: July 5/19, Aug 2/16, Sep 6/20, Oct 4/18... (1st+3rd Sundays).
  - Carolina Buddhist Vihara: Theravada center at 113 Woodridge Circle, Greenville SC 29607.
    Bhikkhuni-led (Sri Lankan lineage). Saturday mornings: guided meditation 9–10am,
    sutta study 10:15–11:30am. Offered in-person and via Zoom. Email registration
    requested (greenvillebv@gmail.com for Zoom link or to notify attendance).
    Free (dana-based). Contact: (864) 329-9961.
  - KMC SC Greenville Branch: Kadampa (NKT) class at Greenville UU Fellowship,
    1135 State Park Rd, Greenville SC 29609. Monday evenings 6:30–7:45pm. Guided
    breathing meditation, teaching, and second meditation. Drop-in ($15), series ($75),
    free for members. On summer break as of July 2026; classes resume fall 2026.
    Taught by Gen Kelsang Tabkay. Meetup: meetup.com/Greenville-Meditation-and-Buddhism-Group/
    (1,430+ members). meditationinsouthcarolina.org/greenville/.
  - No Shambhala or standalone Vipassana/Insight center confirmed in Greenville.
  - Bao An Buddhist Center (Vietnamese Mahayana): address unconfirmed, schedule
    Vietnamese-language, no public meditation confirmed — deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "greenville_zen": Center(
        id="greenville_zen",
        name="Greenville Zen Center",
        url="https://greenvillezen.org",
        address="52 Cleveland Street",
        city="Greenville",
        state="SC",
        zip_code="29601",
        lat=34.8490,
        lng=-82.4012,
        neighborhood="Downtown Greenville",
        tradition=Tradition.ZEN,
        notes=(
            "Greenville Zen Center is a registered 501(c)(3) lay Soto Zen group "
            "in Greenville, South Carolina, meeting at the Cancer Survivors Park "
            "Center for Hope & Healing, 52 Cleveland Street, Greenville SC 29601 "
            "(free parking at 44 Cleveland Street). Sits are held on the 1st and "
            "3rd Sundays of each month, 8:15–9:30am: two rounds of zazen (sitting "
            "meditation) separated by kinhin (walking meditation), followed by a "
            "brief dharma reading and conversation. Newcomers should arrive by "
            "7:50am for a brief orientation; the bell rings at 8:15 as a strict "
            "start. Free and open to all adults; true drop-in. "
            "greenvillezen.org."
        ),
    ),
    "carolina_buddhist_vihara": Center(
        id="carolina_buddhist_vihara",
        name="Carolina Buddhist Vihara",
        url="https://carolinabuddhist.org",
        address="113 Woodridge Circle",
        city="Greenville",
        state="SC",
        zip_code="29607",
        lat=34.8342,
        lng=-82.3571,
        neighborhood="Southeast Greenville",
        tradition=Tradition.THERAVADA,
        notes=(
            "Carolina Buddhist Vihara is a Theravada Buddhist center at "
            "113 Woodridge Circle, Greenville SC 29607, led by Bhikkhunis in the "
            "Sri Lankan lineage. Saturday morning program: guided meditation "
            "9:00–10:00am, short break, then Sutta Study 10:15–11:30am. Offered "
            "in-person and via Zoom. Email registration is requested "
            "(greenvillebv@gmail.com) to receive the Zoom link or to notify the "
            "teacher of in-person attendance. Free (dana-based). "
            "Contact: (864) 329-9961. carolinabuddhist.org."
        ),
    ),
    "kmc_sc_greenville": Center(
        id="kmc_sc_greenville",
        name="KMC South Carolina — Greenville Branch",
        url="https://meditationinsouthcarolina.org/greenville/",
        address="1135 State Park Road",
        city="Greenville",
        state="SC",
        zip_code="29609",
        lat=34.8738,
        lng=-82.4094,
        neighborhood="North Greenville",
        tradition=Tradition.TIBETAN,
        notes=(
            "KMC South Carolina Greenville Branch is a Kadampa Buddhist (New "
            "Kadampa Tradition) meditation class hosted at the Greenville "
            "Unitarian Universalist Fellowship, 1135 State Park Road, "
            "Greenville SC 29609. Monday evenings 6:30–7:45pm (resumes fall 2026 "
            "after summer break). Each self-contained class includes guided "
            "breathing meditation, a dharma teaching, and a second meditation — "
            "suitable for complete beginners. Taught by Gen Kelsang Tabkay. "
            "Drop-in $15; series $75; free for members. "
            "meditationinsouthcarolina.org/greenville/."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "greenville_zen": {
        "url": "https://greenvillezen.org/greenville-zen-sittings.ics",
        "filter_to_sits": True,
    },
}
