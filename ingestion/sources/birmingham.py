"""
Birmingham, Alabama — Phase 3 expansion (heartbeat 73).

Birmingham (pop. ~210k; metro ~1.1M) is Alabama's largest city. The Buddhist
meditation scene is anchored by Birmingham Shambhala, which also hosts two
visiting groups (Burning Rock Soto Zen and Recovery Dharma). A Plum Village
sangha (Cahaba River) meets at Unity Church in Southside, and a Tibetan
center (Losel Maitri) serves the southeast suburbs.

Centers included:
  - Birmingham Shambhala Meditation Center (birmingham_shambhala)
    Vajrayana / Kagyu-Shambhala, 714 37th St S, Birmingham AL 35222 (Avondale)
    birmingham.shambhala.org · Mon/Tue 7pm + Wed/Fri 7am + 1st Sun 10am hybrid
    No iCal (Cologne server 404, local site Cloudflare-blocked) — seeded as recurring.

  - Burning Rock Soto Zen (burning_rock_soto_zen)
    Soto Zen (Silent Thunder Order / Atlanta Soto Zen lineage)
    Meets at Birmingham Shambhala, 714 37th St S, Birmingham AL 35222
    Sun 1:15–2pm in-person. No iCal — seeded as recurring.

  - Cahaba River Sangha (cahaba_river_sangha)
    Plum Village / Thich Nhat Hanh, Unity Church, 2803 Highland Ave, Birmingham AL 35205
    cahabariversangha.com · Thu 7–8:30pm hybrid (main public sit)
    WordPress site (?ical=1 returns HTML — no iCal plugin). Seeded as recurring.

  - Losel Maitri Tibetan Buddhist Center (losel_maitri)
    Vajrayana / Tibetan (Namgyal Monastery lineage, resident teacher Tenzin Deshek)
    3224 Green Valley Rd, Cahaba Heights AL 35243 (southeast suburb)
    Website down (ECONNREFUSED). Tue 7pm open to all. Seeded from Facebook/directory data.

Research notes (2026-05-31):
  - Birmingham Shambhala (center=175): shambhala.org/calendar/ical/?center=175 returns
    404 — Cologne server pattern does not cover this center. Local site blocked by
    Cloudflare (403). Seeded manually from website schedule.
  - Burning Rock Soto Zen: affiliated with Silent Thunder Order and ASZC. Teacher is
    Andrew Keitt. Meets at Shambhala space. No dedicated website accessible.
    burningrocksotozen.org domain exists but may redirect or be down.
  - Cahaba River Sangha: active Plum Village group, Thursday sits are primary public event.
    Site has WordPress backend but no working iCal endpoint (?ical=1 returns full HTML,
    /my-calendar-ics/ returns 404). Email reminders only.
  - Losel Maitri: Namgyal Monastery lineage (Ithaca NY). Resident teacher Ven. Tenzin
    Deshek. 3224 Green Valley Rd, Cahaba Heights AL 35243; also listed as 3118 Bellwood
    Drive. Website (loselmaitribuddhist.org) ECONNREFUSED. FB page active (2,920 followers).
    Tuesday 5:50pm intro class + 7pm open worship service. Phone: (205) 470-6940.
  - Alabama Buddhist Vihara: relocated to Pell City, AL (35 miles east) Nov 2025 —
    outside Birmingham metro coverage; deferred.
  - Firefly Sangha (Indian Springs): small Plum Village group at St. Francis Episcopal,
    Cahaba Valley Rd. Monday 7pm sits. Small and suburban — deferred; may add later.
  - Longleaf Forest Dhamma: Zoom-only, Thai Forest. No physical Birmingham presence.
    Deferred.
  - UUCB Meditation Group: Interfaith, Sunday 11:30am at UU Church. Fits profile but
    very small. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "birmingham_shambhala": Center(
        id="birmingham_shambhala",
        name="Birmingham Shambhala Meditation Center",
        url="https://birmingham.shambhala.org",
        address="714 37th Street South",
        city="Birmingham",
        state="AL",
        zip_code="35222",
        lat=33.5132,
        lng=-86.7684,
        neighborhood="Avondale",
        tradition=Tradition.TIBETAN,
        notes=(
            "Birmingham Shambhala Meditation Center has served the Birmingham area "
            "since 1997, offering a welcoming entry point to Shambhala Buddhist "
            "meditation practice. Located in the Avondale neighborhood at 714 37th "
            "Street South. Regular public sits: Monday and Tuesday 7–8pm (hybrid "
            "in-person + Zoom; newcomers receive abbreviated instruction), Wednesday "
            "7–8am (in-person), Friday 7–8am (hybrid), and First Sunday 10am–noon "
            "(hybrid community sit). The center also hosts Burning Rock Soto Zen "
            "(Sunday 1:15pm) and Recovery Dharma (Sunday 6:30pm). All sits are free "
            "and open to all. birmingham.shambhala.org. (205) 515-1756."
        ),
    ),
    "burning_rock_soto_zen": Center(
        id="burning_rock_soto_zen",
        name="Burning Rock Soto Zen",
        url="https://alabamameditationnetwork.com/burning-rock-soto-zen/",
        address="714 37th Street South",
        city="Birmingham",
        state="AL",
        zip_code="35222",
        lat=33.5132,
        lng=-86.7684,
        neighborhood="Avondale",
        tradition=Tradition.ZEN,
        notes=(
            "Burning Rock Soto Zen is a Soto Zen sitting group led by Andrew Keitt, "
            "affiliated with the Silent Thunder Order and the Atlanta Soto Zen Center. "
            "Meets at the Birmingham Shambhala Meditation Center, 714 37th Street "
            "South, Avondale. Public zazen: Sundays 1:15–2pm (beginner orientation "
            "1:15–1:30pm, zazen 1:30–2pm). Quarterly extended sittings noon–5pm. "
            "Free and open to all; drop-in welcome. Listed at "
            "alabamameditationnetwork.com/burning-rock-soto-zen/."
        ),
    ),
    "cahaba_river_sangha": Center(
        id="cahaba_river_sangha",
        name="Cahaba River Sangha",
        url="https://cahabariversangha.com",
        address="2803 Highland Ave",
        city="Birmingham",
        state="AL",
        zip_code="35205",
        lat=33.5011,
        lng=-86.7975,
        neighborhood="Southside",
        tradition=Tradition.ZEN,
        notes=(
            "Cahaba River Sangha is Birmingham's Plum Village / Thich Nhat Hanh "
            "community, meeting at Unity Church of Birmingham in the Southside "
            "neighborhood (2803 Highland Ave). The main weekly public sit is Thursday "
            "7:00–8:30pm (meditation, dharma talk/discussion; hybrid in-person + Zoom). "
            "Additional sits and study groups during the week. Monthly Days of "
            "Mindfulness (free, registration requested). cahabariversangha.com."
        ),
    ),
    "losel_maitri": Center(
        id="losel_maitri",
        name="Losel Maitri Tibetan Buddhist Center",
        url="https://www.facebook.com/LoselMaitriBuddhist/",
        address="3224 Green Valley Rd",
        city="Vestavia Hills",
        state="AL",
        zip_code="35243",
        lat=33.4728,
        lng=-86.7332,
        neighborhood="Cahaba Heights",
        tradition=Tradition.TIBETAN,
        notes=(
            "Losel Maitri Tibetan Buddhist Center is affiliated with Namgyal Monastery "
            "(Ithaca, NY), the personal monastery of His Holiness the Dalai Lama in "
            "North America. Resident teacher: Ven. Tenzin Deshek. Located in Cahaba "
            "Heights (Vestavia Hills). Weekly open worship service Tuesdays 7–8pm, "
            "open to all. Tuesday 5:50pm introduction to Buddhism class. Website is "
            "currently offline; check Facebook for current schedule. (205) 470-6940. "
            "loselmaitribuddhist.org (offline — see Facebook)."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — all centers seeded via scripts/sangha-seed-recurring.js
