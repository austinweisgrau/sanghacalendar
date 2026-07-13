"""
Albany, NY Capital Region — Phase 3 expansion (heartbeat 87).

Albany (pop. ~100K city / ~900K metro) is New York's state capital. The Capital
Region spans Albany, Troy, Schenectady, and surrounding suburbs. Despite its
modest size, the area supports a solid Buddhist community with Tibetan, Plum
Village/Zen, and Insight representation.

Centers included:
  - Kingfisher Sangha (kingfisher_sangha_schenectady)
    Plum Village / Thich Nhat Hanh lineage (Order of Interbeing)
    Unitarian Universalist Society of Schenectady, 1221 Wendell Ave, Schenectady NY 12308
    kingfishersangha.com · Live WordPress iCal feed
    Primary in-person: Sunday 4:30–6pm (hybrid); multiple Zoom sub-groups

  - Shambhala Meditation Center of Albany (shambhala_albany)
    Tibetan Vajrayana (Shambhala / Chögyam Trungpa lineage)
    747 Madison Avenue Suite 202, Albany NY 12208
    albany.shambhala.org · Mon 5:30pm, Wed 6pm open sits; last Sun 11am
    Shambhala Cologne server down; seeded as recurring

  - Shambhala Meditation Group of Troy (shambhala_troy)
    Tibetan Vajrayana (Shambhala / Chögyam Trungpa lineage)
    Congress Street, Troy NY 12180
    troy.shambhala.org · Thursday 6:30pm weekly sit (hybrid Zoom + in-person)
    Shambhala Cologne server down; seeded as recurring

  - Albany KTC (albany_ktc)
    Tibetan Buddhism — Kagyu lineage (Karma Triyana Dharmachakra affiliate)
    199 Washington Avenue, Rensselaer NY 12144
    albanyktc.org · Sunday 9:30am public meditation
    No iCal feed confirmed; seeded as recurring

Research notes (2026-07-13):
  - Kingfisher Sangha: Plum Village network with 5 sub-groups throughout Capital Region.
    Primary in-person sit is Kingfisher South every Sunday 4:30–6pm at UU Society of
    Schenectady (1221 Wendell Ave, Schenectady), hybrid in-person + Zoom. Other
    sub-groups (North, East, Village, Sun) are Zoom-only. WordPress iCal feed confirmed
    at kingfishersangha.com/events/?ical=1. Contact: kingfishersanghany@gmail.com.
  - Shambhala Albany: 747 Madison Ave Suite 202 (Pine Hills neighborhood). Multiple
    weekly public sits: Monday 5:30–6:30pm, Wednesday 6–7pm (open sitting; instruction
    available), last Sunday of month 11am–1pm (Nyinthun/extended). Also Learn to
    Meditate (1st Wednesday 7–8:30pm) and Heart of Recovery (Monday 7–8pm).
    Shambhala Cologne iCal server (shambhala-koeln.de) timing out as of 2026-07-13.
  - Shambhala Troy: Meets on Congress Street, Troy (exact address via troy.shambhala.org).
    Thursday 6:30–7:30pm sit (instruction at 6pm), format: sitting + teaching + discussion.
    Offered hybrid (in-person + Zoom). Contact: troy@shambhala.org.
    Cologne server unavailable; seeded as recurring.
  - Albany KTC: Karma Thegsum Choling affiliated with KTD (Karma Triyana Dharmachakra,
    North American seat of 17th Karmapa Ogyen Trinley Dorje). 199 Washington Ave,
    Rensselaer NY 12144. Sunday 9:30am public meditation; additional programs vary.
    Contact: ktc.director@albanyktc.org / (518) 434-7420.
  - Diamond Way Albany (265 Morris St): meditation posted as canceled as of research date.
  - Kadampa Saratoga Springs: class suspended (looking for new venue). Not added.
  - Albany Buddhist Sangha (Shin/Jodo Shinshu): more community service + chanting than
    sitting meditation; not added as a sit-focused center.
  - Albany Tendai Buddhist Sangha: monthly schedule unconfirmed; defer.
  - Albany Vipassana Group: meets Mon 7:30pm, but no current web presence confirmed.
    Monitor; contact if web presence returns.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "kingfisher_sangha_schenectady": Center(
        id="kingfisher_sangha_schenectady",
        name="Kingfisher Sangha",
        url="https://kingfishersangha.com",
        address="1221 Wendell Ave",
        city="Schenectady",
        state="NY",
        zip_code="12308",
        lat=42.8033,
        lng=-73.9507,
        neighborhood="Woodlawn",
        tradition=Tradition.ZEN,
        notes=(
            "Kingfisher Sangha is a Plum Village / Thich Nhat Hanh community in the "
            "Capital Region of New York, practicing in the Order of Interbeing tradition. "
            "The primary in-person sit is Kingfisher South every Sunday 4:30–6pm at the "
            "Unitarian Universalist Society of Schenectady, 1221 Wendell Ave — hybrid "
            "in-person and Zoom, all welcome, handicap accessible. Multiple sub-groups "
            "meet throughout the week via Zoom: Kingfisher North (Tuesdays 7pm), "
            "Kingfisher East (Wednesdays 5pm), Kingfisher Sun (Thursdays 1:30pm). "
            "Contact: kingfishersanghany@gmail.com. kingfishersangha.com."
        ),
    ),
    "shambhala_albany": Center(
        id="shambhala_albany",
        name="Shambhala Meditation Center of Albany",
        url="https://albany.shambhala.org",
        address="747 Madison Avenue Suite 202",
        city="Albany",
        state="NY",
        zip_code="12208",
        lat=42.6539,
        lng=-73.7884,
        neighborhood="Pine Hills",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Center of Albany offers meditation in the Shambhala "
            "tradition founded by Chögyam Trungpa Rinpoche. Weekly public sits: Monday "
            "5:30–6:30pm (open sitting, free, all welcome) and Wednesday 6–7pm (open "
            "sitting with instruction available). The last Sunday of each month hosts an "
            "extended Nyinthun (11am–1pm). Also offers Learn to Meditate (1st Wednesday "
            "7pm) and Heart of Recovery (Monday 7pm, 12-step compatible). Located at "
            "747 Madison Avenue Suite 202, Pine Hills neighborhood, Albany NY 12208. "
            "albany.shambhala.org."
        ),
    ),
    "shambhala_troy": Center(
        id="shambhala_troy",
        name="Shambhala Meditation Group of Troy",
        url="https://troy.shambhala.org",
        address="Congress Street",
        city="Troy",
        state="NY",
        zip_code="12180",
        lat=42.7296,
        lng=-73.6930,
        neighborhood="Downtown Troy",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Group of Troy is a small Shambhala sitting group in "
            "Troy, NY (Capital Region). Meets weekly on Thursdays at 6:30–7:30pm for "
            "sitting meditation, a brief teaching, and discussion. Free meditation "
            "instruction available at 6pm for newcomers. Offered hybrid (in-person + "
            "Zoom). Part of the international Shambhala community founded by Chögyam "
            "Trungpa Rinpoche. Contact: troy@shambhala.org. troy.shambhala.org."
        ),
    ),
    "albany_ktc": Center(
        id="albany_ktc",
        name="Albany KTC — Karma Thegsum Choling",
        url="https://www.albanyktc.org",
        address="199 Washington Avenue",
        city="Rensselaer",
        state="NY",
        zip_code="12144",
        lat=42.6523,
        lng=-73.7371,
        neighborhood="Rensselaer (Albany metro)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Albany KTC (Karma Thegsum Choling) is a Kagyu Tibetan Buddhist center "
            "affiliated with Karma Triyana Dharmachakra (KTD), the North American seat "
            "of His Holiness the 17th Karmapa Ogyen Trinley Dorje, located in Woodstock, "
            "NY. Offers Sunday morning public meditation (9:30am) and additional programs. "
            "199 Washington Avenue, Rensselaer, NY 12144 (across the Hudson River from "
            "Albany). Contact: ktc.director@albanyktc.org / (518) 434-7420. "
            "albanyktc.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {
    "kingfisher_sangha_schenectady": {
        # WordPress Events Calendar (ECPv6) iCal export.
        # Verified working 2026-07-13: returns multiple recurring sits for all
        # Kingfisher sub-groups (South in-person Schenectady, North/East/Sun/Village Zoom).
        # Enrichment will classify location_type per event (in-person vs online).
        "url": "https://kingfishersangha.com/events/?ical=1",
        "filter_to_sits": True,
    },
}
