"""
Buffalo, NY — Phase 3 expansion (heartbeat 86).

Buffalo (pop. ~278K city / ~1.2M metro) is the second-largest city in New York State,
situated at the eastern end of Lake Erie. While not a major Buddhist hub, it has a
handful of well-established practice communities including a Zen center affiliated with
Zen Mountain Monastery, a Shambhala group, a Thai Theravada temple, and a Plum Village
sangha.

Centers included:
  - Buffalo Zen Dharma Community (bzdc)
    Zen (Mountains and Rivers Order — John Daido Loori / Shugen Arnold lineage)
    Westminster Presbyterian Church, 724 Delaware Avenue, Buffalo NY 14209
    buffalozen.org · Tuesday evenings (no iCal) — seeded as recurring

  - Shambhala Meditation Group of Buffalo (shambhala_buffalo)
    Tibetan Vajrayana (Shambhala / Chögyam Trungpa lineage)
    C.G. Jung Center, 408 Franklin Street, Buffalo NY 14202
    No current website (stale blogspot) · Thu 7pm + 2nd Sun — seeded as recurring

  - Wat Prodketusa / Niagara Falls Buddhist Meditation Center of NY (wat_prodketusa)
    Thai Theravada
    2660 Bedell Road, Grand Island, NY 14072
    watprodketusa.org · Wednesday 6pm public meditation — seeded as recurring

  - Peaceful Heart Sangha (peaceful_heart_buffalo)
    Plum Village / Thich Nhat Hanh lineage (Order of Interbeing)
    Unitarian Universalist Church of Buffalo, 695 Elmwood Avenue, Buffalo NY 14222
    buffalomindfulness.org · Saturday 11am (Zoom) — seeded as recurring

Research notes (2026-07-10):
  - BZDC: Mountains and Rivers Order (affiliated with Zen Mountain Monastery, Mt. Tremper NY,
    teacher Shugen Arnold Roshi). Meets Tuesday evenings at Westminster Presbyterian Church,
    724 Delaware Avenue (near Allentown neighborhood). First Tuesday is orientation/newcomer
    intro. Monthly Saturday half-day zazen intensive at 1272 Delaware Ave (Network of Religious
    Communities) — by invitation via email list; not seeded (not public drop-in). No iCal feed;
    schedule on buffalozen.org.
  - Shambhala Buffalo: Stale Blogspot site; active schedule confirmed via GoSit.org and
    multiple secondary sources. Meets at C.G. Jung Center (408 Franklin St, Allentown
    neighborhood, Buffalo). Thursday 7–9pm: 1hr sitting + walking meditation, short reading,
    tea; free instruction at 6:45pm. 2nd Sunday monthly: extended Nyinthun. Third Thursday
    has dharma talk after regular sit. Contact: buffaloshambhala@gmail.com / 716-445-4446.
  - Wat Prodketusa: Thai Theravada temple at 2660 Bedell Road, Grand Island NY 14072
    (suburban island between Buffalo and Niagara Falls). watprodketusa.org. Wednesday
    6–7:30pm open public meditation session; daily chanting 6am + 6pm; Sunday services.
    Also known as "Niagara Falls Buddhist Meditation Center of NY."
  - Peaceful Heart Sangha: Plum Village / Thich Nhat Hanh lineage. buffalomindfulness.org
    (WordPress). Meets at UU Church of Buffalo, 695 Elmwood Avenue, Buffalo NY 14222.
    Saturday 11am–12pm Zoom sit confirmed active. In-person schedule (Tue/Wed evenings)
    reportedly returning but unconfirmed — only seeding the confirmed Saturday Zoom sit.
  - Not added: WNY Meditation & Mindfulness Community — primary website (wnymeditation.org)
    unreachable; backup Google Sites shows Wed 7pm (Williamsville) + Sun 6:30pm (Elmwood).
    Deferred until website reliability confirmed.
  - Not added: Urban Monks (Delaware Park, outdoor) — schedule last confirmed circa 2020;
    unverified as active. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "bzdc": Center(
        id="bzdc",
        name="Buffalo Zen Dharma Community",
        url="https://www.buffalozen.org",
        address="724 Delaware Avenue",
        city="Buffalo",
        state="NY",
        zip_code="14209",
        lat=42.9130,
        lng=-78.8828,
        neighborhood="Allentown",
        tradition=Tradition.ZEN,
        notes=(
            "Buffalo Zen Dharma Community (BZDC) is a Mountains and Rivers Order sangha "
            "affiliated with Zen Mountain Monastery (Mt. Tremper, NY) and teacher Shugen "
            "Arnold Roshi. Offers weekly Tuesday evening zazen, dharma study, and "
            "community practice at Westminster Presbyterian Church, 724 Delaware Avenue. "
            "The first Tuesday of each month is an orientation/newcomer introduction. "
            "Monthly Saturday half-day sittings are held for practicing members. "
            "Drop-in welcome on Tuesdays; free. buffalozen.org."
        ),
    ),
    "shambhala_buffalo": Center(
        id="shambhala_buffalo",
        name="Shambhala Meditation Group of Buffalo",
        url="https://buffalo.shambhala.org",
        address="408 Franklin Street",
        city="Buffalo",
        state="NY",
        zip_code="14202",
        lat=42.8962,
        lng=-78.8777,
        neighborhood="Allentown",
        tradition=Tradition.TIBETAN,
        notes=(
            "Shambhala Meditation Group of Buffalo is part of the Shambhala community "
            "founded by Chögyam Trungpa Rinpoche. Meets weekly at the C.G. Jung Center "
            "(408 Franklin Street, Allentown), Thursdays 7–9pm: one hour of sitting and "
            "walking meditation, a short reading, and tea. Free meditation instruction "
            "available at 6:45pm. The second Sunday monthly is an extended Nyinthun "
            "(longer sitting). Open to all; free (donations welcome). "
            "Contact: buffaloshambhala@gmail.com / (716) 445-4446."
        ),
    ),
    "wat_prodketusa": Center(
        id="wat_prodketusa",
        name="Wat Prodketusa — Niagara Falls Buddhist Meditation Center of NY",
        url="https://watprodketusa.org",
        address="2660 Bedell Road",
        city="Grand Island",
        state="NY",
        zip_code="14072",
        lat=43.0187,
        lng=-78.9627,
        neighborhood="Grand Island (Buffalo metro)",
        tradition=Tradition.THERAVADA,
        notes=(
            "Wat Prodketusa (also known as Niagara Falls Buddhist Meditation Center of NY) "
            "is a Thai Theravada temple on Grand Island, between Buffalo and Niagara Falls. "
            "Offers public Wednesday evening meditation (6–7:30pm), daily chanting sessions "
            "(6am and 6pm), and Sunday services open to all. The Wednesday evening program "
            "is the primary public sit. 2660 Bedell Road, Grand Island, NY 14072. "
            "(716) 775-5446. watprodketusa.org."
        ),
    ),
    "peaceful_heart_buffalo": Center(
        id="peaceful_heart_buffalo",
        name="Peaceful Heart Sangha",
        url="https://buffalomindfulness.org",
        address="695 Elmwood Avenue",
        city="Buffalo",
        state="NY",
        zip_code="14222",
        lat=42.9202,
        lng=-78.8792,
        neighborhood="Elmwood Village",
        tradition=Tradition.ZEN,
        notes=(
            "Peaceful Heart Sangha is a Buffalo-area meditation community practicing in "
            "the tradition of Thich Nhat Hanh and the Plum Village lineage (Order of "
            "Interbeing). Meets weekly on Saturday mornings via Zoom (11am–12pm ET) "
            "and occasionally in-person at the Unitarian Universalist Church of Buffalo, "
            "695 Elmwood Avenue. Guided sitting and walking meditation, dharma sharing. "
            "All are welcome; free. buffalomindfulness.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

# No iCal feeds available for any Buffalo centers. All sits seeded as recurring.
ICAL_FEEDS: dict = {}
