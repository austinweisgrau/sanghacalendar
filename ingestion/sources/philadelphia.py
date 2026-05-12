"""
Philadelphia, PA meditation center sources — Phase 3 expansion.

iCal feeds:
  - Shambhala Philadelphia (center=210): Cologne server returning 522 as of 2026-05-12.
    Recurring sits seeded instead (Sun 10am, Thu 6pm).

Recurring sits (seeded in scripts/sangha-seed-recurring.js):
  - Shambhala Meditation Center of Philadelphia — Sun 10am, Thu 6pm (in-person)
    2030 Sansom St, Center City Philadelphia, PA 19103.
  - Kadampa Meditation Center Philadelphia — Mon/Wed/Thu 6:30pm, Sun 10:30am (in-person)
    47-49 N 2nd St, Old City Philadelphia, PA 19106.
    Very active daily program; Wix site (no iCal).
  - Zen Center of Philadelphia — Sun 10am, Wed 7pm (hybrid in-person + Zoom)
    4904 Cedar Ave, West Philadelphia, PA 19143.
    Ordinary Mind Zen School (Charlotte Joko Beck lineage).
    Uses Google Calendar plugin (Simple Calendar) — no extractable public iCal URL.
  - Chenrezig Tibetan Buddhist Center — Sun 10am, Thu 7pm (in-person + hybrid)
    954 N Marshall St, Northern Liberties, Philadelphia, PA 19123.
    Ecumenical Tibetan center founded 1989 by Lama Losang Samten.

Research notes (2026-05-12):
  - Shambhala Philadelphia iCal (shambhala-koeln.de center=210): server returning 522.
    Monitor for recovery; re-add to ICAL_FEEDS when back online.
  - Kadampa Philadelphia (meditationinphiladelphia.org): Wix platform, no iCal.
    Also has Meetup presence — possible Eventbrite-style scrape in future.
  - Zen Center of Philadelphia: uses WordPress + Simple Calendar plugin (Google Cal embedded).
    data-calendar-id="6098" is internal WP plugin ID, not Google Calendar ID.
    No public iCal URL extractable without authenticated API access.
  - Chenrezig TBC (tibetanbuddhist.org): Wix platform, no iCal.
    Thu 7pm is Green Tara Puja — mixed sit/puja, but good weekly in-person practice.
  - Nalandabodhi Philadelphia (phil.nalandabodhi.org): empty iCal feed, no stable address.
    Meets at Temple Univ. and Pendle Hill; deferred until stable address confirmed.
  - Delaware Valley Insight Meditation: sitting groups at home locations — deferred.
  - Heart Sangha: sporadic Sunday Sangha (not weekly) — skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "shambhala_philadelphia": Center(
        id="shambhala_philadelphia",
        name="Shambhala Meditation Center of Philadelphia",
        url="https://philadelphia.shambhala.org",
        address="2030 Sansom St",
        city="Philadelphia",
        state="PA",
        zip_code="19103",
        lat=39.9518,
        lng=-75.1748,
        neighborhood="Center City West / Rittenhouse Square",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Center of Philadelphia is a contemplative community in "
            "the Shambhala lineage of Chögyam Trungpa Rinpoche, located in Center City "
            "near Rittenhouse Square. Offers regular drop-in Sunday Sitting Meditation "
            "(10–11am, first Sunday extended 9:30am–noon) and Thursday Sitting Meditation "
            "(6–7pm). Also hosts Monday Night sangha, Shambhala Training weekends, and "
            "dharma study groups. All are welcome; no experience required."
        ),
    ),
    "kadampa_philadelphia": Center(
        id="kadampa_philadelphia",
        name="Kadampa Meditation Center Philadelphia",
        url="https://www.meditationinphiladelphia.org",
        address="47-49 N 2nd St",
        city="Philadelphia",
        state="PA",
        zip_code="19106",
        lat=39.9504,
        lng=-75.1431,
        neighborhood="Old City",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center Philadelphia (KMC Philadelphia) is a Tibetan Buddhist "
            "center in the New Kadampa Tradition (NKT-IKBU), located in Old City Philadelphia "
            "steps from the Delaware waterfront. One of the most active meditation centers in "
            "the city, with classes nearly every day of the week — Monday, Wednesday, and "
            "Thursday evenings (6:30pm), Tuesday afternoons and evenings (5pm), Friday "
            "mornings (8am), and Sunday mornings (10:30am). All sessions include guided "
            "meditation and Buddhist teachings. Drop-in fee; free for members. "
            "No experience necessary."
        ),
    ),
    "zen_center_philadelphia": Center(
        id="zen_center_philadelphia",
        name="Zen Center of Philadelphia",
        url="https://www.zencenterphiladelphia.net",
        address="4904 Cedar Ave",
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        lat=39.9476,
        lng=-75.2277,
        neighborhood="Cedar Park / West Philadelphia",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Center of Philadelphia (ZCP) is a Zen Buddhist community in the Ordinary "
            "Mind Zen School lineage of Charlotte Joko Beck and Joko's successor Jan Chozen "
            "Bays Roshi. Located in the Cedar Park neighborhood of West Philadelphia. Offers "
            "weekly public zazen: Sunday Morning Program (10am–noon, hybrid in-person + Zoom), "
            "Wednesday Evening Sitting (7–8pm, hybrid), and daily online sits via Zoom "
            "(Mon–Fri 7–8am). Monthly sesshin retreats (all-day sitting, last Sat or Sun). "
            "Drop-in welcome; sliding scale/donation-based."
        ),
    ),
    "chenrezig_philadelphia": Center(
        id="chenrezig_philadelphia",
        name="Chenrezig Tibetan Buddhist Center",
        url="https://www.tibetanbuddhist.org",
        address="954 N Marshall St",
        city="Philadelphia",
        state="PA",
        zip_code="19123",
        lat=39.9633,
        lng=-75.1504,
        neighborhood="Northern Liberties / Callowhill",
        tradition=Tradition.TIBETAN,
        notes=(
            "Chenrezig Tibetan Buddhist Center of Philadelphia is a non-sectarian Tibetan "
            "Buddhist center founded in 1989 by Lama Losang Samten, a former monk of the "
            "Dalai Lama's Namgyal Monastery. One of the oldest Tibetan Buddhist centers in "
            "Philadelphia. Offers weekly Sunday Sangha (10–11:30am, hybrid in-person + Zoom "
            "with center open at 9am for self-guided practice) and Thursday Green Tara Puja "
            "(7pm, in-person). Monthly Medicine Buddha and other ceremonial programs. "
            "Open to all traditions; drop-in welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# iCal feeds
# ---------------------------------------------------------------------------

# Shambhala Philadelphia center=210: Cologne server returning 522 as of 2026-05-12.
# Re-add entry below when server recovers:
# ICAL_FEEDS = {
#     "shambhala_philadelphia": {
#         "url": "https://shambhala-koeln.de/ical.php?center=210",
#         "center_id": "shambhala_philadelphia",
#         "filter_to_sits": True,
#     },
# }
ICAL_FEEDS = {}
