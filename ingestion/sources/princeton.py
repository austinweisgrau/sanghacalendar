"""
Princeton / Central New Jersey — Phase 3 expansion (heartbeat 127).

Princeton (pop. ~30k; Mercer County) is a university town with a strong,
multi-tradition Buddhist community concentrated around Fellowship in Prayer
(291 Witherspoon St). New Brunswick (pop. ~56k; Middlesex County) hosts
Cold Mountain Zen at Rutgers University.

Centers included:
  - Princeton Insight Meditation (princeton_insight_meditation)
    — Vipassana / Insight Meditation, nonsectarian
    291 Witherspoon St, Princeton NJ 08540 (Fellowship in Prayer)
    princetoninsightmeditation.org
    Mon 7pm (hybrid) + Sun 3pm (hybrid) + 2nd+4th Wed 7pm (Zoom only, skip)
    No iCal (WordPress Events Calendar plugin returns 406); recurring seeded.

  - Princeton Buddhist Meditation Group (princeton_buddhist_mg)
    — Eclectic (Tibetan-influenced), unaffiliated / nonsectarian
    291 Witherspoon St, Princeton NJ 08540 (Fellowship in Prayer)
    princetonbuddhist.org
    Sun 12:30pm (hybrid) + Thu 7pm (hybrid) + 1st Sat 10am (Zoom, skip)
    Live Google Calendar iCal: wired.

  - Princeton Area Zen Group (princeton_zen_group)
    — Zen, unaffiliated / Grassroots Zen; founded 1991
    291 Witherspoon St, Princeton NJ 08540 (Fellowship in Prayer)
    princetonzengroup.org
    Sun 7pm (in-person; newcomers arrive 6:30pm for intro)
    No iCal; recurring seeded.

  - Cold Mountain Zen (cold_mountain_zen)
    — Rinzai Zen; Kankan Roshi Kurt Spellmeyer; Rutgers-based
    510 George St, Murray Hall Rm 302, New Brunswick NJ 08901
    coldmountainzen.org
    Fri 7pm (hybrid) + Mon 7pm (Zoom only, skip) + bi-weekly Sat 7am (advance)
    No iCal; recurring Fri 7pm sit seeded.

Research notes (2026-11-28):
  - Princeton Insight Meditation: Active through Nov 2026. Monday Sitting Group
    every Monday 7:00–9:00pm at Fellowship in Prayer, 291 Witherspoon St,
    Princeton NJ 08540. Drop-ins welcome, no registration. Also Sunday Dharma
    Study Group: Sundays 3:00–5:00pm (hybrid). Engaged Buddhism Group: 2nd+4th
    Wednesdays 7pm (Zoom only — not seeded). WordPress Events Calendar plugin;
    /events/?ical=1 returns 406 (server rejects without browser user-agent).
    princetoninsightmeditation.org.

  - Princeton Buddhist Meditation Group (PBMG): Founded ca. 2010s; meets at
    Fellowship in Prayer (same building as PIM and PAZG — Princeton's main
    ecumenical meditation hub). Google Calendar confirmed public + subscribable.
    Calendar ID: o3chvu5ejc6pqfbat4bbo0o8k0@group.calendar.google.com.
    Sunday meditation 12:30–2:00pm (in-person + Zoom). Thursday 7:00–8:30pm
    (in-person + Zoom). 1st Sat 10:00–11:00am (Zoom only — not seeded). 2nd
    Sunday 11:15–noon intro to shamatha/vipashyana (included in GCal). Temporarily
    moved to online-only in late Nov 2026 due to facility repairs; check
    infoplease@princetonbuddhist.org. princetonbuddhist.org.

  - Princeton Area Zen Group (PAZG): Founded 1991 by Manfred Steger and Perle
    Besserman. Unaffiliated "Grassroots Zen" community; no Roshi affiliation.
    291 Witherspoon St, Princeton NJ 08540. Sunday evenings 7:00–9:00pm; newcomers
    arrive 6:30pm for introduction to forms. Events confirmed through Oct 2026.
    princetonzengroup.org.

  - Cold Mountain Zen: Rinzai Zen; directed by Kankan Roshi Kurt Spellmeyer, a
    professor at Rutgers and author of "The Zen of You and Me." Meets in Murray
    Hall Room 302 at Rutgers, 510 George St, New Brunswick NJ 08901. Friday
    7:00–8:30pm (in-person + Zoom; tea afterward); Monday 7:00–8:30pm (Zoom only
    — not seeded); every other Saturday 7:00am–noon (irregular — not seeded).
    Events confirmed through Dec 2026. coldmountainzen.org.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "princeton_insight_meditation": Center(
        id="princeton_insight_meditation",
        name="Princeton Insight Meditation",
        url="https://princetoninsightmeditation.org",
        address="291 Witherspoon Street",
        city="Princeton",
        state="NJ",
        zip_code="08540",
        lat=40.3604,
        lng=-74.6560,
        neighborhood="Princeton (Fellowship in Prayer)",
        tradition=Tradition.VIPASSANA,
        notes=(
            "Princeton Insight Meditation (PIM) is a Vipassana / Insight Meditation "
            "community in Princeton, NJ, meeting at Fellowship in Prayer (291 "
            "Witherspoon St). The Monday Sitting Group meets every Monday 7:00–9:00pm "
            "(in-person + Zoom): 30-min guided meditation, 30-min sit, dharma "
            "discussion; drop-ins welcome, no registration required. The Sunday "
            "Dharma Study Group meets Sundays 3:00–5:00pm (in-person + Zoom): "
            "dharma readings and discussion. Affiliated with the Spirit Rock / "
            "IMS Vipassana lineage. All levels welcome; free (dana). "
            "princetoninsightmeditation.org."
        ),
    ),
    "princeton_buddhist_mg": Center(
        id="princeton_buddhist_mg",
        name="Princeton Buddhist Meditation Group",
        url="https://www.princetonbuddhist.org",
        address="291 Witherspoon Street",
        city="Princeton",
        state="NJ",
        zip_code="08540",
        lat=40.3604,
        lng=-74.6560,
        neighborhood="Princeton (Fellowship in Prayer)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Princeton Buddhist Meditation Group (PBMG) is an eclectic, unaffiliated "
            "Buddhist community in Princeton, NJ, drawing on Tibetan, Zen, and "
            "Theravada influences. Meets at Fellowship in Prayer (291 Witherspoon St). "
            "Sunday Group: Sundays 12:30–2:00pm (in-person + Zoom), meditation and "
            "contemplation. Thursday Group: Thursdays 7:00–8:30pm (in-person + Zoom), "
            "meditation + study and discussion. Second Sunday: introductory "
            "shamatha/vipashyana, 11:15am–noon. Open to all; beginners welcome. "
            "Contact: infoplease@princetonbuddhist.org. princetonbuddhist.org."
        ),
    ),
    "princeton_zen_group": Center(
        id="princeton_zen_group",
        name="Princeton Area Zen Group",
        url="http://www.princetonzengroup.org",
        address="291 Witherspoon Street",
        city="Princeton",
        state="NJ",
        zip_code="08540",
        lat=40.3604,
        lng=-74.6560,
        neighborhood="Princeton (Fellowship in Prayer)",
        tradition=Tradition.ZEN,
        notes=(
            "Princeton Area Zen Group (PAZG) is an independent Zen community in "
            "Princeton, NJ, founded in 1991 by Manfred Steger and Perle Besserman. "
            "The group practices 'Grassroots Zen' — lay Zen without formal "
            "Roshi affiliation — meeting at Fellowship in Prayer (291 Witherspoon "
            "St). Sunday evening zazen: Sundays 7:00–9:00pm (in-person); newcomers "
            "arrive 6:30pm for an introduction to forms (chanting, sitting, walking). "
            "Open to all; free. princetonzengroup.org."
        ),
    ),
    "cold_mountain_zen": Center(
        id="cold_mountain_zen",
        name="Cold Mountain Zen",
        url="https://www.coldmountainzen.org",
        address="510 George Street, Murray Hall Rm 302",
        city="New Brunswick",
        state="NJ",
        zip_code="08901",
        lat=40.4998,
        lng=-74.4463,
        neighborhood="Rutgers University campus",
        tradition=Tradition.ZEN,
        notes=(
            "Cold Mountain Zen is a Rinzai Zen community at Rutgers University in "
            "New Brunswick, NJ, directed by Kankan Roshi Kurt Spellmeyer. Traces "
            "its lineage to 9th-century Chinese Chan through the Rinzai tradition. "
            "Friday Evening Sit: Fridays 7:00–8:30pm in Murray Hall Room 302, 510 "
            "George St (in-person + Zoom; tea and conversation afterward). Monday "
            "7:00–8:30pm sit is Zoom-only. Every-other-Saturday 7:00am–noon intensive "
            "sessions held periodically. Open to all levels; beginners welcome. Free. "
            "coldmountainzen.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    # Princeton Buddhist Meditation Group — public Google Calendar
    "princeton_buddhist_mg": {
        "url": (
            "https://calendar.google.com/calendar/ical/"
            "o3chvu5ejc6pqfbat4bbo0o8k0%40group.calendar.google.com"
            "/public/basic.ics"
        ),
        "filter_to_sits": True,
    },
}

EVENTBRITE_FEEDS: dict = {}
