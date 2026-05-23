"""
Burlington, VT — Phase 3 expansion.

Burlington is Vermont's largest city (~45k, ~230k metro), home to the University
of Vermont and Champlain College. Its progressive culture supports a small but
active Buddhist community spanning Tibetan Shambhala, Soto Zen, Vipassana, and
Vajrayana lineages.

Centers included:
  - Burlington Shambhala Meditation Center (burlington_shambhala) — Tibetan (Shambhala)
    187 S Winooski Ave, Burlington VT 05401. burlington.shambhala.org
    Sun 9–12pm (Open Meditation), Wed 5:30–7pm (MidWeek Dharma). Live iCal feed.

  - Vermont Zen Center (vermont_zen_center) — Zen (Soto/Rinzai, Kapleau lineage)
    480 Thomas Road, Shelburne VT 05482. vermontzen.org
    Live Tockify iCal feed. Founded 1988; now led by Sensei Bodhi Murillo.
    Members + trial members for in-person; weekday AM Zoom open to workshop attendees.

  - Burlington Buddhist Sangha (burlington_buddhist_sangha) — Theravada (Insight)
    187 S Winooski Ave, Burlington VT 05401 (at Burlington Shambhala Center).
    burlingtonbuddhist.org
    1st/2nd/3rd Sundays 9:30–11:30am in-person; 4th Sunday Zoom-only. No iCal; seeded.

  - Burlington Dharma Collective (burlington_dharma_collective) — Tibetan (Vajrayana)
    241 N Winooski Ave, Burlington VT 05401 (Outright VT). burlingtondharmacollective.com
    Fri 8–8:45am weekly; 2nd Monday 7–8:30pm. No iCal; seeded.

Research notes (2026-05-23):
  - Burlington Shambhala iCal (center=215): shambhala-koeln.de feed verified working
    (58 events: MidWeek Dharma recurring ~42x, courses/special programs).
  - Vermont Zen Center Tockify: tockify.com/api/feeds/ics/vermont.zen.center confirmed
    active. Center is in Shelburne (~8 miles south of Burlington); included as closest
    Zen center to Burlington metro.
  - Burlington Buddhist Sangha: peer-led Vipassana group, meets at Shambhala Center.
    4th-Sunday Zoom-only sits not seeded (online-only).
  - Burlington Dharma Collective: founded ~2023, led by Zac Ispa-Landa (student of
    Lama Rod Owens, Bhumisparsha lineage). Meets at Outright VT (LGBTQ+ org).
  - Kadampa Burlington (173 N Prospect St): monthly Mon evenings only — too infrequent
    for seeding; branch of Kadampa NYC, $10/class. Skipped.
  - Karmê Chöling (Barnet VT, ~2 hrs): major Shambhala land center, too far.
  - Vermont Insight Meditation Center (Brattleboro, ~90 min): too far.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "burlington_shambhala": Center(
        id="burlington_shambhala",
        name="Burlington Shambhala Meditation Center",
        url="https://burlington.shambhala.org",
        address="187 S Winooski Ave",
        city="Burlington",
        state="VT",
        zip_code="05401",
        lat=44.4710,
        lng=-73.2135,
        neighborhood="Downtown Burlington",
        tradition=Tradition.TIBETAN,
        notes=(
            "Burlington Shambhala Meditation Center, founded 1972, offers two weekly "
            "drop-in programs. Sunday Open Meditation (9am–12pm): sitting practice with "
            "instruction available 10am–12pm; no registration required. Mid-Week Dharma "
            "(Wednesday 5:30–7pm): weekly drop-in with meditation, instruction, and "
            "dharma discussion. Located in the Hood Plant building at 187 S Winooski Ave "
            "(corner of King St). Part of the international Shambhala community."
        ),
    ),
    "vermont_zen_center": Center(
        id="vermont_zen_center",
        name="Vermont Zen Center",
        url="https://vermontzen.org",
        address="480 Thomas Road",
        city="Shelburne",
        state="VT",
        zip_code="05482",
        lat=44.3910,
        lng=-73.2210,
        neighborhood="Shelburne (Burlington metro)",
        tradition=Tradition.ZEN,
        notes=(
            "Vermont Zen Center (founded 1988) is a Kapleau-lineage Soto/Rinzai Zen "
            "community in Shelburne, 8 miles south of Burlington, now led by Sensei "
            "Bodhi Murillo. Weekday morning Zoom zazen (Mon–Fri 6–7am) is open to "
            "adults who have attended an introductory workshop. In-person evening and "
            "Sunday sits are for members and trial members. First Monday monthly: "
            "'Finding Your Seat' for new and trial members. Sesshin and retreats "
            "offered regularly."
        ),
    ),
    "burlington_buddhist_sangha": Center(
        id="burlington_buddhist_sangha",
        name="Burlington Buddhist Sangha",
        url="https://burlingtonbuddhist.org",
        address="187 S Winooski Ave",
        city="Burlington",
        state="VT",
        zip_code="05401",
        lat=44.4710,
        lng=-73.2135,
        neighborhood="Downtown Burlington",
        tradition=Tradition.THERAVADA,
        notes=(
            "Burlington Buddhist Sangha (formerly Burlington Area Buddhist Fellowship) "
            "is a peer-led Insight Meditation community practicing in the Theravada "
            "tradition. 1st, 2nd, and 3rd Sundays of each month, 9:30–11:30am: sitting "
            "meditation, dharma talk, and discussion at the Burlington Shambhala Center "
            "(187 S Winooski Ave). 4th Sundays are online-only (Zoom). Experienced "
            "practitioners drop-in welcome; beginners encouraged to attend a monthly "
            "intro class first. Dana-based; free."
        ),
    ),
    "burlington_dharma_collective": Center(
        id="burlington_dharma_collective",
        name="Burlington Dharma Collective",
        url="https://www.burlingtondharmacollective.com",
        address="241 N Winooski Ave",
        city="Burlington",
        state="VT",
        zip_code="05401",
        lat=44.4777,
        lng=-73.2126,
        neighborhood="Old North End Burlington",
        tradition=Tradition.TIBETAN,
        notes=(
            "Burlington Dharma Collective is a liberatory Vajrayana community founded "
            "~2023, led by Zac Ispa-Landa (student of Lama Rod Owens, Bhumisparsha "
            "lineage). Meets at Outright VT (241 N Winooski Ave, side door). Weekly "
            "Meditation: Friday 8–8:45am, fully open drop-in. Monday Night Dharma: "
            "2nd Monday monthly, 7–8:30pm. Donations welcome."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "burlington_shambhala": {
        "url": "https://shambhala-koeln.de/ical.php?center=215",
        "filter_to_sits": True,
    },
    "vermont_zen_center": {
        "url": "https://tockify.com/api/feeds/ics/vermont.zen.center",
        "filter_to_sits": True,
    },
}
