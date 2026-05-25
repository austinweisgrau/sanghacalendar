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
        "lat": 44.9419,
        "lng": -93.3032,
        "description": (
            "Minnesota Zen Meditation Center (MZMC) is a Soto Zen center founded in 1972 in "
            "the Dainin Katagiri Roshi lineage, on the east shore of Bde Maka Ska (Lake Calhoun). "
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
    "kmc_arizona_tucson": {
        "id": "kmc_arizona_tucson",
        "name": "Kadampa Meditation Center Arizona",
        "tradition": "tibetan",
        "url": "https://www.meditationintucson.org",
        "address": "5326 East Pima Street",
        "city": "Tucson",
        "state": "AZ",
        "zip": "85712",
        "neighborhood": "Midtown / East Tucson",
        "lat": 32.2432,
        "lng": -110.8789,
        "description": (
            "Kadampa Meditation Center Arizona (KMC Arizona) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located in Midtown Tucson. Offers weekly "
            "General Program meditation classes open to all: Sunday morning, Tuesday evening, "
            "and a brief Saturday morning drop-in. Classes include guided meditation and "
            "dharma teaching on modern Kadampa Buddhism. No experience necessary; "
            "all are welcome."
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
    "shambhala_albuquerque": {
        "id": "shambhala_albuquerque",
        "name": "Albuquerque Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://albuquerque.shambhala.org",
        "address": "1102 Mountain Rd NW",
        "city": "Albuquerque",
        "state": "NM",
        "zip": "87102",
        "neighborhood": "Old Town / Downtown",
        "lat": 35.0912,
        "lng": -106.6616,
        "description": (
            "Albuquerque Shambhala Meditation Center (ASMC) is a Tibetan Buddhist community "
            "in the Shambhala lineage, located in Albuquerque's historic Old Town/Downtown "
            "corridor. Offers Sunday Public Sitting (in-person and online), Heart of Recovery "
            "programs, Nyinthün (all-day group practice), Shambhala Training weekends, and "
            "dharma study groups. Now also hosts programming from Phoenix Shambhala (closed "
            "Dec 31, 2025). Free and open to all; donations welcome."
        ),
    },
    "upaya_zen_center": {
        "id": "upaya_zen_center",
        "name": "Upaya Zen Center",
        "tradition": "zen",
        "url": "https://www.upaya.org",
        "address": "1404 Cerro Gordo Rd",
        "city": "Santa Fe",
        "state": "NM",
        "zip": "87501",
        "neighborhood": "Canyon Road / Arts District",
        "lat": 35.6870,
        "lng": -105.9393,
        "description": (
            "Upaya Zen Center is one of the most prominent Soto Zen communities in the American "
            "Southwest, founded by Roshi Joan Halifax in 1990 on a five-acre campus in the "
            "foothills of Santa Fe, NM. Daily practice open to visitors: Morning Zazen (7am), "
            "Midday Zazen (~12:20pm), and Evening Zazen (5:30pm) — all in the zendo and often "
            "via Zoom. Weekly Dharma talks, periodic sesshins, and transformative residential "
            "retreats including the renowned Being with Dying professional training. The "
            "Chaplaincy Training Program and Socially Engaged Buddhism initiatives draw "
            "practitioners nationwide. Drop-in welcome; all traditions honored."
        ),
    },
    "drepung_loseling_texas": {
        "id": "drepung_loseling_texas",
        "name": "Drepung Loseling Institute of Texas",
        "tradition": "tibetan",
        "url": "https://www.drepungloselinginstitute.org",
        "address": "11510 S Garden St",
        "city": "Houston",
        "state": "TX",
        "zip": "77071",
        "neighborhood": "Westbury / Southwest Houston",
        "lat": 29.6620,
        "lng": -95.4908,
        "description": (
            "Drepung Loseling Institute of Texas is a Tibetan Buddhist temple and meditation "
            "center in the Westbury area of southwest Houston, affiliated with Drepung Loseling "
            "Monastery in India under the patronage of His Holiness the 14th Dalai Lama "
            "(Gelugpa lineage). Weekly Thursday morning practice sessions (7–9am) and Sunday "
            "programs — morning (10am–noon) and afternoon (3–7pm) — include meditation, dharma "
            "teachings, and traditional Tibetan Buddhist practice. All are welcome; no "
            "experience necessary."
        ),
    },
    "kmc_miami": {
        "id": "kmc_miami",
        "name": "Kadampa Meditation Center Miami",
        "tradition": "tibetan",
        "url": "https://meditationinmiami.org",
        "address": "316 Miracle Mile",
        "city": "Coral Gables",
        "state": "FL",
        "zip": "33134",
        "neighborhood": "Coral Gables / Downtown Miami",
        "lat": 25.7474,
        "lng": -80.2575,
        "description": (
            "Kadampa Meditation Center Miami (KMC Miami) is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located on the famous Miracle Mile shopping "
            "district in Coral Gables, FL. Offers weekly General Program meditation classes "
            "open to all — no experience needed: Sunday 11am, Monday 7:30pm, Tuesday 7:30pm "
            "(Meditación en español), Thursday 7:30pm, and a Friday lunchtime sit (12:15pm). "
            "Monthly Tsog days, empowerments, and special programs. Branch of KMC Florida "
            "(Sarasota). Free to attend; donations welcome."
        ),
    },
    "kmc_fort_lauderdale": {
        "id": "kmc_fort_lauderdale",
        "name": "Kadampa Meditation Center Fort Lauderdale",
        "tradition": "tibetan",
        "url": "https://meditateinfortlauderdale.org",
        "address": "4342 E Tradewinds Ave",
        "city": "Lauderdale-by-the-Sea",
        "state": "FL",
        "zip": "33308",
        "neighborhood": "Fort Lauderdale / Lauderdale-by-the-Sea",
        "lat": 26.1904,
        "lng": -80.0978,
        "description": (
            "Kadampa Meditation Center Fort Lauderdale is a Tibetan Buddhist center in "
            "the New Kadampa Tradition (NKT-IKBU), located in the beach community of "
            "Lauderdale-by-the-Sea (Broward County, ~30 miles north of Miami). Offers weekly "
            "General Program meditation classes: Sundays 11am (90 min), Thursdays 7pm, "
            "and a Wednesday lunchtime sit. Satellite sits in Delray Beach (2nd Wed) and "
            "Hollywood (1st Fri). Monthly Tsog and special programs. Free to attend; "
            "donations welcome."
        ),
    },
    "kmc_san_diego": {
        "id": "kmc_san_diego",
        "name": "Kadampa Meditation Center San Diego",
        "tradition": "tibetan",
        "url": "https://meditateinsandiego.org",
        "address": "3502 Adams Ave",
        "city": "San Diego",
        "state": "CA",
        "zip": "92116",
        "neighborhood": "Normal Heights / North Park",
        "lat": 32.7437,
        "lng": -117.1381,
        "description": (
            "Kadampa Meditation Center San Diego (KMC San Diego) is a Tibetan Buddhist center "
            "in the New Kadampa Tradition (NKT-IKBU), located in the Normal Heights neighborhood "
            "of San Diego. Offers regular General Program meditation classes open to all — no "
            "experience needed: Sunday 10:30am, Monday 6:30pm, and Thursday 6:30pm. Special "
            "events including empowerments, day retreats, and silent retreats are held monthly. "
            "Branch locations in Chula Vista and Oceanside. Free to attend; donations welcome."
        ),
    },
    "shambhala_san_diego": {
        "id": "shambhala_san_diego",
        "name": "San Diego Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://sandiego.shambhala.org",
        "address": "4622 Clairemont Dr",
        "city": "San Diego",
        "state": "CA",
        "zip": "92117",
        "neighborhood": "Clairemont / Bay Park",
        "lat": 32.8030,
        "lng": -117.1978,
        "description": (
            "San Diego Shambhala Meditation Center is a contemplative community in the Shambhala "
            "lineage of Chögyam Trungpa Rinpoche, meeting in a home practice space in the "
            "Clairemont neighborhood of San Diego. Offers a Sunday morning public meditation sit "
            "(10–11am, in-person), bi-weekly Wednesday evening online meditation (7pm via Zoom), "
            "a monthly EcoDharma & EcoSattva training group, and occasional Nyinthün all-day "
            "group practice sessions. Open to all; drop-in welcome."
        ),
    },
    # ── Atlanta, GA ───────────────────────────────────────────────────────────
    "shambhala_atlanta": {
        "id": "shambhala_atlanta",
        "name": "Atlanta Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://atlanta.shambhala.org",
        "address": "1447 Church St",
        "city": "Decatur",
        "state": "GA",
        "zip": "30030",
        "neighborhood": "Decatur / Atlanta metro",
        "lat": 33.7763,
        "lng": -84.2960,
        "description": (
            "Atlanta Shambhala Meditation Center is a contemplative community in the Shambhala "
            "lineage of Chögyam Trungpa Rinpoche, located in a charming bungalow in Decatur "
            "(just east of Atlanta proper). Offers drop-in public meditation on Sundays "
            "(10am–noon), Tuesdays (7–8:30pm), and Fridays (noon–1pm). Also hosts the One "
            "Breath Group, monthly BIPOC Sangha, monthly Queer Dharma group, and Shambhala "
            "Training weekends. Open to all; drop-in welcome."
        ),
    },
    "aszc": {
        "id": "aszc",
        "name": "Atlanta Soto Zen Center",
        "tradition": "zen",
        "url": "https://www.aszc.org",
        "address": "1167 Zonolite Pl NE, Suite C",
        "city": "Atlanta",
        "state": "GA",
        "zip": "30306",
        "neighborhood": "Morningside / Lenox",
        "lat": 33.8060,
        "lng": -84.3420,
        "description": (
            "Atlanta Soto Zen Center (ASZC) is one of Atlanta's longest-running Zen centers, "
            "founded in 1977 in the Soto Zen tradition. Offers daily zazen including a morning "
            "Sunrise Sangha (6am, hybrid in-person + Zoom), Wednesday evening Introduction to "
            "Zen Meditation (7–8:30pm, in-person drop-in), and Sunday Morning Service "
            "(9am–noon, hybrid). Monthly Just Sit Saturdays and Roshi seminars. Located in "
            "Morningside near Piedmont Park. Drop-in welcome."
        ),
    },
    "kmc_georgia": {
        "id": "kmc_georgia",
        "name": "Kadampa Meditation Center Georgia",
        "tradition": "tibetan",
        "url": "https://www.meditationingeorgia.org",
        "address": "741 Edgewood Ave NE",
        "city": "Atlanta",
        "state": "GA",
        "zip": "30307",
        "neighborhood": "Inman Park / Old Fourth Ward",
        "lat": 33.7565,
        "lng": -84.3560,
        "description": (
            "Kadampa Meditation Center Georgia (KMC Georgia) is a Tibetan Buddhist center in the "
            "New Kadampa Tradition (NKT-IKBU), located in the Inman Park neighborhood near the "
            "Atlanta BeltLine. Offers weekly drop-in General Program classes: Sunday 'Advice for "
            "a Happy Life' (10:30–11:45am), Tuesday 'Meditation for Beginners' (7–8pm), and "
            "Wednesday 'Modern Buddhism and Meditation' (7–8:15pm). All sessions include guided "
            "meditation and Buddhist teachings. Drop-in welcome."
        ),
    },
    "red_clay_sangha": {
        "id": "red_clay_sangha",
        "name": "Red Clay Sangha",
        "tradition": "pluralist",
        "url": "https://www.redclaysangha.org",
        "address": "3315 Chamblee Dunwoody Rd",
        "city": "Chamblee",
        "state": "GA",
        "zip": "30341",
        "neighborhood": "Chamblee / Atlanta metro",
        "lat": 33.8895,
        "lng": -84.2984,
        "description": (
            "Red Clay Sangha is a vibrant multi-tradition Buddhist community in Chamblee "
            "(northeast Atlanta metro), drawing from Theravada, Chan/Zen, and Plum Village "
            "(Thich Nhat Hanh) lineages. Weekly events include Sunday Morning Meditation, Talk "
            "and Service (9am, hybrid in-person + Zoom) and the Peach Blossom Sangha's "
            "Mindfulness Practice in the Plum Village Tradition (Sundays 5pm, hybrid). Also "
            "hosts a monthly Insight Dialog Practice Group (3rd Monday 7pm, Zoom), day retreats, "
            "and community events. Drop-in welcome at all sitting sessions."
        ),
    },
    "drepung_loseling_atlanta": {
        "id": "drepung_loseling_atlanta",
        "name": "Drepung Loseling Institute",
        "tradition": "tibetan",
        "url": "https://www.drepung.org",
        "address": "1781 Dresden Dr NE",
        "city": "Atlanta",
        "state": "GA",
        "zip": "30319",
        "neighborhood": "Brookhaven / Lynwood Hills",
        "lat": 33.8505,
        "lng": -84.3247,
        "description": (
            "Drepung Loseling Institute is one of the foremost Tibetan Buddhist institutions in "
            "North America, established in Atlanta in 1988 with the blessing of His Holiness the "
            "Dalai Lama. Home to a community of resident Gelugpa monks, the center is a partner "
            "institution of Emory University's Contemplative Studies program and the Mind & Life "
            "Institute. Open public programs include Sunday 11am Meditation (in-person + "
            "livestream) and a Tuesday 7pm Public Talk series by resident geshe Ngawang Phende "
            "(in-person + livestream). Monthly Tsog ceremonies, retreats, and visiting teacher "
            "programs are also offered."
        ),
    },
    # ── Philadelphia ──────────────────────────────────────────────────────────
    "shambhala_philadelphia": {
        "id": "shambhala_philadelphia",
        "name": "Shambhala Meditation Center of Philadelphia",
        "tradition": "tibetan",
        "url": "https://philadelphia.shambhala.org",
        "address": "2030 Sansom St",
        "city": "Philadelphia",
        "state": "PA",
        "zip": "19103",
        "neighborhood": "Center City West / Rittenhouse Square",
        "lat": 39.9518,
        "lng": -75.1748,
        "description": (
            "Shambhala Meditation Center of Philadelphia is a contemplative community in the "
            "Shambhala lineage of Chögyam Trungpa Rinpoche, located in Center City near "
            "Rittenhouse Square. Offers regular drop-in Sunday Sitting Meditation (10–11am, "
            "first Sunday extended 9:30am–noon) and Thursday Sitting Meditation (6–7pm). "
            "Also hosts Monday Night sangha, Shambhala Training weekends, and dharma study "
            "groups. All are welcome; no experience required."
        ),
    },
    "kadampa_philadelphia": {
        "id": "kadampa_philadelphia",
        "name": "Kadampa Meditation Center Philadelphia",
        "tradition": "tibetan",
        "url": "https://www.meditationinphiladelphia.org",
        "address": "47-49 N 2nd St",
        "city": "Philadelphia",
        "state": "PA",
        "zip": "19106",
        "neighborhood": "Old City",
        "lat": 39.9504,
        "lng": -75.1431,
        "description": (
            "Kadampa Meditation Center Philadelphia (KMC Philadelphia) is a Tibetan Buddhist "
            "center in the New Kadampa Tradition (NKT-IKBU), located in Old City Philadelphia "
            "steps from the Delaware waterfront. One of the most active meditation centers in "
            "the city, with classes nearly every day of the week — Monday, Wednesday, and "
            "Thursday evenings (6:30pm), Tuesday (5pm), Friday mornings (8am), and Sunday "
            "mornings (10:30am). All sessions include guided meditation and Buddhist teachings. "
            "Drop-in fee; free for members. No experience necessary."
        ),
    },
    "zen_center_philadelphia": {
        "id": "zen_center_philadelphia",
        "name": "Zen Center of Philadelphia",
        "tradition": "zen",
        "url": "https://www.zencenterphiladelphia.net",
        "address": "4904 Cedar Ave",
        "city": "Philadelphia",
        "state": "PA",
        "zip": "19143",
        "neighborhood": "Cedar Park / West Philadelphia",
        "lat": 39.9476,
        "lng": -75.2277,
        "description": (
            "Zen Center of Philadelphia (ZCP) is a Zen Buddhist community in the Ordinary "
            "Mind Zen School lineage of Charlotte Joko Beck. Located in the Cedar Park "
            "neighborhood of West Philadelphia. Offers weekly public zazen: Sunday Morning "
            "Program (10am–noon, hybrid in-person + Zoom), Wednesday Evening Sitting "
            "(7–8pm, hybrid), and daily online sits Mon–Fri 7–8am. Monthly sesshin retreats. "
            "Drop-in welcome; sliding scale/donation-based."
        ),
    },
    "chenrezig_philadelphia": {
        "id": "chenrezig_philadelphia",
        "name": "Chenrezig Tibetan Buddhist Center",
        "tradition": "tibetan",
        "url": "https://www.tibetanbuddhist.org",
        "address": "954 N Marshall St",
        "city": "Philadelphia",
        "state": "PA",
        "zip": "19123",
        "neighborhood": "Northern Liberties / Callowhill",
        "lat": 39.9633,
        "lng": -75.1504,
        "description": (
            "Chenrezig Tibetan Buddhist Center of Philadelphia is a non-sectarian Tibetan "
            "Buddhist center founded in 1989 by Lama Losang Samten, a former monk of the "
            "Dalai Lama's Namgyal Monastery. One of the oldest Tibetan Buddhist centers in "
            "Philadelphia. Weekly Sunday Sangha (10–11:30am, hybrid in-person + Zoom, center "
            "opens 9am for self-guided practice) and Thursday Green Tara Puja (7pm, in-person). "
            "Monthly Medicine Buddha and other ceremonial programs. Open to all; drop-in welcome."
        ),
    },
    # ── Las Vegas ─────────────────────────────────────────────────────────────
    "chaiya_las_vegas": {
        "id": "chaiya_las_vegas",
        "name": "Chaiya Meditation Monastery",
        "tradition": "theravada",
        "url": "https://chaiyacmm.org",
        "address": "7925 Virtue Ct",
        "city": "Las Vegas",
        "state": "NV",
        "zip": "89113",
        "lat": 36.0602,
        "lng": -115.2246,
        "neighborhood": "Enterprise / Southwest Las Vegas",
        "bio": (
            "Chaiya Meditation Monastery (CMM) is a Theravada Buddhist monastery in the "
            "Enterprise area of southwest Las Vegas, founded in the Burmese Theravada "
            "tradition. One of the most active Buddhist centers in the Las Vegas valley, "
            "offering four daily meditation sessions open to the public: 9–10 AM, "
            "11 AM–12:15 PM, 2–3 PM, and 5–6:15 PM. All sessions are free and open to "
            "beginners; no experience required. Also available on Zoom (ID: 568 279 3041, "
            "passcode: Cmm45678). Special programs include Vesak, Vassa (Rains Retreat), "
            "and group ordinations."
        ),
    },
    "zen_center_las_vegas": {
        "id": "zen_center_las_vegas",
        "name": "Zen Center of Las Vegas",
        "tradition": "zen",
        "url": "https://zenlasvegas.com",
        "address": "7925 Virtue Ct",
        "city": "Las Vegas",
        "state": "NV",
        "zip": "89113",
        "lat": 36.0602,
        "lng": -115.2246,
        "neighborhood": "Enterprise / Southwest Las Vegas",
        "bio": (
            "Zen Center of Las Vegas is a Korean Zen community in the Kwan Um School of Zen, "
            "the lineage of Zen Master Seung Sahn. Located on the same campus as Chaiya "
            "Meditation Monastery in southwest Las Vegas. Teacher: Zen Master Ji Haeng. "
            "Weekly Sunday practice at 1 PM — all levels welcome, drop-in. First Sunday of "
            "each month includes a free Beginners Introduction at noon. "
            "Donations appreciated but not required."
        ),
    },
    "diamond_way_las_vegas": {
        "id": "diamond_way_las_vegas",
        "name": "Diamond Way Buddhist Center Las Vegas",
        "tradition": "tibetan",
        "url": "https://diamondway.org/lasvegas/",
        "address": "3743 N Rosecrest Circle",
        "city": "Las Vegas",
        "state": "NV",
        "zip": "89121",
        "lat": 36.1448,
        "lng": -115.0803,
        "neighborhood": "East Las Vegas",
        "bio": (
            "Diamond Way Buddhist Center Las Vegas is a Tibetan Buddhist center in the "
            "Karma Kagyu lineage of Lama Ole Nydahl. Located in east Las Vegas. Offers a "
            "weekly public meditation every Tuesday at 7 PM — no prior experience required, "
            "drop-in welcome. First Tuesday of each month is a free Open House with an "
            "introduction to Buddhism and meditation. Part of the global Diamond Way "
            "Buddhist network with 600+ centers worldwide."
        ),
    },
    "nevada_buddhist_temple": {
        "id": "nevada_buddhist_temple",
        "name": "Nevada Buddhist Temple",
        "tradition": "theravada",
        "url": "https://www.nevadabuddhisttemple.org",
        "address": "2040 Abels Lane",
        "city": "North Las Vegas",
        "state": "NV",
        "zip": "89115",
        "lat": 36.2103,
        "lng": -115.1214,
        "neighborhood": "North Las Vegas",
        "bio": (
            "Nevada Buddhist Temple is a Sri Lankan Theravada Buddhist temple in North Las "
            "Vegas, with resident monk Bhante Deepananda. Offers weekly Wednesday Evening "
            "Meditation (7–8 PM in-person) and daily online meditation and chanting via "
            "Zoom (7:30 PM, except Wednesday and Friday). Monthly 'Meditation with a Monk' "
            "sessions and traditional observances including Vesak, Poson, and Kathina. "
            "All programs are free and open to the public."
        ),
    },
    # ---------------------------------------------------------------------------
    # Nashville, TN — Phase 3 (heartbeat 27)
    # ---------------------------------------------------------------------------
    "one_dharma_nashville": {
        "id": "one_dharma_nashville",
        "name": "One Dharma Nashville",
        "tradition": "theravada",
        "url": "https://onedharmanashville.com",
        "address": "530 26th Ave N",
        "city": "Nashville",
        "state": "TN",
        "zip": "37209",
        "lat": 36.1650,
        "lng": -86.8149,
        "neighborhood": "Germantown / Midtown",
        "bio": (
            "One Dharma Nashville is an Insight Meditation community guided by teacher "
            "Lisa Ernst, offering weekly drop-in sits in the Vipassana/Theravada tradition. "
            "Monday Evening Meditation (7–8:30pm, hybrid in-person at 530 26th Ave N + Zoom) "
            "includes guided meditation, dharma talk, and discussion — all levels welcome, "
            "suggested donation $10–$15. Also Friday morning online sit (7:30–8am Zoom) and "
            "1st & 3rd Thursday sits in Franklin, TN (The Factory at Franklin, 230 Franklin Rd). "
            "No experience required."
        ),
    },
    "wild_heart_meditation": {
        "id": "wild_heart_meditation",
        "name": "Wild Heart Meditation Center",
        "tradition": "theravada",
        "url": "https://www.wildheartmeditationcenter.org",
        "address": "3123 Gallatin Pike",
        "city": "Nashville",
        "state": "TN",
        "zip": "37216",
        "lat": 36.2038,
        "lng": -86.7178,
        "neighborhood": "East Nashville",
        "bio": (
            "Wild Heart Meditation Center is an inclusive, secular meditation community "
            "in East Nashville, rooted in the Dharma Punx and Against the Stream lineage. "
            "Co-located with Nashville Zen Center at 3123 Gallatin Pike. Weekly in-person "
            "sessions include Wednesday Dharma & Discussion (7–8:30pm), Friday Dharma & "
            "Discussion (7–8:30pm), and Sunday Dharma & Discussion (9–10:30am). Also "
            "hosts Monday Recovery Dharma (7pm), Tuesday POC Sangha (1st & 3rd Tue), "
            "Thursday Queer Sangha (7pm), and daily morning online sits. All drop-in, "
            "no registration, by donation."
        ),
    },
    "nashville_zen_center": {
        "id": "nashville_zen_center",
        "name": "Nashville Zen Center",
        "tradition": "zen",
        "url": "https://nashvillezencenter.org",
        "address": "3123 Gallatin Pike",
        "city": "Nashville",
        "state": "TN",
        "zip": "37216",
        "lat": 36.2038,
        "lng": -86.7178,
        "neighborhood": "East Nashville",
        "bio": (
            "Nashville Zen Center is a Soto Zen community in the Silent Thunder Order, "
            "in the lineage of Zengaku Soyu Matsuoka, affiliated with Atlanta Soto Zen "
            "Center. Located in East Nashville, sharing space with Wild Heart Meditation "
            "Center. Weekly zazen: Tuesday 7pm (newcomers arrive at 6:30pm for orientation) "
            "and Saturday 7am. Instruction provided for beginners; no prior experience "
            "needed. Open to all."
        ),
    },
    "pbc_tennessee": {
        "id": "pbc_tennessee",
        "name": "Padmasambhava Buddhist Center of Tennessee",
        "tradition": "tibetan",
        "url": "https://www.pbc-tn.org",
        "address": "419 East Iris Drive",
        "city": "Nashville",
        "state": "TN",
        "zip": "37204",
        "lat": 36.1388,
        "lng": -86.7903,
        "neighborhood": "12South / Waverly-Belmont",
        "bio": (
            "Padmasambhava Buddhist Center of Tennessee (PBC-TN) is a Tibetan Buddhist "
            "center in the Nyingma tradition (Dzogchen), part of the international PBC "
            "network founded by Venerable Khenchen Palden Sherab Rinpoche. One of the "
            "oldest and largest Tibetan dharma centers in the South, established in 1990. "
            "Home practice at Yeshe Tsogyal Temple in Nashville's 12South neighborhood. "
            "Weekly Sunday Calm Abiding Meditation (9:30–11am) is open to all — no "
            "Buddhist background required. Teachings include Dzogchen, Vajrayana "
            "practices, and seasonal retreats."
        ),
    },
    # ── Detroit / SE Michigan ────────────────────────────────────────────────
    "detroit_zen_center": {
        "id": "detroit_zen_center",
        "name": "Detroit Zen Center",
        "tradition": "zen",
        "url": "https://www.detroitzencenter.org",
        "address": "3030 Casmere St",
        "city": "Hamtramck",
        "state": "MI",
        "zip": "48212",
        "lat": 42.3936,
        "lng": -83.0566,
        "neighborhood": "Hamtramck (Detroit metro)",
        "bio": (
            "Detroit Zen Center is a Korean Zen community in the Chogye Order, a "
            "spiritual branch of Sudeok-sa Temple in Korea (founded 6th century CE). "
            "Established in 1990 by Abbot Hwalson Sunim in Hamtramck, a small city "
            "encircled by Detroit. Sunday Zen Workshop (10am–12pm): guided meditation, "
            "dharma talk, and tea — open to all levels, drop-in welcome. First Sunday "
            "Beginners Workshop & Brunch (9am–12pm) includes meditation instruction, "
            "group sit, dharma talk, and dialogue. Organic gardens, plant-based meals, "
            "and guest retreat lodging available on site. By donation."
        ),
    },
    "still_point_zen_detroit": {
        "id": "still_point_zen_detroit",
        "name": "Still Point Zen Buddhist Temple",
        "tradition": "zen",
        "url": "https://www.stillpointzenbuddhisttemple.org",
        "address": "4345 Trumbull Ave",
        "city": "Detroit",
        "state": "MI",
        "zip": "48208",
        "lat": 42.3527,
        "lng": -83.0731,
        "neighborhood": "Corktown / Woodbridge",
        "bio": (
            "Still Point Zen Buddhist Temple is a Korean Zen community in Detroit's "
            "Corktown neighborhood, in the lineage of Venerable Samu Sunim. Founded "
            "by P'arang Geri Larkin; current guiding teacher is Koho Vince Anila. "
            "Sunday service (8:30–11:30am): zazen, chanting, dharma talk — in-person "
            "and livestreamed. Saturday service also available in-person with "
            "livestream. Hosts Recovery Dharma meetings and One Sangha outreach. "
            "Known for deep engagement with Detroit's communities. Free and open to all."
        ),
    },
    "field_temple_detroit": {
        "id": "field_temple_detroit",
        "name": "Field Temple",
        "tradition": "zen",
        "url": "https://fieldtemple.org",
        "address": "5333 Elmwood Ave",
        "city": "Detroit",
        "state": "MI",
        "zip": "48211",
        "lat": 42.3699,
        "lng": -83.0431,
        "neighborhood": "Poletown East",
        "bio": (
            "Field Temple is a small Zen community in Detroit's Poletown East "
            "neighborhood, practicing in the Korean Zen tradition. Sunday meditation "
            "(10–11am): two twenty-minute zazen periods, chanting the three refuges "
            "in Pali and English, followed by a dharma talk and tea. Sessions are "
            "held in the garden or under the trees. Open to all — no experience "
            "required. Free."
        ),
    },
    "dharma_gate_zen_troy": {
        "id": "dharma_gate_zen_troy",
        "name": "Dharma Gate Zen Center",
        "tradition": "zen",
        "url": "https://dharmagatezen.org",
        "address": "360 East Maple Suite K",
        "city": "Troy",
        "state": "MI",
        "zip": "48083",
        "lat": 42.5798,
        "lng": -83.1446,
        "neighborhood": "Troy (Detroit suburb)",
        "bio": (
            "Dharma Gate Zen Center is a Soto Zen community in Troy, Michigan (north "
            "Detroit suburb). Sunday service (10–11am) includes a 20-minute zazen "
            "period and dharma talk — open to all, beginners welcome with visitor "
            "guide available. Also hosts Recovery Dharma meetings (Saturdays 10am "
            "and Wednesdays noon) and Shinrin-Yoku forest bathing practice. "
            "Weekday sitting currently on hiatus. Free to attend."
        ),
    },
    "sbmg_sacramento": {
        "id": "sbmg_sacramento",
        "name": "Sacramento Buddhist Meditation Group",
        "tradition": "pluralist",
        "url": "https://sbmg.org",
        "address": "3111 Wissemann Drive",
        "city": "Sacramento",
        "state": "CA",
        "zip": "95826",
        "lat": 38.5516,
        "lng": -121.3810,
        "neighborhood": "South Sacramento (Sacramento Dharma Center)",
        "bio": (
            "Sacramento Buddhist Meditation Group (SBMG) is the oldest and largest "
            "pluralist meditation sangha in Sacramento, meeting since the 1970s. "
            "Based at Sacramento Dharma Center, a shared nonprofit campus at 3111 "
            "Wissemann Drive. Weekly Sunday Meditation & Dharma Talk (10am–12pm, "
            "hybrid): 40-minute silent sit followed by a talk from rotating teachers "
            "across Zen, Vipassana, Tibetan, and secular traditions. Also Tuesday "
            "Online Morning Meditation (7am via Zoom), BIPOC Sangha (4th Sunday), "
            "Family Sangha (4th Sunday), and Introduction to Meditation (1st Sundays). "
            "All programs dana-based; all welcome."
        ),
    },
    "valley_streams_zen": {
        "id": "valley_streams_zen",
        "name": "Valley Streams Zen Sangha",
        "tradition": "zen",
        "url": "https://valleystreamszen.org",
        "address": "3111 Wissemann Drive",
        "city": "Sacramento",
        "state": "CA",
        "zip": "95826",
        "lat": 38.5516,
        "lng": -121.3810,
        "neighborhood": "South Sacramento (Sacramento Dharma Center)",
        "bio": (
            "Valley Streams Zen Sangha practices Soto Zen in the Ordinary Mind Zen "
            "school — the lineage of Charlotte Joko Beck, adapting Zen practice for "
            "Western students while maintaining traditional rigor. Based at Sacramento "
            "Dharma Center, 3111 Wissemann Drive. Weekly Morning Zazen & Service "
            "(Thursdays 6–7:30am, hybrid): zazen, kinhin, service, and tea. Monday "
            "Evening Program (7–9pm, hybrid): dharma talks, study, and sitting. "
            "Introduction to Zen Meditation offered monthly (2nd Monday 6pm). "
            "Drop-in welcome; free."
        ),
    },
    "sacramento_insight_meditation": {
        "id": "sacramento_insight_meditation",
        "name": "Sacramento Insight Meditation",
        "tradition": "theravada",
        "url": "https://sactoinsight.org",
        "address": "3111 Wissemann Drive",
        "city": "Sacramento",
        "state": "CA",
        "zip": "95826",
        "lat": 38.5516,
        "lng": -121.3810,
        "neighborhood": "South Sacramento (Sacramento Dharma Center)",
        "bio": (
            "Sacramento Insight Meditation (SIM) is a Vipassana/Theravada sangha "
            "meeting at Sacramento Dharma Center, 3111 Wissemann Drive. Weekly "
            "Thursday Meditation & Dharma Talk (7–9pm, hybrid): guided sitting "
            "practice, dharma talk, and discussion — open to all levels. Also "
            "Tuesday Dharma Recovery Sangha (6:30–8pm, in-person): meditation and "
            "community for people seeking recovery, open to everyone. Monthly one-day "
            "retreats offered. Young Persons Sangha (Wednesdays, bi-weekly) for "
            "adults in their 20s–40s. All programs dana-based."
        ),
    },
    # Baltimore, MD — Phase 3 (heartbeat 30)
    "baltimore_shambhala": {
        "id": "baltimore_shambhala",
        "name": "Baltimore Shambhala Centre",
        "tradition": "tibetan",
        "url": "https://baltimore.shambhala.org",
        "address": "33 W 33rd St",
        "city": "Baltimore",
        "state": "MD",
        "zip": "21218",
        "lat": 39.3277,
        "lng": -76.6093,
        "neighborhood": "Charles Village (33rd Street YMCA)",
        "bio": (
            "Baltimore Shambhala Centre is a meditation community in the Shambhala "
            "lineage of Chögyam Trungpa Rinpoche and Sakyong Mipham Rinpoche, meeting "
            "at the 33rd Street YMCA in Charles Village. Offers biweekly in-person "
            "practice (Meditation@33rd, 2nd & 4th Saturdays 9–10am, hybrid in-person "
            "and Zoom) and weekday morning sittings via Zoom (Mon–Fri 7–8am). Sunday "
            "Morning Sitting (9–9:30am, Zoom) and Thursday Lojong Study Group also "
            "offered. Programs are free and open to all — no experience required."
        ),
    },
    "kmc_maryland": {
        "id": "kmc_maryland",
        "name": "Kadampa Meditation Center Maryland",
        "tradition": "tibetan",
        "url": "https://www.meditationmd.org",
        "address": "901 Dartmouth Road",
        "city": "Baltimore",
        "state": "MD",
        "zip": "21212",
        "lat": 39.3562,
        "lng": -76.6383,
        "neighborhood": "Roland Park",
        "bio": (
            "Kadampa Meditation Center Maryland (KMC Maryland) is a New Kadampa "
            "Tradition center in Roland Park, north Baltimore, offering multiple weekly "
            "drop-in meditation classes. Schedule: Sunday Meditations for Modern Life "
            "(10:30–11:45am), Wednesday Meditations for Modern Life (11am–noon), "
            "Wednesday World Peace Meditation (6–7pm), Thursday Meditations for Modern "
            "Life (6:30–7:45pm). Also runs a Canton branch (1025 S Potomac St) on "
            "Tuesdays at 7pm. All classes taught in the NKT tradition (Tibetan Gelugpa "
            "lineage). First class free; $12 thereafter. No Buddhist background required."
        ),
    },
    "kmc_maryland_canton": {
        "id": "kmc_maryland_canton",
        "name": "Kadampa Meditation Center Maryland — Canton",
        "tradition": "tibetan",
        "url": "https://www.meditationmd.org",
        "address": "1025 S Potomac St",
        "city": "Baltimore",
        "state": "MD",
        "zip": "21224",
        "lat": 39.2848,
        "lng": -76.5758,
        "neighborhood": "Canton",
        "bio": (
            "Kadampa Meditation Center Maryland's Canton branch meets at Church on "
            "the Square (1025 S Potomac St) in southeast Baltimore's Canton "
            "neighborhood. Weekly Tuesday meditation class (7–8pm): guided practice "
            "in the New Kadampa Tradition (Tibetan Gelugpa lineage). Open to all "
            "levels — no experience required. First class free, $12 thereafter. "
            "For more information visit meditationmd.org."
        ),
    },
    "baltimore_dharma_group": {
        "id": "baltimore_dharma_group",
        "name": "Baltimore Dharma Group",
        "tradition": "zen",
        "url": "https://www.baltimoredharmagroup.org",
        "address": "3107 N Charles St",
        "city": "Baltimore",
        "state": "MD",
        "zip": "21218",
        "lat": 39.3262,
        "lng": -76.6202,
        "neighborhood": "Guilford / Charles Village (Homewood Friends Meeting)",
        "bio": (
            "Baltimore Dharma Group is a lay Soto Zen sangha practicing shikantaza "
            "(just sitting) at Homewood Friends Meeting House in Baltimore's Charles "
            "Village / Guilford area. Sunday morning zazen (8–9:30am): two "
            "thirty-minute sitting periods with kinhin walking meditation, arrive by "
            "7:55am. Thursday evenings alternate between open zazen (two 30-min "
            "periods + kinhin) and dharma class (30-min sit + discussion). Free "
            "and open to all — no prior meditation experience needed."
        ),
    },
    "lions_roar_dharma_center": {
        "id": "lions_roar_dharma_center",
        "name": "Lion's Roar Dharma Center",
        "tradition": "tibetan",
        "url": "https://lionsroardharmacenter.org",
        "address": "3240 B Street",
        "city": "Sacramento",
        "state": "CA",
        "zip": "95816",
        "lat": 38.5768,
        "lng": -121.4545,
        "neighborhood": "Midtown Sacramento",
        "bio": (
            "Lion's Roar Dharma Center (LRDC) is a Tibetan Buddhist center in "
            "Midtown Sacramento at the Do Nga Dargey Temple (3240 B Street, between "
            "32nd and 33rd). Teacher: Lama Yeshe Jinpa. Offers monthly in-person "
            "Vajrayana practices on the moon phases (waxing, full, waning, new), "
            "Sunday services including Shambhala Journey, visiting teacher programs, "
            "and the Sustainable Service Program (quarterly half-day retreats). "
            "All programs are hybrid (in-person and online). Dana-based; all welcome."
        ),
    },

    # ── Ann Arbor, MI ───────────────────────────────────────────────────────

    "jewel_heart_ann_arbor": {
        "id": "jewel_heart_ann_arbor",
        "name": "Jewel Heart",
        "tradition": "tibetan",
        "url": "https://www.jewelheart.org",
        "address": "1129 Oak Valley Drive",
        "city": "Ann Arbor",
        "state": "MI",
        "zip": "48108",
        "lat": 42.2209,
        "lng": -83.6972,
        "neighborhood": "Southeast Ann Arbor",
        "bio": (
            "Jewel Heart is a Tibetan Buddhist (Gelugpa/Mahayana) center founded by "
            "Kyabje Gelek Rimpoche and now led by resident director Demo Rinpoche. "
            "International headquarters at 1129 Oak Valley Drive, Ann Arbor — Gelek "
            "Rimpoche taught here from 1988, and the 14th Dalai Lama offered teachings "
            "here in 2008. Regular public offerings include a free weekly Community "
            "Meditation (Tuesdays 6–6:45pm, in-person), Sunday programs (White Tara "
            "Guided Meditation 9:30–10:30am, onsite + online), and periodic Wednesday "
            "courses. All levels welcome; weekly sit is free."
        ),
    },
    "insight_meditation_ann_arbor": {
        "id": "insight_meditation_ann_arbor",
        "name": "Insight Meditation Ann Arbor",
        "tradition": "theravada",
        "url": "https://insightmeditationannarbor.org",
        "address": "180 Little Lake Drive, Suite 1",
        "city": "Ann Arbor",
        "state": "MI",
        "zip": "48103",
        "lat": 42.2810,
        "lng": -83.7912,
        "neighborhood": "West Ann Arbor (near Westgate)",
        "bio": (
            "Insight Meditation Ann Arbor (IMAA) offers Theravada / Insight Meditation "
            "sits for all experience levels. Regular schedule: Sunday in-person meditation "
            "(10–11:15am: 45-minute sit + dharma talk, at 180 Little Lake Drive Suite 1); "
            "Saturday online meditation via Zoom (10–11:30am); weekday morning sits "
            "Mon–Fri via Zoom (7:30–8:00am, optional continuation to 8:30am). Courses "
            "in MBSR and other contemplative programs also offered. No experience required; "
            "free and donation-based."
        ),
    },
    "zen_buddhist_temple_ann_arbor": {
        "id": "zen_buddhist_temple_ann_arbor",
        "name": "Zen Buddhist Temple — Ann Arbor",
        "tradition": "zen",
        "url": "https://www.zenbuddhisttemple.org/annarbor",
        "address": "1214 Packard Street",
        "city": "Ann Arbor",
        "state": "MI",
        "zip": "48104",
        "lat": 42.2631,
        "lng": -83.7423,
        "neighborhood": "Burns Park (near UMich campus)",
        "bio": (
            "Zen Buddhist Temple Ann Arbor is a Korean Zen (Son Buddhism) temple in "
            "the Burns Park neighborhood, part of the Buddhist Society of Compassionate "
            "Wisdom (founded by Samu Sunim). Resident priests: Haju Sunim and Maum. "
            "Sunday Public Service (10am, in-person + livestreamed): meditation, dharma "
            "talk, and ceremonies. Recovery Dharma (Sundays noon, online) and periodic "
            "5-week Meditation Courses (Thursdays 6:30–8:30pm) also offered. Drop-in "
            "welcome for Sunday services. Free."
        ),
    },

    # ── Pittsburgh, PA ──────────────────────────────────────────────────────

    "stillpoint_zen_pittsburgh": {
        "id": "stillpoint_zen_pittsburgh",
        "name": "Stillpoint — A Pittsburgh Zen Community",
        "tradition": "zen",
        "url": "https://www.stillpointzen.org",
        "address": "137 41st St",
        "city": "Pittsburgh",
        "state": "PA",
        "zip": "15201",
        "lat": 40.4646,
        "lng": -79.9644,
        "neighborhood": "Lawrenceville",
        "bio": (
            "Stillpoint is a lay Zen community in the Lawrenceville neighborhood of "
            "Pittsburgh, offering drop-in zazen twice a week: Sunday morning "
            "(9:30–10:40am) and Wednesday evening (7–8pm), plus a monthly all-day "
            "zazenkai (fourth Saturday). Newcomers are warmly welcomed; a private "
            "introduction to zazen is offered to those new to the practice. "
            "No experience or membership required. Free, donation welcome. "
            "Contact: sit@stillpointzen.org."
        ),
    },
    "pittsburgh_buddhist_center": {
        "id": "pittsburgh_buddhist_center",
        "name": "Pittsburgh Buddhist Center",
        "tradition": "theravada",
        "url": "https://www.pittsburghbuddhistcenter.org",
        "address": "58 QSI Lane",
        "city": "Allison Park",
        "state": "PA",
        "zip": "15101",
        "lat": 40.5760,
        "lng": -79.9576,
        "neighborhood": "Allison Park (Hampton Township)",
        "bio": (
            "Pittsburgh Buddhist Center is a Theravada community with resident Burmese "
            "monks offering free public weekly sits. Main center: Wednesday evenings "
            "(7–9:30pm, 58 QSI Lane, Allison Park; beginners arrive 6:30pm for private "
            "instruction from monks). Outreach sits at Oakmont Carnegie Library "
            "(Tuesday 6pm) and East Liberty Carnegie Library (Monday 6pm). Monks "
            "available for dharma conversation after each sit. All programs free and "
            "open to the public. Livestream: youtube.com/pbclive."
        ),
    },
    "pittsburgh_buddhist_center_oakmont": {
        "id": "pittsburgh_buddhist_center_oakmont",
        "name": "Pittsburgh Buddhist Center — Oakmont",
        "tradition": "theravada",
        "url": "https://www.pittsburghbuddhistcenter.org",
        "address": "700 Allegheny River Blvd",
        "city": "Oakmont",
        "state": "PA",
        "zip": "15139",
        "lat": 40.5209,
        "lng": -79.8362,
        "neighborhood": "Oakmont Carnegie Library",
        "bio": (
            "Pittsburgh Buddhist Center outreach sit at Oakmont Carnegie Library. "
            "Weekly Tuesday evenings, 6pm. Led by resident Burmese monks from the "
            "main Pittsburgh Buddhist Center in Allison Park. Free and open to the "
            "public; all experience levels welcome. Monks available for dharma Q&A "
            "after sits."
        ),
    },
    "olmo_ling_pittsburgh": {
        "id": "olmo_ling_pittsburgh",
        "name": "Olmo Ling Bon Center and Institute",
        "tradition": "tibetan",
        "url": "https://www.olmoling.org",
        "address": "1101 Greenfield Ave",
        "city": "Pittsburgh",
        "state": "PA",
        "zip": "15217",
        "lat": 40.4180,
        "lng": -79.9449,
        "neighborhood": "Greenfield",
        "bio": (
            "Olmo Ling Bon Center is a center for Tibetan Bon Buddhism — the indigenous "
            "pre-Buddhist spiritual tradition of Tibet, closely related to but distinct "
            "from Vajrayana Buddhism. Located in the Greenfield neighborhood of "
            "Pittsburgh. The Sunday Dzogchen Practice Group (4–6pm) meets on 1st and "
            "3rd Sundays in-person with Zoom option: meditation practice on 1st/3rd "
            "Sundays, reading and discussion on 2nd/4th Sundays. Free and open to all. "
            "Founded in the lineage of Geshe Tenzin Wangyal Rinpoche. "
            "Contact: bon@olmoling.org."
        ),
    },
    # ── St. Louis, MO ────────────────────────────────────────────────────────

    "confluence_zen_stl": {
        "id": "confluence_zen_stl",
        "name": "Confluence Zen Center STL",
        "tradition": "zen",
        "url": "https://www.confluencezen.org",
        "address": "3544 Oxford Avenue",
        "city": "Maplewood",
        "state": "MO",
        "zip": "63143",
        "lat": 38.5981,
        "lng": -90.3287,
        "neighborhood": "Maplewood (St. Louis suburb)",
        "bio": (
            "Confluence Zen Center STL is a Soto Zen lay community in Maplewood, MO, "
            "led by Daigaku Rumme (SZBA-authorized teacher). Regular schedule: Morning "
            "Zazen Mon/Tue/Thu 6:20–7:15am; Evening Zazen Monday 7–8pm; Sunday Zazen "
            "9–11am (2nd, 3rd, 4th, and 5th Sundays); Beginner's Night first Tuesday "
            "monthly 6:30pm. Periodic one-day sittings, sesshins (including Rohatsu in "
            "December), and dharma study groups. Drop-in welcome for zazen; beginners "
            "encouraged to attend Beginner's Night first. Free, dana-based."
        ),
    },
    "sunday_sangha_stl": {
        "id": "sunday_sangha_stl",
        "name": "Sunday Sangha St. Louis",
        "tradition": "theravada",
        "url": "https://sundaysangha-stl.org",
        "address": "",
        "city": "Brentwood",
        "state": "MO",
        "zip": "63144",
        "lat": 38.6107,
        "lng": -90.3494,
        "neighborhood": "Brentwood (St. Louis suburb)",
        "bio": (
            "Sunday Sangha St. Louis is a Theravada/Insight Meditation community "
            "meeting every Sunday 11am–12:30pm in Brentwood, MO (hybrid: in-person "
            "and Zoom). Sessions begin with ~40 minutes of silent meditation, followed "
            "by brief instruction in the Insight tradition, facilitator sharing, and "
            "open discussion. All spiritual backgrounds welcome. Free (donations "
            "cover the $35/week space rental — cash only). Meeting location and Zoom "
            "link shared with email list subscribers at sundaysangha-stl.org."
        ),
    },
    "center_pragmatic_buddhism_stl": {
        "id": "center_pragmatic_buddhism_stl",
        "name": "Center for Pragmatic Buddhism — St. Louis",
        "tradition": "zen",
        "url": "https://www.pragmaticbuddhism.org/stlouis",
        "address": "5007 Waterman Boulevard",
        "city": "St. Louis",
        "state": "MO",
        "zip": "63108",
        "lat": 38.6428,
        "lng": -90.2724,
        "neighborhood": "Central West End (at First Unitarian Church)",
        "bio": (
            "The Center for Pragmatic Buddhism (CPB) St. Louis chapter holds weekly "
            "Thursday practice 7–8:30pm Central at First Unitarian Church of St. Louis "
            "(5007 Waterman Blvd at Kingshighway, MO 63108). CPB synthesizes early "
            "Indian Buddhist teachings (Nikayan), Chinese Chan and Japanese Zen, and "
            "American Pragmatism. Practice combines zazen, dharma talks, and group "
            "discussion. Enter through the north/back garden walkway to glass doors "
            "on the left. Free and open to all. Weekday online sits also available "
            "nationally via the CPB community."
        ),
    },

    "cincinnati_zen_center": {
        "id": "cincinnati_zen_center",
        "name": "Cincinnati Zen Center",
        "tradition": "zen",
        "url": "https://www.cincinnatizencenter.org",
        "address": "6015 Vine Street",
        "city": "Cincinnati",
        "state": "OH",
        "zip": "45216",
        "lat": 39.1851,
        "lng": -84.5036,
        "neighborhood": "Hartwell (North Cincinnati)",
        "bio": (
            "Cincinnati Zen Center offers weekly in-person and online sits in the Hartwell "
            "neighborhood of North Cincinnati. Founded under Zen Master Dae Gak (Furnace "
            "Mountain Sangha), the center blends Korean Kwan Um and Soto Zen influences. "
            "In-person schedule: Sunday 8am, Monday 7pm, Wednesday 5:30pm, Thursday 7pm — "
            "all drop-in welcome; arrive 10–15 minutes early for your first visit. "
            "Saturday 8:30am is virtual Zoom only. Doors lock at the start of sits. Free."
        ),
    },

    "buddhist_dharma_center_cincinnati": {
        "id": "buddhist_dharma_center_cincinnati",
        "name": "Buddhist Dharma Center of Cincinnati",
        "tradition": "pluralist",
        "url": "https://www.cincinnatidharma.org",
        "address": "15 Moline Court",
        "city": "Cincinnati",
        "state": "OH",
        "zip": "45223",
        "lat": 39.1716,
        "lng": -84.5222,
        "neighborhood": "Northside",
        "bio": (
            "The Buddhist Dharma Center of Cincinnati is a non-sectarian, ecumenical "
            "practice community in the Northside neighborhood. Rooted in the Theravada/"
            "Insight tradition but welcoming all approaches. Offers daily 7am Zoom sits "
            "(seven days a week), Sunday 10am hybrid sits (ritual, two sits, and walking "
            "meditation), Tuesday 7pm silent in-person sitting, and Wednesday 7pm hybrid "
            "instruction and discussion. Periodic day-long retreats. Free; donations welcome."
        ),
    },

    "gaden_samdrupling_monastery": {
        "id": "gaden_samdrupling_monastery",
        "name": "Gaden Samdrupling Buddhist Monastery",
        "tradition": "tibetan",
        "url": "https://www.gslmonastery.org",
        "address": "3046 Pavlova Drive",
        "city": "Cincinnati",
        "state": "OH",
        "zip": "45251",
        "lat": 39.2147,
        "lng": -84.6198,
        "neighborhood": "Colerain Township (West Side)",
        "bio": (
            "Gaden Samdrupling Buddhist Monastery (GSL) is a Tibetan Buddhist monastery "
            "of the Gelug school (Gaden lineage) on Cincinnati's West Side. The Wednesday "
            "7–8pm Open Meditation is open to the public as a drop-in silent sitting — "
            "monastery prayer books provided. Friday evenings offer an Introduction to "
            "Buddhism with Ven. Jamyan Lama. One of the few Tibetan monasteries in the "
            "greater Cincinnati region."
        ),
    },

    "rime_buddhist_center": {
        "id": "rime_buddhist_center",
        "name": "Rime Buddhist Center",
        "tradition": "pluralist",
        "url": "https://www.rimecenter.org",
        "address": "2939 Wayne Avenue",
        "city": "Kansas City",
        "state": "MO",
        "zip": "64109",
        "lat": 39.0278,
        "lng": -94.5594,
        "neighborhood": "Waldo/Brookside",
        "bio": (
            "Rime Buddhist Center is one of the most active non-sectarian Buddhist "
            "centers in the Midwest, with over 30 years in Kansas City's "
            "Waldo/Brookside neighborhood. Founded on Rimé philosophy — drawing from "
            "all four major Tibetan schools plus Zen — the center welcomes all "
            "traditions and experience levels. Regular schedule: Mon–Fri 12–12:30pm "
            "daily group meditation; Monday 7–8pm Zen Meditation; Wednesday 7–7:30pm "
            "Group Meditation; Thursday 7–7:30pm Group Meditation and Medicine Buddha "
            "Sadhana; Sunday 10:30am Service/Practice (childcare available). "
            "Free; donations welcome."
        ),
    },

    "kansas_zen_center_kc": {
        "id": "kansas_zen_center_kc",
        "name": "Kansas Zen Center — Kansas City",
        "tradition": "zen",
        "url": "https://www.kansaszencenter.org",
        "address": "707 West 47th Street",
        "city": "Kansas City",
        "state": "MO",
        "zip": "64112",
        "lat": 39.0462,
        "lng": -94.5905,
        "neighborhood": "Country Club Plaza (at Unity Temple)",
        "bio": (
            "The Kansas City branch of the Kansas Zen Center holds weekly Thursday "
            "evening sits at Unity Temple on the Plaza (47th & Jefferson). Practice "
            "follows the Kwan Um School of Zen (Korean Zen) under Zen Master Bon Hae "
            "(Judy Roitman). The first Thursday includes Q&A with the teacher; the "
            "fourth Thursday features kong-an interviews with Dennis Duermeier JDPSN. "
            "In-person only. Drop-in welcome. Free."
        ),
    },

    "imcr": {
        "id": "imcr",
        "name": "Insight Meditation Community of Richmond",
        "tradition": "theravada",
        "url": "https://imcrva.org",
        "address": "3411 Grove Avenue",
        "city": "Richmond",
        "state": "VA",
        "zip": "23221",
        "lat": 37.5532,
        "lng": -77.4774,
        "neighborhood": "Fan District (at Ekoji)",
        "bio": (
            "Insight Meditation Community of Richmond (IMCR) is Richmond's primary "
            "Vipassana/Insight Meditation community, meeting at Ekoji Buddhist Sangha "
            "in the Fan District. Weekly sits: Tuesdays 7–9pm and Fridays 5:45–7:30pm "
            "— sit, walking meditation, dharma teaching or book discussion — in-person "
            "at Ekoji and via Zoom. Monthly specials include the 1st Sunday 'Unplug' "
            "program, 2nd Saturday Early Sit (starting 5:45am), and Engaged Buddhism "
            "evenings. Also offers daylong retreats and weekend retreats at off-site "
            "locations. Free; dana welcome."
        ),
    },

    "richmond_zen": {
        "id": "richmond_zen",
        "name": "Richmond Zen",
        "tradition": "zen",
        "url": "https://www.richmondzen.org",
        "address": "3411 Grove Avenue",
        "city": "Richmond",
        "state": "VA",
        "zip": "23221",
        "lat": 37.5532,
        "lng": -77.4774,
        "neighborhood": "Fan District (at Ekoji)",
        "bio": (
            "Richmond Zen practices in the Soto Zen lineage of Shunryu Suzuki Roshi, "
            "affiliated with Branching Streams. Guiding teacher: Josho Phelan Roshi "
            "(abbess, Chapel Hill Zen Center); head priest: Eden Kevin Heffernan. "
            "Meets at Ekoji Buddhist Sangha in Richmond's Fan District. Schedule: "
            "Sundays 9–11:30am, Tuesdays 6:30–7:30am, Wednesdays 7–8:30pm, Fridays "
            "6:30–7:30am — all in-person. Newcomer orientations offered regularly. "
            "Drop-in welcome. Free."
        ),
    },

    "nyama_sangha": {
        "id": "nyama_sangha",
        "name": "Nyama Sangha",
        "tradition": "tibetan",
        "url": "https://ekojirichmond.org/richmond-shambhala/",
        "address": "3411 Grove Avenue",
        "city": "Richmond",
        "state": "VA",
        "zip": "23221",
        "lat": 37.5532,
        "lng": -77.4774,
        "neighborhood": "Fan District (at Ekoji)",
        "bio": (
            "Nyama Sangha is Richmond's Shambhala-lineage meditation community, "
            "meeting weekly at Ekoji Buddhist Sangha in the Fan District. Saturday "
            "morning sits at 10:30am in-person and via Zoom. Open to practitioners "
            "of all backgrounds; no experience necessary. Instruction available for "
            "newcomers. Free; donations appreciated."
        ),
    },

    "palpung_richmond": {
        "id": "palpung_richmond",
        "name": "Palpung Shenpen Tharchin",
        "tradition": "tibetan",
        "url": "https://palpungrichmond.org",
        "address": "3411 Grove Avenue",
        "city": "Richmond",
        "state": "VA",
        "zip": "23221",
        "lat": 37.5532,
        "lng": -77.4774,
        "neighborhood": "Fan District (at Ekoji)",
        "bio": (
            "Palpung Shenpen Tharchin is a Tibetan Buddhist community in the Palpung "
            "Kagyu lineage, meeting at Ekoji Buddhist Sangha under the guidance of "
            "Lama Linda. Thursday evenings 7pm in-person at Ekoji and via Zoom. "
            "Practices rotate by week: 1st Thursday — Chenrezig in English; "
            "2nd Thursday — Chenrezig in Tibetan; 3rd Thursday — Green Tara in "
            "English; 4th Thursday — Green Tara in Tibetan; 5th Thursday — Medicine "
            "Buddha. 4th Sunday afternoon teachings with Lama Linda (monthly). "
            "All open to the public; newcomers welcome. Free."
        ),
    },

    "columbus_ktc": {
        "id": "columbus_ktc",
        "name": "Columbus Karma Thegsum Choling",
        "tradition": "tibetan",
        "url": "https://columbusktc.org",
        "address": "645 W. Rich Street",
        "city": "Columbus",
        "state": "OH",
        "zip": "43215",
        "lat": 39.9553,
        "lng": -83.0057,
        "neighborhood": "Franklinton",
        "bio": (
            "Columbus Karma Thegsum Choling (KTC) is a Tibetan Buddhist meditation "
            "center in the Karma Kagyu lineage, affiliated with Karma Triyana Dharmachakra "
            "monastery in Woodstock, NY. Founded in 1977, one of the oldest Tibetan "
            "Buddhist centers in the Midwest. Weekly program: Sunday Introduction to "
            "Meditation (10am, hybrid) and Dharma Talk (11:30am), Tuesday Chenrezig "
            "Puja (7pm, virtual), Wednesday Midday Meditation (12:15pm, virtual). "
            "Free and open to all; no experience required."
        ),
    },

    "mud_lotus_sangha": {
        "id": "mud_lotus_sangha",
        "name": "Mud Lotus Sangha",
        "tradition": "zen",
        "url": "https://www.mudlotussangha.org",
        "address": "17 E. Tulane Road",
        "city": "Columbus",
        "state": "OH",
        "zip": "43202",
        "lat": 40.0135,
        "lng": -82.9975,
        "neighborhood": "Clintonville (at ILLIO Studios)",
        "bio": (
            "Mud Lotus Sangha is Columbus's most active Zen community, practicing "
            "Soto Zen (White Plum lineage) with engaged Buddhism influences, meeting "
            "at ILLIO Studios in Clintonville. Weekly sits: Tuesday 7:30–8am Morning "
            "Meditation (in-person), Wednesday 7–9pm Evening Zen with dharma discussion "
            "(in-person), Thursday 9–10am Morning Meditation (hybrid). Monthly sesshins "
            "and day retreats. Drop-in welcome; free."
        ),
    },

    "zen_columbus": {
        "id": "zen_columbus",
        "name": "Zen Columbus Sangha",
        "tradition": "zen",
        "url": "http://zencolumbus.org",
        "address": "93 W. Weisheimer Road",
        "city": "Columbus",
        "state": "OH",
        "zip": "43214",
        "lat": 40.0569,
        "lng": -83.0201,
        "neighborhood": "Clintonville (at First UU Church)",
        "bio": (
            "Zen Columbus Sangha is an independent Soto Zen community offering weekly "
            "zazen at the First Unitarian Universalist Church. Tuesday evenings 7–8:15pm "
            "and Saturday mornings 8:30–9:45am: two 25-minute zazen periods with kinhin "
            "and brief service. Both sessions are hybrid (in-person + Zoom). Introduction "
            "to Zazen on the 2nd Saturday and 4th Tuesday monthly. All welcome; free."
        ),
    },

    "cocpb_columbus": {
        "id": "cocpb_columbus",
        "name": "Central Ohio Center for Pragmatic Buddhism",
        "tradition": "zen",
        "url": "https://www.cocpb.com",
        "address": "77 N. Brinker Avenue",
        "city": "Columbus",
        "state": "OH",
        "zip": "43204",
        "lat": 39.9706,
        "lng": -83.0453,
        "neighborhood": "West Side",
        "bio": (
            "The Central Ohio Center for Pragmatic Buddhism (COCPB) synthesizes early "
            "Nikayan Buddhism, Chan, Japanese Zen, and American Pragmatist philosophy. "
            "Sensei Manny Shinshim leads weekly Sunday zazen (9:30am–noon) with dharma "
            "talk in an intimate second-floor zendo on Columbus's West Side. In-person. "
            "All welcome; donations appreciated."
        ),
    },

    "bliss_run_sangha": {
        "id": "bliss_run_sangha",
        "name": "Bliss Run Sangha",
        "tradition": "other",
        "url": "https://www.blissrun.org",
        "address": "4211 Maize Road",
        "city": "Columbus",
        "state": "OH",
        "zip": "43224",
        "lat": 40.0762,
        "lng": -82.9981,
        "neighborhood": "North Linden (at Unity Church)",
        "bio": (
            "Bliss Run Sangha is a Plum Village (Thich Nhat Hanh / Order of Interbeing) "
            "practice community at Unity Church in Columbus's North Linden neighborhood. "
            "Thursday evenings: newcomer orientation at 6:45pm, then 7–9pm walking "
            "meditation, sitting meditation, and dharma discussion. In-person. "
            "All welcome; free."
        ),
    },

    "durham_shambhala": {
        "id": "durham_shambhala",
        "name": "Durham Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://durham.shambhala.org",
        "address": "733 Rutherford Street",
        "city": "Durham",
        "state": "NC",
        "zip": "27705",
        "lat": 36.0018,
        "lng": -78.9281,
        "neighborhood": "Duke Park",
        "bio": (
            "Durham Shambhala Meditation Center is part of the international Shambhala "
            "network, offering meditation instruction rooted in the Tibetan and Shambhala "
            "warrior traditions. Weekly schedule: Thursday Night Open House (7–8:30pm, "
            "in-person — free meditation instruction, group sit, and refreshments, great "
            "for newcomers); Sunday Morning Meditation (9am–noon, in-person); Saturday "
            "Dharma Discussions (10:30am–noon, Zoom); Heart of Recovery on Wednesdays "
            "(7pm, in-person). All are welcome; no experience required. Free."
        ),
    },

    "chapel_hill_zen": {
        "id": "chapel_hill_zen",
        "name": "Chapel Hill Zen Center",
        "tradition": "zen",
        "url": "https://www.chzc.org",
        "address": "5322 NC Highway 86",
        "city": "Chapel Hill",
        "state": "NC",
        "zip": "27514",
        "lat": 35.9763,
        "lng": -79.0485,
        "neighborhood": "North Chapel Hill",
        "bio": (
            "The Chapel Hill Zen Center practices Soto Zen in the lineage of Shunryu "
            "Suzuki-roshi (San Francisco Zen Center tradition). Embracing diversity, the "
            "center welcomes everyone to the practice of zazen. Located 2.5 miles north "
            "of I-40 exit 266 on NC-86. Weekly schedule: Monday–Friday morning zazen at "
            "6am and 6:50am (in-person and Zoom); Tuesday evening zazen at 7pm and 7:50pm "
            "(in-person); Sunday morning zazen at 9am and 9:50am (in-person). Instruction "
            "available Tuesday evenings and Sunday mornings — please contact before your "
            "first visit."
        ),
    },

    "nc_zen_center": {
        "id": "nc_zen_center",
        "name": "North Carolina Zen Center",
        "tradition": "zen",
        "url": "https://nczencenter.org",
        "address": "390 Ironwood Road",
        "city": "Pittsboro",
        "state": "NC",
        "zip": "27312",
        "lat": 35.7268,
        "lng": -79.1823,
        "neighborhood": "Rural Chatham County",
        "bio": (
            "The North Carolina Zen Center (NCZC) is a residential Zen Buddhist community "
            "and retreat center on 15 wooded acres south of Chapel Hill, led by Teshin "
            "Roshi. A full week of practice is offered: Sunday morning (10am–noon, two "
            "zazen periods + chanting service + dharma talk); Monday morning Zoom zazen "
            "(7–7:50am); Tuesday evening dharma study + zazen (7–8:30pm, in-person); "
            "Wednesday morning zazen (7–7:50am, hybrid); Thursday evening zazen + chanting "
            "service with dokusan available (7–8:30pm, in-person); Friday morning zazen "
            "(7–7:50am, hybrid). Residential practice and personal retreats available. "
            "All levels welcome."
        ),
    },

    "three_rivers_tibetan_pittsburgh": {
        "id": "three_rivers_tibetan_pittsburgh",
        "name": "Three Rivers Tibetan Cultural Center",
        "tradition": "tibetan",
        "url": "https://www.threeriverstibetancc.org",
        "address": "1660 Lincoln Way",
        "city": "White Oak",
        "state": "PA",
        "zip": "15131",
        "lat": 40.3407,
        "lng": -79.8289,
        "neighborhood": "White Oak (SE Pittsburgh metro)",
        "bio": (
            "Three Rivers Tibetan Cultural Center (TRTCC) is a Drikung Kagyu lineage "
            "Tibetan Buddhist center in White Oak, PA (~12 miles southeast of Pittsburgh), "
            "with resident teachers Ven. Khenpo Choephel and Ven. Lama Kalsang. Weekly "
            "practices include rotating Chenrezig, Manjushri, Medicine Buddha, and Green "
            "Tara pujas on Wednesday evenings (7pm, hybrid in-person + Zoom), Vajrasattva "
            "practice on Sunday mornings (10am, hybrid), and Dharma Discussion on Saturdays "
            "(10–10:30am, hybrid). Tuesday 7pm online Beginner Buddhism class. All levels "
            "welcome; no experience required. Free."
        ),
    },
    # ── Salt Lake City, UT ───────────────────────────────────────────────────
    "two_arrows_zen": {
        "id": "two_arrows_zen",
        "name": "Two Arrows Zen",
        "tradition": "zen",
        "url": "https://twoarrowszen.org",
        "address": "21 G Street",
        "city": "Salt Lake City",
        "state": "UT",
        "zip": "84103",
        "neighborhood": "The Avenues",
        "lat": 40.7729,
        "lng": -111.8844,
        "description": (
            "Two Arrows Zen is a Soto Zen community in Salt Lake City's historic Avenues "
            "neighborhood, practicing in the White Plum Asanga lineage (Maezumi Roshi). "
            "Founded by Genro Gauntt Roshi. The zendo offers weekday morning zazen "
            "(Mon–Fri 7:00am, two periods) and Thursday evening Zen service (5:30pm, "
            "zazen + dharma talk). Seasonal sesshins and weekend intensives throughout "
            "the year. Drop-in welcome; please arrive before the bell. Free."
        ),
    },
    "urgyen_samten_ling": {
        "id": "urgyen_samten_ling",
        "name": "Urgyen Samten Ling Gonpa",
        "tradition": "tibetan",
        "url": "https://www.urgyensamtenling.org",
        "address": "740 South 300 West",
        "city": "Salt Lake City",
        "state": "UT",
        "zip": "84101",
        "neighborhood": "Downtown Salt Lake City",
        "lat": 40.7520,
        "lng": -111.9006,
        "description": (
            "Urgyen Samten Ling Gonpa is a Nyingma Tibetan Buddhist center two blocks "
            "from downtown Salt Lake City, founded by Khenpo Ugyen Tenzin Rinpoche. "
            "Practices in the Ati Yoga / Dzogchen tradition. Public online practices "
            "include Sunday Chenrezig (10am MST, Zoom), Friday Green Tara (10am, Zoom), "
            "and Saturday Ngondro (10am, Zoom). In-person teachings available. "
            "All levels welcome; no prior experience required."
        ),
    },

    # ── New Orleans, LA ──────────────────────────────────────────────────────
    "nozt": {
        "id": "nozt",
        "name": "New Orleans Zen Temple",
        "tradition": "zen",
        "url": "https://www.neworleanszentemple.org",
        "address": "8338 Oak Street, 2nd Floor",
        "city": "New Orleans",
        "state": "LA",
        "zip": "70118",
        "neighborhood": "Riverbend / Carrollton",
        "lat": 29.9370,
        "lng": -90.1195,
        "description": (
            "New Orleans Zen Temple (American Zen Association) is the oldest Zen center "
            "in New Orleans, founded in 1983 by Robert Livingston Roshi in the lineage of "
            "Master Taisen Deshimaru and the Association Zen Internationale. Moved to its "
            "Oak Street location (above Yes, Yoga) in January 2023. Weekly zazen: Tuesday "
            "evenings at 7pm, Thursday mornings at 6:30am, and Sunday mornings at 10am. "
            "New practitioners should contact noztinfo@gmail.com to register for an intro "
            "session before attending. Some sessions also available via Zoom. Donation-based."
        ),
    },
    "mid_city_zen": {
        "id": "mid_city_zen",
        "name": "Mid City Zen",
        "tradition": "zen",
        "url": "https://midcityzen.org",
        "address": "3248 Castiglione St",
        "city": "New Orleans",
        "state": "LA",
        "zip": "70119",
        "neighborhood": "Mid-City",
        "lat": 29.9634,
        "lng": -90.0888,
        "description": (
            "Mid City Zen is a peer-led Soto Zen community in New Orleans's Mid-City "
            "neighborhood, founded in 2011 in the lineage of Shunryu Suzuki Roshi and the "
            "San Francisco Zen Center. At its Castiglione Street location since 2014. "
            "Regular practice: Mon/Wed/Fri morning zazen at 8am (in-person + Zoom); "
            "Sunday Program at 9:30am — chanting, zazen, dharma study; Beginner's "
            "Instruction 2nd/4th Sundays at 8:45am; first-Sunday half-day sits. "
            "Special programs: Queer Zen, Sober Zen, seasonal retreats. Drop-in welcome; "
            "dana basis."
        ),
    },
    "kmc_tampa_bay": {
        "id": "kmc_tampa_bay",
        "name": "Kadampa Meditation Center Tampa Bay",
        "tradition": "tibetan",
        "url": "https://meditationintampabay.org",
        "address": "201 6th Ave S",
        "city": "Safety Harbor",
        "state": "FL",
        "zip": "34695",
        "neighborhood": "Safety Harbor",
        "lat": 27.9869,
        "lng": -82.6932,
        "description": (
            "Kadampa Meditation Center Tampa Bay is a New Kadampa Tradition (NKT-IKBU) "
            "Tibetan Buddhist center in Safety Harbor, serving the greater Tampa Bay metro. "
            "Weekly drop-in classes include Sunday 'Meditations for World Peace' (10–11:15am), "
            "Tuesday General Program (10–11am), and Thursday General Program (7–8:15pm). "
            "All sessions include guided meditation and Buddhist teachings. Branch classes "
            "held throughout Tampa Bay. Free or by donation for new students."
        ),
    },
    "clear_water_zen": {
        "id": "clear_water_zen",
        "name": "Clear Water Zen Center",
        "tradition": "zen",
        "url": "https://www.clearwaterzencenter.org",
        "address": "2476 Nursery Rd",
        "city": "Clearwater",
        "state": "FL",
        "zip": "33764",
        "neighborhood": "South Clearwater",
        "lat": 27.9328,
        "lng": -82.7555,
        "description": (
            "Clear Water Zen Center is a non-sectarian Zen meditation community in Clearwater, "
            "founded in the 1980s by Ken Rosen. Weekly sits open to all: Sunday 9:30am–11:30am "
            "(formal zazen rounds with dharma talk), Monday 7–8pm (open meditation), Wednesday "
            "6:45pm (beginner class with instruction), and Friday 7–8pm (open meditation). "
            "Periodic zazenkai Saturdays and multi-day mini sesshin. Drop-in welcome; "
            "no experience needed. Free; donations appreciated."
        ),
    },
    "fcm_tampa": {
        "id": "fcm_tampa",
        "name": "Florida Community of Mindfulness",
        "tradition": "theravada",
        "url": "https://www.floridamindfulness.org",
        "address": "6501 N Nebraska Ave",
        "city": "Tampa",
        "state": "FL",
        "zip": "33604",
        "neighborhood": "Seminole Heights",
        "lat": 27.9987,
        "lng": -82.4530,
        "description": (
            "The Florida Community of Mindfulness (FCM) is a contemplative community in the "
            "Plum Village tradition of Thich Nhat Hanh, led by teacher Fred Eppsteiner. "
            "Located in the Seminole Heights neighborhood of Tampa. Regular practice: daily "
            "Morning Meditation (7–8am, in-person and online) and Sunday Meditation and Dharma "
            "Talk (9:30–11:30am, in-person and online). Also hosts Mindful Yoga, Qigong, "
            "Meditation in Recovery, Days of Mindfulness, and extended retreats. "
            "Open to all; sliding scale fees for special programs."
        ),
    },
    "shambhala_stpete": {
        "id": "shambhala_stpete",
        "name": "Shambhala Meditation Center of St. Petersburg",
        "tradition": "tibetan",
        "url": "https://stpetersburg.shambhala.org",
        "address": "5901 Haines Rd N",
        "city": "St. Petersburg",
        "state": "FL",
        "zip": "33714",
        "neighborhood": "North St. Petersburg",
        "lat": 27.8284,
        "lng": -82.6788,
        "description": (
            "Shambhala Meditation Center of St. Petersburg is one of five Shambhala Florida "
            "centers, in the Chögyam Trungpa Rinpoche lineage. Regular offerings include "
            "Sunday Community Practice (10am–noon, in-person sitting and walking meditation "
            "with instruction at 11am and discussion) and Tuesday Evening Contemplations "
            "(7–8pm, Zoom only). First Sunday monthly: 'Learn to Meditate' intro class "
            "(9am–noon). Also hosts Heart of Recovery and Shambhala Training weekends. "
            "Drop-in welcome; no experience required."
        ),
    },

    # -----------------------------------------------------------------------
    # Charlotte, NC
    # -----------------------------------------------------------------------

    "charlotte_vihara": {
        "id": "charlotte_vihara",
        "name": "Charlotte Buddhist Vihara",
        "tradition": "theravada",
        "url": "https://www.charlottebuddhistvihara.org",
        "address": "3423 Stonehaven Dr",
        "city": "Charlotte",
        "state": "NC",
        "zip": "28215",
        "neighborhood": "Northeast Charlotte",
        "lat": 35.2379,
        "lng": -80.7626,
        "description": (
            "Charlotte Buddhist Vihara is a Theravada Buddhist center led by Ayya Sudhamma, "
            "one of the first fully ordained Theravada bhikkhunis (nuns) in the West. "
            "Weekly offerings include Tuesday 'Evening of Personal Growth' (6pm, talk and "
            "meditation, hybrid), Wednesday Meditation (10:30am, hybrid), Thursday "
            "'Meditation for Awakening' (7pm, talk and meditation, hybrid), and Saturday "
            "'Buddhist Teachings' (2pm, hybrid). All sessions include guided meditation "
            "and Dhamma discussion. Drop-in welcome; donations appreciated."
        ),
    },
    "imcc": {
        "id": "imcc",
        "name": "Insight Meditation Community of Charlotte",
        "tradition": "theravada",
        "url": "https://www.imccharlotte.org",
        "address": "3900 Park Road",
        "city": "Charlotte",
        "state": "NC",
        "zip": "28209",
        "neighborhood": "South Charlotte / Park Road",
        "lat": 35.1870,
        "lng": -80.8565,
        "description": (
            "The Insight Meditation Community of Charlotte (IMCC) is a Theravada / Vipassana "
            "sangha founded in 2009, meeting at Park Road Baptist Church. Offerings include "
            "Tuesday noon Dharma teaching and silent meditation (Zoom), Wednesday 7pm "
            "newcomer instruction (in-person) and 7:30pm silent meditation with Dharma "
            "talk (hybrid). Drop-in welcome; dana basis."
        ),
    },
    "kmc_nc": {
        "id": "kmc_nc",
        "name": "Kadampa Meditation Center North Carolina",
        "tradition": "tibetan",
        "url": "https://www.meditationcharlotte.org",
        "address": "528 East Blvd",
        "city": "Charlotte",
        "state": "NC",
        "zip": "28203",
        "neighborhood": "Dilworth",
        "lat": 35.2153,
        "lng": -80.8422,
        "description": (
            "Kadampa Meditation Center North Carolina (KMC NC) is a New Kadampa Tradition "
            "(NKT-IKBU) Tibetan Buddhist center in Charlotte's Dilworth neighborhood. "
            "Weekly drop-in classes with guided meditation and Buddhist teachings: Sunday "
            "9:30am, Tuesday 5pm, Wednesday 5pm, Thursday 5pm, Saturday 10am. Also hosts "
            "Foundation Program and special events. All welcome; no experience required."
        ),
    },
    "ccm_charlotte": {
        "id": "ccm_charlotte",
        "name": "Charlotte Community of Mindfulness",
        "tradition": "zen",
        "url": "https://www.charlottemindfulness.org",
        "address": "1931 Selwyn Ave",
        "city": "Charlotte",
        "state": "NC",
        "zip": "28207",
        "neighborhood": "Myers Park",
        "lat": 35.2025,
        "lng": -80.8400,
        "description": (
            "The Charlotte Community of Mindfulness (CCM) is one of the oldest Plum Village "
            "sanghas in the Southeast, founded in 1993 in the tradition of Thich Nhat Hanh. "
            "Meets at Myers Park Baptist Church. Sunday Morning Sangha (8:30–10am) includes "
            "sitting meditation, walking meditation, Dharma reading, and sharing circle "
            "(in-person and Zoom). Last Sunday: Recitation ceremony. Free; donations welcomed."
        ),
    },
    # ── Honolulu, HI ─────────────────────────────────────────────────────────
    "diamond_sangha_honolulu": {
        "id": "diamond_sangha_honolulu",
        "name": "Honolulu Diamond Sangha",
        "tradition": "zen",
        "url": "https://www.diamondsangha.org",
        "address": "2747 Waiomao Road",
        "city": "Honolulu",
        "state": "HI",
        "zip": "96816",
        "neighborhood": "Palolo",
        "lat": 21.3033,
        "lng": -157.8018,
        "description": (
            "Honolulu Diamond Sangha (Ko Ko An Zendo) is one of the most historically "
            "significant Zen communities in Hawaii, founded in the lineage of Robert Aitken "
            "Roshi — a founder of engaged Buddhism in the West and co-founder of the "
            "international Diamond Sangha network. Situated in Palolo Valley, the zendo "
            "offers early morning zazen Mon–Fri, evening sitting on Wednesdays, and Sunday "
            "morning practice. Newcomers attend a one-time orientation (1st Saturday, 9am–noon); "
            "regular students sit freely thereafter."
        ),
    },
    "soto_mission_honolulu": {
        "id": "soto_mission_honolulu",
        "name": "Soto Mission of Hawaii",
        "tradition": "zen",
        "url": "https://www.sotomission.org",
        "address": "1708 Nuuanu Avenue",
        "city": "Honolulu",
        "state": "HI",
        "zip": "96817",
        "neighborhood": "Nuuanu",
        "lat": 21.3219,
        "lng": -157.8431,
        "description": (
            "Soto Mission of Hawaii (Shoboji) is a Soto Zen temple on Nuuanu Avenue in "
            "downtown Honolulu. One of the oldest Japanese-lineage Zen communities in Hawaii. "
            "Morning zazen is explicitly open to the public on Mondays, Wednesdays, and Fridays "
            "at 6:30 AM — no reservation required, just arrive five minutes early in comfortable "
            "clothes. Free (donations appreciated). Sunday service at 9:30 AM. Welcoming to "
            "complete beginners."
        ),
    },
    "bodhi_tree_honolulu": {
        "id": "bodhi_tree_honolulu",
        "name": "Bodhi Tree Dharma Center",
        "tradition": "theravada",
        "url": "https://www.bodhitreehawaii.com",
        "address": "654A N. Judd Street",
        "city": "Honolulu",
        "state": "HI",
        "zip": "96817",
        "neighborhood": "Palama",
        "lat": 21.3179,
        "lng": -157.8443,
        "description": (
            "Bodhi Tree Dharma Center is a multi-tradition meditation hub in Honolulu's "
            "Palama neighborhood, hosting several regular sanghas including Vipassana "
            "meditation, the Honolulu Mindfulness Community (Plum Village / Thich Nhat Hanh "
            "lineage), and a Stillness & Awakenings practice group. Classes run Monday through "
            "Saturday. Donation-based, beginner-friendly."
        ),
    },
    "aloha_sangha_honolulu": {
        "id": "aloha_sangha_honolulu",
        "name": "Aloha Sangha",
        "tradition": "theravada",
        "url": "https://www.alohasangha.com",
        "address": "2439 Holomua Place",
        "city": "Honolulu",
        "state": "HI",
        "zip": "96816",
        "neighborhood": "Palolo Valley",
        "lat": 21.2989,
        "lng": -157.7997,
        "description": (
            "Aloha Sangha is a small, donation-based Theravada / Insight Meditation community "
            "in Palolo Valley, operating since 1998. Thursday evening sits (6–7:30 PM) combine "
            "qigong, two 25-minute seated sessions, a short dharma talk, and Q&A. "
            "Beginner-friendly; no meditation experience required. Located in a residential "
            "setting in upper Palolo Valley."
        ),
    },
    # ── Rochester, NY ─────────────────────────────────────────────────────────
    "rzc": {
        "id": "rzc",
        "name": "Rochester Zen Center",
        "tradition": "zen",
        "url": "https://www.rzc.org",
        "address": "7 Arnold Park",
        "city": "Rochester",
        "state": "NY",
        "zip": "14607",
        "neighborhood": "Park Avenue",
        "lat": 43.1596,
        "lng": -77.5825,
        "description": (
            "The Rochester Zen Center is one of the most historically significant Zen "
            "communities in North America. Founded in 1966 by Philip Kapleau Roshi — "
            "author of The Three Pillars of Zen and one of the first Western teachers "
            "authorized in the Zen tradition — RZC has shaped generations of Western "
            "practitioners and teachers. Sitting practice is rigorous and formal: "
            "zazen, kinhin, chanting, and dokusan (individual teacher meetings). Morning "
            "sits run Tuesday through Friday at 6 AM; evening sits Monday and Thursday "
            "at 7 PM; Saturday at 6:30 AM; Sunday program at 8:30 AM with zazen and a "
            "Dharma talk. Drop-in students are welcome at most sits — newcomers should "
            "contact the center for orientation. RZC also stewards Chapin Mill Retreat "
            "Center, a 135-acre rural property near Batavia, NY."
        ),
    },
    "endless_path_zendo": {
        "id": "endless_path_zendo",
        "name": "Endless Path Zendo",
        "tradition": "zen",
        "url": "https://www.endlesspathzendo.org",
        "address": "56 Brighton Street",
        "city": "Rochester",
        "state": "NY",
        "zip": "14607",
        "neighborhood": "Swillburg",
        "lat": 43.1540,
        "lng": -77.5870,
        "description": (
            "Endless Path Zendo is a small Zen community in Rochester led by Roshi Rafe "
            "Martin — a Dharma heir trained under both Philip Kapleau Roshi (Rochester "
            "Zen Center) and Robert Aitken Roshi (Diamond Sangha). Formal zazen with "
            "dokusan offered Tuesday and Wednesday mornings and evenings, Monday evenings "
            "(informal), and Saturday mornings. First-time visitors join Tuesday evening "
            "at 6:15 PM for orientation. Monthly sesshin, hybrid in-person and Zoom."
        ),
    },
    "dharma_refuge_rochester": {
        "id": "dharma_refuge_rochester",
        "name": "Dharma Refuge",
        "tradition": "tibetan",
        "url": "https://www.dharmarefuge.com",
        "address": "1124 Culver Road",
        "city": "Rochester",
        "state": "NY",
        "zip": "14609",
        "neighborhood": "Culver-University",
        "lat": 43.1647,
        "lng": -77.5604,
        "description": (
            "Dharma Refuge is a Rochester meditation community inspired by the teachings "
            "of Anam Thubten Rinpoche and Pema Chodron's Lojong tradition. Hybrid "
            "in-person (Covenant United Methodist Church) and Zoom. Meetings rotate "
            "between guided sitting, video teachings, and book discussion. Wednesday "
            "evenings 7–8:15 PM; Saturday mornings 10–11:30 AM. Donation-based, "
            "drop-in welcome. All traditions and backgrounds welcome."
        ),
    },
    # ── Louisville, KY — Phase 3 (heartbeat 46) ──────────────────────────────
    "louisville_zen_center": {
        "id": "louisville_zen_center",
        "name": "Louisville Zen Center",
        "tradition": "zen",
        "url": "https://www.louisvillezen.org",
        "address": "917 Rosemary Drive",
        "city": "Louisville",
        "state": "KY",
        "zip": "40205",
        "lat": 38.2355,
        "lng": -85.7116,
        "neighborhood": "Highlands / Tyler Park",
        "bio": (
            "Louisville Zen Center is a Rinzai-Soto Zen community in the lineage of "
            "Rochester Zen Center (Philip Kapleau Roshi). Sits are held at two "
            "Louisville locations: 917 Rosemary Dr (Tuesday evenings) and Infinite "
            "Bliss Yoga at 1507 Bardstown Rd (Sunday evenings). Both sits run "
            "6:30–8pm, hybrid in-person and Zoom. Newcomer orientation offered at "
            "6pm before Tuesday's sit. Drop-in welcome; donation-based."
        ),
    },
    "omz_louisville": {
        "id": "omz_louisville",
        "name": "Open Mind Zen Louisville",
        "tradition": "zen",
        "url": "https://www.omzlouisville.com",
        "address": "1013 Bardstown Road",
        "city": "Louisville",
        "state": "KY",
        "zip": "40204",
        "lat": 38.2253,
        "lng": -85.7212,
        "neighborhood": "Highlands / Bardstown Road",
        "bio": (
            "Open Mind Zen Louisville is a lay Zen community in the White Plum Asanga "
            "lineage, meeting at the Garner Large art space on Bardstown Road. "
            "Saturday Morning Meditation (10:30am–noon): in-person zazen + Dharma "
            "talk, hybrid Zoom available. Daily morning Zoom zazen (7–8am) drop-in. "
            "Part of the Open Mind Zen network. Beginner-friendly, no registration required."
        ),
    },
    "sangha_lou": {
        "id": "sangha_lou",
        "name": "Louisville Community of Mindful Living (Sangha Lou)",
        "tradition": "zen",
        "url": "https://www.sanghalou.org",
        "address": "115 S Ewing Avenue",
        "city": "Louisville",
        "state": "KY",
        "zip": "40206",
        "lat": 38.2322,
        "lng": -85.7069,
        "neighborhood": "Crescent Hill",
        "bio": (
            "Louisville Community of Mindful Living (Sangha Lou) practices in the "
            "tradition of Thich Nhat Hanh and Plum Village. Sunday gatherings "
            "(10am–noon) include guided sitting, walking meditation, dharma sharing, "
            "and discussion — hybrid in-person and Zoom. Open to all regardless of "
            "background. Emphasis on applied mindfulness and engaged Buddhism."
        ),
    },
    "louisville_vipassana_community": {
        "id": "louisville_vipassana_community",
        "name": "Louisville Vipassana Community",
        "tradition": "theravada",
        "url": "http://www.louisville-vipassana-community.org",
        "address": "2231 Payne Street",
        "city": "Louisville",
        "state": "KY",
        "zip": "40206",
        "lat": 38.2504,
        "lng": -85.7105,
        "neighborhood": "Clifton",
        "bio": (
            "Louisville Vipassana Community offers weekly Insight Meditation gatherings "
            "in the IMS / Spirit Rock tradition. Monday Evening Meditation (6:30–8pm) "
            "meets at Clifton Unitarian Universalist Church — guided sitting, walking "
            "meditation, dharma talk, and discussion. Hybrid in-person + Zoom. "
            "Also Tuesday and Wednesday morning Zoom-only sits (7:30–8:05am). "
            "Drop-in welcome; donation-based."
        ),
    },
    "drepung_gomang_louisville": {
        "id": "drepung_gomang_louisville",
        "name": "Drepung Gomang Center for Engaging Compassion",
        "tradition": "tibetan",
        "url": "https://www.drepunggomangusa.org",
        "address": "411 N Hubbards Lane",
        "city": "Louisville",
        "state": "KY",
        "zip": "40207",
        "lat": 38.2632,
        "lng": -85.6900,
        "neighborhood": "St. Matthews",
        "bio": (
            "Drepung Gomang Center for Engaging Compassion (DGCEC) is the Louisville "
            "branch of Drepung Gomang monastery — one of the three great Gelugpa "
            "monasteries of Tibet, re-established in South India after 1959. Resident "
            "Geshe offers Tibetan Buddhist teachings and community practice. Weekly "
            "Wednesday Noontime Meditation (12:10–12:40pm) and Wednesday Evening "
            "Community Meditation with chanting and prayers (7–8pm). All sessions "
            "open to the public; no prior experience needed."
        ),
    },
    "kmpc_louisville": {
        "id": "kmpc_louisville",
        "name": "Kentucky Meditation Peace Center",
        "tradition": "theravada",
        "url": "https://kmpc.co",
        "address": "4815 Manslick Road",
        "city": "Louisville",
        "state": "KY",
        "zip": "40216",
        "lat": 38.1755,
        "lng": -85.8014,
        "neighborhood": "Pleasure Ridge Park / SW Jefferson",
        "bio": (
            "Kentucky Meditation Peace Center and Buddhist Vihara (KMPC) is a "
            "Theravada Buddhist center in southwest Louisville with resident monks "
            "teaching Vipassana insight meditation. Weekly group meditation: Monday "
            "and Wednesday evenings (7–8:30pm), in-person. Guided meditation for all "
            "levels — beginners explicitly welcome. Also operates as Kentucky "
            "Meditation Center and Buddhist Vihara (KMCBV) at the same address."
        ),
    },
    # ── Providence, RI — Phase 3 (heartbeat 47) ───────────────────────────────
    "pzc": {
        "id": "pzc",
        "name": "Providence Zen Center",
        "tradition": "zen",
        "url": "https://providencezen.org",
        "address": "99 Pound Road",
        "city": "Cumberland",
        "state": "RI",
        "zip": "02864",
        "lat": 41.9728,
        "lng": -71.4300,
        "neighborhood": "Cumberland",
        "bio": (
            "Providence Zen Center is the founding temple of the Kwan Um School of Zen "
            "in the West, established in 1972 by Korean master Seung Sahn Sunim. One of "
            "the most active residential Zen centers in North America, PZC offers daily "
            "formal practice (108 bows, chanting, zazen) alongside public programs. The "
            "Sunday Dharma Program (9–11 AM) includes beginner instruction, sitting, "
            "walking, and a Dharma talk — drop-ins welcome. Wednesday evenings feature a "
            "community dinner followed by meditation instruction and chanting. A satellite "
            "West Side Zen Group meets in Providence on Fridays. Intensive retreats "
            "(Kyol Che, YMJJ) offered throughout the year. Located in Cumberland, RI, "
            "about 15 miles north of downtown Providence."
        ),
    },
    "akbc_providence": {
        "id": "akbc_providence",
        "name": "Atisha Kadampa Buddhist Center",
        "tradition": "tibetan",
        "url": "https://meditationinrhodeisland.org",
        "address": "339 Ives Street",
        "city": "Providence",
        "state": "RI",
        "zip": "02906",
        "lat": 41.8198,
        "lng": -71.3955,
        "neighborhood": "Fox Point",
        "bio": (
            "Atisha Kadampa Buddhist Center (AKBC) is Rhode Island's New Kadampa "
            "Tradition (NKT) center in Providence's Fox Point neighborhood. Weekly "
            "programs include a Sunday morning class (11 AM–12:15 PM), lunchtime sits "
            "on Mondays and Thursdays (12:15–12:45 PM), and a Wednesday evening class "
            "(6–7:30 PM). All classes combine guided meditation with Buddhist teachings "
            "in the Kadampa style. Beginners welcome; AKBC also runs a satellite group "
            "in Little Compton, RI."
        ),
    },
    "imcp": {
        "id": "imcp",
        "name": "Insight Meditation Community of Providence",
        "tradition": "theravada",
        "url": "https://www.insightprovidence.org",
        "address": "354 Broadway",
        "city": "Providence",
        "state": "RI",
        "zip": "02909",
        "lat": 41.8220,
        "lng": -71.4272,
        "neighborhood": "Broadway / West End",
        "bio": (
            "The Insight Meditation Community of Providence (IMCP) is a "
            "practitioner-led Vipassana sangha meeting the 1st and 3rd Thursday of "
            "each month. Evenings include 40 minutes of silent sitting, a Dharma "
            "reading, and a discussion circle. Rooted in the Theravada/Insight "
            "tradition, affiliated with the Insight Meditation Society and the Open "
            "Sangha Foundation. Drop-in, donation-based."
        ),
    },
    "insight_pvd": {
        "id": "insight_pvd",
        "name": "Insight Meditation Sangha Providence",
        "tradition": "theravada",
        "url": "https://www.insightpvd.com",
        "address": "27 Sims Avenue",
        "city": "Providence",
        "state": "RI",
        "zip": "02909",
        "lat": 41.8164,
        "lng": -71.4256,
        "neighborhood": "West End",
        "bio": (
            "Insight Meditation Sangha Providence is a Vipassana community in "
            "Providence's West End offering weekly Wednesday evening meditation. "
            "Sitting practice in the Insight/Theravada tradition; dharma study and "
            "community discussion also offered. Drop-in friendly, donation-based. "
            "Periodic retreats and practice groups throughout the year."
        ),
    },
    "ricm_radiant_bell": {
        "id": "ricm_radiant_bell",
        "name": "RI Community of Mindfulness – Radiant Bell Sangha",
        "tradition": "zen",
        "url": "https://www.mindfulnessri.org",
        "address": "5 Bell Street",
        "city": "Providence",
        "state": "RI",
        "zip": "02909",
        "lat": 41.8248,
        "lng": -71.4290,
        "neighborhood": "College Hill / Wayland Square",
        "bio": (
            "The Radiant Bell Sangha is part of the Rhode Island Community of "
            "Mindfulness (RICM), a network of Plum Village–tradition sanghas inspired "
            "by Thich Nhat Hanh. Saturday morning gatherings (8–9:30 AM) at Bell "
            "Street Chapel include sitting meditation, walking meditation, and a "
            "Dharma talk or reading. Free and open to all; beginners welcome."
        ),
    },
    "kmc_indianapolis": {
        "id": "kmc_indianapolis",
        "name": "Kadampa Meditation Center Indianapolis",
        "tradition": "tibetan",
        "url": "https://www.meditation-indianapolis.org",
        "address": "4010 W 86th Street, Suite C",
        "city": "Indianapolis",
        "state": "IN",
        "zip": "46268",
        "lat": 39.9080,
        "lng": -86.2012,
        "neighborhood": "NW Indianapolis / North Willow",
        "bio": (
            "Kadampa Meditation Center Indianapolis (Dromtonpa KMC) is Indiana's "
            "New Kadampa Tradition (NKT) center, founded in 1998 — one of the oldest "
            "KMC centers in the US Midwest. Weekly public classes: Sunday General "
            "Program (11 AM–12:15 PM), Thursday Evening Meditation (6–7 PM), and "
            "Friday Morning Meditation (10–11:15 AM). All classes combine guided "
            "meditation with Buddhist teachings in the Kadampa style. Drop-in "
            "welcome; suggested donation ~$12. Located in northwest Indianapolis."
        ),
    },
    "indianapolis_zen_center": {
        "id": "indianapolis_zen_center",
        "name": "Indianapolis Zen Center",
        "tradition": "zen",
        "url": "https://www.indyzen.org",
        "address": "3703 N. Washington Boulevard",
        "city": "Indianapolis",
        "state": "IN",
        "zip": "46205",
        "lat": 39.8373,
        "lng": -86.1569,
        "neighborhood": "Meridian-Kessler",
        "bio": (
            "The Indianapolis Zen Center has offered Korean Zen practice in central "
            "Indiana since 1991, as a member of the Kwan Um School of Zen (Seung Sahn "
            "lineage). Evening sits Monday and Wednesday (7–8:30 PM) include two "
            "25-minute sitting periods with walking meditation. Morning practice "
            "Monday, Wednesday, and Friday (6:45–7:15 AM) combines sitting with a "
            "brief reading and discussion. Saturday mornings (9:30–10:30 AM) include "
            "chanting and sitting/walking. All sessions hybrid in-person + Zoom. "
            "Monthly retreat 2nd Saturday. Drop-in, no charge."
        ),
    },
    "okbv": {
        "id": "okbv",
        "name": "Oklahoma Buddhist Vihara",
        "tradition": "theravada",
        "url": "https://okbv.org",
        "address": "4820 N Portland Ave",
        "city": "Oklahoma City",
        "state": "OK",
        "zip": "73112",
        "lat": 35.5005,
        "lng": -97.5263,
        "neighborhood": "Nichols Hills area / Uptown OKC",
        "bio": (
            "The Oklahoma Buddhist Vihara (OKBV) is a Theravada monastery in central "
            "Oklahoma City, guided by resident monastics trained in the Theravada "
            "tradition but welcoming practitioners of all backgrounds. Three weekly "
            "public sits: Wednesday Silent Meditation (6–7 PM, in-person), Saturday "
            "Pali Chanting and Meditation (6–7 PM, in-person), and Sunday Guided "
            "Meditation and Discussion (5–6 PM, hybrid in-person + Google Meet — "
            "30 min guided sit + 30 min dharma discussion). Free; donations welcome."
        ),
    },
    "buddha_mind_okc": {
        "id": "buddha_mind_okc",
        "name": "Buddha Mind Monastery",
        "tradition": "zen",
        "url": "https://www.ctbuddhamind.org",
        "address": "5800 S Anderson Rd",
        "city": "Oklahoma City",
        "state": "OK",
        "zip": "73150",
        "lat": 35.3908,
        "lng": -97.4218,
        "neighborhood": "SE Oklahoma City",
        "bio": (
            "Buddha Mind Monastery (佛心禪寺) is a Chinese Mahayana Zen monastery "
            "in southeast Oklahoma City, founded in 2004. It offers free one-hour "
            "guided meditation every Sunday from 3–4 PM, open to all regardless of "
            "background or experience. The monastery also hosts monthly dharma "
            "ceremonies and half-day meditation retreats. Situated on eleven acres; "
            "open daily 2–5 PM for visits."
        ),
    },
    "tmbcc": {
        "id": "tmbcc",
        "name": "Tibetan Mongolian Buddhist Cultural Center",
        "tradition": "tibetan",
        "url": "https://tmbcc.org",
        "address": "3655 S Snoddy Road",
        "city": "Bloomington",
        "state": "IN",
        "zip": "47401",
        "lat": 39.1198,
        "lng": -86.5097,
        "neighborhood": "South Bloomington",
        "bio": (
            "The Tibetan Mongolian Buddhist Cultural Center (TMBCC) is one of the "
            "most significant Tibetan Buddhist institutions in North America. Founded "
            "by Thubten Norbu — elder brother of His Holiness the 14th Dalai Lama — "
            "on 108 acres in southern Bloomington, the campus includes the Kumbum "
            "Chamtse Ling temple and Kumbum West monastery. Three weekly public "
            "meditation programs: Monday Group Meditation (6:30–7:30 PM), Wednesday "
            "Open Meditation (6–7 PM, open to anyone wishing to sit in stillness, "
            "prayer, or practice), and Sunday Buddhist Philosophy Teachings "
            "(10:30 AM–noon). Free and open to all."
        ),
    },
    "kmc_bloomington": {
        "id": "kmc_bloomington",
        "name": "Kadampa Meditation Center Bloomington",
        "tradition": "tibetan",
        "url": "https://www.meditationinbloomington.org",
        "address": "234 N. Morton Street",
        "city": "Bloomington",
        "state": "IN",
        "zip": "47404",
        "lat": 39.1662,
        "lng": -86.5340,
        "neighborhood": "Downtown Bloomington",
        "bio": (
            "Kadampa Meditation Center Bloomington (KMC Bloomington) is a New "
            "Kadampa Tradition (NKT) center offering modern Tibetan Buddhist "
            "teachings and guided meditation in downtown Bloomington, steps from "
            "Indiana University. Three weekly drop-in public classes: Tuesday "
            "Evening (6–7:15 PM), Wednesday Lunchtime (12:15–12:45 PM), and "
            "Sunday General Program (11 AM–12:15 PM). Classes combine guided "
            "meditation with Buddhist teachings. Drop-in welcome; suggested donation."
        ),
    },
    "open_mind_zen_indiana": {
        "id": "open_mind_zen_indiana",
        "name": "Open Mind Zen Indiana",
        "tradition": "zen",
        "url": "https://openmindzenbloomington.org",
        "address": "3820 E. Moores Pike",
        "city": "Bloomington",
        "state": "IN",
        "zip": "47402",
        "lat": 39.1539,
        "lng": -86.4839,
        "neighborhood": "East Bloomington / Friends Meeting House",
        "bio": (
            "Open Mind Zen Indiana (OMZI) is a contemporary Zen sangha meeting "
            "weekly at the Bloomington Friends Meeting House. Practice includes "
            "zazen sitting and walking meditation, koan study, dharma talks, "
            "workshops, and retreats. Monday evening sits (7–9 PM) are open to "
            "all; no experience required. OMZI is a 501(c)(3) nonprofit affiliated "
            "with the Open Mind Zen tradition."
        ),
    },
    "hoosier_heartland_shambhala": {
        "id": "hoosier_heartland_shambhala",
        "name": "Hoosier Heartland Shambhala Meditation Group",
        "tradition": "tibetan",
        "url": "https://hhsmg.shambhala.org",
        "address": "2120 N Fee Lane",
        "city": "Bloomington",
        "state": "IN",
        "zip": "47408",
        "lat": 39.1810,
        "lng": -86.5282,
        "neighborhood": "North Bloomington / UU Church",
        "bio": (
            "The Hoosier Heartland Shambhala Meditation Group (HHSMG) offers three "
            "weekly open sits in Bloomington, requiring no prior experience. Monday "
            "Open Sit (noon–1 PM) at the Unitarian Universalist Church, 2120 N Fee "
            "Ln — hybrid in-person + Zoom. Thursday Evening Sit (6–7:30 PM) at the "
            "Tibetan Mongolian Buddhist Cultural Center (TMBCC). Friday Night Sit "
            "(6–7:30 PM, instruction 6–6:30 PM) at the Center for Wholism, 2401 N. "
            "Walnut St. All sits are free and open to the public. Part of the "
            "international Shambhala Buddhist community (Chögyam Trungpa lineage)."
        ),
    },
    "cleveland_shambhala": {
        "id": "cleveland_shambhala",
        "name": "Cleveland Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://cleveland.shambhala.org",
        "address": "17309 Madison Avenue",
        "city": "Cleveland",
        "state": "OH",
        "zip": "44107",
        "lat": 41.4815,
        "lng": -81.8025,
        "neighborhood": "Lakewood",
        "bio": (
            "The Cleveland Shambhala Meditation Center offers authentic meditation "
            "instruction rooted in the Tibetan Buddhist tradition brought to the West "
            "by Chögyam Trungpa Rinpoche. Located in the Lakewood neighborhood west of "
            "Cleveland, the center hosts three weekly open sits: Sunday Morning Sit "
            "(10–11 AM), Tuesday Evening Sit (7–8 PM), and Wednesday Morning Sit "
            "(10–11 AM). All sessions include alternating sitting and walking meditation "
            "periods. No experience required; walk-in welcome. Part of the "
            "international Shambhala community."
        ),
    },
    "imc_cleveland": {
        "id": "imc_cleveland",
        "name": "Insight Meditation Cleveland",
        "tradition": "vipassana",
        "url": "https://imcleveland.org",
        "address": "21600 Shaker Boulevard",
        "city": "Cleveland",
        "state": "OH",
        "zip": "44122",
        "lat": 41.4726,
        "lng": -81.5575,
        "neighborhood": "Shaker Heights / First Unitarian Church",
        "bio": (
            "Insight Meditation Cleveland (IMC) offers a network of drop-in sitting "
            "groups throughout Northeast Ohio, rooted in the Theravada/Vipassana "
            "tradition. The flagship Shaker Heights group meets weekly at the First "
            "Unitarian Church of Cleveland (21600 Shaker Blvd) every Thursday "
            "7–8:30 PM. Sessions include guided sitting meditation, walking "
            "meditation, and dharma discussion. No registration required; dana "
            "(donation) based. All levels welcome."
        ),
    },
    "crooked_river_zen": {
        "id": "crooked_river_zen",
        "name": "Crooked River Zen Center",
        "tradition": "zen",
        "url": "https://www.crookedriverzen.org",
        "address": "1813 Wilton Road",
        "city": "Cleveland",
        "state": "OH",
        "zip": "44118",
        "lat": 41.5095,
        "lng": -81.5695,
        "neighborhood": "Cleveland Heights",
        "bio": (
            "Crooked River Zen Center is a Soto Zen community in Cleveland Heights, "
            "affiliated with the Soto Zen Buddhist Association. Teacher Sensei Dean "
            "Williams leads three weekly sits open to all: Tuesday Evening (6–7 PM, "
            "two 15-minute periods with kinhin and chanting), Thursday Evening "
            "(7–8:30 PM, two 25-minute periods with kinhin, chanting, and dharma "
            "talk), and Sunday Morning (9:30–11 AM, two 30-minute periods with "
            "kinhin, chanting, and dharma talk). All sessions available in-person "
            "and via Google Meet. No experience required; drop-in welcome."
        ),
    },
    "cleveland_zazen_group": {
        "id": "cleveland_zazen_group",
        "name": "Cleveland Zazen Group",
        "tradition": "zen",
        "url": "https://www.zencleveland.com",
        "address": "1813 Wilton Road",
        "city": "Cleveland",
        "state": "OH",
        "zip": "44118",
        "lat": 41.5097,
        "lng": -81.5697,
        "neighborhood": "Cleveland Heights",
        "bio": (
            "The Cleveland Zazen Group is one of Northeast Ohio's longest-standing "
            "Zen communities, with over 40 years of continuous practice. Rooted in "
            "the Rinzai–Soto lineage of Philip Kapleau and the Rochester Zen Center, "
            "the group meets twice weekly in Cleveland Heights: Tuesday Evening "
            "(7:30–8:45 PM, two rounds of zazen and kinhin) and Sunday Morning "
            "(9 AM–11 AM or longer, with group instruction, dharma talks, and work "
            "practice). The group shares its space at 1813 Wilton Road with Crooked "
            "River Zen Center. Drop-in welcome; no prior experience necessary."
        ),
    },
    "cloudwater_zendo": {
        "id": "cloudwater_zendo",
        "name": "CloudWater Zendo",
        "tradition": "zen",
        "url": "https://cloudwater.org",
        "address": "4388 W Pleasant Valley Road",
        "city": "Cleveland",
        "state": "OH",
        "zip": "44134",
        "lat": 41.3738,
        "lng": -81.7645,
        "neighborhood": "Parma",
        "bio": (
            "CloudWater Zendo is a Chan Buddhist and Pure Land community affiliated "
            "with the Dragon Flower Ch'an Temples lineage. The zendo hosts weekly "
            "practice sessions open to all: Tuesday Evening (7 PM, two periods of "
            "seated meditation, walking meditation, chanting, and dharma talk) and "
            "Sunday Morning (9:30 AM, group Zen meditation). An introductory class "
            "is offered on the 1st and 3rd Saturday at 11 AM. All are welcome; "
            "no experience required."
        ),
    },
    # ── Madison, WI ────────────────────────────────────────────────────────────
    "shambhala_madison": {
        "id": "shambhala_madison",
        "name": "Shambhala Meditation Center of Madison",
        "tradition": "tibetan",
        "url": "https://madison.shambhala.org",
        "address": "408 S. Baldwin Street",
        "city": "Madison",
        "state": "WI",
        "zip": "53703",
        "lat": 43.0706,
        "lng": -89.3887,
        "neighborhood": "Isthmus / Downtown Madison",
        "bio": (
            "The Shambhala Meditation Center of Madison offers weekly open sits "
            "rooted in the Tibetan Buddhist tradition brought to the West by "
            "Chögyam Trungpa Rinpoche. Located on the Madison Isthmus near the "
            "Capitol, the center hosts Sunday Morning Public Meditation (10 AM–noon) "
            "and Thursday Evening Public Meditation (7–8:30 PM). Both sessions "
            "include alternating sitting and walking meditation periods with "
            "instruction available. No experience required; drop-in welcome. "
            "Part of the international Shambhala community."
        ),
    },
    "kmc_madison": {
        "id": "kmc_madison",
        "name": "Kadampa Meditation Center Madison",
        "tradition": "tibetan",
        "url": "https://www.meditationinmadison.org",
        "address": "1825 S. Park Street",
        "city": "Madison",
        "state": "WI",
        "zip": "53713",
        "lat": 43.0568,
        "lng": -89.4019,
        "neighborhood": "South Madison",
        "bio": (
            "Kadampa Meditation Center Madison (KMC Madison) is Wisconsin's "
            "New Kadampa Tradition (NKT-IKBU) center, offering modern Tibetan "
            "Buddhist teachings and guided meditation at 1825 S. Park Street "
            "in South Madison. Three weekly drop-in public classes: Sunday "
            "Morning Meditation (10–11:15 AM), Wednesday Meditation at Noon "
            "(noon–12:30 PM, $5), and Thursday Buddhist Wisdom for Daily Life "
            "(6:30–7:30 PM). Classes combine guided meditation with Buddhist "
            "philosophy in the Kadampa style. Drop-in welcome; suggested $12/class."
        ),
    },
    "madison_zen_center": {
        "id": "madison_zen_center",
        "name": "Madison Zen Center",
        "tradition": "zen",
        "url": "https://www.madisonzen.org",
        "address": "1820 Jefferson Street",
        "city": "Madison",
        "state": "WI",
        "zip": "53711",
        "lat": 43.0617,
        "lng": -89.3957,
        "neighborhood": "Regent / UW Campus Area",
        "bio": (
            "The Madison Zen Center (MZC) is a lay Zen community affiliated with "
            "the Rochester Zen Center, practicing in the combined Rinzai–Soto "
            "lineage of Philip Kapleau Roshi. Under teacher Sensei Rick Smith, "
            "MZC offers an extensive daily schedule: early morning zazen "
            "Tuesday–Friday (6:30 AM), Monday Evening (7–8:30 PM, three 25-minute "
            "rounds with kinhin and instruction), Wednesday Evening (6:30–8:30 PM), "
            "and the main Sunday Program (8:30–10:30 AM with sitting, chanting, "
            "and dharma talk). Drop-in welcome; all levels. Online via Zoom "
            "available by contacting mzc@madisonzen.org."
        ),
    },
    "snowflower_sangha": {
        "id": "snowflower_sangha",
        "name": "Snowflower Sangha",
        "tradition": "zen",
        "url": "https://snowflower.org",
        "address": "1704 Roberts Court",
        "city": "Madison",
        "state": "WI",
        "zip": "53711",
        "lat": 43.0676,
        "lng": -89.3780,
        "neighborhood": "Vilas / Friends Meetinghouse",
        "bio": (
            "Snowflower Sangha is Madison's Plum Village community, practicing "
            "in the tradition of Thich Nhat Hanh. The sangha meets multiple "
            "times weekly across Madison. Tuesday Evening (7–8:30 PM) is held "
            "hybrid at the Friends Meetinghouse (1704 Roberts Court) + Zoom. "
            "Saturday Morning (10–11:30 AM) meets in-person at the Friends "
            "Meetinghouse. Practice includes sitting meditation, walking "
            "meditation, Dharma sharing, and chanting. Open to all; no "
            "experience required. Free; dana welcome."
        ),
    },
    "diamond_way_madison": {
        "id": "diamond_way_madison",
        "name": "Diamond Way Buddhist Center Madison",
        "tradition": "tibetan",
        "url": "https://diamondway.org/madison/",
        "address": "104 King Street, Suite 302",
        "city": "Madison",
        "state": "WI",
        "zip": "53703",
        "lat": 43.0740,
        "lng": -89.3840,
        "neighborhood": "Downtown Madison",
        "bio": (
            "Diamond Way Buddhist Center Madison is a lay Karma Kagyu Tibetan "
            "Buddhist center in downtown Madison, affiliated with Lama Ole "
            "Nydahl's Diamond Way Buddhist Union and the 17th Karmapa Trinley "
            "Thaye Dorje. Two weekly public meditation sessions open to all: "
            "Sunday Evening (7:30 PM) and Wednesday Evening (7:30 PM) — each "
            "featuring a short talk followed by a guided meditation. Located "
            "on the third floor at 104 King Street, near the Capitol Square. "
            "Free; no experience required; no registration needed."
        ),
    },
    # -----------------------------------------------------------------------
    # Connecticut — Hartford / New Haven Phase 3 (heartbeat 53)
    # -----------------------------------------------------------------------
    "new_haven_zen": {
        "id": "new_haven_zen",
        "name": "New Haven Zen Center",
        "tradition": "zen",
        "url": "https://www.newhavenzen.org",
        "address": "193 Mansfield Street",
        "city": "New Haven",
        "state": "CT",
        "zip": "06511",
        "lat": 41.3117,
        "lng": -72.9278,
        "neighborhood": "East Rock",
        "bio": (
            "The New Haven Zen Center (NHZC) is a Kwan Um School of Zen community "
            "founded in 1977, practicing Korean Zen in the lineage of Zen Master "
            "Seungsahn. Located in New Haven's East Rock neighborhood, NHZC offers "
            "two weekly public sitting programs open to all: Wednesday Evening "
            "(7:30 PM — sitting, walking, and chanting; newcomer orientation 2nd "
            "and 4th Wednesdays at 6:30 PM) and Sunday Morning (9 AM — sitting, "
            "walking, and chanting through ~10:50 AM with dharma talk). One of "
            "the oldest and most established Zen centers in New England. Drop-in "
            "welcome; no experience required. Free; dana appreciated."
        ),
    },
    "shambhala_new_haven": {
        "id": "shambhala_new_haven",
        "name": "Shambhala Meditation Center of New Haven",
        "tradition": "tibetan",
        "url": "https://newhaven.shambhala.org",
        "address": "493 Whitney Avenue, 2nd Floor",
        "city": "New Haven",
        "state": "CT",
        "zip": "06511",
        "lat": 41.3238,
        "lng": -72.9303,
        "neighborhood": "East Rock / Whitney Avenue",
        "bio": (
            "The Shambhala Meditation Center of New Haven is part of the international "
            "Shambhala community, rooted in the Tibetan Buddhist teachings of Chögyam "
            "Trungpa Rinpoche and Sakyong Mipham Rinpoche. Located on the second floor "
            "of East Rock Health & Wellness at 493 Whitney Avenue, the center offers "
            "Sunday Morning Open Meditation (9:30–11:30 AM) — alternating sitting and "
            "walking periods with instruction available for newcomers and a dharma talk "
            "on the first Sunday of each month. Open to all; no experience required; "
            "drop-in welcome. Suggested donation."
        ),
    },
    "odiyana_kadampa": {
        "id": "odiyana_kadampa",
        "name": "Odiyana Kadampa Meditation Center",
        "tradition": "tibetan",
        "url": "https://www.meditationinconnecticut.org",
        "address": "450 New London Turnpike",
        "city": "Glastonbury",
        "state": "CT",
        "zip": "06033",
        "lat": 41.7084,
        "lng": -72.5950,
        "neighborhood": "Glastonbury (Hartford suburb)",
        "bio": (
            "Odiyana Kadampa Meditation Center is Connecticut's New Kadampa Tradition "
            "(NKT-IKBU) center, offering modern Tibetan Buddhist teachings and guided "
            "meditation at 450 New London Turnpike in Glastonbury, a suburb of Hartford. "
            "Two weekly drop-in public classes: Sunday Morning (11 AM–12:15 PM, "
            "'Meditation Made Easy') and Thursday Evening (7–8:15 PM). Classes combine "
            "guided meditation with Buddhist philosophy in the Kadampa style and are "
            "open to all levels. Suggested donation $8–12; free for members."
        ),
    },
    "nalandabodhi_ct": {
        "id": "nalandabodhi_ct",
        "name": "Nalandabodhi Connecticut",
        "tradition": "tibetan",
        "url": "https://ct.nalandabodhi.org",
        "address": "3 Barnard Lane, Suite 305",
        "city": "Bloomfield",
        "state": "CT",
        "zip": "06002",
        "lat": 41.8438,
        "lng": -72.7197,
        "neighborhood": "Bloomfield (Hartford suburb)",
        "bio": (
            "Nalandabodhi Connecticut is part of the Nalandabodhi international "
            "sangha founded by Dzogchen Ponlop Rinpoche, practicing in the Kagyu "
            "and Nyingma lineages of Tibetan Buddhism. The Connecticut center meets "
            "at 3 Barnard Lane, Suite 305, Bloomfield (a Hartford suburb), and on "
            "Zoom. Sunday morning program: 10–10:50 AM guided meditation followed "
            "by 11–11:30 AM dharma discussion. Hybrid in-person and Zoom. Open to "
            "all; free; no experience required."
        ),
    },
    "hartford_ktc": {
        "id": "hartford_ktc",
        "name": "Hartford Karma Thegsum Choling",
        "tradition": "tibetan",
        "url": "https://ktchartford.org",
        "address": "157 Elizabeth Street",
        "city": "Hartford",
        "state": "CT",
        "zip": "06105",
        "lat": 41.7627,
        "lng": -72.6990,
        "neighborhood": "West End, Hartford",
        "bio": (
            "Hartford Karma Thegsum Choling (KTC) is a Tibetan Buddhist meditation "
            "center affiliated with Karma Triyana Dharmachakra (KTD Monastery) in "
            "Woodstock, New York — the North American seat of His Holiness the "
            "Gyalwang Karmapa in the Karma Kagyu lineage. Located in Hartford's "
            "West End neighborhood, the center offers a Tuesday Evening practice "
            "and study group (7 PM). Open to all; no experience required; "
            "contact (860) 232-8366 for current schedule and programs."
        ),
    },
    # -----------------------------------------------------------------------
    # Omaha / Lincoln, NE — Phase 3 (heartbeat 54)
    # -----------------------------------------------------------------------
    "nebraska_zen_center": {
        "id": "nebraska_zen_center",
        "name": "Nebraska Zen Center / Heartland Temple",
        "tradition": "zen",
        "url": "https://nebraskazencenter.org",
        "address": "3625 Lafayette Avenue",
        "city": "Omaha",
        "state": "NE",
        "zip": "68131",
        "lat": 41.2613,
        "lng": -96.0013,
        "neighborhood": "Bemis Park / Midtown Omaha",
        "bio": (
            "Nebraska Zen Center (NZC), also known as Heartland Temple, is a Soto "
            "Zen community in the lineage of Dainin Katagiri Roshi, founded in "
            "Omaha in 1975 and one of the oldest Zen centers in the Midwest. "
            "Located at 3625 Lafayette Avenue in Omaha's Bemis Park neighborhood "
            "(since 1992). Sunday Open Zen (10 AM–noon): zazen, kinhin, and dharma "
            "talk with tea; newcomers arrive at 9:15 AM for orientation. Wednesday "
            "Evening (7 PM): two 30-minute zazen periods with kinhin and "
            "Fukanzazengi recitation. Mon–Fri Morning Zazen (6–7:30 AM): in-person "
            "and Zoom, open to all. All programs are by donation; drop-in welcome."
        ),
    },
    "flatwater_collective": {
        "id": "flatwater_collective",
        "name": "Flatwater Collective",
        "tradition": "pluralist",
        "url": "https://www.flatwatercollective.org",
        "address": "1219 Leavenworth Street",
        "city": "Omaha",
        "state": "NE",
        "zip": "68102",
        "lat": 41.2571,
        "lng": -95.9350,
        "neighborhood": "Downtown Omaha",
        "bio": (
            "Flatwater Collective is a non-sectarian, community-focused Buddhist "
            "meditation center in downtown Omaha offering freely given teachings "
            "and a welcoming environment for practitioners of all backgrounds. "
            "Thursday Evening (7–8 PM): 'Meditation Practice and Reflection' — "
            "dharma talk + sitting meditation, beginner-friendly, freely offered. "
            "Sunday Practice (4–5 PM): guided and silent meditation with a "
            "different teacher each week. Also hosts daylong retreats, intro "
            "meditation courses, and dharma study groups. Located at 1219 "
            "Leavenworth Street; dana/donation appreciated."
        ),
    },
    "honey_locust_sangha": {
        "id": "honey_locust_sangha",
        "name": "Honey Locust Sangha",
        "tradition": "pluralist",
        "url": "https://honeylocustsangha.org",
        "address": "7641 Pacific Street",
        "city": "Omaha",
        "state": "NE",
        "zip": "68114",
        "lat": 41.2376,
        "lng": -96.0484,
        "neighborhood": "Midtown / Pacific Street",
        "bio": (
            "Honey Locust Sangha is Omaha's Plum Village community, practicing in "
            "the tradition of Thich Nhat Hanh and the Order of Interbeing. Meets "
            "at The Yoga Path, 7641 Pacific Street. Monday Evening (6:30–8:30 PM): "
            "sitting meditation, walking meditation, and dharma discussion. Friday "
            "Evening (6–7 PM): sitting and walking meditation in noble silence. "
            "First Saturday monthly: Thich Nhat Hanh book study. Zoom available. "
            "All programs free and open to all; no experience required."
        ),
    },
    "lincoln_zen_center": {
        "id": "lincoln_zen_center",
        "name": "Lincoln Zen Center",
        "tradition": "zen",
        "url": "https://www.lincolnzencenter.org",
        "address": "3701 O Street, Suite 204",
        "city": "Lincoln",
        "state": "NE",
        "zip": "68510",
        "lat": 40.8057,
        "lng": -96.6720,
        "neighborhood": "Near South Lincoln",
        "bio": (
            "Lincoln Zen Center is a Soto Zen community in Lincoln, Nebraska "
            "(the state capital, 55 miles southwest of Omaha). Located at 3701 "
            "O Street, Suite 204. Three weekly public sitting programs: Sunday "
            "Morning (10:30 AM–noon — meditation + dharma talk/discussion), "
            "Monday Evening (5:30–6:45 PM — sitting, beginners welcome), and "
            "Wednesday Morning (10:30–11:45 AM). Open to all; no experience "
            "required; drop-in welcome."
        ),
    },
    # -----------------------------------------------------------------------
    # Boise, ID — Phase 3 (heartbeat 55)
    # -----------------------------------------------------------------------
    "boise_zen_center": {
        "id": "boise_zen_center",
        "name": "Boise Zen Center",
        "tradition": "zen",
        "url": "https://www.boisezencenter.org",
        "address": "1524 W. Hays Street, Suite 101a",
        "city": "Boise",
        "state": "ID",
        "zip": "83702",
        "lat": 43.6194,
        "lng": -116.2052,
        "neighborhood": "Downtown Boise",
        "bio": (
            "Boise Zen Center is a Soto Zen community (SZBA member) in downtown "
            "Boise, guided by teacher Jisen Coghlan. Wednesday Morning (7–8:30 AM): "
            "zazen and kinhin, in-person and Zoom. Thursday Evening (6–7:10 PM): "
            "two sitting periods with kinhin, in-person. Saturday Morning "
            "(8–9:30 AM): zazen and kinhin, in-person and Zoom. First Saturday "
            "monthly includes Introduction to Meditation. Drop-in welcome; "
            "donation-based. 501(c)(3) non-profit."
        ),
    },
    "empty_gate_zen_boise": {
        "id": "empty_gate_zen_boise",
        "name": "Empty Gate Zen Center Boise",
        "tradition": "zen",
        "url": "https://bibscenter.org",
        "address": "901 N. 15th Street",
        "city": "Boise",
        "state": "ID",
        "zip": "83702",
        "lat": 43.6218,
        "lng": -116.2118,
        "neighborhood": "North End Boise",
        "bio": (
            "Empty Gate Zen Center Boise is a Kwan Um School of Zen community "
            "(Korean Zen), hosted at the Boise Institute for Buddhist Studies "
            "(BIBS), 901 N. 15th Street. Guiding teacher Jeff Kitzes (Zen Master "
            "Bon Soeng). Mon–Thu Morning (6:30–7:30 AM): sitting and kinhin, "
            "in-person and Zoom. Thursday Evening (7 PM): evening sitting, "
            "in-person and Zoom. Drop-in welcome."
        ),
    },
    "boise_insight_sangha": {
        "id": "boise_insight_sangha",
        "name": "Boise Insight Sangha",
        "tradition": "theravada",
        "url": "https://boiseinsightsangha.wordpress.com",
        "address": "901 N. 15th Street",
        "city": "Boise",
        "state": "ID",
        "zip": "83702",
        "lat": 43.6218,
        "lng": -116.2118,
        "neighborhood": "North End Boise",
        "bio": (
            "Boise Insight Sangha is an Insight Meditation group hosted at the "
            "Boise Institute for Buddhist Studies (BIBS), 901 N. 15th Street. "
            "Tuesday Evening (6–7:30 PM): sitting meditation and dharma discussion. "
            "First Saturday monthly: half-day sitting (9 AM–12:30 PM). "
            "Drop-in welcome; open to all levels."
        ),
    },
    "beginners_mind_sangha_boise": {
        "id": "beginners_mind_sangha_boise",
        "name": "Beginner's Mind Sangha",
        "tradition": "pluralist",
        "url": "https://www.beginnersmindsangha.org",
        "address": "901 N. 15th Street",
        "city": "Boise",
        "state": "ID",
        "zip": "83702",
        "lat": 43.6218,
        "lng": -116.2118,
        "neighborhood": "North End Boise",
        "bio": (
            "Beginner's Mind Sangha is Boise's Plum Village community, practicing "
            "in the tradition of Thich Nhat Hanh and the Order of Interbeing. "
            "Hosted at BIBS, 901 N. 15th Street. Wednesday Evening (7–8:15 PM): "
            "sitting, walking meditation, and dharma sharing. Sunday Morning "
            "(10:15–11:45 AM): sitting and dharma discussion, hybrid (in-person "
            "+ Zoom). Third Sunday includes Three Jewels ceremony; fifth Sunday "
            "is a Day of Mindfulness. Free; open to all."
        ),
    },
    "heart_of_the_dharma_boise": {
        "id": "heart_of_the_dharma_boise",
        "name": "Heart of the Dharma",
        "tradition": "tibetan",
        "url": "https://heartofdharma.org",
        "address": "1627 S. Orchard Street, Suite 200",
        "city": "Boise",
        "state": "ID",
        "zip": "83705",
        "lat": 43.5935,
        "lng": -116.2210,
        "neighborhood": "South Boise",
        "bio": (
            "Heart of the Dharma is a Nyingma Tibetan Buddhist center in Boise, "
            "guided by teacher Dana Marsh (ordained by Anam Thubten Rinpoche). "
            "Located at 1627 S. Orchard Street, Suite 200. Sunday Practice "
            "(11 AM–12:15 PM): in-person and livestream. Tuesday Evening (7 PM): "
            "online/livestream only. Also offers day-long and residential retreats "
            "throughout the year. Dana-based; open to all."
        ),
    },
    # -----------------------------------------------------------------------
    # Spokane, WA — Phase 3 (heartbeat 56)
    # -----------------------------------------------------------------------
    "zen_center_spokane": {
        "id": "zen_center_spokane",
        "name": "Zen Center of Spokane",
        "tradition": "zen",
        "url": "https://zencenterspokane.org",
        "address": "25 W Main Ave, Suite 200",
        "city": "Spokane",
        "state": "WA",
        "zip": "99201",
        "lat": 47.6590,
        "lng": -117.4260,
        "neighborhood": "Downtown Spokane",
        "bio": (
            "Zen Center of Spokane is a Diamond Sangha community (blending Soto "
            "and Rinzai Zen), located in the Saranac Building, 25 W Main Ave, 2nd "
            "floor, Downtown Spokane. Monday Morning (7–7:50 AM): two 25-min "
            "sitting periods, kinhin, and sutra recitation. Wednesday Evening "
            "(7:15–8:15 PM): same format. Saturday Morning (8–9:30 AM): sitting, "
            "kinhin, sutra, and dharma reading. All sessions offered in-person "
            "and on Zoom. Drop-in welcome."
        ),
    },
    "biuc_spokane": {
        "id": "biuc_spokane",
        "name": "Buddhist Institute of Universal Compassion",
        "tradition": "tibetan",
        "url": "https://www.universalcompassion.org",
        "address": "728 E Rich Ave",
        "city": "Spokane",
        "state": "WA",
        "zip": "99207",
        "lat": 47.6608,
        "lng": -117.3812,
        "neighborhood": "East Spokane",
        "bio": (
            "Buddhist Institute of Universal Compassion (BIUC) is a Gelug "
            "Tibetan Buddhist center in Spokane, founded 2017 and led by "
            "Venerable Geshe Thupten Phelgye. Located at 728 E Rich Ave. "
            "Saturday (9:30 AM–12 PM): meditation and teachings. Sunday "
            "(10 AM–12 PM): meditation and teachings. Both sessions offered "
            "in-person and on Zoom (ID: 890 7744 2439). Open to all; dana-based."
        ),
    },
    "padma_ling_spokane": {
        "id": "padma_ling_spokane",
        "name": "Chagdud Gonpa Padma Ling",
        "tradition": "tibetan",
        "url": "https://www.chagdudgonpa.org/centers/padma-ling",
        "address": "1014 W 7th Ave",
        "city": "Spokane",
        "state": "WA",
        "zip": "99204",
        "lat": 47.6496,
        "lng": -117.4273,
        "neighborhood": "South Hill",
        "bio": (
            "Chagdud Gonpa Padma Ling is a Nyingma Tibetan Buddhist center in "
            "Spokane, active since 1990. Resident Lama Inge Zangmo offers "
            "teachings twice weekly; contact padmaling21@gmail.com or "
            "(509) 747-1559 for current schedule. Part of the Chagdud Gonpa "
            "Foundation."
        ),
    },
    # -----------------------------------------------------------------------
    # Fresno, CA — Phase 3 (heartbeat 57)
    # -----------------------------------------------------------------------
    "zen_center_fresno": {
        "id": "zen_center_fresno",
        "name": "Zen Center of Fresno",
        "tradition": "zen",
        "url": "https://zenfresno.org",
        "address": "371 E. Bullard Ave., Suite 102",
        "city": "Fresno",
        "state": "CA",
        "zip": "93710",
        "lat": 36.8240,
        "lng": -119.7965,
        "neighborhood": "Central Fresno",
        "bio": (
            "Zen Center of Fresno is part of the Central Valley Zen Foundation, "
            "in the Soto Zen lineage of Suzuki Roshi and Eihei Dogen. Saturday "
            "mornings (9–11 AM): two 25-minute zazen periods with kinhin, "
            "followed by a dharma talk at 10 AM and closing vows at 11 AM. "
            "Drop-in welcome. Teacher: Soshin Bruce Jewell (transmitted Soto "
            "teacher). Abbess: Myoan Grace Schireson."
        ),
    },
    "fresno_buddhist_temple": {
        "id": "fresno_buddhist_temple",
        "name": "Fresno Buddhist Temple",
        "tradition": "other",
        "url": "https://fresnobuddhisttemple.org",
        "address": "2690 E. Alluvial Ave.",
        "city": "Fresno",
        "state": "CA",
        "zip": "93720",
        "lat": 36.8776,
        "lng": -119.7590,
        "neighborhood": "Northeast Fresno",
        "bio": (
            "Fresno Buddhist Temple (Fresno Betsuin) is a Jodo Shinshu "
            "(Pure Land) temple of the Buddhist Churches of America. Offers "
            "regular public meditation: Sunday Meditation Class (8:30–9:15 AM) "
            "in the Hondo — sitting and walking meditation, open to all. "
            "Thursday Evening Meditation with Rev. Kaz (7–7:45 PM): hybrid "
            "in-person + Zoom (email temple for link). Free; donations welcome."
        ),
    },
    # -----------------------------------------------------------------------
    # Asheville, NC — Phase 3 (heartbeat 58)
    # -----------------------------------------------------------------------
    "zen_center_asheville": {
        "id": "zen_center_asheville",
        "name": "Zen Center of Asheville",
        "tradition": "zen",
        "url": "https://zcasheville.org",
        "address": "227 Edgewood Rd",
        "city": "Asheville",
        "state": "NC",
        "zip": "28804",
        "lat": 35.6182,
        "lng": -82.5564,
        "neighborhood": "North Asheville",
        "bio": (
            "Zen Center of Asheville (ZCA) offers regular zazen in the Soto Zen "
            "tradition at the Asheville Friends Meeting building. Morning zazen: "
            "Mon/Wed/Fri 6–6:50am (40 min zazen). Saturday 6–7:40am (extended: "
            "two zazen periods, kinhin, and Heart Sutra). Tuesday evenings: 7pm "
            "zazen (30 min) + dharma talk and discussion until 8:30pm. New student "
            "instruction 1st Tuesdays at 6pm by registration. Dana $10 for evenings."
        ),
    },
    "mountain_mindfulness_asheville": {
        "id": "mountain_mindfulness_asheville",
        "name": "Mountain Mindfulness Sangha of Asheville",
        "tradition": "other",
        "url": "https://www.mountainmindfulness.org",
        "address": "227 Edgewood Road",
        "city": "Asheville",
        "state": "NC",
        "zip": "28804",
        "lat": 35.6182,
        "lng": -82.5564,
        "neighborhood": "North Asheville",
        "bio": (
            "Mountain Mindfulness Sangha practices engaged Buddhism in the Plum Village "
            "tradition of Thich Nhat Hanh. Thursday 7–8:30pm at Asheville Friends "
            "Meeting, 227 Edgewood Rd: four rotating formats — 1st Thu: Heart Sutra "
            "chanting and study; 2nd Thu: Plum Village book reading; 3rd Thu: silent "
            "sitting and walking; 4th Thu: Five Mindfulness Trainings recitation. "
            "First Saturday of month (warm season): 10–11:30am outdoor practice at "
            "Weaverville Main Street Nature Park. Drop-in; free."
        ),
    },
    "asheville_insight_meditation": {
        "id": "asheville_insight_meditation",
        "name": "Asheville Insight Meditation",
        "tradition": "theravada",
        "url": "https://www.ashevillemeditation.com",
        "address": "85 Weaverville Road, Unit 5",
        "city": "Woodfin",
        "state": "NC",
        "zip": "28804",
        "lat": 35.6481,
        "lng": -82.5802,
        "neighborhood": "Woodfin (North Asheville metro)",
        "bio": (
            "Asheville Insight Meditation offers weekly Vipassana sits ('Dharma without "
            "the Dogma'). Thursday Evening Meditation 7–8:30pm: 30-min guided "
            "meditation, 30-min dharma talk with visiting teachers, and 30-min Q&A — "
            "in-person at 85 Weaverville Road, Unit 5, Woodfin, plus Zoom. Sunday "
            "morning sits are Zoom-only. Drop-in; free."
        ),
    },
    "anattasati_magga": {
        "id": "anattasati_magga",
        "name": "Anattasati Magga",
        "tradition": "zen",
        "url": "https://anattasatimagga.org",
        "address": "32 Mineral Dust Drive",
        "city": "Asheville",
        "state": "NC",
        "zip": "28806",
        "lat": 35.5668,
        "lng": -82.6224,
        "neighborhood": "West Asheville",
        "bio": (
            "Anattasati Magga ('Path of Non-Self') is a lay Soto Zen sangha set on "
            "7 quiet acres in West Asheville. Sunday 10am–12pm: 30-min sitting "
            "meditation, chants and recitations, and a dharma class — in-person or "
            "Zoom. Second Sunday includes new-student orientation. Teacher: Sujata "
            "(Nancy Hampton). Free; donations welcome."
        ),
    },
    "burlington_shambhala": {
        "id": "burlington_shambhala",
        "name": "Burlington Shambhala Meditation Center",
        "tradition": "tibetan",
        "url": "https://burlington.shambhala.org",
        "address": "187 S Winooski Ave",
        "city": "Burlington",
        "state": "VT",
        "zip": "05401",
        "lat": 44.4710,
        "lng": -73.2135,
        "neighborhood": "Downtown Burlington",
        "bio": (
            "Burlington Shambhala Meditation Center, founded 1972, offers two weekly "
            "drop-in programs in the Tibetan Kagyu/Shambhala tradition. Sunday Open "
            "Meditation (9am–12pm): sitting practice with instruction available "
            "10am–12pm. Mid-Week Dharma (Wednesday 5:30–7pm): weekly drop-in with "
            "meditation, instruction, and dharma discussion. Located in the Hood Plant "
            "building at S Winooski Ave and King St, Downtown Burlington."
        ),
    },
    "vermont_zen_center": {
        "id": "vermont_zen_center",
        "name": "Vermont Zen Center",
        "tradition": "zen",
        "url": "https://vermontzen.org",
        "address": "480 Thomas Road",
        "city": "Shelburne",
        "state": "VT",
        "zip": "05482",
        "lat": 44.3910,
        "lng": -73.2210,
        "neighborhood": "Shelburne (Burlington metro)",
        "bio": (
            "Vermont Zen Center (founded 1988) is a Kapleau-lineage Soto/Rinzai Zen "
            "community in Shelburne, 8 miles south of Burlington, now led by Sensei "
            "Bodhi Murillo. Weekday morning zazen (Mon–Fri 6–7am, Zoom) is open to "
            "those who have attended an introductory workshop. In-person evening and "
            "Sunday sits are for members and trial members. First Monday monthly: "
            "'Finding Your Seat' orientation for newcomers. Sesshin and retreats "
            "offered throughout the year."
        ),
    },
    "burlington_buddhist_sangha": {
        "id": "burlington_buddhist_sangha",
        "name": "Burlington Buddhist Sangha",
        "tradition": "theravada",
        "url": "https://burlingtonbuddhist.org",
        "address": "187 S Winooski Ave",
        "city": "Burlington",
        "state": "VT",
        "zip": "05401",
        "lat": 44.4710,
        "lng": -73.2135,
        "neighborhood": "Downtown Burlington",
        "bio": (
            "Burlington Buddhist Sangha is a peer-led Insight Meditation community "
            "practicing in the Theravada tradition. 1st, 2nd, and 3rd Sundays "
            "(9:30–11:30am): sitting meditation, dharma talk, and discussion at the "
            "Burlington Shambhala Center (187 S Winooski Ave). 4th Sundays are "
            "online-only (Zoom). Dana-based; free. Beginners are welcome to monthly "
            "intro sessions before joining regular sits."
        ),
    },
    "burlington_dharma_collective": {
        "id": "burlington_dharma_collective",
        "name": "Burlington Dharma Collective",
        "tradition": "tibetan",
        "url": "https://www.burlingtondharmacollective.com",
        "address": "241 N Winooski Ave",
        "city": "Burlington",
        "state": "VT",
        "zip": "05401",
        "lat": 44.4777,
        "lng": -73.2126,
        "neighborhood": "Old North End Burlington",
        "bio": (
            "Burlington Dharma Collective is a liberatory Vajrayana community (founded "
            "~2023) led by Zac Ispa-Landa, a student of Lama Rod Owens "
            "(Bhumisparsha lineage). Meets at Outright VT (241 N Winooski Ave). "
            "Weekly Meditation: Friday 8–8:45am, fully open drop-in. Monday Night "
            "Dharma: 2nd Monday monthly, 7–8:30pm. Donations welcome."
        ),
    },
    # -------------------------------------------------------------------------
    # Eugene, OR — Phase 3 (heartbeat 60)
    # -------------------------------------------------------------------------
    "buddha_eye_temple": {
        "id": "buddha_eye_temple",
        "name": "Buddha Eye Temple",
        "tradition": "zen",
        "url": "https://www.buddhaeye.org",
        "address": "2190 Garfield St",
        "city": "Eugene",
        "state": "OR",
        "zip": "97405",
        "lat": 44.0268,
        "lng": -123.0978,
        "neighborhood": "South Eugene",
        "bio": (
            "Buddha Eye Temple is a Soto Zen temple (registered Soto Zen School) in "
            "South Eugene, founded 2002. The main public program is the Sunday morning "
            "service: Introduction to Meditation 8:45–9:50am, then Zazen 9:00am, and "
            "Assembly/ceremony at 10:00am. All are welcome to the intro and zazen; no "
            "registration required. Weekday zazen at 5:00am (Sep–Jun) or 5:30am "
            "(summer). Sesshin and retreats offered several times a year."
        ),
    },
    "blue_cliff_zen_eugene": {
        "id": "blue_cliff_zen_eugene",
        "name": "Blue Cliff Zen Center",
        "tradition": "zen",
        "url": "https://www.bluecliffzen.org",
        "address": "352 W 12th Ave",
        "city": "Eugene",
        "state": "OR",
        "zip": "97401",
        "lat": 44.0477,
        "lng": -123.0888,
        "neighborhood": "West University / Downtown Eugene",
        "bio": (
            "Blue Cliff Zen Center is a Western Zen community (Soto/Rinzai hybrid) "
            "meeting inside Everyday People Yoga studio in Eugene, led by teacher "
            "Matt Shinkai Kane. In-person + online hybrid programs: Tuesday and "
            "Thursday 7:00–8:00am (zazen + optional instruction), Sunday 4:30–6:00pm "
            "(zazen + dharma discussion). Drop-in welcome; dana-based."
        ),
    },
    "zen_west_eugene": {
        "id": "zen_west_eugene",
        "name": "Zen West Eugene",
        "tradition": "zen",
        "url": "https://www.zenwesteugene.org",
        "address": "1685 W 13th Ave",
        "city": "Eugene",
        "state": "OR",
        "zip": "97402",
        "lat": 44.0456,
        "lng": -123.1172,
        "neighborhood": "Jefferson Westside / West Eugene",
        "bio": (
            "Zen West Eugene is a Soto Zen community affiliated with Dharma Rain Zen "
            "Center (Portland), led by Debra Seido Martin (transmitted Soto Zen lay "
            "teacher). Thursday evening program (7:00–8:45pm) at UUCE (1685 W 13th "
            "Ave): zazen, kinhin, chanting, dharma talk/discussion. Monthly zazenkai "
            "and sesshin 4x/year. Drop-in welcome."
        ),
    },
    "river_wisdom_insight": {
        "id": "river_wisdom_insight",
        "name": "River Wisdom Insight Meditation Community",
        "tradition": "theravada",
        "url": "https://riverwisdominsight.com",
        "address": "1685 W 13th Ave",
        "city": "Eugene",
        "state": "OR",
        "zip": "97402",
        "lat": 44.0456,
        "lng": -123.1172,
        "neighborhood": "Jefferson Westside / West Eugene",
        "bio": (
            "River Wisdom Insight Meditation Community offers Insight Meditation in "
            "the Theravada tradition, led by Linda Rose (student of Howie Cohn / "
            "Spirit Rock lineage). 1st Saturday of month: 10:30am–12pm at UUCE "
            "(1685 W 13th Ave) — sitting, dharma talk, discussion. 3rd Saturday: "
            "10:30–11:30am at Buddha Eye Temple (2190 Garfield St). Drop-in welcome; "
            "dana-based."
        ),
    },
    # --- Santa Cruz, CA ---
    "ocean_gate_zen": {
        "id": "ocean_gate_zen",
        "name": "Ocean Gate Zen Center",
        "tradition": "zen",
        "url": "https://oceangatezen.org",
        "address": "920 41st Ave Suite F",
        "city": "Santa Cruz",
        "state": "CA",
        "zip": "95062",
        "lat": 36.9719,
        "lng": -121.9920,
        "neighborhood": "Opal Cliffs / 41st Ave District",
        "bio": (
            "Ocean Gate Zen Center is a Soto Zen community founded ~2021, led by "
            "Eikei Susan O'Brien (transmitted Soto teacher, dharma successor of "
            "Shohaku Okumura). Located at 920 41st Ave Suite F (enter from back "
            "parking lot). Public programs: Tue/Thu morning zazen 6:45–8:00am "
            "(in-person + Zoom); Fri morning zazen 9:00–9:40am; Thu evening 6:00pm "
            "zazen + dharma Q&A (in-person + Zoom); Sat 9:00am 'Come As You Are' "
            "sit + dharma talk (in-person). Drop-in welcome."
        ),
    },
    "sczc": {
        "id": "sczc",
        "name": "Santa Cruz Zen Center",
        "tradition": "zen",
        "url": "https://sczc.org",
        "address": "113 School St",
        "city": "Santa Cruz",
        "state": "CA",
        "zip": "95060",
        "lat": 36.9783,
        "lng": -122.0278,
        "neighborhood": "Downtown Santa Cruz",
        "bio": (
            "Santa Cruz Zen Center (SCZC, formally Jorinzan Gyokuon-ji) is the oldest "
            "and largest Zen center in Santa Cruz, founded 1970 in the Soto Zen "
            "lineage (SZBA member). Daily zazen schedule: Mon–Fri 6:00am and 6:00pm "
            "(in-person + Zoom); Wednesday evening 6:30pm kinhin + dharma talk; "
            "Saturday 8:30am zazen; Sunday 6:00pm zazen. Introduction to Zen "
            "typically 3rd Saturday 1–2pm. Sesshin and retreats throughout the year. "
            "Drop-in welcome."
        ),
    },
    "insight_santa_cruz": {
        "id": "insight_santa_cruz",
        "name": "Insight Santa Cruz",
        "tradition": "theravada",
        "url": "https://www.insightsantacruz.org",
        "address": "740 Front Street, Suite 240",
        "city": "Santa Cruz",
        "state": "CA",
        "zip": "95060",
        "lat": 36.9742,
        "lng": -122.0308,
        "neighborhood": "Downtown Santa Cruz",
        "bio": (
            "Insight Santa Cruz is a Vipassana/Insight Meditation community in "
            "downtown Santa Cruz (740 Front St, Suite 240). Regular in-person/hybrid "
            "public sits: Sunday 9:00am volunteer-led sit; Tuesday 12:00pm "
            "All-Community Sit with teacher; Wednesday 6:00pm All-Community Sit; "
            "4th Tuesday 7pm Rainbow Sangha (LGBTQ+ inclusive). Dana-based; all welcome."
        ),
    },
    "land_of_medicine_buddha": {
        "id": "land_of_medicine_buddha",
        "name": "Land of Medicine Buddha",
        "tradition": "tibetan",
        "url": "https://www.landofmedicinebuddha.org",
        "address": "5800 Prescott Rd",
        "city": "Soquel",
        "state": "CA",
        "zip": "95073",
        "lat": 37.0061,
        "lng": -121.9497,
        "neighborhood": "Santa Cruz Mountains / Soquel Hills",
        "bio": (
            "Land of Medicine Buddha (LMB) is an FPMT/Gelug Tibetan Buddhist retreat "
            "and study center in the hills above Soquel, near Santa Cruz. The main "
            "public sit is the weekly Sunday Drop-In Meditation (9:00–10:00am) at the "
            "Gompa, led by Ven. Yangchen — suitable for all levels, no registration "
            "required. Online daily Zoom meditation sessions also available. Retreats "
            "and teachings offered throughout the year."
        ),
    },
    # -------------------------------------------------------------------------
    # Wichita, KS — Phase 3 (heartbeat 62)
    # -------------------------------------------------------------------------
    "southwind_sangha": {
        "id": "southwind_sangha",
        "name": "Southwind Sangha",
        "tradition": "zen",
        "url": "https://southwindsangha.org",
        "address": "5620 E 21st St N",
        "city": "Wichita",
        "state": "KS",
        "zip": "67208",
        "lat": 37.7220,
        "lng": -97.2520,
        "neighborhood": "Northeast Wichita",
        "bio": (
            "Southwind Sangha is a Soto Zen Buddhist community (Soto Zen Buddhist "
            "Association / SZBA member) meeting at Pine Valley Christian Church in "
            "northeast Wichita. Regular schedule: Sunday 9:00–10:30am (zazen, kinhin, "
            "Heart Sutra chanting) and Wednesday 7:00–8:00pm sits. Third Saturday of "
            "each month: 8:00am–12:00pm silent half-day retreat. Drop-in welcome. "
            "Contact via Facebook or harold.sanki@gmail.com for Zoom link."
        ),
    },
    "wichita_ktc": {
        "id": "wichita_ktc",
        "name": "Wichita KTC",
        "tradition": "tibetan",
        "url": "https://wichitaktc.org",
        "address": "425 S Yale Ave",
        "city": "Wichita",
        "state": "KS",
        "zip": "67218",
        "lat": 37.6810,
        "lng": -97.2680,
        "neighborhood": "East Wichita",
        "bio": (
            "Wichita KTC (Karma Thegsum Chöling) is a Tibetan Buddhist meditation "
            "center in the Karma Kagyu lineage. Sunday program 10:00am–11:45am: "
            "1st and 3rd Sundays feature the Chenrezik Sadhana (compassion practice, "
            "sitting meditation, dharma talk); 2nd and 4th Sundays offer explicit "
            "sitting meditation followed by discussion and book study. All are welcome. "
            "Contact: ktcwichita@yahoo.com."
        ),
    },
    "dmck": {
        "id": "dmck",
        "name": "Dhammakaya Meditation Center Kansas",
        "tradition": "theravada",
        "url": "https://www.meditationkansas.org",
        "address": "1650 S Water St",
        "city": "Wichita",
        "state": "KS",
        "zip": "67213",
        "lat": 37.6635,
        "lng": -97.3305,
        "neighborhood": "South Wichita",
        "bio": (
            "Dhammakaya Meditation Center Kansas (DMCK) is a Thai Theravada Buddhist "
            "center offering public meditation classes in Wichita. Saturday public "
            "meditation class 3:30–5:00pm at 1650 S Water St (most Saturdays; first "
            "Saturday of month and special holidays off). No experience necessary; "
            "open to all. The Dhammakaya tradition emphasizes samadhi (concentration) "
            "meditation and the Middle Way of inner stillness."
        ),
    },
    # -------------------------------------------------------------------------
    # Missoula, MT
    # -------------------------------------------------------------------------
    "open_way_sangha": {
        "id": "open_way_sangha",
        "name": "Open Way Sangha",
        "tradition": "zen",
        "url": "https://www.openway.org",
        "address": "702 Brooks St",
        "city": "Missoula",
        "state": "MT",
        "zip": "59801",
        "lat": 46.8533,
        "lng": -114.0078,
        "neighborhood": "South Missoula",
        "bio": (
            "Open Way Sangha is a Plum Village (Thich Nhat Hanh / Vietnamese Zen) "
            "community that has been practicing in Missoula since the 1990s. Meets at "
            "702 Brooks St: Tuesdays 7:00–9:00pm and Saturdays 10:00am–12:00pm. "
            "Monthly format rotates between dharma talk + sharing, sutra service + "
            "meditation, Mindfulness Trainings recitation, tea ceremony, and special "
            "programs. All are welcome — new people encouraged. Dana-based. "
            "Contact openwaysangha@gmail.com."
        ),
    },
    "osel_shen_phen_ling": {
        "id": "osel_shen_phen_ling",
        "name": "Osel Shen Phen Ling",
        "tradition": "tibetan",
        "url": "https://fpmtosel.wordpress.com",
        "address": "500 N Higgins Ave, Suite 208A",
        "city": "Missoula",
        "state": "MT",
        "zip": "59802",
        "lat": 46.8723,
        "lng": -113.9940,
        "neighborhood": "Downtown Missoula",
        "bio": (
            "Osel Shen Phen Ling is an FPMT (Foundation for the Preservation of the "
            "Mahayana Tradition) Gelug Tibetan Buddhist center established in 1986 — "
            "one of Montana's oldest Buddhist organizations. Located at 500 N Higgins "
            "Ave in downtown Missoula. Monday 7:00pm: weekly guided meditation (~30 "
            "minutes of shamatha with brief prayers). No experience necessary; free. "
            "Also offers seasonal intro courses (Meditation 101, Buddhism in a Nutshell). "
            "Contact oselshenphenling@gmail.com."
        ),
    },
    "rocky_mountain_bc": {
        "id": "rocky_mountain_bc",
        "name": "Rocky Mountain Buddhist Center",
        "tradition": "other",
        "url": "http://rockymountainbuddhistcenter.org",
        "address": "540 South 2nd West",
        "city": "Missoula",
        "state": "MT",
        "zip": "59801",
        "lat": 46.8645,
        "lng": -114.0120,
        "neighborhood": "University District",
        "bio": (
            "Rocky Mountain Buddhist Center is part of the Triratna Buddhist Community "
            "(formerly Friends of the Western Buddhist Order / FWBO), located near the "
            "University of Montana campus. Founded by UM Asian Studies professor Alan "
            "Sponburg. Wednesday Sangha Night 7:00–9:00pm teaches Mindfulness of "
            "Breathing and Metta Bhavana. Open to those who have completed their "
            "5-week intro course. Intro sessions run periodically — contact "
            "fwbomissoula@gmail.com."
        ),
    },
    # -------------------------------------------------------------------------
    # Bozeman, MT
    # -------------------------------------------------------------------------
    "bozeman_dharma_center": {
        "id": "bozeman_dharma_center",
        "name": "Bozeman Dharma Center",
        "tradition": "other",
        "url": "https://bozemandharmacenter.org",
        "address": "206 E Griffin Dr",
        "city": "Bozeman",
        "state": "MT",
        "zip": "59715",
        "lat": 45.6784,
        "lng": -111.0346,
        "neighborhood": "Downtown Bozeman",
        "bio": (
            "Bozeman Dharma Center is a multi-tradition Buddhist hub in Bozeman, MT, "
            "meeting at Fork & Spoon (206 E Griffin Dr). It hosts seven resident "
            "groups: Bozeman Zen Group (Soto Zen / Branching Streams / Berkeley Zen "
            "Center lineage), Bozeman Insight Community (Vipassana, est. 1996), "
            "Joining Rivers Sangha (Plum Village/Thich Nhat Hanh), Tergar Bozeman "
            "(Yongey Mingyur Rinpoche), Palyul Tibetan Buddhist Sangha "
            "(Nyingma/Namdroling), MindSpace (young adults 18–40), and Recovery "
            "Dharma. Also hosts a daily Noon Sit (M–F 12–1pm, open and silent). "
            "Northwest Dharma Association member. All traditions welcome. "
            "(406) 219-2140 · info@bozemandharmacenter.org."
        ),
    },
}
