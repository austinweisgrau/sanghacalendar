#!/usr/bin/env bun
/**
 * Seeds the sangha calendar DB with recurring weekly sits from meditations.html.
 * Generates dated instances for the next 90 days and POSTs to the app.
 */

import crypto from "crypto";

const APP_URL      = "https://sangha-calendar.fly.dev";
const INGEST_TOKEN = (await Bun.file("/workspace/group/memory/sangha-ingest-token.txt").text()).trim();

// ── Recurring sits (sourced from meditations.html) ────────────────────────────

const SITS = [
  // Berkeley Shambhala
  {
    org_id: "shambhala_berkeley", org_name: "Berkeley Shambhala Center",
    title: "Drop-in Sitting Meditation",
    days: ["Tuesday"], time: { h: 9, m: 30 }, duration_min: 90,
    address: "2288 Fulton St", city: "Berkeley", state: "CA", neighborhood: "South Campus Berkeley",
    lat: 37.8696, lng: -122.2677, tradition: "tibetan", location_type: "in-person",
    source_url: "https://berkeley.shambhala.org", event_url: "https://berkeley.shambhala.org/",
  },
  {
    org_id: "shambhala_berkeley", org_name: "Berkeley Shambhala Center",
    title: "Drop-in Sitting Meditation",
    days: ["Tuesday"], time: { h: 12, m: 15 }, duration_min: 90,
    address: "2288 Fulton St", city: "Berkeley", state: "CA", neighborhood: "South Campus Berkeley",
    lat: 37.8696, lng: -122.2677, tradition: "tibetan", location_type: "in-person",
    source_url: "https://berkeley.shambhala.org", event_url: "https://berkeley.shambhala.org/",
  },
  // Metta Dharma
  {
    org_id: "metta_dharma", org_name: "Metta Dharma Foundation",
    title: "Wednesday Evening Sit",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "2837 Claremont Blvd", city: "Berkeley", state: "CA", neighborhood: "Claremont",
    lat: 37.8579, lng: -122.2432, tradition: "theravada", location_type: "hybrid",
    notes: "Teacher: Richard Shankman. Sit followed by brief dharma. Also on Zoom: zoom.us/j/93748448333.",
    source_url: "https://www.mettadharma.org", event_url: "https://www.mettadharma.org/",
  },
  // Bay Zen
  {
    org_id: "bay_zen", org_name: "Bay Zen Center",
    title: "Zazen",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "3824 Grand Ave", city: "Oakland", state: "CA", neighborhood: "Grand Lake",
    lat: 37.8145, lng: -122.2286, tradition: "zen", location_type: "in-person",
    source_url: "https://bayzen.org", event_url: "https://www.bayzen.org/calendar",
  },
  // Berkeley Buddhist Monastery (Chan)
  {
    org_id: "berkeley_buddhist_monastery", org_name: "Berkeley Buddhist Monastery",
    title: "Open Morning Meditation",
    days: ["Thursday", "Friday"], time: { h: 6, m: 15 }, duration_min: 60,
    address: "2304 McKinley Ave", city: "Berkeley", state: "CA", neighborhood: "North Berkeley",
    lat: 37.8758, lng: -122.2637, tradition: "zen", location_type: "in-person",
    source_url: "https://www.berkeleymonastery.org", event_url: "https://www.berkeleymonastery.org/",
  },
  {
    org_id: "berkeley_buddhist_monastery", org_name: "Berkeley Buddhist Monastery",
    title: "Evening Meditation",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    time: { h: 17, m: 15 }, duration_min: 60,
    address: "2304 McKinley Ave", city: "Berkeley", state: "CA", neighborhood: "North Berkeley",
    lat: 37.8758, lng: -122.2637, tradition: "zen", location_type: "in-person",
    source_url: "https://www.berkeleymonastery.org", event_url: "https://www.berkeleymonastery.org/",
  },
  // Insight Berkeley (Thursday)
  {
    org_id: "insight_berkeley", org_name: "Insight Meditation Community of Berkeley",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "2304 McKinley Ave", city: "Berkeley", state: "CA", neighborhood: "North Berkeley",
    lat: 37.8758, lng: -122.2637, tradition: "theravada", location_type: "in-person",
    notes: "James Baraz + Eve Decker. Sit-centered with brief dharma sharing.",
    source_url: "https://www.insightberkeley.org", event_url: "https://www.insightberkeley.org/events",
  },
  // Oakland Zen (Kojin-an)
  {
    org_id: "oakland_zen", org_name: "Oakland Zen Center / Kojin-an",
    title: "Morning Zazen",
    days: ["Friday"], time: { h: 6, m: 0 }, duration_min: 60,
    address: "6140 Chabot Rd", city: "Oakland", state: "CA", neighborhood: "Rockridge",
    lat: 37.8397, lng: -122.2278, tradition: "zen", location_type: "in-person",
    notes: "Small family zendo. Email or call before first visit.",
    source_url: "https://oaklandzencenter.org", event_url: "http://oaklandzencenter.org/schedule",
  },
  {
    org_id: "oakland_zen", org_name: "Oakland Zen Center / Kojin-an",
    title: "Zazenkai",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 120,
    address: "6140 Chabot Rd", city: "Oakland", state: "CA", neighborhood: "Rockridge",
    lat: 37.8397, lng: -122.2278, tradition: "zen", location_type: "in-person",
    notes: "Intro instruction 8am. Full zazen 9am, chanting, cleaning, tea.",
    source_url: "https://oaklandzencenter.org", event_url: "http://oaklandzencenter.org/kojinan-events/",
  },
  // Berkeley Buddhist Priory
  {
    org_id: "berkeley_priory", org_name: "Berkeley Buddhist Priory",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 60,
    address: "1358 Marin Ave", city: "Albany", state: "CA", neighborhood: "Albany",
    lat: 37.8934, lng: -122.2987, tradition: "zen", location_type: "in-person",
    notes: "Order of Buddhist Contemplatives lineage (British Soto Zen).",
    source_url: "https://berkeleybuddhistpriory.org", event_url: "https://berkeleybuddhistpriory.org/",
  },
  // Empty Gate Zen
  {
    org_id: "empty_gate_zen", org_name: "Empty Gate Zen Center",
    title: "Saturday Sitting",
    days: ["Saturday"], time: { h: 8, m: 0 }, duration_min: 60,
    address: "2200 Parker St", city: "Berkeley", state: "CA", neighborhood: "South Berkeley",
    lat: 37.8634, lng: -122.2597, tradition: "zen", location_type: "in-person",
    notes: "Korean Zen (Kwan Um). Confirm schedule on website.",
    source_url: "https://emptygatezen.com", event_url: "https://www.emptygatezen.com/schedule",
  },
  {
    org_id: "empty_gate_zen", org_name: "Empty Gate Zen Center",
    title: "Monday Evening Meditation",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "2200 Parker St", city: "Berkeley", state: "CA", neighborhood: "South Berkeley",
    lat: 37.8634, lng: -122.2597, tradition: "zen", location_type: "in-person",
    source_url: "https://emptygatezen.com", event_url: "https://www.emptygatezen.com/schedule",
  },

  // ── SF / Marin ───────────────────────────────────────────────────────────────

  // SF Zen Center — City Center (daily zazen)
  {
    org_id: "sfzc_city_center", org_name: "SF Zen Center — City Center",
    title: "Evening Zazen",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday"], time: { h: 17, m: 40 }, duration_min: 40,
    address: "300 Page St", city: "San Francisco", state: "CA", neighborhood: "Hayes Valley",
    lat: 37.7730, lng: -122.4248, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen. Public welcome. Please arrive on time.",
    source_url: "https://sfzc.org", event_url: "https://sfzc.org/calendar",
  },
  {
    org_id: "sfzc_city_center", org_name: "SF Zen Center — City Center",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 6, m: 30 }, duration_min: 90,
    address: "300 Page St", city: "San Francisco", state: "CA", neighborhood: "Hayes Valley",
    lat: 37.7730, lng: -122.4248, tradition: "zen", location_type: "in-person",
    notes: "Zazen followed by dharma talk at 10am. All welcome.",
    source_url: "https://sfzc.org", event_url: "https://sfzc.org/calendar",
  },
  {
    org_id: "sfzc_city_center", org_name: "SF Zen Center — City Center",
    title: "Thursday Online Drop-in Practice",
    days: ["Thursday"], time: { h: 17, m: 30 }, duration_min: 60,
    address: "300 Page St", city: "San Francisco", state: "CA", neighborhood: "Hayes Valley",
    lat: 37.7730, lng: -122.4248, tradition: "zen", location_type: "online",
    notes: "Online only via Zoom. Check sfzc.org for link.",
    source_url: "https://sfzc.org", event_url: "https://sfzc.org/calendar",
  },

  // Hartford Street Zen Center / Issan-ji (Castro — LGBTQ+ community)
  {
    org_id: "hartford_zen", org_name: "Hartford Street Zen Center",
    title: "Morning Zazen",
    days: ["Tuesday","Thursday","Saturday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "57 Hartford St", city: "San Francisco", state: "CA", neighborhood: "Castro",
    lat: 37.7609, lng: -122.4353, tradition: "zen", location_type: "in-person",
    identity_focus: "LGBTQ+",
    notes: "Soto Zen temple for LGBTQ+ community and allies. Morning service follows zazen.",
    source_url: "https://hszc.org", event_url: "https://hszc.org/schedule",
  },
  {
    org_id: "hartford_zen", org_name: "Hartford Street Zen Center",
    title: "Evening Zazen",
    days: ["Wednesday","Friday"], time: { h: 18, m: 0 }, duration_min: 40,
    address: "57 Hartford St", city: "San Francisco", state: "CA", neighborhood: "Castro",
    lat: 37.7609, lng: -122.4353, tradition: "zen", location_type: "in-person",
    identity_focus: "LGBTQ+",
    notes: "Soto Zen. Evening service follows zazen.",
    source_url: "https://hszc.org", event_url: "https://hszc.org/schedule",
  },
  {
    org_id: "hartford_zen", org_name: "Hartford Street Zen Center",
    title: "Saturday Sangha",
    days: ["Saturday"], time: { h: 9, m: 30 }, duration_min: 120,
    address: "57 Hartford St", city: "San Francisco", state: "CA", neighborhood: "Castro",
    lat: 37.7609, lng: -122.4353, tradition: "zen", location_type: "hybrid",
    identity_focus: "LGBTQ+",
    notes: "Zazen 6:30am, then 9:30am zazen + 10:30am dharma talk. Zoom starts 9am.",
    source_url: "https://hszc.org", event_url: "https://hszc.org/schedule",
  },

  // Mission Dharma (Tuesday evening)
  {
    org_id: "mission_dharma", org_name: "Mission Dharma",
    title: "Tuesday Evening Meditation",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "Mission District", city: "San Francisco", state: "CA", neighborhood: "Mission District",
    lat: 37.7599, lng: -122.4148, tradition: "theravada", location_type: "online",
    notes: "Howard Cohn + rotating teachers. 40-min sit + Q&A + dharma talk. Zoom + YouTube livestream.",
    source_url: "https://missiondharma.org", event_url: "https://missiondharma.org/tuesday-night-schedule.html",
  },

  // Marin Sangha (Sunday evening)
  {
    org_id: "marin_sangha", org_name: "Marin Sangha",
    title: "Sunday Evening Meditation",
    days: ["Sunday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "10 Bayview Dr", city: "San Rafael", state: "CA", neighborhood: "San Rafael",
    lat: 37.9735, lng: -122.5311, tradition: "theravada", location_type: "hybrid",
    notes: "Donald Rothberg + rotating Spirit Rock teachers. Zoom + occasional in-person at St. Luke Church.",
    source_url: "https://marinsangha.org", event_url: "https://www.marinsangha.org",
  },

  // Berkeley Zen Center — daily zazen (not in their iCal feed, which only tracks special events)
  {
    org_id: "berkeley_zen_center", org_name: "Berkeley Zen Center",
    title: "Morning Zazen",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    time: { h: 6, m: 0 }, duration_min: 90,
    address: "1931 Russell St", city: "Berkeley", state: "CA", neighborhood: "South Berkeley",
    lat: 37.8582, lng: -122.2705, tradition: "zen", location_type: "hybrid",
    notes: "Daily morning zazen + service. In-person and online. Founded 1967 by Sojun Mel Weitsman and Shunryu Suzuki Roshi.",
    source_url: "https://berkeleyzencenter.org", event_url: "https://berkeleyzencenter.org/weekly-schedule/",
  },
  {
    org_id: "berkeley_zen_center", org_name: "Berkeley Zen Center",
    title: "Evening Zazen",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    time: { h: 17, m: 40 }, duration_min: 50,
    address: "1931 Russell St", city: "Berkeley", state: "CA", neighborhood: "South Berkeley",
    lat: 37.8582, lng: -122.2705, tradition: "zen", location_type: "hybrid",
    notes: "Evening zazen + service. In-person and online.",
    source_url: "https://berkeleyzencenter.org", event_url: "https://berkeleyzencenter.org/weekly-schedule/",
  },
  {
    org_id: "berkeley_zen_center", org_name: "Berkeley Zen Center",
    title: "Evening Drop-In Zazen",
    days: ["Wednesday"], time: { h: 19, m: 10 }, duration_min: 110,
    address: "1931 Russell St", city: "Berkeley", state: "CA", neighborhood: "South Berkeley",
    lat: 37.8582, lng: -122.2705, tradition: "zen", location_type: "in-person",
    notes: "In-person only. Zazen + dharma reading and discussion. Open to all.",
    source_url: "https://berkeleyzencenter.org", event_url: "https://berkeleyzencenter.org/weekly-schedule/",
  },

  // Ewam Choden — weekly Sunday public meditation (Sakya Tibetan, Kensington)
  {
    org_id: "ewam_choden", org_name: "Ewam Choden Tibetan Buddhist Center",
    title: "Sunday Public Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "254 Cambridge Ave", city: "Kensington", state: "CA", neighborhood: "Kensington",
    lat: 37.9024, lng: -122.2694, tradition: "tibetan", location_type: "in-person",
    notes: "Open to all. Compassion meditation practice. Session begins promptly at 10am.",
    source_url: "https://www.ewamchoden.org", event_url: "https://www.ewamchoden.org/",
  },

  // IMC Berkeley — New Monday Evening Sitting Group at Berkeley Finnish Hall (starts May 25, 2026)
  {
    org_id: "imc_berkeley", org_name: "Insight Meditation Center",
    title: "Monday Evening Sitting Group",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "1970 Chestnut St", city: "Berkeley", state: "CA", neighborhood: "West Berkeley",
    lat: 37.8778, lng: -122.2890, tradition: "theravada", location_type: "in-person",
    notes: "New Berkeley satellite group of IMC. Lightly guided sit + short Dharma talk + discussion. At Berkeley Finnish Hall. Meets at 7pm; intro talks through May 18, open sitting group from May 25.",
    source_url: "https://www.insightmeditationcenter.org", event_url: "https://www.insightmeditationcenter.org/2026/04/new-berkeley-imc-sitting-group-starting-monday-april-20th/",
  },

  // Mount Diablo Zen Group — weekly Wednesday 7pm, hybrid (in-person odd weeks, Zoom even weeks)
  {
    org_id: "mount_diablo_zen", org_name: "Mount Diablo Zen Group",
    title: "Wednesday Evening Zazen",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "404 Gregory Lane, Room 9", city: "Pleasant Hill", state: "CA", neighborhood: "Pleasant Hill",
    lat: 37.9499, lng: -122.0935, tradition: "zen", location_type: "hybrid",
    notes: "Soto Zen (SZBA). In-person 1st/3rd/5th Wednesdays; Zoom 2nd/4th Wednesdays. Drop-in welcome, meditation instruction available. Free.",
    source_url: "https://mtdiablozen.com", event_url: "https://mtdiablozen.com/",
  },

  // Green Gulch Farm Zen Center (SFZC Marin) — daily zazen + Sunday morning program
  // No iCal feed (SFZC uses Drupal 10 with no ical endpoint). Seeded from daily schedule page.
  // "No Zendo schedule on Monday afternoons and Tuesdays."
  {
    org_id: "green_gulch_farm", org_name: "Green Gulch Farm Zen Center",
    title: "Morning Zazen",
    days: ["Monday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    time: { h: 6, m: 0 }, duration_min: 60,
    address: "1601 Shoreline Hwy", city: "Muir Beach", state: "CA", neighborhood: "Muir Beach / West Marin",
    lat: 37.8694, lng: -122.5630, tradition: "zen", location_type: "in-person",
    notes: "Daily morning zazen open to public. Schedule varies — call office at 415.383.3134 to confirm. No Tuesday zazen.",
    source_url: "https://sfzc.org/green-gulch-farm", event_url: "https://sfzc.org/locations/green-gulch-farm/zen-meditation-practice-green-gulch/daily-schedule-green-gulch",
  },
  {
    org_id: "green_gulch_farm", org_name: "Green Gulch Farm Zen Center",
    title: "Evening Zazen",
    days: ["Wednesday","Thursday","Friday","Saturday"],
    time: { h: 19, m: 50 }, duration_min: 60,
    address: "1601 Shoreline Hwy", city: "Muir Beach", state: "CA", neighborhood: "Muir Beach / West Marin",
    lat: 37.8694, lng: -122.5630, tradition: "zen", location_type: "in-person",
    notes: "Evening zazen open to public. Schedule varies — call office at 415.383.3134 to confirm.",
    source_url: "https://sfzc.org/green-gulch-farm", event_url: "https://sfzc.org/locations/green-gulch-farm/zen-meditation-practice-green-gulch/daily-schedule-green-gulch",
  },
  {
    org_id: "green_gulch_farm", org_name: "Green Gulch Farm Zen Center",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 110,
    address: "1601 Shoreline Hwy", city: "Muir Beach", state: "CA", neighborhood: "Muir Beach / West Marin",
    lat: 37.8694, lng: -122.5630, tradition: "zen", location_type: "hybrid",
    notes: "Open to all, no registration required. 8:15am zazen instruction, 9:30am sitting meditation, 10am public Dharma talk (in-person + Online Zendo livestream), 11am discussion, 11:20am tea.",
    source_url: "https://sfzc.org/green-gulch-farm", event_url: "https://sfzc.org/calendar",
  },

  // San Francisco Shambhala Center (Glen Park)
  // iCal server (shambhala-koeln.de center=177) is dead — seeding from website schedule
  {
    org_id: "shambhala_sf", org_name: "San Francisco Shambhala Center",
    title: "Beginners Night",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    week_of_month: 2,
    address: "280 Claremont St", city: "San Francisco", state: "CA", neighborhood: "Glen Park",
    lat: 37.7315, lng: -122.4296, tradition: "tibetan", location_type: "in-person",
    notes: "2nd Wednesday each month. Open to all — no experience needed. Shambhala Buddhist tradition.",
    source_url: "https://sf.shambhala.org", event_url: "https://sf.shambhala.org",
  },
  {
    org_id: "shambhala_sf", org_name: "San Francisco Shambhala Center",
    title: "Beginners Night",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    week_of_month: 4,
    address: "280 Claremont St", city: "San Francisco", state: "CA", neighborhood: "Glen Park",
    lat: 37.7315, lng: -122.4296, tradition: "tibetan", location_type: "in-person",
    notes: "4th Wednesday each month. Open to all — no experience needed. Shambhala Buddhist tradition.",
    source_url: "https://sf.shambhala.org", event_url: "https://sf.shambhala.org",
  },
  {
    org_id: "shambhala_sf", org_name: "San Francisco Shambhala Center",
    title: "Saturday Morning Meditation",
    days: ["Saturday"], time: { h: 9, m: 0 }, duration_min: 90,
    week_of_month: 3,
    address: "280 Claremont St", city: "San Francisco", state: "CA", neighborhood: "Glen Park",
    lat: 37.7315, lng: -122.4296, tradition: "tibetan", location_type: "in-person",
    notes: "3rd Saturday each month. Open to all — newcomers and experienced practitioners welcome.",
    source_url: "https://sf.shambhala.org", event_url: "https://sf.shambhala.org",
  },
  {
    org_id: "shambhala_sf", org_name: "San Francisco Shambhala Center",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 135,
    week_of_month: 1,
    address: "280 Claremont St", city: "San Francisco", state: "CA", neighborhood: "Glen Park",
    lat: 37.7315, lng: -122.4296, tradition: "tibetan", location_type: "online",
    notes: "1st Sunday each month. Online only via Zoom. 10am–12:15pm.",
    source_url: "https://sf.shambhala.org", event_url: "https://sf.shambhala.org",
  },
  {
    org_id: "shambhala_sf", org_name: "San Francisco Shambhala Center",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 135,
    week_of_month: 2,
    address: "280 Claremont St", city: "San Francisco", state: "CA", neighborhood: "Glen Park",
    lat: 37.7315, lng: -122.4296, tradition: "tibetan", location_type: "online",
    notes: "2nd Sunday each month. Online only via Zoom. 10am–12:15pm.",
    source_url: "https://sf.shambhala.org", event_url: "https://sf.shambhala.org",
  },

  // Karuna Buddhist Vihara — East Bay (Berkeley satellite, monthly Saturday sits)
  // Mostly 2nd Saturday but schedule varies — using specific 2026 dates from karunabv.org
  {
    org_id: "karuna_berkeley", org_name: "Karuna Buddhist Vihara — East Bay",
    title: "East Bay Dhamma Sit",
    days: ["Saturday"], time: { h: 15, m: 0 }, duration_min: 120,
    address: "1438 Neilson St", city: "Berkeley", state: "CA", neighborhood: "Westbrae",
    lat: 37.8821, lng: -122.2945, tradition: "theravada", location_type: "hybrid",
    dates: ["2026-05-09", "2026-06-20", "2026-07-11", "2026-08-08", "2026-09-12", "2026-10-10", "2026-11-14", "2026-12-12"],
    notes: "Monthly Saturday sit. Guided meditation + Dhammapada reading/discussion. Berkeley satellite of Karuna BV (Sunnyvale). Zoom available. Check karunabv.org for exact dates.",
    source_url: "https://www.karunabv.org/eastbay-dhamma.html", event_url: "https://www.karunabv.org/eastbay-dhamma.html",
  },

  // ── NYC Phase 3b — NY Zen Center for Contemplative Care (NYZCCC) ─────────────
  // No iCal feed (Webflow site). Stable schedule seeded here for quarterly refresh.
  {
    org_id: "nyzccc", org_name: "NY Zen Center for Contemplative Care",
    title: "Mid-Day Zazen",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    time: { h: 12, m: 30 }, duration_min: 30,
    address: "119 W 23rd St, 4th Floor", city: "Manhattan", state: "NY", neighborhood: "Chelsea",
    lat: 40.7435, lng: -73.9949, tradition: "zen", location_type: "online",
    notes: "Daily online zazen, Monday–Saturday 12:30pm ET via Zoom. Open to all. No registration required.",
    source_url: "https://zencare.org/online-zendo", event_url: "https://zencare.org/online-zendo",
  },
  {
    org_id: "nyzccc", org_name: "NY Zen Center for Contemplative Care",
    title: "Sunday Morning Service",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "119 W 23rd St, 4th Floor", city: "Manhattan", state: "NY", neighborhood: "Chelsea",
    lat: 40.7435, lng: -73.9949, tradition: "zen", location_type: "hybrid",
    notes: "10am zazen (in-person + online), 11:30am dharma talk. Soto Zen service. All welcome.",
    source_url: "https://zencare.org/online-zendo", event_url: "https://zencare.org/online-zendo",
  },
  {
    org_id: "nyzccc", org_name: "NY Zen Center for Contemplative Care",
    title: "Monday Evening Sitting",
    days: ["Monday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "119 W 23rd St, 4th Floor", city: "Manhattan", state: "NY", neighborhood: "Chelsea",
    lat: 40.7435, lng: -73.9949, tradition: "zen", location_type: "hybrid",
    notes: "In-person + online. Open sitting. Soto Zen.",
    source_url: "https://zencare.org/online-zendo", event_url: "https://zencare.org/online-zendo",
  },
  {
    org_id: "nyzccc", org_name: "NY Zen Center for Contemplative Care",
    title: "Wednesday Evening Sitting",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "119 W 23rd St, 4th Floor", city: "Manhattan", state: "NY", neighborhood: "Chelsea",
    lat: 40.7435, lng: -73.9949, tradition: "zen", location_type: "hybrid",
    notes: "In-person + online. Open sitting. Soto Zen.",
    source_url: "https://zencare.org/online-zendo", event_url: "https://zencare.org/online-zendo",
  },

  // Tibet House US — Lunchtime Meditation Mon-Fri 1pm ET (online)
  // No iCal feed (WordPress + Elementor). Seeded for quarterly refresh.
  {
    org_id: "tibet_house_us", org_name: "Tibet House US",
    title: "Lunchtime Meditation",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    time: { h: 13, m: 0 }, duration_min: 45,
    address: "22 W 15th St", city: "Manhattan", state: "NY", neighborhood: "Chelsea / Flatiron",
    lat: 40.7382, lng: -73.9972, tradition: "tibetan", location_type: "online",
    notes: "Free daily online meditation 1:00–1:45pm ET. Rotating teachers from Buddhist and contemplative traditions. Zoom. Register at thus.org/lunchtime-meditation.",
    source_url: "https://thus.org", event_url: "https://thus.org/lunchtime-meditation",
  },

  // ── NYC Phase 3c — New York Zendo Shobo-Ji (Zen Studies Society) ─────────────
  // iCal feed available (see abraxis_ingest.py) but daily sits seeded here as safety net.
  {
    org_id: "zenstudies_nyc", org_name: "New York Zendo Shobo-Ji",
    title: "Morning Zazen",
    days: ["Monday","Tuesday","Wednesday","Thursday"],
    time: { h: 6, m: 45 }, duration_min: 60,
    address: "223 E 67th St", city: "Manhattan", state: "NY", neighborhood: "Upper East Side",
    lat: 40.7657, lng: -73.9600, tradition: "zen", location_type: "in-person",
    notes: "Rinzai Zen. 6:45–7:45am. Open to the public. Arrive before 6:45am — late arrivals may not be admitted during zazen. No registration required.",
    source_url: "https://zenstudies.org/new-york-zendo/", event_url: "https://zenstudies.org/new-york-zendo/regular-schedule/",
  },
  {
    org_id: "zenstudies_nyc", org_name: "New York Zendo Shobo-Ji",
    title: "Evening Zazen",
    days: ["Monday","Tuesday","Wednesday"],
    time: { h: 19, m: 0 }, duration_min: 120,
    address: "223 E 67th St", city: "Manhattan", state: "NY", neighborhood: "Upper East Side",
    lat: 40.7657, lng: -73.9600, tradition: "zen", location_type: "in-person",
    notes: "Rinzai Zen. 7:00–9:00pm. Evening sitting, chanting, and instruction. Open to the public. Arrive before 7pm — late arrivals may not be admitted during zazen.",
    source_url: "https://zenstudies.org/new-york-zendo/", event_url: "https://zenstudies.org/new-york-zendo/regular-schedule/",
  },
  {
    org_id: "zenstudies_nyc", org_name: "New York Zendo Shobo-Ji",
    title: "Sunday Morning Service and Zazen",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 180,
    address: "223 E 67th St", city: "Manhattan", state: "NY", neighborhood: "Upper East Side",
    lat: 40.7657, lng: -73.9600, tradition: "zen", location_type: "hybrid",
    notes: "10am–1pm. Full Sunday service: zazen, chanting, dharma talk. In-person at the zendo and livestreamed online. All are welcome.",
    source_url: "https://zenstudies.org/new-york-zendo/", event_url: "https://zenstudies.org/new-york-zendo/regular-schedule/",
  },

  // ── NYC Phase 3c — Zen Center of New York City / Fire Lotus Temple (ZCNYC) ────
  // HTML-scraped via abraxis_ingest.py (zcnyc.org/calendar/) but Sunday program seeded here.
  {
    org_id: "zcnyc", org_name: "Zen Center of New York City (Fire Lotus Temple)",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 180,
    address: "500 State St", city: "Brooklyn", state: "NY", neighborhood: "Boerum Hill",
    lat: 40.6824, lng: -73.9887, tradition: "zen", location_type: "in-person",
    notes: "9:30am–12:30pm. Zazen, beginning instruction, dharma talk, liturgy. Soto Zen (Mountains and Rivers Order). All welcome, no prior experience needed.",
    source_url: "https://zcnyc.org", event_url: "https://zcnyc.org/practice/",
  },
  {
    org_id: "zcnyc", org_name: "Zen Center of New York City (Fire Lotus Temple)",
    title: "LGBTQIA+ Sitting Group",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 90,
    week_of_month: 1,
    address: "500 State St", city: "Brooklyn", state: "NY", neighborhood: "Boerum Hill",
    lat: 40.6824, lng: -73.9887, tradition: "zen", location_type: "online",
    identity_focus: "LGBTQ+",
    notes: "1st and 3rd Tuesdays 6pm ET, online via Zoom. Open to LGBTQIA+ practitioners. Soto Zen practice.",
    source_url: "https://zcnyc.org", event_url: "https://zcnyc.org/practice/",
  },
  {
    org_id: "zcnyc", org_name: "Zen Center of New York City (Fire Lotus Temple)",
    title: "LGBTQIA+ Sitting Group",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 90,
    week_of_month: 3,
    address: "500 State St", city: "Brooklyn", state: "NY", neighborhood: "Boerum Hill",
    lat: 40.6824, lng: -73.9887, tradition: "zen", location_type: "online",
    identity_focus: "LGBTQ+",
    notes: "1st and 3rd Tuesdays 6pm ET, online via Zoom. Open to LGBTQIA+ practitioners. Soto Zen practice.",
    source_url: "https://zcnyc.org", event_url: "https://zcnyc.org/practice/",
  },
  // ── Boston / Cambridge ────────────────────────────────────────────────────
  // Greater Boston Zen Center (GBZC) — Central Square, Cambridge
  {
    org_id: "gbzc", org_name: "Greater Boston Zen Center",
    title: "Tuesday Evening Program",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "552 Massachusetts Ave, Suite 208", city: "Cambridge", state: "MA", neighborhood: "Central Square",
    lat: 42.3638, lng: -71.1059, tradition: "zen", location_type: "hybrid",
    notes: "Hybrid in-person + Zoom. Zazen, dharma talk, and discussion. Drop-in welcome, dana-based.",
    source_url: "https://bostonzen.org", event_url: "https://bostonzen.org/schedule/",
  },
  {
    org_id: "gbzc", org_name: "Greater Boston Zen Center",
    title: "Saturday Morning Practice",
    days: ["Saturday"], time: { h: 9, m: 0 }, duration_min: 50,
    address: "552 Massachusetts Ave, Suite 208", city: "Cambridge", state: "MA", neighborhood: "Central Square",
    lat: 42.3638, lng: -71.1059, tradition: "zen", location_type: "online",
    notes: "Online only via Zoom. Zazen and optional dharma discussion.",
    source_url: "https://bostonzen.org", event_url: "https://bostonzen.org/schedule/",
  },
  // Cambridge Insight Meditation Center (CIMC) — Cambridgeport
  {
    org_id: "cimc", org_name: "Cambridge Insight Meditation Center",
    title: "Monday Sitting & Sangha",
    days: ["Monday"], time: { h: 18, m: 0 }, duration_min: 75,
    address: "331 Broadway", city: "Cambridge", state: "MA", neighborhood: "MIT/Cambridgeport",
    lat: 42.3652, lng: -71.1107, tradition: "theravada", location_type: "in-person",
    notes: "Weekly sit with dharma sharing. Drop-in, free (donations welcome). Part of CIMC's regular schedule.",
    source_url: "https://cambridgeinsight.org", event_url: "https://cambridgeinsight.org/practice-groups/",
  },
  {
    org_id: "cimc", org_name: "Cambridge Insight Meditation Center",
    title: "Evening Sit",
    days: ["Tuesday", "Thursday", "Friday"], time: { h: 18, m: 0 }, duration_min: 45,
    address: "331 Broadway", city: "Cambridge", state: "MA", neighborhood: "MIT/Cambridgeport",
    lat: 42.3652, lng: -71.1107, tradition: "theravada", location_type: "in-person",
    notes: "Drop-in 45-minute sit. No instruction — for practitioners with some meditation experience.",
    source_url: "https://cambridgeinsight.org", event_url: "https://cambridgeinsight.org/practice-groups/",
  },
  // Cambridge Zen Center — Cambridgeport
  {
    org_id: "cambridge_zen", org_name: "Cambridge Zen Center",
    title: "Tuesday Evening Zazen",
    days: ["Tuesday"], time: { h: 19, m: 30 }, duration_min: 70,
    address: "199 Auburn St", city: "Cambridge", state: "MA", neighborhood: "Cambridgeport",
    lat: 42.3620, lng: -71.1176, tradition: "zen", location_type: "hybrid",
    notes: "Hybrid in-person + Zoom. Kwan Um School of Zen. Drop-in welcome.",
    source_url: "https://cambridgezen.org", event_url: "https://cambridgezen.org/schedule/",
  },
  {
    org_id: "cambridge_zen", org_name: "Cambridge Zen Center",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 120,
    address: "199 Auburn St", city: "Cambridge", state: "MA", neighborhood: "Cambridgeport",
    lat: 42.3620, lng: -71.1176, tradition: "zen", location_type: "hybrid",
    notes: "Four 30-minute sitting periods with kinhin (walking meditation). Hybrid in-person + Zoom. Drop-in welcome.",
    source_url: "https://cambridgezen.org", event_url: "https://cambridgezen.org/schedule/",
  },
  // Kadampa Meditation Center Boston — North Cambridge
  {
    org_id: "kadampa_boston", org_name: "Kadampa Meditation Center Boston",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "2298 Massachusetts Ave", city: "Cambridge", state: "MA", neighborhood: "North Cambridge",
    lat: 42.3852, lng: -71.1248, tradition: "tibetan", location_type: "in-person",
    notes: "New Kadampa Tradition (NKT). Guided meditation class. Drop-in, beginners welcome.",
    source_url: "https://meditationinboston.org", event_url: "https://meditationinboston.org/wednesdays-in-cambridge",
  },
  {
    org_id: "kadampa_boston", org_name: "Kadampa Meditation Center Boston",
    title: "Sunday Meditation",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 90,
    address: "2298 Massachusetts Ave", city: "Cambridge", state: "MA", neighborhood: "North Cambridge",
    lat: 42.3852, lng: -71.1248, tradition: "tibetan", location_type: "in-person",
    notes: "New Kadampa Tradition (NKT). Guided meditation class. Drop-in, beginners welcome.",
    source_url: "https://meditationinboston.org", event_url: "https://meditationinboston.org/sundays-in-cambridge",
  },

  // ── Washington DC Metro ────────────────────────────────────────────────────
  // DC Shambhala Center — first Sunday monthly, 1:30pm at Seekers Church
  {
    org_id: "shambhala_dc", org_name: "Shambhala Meditation Center of Washington DC",
    title: "Open Public Sitting",
    days: ["Sunday"], week_of_month: 1, time: { h: 13, m: 30 }, duration_min: 60,
    address: "276 Carroll St NW", city: "Washington", state: "DC", neighborhood: "Takoma",
    lat: 38.9776, lng: -77.0128, tradition: "tibetan", location_type: "in-person",
    notes: "First Sunday monthly. Free meditation instruction available 1:15–1:30pm. Tea and dharma video/talk follows sitting.",
    source_url: "https://dc.shambhala.org", event_url: "https://dc.shambhala.org/monthly-calendar/",
  },

  // ── Seattle, WA ───────────────────────────────────────────────────────────
  // Shambhala Seattle — iCal blocked by Cloudflare; seeded from website schedule
  {
    org_id: "shambhala_seattle", org_name: "Shambhala Meditation Center of Seattle",
    title: "Thursday Evening Open House",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3107 E Harrison St", city: "Seattle", state: "WA", neighborhood: "Capitol Hill",
    lat: 47.6197, lng: -122.3023, tradition: "tibetan", location_type: "in-person",
    notes: "Open house meditation 7–8:30pm. All welcome, free meditation instruction available.",
    source_url: "https://seattle.shambhala.org", event_url: "https://seattle.shambhala.org/calendar/",
  },
  {
    org_id: "shambhala_seattle", org_name: "Shambhala Meditation Center of Seattle",
    title: "Sunday Morning Open House",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "3107 E Harrison St", city: "Seattle", state: "WA", neighborhood: "Capitol Hill",
    lat: 47.6197, lng: -122.3023, tradition: "tibetan", location_type: "in-person",
    notes: "Open house meditation 10–11:30am. All welcome.",
    source_url: "https://seattle.shambhala.org", event_url: "https://seattle.shambhala.org/calendar/",
  },
  {
    org_id: "shambhala_seattle", org_name: "Shambhala Meditation Center of Seattle",
    title: "Shambhala Practice Night",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 60,
    address: "3107 E Harrison St", city: "Seattle", state: "WA", neighborhood: "Capitol Hill",
    lat: 47.6197, lng: -122.3023, tradition: "tibetan", location_type: "online",
    notes: "Online meditation practice night 6:30pm. Zoom link via seattle.shambhala.org.",
    source_url: "https://seattle.shambhala.org", event_url: "https://seattle.shambhala.org/calendar/",
  },
  {
    org_id: "shambhala_seattle", org_name: "Shambhala Meditation Center of Seattle",
    title: "Heart of Recovery",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "3107 E Harrison St", city: "Seattle", state: "WA", neighborhood: "Capitol Hill",
    lat: 47.6197, lng: -122.3023, tradition: "tibetan", location_type: "hybrid",
    notes: "Hybrid meditation group for people in recovery. 7pm Wednesdays.",
    source_url: "https://seattle.shambhala.org", event_url: "https://seattle.shambhala.org/calendar/",
  },
  // Seattle Buddhist Center (Triratna) — no iCal
  {
    org_id: "seattle_buddhist_center", org_name: "Seattle Buddhist Center",
    title: "Thursday Night Meditation",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "12056 15th Ave NE, Suite C-2", city: "Seattle", state: "WA", neighborhood: "Northgate / Pinehurst",
    lat: 47.7203, lng: -122.3145, tradition: "pluralist", location_type: "in-person",
    notes: "Triratna Buddhist Community. 7–8pm in-person. Drop-in welcome.",
    source_url: "https://seattlebuddhistcenter.org", event_url: "https://seattlebuddhistcenter.org/events/",
  },
  {
    org_id: "seattle_buddhist_center", org_name: "Seattle Buddhist Center",
    title: "Sunday Sangha Night",
    days: ["Sunday"], time: { h: 18, m: 0 }, duration_min: 120,
    address: "12056 15th Ave NE, Suite C-2", city: "Seattle", state: "WA", neighborhood: "Northgate / Pinehurst",
    lat: 47.7203, lng: -122.3145, tradition: "pluralist", location_type: "in-person",
    notes: "Triratna Buddhist Community. 6–8pm in-person, dharma discussion and meditation. Drop-in welcome.",
    source_url: "https://seattlebuddhistcenter.org", event_url: "https://seattlebuddhistcenter.org/events/",
  },

  // ── Denver / Boulder, CO ──────────────────────────────────────────────────
  // Boulder Shambhala Center — Cologne iCal server down
  {
    org_id: "shambhala_boulder", org_name: "Boulder Shambhala Center",
    title: "Thursday Night Open Class",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 105,
    address: "1345 Spruce St", city: "Boulder", state: "CO", neighborhood: "Central Boulder",
    lat: 40.0150, lng: -105.2705, tradition: "tibetan", location_type: "in-person",
    notes: "7–8:45pm in-person. Shambhala Buddhist tradition. All welcome, free meditation instruction available.",
    source_url: "https://boulder.shambhala.org", event_url: "https://boulder.shambhala.org/calendar/",
  },
  // Denver Shambhala Center — Cologne iCal server down
  {
    org_id: "shambhala_denver", org_name: "Shambhala Meditation Center of Denver",
    title: "Sunday Group Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "2305 S Syracuse Way, Suite 214", city: "Denver", state: "CO", neighborhood: "Hampden South / Tamarac Square",
    lat: 39.6519, lng: -104.8822, tradition: "tibetan", location_type: "in-person",
    notes: "10am Sunday in-person. Shambhala Buddhist tradition. Free meditation instruction available before session.",
    source_url: "https://denver.shambhala.org", event_url: "https://denver.shambhala.org/calendar/",
  },

  // ── Portland, OR ──────────────────────────────────────────────────────────
  // Portland Insight Meditation Community (PIMC) — Wix site, no iCal
  {
    org_id: "portland_insight", org_name: "Portland Insight Meditation Community",
    title: "Sunday Morning Sit & Dharma Talk",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 90,
    address: "6536 SE Duke St", city: "Portland", state: "OR", neighborhood: "Brentwood-Darlington",
    lat: 45.4738, lng: -122.6186, tradition: "theravada", location_type: "hybrid",
    notes: "Theravada Vipassana (Ruth Denison lineage). In-person + Zoom. Drop-in welcome.",
    source_url: "https://www.portlandinsight.org", event_url: "https://www.portlandinsight.org/weeklygroups",
  },
  {
    org_id: "portland_insight", org_name: "Portland Insight Meditation Community",
    title: "Monday Morning Sit",
    days: ["Monday"], time: { h: 7, m: 30 }, duration_min: 45,
    address: "6536 SE Duke St", city: "Portland", state: "OR", neighborhood: "Brentwood-Darlington",
    lat: 45.4738, lng: -122.6186, tradition: "theravada", location_type: "hybrid",
    notes: "Morning sit with poem, 45-min meditation, group discussion. Online + some in-person.",
    source_url: "https://www.portlandinsight.org", event_url: "https://www.portlandinsight.org/weeklygroups",
  },
  {
    org_id: "portland_insight", org_name: "Portland Insight Meditation Community",
    title: "Tuesday Evening Sangha",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "6536 SE Duke St", city: "Portland", state: "OR", neighborhood: "Brentwood-Darlington",
    lat: 45.4738, lng: -122.6186, tradition: "theravada", location_type: "in-person",
    notes: "In-person weekly group. 6:30–8pm. Drop-in welcome.",
    source_url: "https://www.portlandinsight.org", event_url: "https://www.portlandinsight.org/weeklygroups",
  },
  {
    org_id: "portland_insight", org_name: "Portland Insight Meditation Community",
    title: "Heart of Freedom Meditation Class",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "6536 SE Duke St", city: "Portland", state: "OR", neighborhood: "Brentwood-Darlington",
    lat: 45.4738, lng: -122.6186, tradition: "theravada", location_type: "hybrid",
    notes: "Guided meditation, compassion and wisdom teachings, Q&A. Hybrid in-person + online.",
    source_url: "https://www.portlandinsight.org", event_url: "https://www.portlandinsight.org/weeklygroups",
  },
  // Portland Shambhala — dynamic FullCalendar, no static iCal feed
  {
    org_id: "shambhala_portland", org_name: "Portland Shambhala Meditation Center",
    title: "Decompress + Connect Evening Meditation",
    days: ["Monday", "Friday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "1404 SE 25th Ave", city: "Portland", state: "OR", neighborhood: "Buckman / Richmond",
    lat: 45.5168, lng: -122.6434, tradition: "tibetan", location_type: "in-person",
    notes: "In-person meditation group at 1404 SE 25th Ave. Shambhala Buddhist tradition. All welcome.",
    source_url: "https://portland.shambhala.org", event_url: "https://portland.shambhala.org/calendar/",
  },
  {
    org_id: "shambhala_portland", org_name: "Portland Shambhala Meditation Center",
    title: "Sunday Community Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "1404 SE 25th Ave", city: "Portland", state: "OR", neighborhood: "Buckman / Richmond",
    lat: 45.5168, lng: -122.6434, tradition: "tibetan", location_type: "online",
    notes: "Online Sunday morning meditation. Zoom link via portland.shambhala.org.",
    source_url: "https://portland.shambhala.org", event_url: "https://portland.shambhala.org/calendar/",
  },

  // ── Austin, TX ────────────────────────────────────────────────────────────
  // Austin Zen Center — site under maintenance 2026-05-08; schedule from archived content
  // Soto Zen, Hyde Park, Central Austin. Full residential + lay schedule.
  {
    org_id: "austin_zen", org_name: "Austin Zen Center",
    title: "Morning Zazen",
    days: ["Tuesday", "Wednesday", "Thursday", "Friday"], time: { h: 6, m: 0 }, duration_min: 90,
    address: "3014 Washington Square", city: "Austin", state: "TX", neighborhood: "Hyde Park / Central Austin",
    lat: 30.3073, lng: -97.7421, tradition: "zen", location_type: "in-person",
    notes: "Morning Program: 6:00am zazen, 6:35am kinhin, 6:45am zazen, 7:20am service. Soto Zen. Drop-in welcome.",
    source_url: "https://austinzencenter.org", event_url: "https://austinzencenter.org/event-calendar/",
  },
  {
    org_id: "austin_zen", org_name: "Austin Zen Center",
    title: "Midday Zazen",
    days: ["Tuesday", "Wednesday", "Thursday"], time: { h: 12, m: 0 }, duration_min: 60,
    address: "3014 Washington Square", city: "Austin", state: "TX", neighborhood: "Hyde Park / Central Austin",
    lat: 30.3073, lng: -97.7421, tradition: "zen", location_type: "in-person",
    notes: "Informal zazen 12–1pm. Open to all.",
    source_url: "https://austinzencenter.org", event_url: "https://austinzencenter.org/event-calendar/",
  },
  {
    org_id: "austin_zen", org_name: "Austin Zen Center",
    title: "Evening Zazen",
    days: ["Tuesday", "Wednesday", "Thursday"], time: { h: 17, m: 40 }, duration_min: 45,
    address: "3014 Washington Square", city: "Austin", state: "TX", neighborhood: "Hyde Park / Central Austin",
    lat: 30.3073, lng: -97.7421, tradition: "zen", location_type: "in-person",
    notes: "Evening Program: 5:40pm zazen, 6:15pm service. No evening program on Fridays.",
    source_url: "https://austinzencenter.org", event_url: "https://austinzencenter.org/event-calendar/",
  },
  {
    org_id: "austin_zen", org_name: "Austin Zen Center",
    title: "Saturday Zazen & Dharma Talk",
    days: ["Saturday"], time: { h: 9, m: 15 }, duration_min: 120,
    address: "3014 Washington Square", city: "Austin", state: "TX", neighborhood: "Hyde Park / Central Austin",
    lat: 30.3073, lng: -97.7421, tradition: "zen", location_type: "in-person",
    notes: "Saturday Program: 8am informal zazen + beginner instruction (most Saturdays), 9:15am zazen, 10:15am Dharma talk, 11:15am tea.",
    source_url: "https://austinzencenter.org", event_url: "https://austinzencenter.org/event-calendar/",
  },

  // ── Minneapolis / Saint Paul, MN ──────────────────────────────────────────
  // Minnesota Zen Meditation Center — Squarespace (no iCal)
  // Dainin Katagiri Roshi lineage. 3343 East Bde Maka Ska Pkwy, Minneapolis.
  {
    org_id: "mn_zen", org_name: "Minnesota Zen Meditation Center",
    title: "Morning Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "3343 East Bde Maka Ska Pkwy", city: "Minneapolis", state: "MN", neighborhood: "Lakewood / Bde Maka Ska",
    lat: 44.9434, lng: -93.3173, tradition: "zen", location_type: "in-person",
    notes: "Weekday morning zazen 6:30am. Drop-in welcome.",
    source_url: "https://mnzencenter.org", event_url: "https://mnzencenter.org/calendar/",
  },
  {
    org_id: "mn_zen", org_name: "Minnesota Zen Meditation Center",
    title: "Morning Zazen",
    days: ["Saturday", "Sunday"], time: { h: 7, m: 30 }, duration_min: 60,
    address: "3343 East Bde Maka Ska Pkwy", city: "Minneapolis", state: "MN", neighborhood: "Lakewood / Bde Maka Ska",
    lat: 44.9434, lng: -93.3173, tradition: "zen", location_type: "in-person",
    notes: "Weekend morning zazen 7:30am. Drop-in welcome.",
    source_url: "https://mnzencenter.org", event_url: "https://mnzencenter.org/calendar/",
  },
  {
    org_id: "mn_zen", org_name: "Minnesota Zen Meditation Center",
    title: "Evening Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday"], time: { h: 17, m: 30 }, duration_min: 60,
    address: "3343 East Bde Maka Ska Pkwy", city: "Minneapolis", state: "MN", neighborhood: "Lakewood / Bde Maka Ska",
    lat: 44.9434, lng: -93.3173, tradition: "zen", location_type: "in-person",
    notes: "Weekday evening zazen 5:30pm (Mon–Thu). Drop-in welcome.",
    source_url: "https://mnzencenter.org", event_url: "https://mnzencenter.org/calendar/",
  },
  {
    org_id: "mn_zen", org_name: "Minnesota Zen Meditation Center",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 120,
    address: "3343 East Bde Maka Ska Pkwy", city: "Minneapolis", state: "MN", neighborhood: "Lakewood / Bde Maka Ska",
    lat: 44.9434, lng: -93.3173, tradition: "zen", location_type: "in-person",
    notes: "Sunday Morning Program 9:30am: zazen, kinhin, service, dharma talk. Drop-in welcome.",
    source_url: "https://mnzencenter.org", event_url: "https://mnzencenter.org/calendar/",
  },

  // Clouds in Water Zen Center — Squarespace (no iCal)
  // Soto Zen. 308 Prince St, Lowertown, Saint Paul.
  {
    org_id: "clouds_in_water", org_name: "Clouds in Water Zen Center",
    title: "Morning Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], time: { h: 7, m: 0 }, duration_min: 90,
    address: "308 Prince St", city: "Saint Paul", state: "MN", neighborhood: "Lowertown / Saint Paul",
    lat: 44.9397, lng: -93.0961, tradition: "zen", location_type: "in-person",
    notes: "Morning zazen 7–8:30am, Mon–Fri. Wednesday adds dharma study after zazen. Drop-in welcome.",
    source_url: "https://cloudsinwater.org", event_url: "https://cloudsinwater.org/calendar",
  },
  {
    org_id: "clouds_in_water", org_name: "Clouds in Water Zen Center",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 120,
    address: "308 Prince St", city: "Saint Paul", state: "MN", neighborhood: "Lowertown / Saint Paul",
    lat: 44.9397, lng: -93.0961, tradition: "zen", location_type: "in-person",
    notes: "Sunday morning 9:30am zazen + dharma talk. Drop-in welcome.",
    source_url: "https://cloudsinwater.org", event_url: "https://cloudsinwater.org/calendar",
  },

  // Shambhala Meditation Center of Minneapolis — Cloudflare-blocked (no iCal)
  // 1544 Nicollet Ave, Whittier, Minneapolis.
  {
    org_id: "shambhala_minneapolis", org_name: "Shambhala Meditation Center of Minneapolis",
    title: "Community Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "1544 Nicollet Ave", city: "Minneapolis", state: "MN", neighborhood: "Whittier",
    lat: 44.9657, lng: -93.2896, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly community meditation. Shambhala tradition (Chögyam Trungpa lineage). All welcome.",
    source_url: "https://minneapolis.shambhala.org", event_url: "https://minneapolis.shambhala.org/calendar/",
  },

  // ── Phoenix, AZ ───────────────────────────────────────────────────────────
  // Kadampa Meditation Center Phoenix — Wix site (no iCal). NKT-IKBU.
  // 614 East Townley Ave, Sunnyslope / North Phoenix. Verified 2026-05-09.
  // Schedule from site nav: Sunday Morning, Monday Evening, Wednesday Evening GPs.
  // Standard NKT General Program times used (7pm weeknight, 11am Sunday).
  {
    org_id: "kadampa_phoenix", org_name: "Kadampa Meditation Center Phoenix",
    title: "Sunday Morning Meditation Class",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 90,
    address: "614 East Townley Ave", city: "Phoenix", state: "AZ", neighborhood: "Sunnyslope / North Phoenix",
    lat: 33.5731, lng: -112.0539, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome, no experience needed.",
    source_url: "https://www.meditationinarizona.org", event_url: "https://www.meditationinarizona.org/sunday-morning",
  },
  {
    org_id: "kadampa_phoenix", org_name: "Kadampa Meditation Center Phoenix",
    title: "Monday Evening Meditation Class",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "614 East Townley Ave", city: "Phoenix", state: "AZ", neighborhood: "Sunnyslope / North Phoenix",
    lat: 33.5731, lng: -112.0539, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome.",
    source_url: "https://www.meditationinarizona.org", event_url: "https://www.meditationinarizona.org/monday-evening",
  },
  {
    org_id: "kadampa_phoenix", org_name: "Kadampa Meditation Center Phoenix",
    title: "Wednesday Evening Meditation Class",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "614 East Townley Ave", city: "Phoenix", state: "AZ", neighborhood: "Sunnyslope / North Phoenix",
    lat: 33.5731, lng: -112.0539, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome.",
    source_url: "https://www.meditationinarizona.org", event_url: "https://www.meditationinarizona.org/wednesday-evening",
  },

  // ── Houston, TX ────────────────────────────────────────────────────────────
  {
    org_id: "insight_meditation_houston", org_name: "Insight Meditation Houston",
    title: "Monday Evening Meditation & Dharma Talk",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "4949 Caroline St", city: "Houston", state: "TX", neighborhood: "Museum District / Midtown",
    lat: 29.7268, lng: -95.3836, tradition: "theravada", location_type: "hybrid",
    notes: "Vipassana / Insight Meditation sit + dharma talk. At Covenant Church, Building B (Huff Fellowship Hall). Also via Zoom (ID: 848 4819 9460). Free; donations welcome. Held most Mondays except federal holidays.",
    source_url: "https://insighthouston.org", event_url: "https://insighthouston.org/events",
  },
  {
    org_id: "diamond_way_houston", org_name: "Diamond Way Buddhist Center Houston",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 30 }, duration_min: 30,
    address: "5102 Center St", city: "Houston", state: "TX", neighborhood: "Heights / Washington Corridor",
    lat: 29.7653, lng: -95.3987, tradition: "tibetan", location_type: "in-person",
    notes: "Short Buddhist teaching + guided Guru Yoga meditation (~30 min). Karma Kagyu lineage (Diamond Way, Lama Ole Nydahl). Free; donations welcome. All are welcome.",
    source_url: "https://diamondway.org/houston/", event_url: "https://diamondway.org/houston/events/",
  },
  // Houston Zen Center — daily zazen (The Heights neighborhood, 1605 Heights Blvd)
  // Schedule: houstonzen.org/schedule-of-meditation
  {
    org_id: "houston_zen", org_name: "Houston Zen Center",
    title: "Morning Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday"], time: { h: 5, m: 50 }, duration_min: 85,
    address: "1605 Heights Blvd", city: "Houston", state: "TX", neighborhood: "The Heights",
    lat: 29.8004, lng: -95.3984, tradition: "zen", location_type: "hybrid",
    notes: "Morning zazen at Houston Zen Center. Two periods: 5:50–6:30am (zazen), 6:30am kinhin, 6:40–7:10am (zazen). Chanting 7:10–7:15am. Virtual participation via Zoom Zendo. In-person and online. Free; all welcome.",
    source_url: "https://houstonzen.org", event_url: "https://houstonzen.org/schedule-of-meditation",
  },
  {
    org_id: "houston_zen", org_name: "Houston Zen Center",
    title: "Evening Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday"], time: { h: 17, m: 30 }, duration_min: 40,
    address: "1605 Heights Blvd", city: "Houston", state: "TX", neighborhood: "The Heights",
    lat: 29.8004, lng: -95.3984, tradition: "zen", location_type: "hybrid",
    notes: "Evening zazen period at Houston Zen Center, 5:30–6:10pm. In-person and via Zoom Zendo. Free; all welcome.",
    source_url: "https://houstonzen.org", event_url: "https://houstonzen.org/schedule-of-meditation",
  },
  {
    org_id: "houston_zen", org_name: "Houston Zen Center",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 8, m: 20 }, duration_min: 40,
    address: "1605 Heights Blvd", city: "Houston", state: "TX", neighborhood: "The Heights",
    lat: 29.8004, lng: -95.3984, tradition: "zen", location_type: "hybrid",
    notes: "Saturday morning zazen, 8:20–9:00am. In-person and via Zoom Zendo. Free; all welcome.",
    source_url: "https://houstonzen.org", event_url: "https://houstonzen.org/schedule-of-meditation",
  },
  {
    org_id: "houston_zen", org_name: "Houston Zen Center",
    title: "Sunday Zazen",
    days: ["Sunday"], time: { h: 8, m: 50 }, duration_min: 30,
    address: "1605 Heights Blvd", city: "Houston", state: "TX", neighborhood: "The Heights",
    lat: 29.8004, lng: -95.3984, tradition: "zen", location_type: "hybrid",
    notes: "Sunday zazen, part of the full Sunday Program (8:20am–noon). Preceded by chanting at 8:20am; followed by newcomer orientation at 9:20am and dharma talk at 9:45am. In-person and Zoom. Free; all welcome.",
    source_url: "https://houstonzen.org", event_url: "https://houstonzen.org/sunday-program",
  },
  // ── Drepung Loseling Institute of Texas (Westbury, SW Houston) ─────────────
  // Gelugpa Tibetan Buddhist center affiliated with Drepung Loseling Monastery.
  // Schedule from drepungloselinginstitute.org (Wix site, no iCal — seeded as recurring)
  {
    org_id: "drepung_loseling_texas", org_name: "Drepung Loseling Institute of Texas",
    title: "Thursday Morning Practice",
    days: ["Thursday"], time: { h: 7, m: 0 }, duration_min: 120,
    address: "11510 S Garden St", city: "Houston", state: "TX", neighborhood: "Westbury / Southwest Houston",
    lat: 29.6620, lng: -95.4908, tradition: "tibetan", location_type: "in_person",
    notes: "Weekly Thursday morning Tibetan Buddhist practice session, 7–9am. Gelugpa lineage (Drepung Loseling Monastery / His Holiness the 14th Dalai Lama). Includes meditation, prayers, and practice instruction. All are welcome; no experience necessary.",
    source_url: "https://www.drepungloselinginstitute.org", event_url: "https://www.drepungloselinginstitute.org/schedule",
  },
  {
    org_id: "drepung_loseling_texas", org_name: "Drepung Loseling Institute of Texas",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "11510 S Garden St", city: "Houston", state: "TX", neighborhood: "Westbury / Southwest Houston",
    lat: 29.6620, lng: -95.4908, tradition: "tibetan", location_type: "in_person",
    notes: "Sunday morning Tibetan Buddhist program, 10am–noon. Gelugpa lineage (Drepung Loseling Monastery). Meditation, teachings, and traditional practice. All welcome.",
    source_url: "https://www.drepungloselinginstitute.org", event_url: "https://www.drepungloselinginstitute.org/schedule",
  },
  {
    org_id: "drepung_loseling_texas", org_name: "Drepung Loseling Institute of Texas",
    title: "Sunday Afternoon Program",
    days: ["Sunday"], time: { h: 15, m: 0 }, duration_min: 240,
    address: "11510 S Garden St", city: "Houston", state: "TX", neighborhood: "Westbury / Southwest Houston",
    lat: 29.6620, lng: -95.4908, tradition: "tibetan", location_type: "in_person",
    notes: "Sunday afternoon Tibetan Buddhist program, 3–7pm. Gelugpa lineage (Drepung Loseling Monastery). Extended session with meditation, dharma teachings, and ritual practice. All welcome.",
    source_url: "https://www.drepungloselinginstitute.org", event_url: "https://www.drepungloselinginstitute.org/schedule",
  },

  // ── San Diego, CA ────────────────────────────────────────────────────────────
  // KMC San Diego — 3502 Adams Ave, Normal Heights. No iCal; schedule from meditateinsandiego.org.
  {
    org_id: "kmc_san_diego", org_name: "Kadampa Meditation Center San Diego",
    title: "Sunday Morning Meditation Class",
    days: ["Sunday"], time: { h: 10, m: 30 }, duration_min: 75,
    address: "3502 Adams Ave", city: "San Diego", state: "CA", neighborhood: "Normal Heights / North Park",
    lat: 32.7437, lng: -117.1381, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome, no experience needed.",
    source_url: "https://meditateinsandiego.org", event_url: "https://meditateinsandiego.org/events/",
  },
  {
    org_id: "kmc_san_diego", org_name: "Kadampa Meditation Center San Diego",
    title: "Monday Evening Meditation Class",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 75,
    address: "3502 Adams Ave", city: "San Diego", state: "CA", neighborhood: "Normal Heights / North Park",
    lat: 32.7437, lng: -117.1381, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome.",
    source_url: "https://meditateinsandiego.org", event_url: "https://meditateinsandiego.org/events/",
  },
  {
    org_id: "kmc_san_diego", org_name: "Kadampa Meditation Center San Diego",
    title: "Thursday Evening Meditation Class",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 75,
    address: "3502 Adams Ave", city: "San Diego", state: "CA", neighborhood: "Normal Heights / North Park",
    lat: 32.7437, lng: -117.1381, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome.",
    source_url: "https://meditateinsandiego.org", event_url: "https://meditateinsandiego.org/events/",
  },

  // ── Miami / South Florida, FL ───────────────────────────────────────────────
  // KMC Miami — Coral Gables (316 Miracle Mile). No iCal; schedule from meditationinmiami.org.
  {
    org_id: "kmc_miami", org_name: "Kadampa Meditation Center Miami",
    title: "Sunday Morning Meditation Class",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 60,
    address: "316 Miracle Mile", city: "Coral Gables", state: "FL", neighborhood: "Coral Gables / Downtown Miami",
    lat: 25.7474, lng: -80.2575, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome, no experience needed.",
    source_url: "https://meditationinmiami.org", event_url: "https://meditationinmiami.org/calendar/",
  },
  {
    org_id: "kmc_miami", org_name: "Kadampa Meditation Center Miami",
    title: "Monday Evening Meditation Class",
    days: ["Monday"], time: { h: 19, m: 30 }, duration_min: 60,
    address: "316 Miracle Mile", city: "Coral Gables", state: "FL", neighborhood: "Coral Gables / Downtown Miami",
    lat: 25.7474, lng: -80.2575, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome.",
    source_url: "https://meditationinmiami.org", event_url: "https://meditationinmiami.org/calendar/",
  },
  {
    org_id: "kmc_miami", org_name: "Kadampa Meditation Center Miami",
    title: "Clase de Meditación del Martes (Español)",
    days: ["Tuesday"], time: { h: 19, m: 30 }, duration_min: 60,
    address: "316 Miracle Mile", city: "Coral Gables", state: "FL", neighborhood: "Coral Gables / Downtown Miami",
    lat: 25.7474, lng: -80.2575, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class taught entirely in Spanish. Meditación guiada + enseñanza del dharma. Todos son bienvenidos.",
    source_url: "https://meditationinmiami.org", event_url: "https://meditationinmiami.org/calendar/",
  },
  {
    org_id: "kmc_miami", org_name: "Kadampa Meditation Center Miami",
    title: "Thursday Evening Meditation Class",
    days: ["Thursday"], time: { h: 19, m: 30 }, duration_min: 60,
    address: "316 Miracle Mile", city: "Coral Gables", state: "FL", neighborhood: "Coral Gables / Downtown Miami",
    lat: 25.7474, lng: -80.2575, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome.",
    source_url: "https://meditationinmiami.org", event_url: "https://meditationinmiami.org/calendar/",
  },
  {
    org_id: "kmc_miami", org_name: "Kadampa Meditation Center Miami",
    title: "Friday Lunchtime Meditation",
    days: ["Friday"], time: { h: 12, m: 15 }, duration_min: 30,
    address: "316 Miracle Mile", city: "Coral Gables", state: "FL", neighborhood: "Coral Gables / Downtown Miami",
    lat: 25.7474, lng: -80.2575, tradition: "tibetan", location_type: "in-person",
    notes: "Short lunchtime meditation session, 12:15–12:45pm. Free drop-in; no experience needed.",
    source_url: "https://meditationinmiami.org", event_url: "https://meditationinmiami.org/calendar/",
  },

  // ── Atlanta Soto Zen Center (ASZC) — 1167 Zonolite Pl NE, Suite C, Atlanta GA 30306
  // Squarespace site (no iCal). Schedule from aszc.org.
  {
    org_id: "aszc", org_name: "Atlanta Soto Zen Center",
    title: "Sunrise Sangha",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    time: { h: 6, m: 0 }, duration_min: 50,
    address: "1167 Zonolite Pl NE, Suite C", city: "Atlanta", state: "GA", neighborhood: "Morningside / Lenox",
    lat: 33.8060, lng: -84.3420, tradition: "zen", location_type: "hybrid",
    notes: "Daily morning zazen at 6am, hybrid in-person + Zoom. All experience levels welcome.",
    source_url: "https://www.aszc.org", event_url: "https://www.aszc.org/schedule",
  },
  {
    org_id: "aszc", org_name: "Atlanta Soto Zen Center",
    title: "Introduction to Zen Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "1167 Zonolite Pl NE, Suite C", city: "Atlanta", state: "GA", neighborhood: "Morningside / Lenox",
    lat: 33.8060, lng: -84.3420, tradition: "zen", location_type: "in-person",
    notes: "Drop-in friendly evening zazen with instruction. 7–8:30pm in-person. No experience needed.",
    source_url: "https://www.aszc.org", event_url: "https://www.aszc.org/schedule",
  },
  {
    org_id: "aszc", org_name: "Atlanta Soto Zen Center",
    title: "Sunday Morning Service",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 180,
    address: "1167 Zonolite Pl NE, Suite C", city: "Atlanta", state: "GA", neighborhood: "Morningside / Lenox",
    lat: 33.8060, lng: -84.3420, tradition: "zen", location_type: "hybrid",
    notes: "Sunday program 9am–noon: silent meditation (9–10:30am), chanting, and dharma talk. Hybrid.",
    source_url: "https://www.aszc.org", event_url: "https://www.aszc.org/schedule",
  },

  // ── Kadampa Meditation Center Georgia (KMC Georgia) — 741 Edgewood Ave NE, Atlanta GA 30307
  // Squarespace site (no iCal). Schedule from meditationingeorgia.org.
  {
    org_id: "kmc_georgia", org_name: "Kadampa Meditation Center Georgia",
    title: "Advice for a Happy Life",
    days: ["Sunday"], time: { h: 10, m: 30 }, duration_min: 75,
    address: "741 Edgewood Ave NE", city: "Atlanta", state: "GA", neighborhood: "Inman Park / Old Fourth Ward",
    lat: 33.7565, lng: -84.3560, tradition: "tibetan", location_type: "in-person",
    notes: "General Program class. Guided meditation + Buddhist wisdom on lasting happiness. Drop-in $15.",
    source_url: "https://www.meditationingeorgia.org", event_url: "https://www.meditationingeorgia.org/calendar",
  },
  {
    org_id: "kmc_georgia", org_name: "Kadampa Meditation Center Georgia",
    title: "Meditation for Beginners",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "741 Edgewood Ave NE", city: "Atlanta", state: "GA", neighborhood: "Inman Park / Old Fourth Ward",
    lat: 33.7565, lng: -84.3560, tradition: "tibetan", location_type: "in-person",
    notes: "Beginner-friendly drop-in meditation class. 7–8pm in-person. Drop-in $10.",
    source_url: "https://www.meditationingeorgia.org", event_url: "https://www.meditationingeorgia.org/calendar",
  },
  {
    org_id: "kmc_georgia", org_name: "Kadampa Meditation Center Georgia",
    title: "Modern Buddhism and Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 75,
    address: "741 Edgewood Ave NE", city: "Atlanta", state: "GA", neighborhood: "Inman Park / Old Fourth Ward",
    lat: 33.7565, lng: -84.3560, tradition: "tibetan", location_type: "in-person",
    notes: "General Program class. Guided meditation + dharma teaching on modern Buddhist topics. Drop-in $15.",
    source_url: "https://www.meditationingeorgia.org", event_url: "https://www.meditationingeorgia.org/calendar",
  },

  // ── Drepung Loseling Institute — 1781 Dresden Dr NE, Brookhaven, Atlanta GA 30319
  // Major Gelugpa Tibetan institution, partner of Emory CBCT. Resident monks.
  // Public sits: Sunday 11am Open Meditation (in-person + livestream).
  // Tuesday 7pm Public Talk series handled by static HTML scraper.
  {
    org_id: "drepung_loseling_atlanta", org_name: "Drepung Loseling Institute",
    title: "Sunday Meditation",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 60,
    address: "1781 Dresden Dr NE", city: "Atlanta", state: "GA", neighborhood: "Brookhaven / Lynwood Hills",
    lat: 33.8505, lng: -84.3247, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly open meditation led by resident teacher. In-person at 1781 Dresden Dr NE + livestream. All welcome, no experience needed.",
    source_url: "https://www.drepung.org", event_url: "https://www.drepung.org/changing/calendar/current.htm",
  },

  // ── Philadelphia ────────────────────────────────────────────────────────────────────────
  // Phase 3 Philadelphia — added 2026-05-12.
  // Shambhala iCal (center=210) is down (522); seeding recurring sits instead.

  // ── Shambhala Meditation Center of Philadelphia — 2030 Sansom St, Center City, PA 19103
  // shambhala-koeln.de/ical.php?center=210 — returning 522 as of 2026-05-12. Monitor.
  // Schedule from philadelphia.shambhala.org: Sun 10am drop-in sit, Thu 6pm drop-in sit.
  {
    org_id: "shambhala_philadelphia", org_name: "Shambhala Meditation Center of Philadelphia",
    title: "Sunday Sitting Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "2030 Sansom St", city: "Philadelphia", state: "PA", neighborhood: "Center City West / Rittenhouse Square",
    lat: 39.9518, lng: -75.1748, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly drop-in sitting meditation. In-person. First Sunday of each month is extended: 9:30am–noon.",
    source_url: "https://philadelphia.shambhala.org", event_url: "https://philadelphia.shambhala.org/monthly-calendar/",
  },
  {
    org_id: "shambhala_philadelphia", org_name: "Shambhala Meditation Center of Philadelphia",
    title: "Thursday Sitting Meditation",
    days: ["Thursday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "2030 Sansom St", city: "Philadelphia", state: "PA", neighborhood: "Center City West / Rittenhouse Square",
    lat: 39.9518, lng: -75.1748, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly drop-in sitting meditation. In-person.",
    source_url: "https://philadelphia.shambhala.org", event_url: "https://philadelphia.shambhala.org/monthly-calendar/",
  },

  // ── Kadampa Meditation Center Philadelphia — 47-49 N 2nd St, Old City, PA 19106
  // Wix site (meditationinphiladelphia.org) — no iCal. Schedule from website.
  // Very active daily program; seeding Mon/Wed/Thu evenings and Sunday morning.
  {
    org_id: "kadampa_philadelphia", org_name: "Kadampa Meditation Center Philadelphia",
    title: "Monday Evening Meditation",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 120,
    address: "47-49 N 2nd St", city: "Philadelphia", state: "PA", neighborhood: "Old City",
    lat: 39.9504, lng: -75.1431, tradition: "tibetan", location_type: "in-person",
    notes: "General Program class. Guided meditation + Buddhist teachings. Drop-in welcome.",
    source_url: "https://www.meditationinphiladelphia.org", event_url: "https://www.meditationinphiladelphia.org/calendar",
  },
  {
    org_id: "kadampa_philadelphia", org_name: "Kadampa Meditation Center Philadelphia",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 18, m: 30 }, duration_min: 120,
    address: "47-49 N 2nd St", city: "Philadelphia", state: "PA", neighborhood: "Old City",
    lat: 39.9504, lng: -75.1431, tradition: "tibetan", location_type: "in-person",
    notes: "General Program class. Guided meditation + Buddhist teachings. Drop-in welcome.",
    source_url: "https://www.meditationinphiladelphia.org", event_url: "https://www.meditationinphiladelphia.org/calendar",
  },
  {
    org_id: "kadampa_philadelphia", org_name: "Kadampa Meditation Center Philadelphia",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 120,
    address: "47-49 N 2nd St", city: "Philadelphia", state: "PA", neighborhood: "Old City",
    lat: 39.9504, lng: -75.1431, tradition: "tibetan", location_type: "in-person",
    notes: "General Program class. Guided meditation + Buddhist teachings. Drop-in welcome.",
    source_url: "https://www.meditationinphiladelphia.org", event_url: "https://www.meditationinphiladelphia.org/calendar",
  },
  {
    org_id: "kadampa_philadelphia", org_name: "Kadampa Meditation Center Philadelphia",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 30 }, duration_min: 90,
    address: "47-49 N 2nd St", city: "Philadelphia", state: "PA", neighborhood: "Old City",
    lat: 39.9504, lng: -75.1431, tradition: "tibetan", location_type: "in-person",
    notes: "General Program class. Guided meditation + Buddhist teachings. Drop-in welcome.",
    source_url: "https://www.meditationinphiladelphia.org", event_url: "https://www.meditationinphiladelphia.org/calendar",
  },

  // ── Zen Center of Philadelphia — 4904 Cedar Ave, West Philadelphia, PA 19143
  // Ordinary Mind Zen School (Charlotte Joko Beck lineage). No public iCal.
  // Google Calendar embedded via Simple Calendar WP plugin; calendar ID not extractable.
  // Schedule from zencenterphiladelphia.net: Sun 10am (hybrid), Wed 7pm (hybrid).
  {
    org_id: "zen_center_philadelphia", org_name: "Zen Center of Philadelphia",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "4904 Cedar Ave", city: "Philadelphia", state: "PA", neighborhood: "Cedar Park / West Philadelphia",
    lat: 39.9476, lng: -75.2277, tradition: "zen", location_type: "hybrid",
    notes: "Weekly zazen and dharma talk. Hybrid in-person + Zoom. Drop-in welcome; sliding scale/donation.",
    source_url: "https://www.zencenterphiladelphia.net", event_url: "https://www.zencenterphiladelphia.net/zcp-calendar/",
  },
  {
    org_id: "zen_center_philadelphia", org_name: "Zen Center of Philadelphia",
    title: "Wednesday Evening Sitting",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "4904 Cedar Ave", city: "Philadelphia", state: "PA", neighborhood: "Cedar Park / West Philadelphia",
    lat: 39.9476, lng: -75.2277, tradition: "zen", location_type: "hybrid",
    notes: "Weekly zazen. Hybrid in-person + Zoom. Drop-in welcome; donation-based.",
    source_url: "https://www.zencenterphiladelphia.net", event_url: "https://www.zencenterphiladelphia.net/zcp-calendar/",
  },

  // ── Chenrezig Tibetan Buddhist Center — 954 N Marshall St, Northern Liberties, PA 19123
  // Founded 1989 by Lama Losang Samten (Namgyal Monastery lineage). Non-sectarian Tibetan.
  // Wix site (tibetanbuddhist.org) — no iCal. Schedule from website.
  {
    org_id: "chenrezig_philadelphia", org_name: "Chenrezig Tibetan Buddhist Center",
    title: "Sunday Sangha",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "954 N Marshall St", city: "Philadelphia", state: "PA", neighborhood: "Northern Liberties / Callowhill",
    lat: 39.9633, lng: -75.1504, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly gathering: guided meditation, teachings, and community. Hybrid in-person + Zoom. Center opens 9am for self-guided practice. Drop-in welcome.",
    source_url: "https://www.tibetanbuddhist.org", event_url: "https://www.tibetanbuddhist.org/calendar",
  },
  {
    org_id: "chenrezig_philadelphia", org_name: "Chenrezig Tibetan Buddhist Center",
    title: "Thursday Green Tara Puja",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "954 N Marshall St", city: "Philadelphia", state: "PA", neighborhood: "Northern Liberties / Callowhill",
    lat: 39.9633, lng: -75.1504, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Tibetan Buddhist puja ceremony. In-person. Lama Losang Samten lineage. Drop-in welcome.",
    source_url: "https://www.tibetanbuddhist.org", event_url: "https://www.tibetanbuddhist.org/calendar",
  },

  // ── Chaiya Meditation Monastery — 7925 Virtue Ct, Las Vegas, NV 89113
  // Theravada (Burmese lineage). Daily public meditation, free, drop-in. Also on Zoom.
  // 4 daily sessions: 9am, 11am, 2pm, 5pm. Seeding 3 most accessible.
  {
    org_id: "chaiya_las_vegas", org_name: "Chaiya Meditation Monastery",
    title: "Morning Meditation",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    time: { h: 9, m: 0 }, duration_min: 60,
    address: "7925 Virtue Ct", city: "Las Vegas", state: "NV", neighborhood: "Enterprise / Southwest Las Vegas",
    lat: 36.0602, lng: -115.2246, tradition: "theravada", location_type: "in-person",
    notes: "Daily morning meditation. Free, drop-in. Also on Zoom (ID: 568 279 3041, passcode: Cmm45678).",
    source_url: "https://chaiyacmm.org", event_url: "https://chaiyacmm.org/events",
  },
  {
    org_id: "chaiya_las_vegas", org_name: "Chaiya Meditation Monastery",
    title: "Afternoon Meditation",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    time: { h: 14, m: 0 }, duration_min: 60,
    address: "7925 Virtue Ct", city: "Las Vegas", state: "NV", neighborhood: "Enterprise / Southwest Las Vegas",
    lat: 36.0602, lng: -115.2246, tradition: "theravada", location_type: "in-person",
    notes: "Daily afternoon meditation. Free, drop-in. Also on Zoom (ID: 568 279 3041, passcode: Cmm45678).",
    source_url: "https://chaiyacmm.org", event_url: "https://chaiyacmm.org/events",
  },
  {
    org_id: "chaiya_las_vegas", org_name: "Chaiya Meditation Monastery",
    title: "Evening Meditation",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    time: { h: 17, m: 0 }, duration_min: 75,
    address: "7925 Virtue Ct", city: "Las Vegas", state: "NV", neighborhood: "Enterprise / Southwest Las Vegas",
    lat: 36.0602, lng: -115.2246, tradition: "theravada", location_type: "in-person",
    notes: "Daily evening meditation. Free, drop-in. Also on Zoom (ID: 568 279 3041, passcode: Cmm45678).",
    source_url: "https://chaiyacmm.org", event_url: "https://chaiyacmm.org/events",
  },

  // ── Zen Center of Las Vegas — 7925 Virtue Ct, Las Vegas, NV 89113
  // Kwan Um School of Zen (Seung Sahn lineage). Teacher: Zen Master Ji Haeng.
  // Same campus as Chaiya Meditation Monastery.
  {
    org_id: "zen_center_las_vegas", org_name: "Zen Center of Las Vegas",
    title: "Sunday Zen Sitting",
    days: ["Sunday"], time: { h: 13, m: 0 }, duration_min: 90,
    address: "7925 Virtue Ct", city: "Las Vegas", state: "NV", neighborhood: "Enterprise / Southwest Las Vegas",
    lat: 36.0602, lng: -115.2246, tradition: "zen", location_type: "in-person",
    notes: "Weekly public Zen sitting. All levels welcome. Donation-based. Teacher: Zen Master Ji Haeng.",
    source_url: "https://zenlasvegas.com", event_url: "https://zenlasvegas.com/practice-schedule/",
  },
  {
    org_id: "zen_center_las_vegas", org_name: "Zen Center of Las Vegas",
    title: "Beginners Introduction to Zen",
    days: ["Sunday"], time: { h: 12, m: 0 }, duration_min: 60,
    week_of_month: 1,
    address: "7925 Virtue Ct", city: "Las Vegas", state: "NV", neighborhood: "Enterprise / Southwest Las Vegas",
    lat: 36.0602, lng: -115.2246, tradition: "zen", location_type: "in-person",
    notes: "First Sunday of each month. Free introduction to Zen practice. No experience needed.",
    source_url: "https://zenlasvegas.com", event_url: "https://zenlasvegas.com/practice-schedule/",
  },

  // ── Diamond Way Buddhist Center Las Vegas — 3743 N Rosecrest Circle, Las Vegas, NV 89121
  // Karma Kagyu Tibetan Buddhism (Lama Ole Nydahl). East Las Vegas.
  {
    org_id: "diamond_way_las_vegas", org_name: "Diamond Way Buddhist Center Las Vegas",
    title: "Evening Meditation",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3743 N Rosecrest Circle", city: "Las Vegas", state: "NV", neighborhood: "East Las Vegas",
    lat: 36.1448, lng: -115.0803, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Karma Kagyu meditation. Drop-in welcome. No experience needed. First Tuesday: Open House + Buddhism intro.",
    source_url: "https://diamondway.org/lasvegas/", event_url: "https://diamondway.org/lasvegas/",
  },

  // ── Nevada Buddhist Temple — 2040 Abels Lane, North Las Vegas, NV 89115
  // Sri Lankan Theravada. Resident monk: Bhante Deepananda. Free, all welcome.
  {
    org_id: "nevada_buddhist_temple", org_name: "Nevada Buddhist Temple",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "2040 Abels Lane", city: "North Las Vegas", state: "NV", neighborhood: "North Las Vegas",
    lat: 36.2103, lng: -115.1214, tradition: "theravada", location_type: "in-person",
    notes: "Weekly in-person meditation with Bhante Deepananda. Free, open to all.",
    source_url: "https://www.nevadabuddhisttemple.org", event_url: "https://www.nevadabuddhisttemple.org",
  },
  {
    org_id: "nevada_buddhist_temple", org_name: "Nevada Buddhist Temple",
    title: "Online Evening Meditation & Chanting",
    days: ["Monday","Tuesday","Thursday","Saturday","Sunday"],
    time: { h: 19, m: 30 }, duration_min: 60,
    address: "2040 Abels Lane", city: "North Las Vegas", state: "NV", neighborhood: "North Las Vegas",
    lat: 36.2103, lng: -115.1214, tradition: "theravada", location_type: "online",
    notes: "Daily online meditation and chanting via Zoom (except Wednesday and Friday). Free, open to all.",
    source_url: "https://www.nevadabuddhisttemple.org", event_url: "https://www.nevadabuddhisttemple.org",
  },

  // ── Nashville, TN — Phase 3 (heartbeat 27)

  // ── One Dharma Nashville — 530 26th Ave N, Nashville, TN 37209
  // Insight Meditation / Vipassana. Teacher: Lisa Ernst. Germantown/Midtown.
  {
    org_id: "one_dharma_nashville", org_name: "One Dharma Nashville",
    title: "Monday Evening Meditation",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "530 26th Ave N", city: "Nashville", state: "TN", neighborhood: "Germantown / Midtown",
    lat: 36.1650, lng: -86.8149, tradition: "theravada", location_type: "hybrid",
    notes: "Guided meditation, dharma talk, discussion. In-person + Zoom. All levels welcome. Suggested donation $10-$15.",
    source_url: "https://onedharmanashville.com", event_url: "https://onedharmanashville.com/events/",
  },

  // ── Wild Heart Meditation Center — 3123 Gallatin Pike, Nashville, TN 37216
  // Secular / multi-tradition. East Nashville, co-located with Nashville Zen Center.
  // Dharma Punx / Against the Stream lineage. Drop-in, by donation.
  {
    org_id: "wild_heart_meditation", org_name: "Wild Heart Meditation Center",
    title: "Wednesday Dharma & Discussion",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3123 Gallatin Pike", city: "Nashville", state: "TN", neighborhood: "East Nashville",
    lat: 36.2038, lng: -86.7178, tradition: "theravada", location_type: "in-person",
    notes: "Dharma talk and group discussion following meditation. Drop-in, by donation.",
    source_url: "https://www.wildheartmeditationcenter.org", event_url: "https://www.wildheartmeditationcenter.org/weeklyprogramming",
  },
  {
    org_id: "wild_heart_meditation", org_name: "Wild Heart Meditation Center",
    title: "Friday Dharma & Discussion",
    days: ["Friday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3123 Gallatin Pike", city: "Nashville", state: "TN", neighborhood: "East Nashville",
    lat: 36.2038, lng: -86.7178, tradition: "theravada", location_type: "in-person",
    notes: "Dharma talk and group discussion following meditation. Drop-in, by donation.",
    source_url: "https://www.wildheartmeditationcenter.org", event_url: "https://www.wildheartmeditationcenter.org/weeklyprogramming",
  },
  {
    org_id: "wild_heart_meditation", org_name: "Wild Heart Meditation Center",
    title: "Sunday Dharma & Discussion",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 90,
    address: "3123 Gallatin Pike", city: "Nashville", state: "TN", neighborhood: "East Nashville",
    lat: 36.2038, lng: -86.7178, tradition: "theravada", location_type: "in-person",
    notes: "Morning dharma talk and discussion. Rotating format by Sunday of month. Drop-in, by donation.",
    source_url: "https://www.wildheartmeditationcenter.org", event_url: "https://www.wildheartmeditationcenter.org/weeklyprogramming",
  },

  // ── Nashville Zen Center — 3123 Gallatin Pike, Nashville, TN 37216
  // Soto Zen (Silent Thunder Order, lineage of Zengaku Soyu Matsuoka).
  // Co-located with Wild Heart Meditation Center.
  {
    org_id: "nashville_zen_center", org_name: "Nashville Zen Center",
    title: "Tuesday Evening Zazen",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "3123 Gallatin Pike", city: "Nashville", state: "TN", neighborhood: "East Nashville",
    lat: 36.2038, lng: -86.7178, tradition: "zen", location_type: "in-person",
    notes: "Zazen + instruction. Newcomers arrive at 6:30pm for orientation. Open to all.",
    source_url: "https://nashvillezencenter.org", event_url: "https://nashvillezencenter.org",
  },
  {
    org_id: "nashville_zen_center", org_name: "Nashville Zen Center",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 7, m: 0 }, duration_min: 60,
    address: "3123 Gallatin Pike", city: "Nashville", state: "TN", neighborhood: "East Nashville",
    lat: 36.2038, lng: -86.7178, tradition: "zen", location_type: "in-person",
    notes: "Early morning zazen. Open to all, drop-in welcome.",
    source_url: "https://nashvillezencenter.org", event_url: "https://nashvillezencenter.org",
  },

  // ── Padmasambhava Buddhist Center of Tennessee — 419 East Iris Drive, Nashville, TN 37204
  // Tibetan (Nyingma/Dzogchen). PBC network, founded 1990. 12South neighborhood.
  {
    org_id: "pbc_tennessee", org_name: "Padmasambhava Buddhist Center of Tennessee",
    title: "Sunday Calm Abiding Meditation",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 90,
    address: "419 East Iris Drive", city: "Nashville", state: "TN", neighborhood: "12South / Waverly-Belmont",
    lat: 36.1388, lng: -86.7903, tradition: "tibetan", location_type: "in-person",
    notes: "Shamatha / calm abiding meditation open to all. No Buddhist background required. Free.",
    source_url: "https://www.pbc-tn.org", event_url: "https://www.pbc-tn.org/schedule-1",
  },

  // ── Detroit / SE Michigan ────────────────────────────────────────────────

  // ── Detroit Zen Center — 3030 Casmere St, Hamtramck, MI 48212
  // Korean Zen (Chogye Order / Sudeok-sa lineage). Founded 1990 by Abbot Hwalson Sunim.
  {
    org_id: "detroit_zen_center", org_name: "Detroit Zen Center",
    title: "Sunday Zen Workshop",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "3030 Casmere St", city: "Hamtramck", state: "MI", neighborhood: "Hamtramck (Detroit metro)",
    lat: 42.3936, lng: -83.0566, tradition: "zen", location_type: "in-person",
    notes: "Guided meditation, dharma talk, and tea. Drop-in welcome, all levels. By donation. First Sunday is Beginners Workshop & Brunch (9am–12pm).",
    source_url: "https://www.detroitzencenter.org", event_url: "https://www.detroitzencenter.org/events-registration",
  },

  // ── Still Point Zen Buddhist Temple — 4345 Trumbull Ave, Detroit, MI 48208
  // Korean Zen (Samu Sunim lineage). Founded by P'arang Geri Larkin; teacher Koho Vince Anila.
  {
    org_id: "still_point_zen_detroit", org_name: "Still Point Zen Buddhist Temple",
    title: "Sunday Service",
    days: ["Sunday"], time: { h: 8, m: 30 }, duration_min: 180,
    address: "4345 Trumbull Ave", city: "Detroit", state: "MI", neighborhood: "Corktown / Woodbridge",
    lat: 42.3527, lng: -83.0731, tradition: "zen", location_type: "in-person",
    notes: "Zazen, chanting, and dharma talk. In-person and livestreamed. Free, open to all.",
    source_url: "https://www.stillpointzenbuddhisttemple.org", event_url: "https://www.stillpointzenbuddhisttemple.org",
  },
  {
    org_id: "still_point_zen_detroit", org_name: "Still Point Zen Buddhist Temple",
    title: "Saturday Service",
    days: ["Saturday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "4345 Trumbull Ave", city: "Detroit", state: "MI", neighborhood: "Corktown / Woodbridge",
    lat: 42.3527, lng: -83.0731, tradition: "zen", location_type: "in-person",
    notes: "Weekly Saturday service. In-person with livestream. Free, open to all.",
    source_url: "https://www.stillpointzenbuddhisttemple.org", event_url: "https://www.stillpointzenbuddhisttemple.org",
  },

  // ── Field Temple — 5333 Elmwood Ave, Detroit, MI 48211
  // Zen (Korean tradition). Outdoor garden sittings.
  {
    org_id: "field_temple_detroit", org_name: "Field Temple",
    title: "Sunday Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "5333 Elmwood Ave", city: "Detroit", state: "MI", neighborhood: "Poletown East",
    lat: 42.3699, lng: -83.0431, tradition: "zen", location_type: "in-person",
    notes: "Two 20-min zazen periods, three-refuges chanting, dharma talk, and tea. Held in the garden or under trees. Free.",
    source_url: "https://fieldtemple.org", event_url: "https://fieldtemple.org",
  },

  // ── Dharma Gate Zen Center — 360 East Maple Suite K, Troy, MI 48083
  // Soto Zen. Troy is a Detroit northern suburb.
  {
    org_id: "dharma_gate_zen_troy", org_name: "Dharma Gate Zen Center",
    title: "Sunday Service",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "360 East Maple Suite K", city: "Troy", state: "MI", neighborhood: "Troy (Detroit suburb)",
    lat: 42.5798, lng: -83.1446, tradition: "zen", location_type: "in-person",
    notes: "20-minute zazen and dharma talk. Beginners welcome; visitor guide available on website. Free.",
    source_url: "https://dharmagatezen.org", event_url: "https://dharmagatezen.org/calendar/",
  },

  // ── Baltimore, MD ────────────────────────────────────────────────────────

  // ── Baltimore Shambhala Centre — 33 W 33rd St (YMCA), Baltimore, MD 21218
  // Shambhala / Tibetan. Biweekly in-person + Zoom. Shambhala iCal server down.
  {
    org_id: "baltimore_shambhala", org_name: "Baltimore Shambhala Centre",
    title: "Meditation@33rd",
    days: ["Saturday"], week_of_month: 2,
    time: { h: 9, m: 0 }, duration_min: 60,
    address: "33 W 33rd St", city: "Baltimore", state: "MD", neighborhood: "Charles Village (33rd Street YMCA)",
    lat: 39.3277, lng: -76.6093, tradition: "tibetan", location_type: "hybrid",
    notes: "In-person and Zoom. Open to all levels, no experience needed. Free. 2nd Saturday of the month.",
    source_url: "https://baltimore.shambhala.org", event_url: "https://baltimore.shambhala.org/ongoing-offerings/",
  },
  {
    org_id: "baltimore_shambhala", org_name: "Baltimore Shambhala Centre",
    title: "Meditation@33rd",
    days: ["Saturday"], week_of_month: 4,
    time: { h: 9, m: 0 }, duration_min: 60,
    address: "33 W 33rd St", city: "Baltimore", state: "MD", neighborhood: "Charles Village (33rd Street YMCA)",
    lat: 39.3277, lng: -76.6093, tradition: "tibetan", location_type: "hybrid",
    notes: "In-person and Zoom. Open to all levels, no experience needed. Free. 4th Saturday of the month.",
    source_url: "https://baltimore.shambhala.org", event_url: "https://baltimore.shambhala.org/ongoing-offerings/",
  },

  // ── KMC Maryland — 901 Dartmouth Road, Baltimore, MD 21212 (Roland Park)
  // New Kadampa Tradition (Tibetan/Gelug). Squarespace site, no iCal.
  {
    org_id: "kmc_maryland", org_name: "Kadampa Meditation Center Maryland",
    title: "Meditations for Modern Life",
    days: ["Wednesday"], time: { h: 11, m: 0 }, duration_min: 60,
    address: "901 Dartmouth Road", city: "Baltimore", state: "MD", neighborhood: "Roland Park",
    lat: 39.3562, lng: -76.6383, tradition: "tibetan", location_type: "in-person",
    notes: "Drop-in class: guided meditation with Buddhist teaching. No experience needed. First class free, $12 thereafter.",
    source_url: "https://www.meditationmd.org", event_url: "https://www.meditationmd.org/events-calendar",
  },
  {
    org_id: "kmc_maryland", org_name: "Kadampa Meditation Center Maryland",
    title: "Meditations for World Peace",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "901 Dartmouth Road", city: "Baltimore", state: "MD", neighborhood: "Roland Park",
    lat: 39.3562, lng: -76.6383, tradition: "tibetan", location_type: "in-person",
    notes: "Evening guided meditation class focused on developing peace of mind and compassion. First class free, $12 thereafter.",
    source_url: "https://www.meditationmd.org", event_url: "https://www.meditationmd.org/events-calendar",
  },
  {
    org_id: "kmc_maryland", org_name: "Kadampa Meditation Center Maryland",
    title: "Meditations for Modern Life",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 75,
    address: "901 Dartmouth Road", city: "Baltimore", state: "MD", neighborhood: "Roland Park",
    lat: 39.3562, lng: -76.6383, tradition: "tibetan", location_type: "in-person",
    notes: "Drop-in class: guided meditation with Buddhist teaching. No experience needed. First class free, $12 thereafter.",
    source_url: "https://www.meditationmd.org", event_url: "https://www.meditationmd.org/events-calendar",
  },
  {
    org_id: "kmc_maryland", org_name: "Kadampa Meditation Center Maryland",
    title: "Meditations for Modern Life",
    days: ["Sunday"], time: { h: 10, m: 30 }, duration_min: 75,
    address: "901 Dartmouth Road", city: "Baltimore", state: "MD", neighborhood: "Roland Park",
    lat: 39.3562, lng: -76.6383, tradition: "tibetan", location_type: "in-person",
    notes: "Drop-in class: guided meditation with Buddhist teaching. No experience needed. First class free, $12 thereafter.",
    source_url: "https://www.meditationmd.org", event_url: "https://www.meditationmd.org/events-calendar",
  },

  // ── KMC Maryland Canton — 1025 S Potomac St, Baltimore, MD 21224
  {
    org_id: "kmc_maryland_canton", org_name: "Kadampa Meditation Center Maryland — Canton",
    title: "Meditations for Modern Life",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "1025 S Potomac St", city: "Baltimore", state: "MD", neighborhood: "Canton",
    lat: 39.2848, lng: -76.5758, tradition: "tibetan", location_type: "in-person",
    notes: "Drop-in meditation class at the Canton branch (Church on the Square). No experience needed. First class free, $12 thereafter.",
    source_url: "https://www.meditationmd.org", event_url: "https://www.meditationmd.org/events-calendar",
  },

  // ── Baltimore Dharma Group — 3107 N Charles St (Homewood Friends Meeting), Baltimore MD 21218
  // Lay Soto Zen, shikantaza style. Wix site, no iCal.
  {
    org_id: "baltimore_dharma_group", org_name: "Baltimore Dharma Group",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 8, m: 0 }, duration_min: 90,
    address: "3107 N Charles St", city: "Baltimore", state: "MD", neighborhood: "Guilford / Charles Village (Homewood Friends Meeting)",
    lat: 39.3262, lng: -76.6202, tradition: "zen", location_type: "in-person",
    notes: "Two 30-minute zazen periods with kinhin (walking meditation). Arrive by 7:55am. All levels welcome; free.",
    source_url: "https://www.baltimoredharmagroup.org", event_url: "https://www.baltimoredharmagroup.org/schedule",
  },
  {
    org_id: "baltimore_dharma_group", org_name: "Baltimore Dharma Group",
    title: "Thursday Evening Zazen",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3107 N Charles St", city: "Baltimore", state: "MD", neighborhood: "Guilford / Charles Village (Homewood Friends Meeting)",
    lat: 39.3262, lng: -76.6202, tradition: "zen", location_type: "in-person",
    notes: "Alternates between open zazen (two 30-min periods + kinhin) and dharma class (30-min sit + dharma discussion). All levels welcome; free.",
    source_url: "https://www.baltimoredharmagroup.org", event_url: "https://www.baltimoredharmagroup.org/schedule",
  },

  // ── Sacramento, CA ────────────────────────────────────────────────────────

  // ── Sacramento Insight Meditation (SIM) — 3111 Wissemann Dr, Sacramento CA 95826
  // Theravada/Vipassana. iCal blocked by Incapsula; seeded as recurring.
  {
    org_id: "sacramento_insight_meditation", org_name: "Sacramento Insight Meditation",
    title: "Meditation and Dharma Talk",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "3111 Wissemann Drive", city: "Sacramento", state: "CA", neighborhood: "South Sacramento (Sacramento Dharma Center)",
    lat: 38.5516, lng: -121.3810, tradition: "theravada", location_type: "hybrid",
    notes: "Weekly Thursday evening sit: guided meditation, dharma talk, and discussion. Drop-in, all levels welcome. Dana-based.",
    source_url: "https://sactoinsight.org", event_url: "https://sactoinsight.org/activities/practice-opportunities/sitting-groups/",
  },
  {
    org_id: "sacramento_insight_meditation", org_name: "Sacramento Insight Meditation",
    title: "Dharma Recovery Sangha",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "3111 Wissemann Drive", city: "Sacramento", state: "CA", neighborhood: "South Sacramento (Sacramento Dharma Center)",
    lat: 38.5516, lng: -121.3810, tradition: "theravada", location_type: "in-person",
    identity_focus: "recovery",
    notes: "Meditation and community for people seeking recovery from addiction. Open to all. In-person only. Dana-based.",
    source_url: "https://sactoinsight.org", event_url: "https://sactoinsight.org/activities/practice-opportunities/sitting-groups/",
  },

  // ── Pittsburgh, PA ────────────────────────────────────────────────────────

  // ── Stillpoint Zen — 137 41st St, Lawrenceville, Pittsburgh, PA 15201
  // Lay Zen community. WordPress site, no iCal. Drop-in, free.
  {
    org_id: "stillpoint_zen_pittsburgh", org_name: "Stillpoint — A Pittsburgh Zen Community",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 70,
    address: "137 41st St", city: "Pittsburgh", state: "PA", neighborhood: "Lawrenceville",
    lat: 40.4646, lng: -79.9644, tradition: "zen", location_type: "in-person",
    notes: "Drop-in zazen. Newcomers welcome; private intro to zazen available on request. No experience needed. Free, donation welcome.",
    source_url: "https://www.stillpointzen.org", event_url: "https://www.stillpointzen.org",
  },
  {
    org_id: "stillpoint_zen_pittsburgh", org_name: "Stillpoint — A Pittsburgh Zen Community",
    title: "Wednesday Evening Zazen",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "137 41st St", city: "Pittsburgh", state: "PA", neighborhood: "Lawrenceville",
    lat: 40.4646, lng: -79.9644, tradition: "zen", location_type: "in-person",
    notes: "Drop-in zazen. Newcomers welcome; private intro to zazen available on request. No experience needed. Free, donation welcome.",
    source_url: "https://www.stillpointzen.org", event_url: "https://www.stillpointzen.org",
  },

  // ── Pittsburgh Buddhist Center — 58 QSI Lane, Allison Park, PA 15101
  // Theravada; resident Burmese monks. No iCal. Free.
  {
    org_id: "pittsburgh_buddhist_center", org_name: "Pittsburgh Buddhist Center",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 150,
    address: "58 QSI Lane", city: "Allison Park", state: "PA", neighborhood: "Allison Park (Hampton Township)",
    lat: 40.5760, lng: -79.9576, tradition: "theravada", location_type: "in-person",
    notes: "Led by resident Burmese monks. Beginners arrive 6:30pm for private instruction. Monks available for dharma conversation after sit. Free.",
    source_url: "https://www.pittsburghbuddhistcenter.org", event_url: "https://www.pittsburghbuddhistcenter.org/weekly-meditation-programs/",
  },

  // ── Pittsburgh Buddhist Center Oakmont — 700 Allegheny River Blvd, Oakmont, PA 15139
  {
    org_id: "pittsburgh_buddhist_center_oakmont", org_name: "Pittsburgh Buddhist Center — Oakmont",
    title: "Tuesday Evening Meditation",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "700 Allegheny River Blvd", city: "Oakmont", state: "PA", neighborhood: "Oakmont Carnegie Library",
    lat: 40.5209, lng: -79.8362, tradition: "theravada", location_type: "in-person",
    notes: "Outreach sit at Oakmont Carnegie Library. Led by resident monks from Pittsburgh Buddhist Center. Free and open to all.",
    source_url: "https://www.pittsburghbuddhistcenter.org", event_url: "https://www.pittsburghbuddhistcenter.org/weekly-meditation-programs/",
  },

  // ── Olmo Ling Bon Center — 1101 Greenfield Ave, Pittsburgh, PA 15217
  // Tibetan Bon (pre-Buddhist). Dzogchen Practice Group: 1st & 3rd Sundays, in-person + Zoom.
  {
    org_id: "olmo_ling_pittsburgh", org_name: "Olmo Ling Bon Center and Institute",
    title: "Dzogchen Practice Group",
    days: ["Sunday"], week_of_month: 1,
    time: { h: 16, m: 0 }, duration_min: 120,
    address: "1101 Greenfield Ave", city: "Pittsburgh", state: "PA", neighborhood: "Greenfield",
    lat: 40.4180, lng: -79.9449, tradition: "tibetan", location_type: "hybrid",
    notes: "Guided Dzogchen meditation practice. In-person + Zoom. Free and open to all. 1st Sunday of the month. Tibetan Bon tradition.",
    source_url: "https://www.olmoling.org", event_url: "https://www.olmoling.org/events/",
  },
  {
    org_id: "olmo_ling_pittsburgh", org_name: "Olmo Ling Bon Center and Institute",
    title: "Dzogchen Practice Group",
    days: ["Sunday"], week_of_month: 3,
    time: { h: 16, m: 0 }, duration_min: 120,
    address: "1101 Greenfield Ave", city: "Pittsburgh", state: "PA", neighborhood: "Greenfield",
    lat: 40.4180, lng: -79.9449, tradition: "tibetan", location_type: "hybrid",
    notes: "Guided Dzogchen meditation practice. In-person + Zoom. Free and open to all. 3rd Sunday of the month. Tibetan Bon tradition.",
    source_url: "https://www.olmoling.org", event_url: "https://www.olmoling.org/events/",
  },

  // ── Three Rivers Tibetan Cultural Center — 1660 Lincoln Way, White Oak, PA 15131
  // Drikung Kagyu. Resident teachers. ~12 miles SE of Pittsburgh. Hybrid in-person + Zoom.
  {
    org_id: "three_rivers_tibetan_pittsburgh", org_name: "Three Rivers Tibetan Cultural Center",
    title: "Wednesday Evening Practice",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "1660 Lincoln Way", city: "White Oak", state: "PA", neighborhood: "White Oak (SE Pittsburgh metro)",
    lat: 40.3407, lng: -79.8289, tradition: "tibetan", location_type: "hybrid",
    notes: "Rotating practices: Chenrezig, Manjushri, Medicine Buddha, and Green Tara (schedule distributed via email). Hybrid in-person + Zoom. All levels welcome; free.",
    source_url: "https://www.threeriverstibetancc.org", event_url: "https://www.threeriverstibetancc.org/schedule/",
  },
  {
    org_id: "three_rivers_tibetan_pittsburgh", org_name: "Three Rivers Tibetan Cultural Center",
    title: "Sunday Vajrasattva Practice",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "1660 Lincoln Way", city: "White Oak", state: "PA", neighborhood: "White Oak (SE Pittsburgh metro)",
    lat: 40.3407, lng: -79.8289, tradition: "tibetan", location_type: "hybrid",
    notes: "Vajrasattva purification practice. Hybrid in-person + Zoom. All levels welcome; free. Drikung Kagyu lineage.",
    source_url: "https://www.threeriverstibetancc.org", event_url: "https://www.threeriverstibetancc.org/schedule/",
  },

  // ── Ann Arbor, MI ───────────────────────────────────────────────────────

  // ── Insight Meditation Ann Arbor — 180 Little Lake Dr #1, Ann Arbor, MI 48103
  // Theravada/Insight. No iCal. Sun in-person + Sat/weekday Zoom sits.
  {
    org_id: "insight_meditation_ann_arbor", org_name: "Insight Meditation Ann Arbor",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 75,
    address: "180 Little Lake Drive, Suite 1", city: "Ann Arbor", state: "MI", neighborhood: "West Ann Arbor (near Westgate)",
    lat: 42.2810, lng: -83.7912, tradition: "theravada", location_type: "in-person",
    notes: "45-minute sit followed by dharma talk. Drop-in welcome; no experience required. Free and donation-based.",
    source_url: "https://insightmeditationannarbor.org", event_url: "https://insightmeditationannarbor.org/regular-sittings/",
  },
  {
    org_id: "insight_meditation_ann_arbor", org_name: "Insight Meditation Ann Arbor",
    title: "Saturday Morning Meditation (Online)",
    days: ["Saturday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "", city: "Ann Arbor", state: "MI", neighborhood: "Online (Zoom)",
    lat: 42.2810, lng: -83.7912, tradition: "theravada", location_type: "online",
    notes: "Weekly online sit via Zoom. No experience required. Free.",
    source_url: "https://insightmeditationannarbor.org", event_url: "https://insightmeditationannarbor.org/regular-sittings/",
  },

  // ── Zen Buddhist Temple Ann Arbor — 1214 Packard St, Ann Arbor, MI 48104
  // Korean Zen (Son Buddhism). Sunday service in-person + livestreamed.
  {
    org_id: "zen_buddhist_temple_ann_arbor", org_name: "Zen Buddhist Temple — Ann Arbor",
    title: "Sunday Public Service",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "1214 Packard Street", city: "Ann Arbor", state: "MI", neighborhood: "Burns Park (near UMich campus)",
    lat: 42.2631, lng: -83.7423, tradition: "zen", location_type: "in-person",
    notes: "Korean Zen (Son Buddhism) Sunday service: meditation, dharma talk, ceremonies. In-person + livestreamed. Drop-in welcome. Free.",
    source_url: "https://www.zenbuddhisttemple.org/annarbor", event_url: "https://www.zenbuddhisttemple.org/annarbor",
  },

  // ── Jewel Heart — 1129 Oak Valley Drive, Ann Arbor, MI 48108
  // Tibetan Buddhist (Gelugpa). Free weekly community meditation Tuesdays.
  // Special events via Google Calendar iCal (wired into coordinator + abraxis).
  {
    org_id: "jewel_heart_ann_arbor", org_name: "Jewel Heart",
    title: "Community Meditation",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 45,
    address: "1129 Oak Valley Drive", city: "Ann Arbor", state: "MI", neighborhood: "Southeast Ann Arbor",
    lat: 42.2209, lng: -83.6972, tradition: "tibetan", location_type: "in-person",
    notes: "Free weekly community meditation open to all. Tibetan Buddhist (Gelugpa/Mahayana). No experience required.",
    source_url: "https://www.jewelheart.org", event_url: "https://www.jewelheart.org/jewel-heart-calendar/",
  },

  // ── St. Louis, MO ───────────────────────────────────────────────────────

  // ── Sunday Sangha St. Louis — Brentwood, MO
  // Theravada/Insight. No iCal. Sunday hybrid sit.
  // Confluence Zen Center zazen sits come from iCal feed (coordinator + abraxis).
  {
    org_id: "sunday_sangha_stl", org_name: "Sunday Sangha St. Louis",
    title: "Sunday Meditation",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 90,
    address: "", city: "Brentwood", state: "MO", neighborhood: "Brentwood (St. Louis suburb)",
    lat: 38.6107, lng: -90.3494, tradition: "theravada", location_type: "hybrid",
    notes: "Insight Meditation community. ~40 min silent sit, brief instruction, dharma sharing, open discussion. All backgrounds welcome. Free (cash donations for space rental). Location + Zoom link provided via email list at sundaysangha-stl.org.",
    source_url: "https://sundaysangha-stl.org", event_url: "https://sundaysangha-stl.org",
  },

  // ── Center for Pragmatic Buddhism STL — 5007 Waterman Blvd, St. Louis, MO 63108
  // Chan/Zen/Pragmatist. Weekly Thursday sit at First Unitarian Church.
  {
    org_id: "center_pragmatic_buddhism_stl", org_name: "Center for Pragmatic Buddhism — St. Louis",
    title: "Weekly Practice",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "5007 Waterman Boulevard", city: "St. Louis", state: "MO", neighborhood: "Central West End (at First Unitarian Church)",
    lat: 38.6428, lng: -90.2724, tradition: "zen", location_type: "in-person",
    notes: "Zazen, dharma talk, and group discussion. Enter through north/back garden walkway. Free, open to all.",
    source_url: "https://www.pragmaticbuddhism.org/stlouis", event_url: "https://www.pragmaticbuddhism.org/stlouis",
  },

  // ── Cincinnati, OH ───────────────────────────────────────────────────────

  // ── Cincinnati Zen Center — 6015 Vine St, Cincinnati, OH 45216
  // Korean/Soto Zen. 4 in-person days + Saturday Zoom. Furnace Mountain Sangha lineage.
  {
    org_id: "cincinnati_zen_center", org_name: "Cincinnati Zen Center",
    title: "Sunday Morning Zen",
    days: ["Sunday"], time: { h: 8, m: 0 }, duration_min: 60,
    address: "6015 Vine Street", city: "Cincinnati", state: "OH", neighborhood: "Hartwell (North Cincinnati)",
    lat: 39.1851, lng: -84.5036, tradition: "zen", location_type: "in-person",
    notes: "In-person drop-in zazen. Arrive 10–15 min early for first visit. Doors lock at sit time. Free.",
    source_url: "https://www.cincinnatizencenter.org", event_url: "https://www.cincinnatizencenter.org",
  },
  {
    org_id: "cincinnati_zen_center", org_name: "Cincinnati Zen Center",
    title: "Monday Evening Zen",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "6015 Vine Street", city: "Cincinnati", state: "OH", neighborhood: "Hartwell (North Cincinnati)",
    lat: 39.1851, lng: -84.5036, tradition: "zen", location_type: "in-person",
    notes: "In-person drop-in zazen. Beginner-friendly; orientation offered. Arrive early for first visit. Free.",
    source_url: "https://www.cincinnatizencenter.org", event_url: "https://www.cincinnatizencenter.org",
  },
  {
    org_id: "cincinnati_zen_center", org_name: "Cincinnati Zen Center",
    title: "Wednesday Evening Zen",
    days: ["Wednesday"], time: { h: 17, m: 30 }, duration_min: 60,
    address: "6015 Vine Street", city: "Cincinnati", state: "OH", neighborhood: "Hartwell (North Cincinnati)",
    lat: 39.1851, lng: -84.5036, tradition: "zen", location_type: "in-person",
    notes: "In-person drop-in zazen. Arrive 10–15 min early for first visit. Free.",
    source_url: "https://www.cincinnatizencenter.org", event_url: "https://www.cincinnatizencenter.org",
  },
  {
    org_id: "cincinnati_zen_center", org_name: "Cincinnati Zen Center",
    title: "Thursday Evening Zen",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "6015 Vine Street", city: "Cincinnati", state: "OH", neighborhood: "Hartwell (North Cincinnati)",
    lat: 39.1851, lng: -84.5036, tradition: "zen", location_type: "in-person",
    notes: "In-person drop-in zazen. Arrive 10–15 min early for first visit. Free.",
    source_url: "https://www.cincinnatizencenter.org", event_url: "https://www.cincinnatizencenter.org",
  },
  {
    org_id: "cincinnati_zen_center", org_name: "Cincinnati Zen Center",
    title: "Saturday Morning Zen (Online)",
    days: ["Saturday"], time: { h: 8, m: 30 }, duration_min: 60,
    address: "6015 Vine Street", city: "Cincinnati", state: "OH", neighborhood: "Hartwell (North Cincinnati)",
    lat: 39.1851, lng: -84.5036, tradition: "zen", location_type: "online",
    notes: "Virtual Zoom sit — Saturday morning only (not in-person). Link via website. Free.",
    source_url: "https://www.cincinnatizencenter.org", event_url: "https://www.cincinnatizencenter.org",
  },

  // ── Buddhist Dharma Center of Cincinnati — 15 Moline Court, Northside, Cincinnati OH 45223
  // Ecumenical/pluralist Theravada-leaning. Daily Zoom + weekly in-person and hybrid sits.
  {
    org_id: "buddhist_dharma_center_cincinnati", org_name: "Buddhist Dharma Center of Cincinnati",
    title: "Daily Morning Meditation (Online)",
    days: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    time: { h: 7, m: 0 }, duration_min: 60,
    address: "15 Moline Court", city: "Cincinnati", state: "OH", neighborhood: "Northside",
    lat: 39.1716, lng: -84.5222, tradition: "pluralist", location_type: "online",
    notes: "Daily Zoom silent meditation, 7 days a week. Drop-in; no registration required. Free.",
    source_url: "https://www.cincinnatidharma.org", event_url: "https://www.cincinnatidharma.org",
  },
  {
    org_id: "buddhist_dharma_center_cincinnati", org_name: "Buddhist Dharma Center of Cincinnati",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "15 Moline Court", city: "Cincinnati", state: "OH", neighborhood: "Northside",
    lat: 39.1716, lng: -84.5222, tradition: "pluralist", location_type: "hybrid",
    notes: "In-person + Zoom hybrid. Ritual opening, two sitting periods with walking meditation. All traditions welcome. Free.",
    source_url: "https://www.cincinnatidharma.org", event_url: "https://www.cincinnatidharma.org",
  },
  {
    org_id: "buddhist_dharma_center_cincinnati", org_name: "Buddhist Dharma Center of Cincinnati",
    title: "Tuesday Evening Sitting",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 45,
    address: "15 Moline Court", city: "Cincinnati", state: "OH", neighborhood: "Northside",
    lat: 39.1716, lng: -84.5222, tradition: "pluralist", location_type: "in-person",
    notes: "In-person only silent sitting. Drop-in. Free.",
    source_url: "https://www.cincinnatidharma.org", event_url: "https://www.cincinnatidharma.org",
  },
  {
    org_id: "buddhist_dharma_center_cincinnati", org_name: "Buddhist Dharma Center of Cincinnati",
    title: "Wednesday Evening Practice",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "15 Moline Court", city: "Cincinnati", state: "OH", neighborhood: "Northside",
    lat: 39.1716, lng: -84.5222, tradition: "pluralist", location_type: "hybrid",
    notes: "In-person + Zoom hybrid. Meditation instruction and dharma discussion. Free.",
    source_url: "https://www.cincinnatidharma.org", event_url: "https://www.cincinnatidharma.org",
  },

  // ── Gaden Samdrupling Buddhist Monastery — 3046 Pavlova Dr, Colerain Township, OH 45251
  // Gelugpa Tibetan. Wednesday Open Meditation is specifically public drop-in.
  {
    org_id: "gaden_samdrupling_monastery", org_name: "Gaden Samdrupling Buddhist Monastery",
    title: "Open Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "3046 Pavlova Drive", city: "Cincinnati", state: "OH", neighborhood: "Colerain Township (West Side)",
    lat: 39.2147, lng: -84.6198, tradition: "tibetan", location_type: "in-person",
    notes: "Public drop-in silent meditation. Prayer books provided. Gelugpa Tibetan monastery. Free.",
    source_url: "https://www.gslmonastery.org", event_url: "https://www.gslmonastery.org",
  },

  // ── Rime Buddhist Center — 2939 Wayne Ave, Kansas City MO 64109
  // Non-sectarian Rimé pluralist. 30+ year old center; Mon-Fri noon sits + evening sits + Sunday.
  {
    org_id: "rime_buddhist_center", org_name: "Rime Buddhist Center",
    title: "Daily Lunchtime Meditation",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    time: { h: 12, m: 0 }, duration_min: 30,
    address: "2939 Wayne Avenue", city: "Kansas City", state: "MO", neighborhood: "Waldo/Brookside",
    lat: 39.0278, lng: -94.5594, tradition: "pluralist", location_type: "in-person",
    notes: "Daily 12–12:30pm group meditation, Mon–Fri. Drop-in; all traditions welcome. Free.",
    source_url: "https://www.rimecenter.org", event_url: "https://www.rimecenter.org",
  },
  {
    org_id: "rime_buddhist_center", org_name: "Rime Buddhist Center",
    title: "Monday Evening Zen Meditation",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "2939 Wayne Avenue", city: "Kansas City", state: "MO", neighborhood: "Waldo/Brookside",
    lat: 39.0278, lng: -94.5594, tradition: "zen", location_type: "in-person",
    notes: "Weekly Monday evening Zen meditation, 7–8pm. Drop-in. Free.",
    source_url: "https://www.rimecenter.org", event_url: "https://www.rimecenter.org",
  },
  {
    org_id: "rime_buddhist_center", org_name: "Rime Buddhist Center",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 30,
    address: "2939 Wayne Avenue", city: "Kansas City", state: "MO", neighborhood: "Waldo/Brookside",
    lat: 39.0278, lng: -94.5594, tradition: "pluralist", location_type: "in-person",
    notes: "Weekly Wednesday 6pm free meditation instruction + 7–7:30pm group meditation. Drop-in. Free.",
    source_url: "https://www.rimecenter.org", event_url: "https://www.rimecenter.org",
  },
  {
    org_id: "rime_buddhist_center", org_name: "Rime Buddhist Center",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 30,
    address: "2939 Wayne Avenue", city: "Kansas City", state: "MO", neighborhood: "Waldo/Brookside",
    lat: 39.0278, lng: -94.5594, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Thursday 6–6:45pm group meditation + 7–7:30pm Medicine Buddha Sadhana. Drop-in. Free.",
    source_url: "https://www.rimecenter.org", event_url: "https://www.rimecenter.org",
  },
  {
    org_id: "rime_buddhist_center", org_name: "Rime Buddhist Center",
    title: "Sunday Morning Service",
    days: ["Sunday"], time: { h: 10, m: 30 }, duration_min: 60,
    address: "2939 Wayne Avenue", city: "Kansas City", state: "MO", neighborhood: "Waldo/Brookside",
    lat: 39.0278, lng: -94.5594, tradition: "pluralist", location_type: "in-person",
    notes: "Sunday 10:30am Service/Practice. Childcare available. Drop-in. Free.",
    source_url: "https://www.rimecenter.org", event_url: "https://www.rimecenter.org",
  },

  // ── Kansas Zen Center — Kansas City branch — Unity Temple on the Plaza, 707 W 47th St, KC MO 64112
  // Kwan Um School of Zen. KC branch: Thursday 7pm in-person only.
  {
    org_id: "kansas_zen_center_kc", org_name: "Kansas Zen Center — Kansas City",
    title: "Thursday Evening Zen",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "707 West 47th Street", city: "Kansas City", state: "MO", neighborhood: "Country Club Plaza (at Unity Temple)",
    lat: 39.0462, lng: -94.5905, tradition: "zen", location_type: "in-person",
    notes: "Kwan Um School of Zen, in-person. 1st Thursday: Q&A with Zen Master Bon Hae. 4th Thursday: kong-an interviews. Drop-in welcome. Free.",
    source_url: "https://www.kansaszencenter.org", event_url: "https://www.kansaszencenter.org",
  },

  // ── Richmond, VA — all groups meet at Ekoji Buddhist Sangha, 3411 Grove Ave (Fan District) ──

  // IMCR — Theravada/Insight — Tue 7pm + Fri 5:45pm weekly sits (iCal captures retreats; these cover regular sits)
  {
    org_id: "imcr", org_name: "Insight Meditation Community of Richmond",
    title: "Tuesday Evening Sit",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "theravada", location_type: "hybrid",
    notes: "Sit, walking meditation, dharma talk + discussion. In-person at Ekoji + Zoom. Free; dana welcome.",
    source_url: "https://imcrva.org", event_url: "https://imcrva.org/weekly-events/",
  },
  {
    org_id: "imcr", org_name: "Insight Meditation Community of Richmond",
    title: "Friday Evening Sit",
    days: ["Friday"], time: { h: 17, m: 45 }, duration_min: 105,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "theravada", location_type: "hybrid",
    notes: "Sit, walking meditation, book reading + discussion. In-person at Ekoji + Zoom. Free; dana welcome.",
    source_url: "https://imcrva.org", event_url: "https://imcrva.org/weekly-events/",
  },

  // Richmond Zen — Soto Zen (Branching Streams / Shunryu Suzuki lineage)
  {
    org_id: "richmond_zen", org_name: "Richmond Zen",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 150,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen, Branching Streams lineage. In-person. Newcomer orientations offered regularly. Drop-in welcome. Free.",
    source_url: "https://www.richmondzen.org", event_url: "https://www.richmondzen.org",
  },
  {
    org_id: "richmond_zen", org_name: "Richmond Zen",
    title: "Tuesday Morning Zazen",
    days: ["Tuesday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "zen", location_type: "in-person",
    notes: "Early morning zazen. In-person at Ekoji. Drop-in welcome. Free.",
    source_url: "https://www.richmondzen.org", event_url: "https://www.richmondzen.org",
  },
  {
    org_id: "richmond_zen", org_name: "Richmond Zen",
    title: "Wednesday Evening Zazen",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen. In-person at Ekoji. Drop-in welcome. Free.",
    source_url: "https://www.richmondzen.org", event_url: "https://www.richmondzen.org",
  },
  {
    org_id: "richmond_zen", org_name: "Richmond Zen",
    title: "Friday Morning Zazen",
    days: ["Friday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "zen", location_type: "in-person",
    notes: "Early morning zazen. In-person at Ekoji. Drop-in welcome. Free.",
    source_url: "https://www.richmondzen.org", event_url: "https://www.richmondzen.org",
  },

  // Nyama Sangha — Shambhala lineage — Sat 10:30am
  {
    org_id: "nyama_sangha", org_name: "Nyama Sangha",
    title: "Saturday Morning Sit",
    days: ["Saturday"], time: { h: 10, m: 30 }, duration_min: 60,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "tibetan", location_type: "hybrid",
    notes: "Shambhala-lineage community sit. In-person at Ekoji + Zoom. No experience needed. Free; donations appreciated.",
    source_url: "https://ekojirichmond.org/richmond-shambhala/", event_url: "https://ekojirichmond.org/richmond-shambhala/",
  },

  // Palpung Shenpen Tharchin — Tibetan Kagyu — Thu 7pm
  {
    org_id: "palpung_richmond", org_name: "Palpung Shenpen Tharchin",
    title: "Thursday Evening Practice",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3411 Grove Avenue", city: "Richmond", state: "VA", neighborhood: "Fan District (at Ekoji)",
    lat: 37.5532, lng: -77.4774, tradition: "tibetan", location_type: "hybrid",
    notes: "Tibetan Kagyu (Palpung lineage), teacher Lama Linda. Rotating practices by week-of-month: Chenrezig, Green Tara, Medicine Buddha. In-person at Ekoji + Zoom. All welcome; newcomers welcome. Free.",
    source_url: "https://palpungrichmond.org", event_url: "https://palpungrichmond.org",
  },
];

const DAY_MAP = { Sunday:0, Monday:1, Tuesday:2, Wednesday:3, Thursday:4, Friday:5, Saturday:6 };

function eventId(orgId, title, start) {
  return crypto.createHash("sha256").update(`${orgId}:${title}:${start}`).digest("hex").slice(0, 16);
}

function pad(n) { return String(n).padStart(2, "0"); }

function generateInstances(sit, days_ahead = 90) {
  const events = [];
  const today = new Date();
  today.setHours(0,0,0,0);

  for (let d = 0; d <= days_ahead; d++) {
    const date = new Date(today);
    date.setDate(today.getDate() + d);
    const dow = date.getDay();

    if (!sit.days.some(day => DAY_MAP[day] === dow)) continue;

    // If specific dates provided, only generate on those dates
    if (sit.dates) {
      const dateStr = `${date.getFullYear()}-${pad(date.getMonth()+1)}-${pad(date.getDate())}`;
      if (!sit.dates.includes(dateStr)) continue;
    }

    // If week_of_month provided, only generate on nth occurrence of weekday in month
    if (sit.week_of_month) {
      const occurrenceInMonth = Math.ceil(date.getDate() / 7);
      if (occurrenceInMonth !== sit.week_of_month) continue;
    }

    const start = new Date(date);
    start.setHours(sit.time.h, sit.time.m, 0, 0);

    const end = new Date(start);
    end.setMinutes(end.getMinutes() + (sit.duration_min || 60));

    const startStr = `${start.getFullYear()}-${pad(start.getMonth()+1)}-${pad(start.getDate())}T${pad(start.getHours())}:${pad(start.getMinutes())}:00`;
    const endStr   = `${end.getFullYear()}-${pad(end.getMonth()+1)}-${pad(end.getDate())}T${pad(end.getHours())}:${pad(end.getMinutes())}:00`;

    events.push({
      id:                 eventId(sit.org_id, sit.title, startStr),
      org_id:             sit.org_id,
      org_name:           sit.org_name,
      title:              sit.title,
      start_time:         startStr,
      end_time:           endStr,
      address:            sit.address,
      city:               sit.city,
      state:              sit.state,
      neighborhood:       sit.neighborhood,
      lat:                sit.lat,
      lng:                sit.lng,
      tradition:          sit.tradition,
      location_type:      sit.location_type,
      is_sit:             1,
      accessibility_notes: null,
      identity_focus:     sit.identity_focus || null,
      source:             "manual",
      source_url:         sit.source_url,
      event_url:          sit.event_url,
      last_verified:      new Date().toISOString().slice(0, 10),
      recurrence:         (sit.dates || sit.week_of_month) ? "monthly" : "weekly",
      notes:              sit.notes || null,
    });
  }
  return events;
}

// Generate all instances
const allEvents = SITS.flatMap(s => generateInstances(s, 90));
console.log(`Generated ${allEvents.length} event instances from ${SITS.length} recurring sits`);

// POST to app
const resp = await fetch(`${APP_URL}/api/admin/events`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${INGEST_TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ events: allEvents }),
});

if (!resp.ok) {
  console.error(`POST failed: ${resp.status} ${await resp.text()}`);
  process.exit(1);
}

const result = await resp.json();
console.log(`✓ ${result.upserted} events upserted`);
