"""
Center registry — static metadata for all known centers.
Keyed by org_id. Serves as the source of truth for center bio pages.
"""

CENTERS = {
    "imc_berkeley": {
        "id": "imc_berkeley",
        "name": "Insight Meditation Center",
        "tradition": "theravada",
        "url": "https://www.insightmeditationcenter.org",
        "address": "1205 Hopkins St",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94702",
        "neighborhood": "West Berkeley",
        "lat": 37.8789,
        "lng": -122.2865,
        "description": (
            "IMC Berkeley is a Theravada-based community offering daily sits, "
            "dharma talks, and retreats. Founded by Gil Fronsdal, the center draws "
            "from the Vipassana tradition and is known for accessible, psychologically "
            "sophisticated teachings. Drop-in sits welcome."
        ),
    },
    "ebmc": {
        "id": "ebmc",
        "name": "East Bay Meditation Center",
        "tradition": "pluralist",
        "url": "https://eastbaymeditation.org",
        "address": "285 17th St",
        "city": "Oakland",
        "state": "CA",
        "zip": "94612",
        "neighborhood": "Uptown Oakland",
        "lat": 37.8076,
        "lng": -122.2697,
        "description": (
            "EBMC is a justice-oriented, radically inclusive meditation center in "
            "downtown Oakland. Known for its many identity-centered affinity sanghas — "
            "BIPOC, LGBTQ+, trans and gender-expansive, disabled, and more — alongside "
            "general community sits. Practice is rooted in the Theravada tradition "
            "with a strong commitment to intersectionality and accessibility."
        ),
    },
    "shambhala_berkeley": {
        "id": "shambhala_berkeley",
        "name": "Berkeley Shambhala Center",
        "tradition": "tibetan",
        "url": "https://berkeley.shambhala.org",
        "address": "2288 Fulton St",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94704",
        "neighborhood": "South Campus Berkeley",
        "lat": 37.8696,
        "lng": -122.2677,
        "description": (
            "Berkeley Shambhala offers sitting meditation practice in the Shambhala "
            "Buddhist tradition, which draws from Tibetan Buddhism and emphasizes "
            "meditation as a path to basic goodness. Drop-in sits and longer programs "
            "available. No prior experience required."
        ),
    },
    "empty_gate_zen": {
        "id": "empty_gate_zen",
        "name": "Empty Gate Zen Center",
        "tradition": "zen",
        "url": "https://emptygatezen.com",
        "address": "2200 Parker St",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94704",
        "neighborhood": "South Berkeley",
        "lat": 37.8634,
        "lng": -122.2597,
        "description": (
            "Empty Gate Zen Center is a Korean Zen (Kwan Um School) practice community "
            "with a dense daily schedule of zazen and chanting. Known for rigorous, "
            "traditional practice. Contact the center before your first visit."
        ),
    },
    "oakland_zen": {
        "id": "oakland_zen",
        "name": "Oakland Zen Center / Kojin-an",
        "tradition": "zen",
        "url": "https://oaklandzencenter.org",
        "address": "6140 Chabot Rd",
        "city": "Oakland",
        "state": "CA",
        "zip": "94618",
        "neighborhood": "Rockridge",
        "lat": 37.8397,
        "lng": -122.2278,
        "description": (
            "Kojin-an is a small, intimate Soto Zen zendo in the Rockridge hills. "
            "Family-run and welcoming, with morning and evening zazen, Sunday zazenkai, "
            "and regular sesshins. First-timers should contact ahead of visiting."
        ),
    },
    "bay_zen": {
        "id": "bay_zen",
        "name": "Bay Zen Center",
        "tradition": "zen",
        "url": "https://bayzen.org",
        "address": "3824 Grand Ave",
        "city": "Oakland",
        "state": "CA",
        "zip": "94610",
        "neighborhood": "Grand Lake",
        "lat": 37.8145,
        "lng": -122.2286,
        "description": (
            "Bay Zen Center offers Soto Zen practice in the heart of Grand Lake, Oakland. "
            "Weekly evening zazen, dharma talks, and periodic sesshins."
        ),
    },
    "spirit_rock": {
        "id": "spirit_rock",
        "name": "Spirit Rock Meditation Center",
        "tradition": "theravada",
        "url": "https://www.spiritrock.org",
        "address": "5000 Sir Francis Drake Blvd",
        "city": "Woodacre",
        "state": "CA",
        "zip": "94973",
        "neighborhood": "West Marin",
        "lat": 37.9878,
        "lng": -122.6318,
        "description": (
            "Spirit Rock is a major Insight Meditation retreat center in West Marin, "
            "about an hour from the East Bay. Best known for residential retreats, "
            "it also offers weekly drop-in meditation groups and daylong programs. "
            "A pilgrimage-worthy destination for serious practitioners."
        ),
    },
    "metta_dharma": {
        "id": "metta_dharma",
        "name": "Metta Dharma Foundation",
        "tradition": "theravada",
        "url": "https://www.mettadharma.org",
        "address": "2837 Claremont Blvd",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94705",
        "neighborhood": "Claremont",
        "lat": 37.8579,
        "lng": -122.2432,
        "description": (
            "Metta Dharma Foundation hosts intimate Wednesday evening sits in the "
            "Claremont neighborhood of Berkeley, led by teacher Richard Shankman. "
            "Sit followed by brief dharma sharing. Dana-based."
        ),
    },
}
