"""
Rochester, NY — Phase 3 expansion.

Rochester has one of the most historically significant Zen communities in North
America: the Rochester Zen Center, founded in 1966 by Philip Kapleau Roshi
(author of "The Three Pillars of Zen"), one of the first Western teachers
authorized by a Japanese Zen master. The city has a compact but serious
practice community.

Centers included:
  - Rochester Zen Center (rzc) — Zen (Kapleau lineage)
    7 Arnold Park, Rochester NY 14607
    rzc.org — founded 1966 by Philip Kapleau Roshi
    Recurring: Tue–Fri 6am morning, Mon/Thu 7pm evening, Sat 6:30am, Sun 8:30am
    No iCal (Cloudflare blocks scraping); recurring sits seeded.

  - Endless Path Zendo (endless_path_zendo) — Zen (Diamond Sangha / Kapleau lineage)
    56 Brighton St, Rochester NY 14607
    endlesspathzendo.org — Roshi Rafe Martin lineage
    Recurring: Mon 7pm, Tue 7pm, Wed 6:30am + 7pm, Sat 9am
    No iCal; static HTML site. Recurring sits seeded.

  - Dharma Refuge (dharma_refuge_rochester) — Tibetan-influenced (Anam Thubten)
    1124 Culver Rd (at Covenant United Methodist), Rochester NY 14609
    dharmarefuge.com — hybrid in-person + Zoom
    Recurring: Wed 7pm, Sat 10am
    No iCal (Weebly site); recurring sits seeded.

Research notes (2026-05-18):
  - Rochester Zen Center iCal: rzc.org uses WordPress but Cloudflare bot
    protection blocks all automated requests. Recurring sits seeded instead.
  - White Lotus Buddhist Center (815 Park Ave, Drikung Kagyu): has a WordPress
    iCal endpoint but it currently returns 0 VEVENTs. Deferred — monitor for
    future content.
  - Rochester Chan Buddhist Temple (1040 Winton Rd N): website inaccessible;
    activity level in 2026 unclear. Deferred.
  - Blooming Lilac Sangha (Brighton): Plum Village / TNH lineage, meets in a
    private home — contact required before attending. Skip for now (no public
    drop-in without advance contact).
  - Shambhala Rochester: no active center found (nearest: Albany).
  - Kadampa/KMC: no Rochester center found.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "rzc": Center(
        id="rzc",
        name="Rochester Zen Center",
        url="https://www.rzc.org",
        address="7 Arnold Park",
        city="Rochester",
        state="NY",
        zip_code="14607",
        lat=43.1596,
        lng=-77.5825,
        neighborhood="Park Avenue",
        tradition=Tradition.ZEN,
        notes=(
            "The Rochester Zen Center is one of the most historically significant Zen "
            "communities in North America. Founded in 1966 by Philip Kapleau Roshi — "
            "author of The Three Pillars of Zen and one of the first Western teachers "
            "authorized in the Rinzai/Soto tradition — RZC has trained generations of "
            "Western Zen practitioners and teachers. Sitting practice is rigorous and "
            "formal (zazen, kinhin, chanting, dokusan with the teacher). Morning sits "
            "run Tuesday through Friday at 6 AM; evening sits on Monday and Thursday at "
            "7 PM; Saturday morning at 6:30 AM; Sunday morning program at 8:30 AM with "
            "zazen and a Dharma talk. Drop-in students are welcome at most sits — "
            "contact the center for newcomer orientation. RZC also stewards Chapin Mill "
            "Retreat Center, a 135-acre rural property near Batavia."
        ),
    ),
    "endless_path_zendo": Center(
        id="endless_path_zendo",
        name="Endless Path Zendo",
        url="https://www.endlesspathzendo.org",
        address="56 Brighton Street",
        city="Rochester",
        state="NY",
        zip_code="14607",
        lat=43.1540,
        lng=-77.5870,
        neighborhood="Swillburg",
        tradition=Tradition.ZEN,
        notes=(
            "Endless Path Zendo is a small Zen community in Rochester, led by Roshi Rafe "
            "Martin — a Dharma heir trained under both Philip Kapleau Roshi and Robert "
            "Aitken Roshi (Diamond Sangha). Formal zazen practice with dokusan (individual "
            "teacher interviews) offered on Tuesday and Wednesday mornings. The zendo sits "
            "Tuesday evenings (three 25-min rounds, kinhin, chanting service), Monday "
            "evenings (informal, one hour), Wednesday mornings and evenings, and Saturday "
            "mornings. First-time visitors arrive at 6:15 PM on Tuesdays for a brief "
            "orientation. Monthly sesshin and Dharma talks. Hybrid in-person and Zoom."
        ),
    ),
    "dharma_refuge_rochester": Center(
        id="dharma_refuge_rochester",
        name="Dharma Refuge",
        url="https://www.dharmarefuge.com",
        address="1124 Culver Road",
        city="Rochester",
        state="NY",
        zip_code="14609",
        lat=43.1647,
        lng=-77.5604,
        neighborhood="Culver-University",
        tradition=Tradition.TIBETAN,
        notes=(
            "Dharma Refuge is a meditation community in Rochester inspired by the teachings "
            "of Anam Thubten Rinpoche and Pema Chodron's Lojong practice. It evolved from "
            "the former Dharmata Meditation Sangha. Meetings are hybrid (in-person at "
            "Covenant United Methodist Church + Zoom) and rotate between guided sitting, "
            "video teachings, and book discussion. Wednesday evenings 7–8:15 PM; Saturday "
            "mornings 10–11:30 AM. Donation-based, drop-in welcome."
        ),
    ),
}

# No live iCal feeds — all Rochester centers use recurring sit seeding
ICAL_FEEDS = {}
