"""
Salt Lake City, UT — Phase 3 expansion.

Salt Lake City sits in the Rocky Mountain Intermountain region, surrounded by
the Wasatch Range. Its Buddhist community is small but well-established —
a contemplative counterpoint to the dominant LDS culture.

Centers included:
  - Two Arrows Zen — Soto Zen (White Plum Asanga lineage), recurring sits
    21 G Street, Salt Lake City UT 84103 (The Avenues)
  - Urgyen Samten Ling Gonpa — Tibetan Nyingma, recurring sits
    740 South 300 West, Salt Lake City UT 84101 (Downtown)

Research notes (2026-05-16):
  - Two Arrows Zen (twoarrowszen.org): White Plum Asanga lineage (Maezumi Roshi
    lineage). Uses EventON AJAX calendar — no static iCal accessible. Confirmed
    schedule:
      Mon–Fri 7:00–8:15am: Morning Zazen (in-person)
      Thu 5:30–8:00pm: Evening Zen Service (zazen + dharma talk, in-person)
    Address: 21 G Street, Salt Lake City UT 84103 (Avenues neighborhood).
    Founded by Genro Gauntt Roshi; drop-in welcome.

  - Urgyen Samten Ling Gonpa (urgyensamtenling.org): Nyingma Tibetan tradition,
    Khenpo Ugyen Tenzin Rinpoche (founder), located 2 blocks from downtown SLC.
    No iCal feed (Wix-based site). Confirmed online schedule:
      Sun 10:00am MST: Chenrezig Practice (Zoom — public/open)
    In-person teachings and practices also offered; Zoom classes open to all.
    Address: 740 South 300 West, Salt Lake City UT 84101.

  Skipped for now:
  - Katog Janaling (katogjanaling.org): Nyingma Tibetan. Schedule unclear; site
    primarily Meetup-based. 3540 S 2208 E Keller Lane. Monitor for regular
    public sits.
  - Salt Lake Buddhist Temple (slbuddhist.org): Jodo Shinshu / Pure Land.
    Squarespace site, no iCal. Sunday 9am meditation is appropriate but temple
    is primarily devotional. Deferred.
  - Salt Lake Buddhist Fellowship (saltlakebuddhist.org): Jodo Shinshu.
    WordPress.com hosted, no accessible iCal. Deferred.
  - Shambhala SLC: saltlake.shambhala.org redirects to shambhalanetwork.org —
    appears to have reorganized. Monitor for schedule access.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "two_arrows_zen": Center(
        id="two_arrows_zen",
        name="Two Arrows Zen",
        url="https://twoarrowszen.org",
        address="21 G Street",
        city="Salt Lake City",
        state="UT",
        zip_code="84103",
        lat=40.7729,
        lng=-111.8844,
        neighborhood="The Avenues",
        tradition=Tradition.ZEN,
        notes=(
            "Two Arrows Zen is a Soto Zen community in Salt Lake City's historic Avenues "
            "neighborhood, practicing in the White Plum Asanga lineage (Maezumi Roshi). "
            "Founded by Genro Gauntt Roshi. The zendo offers a full week of practice: "
            "Monday through Friday morning zazen at 7:00am (with kinhin and a second "
            "period at 7:40am); Thursday evening Zen service at 5:30pm (zazen, walking "
            "meditation, dharma talk, dokusan). Weekend intensives and seasonal sesshins "
            "offered throughout the year. Drop-in welcome; please arrive before the bell. "
            "A second location (Torrey Zendo) serves rural practice. Free."
        ),
    ),
    "urgyen_samten_ling": Center(
        id="urgyen_samten_ling",
        name="Urgyen Samten Ling Gonpa",
        url="https://www.urgyensamtenling.org",
        address="740 South 300 West",
        city="Salt Lake City",
        state="UT",
        zip_code="84101",
        lat=40.7520,
        lng=-111.9006,
        neighborhood="Downtown Salt Lake City",
        tradition=Tradition.TIBETAN,
        notes=(
            "Urgyen Samten Ling Gonpa (Tib: Place of Abiding in the Nature of Mind) is a "
            "Nyingma Tibetan Buddhist center two blocks from downtown Salt Lake City, founded "
            "by Khenpo Ugyen Tenzin Rinpoche. The gonpa offers weekly online teachings and "
            "practices open to the public, including Sunday Chenrezig practice (10am MST, "
            "Zoom), Friday Green Tara practice (10am MST, Zoom), and Saturday Ngondro "
            "(10am MST, Zoom). In-person teachings and individual instruction also available. "
            "The center draws from the Ati Yoga / Dzogchen tradition. All levels welcome; "
            "no prior experience required."
        ),
    ),
}

# No live iCal feeds — all centers seeded as recurring sits via
# scripts/sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
