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
    "shambhala_la": {
        "id": "shambhala_la",
        "name": "Shambhala Meditation Center of Los Angeles",
        "tradition": "tibetan",
        "url": "https://la.shambhala.org",
        "address": "3580 W 1st St",
        "city": "Los Angeles",
        "state": "CA",
        "zip": "90004",
        "neighborhood": "Koreatown / Westlake",
        "lat": 34.0693,
        "lng": -118.2979,
        "description": (
            "Shambhala Meditation Center of Los Angeles offers sitting meditation and "
            "programs in the Shambhala Buddhist tradition (Tibetan Vajrayana lineage of "
            "Chögyam Trungpa Rinpoche). Located in Koreatown/Westlake. Drop-in sitting "
            "meditation, Shambhala Training weekends, and dharma talks open to all "
            "— no experience required."
        ),
    },
    # ── Boston / Cambridge ────────────────────────────────────────────────────
    "shambhala_boston": {
        "id": "shambhala_boston",
        "name": "Boston Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://boston.shambhala.org",
        "address": "646 Brookline Ave",
        "city": "Brookline",
        "state": "MA",
        "zip": "02445",
        "neighborhood": "Brookline Village",
        "lat": 42.3435,
        "lng": -71.1286,
        "description": (
            "Boston Shambhala Meditation Center offers a welcoming home for Shambhala Buddhist "
            "practice (Chögyam Trungpa lineage) in the Greater Boston area. Regular offerings include "
            "Nyinthün Sunday morning meditation 9am–12pm, Wednesday Open Dharma Gathering 7–8:30pm, "
            "Heart of Recovery (Mondays), and LGBTQ+ Meditation Group 1st/3rd Tuesdays. "
            "The center also hosts Shambhala Training weekends, family practice days, and "
            "monthly Sangha Sundays. Beginners always welcome, first visit free."
        ),
    },
    "gbzc": {
        "id": "gbzc",
        "name": "Greater Boston Zen Center",
        "tradition": "zen",
        "url": "https://bostonzen.org",
        "address": "552 Massachusetts Ave, Suite 208",
        "city": "Cambridge",
        "state": "MA",
        "zip": "02139",
        "neighborhood": "Central Square",
        "lat": 42.3638,
        "lng": -71.1059,
        "description": (
            "Greater Boston Zen Center (GBZC) is a non-residential urban Zen community in Cambridge's "
            "Central Square, serving the Boston metro area since the 1990s. Teachers include Josh Bartok, "
            "Kate Hartland, and others trained in multiple Zen lineages. Weekly offerings include "
            "Tuesday Evening Program 7–9pm (hybrid in-person + Zoom) and Saturday Morning Program "
            "9–9:50am (online). Monthly all-day zazenkai sits for deepening practice. Dana-based."
        ),
    },
    "cimc": {
        "id": "cimc",
        "name": "Cambridge Insight Meditation Center",
        "tradition": "theravada",
        "url": "https://cambridgeinsight.org",
        "address": "331 Broadway",
        "city": "Cambridge",
        "state": "MA",
        "zip": "02139",
        "neighborhood": "MIT/Cambridgeport",
        "lat": 42.3652,
        "lng": -71.1107,
        "description": (
            "Cambridge Insight Meditation Center (CIMC) is one of the most respected urban Vipassana "
            "centers in North America. Founded by Larry Rosenberg, CIMC is rooted in the Theravada "
            "tradition and closely affiliated with the Insight Meditation Society (IMS) in Barre and "
            "Spirit Rock in Marin. Regular drop-in sits run Mon/Tue/Thu/Fri evenings at 6pm, with "
            "Monday Sitting & Sangha 6–7:15pm, Wednesday Evening Dharma 6:30–8:45pm, and Thursday "
            "Morning Retreat 9am–1pm. All events by donation. Deep practice in the heart of Cambridge."
        ),
    },
    "cambridge_zen": {
        "id": "cambridge_zen",
        "name": "Cambridge Zen Center",
        "tradition": "zen",
        "url": "https://cambridgezen.org",
        "address": "199 Auburn St",
        "city": "Cambridge",
        "state": "MA",
        "zip": "02139",
        "neighborhood": "Cambridgeport",
        "lat": 42.3620,
        "lng": -71.1176,
        "description": (
            "Cambridge Zen Center is a residential Zen community practicing in the Kwan Um School "
            "of Zen lineage, founded by Korean Zen Master Seungsahn. One of the oldest Zen centers "
            "in New England, CZC offers a full residential practice schedule and welcomes drop-in "
            "visitors. Regular public sits include Tuesday Evening Zazen 7:30–8:40pm (hybrid), "
            "Thursday Evening 6:45pm instruction + 7:30pm Zoom, and Sunday Morning Zazen 9am "
            "(four 30-min periods, hybrid). Monthly weekend retreats."
        ),
    },
    "kadampa_boston": {
        "id": "kadampa_boston",
        "name": "Kadampa Meditation Center Boston",
        "tradition": "tibetan",
        "url": "https://meditationinboston.org",
        "address": "2298 Massachusetts Ave",
        "city": "Cambridge",
        "state": "MA",
        "zip": "02140",
        "neighborhood": "North Cambridge",
        "lat": 42.3852,
        "lng": -71.1248,
        "description": (
            "Kadampa Meditation Center Boston (KMCB) is part of the New Kadampa Tradition (NKT-IKBU), "
            "an international network of over 1,200 Tibetan Buddhist centers. Located in North "
            "Cambridge, KMCB offers weekly meditation classes (Wednesdays and Sundays), study "
            "programs in the Lamrim and Lojong traditions, and occasional outdoor meditation sessions "
            "at Boston Public Garden. Resident Teacher: Gen Kelsang Khedrub. Drop-in welcome, "
            "beginners especially encouraged."
        ),
    },
    # ── Washington DC Metro ────────────────────────────────────────────────────
    "imcw": {
        "id": "imcw",
        "name": "Insight Meditation Community of Washington",
        "tradition": "theravada",
        "url": "https://imcw.org",
        "address": "276 Carroll St NW",
        "city": "Washington",
        "state": "DC",
        "zip": "20012",
        "neighborhood": "Takoma",
        "lat": 38.9776,
        "lng": -77.0128,
        "description": (
            "IMCW is the largest Insight/Vipassana meditation community in the Washington DC metro area, "
            "co-founded by Tara Brach and Jonathan Foust. Offers drop-in meditation classes at 10+ venues "
            "across DC, Maryland, and Northern Virginia — including Seekers Church (Takoma DC), Iona "
            "(Tenleytown DC), Unity of Washington DC (Logan Circle), River Road UU Church (Bethesda MD), "
            "and Body Grace (Vienna VA). Each class includes 30 minutes of guided meditation, a dharma "
            "talk, and community discussion. Hybrid in-person and Zoom. All welcome, free of charge."
        ),
    },
    "shambhala_dc": {
        "id": "shambhala_dc",
        "name": "Shambhala Meditation Center of Washington DC",
        "tradition": "tibetan",
        "url": "https://dc.shambhala.org",
        "address": "278 Carroll St NW",
        "city": "Washington",
        "state": "DC",
        "zip": "20012",
        "neighborhood": "Takoma",
        "lat": 38.9779,
        "lng": -77.0127,
        "description": (
            "DC Shambhala Center offers Shambhala Buddhist meditation practice "
            "(Chögyam Trungpa lineage), one block from Takoma Metro. Monthly Open Public Sitting "
            "is held the first Sunday of each month, 1:30–2:30pm at Seekers Church (276 Carroll St NW). "
            "Free meditation instruction available before the sit. The center also hosts Shambhala "
            "Training weekends, study groups, and community programs throughout the year."
        ),
    },
    # -----------------------------------------------------------------------
    # Chicago / Illinois — Phase 3
    # -----------------------------------------------------------------------
    "ancient_dragon_chicago": {
        "id": "ancient_dragon_chicago",
        "name": "Ancient Dragon Zen Gate",
        "tradition": "zen",
        "url": "https://www.ancientdragon.org",
        "address": "2255 W Giddings St",
        "city": "Chicago",
        "state": "IL",
        "zip": "60625",
        "neighborhood": "Ravenswood",
        "lat": 41.9680,
        "lng": -87.6840,
        "description": (
            "Soto Zen center in Chicago's Ravenswood neighborhood, affiliated with "
            "San Francisco Zen Center in the lineage of Shunryu Suzuki Roshi. "
            "Sunday morning zazen at 9:30am, Monday evening zazen at The Cenacle "
            "Retreat Center in Lincoln Park. Daily online zazen sessions via Zoom "
            "most weekday mornings. Dharma talks, study groups, and sesshin retreats. "
            "Drop-in welcome. Free of charge."
        ),
    },
    "daiyuzenji_chicago": {
        "id": "daiyuzenji_chicago",
        "name": "Daiyuzenji Rinzai Zen Temple",
        "tradition": "zen",
        "url": "https://daiyuzenji.org",
        "address": "3717 N Ravenswood Ave #112",
        "city": "Chicago",
        "state": "IL",
        "zip": "60613",
        "neighborhood": "Ravenswood",
        "lat": 41.9457,
        "lng": -87.6776,
        "description": (
            "Rinzai Zen temple in Chicago's Ravenswood neighborhood offering traditional "
            "Rinzai practice including zazen, kinhin, and koan work. Hybrid public sittings: "
            "Tuesday and Thursday evenings 7–9pm (two zazen periods), Friday mornings "
            "5:30–6:15am (in-person), Sunday mornings 8:30–10:30am (hybrid, RSVP for Zoom). "
            "Daylong sittings (zazenkai) and week-long sesshins throughout the year."
        ),
    },
    "zbtc_evanston": {
        "id": "zbtc_evanston",
        "name": "Zen Buddhist Temple of Chicago",
        "tradition": "zen",
        "url": "https://www.zbtc.org",
        "address": "608 Dempster St",
        "city": "Evanston",
        "state": "IL",
        "zip": "60202",
        "neighborhood": "Evanston",
        "lat": 42.0451,
        "lng": -87.6905,
        "description": (
            "The oldest continuously operating Zen center in the greater Chicago area, "
            "founded in 1949 by Soyu Matsuoka Roshi — one of the first Japanese Soto Zen "
            "teachers to settle permanently in the United States. Weekly services on Sundays "
            "10am–12pm and 2–4pm, and Wednesdays 7–9pm. In-person at 608 Dempster St in "
            "Evanston, with online attendance available via Zoom."
        ),
    },
    "shambhala_chicago": {
        "id": "shambhala_chicago",
        "name": "Shambhala Meditation Center of Chicago",
        "tradition": "tibetan",
        "url": "https://chicago.shambhala.org",
        "address": "37 N Carpenter St",
        "city": "Chicago",
        "state": "IL",
        "zip": "60607",
        "neighborhood": "West Loop",
        "lat": 41.8826,
        "lng": -87.6524,
        "description": (
            "Shambhala Buddhist meditation center (Chögyam Trungpa lineage) in Chicago's "
            "West Loop. Regular public sittings: Sunday mornings 9:30–11am (sitting, walking, "
            "and dharma discussion), Tuesday evenings 7–8:30pm, and Sunday evenings 5:30–7:30pm "
            "Queer Dharma group. Also online noon meditation on weekdays. Free introductory "
            "meditation instruction available. Shambhala Training weekends and community programs."
        ),
    },
    "cbmg_chicago": {
        "id": "cbmg_chicago",
        "name": "Chicago Buddhist Meditation Group",
        "tradition": "pluralist",
        "url": "https://chicagomeditation.org",
        "address": "4512 N Lincoln Ave",
        "city": "Chicago",
        "state": "IL",
        "zip": "60625",
        "neighborhood": "Ravenswood",
        "lat": 41.9629,
        "lng": -87.6822,
        "description": (
            "Non-sectarian Buddhist meditation community meeting every Sunday at 3:30pm CT "
            "in a hybrid format at 4512 N Lincoln Ave in Ravenswood. Sessions include guided "
            "meditation, dharma talks, and group sharing in an open, ecumenical spirit. "
            "Beginners welcome. Free of charge. Zoom link provided weekly via newsletter."
        ),
    },
    "zen_chicago": {
        "id": "zen_chicago",
        "name": "Chicago Zen Meditation Community",
        "tradition": "zen",
        "url": "https://zenchicago.org",
        "address": "1460 W Chicago Ave",
        "city": "Chicago",
        "state": "IL",
        "zip": "60642",
        "neighborhood": "West Town",
        "lat": 41.8962,
        "lng": -87.6686,
        "description": (
            "Soto Zen meditation center in West Town with one of Chicago's most active "
            "hybrid schedules — approximately 8 sessions per week. Weekday morning zazen "
            "Mon–Sat 8:30am (30 min), Monday afternoon study group 1:15pm, Monday evening "
            "7pm and Wednesday evening zazen, Saturday morning zazen and last-Saturday "
            "zazenkai. Most sessions available via Zoom. Teacher: Myoshi Thomson. Drop-in."
        ),
    },
    "insight_chicago": {
        "id": "insight_chicago",
        "name": "Insight Chicago Meditation Community",
        "tradition": "theravada",
        "url": "https://www.insightchicago.org",
        "address": "",
        "city": "Chicago",
        "state": "IL",
        "zip": "",
        "neighborhood": "Various locations",
        "lat": 41.8781,
        "lng": -87.6298,
        "description": (
            "Insight / Vipassana meditation community with multiple sanghas across the "
            "Chicago metro area, in the IMS / Spirit Rock tradition. Groups include the "
            "Sunday Night Meditation Sangha (in-person/hybrid), Northside Meditation Sangha "
            "(Wednesdays, first week hybrid), Evanston Sangha (Monday and Thursday online), "
            "and the Circle of Stillness (Lake Forest, in-person + Zoom). Regular daylong "
            "retreats with visiting teachers."
        ),
    },
    "kadampa_chicago": {
        "id": "kadampa_chicago",
        "name": "Kadampa Meditation Center Chicago",
        "tradition": "tibetan",
        "url": "https://meditateinchicago.org",
        "address": "1507 E 53rd St",
        "city": "Chicago",
        "state": "IL",
        "zip": "60615",
        "neighborhood": "Hyde Park",
        "lat": 41.7993,
        "lng": -87.5912,
        "description": (
            "Kadampa Meditation Center Chicago (New Kadampa Tradition) in Hyde Park. Offers weekly "
            "drop-in meditation classes, guided meditations, workshops, and retreats based on Geshe "
            "Kelsang Gyatso's modern presentation of Buddhist teachings. Programs for beginners "
            "and experienced practitioners, including the Foundation Program. Events listed on Eventbrite."
        ),
    },
    # ── Seattle / Washington — Phase 3 ────────────────────────────────────────
    "seattle_insight": {
        "id": "seattle_insight",
        "name": "Seattle Insight Meditation Society",
        "tradition": "theravada",
        "url": "https://seattleinsight.org",
        "address": "4001 9th Ave NE",
        "city": "Seattle",
        "state": "WA",
        "zip": "98105",
        "neighborhood": "University District",
        "lat": 47.6568,
        "lng": -122.3142,
        "description": (
            "Seattle Insight Meditation Society (SIMS) is the primary Vipassana / Insight "
            "center in Seattle, offering meditation in the Theravada tradition (IMS / Spirit "
            "Rock lineage). Weekly drop-in programs include Monday Evening Meditation & Dharma, "
            "Stillpoint Sit, Thursday Guided Meditation and Thursday Night Sangha (in-person), "
            "and Sunday Morning Sit & Dharma Talk (hybrid). Identity-centered affinity sanghas "
            "including LGBTQIA+ Sangha. Located in the University District. By donation."
        ),
    },
    "kmc_washington": {
        "id": "kmc_washington",
        "name": "Kadampa Meditation Center Washington",
        "tradition": "tibetan",
        "url": "https://meditateinseattle.org",
        "address": "6556 24th Ave NW",
        "city": "Seattle",
        "state": "WA",
        "zip": "98117",
        "neighborhood": "Crown Hill",
        "lat": 47.6830,
        "lng": -122.3871,
        "description": (
            "Kadampa Meditation Center Washington (KMC Washington) teaches Tibetan Buddhist "
            "meditation in the New Kadampa Tradition (NKT-IKBU) founded by Geshe Kelsang Gyatso. "
            "Located in the Crown Hill neighborhood. Drop-in public classes: Thursday Evening "
            "Meditation 7–8pm, Sunday Morning classes 10–11:15am, Monday Evening classes 7–8:30pm, "
            "and daily morning prostrations. Spanish-language Sunday class also offered. "
            "Beginners especially welcome."
        ),
    },
    "nalandabodhi_seattle": {
        "id": "nalandabodhi_seattle",
        "name": "Nalandabodhi Seattle (Nalanda West)",
        "tradition": "tibetan",
        "url": "https://nalandabodhi.org",
        "address": "3902 Woodland Park Ave N",
        "city": "Seattle",
        "state": "WA",
        "zip": "98103",
        "neighborhood": "Fremont",
        "lat": 47.6574,
        "lng": -122.3363,
        "description": (
            "Nalandabodhi Seattle is based at Nalanda West in Seattle's Fremont neighborhood, "
            "the North American headquarters of Dzogchen Ponlop Rinpoche's international "
            "Nalandabodhi organization. Kagyu/Nyingma Dzogchen lineage. Open public programs "
            "include Thursday Evening Open Meditation 6–7:30pm and Sunday Open Meditation "
            "10–11:30am (both in-person at Nalanda West). Kum Nye (Tibetan Yoga) offered "
            "Tuesdays 5pm. All programs free and open to newcomers."
        ),
    },
    "shambhala_seattle": {
        "id": "shambhala_seattle",
        "name": "Shambhala Meditation Center of Seattle",
        "tradition": "tibetan",
        "url": "https://seattle.shambhala.org",
        "address": "3107 E Harrison St",
        "city": "Seattle",
        "state": "WA",
        "zip": "98112",
        "neighborhood": "Capitol Hill",
        "lat": 47.6197,
        "lng": -122.3023,
        "description": (
            "Shambhala Meditation Center of Seattle offers practice in the Shambhala Buddhist "
            "tradition (Chögyam Trungpa lineage) from their Capitol Hill location. Regular "
            "public programs: Thursday Evening Open House 7–8:30pm (in-person), Sunday Morning "
            "Open House 10–11:30am (in-person), Monday Shambhala Practice Night 6:30pm (online), "
            "and Wednesday Heart of Recovery 7pm (hybrid). Monthly Queer Dharma group. "
            "Free introductory meditation instruction available. All are welcome."
        ),
    },
    "seattle_buddhist_center": {
        "id": "seattle_buddhist_center",
        "name": "Seattle Buddhist Center",
        "tradition": "pluralist",
        "url": "https://seattlebuddhistcenter.org",
        "address": "12056 15th Ave NE, Suite C-2",
        "city": "Seattle",
        "state": "WA",
        "zip": "98125",
        "neighborhood": "Northgate / Pinehurst",
        "lat": 47.7203,
        "lng": -122.3145,
        "description": (
            "Seattle Buddhist Center is part of the Triratna Buddhist Community (formerly FWBO), "
            "an international network that emphasizes meditation, spiritual friendship (kalyana "
            "mitrata), and ethical engagement. Located in the Northgate / Pinehurst area. "
            "Weekly drop-in programs: Thursday Night Meditation 7–8pm (in-person) and Sunday "
            "Sangha Night 6–8pm (in-person). A Buddhist Approach to Recovery meets Fridays 7pm. "
            "Welcoming to all, including beginners and those with no prior Buddhist background."
        ),
    },
    # ── Denver / Boulder — Phase 3 ──────────────────────────────────────────────
    "zen_center_denver": {
        "id": "zen_center_denver",
        "name": "Zen Center of Denver",
        "tradition": "zen",
        "url": "https://zencenterofdenver.org",
        "address": "1856 S Columbine St",
        "city": "Denver",
        "state": "CO",
        "zip": "80210",
        "neighborhood": "Washington Park East",
        "lat": 39.6956,
        "lng": -104.9614,
        "description": (
            "Zen Center of Denver is one of the most active Zen communities in the Rocky Mountain "
            "region, led by resident teacher Peggy Metta Roshi (White Plum Asanga / Soto lineage). "
            "Weekly public sittings: Tuesday morning zazen 6:30am & Tuesday evening 7pm, Thursday "
            "morning zazen 6:30am & Thursday evening 7pm, and Zoom Zen (online zazen daily 6am). "
            "Queer Dharma Meditation monthly, Zen of Recovery, Cha Dao (tea ceremony), Kannon "
            "Ceremony, and Mindfulness Drop-in. Sessions livestreamed on Zoom. Dana-based."
        ),
    },
    "boulder_zen": {
        "id": "boulder_zen",
        "name": "Boulder Zen Center",
        "tradition": "zen",
        "url": "https://www.boulderzen.org",
        "address": "2151 Arapahoe Ave",
        "city": "Boulder",
        "state": "CO",
        "zip": "80302",
        "neighborhood": "Central Boulder",
        "lat": 40.0106,
        "lng": -105.2541,
        "description": (
            "Boulder Zen Center is a Soto Zen practice community in central Boulder near the Pearl "
            "Street Mall, led by Zenki Roshi (White Plum Asanga lineage). Regular public sittings "
            "include weekly zazen, dharma talks, half-day sits, and sesshin intensives. Individual "
            "dokusan (interviews) with the teacher available. Located at 2151 Arapahoe Ave, "
            "walkable from downtown Boulder."
        ),
    },
    "orgyen_khandroling": {
        "id": "orgyen_khandroling",
        "name": "Orgyen Khandroling",
        "tradition": "tibetan",
        "url": "https://orgyenkhandroling.org",
        "address": "3300 Josephine St",
        "city": "Denver",
        "state": "CO",
        "zip": "80205",
        "neighborhood": "Cole / Northeast Denver",
        "lat": 39.7629,
        "lng": -104.9600,
        "description": (
            "Orgyen Khandroling is a Longchen Nyingthig / Dzogchen center in Northeast Denver and "
            "the North American seat of Anyen Rinpoche's international Dharma organization. "
            "The lineage transmits Nyingma Dzogchen teachings from Khenchen Tsewang Rigdzin and "
            "Dilgo Khyentse Rinpoche. Open programs include Wednesday evening and Sunday morning "
            "Open Meditation, Tara Recitation, and Tsok practice on auspicious lunar days. "
            "No prior Buddhist knowledge required. Located in the Cole neighborhood."
        ),
    },
    "shambhala_boulder": {
        "id": "shambhala_boulder",
        "name": "Boulder Shambhala Center",
        "tradition": "tibetan",
        "url": "https://boulder.shambhala.org",
        "address": "1345 Spruce St",
        "city": "Boulder",
        "state": "CO",
        "zip": "80302",
        "neighborhood": "Central Boulder",
        "lat": 40.0150,
        "lng": -105.2705,
        "description": (
            "Boulder Shambhala Center teaches meditation in the Shambhala Buddhist tradition "
            "(Chögyam Trungpa lineage) from their central Boulder location near Pearl Street. "
            "Regular public program: Thursday Night Open Class 7–8:45pm (in-person, all welcome). "
            "Free introductory meditation instruction available at any Open Class. Generosity "
            "policy applies — no one turned away for lack of funds."
        ),
    },
    "shambhala_denver": {
        "id": "shambhala_denver",
        "name": "Shambhala Meditation Center of Denver",
        "tradition": "tibetan",
        "url": "https://denver.shambhala.org",
        "address": "2305 S Syracuse Way, Suite 214",
        "city": "Denver",
        "state": "CO",
        "zip": "80231",
        "neighborhood": "Hampden South / Tamarac Square",
        "lat": 39.6519,
        "lng": -104.8822,
        "description": (
            "Shambhala Meditation Center of Denver teaches in the Shambhala Buddhist tradition "
            "(Chögyam Trungpa lineage) from their southeast Denver location. Weekly drop-in: "
            "Sunday morning group meditation at 10:00 AM (in-person). Open House and Meditation "
            "Instruction monthly — typically the 4th Sunday at 10am, free of charge, followed "
            "by CommuniTea at noon. Additional programs: Heart of Recovery sangha, "
            "Death and Dying study group."
        ),
    },
    "dharma_rain": {
        "id": "dharma_rain",
        "name": "Dharma Rain Zen Center",
        "tradition": "zen",
        "url": "https://dharma-rain.org",
        "address": "8500 NE Siskiyou St",
        "city": "Portland",
        "state": "OR",
        "zip": "97220",
        "neighborhood": "Roseway / Northeast Portland",
        "lat": 45.5508,
        "lng": -122.5946,
        "description": (
            "Dharma Rain Zen Center is the oldest and largest Soto Zen temple in Oregon, founded "
            "in 1975. Located in the Roseway neighborhood of Northeast Portland, the center has "
            "two buildings (Sodo and Uji) and offers a full monastic and lay practice schedule. "
            "Regular public programs include Wednesday Evening Meditation 7–9pm (zazen, chanting, "
            "open Buddhism class; free, donations welcome) and Sunday Morning Program 8:30–11:30am "
            "(two zazen periods, chanting service, Dharma talk). Early morning zazen Wed–Sat "
            "6:30am. Sesshin, zazenkai, dokusan, and MBSR also offered. Drop-in welcome."
        ),
    },
    "kagyu_changchub_chuling": {
        "id": "kagyu_changchub_chuling",
        "name": "Kagyu Changchub Chuling",
        "tradition": "tibetan",
        "url": "https://kcc.org",
        "address": "4936 NE Skidmore St",
        "city": "Portland",
        "state": "OR",
        "zip": "97218",
        "neighborhood": "Beaumont-Wilshire / Northeast Portland",
        "lat": 45.5579,
        "lng": -122.6134,
        "description": (
            "Kagyu Changchub Chuling (KCC) is one of the oldest Tibetan Buddhist centers in the "
            "Pacific Northwest, a Karma Kagyu center in Northeast Portland led by Lama Eric "
            "Yankovitch. Regular public programs: Sunday Shamatha Meditation 9–11am (in-person) "
            "and 6:30–8pm (hybrid), Wednesday Chenrezi Practice 7–8pm (hybrid), Thursday Silent "
            "Sit 11am–12pm (in-person), and Daily Morning Meditation 7–7:45am (online). "
            "Tibetan language classes, Dharma study, and retreat programs also offered. "
            "Located in the Beaumont-Wilshire neighborhood of Northeast Portland."
        ),
    },
    "portland_insight": {
        "id": "portland_insight",
        "name": "Portland Insight Meditation Community",
        "tradition": "theravada",
        "url": "https://www.portlandinsight.org",
        "address": "6536 SE Duke St",
        "city": "Portland",
        "state": "OR",
        "zip": "97206",
        "neighborhood": "Brentwood-Darlington / Southeast Portland",
        "lat": 45.4738,
        "lng": -122.6186,
        "description": (
            "Portland Insight Meditation Community (PIMC) teaches Vipassana meditation in the "
            "Theravada tradition, in the lineage of Ruth Denison. Weekly programs include Sunday "
            "morning meditation and Dharma talk (in-person + Zoom), Monday morning sit with poem "
            "and group discussion, Tuesday Evening Sangha 6:30–8pm (in-person), and Wednesday "
            "evening Heart of Freedom class (guided meditation, compassion and wisdom teachings, "
            "Q&A). Open to all levels; drop-in welcome. Located in Brentwood-Darlington, "
            "Southeast Portland."
        ),
    },
    "shambhala_portland": {
        "id": "shambhala_portland",
        "name": "Portland Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://portland.shambhala.org",
        "address": "1404 SE 25th Ave",
        "city": "Portland",
        "state": "OR",
        "zip": "97214",
        "neighborhood": "Buckman / Richmond, Southeast Portland",
        "lat": 45.5168,
        "lng": -122.6434,
        "description": (
            "Portland Shambhala Meditation Center offers meditation in the Shambhala Buddhist "
            "tradition (Chögyam Trungpa lineage) from their Southeast Portland location near "
            "the Hawthorne district. Regular in-person programs: Monday and Friday evening "
            "'Decompress + Connect' meditation group at 1404 SE 25th Ave (shared space with "
            "Portland Friends of the Dhamma). Online programs: Monday morning meditation, "
            "Tuesday evening open house, Friday morning meditation, Sunday community meditation. "
            "Monthly Laurelhurst Park sit — 3rd Sunday 10–11:30am (outdoor, weather permitting). "
            "Free introductory meditation instruction available."
        ),
    },

    # ── Austin, TX ────────────────────────────────────────────────────────────
    "kadampa_austin": {
        "id": "kadampa_austin",
        "name": "Kadampa Meditation Center Austin",
        "tradition": "tibetan",
        "url": "https://meditationinaustin.org",
        "address": "7101 Easy Wind Drive, Unit 3108",
        "city": "Austin",
        "state": "TX",
        "zip": "78752",
        "neighborhood": "North Austin / Rundberg",
        "lat": 30.3785,
        "lng": -97.7115,
        "description": (
            "Kadampa Meditation Center Austin (KMC Austin) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), offering classes and programs rooted in "
            "Je Tsongkhapa's teachings as presented by Venerable Geshe Kelsang Gyatso. "
            "Located at Vessel Offsite in North Austin, with a satellite branch at Georgetown "
            "Public Library (402 W 8th St, Georgetown, TX 78626). Regular programs include "
            "Heart Jewel, Wishfulfilling Jewel with Tsog, Foundation Program, and Sunday "
            "General Program. Weekend empowerments and day courses offered throughout the year. "
            "All are welcome; no prior experience necessary."
        ),
    },
    "austin_zen": {
        "id": "austin_zen",
        "name": "Austin Zen Center",
        "tradition": "zen",
        "url": "https://austinzencenter.org",
        "address": "3014 Washington Square",
        "city": "Austin",
        "state": "TX",
        "zip": "78705",
        "neighborhood": "Hyde Park / Central Austin",
        "lat": 30.3073,
        "lng": -97.7421,
        "description": (
            "Austin Zen Center (AZC) is a Soto Zen Buddhist temple in the lineage of Shunryu "
            "Suzuki Roshi and the San Francisco Zen Center, located in Hyde Park, Central Austin. "
            "Offers a full monastic and lay practice schedule: Morning Program (6am zazen + kinhin "
            "+ service, Tue–Fri), Midday Sit (12pm informal zazen, Tue–Thu), Evening Program "
            "(5:40pm zazen + service, Tue–Thu), and Saturday Program (8am beginner instruction + "
            "informal zazen, 9:15am zazen, 10:15am Dharma talk). Drop-in welcome; online "
            "participation available for many programs. 'Our intention is to help all beings "
            "realize their true nature.'"
        ),
    },
    # ── Minneapolis / Saint Paul — Phase 3 ───────────────────────────────────
    "common_ground": {
        "id": "common_ground",
        "name": "Common Ground Meditation Center",
        "tradition": "theravada",
        "url": "https://commongroundmeditation.org",
        "address": "2700 East 26th Street",
        "city": "Minneapolis",
        "state": "MN",
        "zip": "55406",
        "neighborhood": "Seward / Longfellow",
        "lat": 44.9620,
        "lng": -93.2305,
        "description": (
            "Common Ground Meditation Center is Minneapolis's home of Insight / Vipassana "
            "meditation in the IMS / Spirit Rock tradition. Located at 2700 East 26th Street in "
            "the Seward neighborhood. Senior teachers Mark Nunberg and Shelly Graf lead a rich "
            "calendar: daily Open Meditation (7am, various teachers), weekly sitting groups, "
            "community groups (BIPOC, LGBTQ+, recovery, young adults), half-day and residential "
            "retreats, and beginner courses. Free and by-donation options available. "
            "Welcoming practice home for all."
        ),
    },
    "mn_zen": {
        "id": "mn_zen",
        "name": "Minnesota Zen Meditation Center",
        "tradition": "zen",
        "url": "https://mnzencenter.org",
        "address": "3343 East Bde Maka Ska Pkwy",
        "city": "Minneapolis",
        "state": "MN",
        "zip": "55408",
        "neighborhood": "Lakewood / Bde Maka Ska",
        "lat": 44.9434,
        "lng": -93.3173,
        "description": (
            "Minnesota Zen Meditation Center (MZMC) is a Soto Zen center founded in 1972 in "
            "the Dainin Katagiri Roshi lineage, on the west shore of Bde Maka Ska (Lake Calhoun). "
            "One of the oldest and most established Zen centers in the Midwest. Resident teacher: "
            "Myo Denis Lahey. Daily zazen: Mon–Fri 6:30am, Sat–Sun 7:30am; evening zazen "
            "Mon–Thu 5:30pm, Fri 6pm. Wednesday dharma talks 7:30pm. Sunday Morning Program "
            "9:30am (zazen + service + dharma talk). Sesshin and workshops offered."
        ),
    },
    "clouds_in_water": {
        "id": "clouds_in_water",
        "name": "Clouds in Water Zen Center",
        "tradition": "zen",
        "url": "https://cloudsinwater.org",
        "address": "308 Prince St",
        "city": "Saint Paul",
        "state": "MN",
        "zip": "55107",
        "neighborhood": "Lowertown / Saint Paul",
        "lat": 44.9397,
        "lng": -93.0961,
        "description": (
            "Clouds in Water Zen Center is a Soto Zen center in historic Lowertown, Saint Paul. "
            "Teacher emerita Roshi Diane Musho Hamilton; current abbot Dokai Georgesen. "
            "Morning zazen Mon–Fri 7–8:30am (in-person + Zoom available some days). "
            "Sunday morning 9:30am zazen + dharma talk. Sesshin, workshops, and retreats. "
            "Drop-in welcome; online practice community."
        ),
    },
    "shambhala_minneapolis": {
        "id": "shambhala_minneapolis",
        "name": "Shambhala Meditation Center of Minneapolis",
        "tradition": "tibetan",
        "url": "https://minneapolis.shambhala.org",
        "address": "1544 Nicollet Ave",
        "city": "Minneapolis",
        "state": "MN",
        "zip": "55403",
        "neighborhood": "Whittier",
        "lat": 44.9657,
        "lng": -93.2896,
        "description": (
            "Shambhala Meditation Center of Minneapolis (Chögyam Trungpa lineage) in the "
            "Whittier neighborhood. Offers Shambhala Training weekends, weekly community "
            "meditation, and open houses. The Shambhala path cultivates basic goodness and "
            "fearless presence in daily life."
        ),
    },
    "kadampa_phoenix": {
        "id": "kadampa_phoenix",
        "name": "Kadampa Meditation Center Phoenix",
        "tradition": "tibetan",
        "url": "https://www.meditationinarizona.org",
        "address": "614 East Townley Ave",
        "city": "Phoenix",
        "state": "AZ",
        "zip": "85020",
        "neighborhood": "Sunnyslope / North Phoenix",
        "lat": 33.5731,
        "lng": -112.0539,
        "description": (
            "Kadampa Meditation Center Phoenix (KMC Phoenix) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located in the Sunnyslope neighborhood of "
            "North Phoenix. Offers regular General Program meditation classes open to all: "
            "Sunday morning, Monday evening, and Wednesday evening at the main Phoenix location, "
            "plus satellite sits in Scottsdale, Surprise, Fountain Hills, and Mesa. "
            "No experience necessary; all are welcome. KMC Phoenix also operates Tucson KMC AZ "
            "and the Williams World Peace Temple retreat center in northern Arizona."
        ),
    },
    "houston_zen": {
        "id": "houston_zen",
        "name": "Houston Zen Center",
        "tradition": "zen",
        "url": "https://houstonzen.org",
        "address": "1605 Heights Blvd",
        "city": "Houston",
        "state": "TX",
        "zip": "77008",
        "neighborhood": "The Heights",
        "lat": 29.8004,
        "lng": -95.3984,
        "description": (
            "Houston Zen Center (HZC) is a Soto Zen community in the historic Heights "
            "neighborhood, offering one of the most active daily practice schedules in Texas. "
            "Morning zazen (Mon–Thu at 5:50am and 6:40am, Saturday at 8:20am) and evening "
            "zazen (Mon–Thu at 5:30pm) are open to all, both in-person and via Zoom Zendo. "
            "The full Sunday program (8:20am–noon) includes chanting, zazen, a newcomer's "
            "orientation, and a weekly dharma talk by Abbot Gaelyn Godwin or guest teachers. "
            "Introduction to Zen meditation courses, identity-focused groups (Queer Dharma, "
            "Zen en Español), a recovery sangha, and retreats at the affiliated Auspicious "
            "Cloud Zen Retreat Center are offered throughout the year. Free; all welcome."
        ),
    },
    "chung_tai_houston": {
        "id": "chung_tai_houston",
        "name": "Chung Tai Zen Center of Houston",
        "tradition": "zen",
        "url": "https://cthouston.org",
        "address": "12129 Bellaire Blvd",
        "city": "Houston",
        "state": "TX",
        "zip": "77072",
        "neighborhood": "Westchase / Bellaire",
        "lat": 29.7122,
        "lng": -95.5832,
        "description": (
            "Chung Tai Zen Center of Houston (普德精舍) is a Chan (Zen) Buddhist center "
            "affiliated with Chung Tai Chan Monastery in Taiwan. Located in the Bellaire/Westchase "
            "area of southwest Houston. Offers structured meditation programs at multiple skill "
            "levels: Level 1 (Beginner) on Monday evenings 7:30pm and Saturday mornings 10am; "
            "Level 2 (Intermediate) and Level 3 (Advanced) on Wednesday evenings 7:30pm; "
            "Sutra Study on Thursday evenings 7pm; Youth and Children's Meditation on Saturday "
            "afternoons 4:30pm. Monthly half-day retreats. All are welcome; no experience needed."
        ),
    },
    "dawn_mountain_houston": {
        "id": "dawn_mountain_houston",
        "name": "Dawn Mountain Center for Tibetan Buddhism",
        "tradition": "tibetan",
        "url": "https://dawnmountain.org",
        "address": "4803 San Felipe St",
        "city": "Houston",
        "state": "TX",
        "zip": "77056",
        "neighborhood": "Galleria / Uptown",
        "lat": 29.7562,
        "lng": -95.4643,
        "description": (
            "Dawn Mountain Center for Tibetan Buddhism is an ecumenical Tibetan Buddhist center "
            "in Houston's Galleria area, founded in 1996 by Anne C. Klein (Rigzin Drolma) and "
            "Harvey B. Aronson. One of the few Tibetan Buddhist centers in the US that bridges "
            "academic Buddhist studies and contemplative practice. Offers free Sunday guided "
            "meditations, Teaching Tuesdays, weekend retreats, and in-depth Dzogchen and Ngondro "
            "study programs. Open to all levels."
        ),
    },
    "insight_meditation_houston": {
        "id": "insight_meditation_houston",
        "name": "Insight Meditation Houston",
        "tradition": "theravada",
        "url": "https://insighthouston.org",
        "address": "4949 Caroline St",
        "city": "Houston",
        "state": "TX",
        "zip": "77004",
        "neighborhood": "Museum District / Midtown",
        "lat": 29.7268,
        "lng": -95.3836,
        "description": (
            "Insight Meditation Houston (IMH) teaches in the Theravada Vipassana / Insight "
            "Meditation tradition (Spirit Rock / IMS lineage). Weekly Monday evening sits "
            "(7–8:30pm) with meditation and dharma talk at Covenant Church, Building B "
            "(Huff Fellowship Hall), 4949 Caroline St, Museum District. Also available via "
            "Zoom. Free; donations welcome. Annual 2-day 'Deepening the Dharma' retreat. "
            "Sits are held most Mondays except federal holidays."
        ),
    },
    "diamond_way_houston": {
        "id": "diamond_way_houston",
        "name": "Diamond Way Buddhist Center Houston",
        "tradition": "tibetan",
        "url": "https://diamondway.org/houston/",
        "address": "5102 Center St",
        "city": "Houston",
        "state": "TX",
        "zip": "77007",
        "neighborhood": "Heights / Washington Corridor",
        "lat": 29.7653,
        "lng": -95.3987,
        "description": (
            "Diamond Way Buddhist Center Houston is part of the worldwide Diamond Way Buddhist "
            "network (Karma Kagyu lineage, Lama Ole Nydahl). Weekly Wednesday evening program "
            "at 7:30pm — a short Buddhist teaching followed by guided Guru Yoga meditation "
            "(~30 minutes). Free; donations welcome. All are welcome, no experience needed."
        ),
    },
}
