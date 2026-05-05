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
    "berkeley_buddhist_monastery": {
        "id": "berkeley_buddhist_monastery",
        "name": "Berkeley Buddhist Monastery",
        "tradition": "zen",
        "url": "https://www.berkeleymonastery.org",
        "address": "2304 McKinley Ave",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94703",
        "neighborhood": "North Berkeley",
        "lat": 37.8758,
        "lng": -122.2637,
        "description": (
            "Berkeley Buddhist Monastery is a Chan (Chinese Zen) monastery offering "
            "daily sitting meditation open to the public — early morning sits Thu/Fri "
            "and evening sits every day of the week. The practice is traditional and "
            "austere, rooted in the City of Ten Thousand Buddhas lineage. Free of charge."
        ),
    },
    "insight_berkeley": {
        "id": "insight_berkeley",
        "name": "Insight Meditation Community of Berkeley",
        "tradition": "theravada",
        "url": "https://www.insightberkeley.org",
        "address": "2304 McKinley Ave",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94703",
        "neighborhood": "North Berkeley",
        "lat": 37.8758,
        "lng": -122.2637,
        "description": (
            "Insight Meditation Community of Berkeley meets Thursday evenings at "
            "Berkeley Buddhist Monastery. Led by James Baraz and Eve Decker, the "
            "community is grounded in Vipassana practice with an emphasis on joy, "
            "lovingkindness, and awakening. Dana-based, drop-in welcome."
        ),
    },
    "berkeley_priory": {
        "id": "berkeley_priory",
        "name": "Berkeley Buddhist Priory",
        "tradition": "zen",
        "url": "https://berkeleybuddhistpriory.org",
        "address": "1358 Marin Ave",
        "city": "Albany",
        "state": "CA",
        "zip": "94706",
        "neighborhood": "Albany",
        "lat": 37.8934,
        "lng": -122.2987,
        "description": (
            "Berkeley Buddhist Priory is a small residential monastery in the Order "
            "of Buddhist Contemplatives lineage — a British Soto Zen tradition founded "
            "by Jiyu-Kennett Roshi. Sunday morning meditation is open to all. The "
            "practice emphasizes stillness, ceremony, and lay-monastic integration."
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
    "berkeley_alembic": {
        "id": "berkeley_alembic",
        "name": "Berkeley Alembic",
        "tradition": "secular",
        "url": "https://www.berkeleyalembic.com",
        "address": "2820 7th St",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94710",
        "neighborhood": "West Berkeley",
        "lat": 37.8604,
        "lng": -122.2988,
        "description": (
            "Berkeley Alembic is a secular meditation and contemplative arts center "
            "in West Berkeley, associated with teacher Michael Taft (Deconstructing "
            "Yourself). Offers meditation sits, workshops, and events drawing from "
            "secular mindfulness, neuroscience, and non-dual inquiry. No religious "
            "affiliation required."
        ),
    },
    "sfzc_city_center": {
        "id": "sfzc_city_center",
        "name": "SF Zen Center — City Center",
        "tradition": "zen",
        "url": "https://www.sfzc.org/city-center",
        "address": "300 Page St",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94102",
        "neighborhood": "Hayes Valley",
        "lat": 37.7726,
        "lng": -122.4243,
        "description": (
            "SF Zen Center's City Center (also called Beginner's Mind Temple) is the "
            "urban home of one of the largest Soto Zen communities outside Japan. "
            "Founded by Shunryu Suzuki Roshi in 1969, it offers daily zazen open to "
            "all, as well as dharma talks, classes, and residential practice. "
            "Drop-in welcome."
        ),
    },
    "hartford_zen": {
        "id": "hartford_zen",
        "name": "Hartford Street Zen Center",
        "tradition": "zen",
        "url": "https://www.hszc.org",
        "address": "57 Hartford St",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94114",
        "neighborhood": "Castro",
        "lat": 37.7588,
        "lng": -122.4353,
        "description": (
            "Hartford Street Zen Center (Issan-ji) is a Soto Zen temple in the Castro, "
            "founded by Issan Dorsey in 1984. It has deep roots in the LGBTQ+ community "
            "and became known during the AIDS crisis for its compassionate care work. "
            "Daily zazen and weekly dharma talks, open to all."
        ),
    },
    "mission_dharma": {
        "id": "mission_dharma",
        "name": "Mission Dharma",
        "tradition": "theravada",
        "url": "https://www.missiondharma.org",
        "address": "Mission District",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94110",
        "neighborhood": "Mission District",
        "lat": 37.7599,
        "lng": -122.4148,
        "description": (
            "Mission Dharma is a Theravada-based meditation community in San Francisco's "
            "Mission District. Offers weekly sits and dharma talks in the Insight "
            "Meditation tradition. Accessible, community-focused, dana-based."
        ),
    },
    "marin_sangha": {
        "id": "marin_sangha",
        "name": "Marin Sangha",
        "tradition": "theravada",
        "url": "https://www.marinsangha.org",
        "address": "10 Bayview Dr",
        "city": "San Rafael",
        "state": "CA",
        "zip": "94901",
        "neighborhood": "San Rafael",
        "lat": 37.9735,
        "lng": -122.5311,
        "description": (
            "Marin Sangha is an Insight Meditation community in San Rafael offering "
            "weekly sitting meditation and dharma study in the Theravada/Vipassana "
            "tradition. Dana-based, drop-in welcome."
        ),
    },
    "berkeley_zen_center": {
        "id": "berkeley_zen_center",
        "name": "Berkeley Zen Center",
        "tradition": "zen",
        "url": "https://berkeleyzencenter.org",
        "address": "1931 Russell St",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94703",
        "neighborhood": "South Berkeley",
        "lat": 37.8582,
        "lng": -122.2705,
        "description": (
            "Berkeley Zen Center is a Soto Zen community founded in 1967, one of the "
            "oldest and most historically significant American Zen centers. Resident "
            "practice includes daily zazen (Mon–Sat 6am, Mon–Fri 5:40pm, Wed 7:10pm "
            "drop-in). Sesshins and dharma talks offered throughout the year."
        ),
    },
    "dharmata_foundation": {
        "id": "dharmata_foundation",
        "name": "Dharmata Foundation",
        "tradition": "tibetan",
        "url": "https://dharmata.org",
        "address": "235 Washington Ave",
        "city": "Richmond",
        "state": "CA",
        "zip": "94801",
        "neighborhood": "Richmond",
        "lat": 37.9045,
        "lng": -122.3795,
        "description": (
            "Dharmata Foundation is a Tibetan Buddhist center led by Anam Thubten "
            "Rinpoche, a recognized teacher in the Nyingma tradition. Offers monthly "
            "in-person teachings (also available via Zoom) and occasional retreats. "
            "Practice emphasizes direct experience and non-conceptual awareness."
        ),
    },
    "everyday_zen": {
        "id": "everyday_zen",
        "name": "Everyday Zen Foundation",
        "tradition": "zen",
        "url": "https://everydayzen.org",
        "address": "145 Rock Hill Rd",
        "city": "Tiburon",
        "state": "CA",
        "zip": "94920",
        "neighborhood": "Tiburon",
        "lat": 37.8816,
        "lng": -122.4577,
        "description": (
            "Everyday Zen Foundation was founded by Norman Fischer, a poet and Soto Zen "
            "priest trained at San Francisco Zen Center. The community emphasizes an "
            "open, pluralistic approach to Zen practice and meets at Community "
            "Congregational Church in Tiburon. Hybrid in-person and online."
        ),
    },
    "ewam_choden": {
        "id": "ewam_choden",
        "name": "Ewam Choden Tibetan Buddhist Center",
        "tradition": "tibetan",
        "url": "https://www.ewamchoden.org",
        "address": "254 Cambridge Ave",
        "city": "Kensington",
        "state": "CA",
        "zip": "94708",
        "neighborhood": "Kensington",
        "lat": 37.9024,
        "lng": -122.2694,
        "description": (
            "Ewam Choden, founded in 1971, is the oldest Tibetan Buddhist center in "
            "the Western hemisphere. A Sakya tradition center in the hills above "
            "Berkeley, it offers weekly Sunday 10am sitting meditation, teachings, "
            "and periodic retreats. Drop-in welcome."
        ),
    },
    "karuna_berkeley": {
        "id": "karuna_berkeley",
        "name": "Karuna Buddhist Vihara — East Bay",
        "tradition": "theravada",
        "url": "https://karunabv.org",
        "address": "1438 Neilson St",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94702",
        "neighborhood": "Westbrae",
        "lat": 37.8821,
        "lng": -122.2945,
        "description": (
            "Karuna Buddhist Vihara East Bay offers monthly Saturday afternoon sits "
            "(mostly 2nd Saturday, 3–5pm) in the Theravada tradition, including guided "
            "meditation and Dhammapada reading and discussion. Hybrid in-person and "
            "Zoom. Located in the Westbrae neighborhood of Berkeley."
        ),
    },
    "mount_diablo_zen": {
        "id": "mount_diablo_zen",
        "name": "Mount Diablo Zen Group",
        "tradition": "zen",
        "url": "https://mountdiablozencenter.org",
        "address": "404 Gregory Lane, Room 9",
        "city": "Pleasant Hill",
        "state": "CA",
        "zip": "94523",
        "neighborhood": "Pleasant Hill",
        "lat": 37.9499,
        "lng": -122.0935,
        "description": (
            "Mount Diablo Zen Group is a Soto Zen community (SZBA member) in Pleasant "
            "Hill offering weekly Wednesday 7pm zazen. In-person 1st, 3rd, and 5th "
            "Wednesdays; Zoom 2nd and 4th Wednesdays. Drop-in, free, no experience "
            "required. Serving the Contra Costa County area."
        ),
    },
    "nyingma_institute": {
        "id": "nyingma_institute",
        "name": "Nyingma Institute",
        "tradition": "tibetan",
        "url": "https://www.nyingmainstitute.com",
        "address": "1815 Highland Pl",
        "city": "Berkeley",
        "state": "CA",
        "zip": "94709",
        "neighborhood": "North Berkeley",
        "lat": 37.8781,
        "lng": -122.2607,
        "description": (
            "Nyingma Institute, founded by Tarthang Tulku Rinpoche in 1972, is a "
            "Tibetan Buddhist study and practice center in North Berkeley. Offers "
            "courses in Tibetan language, philosophy, and meditation, alongside "
            "public sits, Kum Nye yoga, and periodic retreats."
        ),
    },
    "orgyen_dorje_den": {
        "id": "orgyen_dorje_den",
        "name": "Orgyen Dorje Den",
        "tradition": "tibetan",
        "url": "https://www.orgyen.org",
        "address": "2244 Santa Clara Ave",
        "city": "Alameda",
        "state": "CA",
        "zip": "94501",
        "neighborhood": "Alameda",
        "lat": 37.7648,
        "lng": -122.2476,
        "description": (
            "Orgyen Dorje Den is a Tibetan Vajrayana Buddhist center in Alameda "
            "affiliated with the Dudjom Tersar lineage. Offers tsog practice days, "
            "dharma teachings, and Zoom-accessible programs. Practice emphasizes "
            "Dzogchen and Vajrayana ritual within the Nyingma tradition."
        ),
    },
    "green_gulch_farm": {
        "id": "green_gulch_farm",
        "name": "Green Gulch Farm Zen Center",
        "tradition": "zen",
        "url": "https://sfzc.org/green-gulch-farm",
        "address": "1601 Shoreline Hwy",
        "city": "Muir Beach",
        "state": "CA",
        "zip": "94965",
        "neighborhood": "Muir Beach / West Marin",
        "lat": 37.8694,
        "lng": -122.5630,
        "description": (
            "Green Gulch Farm Zen Center is the Marin satellite of San Francisco Zen Center, "
            "set in a coastal valley near Muir Beach. A working farm and residential practice "
            "community in the Soto Zen tradition. The landmark Sunday Morning Program — "
            "open to all, no registration required — includes zazen instruction at 8:15am, "
            "sitting meditation at 9:30am, and a public Dharma talk at 10am (in-person and "
            "livestreamed via Online Zendo). Daily zazen at 6am and 7:50pm most days "
            "(no Tuesday schedule). One of the most beautiful and accessible Zen centers "
            "in the Bay Area."
        ),
    },
    "shambhala_sf": {
        "id": "shambhala_sf",
        "name": "San Francisco Shambhala Center",
        "tradition": "tibetan",
        "url": "https://sf.shambhala.org",
        "address": "280 Claremont St",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94127",
        "neighborhood": "Glen Park",
        "lat": 37.7315,
        "lng": -122.4296,
        "description": (
            "San Francisco Shambhala Center offers meditation programs rooted in "
            "the Shambhala Buddhist tradition (Tibetan Vajrayana lineage of Chögyam "
            "Trungpa Rinpoche). Located in the Glen Park neighborhood. Open to all "
            "— no experience necessary. Regular programs include biweekly Beginners "
            "Night (2nd & 4th Wednesdays), monthly Saturday Morning Meditation "
            "(3rd Saturday), and online Sunday Morning Meditation (1st & 2nd Sundays)."
        ),
    },
    "sf_buddhist_center": {
        "id": "sf_buddhist_center",
        "name": "San Francisco Buddhist Center",
        "tradition": "pluralist",
        "url": "https://www.sfbuddhistcenter.org",
        "address": "37 Belcher St",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94114",
        "neighborhood": "Castro / Duboce Triangle",
        "lat": 37.7649,
        "lng": -122.4327,
        "description": (
            "San Francisco Buddhist Center is part of the Triratna Buddhist Community "
            "(formerly FWBO), an international network emphasizing meditation, "
            "friendship, and ethical engagement. Located in the Castro / Duboce "
            "Triangle neighborhood. Offers weekly sits, courses, and community events "
            "open to all regardless of experience."
        ),
    },
    # ---- NYC Phase 3a centers ----
    "nyimc": {
        "id": "nyimc",
        "name": "New York Insight Meditation Center",
        "tradition": "theravada",
        "url": "https://www.nyimc.org",
        "address": "115 West 29th Street, 12th Floor",
        "city": "Manhattan",
        "state": "NY",
        "zip": "10001",
        "neighborhood": "Midtown South",
        "lat": 40.7473,
        "lng": -73.9932,
        "description": (
            "New York Insight Meditation Center (NYIMC) offers meditation in the Theravada "
            "and secular mindfulness traditions. Founded in 1997, NYIMC provides a space "
            "for regular sitting groups, teacher-led retreats, and MBSR courses in Midtown "
            "Manhattan. Weekly programs include the Thursday Community Sit (co-presented "
            "with Tibet House US) and the Wednesday Community Meditation Gathering. "
            "Open to practitioners of all levels."
        ),
    },
    "brooklyn_zen_center": {
        "id": "brooklyn_zen_center",
        "name": "Brooklyn Zen Center",
        "tradition": "zen",
        "url": "https://brooklynzen.org",
        "address": "326 Clinton St",
        "city": "Brooklyn",
        "state": "NY",
        "zip": "11231",
        "neighborhood": "Carroll Gardens",
        "lat": 40.6820,
        "lng": -73.9984,
        "description": (
            "Brooklyn Zen Center practices Soto Zen with a commitment to social engagement "
            "and accessibility. Their Boundless Mind Temple in Carroll Gardens hosts weekly "
            "Wednesday Dharma Shares and Saturday Morning Programs. Daily online morning "
            "meditation (Mon–Fri 7:30am ET) is open to all. The center emphasizes "
            "progressive values and welcomes practitioners from all backgrounds."
        ),
    },
    "kadampa_nyc": {
        "id": "kadampa_nyc",
        "name": "Kadampa Meditation Center New York",
        "tradition": "tibetan",
        "url": "https://meditationinnewyork.org",
        "address": "127 W 24th St",
        "city": "Manhattan",
        "state": "NY",
        "zip": "10011",
        "neighborhood": "Chelsea",
        "lat": 40.7455,
        "lng": -73.9960,
        "description": (
            "Kadampa Meditation Center New York (Chelsea location) offers over 30 drop-in "
            "meditation classes per week in the New Kadampa Tradition (NKT-IKBU), a "
            "contemporary Tibetan Buddhist tradition emphasizing practical application of "
            "Buddha's teachings in daily life. Classes include guided meditation, "
            "breathing meditation, and Dharma teachings. All levels welcome."
        ),
    },
    # ---- NYC Phase 3b centers ----
    "shambhala_nyc": {
        "id": "shambhala_nyc",
        "name": "Shambhala Meditation Center of New York",
        "tradition": "tibetan",
        "url": "https://ny.shambhala.org",
        "address": "151 W 30th St, 3rd Floor",
        "city": "Manhattan",
        "state": "NY",
        "zip": "10001",
        "neighborhood": "Midtown South",
        "lat": 40.7476,
        "lng": -73.9935,
        "description": (
            "Shambhala Meditation Center of New York is one of the primary centers of the "
            "Shambhala Buddhist tradition, founded by Chögyam Trungpa Rinpoche. Located in "
            "Midtown South, the center offers in-person Tuesday evening meditation (1st and 3rd "
            "Tuesdays 7:15pm), Sunday Dharma Gatherings (2nd Sunday monthly), a Virtual Healing "
            "Circle (last Saturday monthly), and online Learn to Meditate classes. The Shambhala "
            "tradition emphasizes basic goodness, the path of the bodhisattva warrior, and the "
            "integration of meditation into everyday life."
        ),
    },
    "nyzccc": {
        "id": "nyzccc",
        "name": "NY Zen Center for Contemplative Care",
        "tradition": "zen",
        "url": "https://zencare.org",
        "address": "119 W 23rd St, 4th Floor",
        "city": "Manhattan",
        "state": "NY",
        "zip": "10011",
        "neighborhood": "Chelsea",
        "lat": 40.7435,
        "lng": -73.9949,
        "description": (
            "The NY Zen Center for Contemplative Care (NYZCCC) is a Soto Zen center "
            "dedicated to integrating Buddhist practice with compassionate care in healthcare "
            "settings. NYZCCC trains chaplains, hospice workers, and caregivers in "
            "contemplative approaches. Their practice schedule includes Mid-Day Zazen "
            "Mon–Sat 12:30pm (online), Sunday services with zazen at 10am and dharma talk "
            "at 11:30am (in-person + online), and Monday and Wednesday evening sits at 6pm. "
            "Open to practitioners of all levels."
        ),
    },
    "tibet_house_us": {
        "id": "tibet_house_us",
        "name": "Tibet House US",
        "tradition": "tibetan",
        "url": "https://thus.org",
        "address": "22 W 15th St",
        "city": "Manhattan",
        "state": "NY",
        "zip": "10011",
        "neighborhood": "Chelsea / Flatiron",
        "lat": 40.7382,
        "lng": -73.9972,
        "description": (
            "Tibet House US is the cultural center of His Holiness the Dalai Lama in America, "
            "dedicated to preserving Tibetan civilization and making its wisdom accessible to "
            "the world. In addition to cultural exhibitions and lectures, Tibet House offers "
            "a free Lunchtime Meditation series Mon–Fri 1:00–1:45pm ET (online), led by "
            "rotating teachers from Buddhist and contemplative traditions. Ticketed special "
            "events include teachings, film screenings, and public programs."
        ),
    },
    # ---- NYC Phase 3c centers ----
    "zenstudies_nyc": {
        "id": "zenstudies_nyc",
        "name": "New York Zendo Shobo-Ji",
        "tradition": "zen",
        "url": "https://zenstudies.org/new-york-zendo/",
        "address": "223 E 67th St",
        "city": "Manhattan",
        "state": "NY",
        "zip": "10065",
        "neighborhood": "Upper East Side",
        "lat": 40.7657,
        "lng": -73.9600,
        "description": (
            "New York Zendo Shobo-Ji is one of the oldest Rinzai Zen centers in the Western "
            "hemisphere, founded by Eido Roshi in 1968 and part of the Zen Studies Society. "
            "The zendo on the Upper East Side offers daily Morning Zazen (Mon–Thu 6:45–7:45am), "
            "Evening Zazen (Mon/Tue/Wed 7:00–9:00pm), and Sunday Morning Service with zazen at 10am. "
            "Monthly sesshins (intensive retreat periods), Introduction to Zen Meditation classes "
            "on Thursdays, and online programs are also available. The Zen Studies Society also "
            "operates Dai Bosatsu Zendo Kongo-ji, a mountain monastery in the Catskills."
        ),
    },
    "zcnyc": {
        "id": "zcnyc",
        "name": "Zen Center of New York City (Fire Lotus Temple)",
        "tradition": "zen",
        "url": "https://zcnyc.org",
        "address": "500 State St",
        "city": "Brooklyn",
        "state": "NY",
        "zip": "11217",
        "neighborhood": "Boerum Hill",
        "lat": 40.6824,
        "lng": -73.9887,
        "description": (
            "The Zen Center of New York City, also known as Fire Lotus Temple, is a Soto Zen "
            "training center in Boerum Hill, Brooklyn, part of the Mountains and Rivers Order "
            "founded by John Daido Loori Roshi. Practice includes a Sunday Morning Program "
            "(9:30am–12:30pm with zazen, dharma talk, and beginning instruction), daily zazen, "
            "and monthly half-day sits. ZCNYC is committed to inclusive practice and offers "
            "dedicated programs including an LGBTQIA+ Sitting Group (1st and 3rd Tuesdays 6pm, "
            "Zoom) and a TGNC Practice Night (2nd Thursdays 6:30pm, in-person)."
        ),
    },
    "norcal_sangha": {
        "id": "norcal_sangha",
        "name": "NorCal Sangha Community",
        "tradition": "pluralist",
        "url": "https://norcalsangha.org",
        "address": "Bay Area (multiple venues)",
        "city": "Oakland",
        "state": "CA",
        "zip": "94612",
        "neighborhood": "Bay Area",
        "lat": 37.8076,
        "lng": -122.2697,
        "description": (
            "NorCal Sangha Community is the Northern California regional hub for "
            "Plum Village sanghas in the tradition of Thich Nhat Hanh and the Order "
            "of Interbeing. They organize monthly Days of Mindfulness — full-day "
            "retreats in mindfulness practice — and special events at venues across "
            "the Bay Area, frequently co-hosted with East Bay Meditation Center "
            "(EBMC) and Shantideva Monastery in Castro Valley. They also maintain "
            "a directory of local weekly Plum Village sitting groups throughout "
            "Northern California."
        ),
    },
    # -----------------------------------------------------------------------
    # Los Angeles — Phase 3
    # -----------------------------------------------------------------------
    "insightla": {
        "id": "insightla",
        "name": "InsightLA",
        "tradition": "theravada",
        "url": "https://insightla.org",
        "address": "1430 Olympic Blvd",
        "city": "Santa Monica",
        "state": "CA",
        "zip": "90404",
        "neighborhood": "Mid-City Santa Monica",
        "lat": 34.0230,
        "lng": -118.4807,
        "description": (
            "InsightLA is a leading Insight Meditation center in Los Angeles, "
            "founded by Trudy Goodman. Rooted in the Theravada Vipassana tradition "
            "and affiliated with IMS and Spirit Rock, InsightLA offers weekly community "
            "sits, dharma nights, MBSR and Mindful Self-Compassion programs, and "
            "residential retreats. Classes welcome beginners and experienced practitioners "
            "alike, in person at the Santa Monica center and online via Zoom."
        ),
    },
    "zcla": {
        "id": "zcla",
        "name": "Zen Center of Los Angeles",
        "tradition": "zen",
        "url": "https://zcla.org",
        "address": "923 S. Mariposa Ave",
        "city": "Los Angeles",
        "state": "CA",
        "zip": "90006",
        "neighborhood": "Koreatown",
        "lat": 34.0546,
        "lng": -118.3012,
        "description": (
            "ZCLA is one of the oldest and most established Zen centers in North America, "
            "founded by Taizan Maezumi Roshi in 1967. Part of the White Plum Asanga lineage "
            "(Soto/Rinzai fusion), ZCLA offers daily zazen, sesshins, dharma study groups, "
            "and Intro to Zen classes in its Koreatown residential zendo. A landmark in "
            "American Zen — many of today's prominent Zen teachers trained here."
        ),
    },
}
