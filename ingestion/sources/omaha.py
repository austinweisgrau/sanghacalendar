"""
Omaha / Lincoln, NE — Phase 3 expansion.

Nebraska has a small but genuine Buddhist scene anchored by Nebraska Zen Center
(founded 1975, one of the oldest Soto Zen communities in the Midwest) and
Flatwater Collective (non-sectarian, community-focused). Honey Locust Sangha
practices in the Thich Nhat Hanh / Order of Interbeing tradition. Lincoln Zen
Center serves the state capital.

No live iCal feeds are accessible: Nebraska Zen Center's WordPress calendar is
JS-rendered (no Tribe Events iCal endpoint), Flatwater Collective's Squarespace
site does not expose a master iCal feed, Honey Locust Sangha has no machine-
readable calendar, and Lincoln Zen Center uses Wix (no iCal). All sits are
seeded as recurring instances via scripts/sangha-seed-recurring.js.

Centers included:
  - Nebraska Zen Center / Heartland Temple (nebraska_zen_center) — Soto Zen
    3625 Lafayette Avenue, Omaha NE 68131. nebraskazencenter.org
    Sun 10am (Open Zen), Wed 7pm (evening zazen), Mon–Fri 6am (morning zazen).

  - Flatwater Collective (flatwater_collective) — Pluralist / non-sectarian Buddhist
    1219 Leavenworth Street, Omaha NE 68102. flatwatercollective.org
    Thu 7pm (Dharma Talk & Meditation), Sun 4pm (Sunday Practice).

  - Honey Locust Sangha (honey_locust_sangha) — Plum Village (Thich Nhat Hanh)
    Meets at The Yoga Path, 7641 Pacific Street, Omaha NE 68114.
    honeylocustsangha.org
    Mon 6:30pm, Fri 6pm. No machine-readable calendar; recurring seeded.

  - Lincoln Zen Center (lincoln_zen_center) — Soto Zen
    3701 O Street #204, Lincoln NE 68510. lincolnzencenter.org
    Sun 10:30am, Mon 5:30pm, Wed 10:30am.

Research notes (2026-05-21):
  - Nebraska Zen Center: Founded 1975 in Omaha's Bemis Park neighborhood by
    students in Dainin Katagiri Roshi's lineage; in current location (3625
    Lafayette Ave) since 1992. Soto Zen community with strong practice culture.
    Sunday Open Zen (10am–noon): zazen, kinhin, dharma talk + tea; newcomer
    arrival at 9:15am. Also offers Wednesday evening practice (two 30-min
    zazen periods + kinhin + Fukanzazengi + discussion, 7pm) and Mon–Fri
    morning zazen (6–7:30am, in-person + Zoom). WordPress site with WooCommerce
    + GiveWP; events calendar uses custom JS rendering — no iCal endpoint
    accessible (tried /?ical=1, /events/?ical=1, /events/feed/ical).
  - Flatwater Collective: Non-sectarian Buddhist community at 1219 Leavenworth
    Street (downtown Omaha). Multiple teachers. Thursday "Meditation Practice
    and Reflection" (7–8pm): dharma talk + sitting meditation, freely offered,
    beginner-friendly. Sunday Practice (4–5pm): guided + silent meditation with
    rotating teachers. Also hosts daylong retreats and intro courses. Squarespace
    site; tested ?format=ical on calendar root — returns HTML, not iCal data.
    Individual event ICS links exist on each event page but no unified feed URL.
  - Honey Locust Sangha: Omaha Plum Village sangha in the Order of Interbeing
    (Thich Nhat Hanh lineage). Meets at The Yoga Path, 7641 Pacific Street.
    Monday evening (6:30–8:30pm): sitting + walking meditation + dharma
    discussion. Friday evening (6–7pm): sitting + walking meditation, noble
    silence. First Saturday monthly: book study. Zoom also available
    (go.unl.edu/hlsmeditation). Static HTML site; no calendar system.
  - Lincoln Zen Center: Soto Zen at 3701 O Street #204 in Lincoln (state
    capital, 55 mi SW of Omaha). Sunday 10:30am–12pm (sitting + dharma
    talk/discussion), Monday 5:30–6:45pm (sitting, beginners welcome),
    Wednesday 10:30–11:45am. Wix site with dynamically loaded calendar — no
    iCal accessible. Solid community with predictable 3x/week schedule.
  - Mindfulness Outreach Initiative (MOI): Physical location closed Jan 2025.
    Now retreat-only (3 residential weekends/year). No regular drop-in sits.
    Skipped.
  - Midwest Dharma Wheel (Lincoln): Enrollment-based, waitlisted. Not open
    drop-in. Skipped.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "nebraska_zen_center": Center(
        id="nebraska_zen_center",
        name="Nebraska Zen Center / Heartland Temple",
        url="https://nebraskazencenter.org",
        address="3625 Lafayette Avenue",
        city="Omaha",
        state="NE",
        zip_code="68131",
        lat=41.2613,
        lng=-96.0013,
        neighborhood="Bemis Park / Midtown Omaha",
        tradition=Tradition.ZEN,
        notes=(
            "Nebraska Zen Center (NZC), also known as Heartland Temple, is a Soto "
            "Zen community in the lineage of Dainin Katagiri Roshi, founded in Omaha "
            "in 1975 and one of the oldest Zen centers in the Midwest. Located at "
            "3625 Lafayette Avenue in Omaha's Bemis Park neighborhood (since 1992). "
            "Sunday Open Zen (10 AM–noon): sitting + dharma talk + tea; newcomers "
            "arrive at 9:15 AM for orientation. Wednesday Evening (7 PM): two "
            "30-minute zazen periods with kinhin and Fukanzazengi recitation. "
            "Mon–Fri Morning Zazen (6–7:30 AM): open to the public, in-person and "
            "Zoom. All programs are by donation; drop-in welcome."
        ),
    ),
    "flatwater_collective": Center(
        id="flatwater_collective",
        name="Flatwater Collective",
        url="https://www.flatwatercollective.org",
        address="1219 Leavenworth Street",
        city="Omaha",
        state="NE",
        zip_code="68102",
        lat=41.2571,
        lng=-95.9350,
        neighborhood="Downtown Omaha",
        tradition=Tradition.PLURALIST,
        notes=(
            "Flatwater Collective is a community-focused, non-sectarian Buddhist "
            "meditation center in downtown Omaha, offering freely given teachings "
            "and a welcoming environment for practitioners of all backgrounds and "
            "experience levels. Thursday Evening (7–8 PM): 'Meditation Practice "
            "and Reflection' — dharma talk + sitting meditation, beginner-friendly, "
            "freely offered. Sunday Practice (4–5 PM): guided and silent meditation "
            "with a different teacher each week. Also hosts daylong retreats, "
            "intro courses, and study groups. Located at 1219 Leavenworth Street; "
            "dana/donation appreciated."
        ),
    ),
    "honey_locust_sangha": Center(
        id="honey_locust_sangha",
        name="Honey Locust Sangha",
        url="https://honeylocustsangha.org",
        address="7641 Pacific Street",
        city="Omaha",
        state="NE",
        zip_code="68114",
        lat=41.2376,
        lng=-96.0484,
        neighborhood="Midtown / Pacific Street",
        tradition=Tradition.PLURALIST,
        notes=(
            "Honey Locust Sangha is Omaha's Plum Village sangha, practicing in the "
            "tradition of Thich Nhat Hanh and the Order of Interbeing. Meets at "
            "The Yoga Path, 7641 Pacific Street. Monday Evening (6:30–8:30 PM): "
            "sitting meditation, walking meditation, and dharma discussion. Friday "
            "Evening (6–7 PM): sitting and walking meditation in noble silence. "
            "First Saturday monthly: Thich Nhat Hanh book study. Zoom available "
            "(go.unl.edu/hlsmeditation). All programs are free and open to all; "
            "no experience required."
        ),
    ),
    "lincoln_zen_center": Center(
        id="lincoln_zen_center",
        name="Lincoln Zen Center",
        url="https://www.lincolnzencenter.org",
        address="3701 O Street, Suite 204",
        city="Lincoln",
        state="NE",
        zip_code="68510",
        lat=40.8057,
        lng=-96.6720,
        neighborhood="Near South Lincoln",
        tradition=Tradition.ZEN,
        notes=(
            "Lincoln Zen Center is a Soto Zen community in Lincoln, Nebraska (the "
            "state capital, 55 miles southwest of Omaha). Located at 3701 O Street, "
            "Suite 204. Three weekly public sitting programs: Sunday Morning "
            "(10:30 AM–noon — meditation + service/talk/discussion), Monday Evening "
            "(5:30–6:45 PM — sitting meditation, beginners welcome), and Wednesday "
            "Morning (10:30–11:45 AM). All are open to the public; no experience "
            "required; drop-in welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds — none accessible for Omaha/Lincoln centers
# ---------------------------------------------------------------------------

ICAL_FEEDS: dict = {}
