"""
Anchorage, Alaska — Phase 3 expansion (heartbeat 72).

Anchorage (pop. ~290k; metro ~400k) is Alaska's largest city and home to a
small but diverse Buddhist community spanning Zen, Tibetan, and Plum Village
traditions. The practice scene is tight-knit; several groups cross-promote
each other on their websites.

Centers included:
  - Anchorage Zen Community (anchorage_zen)
    Soto Zen, ordained teacher (Genmyo Zeedyk, Dharma transmission 2013)
    711 Barrow St, Anchorage AK 99501 (downtown, between 7th & 8th Ave)
    anchoragezen.com · Sun 8:30–9:55am hybrid (zazen + kinhin + dharma talk)
    No iCal — seeded as recurring.

  - Upright Noble Zen (upright_noble_zen)
    Soto Zen — White Plum Asanga, Maezumi / Chozen-Hogen Bays lineage
    437 E 3rd Ave, Anchorage AK 99501 (Pioneer Schoolhouse)
    uprightnoble.wordpress.com · Sun 5–6:30pm hybrid + Mon–Thu 6:30am Zoom
    No iCal — seeded as recurring.

  - Katog Sangyey Ling (katog_sangyey_ling)
    Tibetan Buddhism — Nyingma (Katog Choling lineage, Khentrul Lodrö Thayé Rinpoche)
    4105 E Turnagain Blvd, Suite C3, Anchorage AK 99517
    katogsangyeyling.org · Tue 6:30–7:30pm hybrid
    No iCal — seeded as recurring.

Research notes (2026-05-28):
  - Anchorage Zen Community: Founded by Genmyo Zeedyk (ordained 2009, Dharma
    transmission 2013). Most active Zen group in Anchorage. 711 Barrow St
    (between 7th & 8th Ave, downtown). Sunday program: 8:30am zazen blocks
    with kinhin, 10am dharma talk + discussion; beginner instruction available.
    Weekday Zoom sittings also offered. anchoragezen.com (SSL expired; http works).
  - Upright Noble Zen: Teacher Dana Kojun Lederhos-Hull, first Dharma Successor
    of Chozen/Hogen Bays. Sunday 5–6:30pm at Pioneer Schoolhouse (437 E 3rd Ave)
    + simultaneous Zoom (898-544-2353, pw: zazen). Mon–Thu 6:30am Zoom-only
    (25-min sit + Heart Sutra). uprightnoble.wordpress.com. Drop-in welcome.
  - Katog Sangyey Ling: formerly Anchorage Sangha Meditation Group. 4105 E
    Turnagain Blvd, Suite C3, Anchorage AK 99517. Nyingma Tibetan under
    Khentrul Lodrö Thayé Rinpoche (Katog Choling lineage). Tuesday 6:30–7:30pm
    in-person + Zoom. Alternates monthly: Tonglen, Shamatha, Heart Sutra.
    No experience required. katogsangyeyling.org.
  - Meditate in Alaska (KMC Washington branch): Sunday 10am in-person at Namaste
    North Yoga (400 L St). NKT Tibetan. First 3 Sundays, September–May only.
    Seasonal — deferred until Sept 2026.
  - Fireweed Sangha: Plum Village / TNH lineage. Monday 6:30pm Zoom-only.
    Transitioned to online-only May 2025. Zoom link via private email subscription
    (not publicly accessible). Skip.
  - Chagdud Gompa Tromge Ling: website ECONNREFUSED (tromgeling.org). Vajrayana
    Nyingma. May be dormant or operating informally. Deferred.
  - Wat Alaska Yanna Vararam (2309 D St, Anchorage): Thai Theravada. Daily 8am
    and 8pm public chanting + meditation. No website; phone: (907) 272-3699.
    Deferred — needs address/lat-lng verification.
  - Buddhist Meditation Center / Wat Dhamma Bhavana (738 W 72nd Ave): Thai
    Theravada (Maha Nikaya). No schedule online; call (907) 344-9994. Deferred.
  - IASC-AK / Mahayana Center for Tibetan Buddhism: website ECONNREFUSED.
    Possible dormant. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "anchorage_zen": Center(
        id="anchorage_zen",
        name="Anchorage Zen Community",
        url="http://www.anchoragezen.com",
        address="711 Barrow St",
        city="Anchorage",
        state="AK",
        zip_code="99501",
        lat=61.2143,
        lng=-149.9003,
        neighborhood="Downtown Anchorage",
        tradition=Tradition.ZEN,
        notes=(
            "Anchorage Zen Community (AZC) is Anchorage's primary Zen sitting group, "
            "led by ordained priest Genmyo Zeedyk (Dharma transmission 2013). Soto "
            "Zen tradition. Located at 711 Barrow St, between 7th and 8th Ave, "
            "downtown Anchorage. Sunday program: 8:30–9:55am zazen blocks with "
            "kinhin (walking meditation) in-person and on Zoom; 10:00am Dharma talk "
            "and discussion. Beginner instruction available Sunday mornings before "
            "the 9am session. Drop-in welcome; no cost. Weekday morning Zoom sittings "
            "also offered (check website for current schedule). anchoragezen.com."
        ),
    ),
    "upright_noble_zen": Center(
        id="upright_noble_zen",
        name="Upright Noble Zen",
        url="https://uprightnoble.wordpress.com",
        address="437 E 3rd Ave",
        city="Anchorage",
        state="AK",
        zip_code="99501",
        lat=61.2163,
        lng=-149.8775,
        neighborhood="Downtown Anchorage",
        tradition=Tradition.ZEN,
        notes=(
            "Upright Noble Zen is an Anchorage Soto Zen group led by Dana Kojun "
            "Lederhos-Hull, the first Dharma Successor of Chozen (Jan) and Hogen "
            "Bays of Great Vow Zen Monastery. Member of the White Plum Asanga and "
            "Soto Zen Buddhist Association. Sunday 5:00–6:30pm in-person at the "
            "Pioneer Schoolhouse (437 E 3rd Avenue) plus simultaneous Zoom; includes "
            "two 25-min zazen periods, Dharma Talk, check-in, and chanting. Monday "
            "through Thursday 6:30am Zoom-only 25-min sitting with Heart Sutra "
            "chanting. Everyone welcome; drop-in. Monthly zazenkai and sesshin "
            "retreats October through April. anchoragemeditation@gmail.com."
        ),
    ),
    "katog_sangyey_ling": Center(
        id="katog_sangyey_ling",
        name="Katog Sangyey Ling",
        url="https://www.katogsangyeyling.org",
        address="4105 E Turnagain Blvd, Suite C3",
        city="Anchorage",
        state="AK",
        zip_code="99517",
        lat=61.2061,
        lng=-149.9448,
        neighborhood="Turnagain",
        tradition=Tradition.TIBETAN,
        notes=(
            "Katog Sangyey Ling (formerly Anchorage Sangha Meditation Group) is a "
            "Tibetan Buddhist center in the Nyingma Katog Choling lineage, under the "
            "guidance of Khentrul Lodrö Thayé Rinpoche. Located at 4105 E Turnagain "
            "Blvd, Suite C3, Anchorage AK 99517 (Turnagain neighborhood). Tuesday "
            "6:30–7:30pm hybrid: in-person and Zoom (email katogsangyeyling@gmail.com "
            "for Zoom link). Sessions alternate monthly between Tonglen (loving-"
            "kindness), Shamatha (calm-abiding meditation), and Heart Sutra practice. "
            "No prior experience necessary; everyone welcome. (907) 947-8881. "
            "katogsangyeyling.org."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — all centers seeded via scripts/sangha-seed-recurring.js
