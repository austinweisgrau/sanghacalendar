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

  // ── Tucson, AZ ─────────────────────────────────────────────────────────────
  // Kadampa Meditation Center Arizona — Wix site (no iCal). NKT-IKBU.
  // 5326 E. Pima Street, Midtown / East Tucson. Verified 2026-05-18.
  // Schedule from /gp page: Sun 10am, Tue 6:30pm, Sat 10am.
  {
    org_id: "kmc_arizona_tucson", org_name: "Kadampa Meditation Center Arizona",
    title: "Sunday Morning Meditation Class",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 75,
    address: "5326 East Pima Street", city: "Tucson", state: "AZ", neighborhood: "Midtown / East Tucson",
    lat: 32.2432, lng: -110.8789, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome, no experience needed.",
    source_url: "https://www.meditationintucson.org", event_url: "https://www.meditationintucson.org/sunday-morning",
  },
  {
    org_id: "kmc_arizona_tucson", org_name: "Kadampa Meditation Center Arizona",
    title: "Tuesday Evening Meditation Class",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 75,
    address: "5326 East Pima Street", city: "Tucson", state: "AZ", neighborhood: "Midtown / East Tucson",
    lat: 32.2432, lng: -110.8789, tradition: "tibetan", location_type: "in-person",
    notes: "NKT General Program class. Guided meditation + dharma teaching. All welcome.",
    source_url: "https://www.meditationintucson.org", event_url: "https://www.meditationintucson.org/tuesday-evening",
  },
  {
    org_id: "kmc_arizona_tucson", org_name: "Kadampa Meditation Center Arizona",
    title: "Saturday Morning Drop-In Meditation",
    days: ["Saturday"], time: { h: 10, m: 0 }, duration_min: 30,
    address: "5326 East Pima Street", city: "Tucson", state: "AZ", neighborhood: "Midtown / East Tucson",
    lat: 32.2432, lng: -110.8789, tradition: "tibetan", location_type: "in-person",
    notes: "Short guided meditation session — drop in any time. Free. Part of NKT 'Simply Meditate' program.",
    source_url: "https://www.meditationintucson.org", event_url: "https://www.meditationintucson.org/simply-meditate",
  },

  // Insight Meditation Tucson — Theravada/Vipassana. Pima Friends Meeting House.
  // 931 N Fifth Ave, Tucson AZ 85705. Verified 2026-05-27.
  // Thu drop-in 6–7:45pm hybrid; 1st Mon 5:30–6:30pm beginner drop-in.
  {
    org_id: "insight_meditation_tucson", org_name: "Insight Meditation Tucson",
    title: "Thursday Evening Drop-In Sit",
    days: ["Thursday"], time: { h: 18, m: 0 }, duration_min: 105,
    address: "931 North Fifth Avenue", city: "Tucson", state: "AZ", neighborhood: "Armory Park / Barrio Historico",
    lat: 32.2282, lng: -110.9741, tradition: "theravada", location_type: "hybrid",
    notes: "Weekly drop-in: guided meditation, dharma talk, discussion. In-person + Zoom. All welcome, no experience needed.",
    source_url: "https://www.insightmeditationtucson.org", event_url: "https://www.insightmeditationtucson.org/classes",
  },

  // Tucson Community Meditation Center — non-sectarian Vipassana, founded 1984.
  // 1147 N Howard Blvd, Tucson AZ 85705. Verified 2026-05-27.
  // Mon 6pm, Tue 5pm, Wed 6pm (hybrid). Thu 6pm, 1st Sun 8:30am also offered.
  {
    org_id: "tcmc_tucson", org_name: "Tucson Community Meditation Center",
    title: "Monday Evening Sit — Meditating in Community",
    days: ["Monday"], time: { h: 18, m: 0 }, duration_min: 80,
    address: "1147 North Howard Boulevard", city: "Tucson", state: "AZ", neighborhood: "Midtown Tucson",
    lat: 32.2337, lng: -110.9734, tradition: "theravada", location_type: "hybrid",
    notes: "Hybrid in-person + Zoom. Guided meditation and community sitting. Drop-in, dana-based.",
    source_url: "https://tucsonmeditation.org", event_url: "https://tucsonmeditation.org/classes-sits/classes",
  },
  {
    org_id: "tcmc_tucson", org_name: "Tucson Community Meditation Center",
    title: "Tuesday Silent Sit",
    days: ["Tuesday"], time: { h: 17, m: 0 }, duration_min: 55,
    address: "1147 North Howard Boulevard", city: "Tucson", state: "AZ", neighborhood: "Midtown Tucson",
    lat: 32.2337, lng: -110.9734, tradition: "theravada", location_type: "in-person",
    notes: "Peer-led silent sitting meditation. In-person only. Drop-in, dana-based.",
    source_url: "https://tucsonmeditation.org", event_url: "https://tucsonmeditation.org/classes-sits/classes",
  },
  {
    org_id: "tcmc_tucson", org_name: "Tucson Community Meditation Center",
    title: "Wednesday Evening Sit — Mindfulness and Loving Kindness",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "1147 North Howard Boulevard", city: "Tucson", state: "AZ", neighborhood: "Midtown Tucson",
    lat: 32.2337, lng: -110.9734, tradition: "theravada", location_type: "hybrid",
    notes: "Guided mindfulness and loving kindness meditation. Hybrid in-person + Zoom. Drop-in, dana-based.",
    source_url: "https://tucsonmeditation.org", event_url: "https://tucsonmeditation.org/classes-sits/classes",
  },

  // Zen Desert Sangha — Diamond Sangha (Robert Aitken Roshi) lineage.
  // 3226 N Martin Ave, Tucson AZ 85712. Verified 2026-05-27.
  // Mon/Wed 6:30–8pm; Sat 7:30am–10:30am; Sun 5–6:30pm.
  {
    org_id: "zen_desert_sangha_tucson", org_name: "Zen Desert Sangha",
    title: "Evening Zazen",
    days: ["Monday", "Wednesday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "3226 North Martin Avenue", city: "Tucson", state: "AZ", neighborhood: "Richland Heights",
    lat: 32.2591, lng: -110.9232, tradition: "zen", location_type: "in-person",
    notes: "Monday and Wednesday evening zazen: sitting and walking meditation. All welcome; no advance contact needed. Free.",
    source_url: "https://www.zendesertsangha.org", event_url: "https://www.zendesertsangha.org/schedule",
  },
  {
    org_id: "zen_desert_sangha_tucson", org_name: "Zen Desert Sangha",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 7, m: 30 }, duration_min: 180,
    address: "3226 North Martin Avenue", city: "Tucson", state: "AZ", neighborhood: "Richland Heights",
    lat: 32.2591, lng: -110.9232, tradition: "zen", location_type: "hybrid",
    notes: "Tea 7:25am, zazen 7:30–8:30am, samu (work practice) 8:30–9am, chanting 9–9:30am, zazen 9:30–10:30am. Also on Zoom.",
    source_url: "https://www.zendesertsangha.org", event_url: "https://www.zendesertsangha.org/schedule",
  },
  {
    org_id: "zen_desert_sangha_tucson", org_name: "Zen Desert Sangha",
    title: "Sunday Evening Sitting",
    days: ["Sunday"], time: { h: 17, m: 0 }, duration_min: 90,
    address: "3226 North Martin Avenue", city: "Tucson", state: "AZ", neighborhood: "Richland Heights",
    lat: 32.2591, lng: -110.9232, tradition: "zen", location_type: "in-person",
    notes: "Sunday evening sitting, 5–6:30pm. All are welcome.",
    source_url: "https://www.zendesertsangha.org", event_url: "https://www.zendesertsangha.org/schedule",
  },

  // Awam Tibetan Buddhist Institute — Nyingma Dzogchen.
  // 301B N Longfellow Ave, Tucson AZ 85711. Verified 2026-05-27.
  // Sun 9:30am teachings (Zoom+YouTube), Wed 6pm mindfulness.
  {
    org_id: "awam_tbi_tucson", org_name: "Awam Tibetan Buddhist Institute",
    title: "Sunday Morning Teachings",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 60,
    address: "301B North Longfellow Avenue", city: "Tucson", state: "AZ", neighborhood: "Midtown Tucson",
    lat: 32.2362, lng: -110.9042, tradition: "tibetan", location_type: "hybrid",
    notes: "In-depth Dzogchen and Nyingma teachings. In-person + Zoom + YouTube livestream. All welcome.",
    source_url: "https://www.awaminstitute.org", event_url: "https://www.awaminstitute.org/schedule",
  },
  {
    org_id: "awam_tbi_tucson", org_name: "Awam Tibetan Buddhist Institute",
    title: "Wednesday Evening Mindfulness Practice",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 30,
    address: "301B North Longfellow Avenue", city: "Tucson", state: "AZ", neighborhood: "Midtown Tucson",
    lat: 32.2362, lng: -110.9042, tradition: "tibetan", location_type: "in-person",
    notes: "Brief mindfulness and meditation practice session. All welcome.",
    source_url: "https://www.awaminstitute.org", event_url: "https://www.awaminstitute.org/schedule",
  },

  // Desert Rain Zen — Harada-Yasutani Zen. UA campus.
  // Little Chapel of All Nations, 1401 E First St, Tucson AZ 85719. Verified 2026-05-27.
  // Thu 6:30–7:30pm hybrid; Sun 3:30–5pm Zoom.
  {
    org_id: "desert_rain_zen_tucson", org_name: "Desert Rain Zen",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 60,
    address: "1401 East First Street", city: "Tucson", state: "AZ", neighborhood: "University of Arizona Campus",
    lat: 32.2253, lng: -110.9459, tradition: "zen", location_type: "hybrid",
    notes: "Guided meditation, hybrid in-person + Zoom. Beginner-friendly. Contact desertrainzen@gmail.com for Zoom link.",
    source_url: "https://www.desertrainzen.org", event_url: "https://www.desertrainzen.org",
  },

  // ── Honolulu, HI ─────────────────────────────────────────────────────────
  // Honolulu Diamond Sangha (Ko Ko An Zendo) — no iCal. Zen (Robert Aitken lineage).
  // 2747 Waiomao Rd, Palolo, Honolulu HI 96816. Verified 2026-05-18.
  // Schedule: Mon–Fri 5:30am early morning zazen, Wed 7pm, Sun 9am.
  // Newcomers attend one-time orientation (1st Sat 9am–noon); then drop-in welcome.
  {
    org_id: "diamond_sangha_honolulu", org_name: "Honolulu Diamond Sangha",
    title: "Early Morning Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], time: { h: 5, m: 30 }, duration_min: 60,
    address: "2747 Waiomao Road", city: "Honolulu", state: "HI", neighborhood: "Palolo",
    lat: 21.3033, lng: -157.8018, tradition: "zen", location_type: "in-person",
    notes: "Early morning formal zazen, Mon–Fri 5:30–6:30am. Robert Aitken Roshi lineage. Newcomers must attend one-time Saturday orientation first.",
    source_url: "https://www.diamondsangha.org", event_url: "https://www.diamondsangha.org/practice/",
  },
  {
    org_id: "diamond_sangha_honolulu", org_name: "Honolulu Diamond Sangha",
    title: "Wednesday Evening Zazen",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "2747 Waiomao Road", city: "Honolulu", state: "HI", neighborhood: "Palolo",
    lat: 21.3033, lng: -157.8018, tradition: "zen", location_type: "in-person",
    notes: "Wednesday evening sitting, 7–9pm. Includes zazen and dharma discussion.",
    source_url: "https://www.diamondsangha.org", event_url: "https://www.diamondsangha.org/practice/",
  },
  {
    org_id: "diamond_sangha_honolulu", org_name: "Honolulu Diamond Sangha",
    title: "Sunday Morning Sitting",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 120,
    address: "2747 Waiomao Road", city: "Honolulu", state: "HI", neighborhood: "Palolo",
    lat: 21.3033, lng: -157.8018, tradition: "zen", location_type: "in-person",
    notes: "Sunday morning sitting 9–11am, followed by tea. All forms taught.",
    source_url: "https://www.diamondsangha.org", event_url: "https://www.diamondsangha.org/practice/",
  },
  // Soto Mission of Hawaii / Shoboji — no iCal. Soto Zen.
  // 1708 Nuuanu Ave, Honolulu HI 96817. Verified 2026-05-18.
  // Schedule: Mon/Wed/Fri 6:30am zazen (drop-in, no reservation), Sun 9:30am service.
  {
    org_id: "soto_mission_honolulu", org_name: "Soto Mission of Hawaii",
    title: "Morning Zazen",
    days: ["Monday", "Wednesday", "Friday"], time: { h: 6, m: 30 }, duration_min: 75,
    address: "1708 Nuuanu Avenue", city: "Honolulu", state: "HI", neighborhood: "Nuuanu",
    lat: 21.3219, lng: -157.8431, tradition: "zen", location_type: "in-person",
    notes: "Drop-in zazen Mon/Wed/Fri 6:30–7:45am. No reservation required; arrive 5 min early in comfortable clothes. Free, donations appreciated. Beginner-friendly.",
    source_url: "https://www.sotomission.org", event_url: "https://www.sotomission.org/services",
  },
  {
    org_id: "soto_mission_honolulu", org_name: "Soto Mission of Hawaii",
    title: "Sunday Service",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 60,
    address: "1708 Nuuanu Avenue", city: "Honolulu", state: "HI", neighborhood: "Nuuanu",
    lat: 21.3219, lng: -157.8431, tradition: "zen", location_type: "in-person",
    notes: "Sunday morning service 9:30am. Soto Zen (Shoboji). Open to the public.",
    source_url: "https://www.sotomission.org", event_url: "https://www.sotomission.org/services",
  },
  // Bodhi Tree Dharma Center — no iCal (Meetup-based). Multi-tradition.
  // 654A N. Judd St, Palama, Honolulu HI 96817. Verified 2026-05-18.
  // Schedule: Mon 6:30pm Vipassana, Tue 6:30pm Plum Village, Wed 6pm Stillness, Sat 9am Vipassana.
  {
    org_id: "bodhi_tree_honolulu", org_name: "Bodhi Tree Dharma Center",
    title: "Vipassana Meditation",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "654A N. Judd Street", city: "Honolulu", state: "HI", neighborhood: "Palama",
    lat: 21.3179, lng: -157.8443, tradition: "theravada", location_type: "in-person",
    notes: "Monday evening Vipassana Meditation, 6:30–8pm. Donation-based, beginner-friendly.",
    source_url: "https://www.bodhitreehawaii.com", event_url: "https://www.meetup.com/bodhi-tree-meditation-centerhonolulu/",
  },
  {
    org_id: "bodhi_tree_honolulu", org_name: "Bodhi Tree Dharma Center",
    title: "Honolulu Mindfulness Community Sit",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "654A N. Judd Street", city: "Honolulu", state: "HI", neighborhood: "Palama",
    lat: 21.3179, lng: -157.8443, tradition: "zen", location_type: "in-person",
    notes: "Plum Village / Thich Nhat Hanh lineage. 1st/2nd/3rd Tuesdays in-person; 4th Tuesday via Zoom. 6:30–8pm. Drop-in welcome.",
    source_url: "https://www.bodhitreehawaii.com", event_url: "https://www.honolulumindfulness.com/meditation-schedule.html",
  },
  {
    org_id: "bodhi_tree_honolulu", org_name: "Bodhi Tree Dharma Center",
    title: "Stillness and Awakenings Meditation",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "654A N. Judd Street", city: "Honolulu", state: "HI", neighborhood: "Palama",
    lat: 21.3179, lng: -157.8443, tradition: "theravada", location_type: "in-person",
    notes: "Wednesday evening Stillness and Awakenings Meditation, 6–7:30pm. Donation-based.",
    source_url: "https://www.bodhitreehawaii.com", event_url: "https://www.meetup.com/bodhi-tree-meditation-centerhonolulu/",
  },
  {
    org_id: "bodhi_tree_honolulu", org_name: "Bodhi Tree Dharma Center",
    title: "Guided Vipassana Meditation",
    days: ["Saturday"], time: { h: 9, m: 0 }, duration_min: 60,
    address: "654A N. Judd Street", city: "Honolulu", state: "HI", neighborhood: "Palama",
    lat: 21.3179, lng: -157.8443, tradition: "theravada", location_type: "in-person",
    notes: "Saturday morning guided Vipassana, 9–10am. Donation-based, beginner-friendly.",
    source_url: "https://www.bodhitreehawaii.com", event_url: "https://www.meetup.com/bodhi-tree-meditation-centerhonolulu/",
  },
  // Aloha Sangha — no iCal. Theravada / Insight Meditation.
  // 2439 Holomua Place, Palolo Valley, Honolulu HI 96816. Active since 1998.
  // Schedule: Thu 6pm (qigong + 2×25min sits + dharma talk).
  {
    org_id: "aloha_sangha_honolulu", org_name: "Aloha Sangha",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "2439 Holomua Place", city: "Honolulu", state: "HI", neighborhood: "Palolo Valley",
    lat: 21.2989, lng: -157.7997, tradition: "theravada", location_type: "in-person",
    notes: "Standing qigong + two 25-min sitting sessions + short dharma talk + Q&A. Beginner-friendly, donation-based. Operating since 1998. Limited parking — walk from 10th Ave.",
    source_url: "https://www.alohasangha.com", event_url: "https://www.alohasangha.com/meditation-hawaii/",
  },

  // ── Rochester, NY ────────────────────────────────────────────────────────
  // Rochester Zen Center — no iCal (Cloudflare blocks scraping).
  // 7 Arnold Park, Rochester NY 14607. Kapleau lineage, founded 1966.
  // Verified 2026-05-18.
  {
    org_id: "rzc", org_name: "Rochester Zen Center",
    title: "Morning Zazen",
    days: ["Tuesday", "Wednesday", "Thursday", "Friday"], time: { h: 6, m: 0 }, duration_min: 75,
    address: "7 Arnold Park", city: "Rochester", state: "NY", neighborhood: "Park Avenue",
    lat: 43.1596, lng: -77.5825, tradition: "zen", location_type: "in-person",
    notes: "Formal morning zazen (1 hr) + 15 min chanting service, Tue–Fri 6–7:15am. Philip Kapleau Roshi lineage. Newcomers welcome — contact RZC for orientation first.",
    source_url: "https://www.rzc.org", event_url: "https://www.rzc.org/sitting-schedule/",
  },
  {
    org_id: "rzc", org_name: "Rochester Zen Center",
    title: "Monday Evening Sitting",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "7 Arnold Park", city: "Rochester", state: "NY", neighborhood: "Park Avenue",
    lat: 43.1596, lng: -77.5825, tradition: "zen", location_type: "in-person",
    notes: "Three 35-min zazen rounds with kinhin; dokusan offered. 7–9pm. Philip Kapleau Roshi lineage.",
    source_url: "https://www.rzc.org", event_url: "https://www.rzc.org/sitting-schedule/",
  },
  {
    org_id: "rzc", org_name: "Rochester Zen Center",
    title: "Thursday Evening Sitting",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "7 Arnold Park", city: "Rochester", state: "NY", neighborhood: "Park Avenue",
    lat: 43.1596, lng: -77.5825, tradition: "zen", location_type: "in-person",
    notes: "Three 35-min zazen rounds with kinhin; dokusan offered. 7–9pm.",
    source_url: "https://www.rzc.org", event_url: "https://www.rzc.org/sitting-schedule/",
  },
  {
    org_id: "rzc", org_name: "Rochester Zen Center",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "7 Arnold Park", city: "Rochester", state: "NY", neighborhood: "Park Avenue",
    lat: 43.1596, lng: -77.5825, tradition: "zen", location_type: "in-person",
    notes: "Zazen only (no chanting service), 6:30–7:30am. Drop-in welcome after orientation.",
    source_url: "https://www.rzc.org", event_url: "https://www.rzc.org/sitting-schedule/",
  },
  {
    org_id: "rzc", org_name: "Rochester Zen Center",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 8, m: 30 }, duration_min: 120,
    address: "7 Arnold Park", city: "Rochester", state: "NY", neighborhood: "Park Avenue",
    lat: 43.1596, lng: -77.5825, tradition: "zen", location_type: "in-person",
    notes: "50-min zazen + kinhin + chanting + teisho (Dharma talk). 8:30–10:30am. Full formal Sunday program.",
    source_url: "https://www.rzc.org", event_url: "https://www.rzc.org/sitting-schedule/",
  },
  // Endless Path Zendo — no iCal (static HTML). Diamond Sangha / Kapleau lineage.
  // 56 Brighton St, Rochester NY 14607. Roshi Rafe Martin. Verified 2026-05-18.
  {
    org_id: "endless_path_zendo", org_name: "Endless Path Zendo",
    title: "Monday Evening Sitting",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "56 Brighton Street", city: "Rochester", state: "NY", neighborhood: "Swillburg",
    lat: 43.1540, lng: -77.5870, tradition: "zen", location_type: "hybrid",
    notes: "Informal Monday evening sitting, one zazen period, 7–8pm. In-person + Zoom. Roshi Rafe Martin (Diamond Sangha / Kapleau lineage).",
    source_url: "https://www.endlesspathzendo.org", event_url: "https://www.endlesspathzendo.org/calendar.html",
  },
  {
    org_id: "endless_path_zendo", org_name: "Endless Path Zendo",
    title: "Tuesday Evening Zazen",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "56 Brighton Street", city: "Rochester", state: "NY", neighborhood: "Swillburg",
    lat: 43.1540, lng: -77.5870, tradition: "zen", location_type: "hybrid",
    notes: "Three 25-min zazen periods, dokusan, kinhin, chanting service. 7–8:30pm. First-timers arrive 6:15pm for orientation.",
    source_url: "https://www.endlesspathzendo.org", event_url: "https://www.endlesspathzendo.org/calendar.html",
  },
  {
    org_id: "endless_path_zendo", org_name: "Endless Path Zendo",
    title: "Wednesday Morning Zazen",
    days: ["Wednesday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "56 Brighton Street", city: "Rochester", state: "NY", neighborhood: "Swillburg",
    lat: 43.1540, lng: -77.5870, tradition: "zen", location_type: "in-person",
    notes: "One hour zazen, dokusan offered. 6:30–7:30am.",
    source_url: "https://www.endlesspathzendo.org", event_url: "https://www.endlesspathzendo.org/calendar.html",
  },
  {
    org_id: "endless_path_zendo", org_name: "Endless Path Zendo",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 9, m: 0 }, duration_min: 150,
    address: "56 Brighton Street", city: "Rochester", state: "NY", neighborhood: "Swillburg",
    lat: 43.1540, lng: -77.5870, tradition: "zen", location_type: "hybrid",
    notes: "Three zazen periods, dokusan, kinhin, teisho, group discussion. 9–11:30am. In-person + Zoom.",
    source_url: "https://www.endlesspathzendo.org", event_url: "https://www.endlesspathzendo.org/calendar.html",
  },
  // Dharma Refuge — no iCal (Weebly). Tibetan-influenced (Anam Thubten / Lojong).
  // 1124 Culver Rd, Rochester NY 14609. Verified 2026-05-18.
  {
    org_id: "dharma_refuge_rochester", org_name: "Dharma Refuge",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 75,
    address: "1124 Culver Road", city: "Rochester", state: "NY", neighborhood: "Culver-University",
    lat: 43.1647, lng: -77.5604, tradition: "tibetan", location_type: "hybrid",
    notes: "Rotating format: guided sitting, video teaching (Anam Thubten / Pema Chodron), or book discussion. 7–8:15pm. In-person at Covenant United Methodist Church + Zoom. Donation-based, all welcome.",
    source_url: "https://www.dharmarefuge.com", event_url: "https://www.dharmarefuge.com/schedule.html",
  },
  {
    org_id: "dharma_refuge_rochester", org_name: "Dharma Refuge",
    title: "Saturday Morning Meditation",
    days: ["Saturday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "1124 Culver Road", city: "Rochester", state: "NY", neighborhood: "Culver-University",
    lat: 43.1647, lng: -77.5604, tradition: "tibetan", location_type: "hybrid",
    notes: "Saturday morning sit, 10–11:30am. In-person only for regular practice; hybrid when a guest teacher is present. Monthly all-day sit extends to 5pm.",
    source_url: "https://www.dharmarefuge.com", event_url: "https://www.dharmarefuge.com/schedule.html",
  },

  // ── Louisville, KY ────────────────────────────────────────────────────────
  // Louisville Zen Center — Rinzai-Soto (Kapleau lineage). Verified 2026-05-19.
  // 917 Rosemary Dr (Tue) / 1507 Bardstown Rd (Sun), Louisville KY 40205/40205.
  {
    org_id: "louisville_zen_center", org_name: "Louisville Zen Center",
    title: "Tuesday Evening Sitting",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "917 Rosemary Drive", city: "Louisville", state: "KY", neighborhood: "Highlands / Tyler Park",
    lat: 38.2355, lng: -85.7116, tradition: "zen", location_type: "hybrid",
    notes: "Hybrid in-person + Zoom sit, 6:30–8pm. Newcomer orientation at 6pm. Philip Kapleau / Rochester Zen Center lineage.",
    source_url: "https://www.louisvillezen.org", event_url: "https://www.louisvillezen.org/sittings.html",
  },
  {
    org_id: "louisville_zen_center", org_name: "Louisville Zen Center",
    title: "Sunday Evening Sitting",
    days: ["Sunday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "1507 Bardstown Road", city: "Louisville", state: "KY", neighborhood: "Highlands / Bardstown Road",
    lat: 38.2204, lng: -85.7212, tradition: "zen", location_type: "hybrid",
    notes: "Sunday evening hybrid sit at Infinite Bliss Yoga, 6:30–8pm. In-person + Zoom. Kapleau lineage.",
    source_url: "https://www.louisvillezen.org", event_url: "https://www.louisvillezen.org/sittings.html",
  },
  // Open Mind Zen Louisville — White Plum Asanga. Verified 2026-05-19.
  // 1013 Bardstown Rd, Louisville KY 40204. Global OMZ iCal is Melbourne-only.
  {
    org_id: "omz_louisville", org_name: "Open Mind Zen Louisville",
    title: "Saturday Morning Meditation",
    days: ["Saturday"], time: { h: 10, m: 30 }, duration_min: 90,
    address: "1013 Bardstown Road", city: "Louisville", state: "KY", neighborhood: "Highlands / Bardstown Road",
    lat: 38.2253, lng: -85.7212, tradition: "zen", location_type: "hybrid",
    notes: "Zazen + Dharma talk, 10:30am–noon. In-person at Garner Large art space (orange door, alley entrance) + Zoom. White Plum Asanga lineage. Drop-in, no registration.",
    source_url: "https://www.omzlouisville.com", event_url: "https://openmindzen.com/venue/open-mind-zen-louisville/",
  },
  // Sangha Lou (Louisville Community of Mindful Living) — Plum Village / TNH. Verified 2026-05-19.
  // 115 S Ewing Ave, Louisville KY 40206.
  {
    org_id: "sangha_lou", org_name: "Louisville Community of Mindful Living (Sangha Lou)",
    title: "Sunday Mindfulness Gathering",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "115 S Ewing Avenue", city: "Louisville", state: "KY", neighborhood: "Crescent Hill",
    lat: 38.2322, lng: -85.7069, tradition: "zen", location_type: "hybrid",
    notes: "Plum Village / Thich Nhat Hanh tradition. Sunday 10am–noon: sitting + walking meditation, dharma sharing, discussion. Hybrid in-person + Zoom. All welcome.",
    source_url: "https://www.sanghalou.org", event_url: "https://www.sanghalou.org",
  },
  // Louisville Vipassana Community — Theravada / Insight Meditation. Verified 2026-05-19.
  // Clifton Unitarian Universalist Church, 2231 Payne St, Louisville KY 40206.
  {
    org_id: "louisville_vipassana_community", org_name: "Louisville Vipassana Community",
    title: "Monday Evening Meditation",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "2231 Payne Street", city: "Louisville", state: "KY", neighborhood: "Clifton",
    lat: 38.2504, lng: -85.7105, tradition: "theravada", location_type: "hybrid",
    notes: "IMS-style Insight Meditation. At Clifton UU Church — guided sit + walking + dharma talk + discussion. 6:30–8pm, in-person + Zoom. Donation-based, all welcome.",
    source_url: "http://www.louisville-vipassana-community.org", event_url: "http://www.louisville-vipassana-community.org/schedule.html",
  },
  // Drepung Gomang Center for Engaging Compassion (DGCEC) — Tibetan (Gelugpa). Verified 2026-05-19.
  // 411 N Hubbards Lane, Louisville KY 40207. Calendarize iCal is JS-rendered (not scrapable).
  {
    org_id: "drepung_gomang_louisville", org_name: "Drepung Gomang Center for Engaging Compassion",
    title: "Wednesday Noontime Meditation",
    days: ["Wednesday"], time: { h: 12, m: 10 }, duration_min: 30,
    address: "411 N Hubbards Lane", city: "Louisville", state: "KY", neighborhood: "St. Matthews",
    lat: 38.2632, lng: -85.6900, tradition: "tibetan", location_type: "in-person",
    notes: "Brief 30-min noontime meditation, 12:10–12:40pm. In-person. All welcome. Gelugpa / Drepung Gomang lineage.",
    source_url: "https://www.drepunggomangusa.org", event_url: "https://www.drepunggomangusa.org/events-calendar/",
  },
  {
    org_id: "drepung_gomang_louisville", org_name: "Drepung Gomang Center for Engaging Compassion",
    title: "Wednesday Evening Community Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "411 N Hubbards Lane", city: "Louisville", state: "KY", neighborhood: "St. Matthews",
    lat: 38.2632, lng: -85.6900, tradition: "tibetan", location_type: "in-person",
    notes: "Community meditation with chanting and prayers, 7–8pm. In-person. Open to all. Resident Geshe teaching. Drepung Gomang Gelugpa lineage.",
    source_url: "https://www.drepunggomangusa.org", event_url: "https://www.drepunggomangusa.org/events-calendar/",
  },
  // Kentucky Meditation Peace Center (KMPC) — Theravada. Verified 2026-05-19.
  // 4815 Manslick Rd, Louisville KY 40216. Resident monks, Vipassana teaching.
  {
    org_id: "kmpc_louisville", org_name: "Kentucky Meditation Peace Center",
    title: "Monday Evening Group Meditation",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "4815 Manslick Road", city: "Louisville", state: "KY", neighborhood: "Pleasure Ridge Park / SW Jefferson",
    lat: 38.1755, lng: -85.8014, tradition: "theravada", location_type: "in-person",
    notes: "Weekly group Vipassana meditation with resident monks, 7–8:30pm. In-person. Beginner-friendly. Also operates as Kentucky Meditation Center and Buddhist Vihara (KMCBV).",
    source_url: "https://kmpc.co", event_url: "https://kmpc.co",
  },
  {
    org_id: "kmpc_louisville", org_name: "Kentucky Meditation Peace Center",
    title: "Wednesday Evening Group Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "4815 Manslick Road", city: "Louisville", state: "KY", neighborhood: "Pleasure Ridge Park / SW Jefferson",
    lat: 38.1755, lng: -85.8014, tradition: "theravada", location_type: "in-person",
    notes: "Weekly group Vipassana meditation with resident monks, 7–8:30pm. In-person. Beginner-friendly.",
    source_url: "https://kmpc.co", event_url: "https://kmpc.co",
  },

  // ── Providence, RI ────────────────────────────────────────────────────────
  // Providence Zen Center — live events via Tockify ICS (no recurring seeds needed).
  // pzc: Sunday Dharma Program + Wednesday sit handled by coordinator iCal fetch.

  // Atisha Kadampa Buddhist Center (AKBC) — NKT Tibetan. Verified 2026-05-19.
  // 339 Ives St, Fox Point, Providence RI 02906. meditationinrhodeisland.org
  {
    org_id: "akbc_providence", org_name: "Atisha Kadampa Buddhist Center",
    title: "Sunday Morning Meditation Class",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 75,
    address: "339 Ives Street", city: "Providence", state: "RI", neighborhood: "Fox Point",
    lat: 41.8198, lng: -71.3955, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Kadampa class: guided meditation + Buddhist teaching, 11am–12:15pm. In-person. Beginners welcome.",
    source_url: "https://meditationinrhodeisland.org", event_url: "https://meditationinrhodeisland.org/akbc-calendar/",
  },
  {
    org_id: "akbc_providence", org_name: "Atisha Kadampa Buddhist Center",
    title: "Monday Lunchtime Meditation",
    days: ["Monday"], time: { h: 12, m: 15 }, duration_min: 30,
    address: "339 Ives Street", city: "Providence", state: "RI", neighborhood: "Fox Point",
    lat: 41.8198, lng: -71.3955, tradition: "tibetan", location_type: "in-person",
    notes: "Brief lunchtime sitting meditation, 12:15–12:45pm. In-person. NKT Kadampa.",
    source_url: "https://meditationinrhodeisland.org", event_url: "https://meditationinrhodeisland.org/akbc-calendar/",
  },
  {
    org_id: "akbc_providence", org_name: "Atisha Kadampa Buddhist Center",
    title: "Wednesday Evening Meditation Class",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "339 Ives Street", city: "Providence", state: "RI", neighborhood: "Fox Point",
    lat: 41.8198, lng: -71.3955, tradition: "tibetan", location_type: "in-person",
    notes: "Evening meditation class, 6–7:30pm. Guided meditation + Buddhist teaching. NKT Kadampa. In-person.",
    source_url: "https://meditationinrhodeisland.org", event_url: "https://meditationinrhodeisland.org/akbc-calendar/",
  },
  {
    org_id: "akbc_providence", org_name: "Atisha Kadampa Buddhist Center",
    title: "Thursday Lunchtime Meditation",
    days: ["Thursday"], time: { h: 12, m: 15 }, duration_min: 30,
    address: "339 Ives Street", city: "Providence", state: "RI", neighborhood: "Fox Point",
    lat: 41.8198, lng: -71.3955, tradition: "tibetan", location_type: "in-person",
    notes: "Brief lunchtime sitting meditation, 12:15–12:45pm. In-person. NKT Kadampa.",
    source_url: "https://meditationinrhodeisland.org", event_url: "https://meditationinrhodeisland.org/akbc-calendar/",
  },
  // Insight Meditation Community of Providence (IMCP) — 1st & 3rd Thursday. Verified 2026-05-19.
  // 354 Broadway, West End, Providence RI 02909. insightprovidence.org
  {
    org_id: "imcp", org_name: "Insight Meditation Community of Providence",
    title: "Thursday Evening Meditation Sit",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90, week_of_month: 1,
    address: "354 Broadway", city: "Providence", state: "RI", neighborhood: "Broadway / West End",
    lat: 41.8220, lng: -71.4272, tradition: "theravada", location_type: "in-person",
    notes: "1st Thursday of each month. 40-min silent sit + Dharma reading + discussion. Vipassana/Insight Meditation. Drop-in, donation-based.",
    source_url: "https://www.insightprovidence.org", event_url: "https://www.insightprovidence.org",
  },
  {
    org_id: "imcp", org_name: "Insight Meditation Community of Providence",
    title: "Thursday Evening Meditation Sit",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90, week_of_month: 3,
    address: "354 Broadway", city: "Providence", state: "RI", neighborhood: "Broadway / West End",
    lat: 41.8220, lng: -71.4272, tradition: "theravada", location_type: "in-person",
    notes: "3rd Thursday of each month. 40-min silent sit + Dharma reading + discussion. Vipassana/Insight Meditation. Drop-in, donation-based.",
    source_url: "https://www.insightprovidence.org", event_url: "https://www.insightprovidence.org",
  },
  // Insight Meditation Sangha Providence — Wednesday evenings. Verified 2026-05-19.
  // 27 Sims Ave, West End, Providence RI 02909. insightpvd.com
  {
    org_id: "insight_pvd", org_name: "Insight Meditation Sangha Providence",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "27 Sims Avenue", city: "Providence", state: "RI", neighborhood: "West End",
    lat: 41.8164, lng: -71.4256, tradition: "theravada", location_type: "in-person",
    notes: "Weekly Vipassana/Insight meditation sit, Wednesday evenings. Drop-in, donation-based.",
    source_url: "https://www.insightpvd.com", event_url: "https://www.insightpvd.com",
  },
  // RI Community of Mindfulness — Radiant Bell Sangha (Plum Village). Verified 2026-05-19.
  // Bell Street Chapel, 5 Bell St, Providence RI 02909. mindfulnessri.org
  {
    org_id: "ricm_radiant_bell", org_name: "RI Community of Mindfulness – Radiant Bell Sangha",
    title: "Saturday Morning Mindfulness Gathering",
    days: ["Saturday"], time: { h: 8, m: 0 }, duration_min: 90,
    address: "5 Bell Street", city: "Providence", state: "RI", neighborhood: "College Hill / Wayland Square",
    lat: 41.8248, lng: -71.4290, tradition: "zen", location_type: "in-person",
    notes: "Plum Village / Thich Nhat Hanh lineage. Sitting meditation, walking meditation, Dharma talk/reading. At Bell Street Chapel. 8–9:30am. Free, all welcome.",
    source_url: "https://www.mindfulnessri.org", event_url: "https://www.mindfulnessri.org/sanghas/",
  },

  // ── Indianapolis, IN ──────────────────────────────────────────────────────
  // KMC Indianapolis (Dromtonpa Kadampa) — NKT Tibetan. Verified 2026-05-19.
  // 4010 W 86th St Ste C, NW Indianapolis IN 46268. meditation-indianapolis.org
  {
    org_id: "kmc_indianapolis", org_name: "Kadampa Meditation Center Indianapolis",
    title: "Sunday General Program",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 75,
    address: "4010 W 86th Street, Suite C", city: "Indianapolis", state: "IN", neighborhood: "NW Indianapolis / North Willow",
    lat: 39.9080, lng: -86.2012, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Kadampa class: guided meditation + Buddhist teaching. 11am–12:15pm. In-person. Beginners welcome; suggested donation ~$12.",
    source_url: "https://www.meditation-indianapolis.org", event_url: "https://www.meditation-indianapolis.org/calendar",
  },
  {
    org_id: "kmc_indianapolis", org_name: "Kadampa Meditation Center Indianapolis",
    title: "Thursday Evening Meditation Class",
    days: ["Thursday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "4010 W 86th Street, Suite C", city: "Indianapolis", state: "IN", neighborhood: "NW Indianapolis / North Willow",
    lat: 39.9080, lng: -86.2012, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Kadampa evening class: guided meditation + Buddhist teaching. 6–7pm. In-person. Drop-in welcome.",
    source_url: "https://www.meditation-indianapolis.org", event_url: "https://www.meditation-indianapolis.org/calendar",
  },
  {
    org_id: "kmc_indianapolis", org_name: "Kadampa Meditation Center Indianapolis",
    title: "Friday Morning Meditation Class",
    days: ["Friday"], time: { h: 10, m: 0 }, duration_min: 75,
    address: "4010 W 86th Street, Suite C", city: "Indianapolis", state: "IN", neighborhood: "NW Indianapolis / North Willow",
    lat: 39.9080, lng: -86.2012, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Kadampa morning class: guided meditation + Buddhist teaching. 10–11:15am. In-person. Drop-in welcome.",
    source_url: "https://www.meditation-indianapolis.org", event_url: "https://www.meditation-indianapolis.org/calendar",
  },
  // Indianapolis Zen Center — Kwan Um Korean Zen (Seung Sahn lineage). Verified 2026-05-19.
  // 3703 N. Washington Blvd, Meridian-Kessler, Indianapolis IN 46205. indyzen.org
  {
    org_id: "indianapolis_zen_center", org_name: "Indianapolis Zen Center",
    title: "Monday Evening Sit",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3703 N. Washington Boulevard", city: "Indianapolis", state: "IN", neighborhood: "Meridian-Kessler",
    lat: 39.8373, lng: -86.1569, tradition: "zen", location_type: "hybrid",
    notes: "Two 25-min sitting periods + walking meditation. Doors open 6:30pm. Hybrid in-person + Zoom (bit.ly/IndyZen). Drop-in, no charge. Kwan Um School of Zen.",
    source_url: "https://www.indyzen.org", event_url: "https://www.indyzen.org/practice",
  },
  {
    org_id: "indianapolis_zen_center", org_name: "Indianapolis Zen Center",
    title: "Wednesday Evening Sit",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3703 N. Washington Boulevard", city: "Indianapolis", state: "IN", neighborhood: "Meridian-Kessler",
    lat: 39.8373, lng: -86.1569, tradition: "zen", location_type: "hybrid",
    notes: "Two 25-min sitting periods + walking meditation. Doors open 6:30pm. Hybrid in-person + Zoom (bit.ly/IndyZen). Drop-in, no charge. Kwan Um School of Zen.",
    source_url: "https://www.indyzen.org", event_url: "https://www.indyzen.org/practice",
  },
  {
    org_id: "indianapolis_zen_center", org_name: "Indianapolis Zen Center",
    title: "Morning Practice",
    days: ["Monday", "Wednesday", "Friday"], time: { h: 6, m: 45 }, duration_min: 30,
    address: "3703 N. Washington Boulevard", city: "Indianapolis", state: "IN", neighborhood: "Meridian-Kessler",
    lat: 39.8373, lng: -86.1569, tradition: "zen", location_type: "hybrid",
    notes: "25–30 min meditation + reading and discussion. 6:45–7:15am. Hybrid in-person + Zoom (bit.ly/IndyZen). Drop-in, no charge.",
    source_url: "https://www.indyzen.org", event_url: "https://www.indyzen.org/practice",
  },
  {
    org_id: "indianapolis_zen_center", org_name: "Indianapolis Zen Center",
    title: "Saturday Morning Practice",
    days: ["Saturday"], time: { h: 9, m: 30 }, duration_min: 60,
    address: "3703 N. Washington Boulevard", city: "Indianapolis", state: "IN", neighborhood: "Meridian-Kessler",
    lat: 39.8373, lng: -86.1569, tradition: "zen", location_type: "hybrid",
    notes: "Chanting + sitting or walking meditation. 9:30–10:30am. Hybrid in-person + Zoom (bit.ly/IndyZen). Drop-in, no charge. Monthly retreat 2nd Saturday.",
    source_url: "https://www.indyzen.org", event_url: "https://www.indyzen.org/practice",
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

  // ── Columbus, OH ──────────────────────────────────────────────────────────────
  // Columbus KTC — Karma Kagyu Tibetan — Sunday hybrid sits (iCal also feeds these)
  {
    org_id: "columbus_ktc", org_name: "Columbus Karma Thegsum Choling",
    title: "Introduction to Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "645 W. Rich Street", city: "Columbus", state: "OH", neighborhood: "Franklinton",
    lat: 39.9553, lng: -83.0057, tradition: "tibetan", location_type: "hybrid",
    notes: "Karma Kagyu lineage (affiliated with KTD monastery, Woodstock NY). Founded 1977. Guided meditation introduction open to all levels. In-person + virtual. Free.",
    source_url: "https://columbusktc.org", event_url: "https://columbusktc.org/schedule/",
  },

  // Mud Lotus Sangha — Soto Zen (White Plum lineage) — 3 weekly sits at ILLIO Studios
  {
    org_id: "mud_lotus_sangha", org_name: "Mud Lotus Sangha",
    title: "Morning Meditation",
    days: ["Tuesday"], time: { h: 7, m: 30 }, duration_min: 30,
    address: "17 E. Tulane Road", city: "Columbus", state: "OH", neighborhood: "Clintonville (at ILLIO Studios)",
    lat: 40.0135, lng: -82.9975, tradition: "zen", location_type: "in_person",
    notes: "Soto Zen, White Plum lineage. Early morning sit at ILLIO Studios. Drop-in; free.",
    source_url: "https://www.mudlotussangha.org", event_url: "https://www.mudlotussangha.org/weekly-meditation",
  },
  {
    org_id: "mud_lotus_sangha", org_name: "Mud Lotus Sangha",
    title: "Evening Zen Meditation",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "17 E. Tulane Road", city: "Columbus", state: "OH", neighborhood: "Clintonville (at ILLIO Studios)",
    lat: 40.0135, lng: -82.9975, tradition: "zen", location_type: "in_person",
    notes: "Soto Zen, White Plum lineage. Zazen + dharma discussion at ILLIO Studios. Drop-in; free.",
    source_url: "https://www.mudlotussangha.org", event_url: "https://www.mudlotussangha.org/weekly-meditation",
  },
  {
    org_id: "mud_lotus_sangha", org_name: "Mud Lotus Sangha",
    title: "Morning Meditation",
    days: ["Thursday"], time: { h: 9, m: 0 }, duration_min: 60,
    address: "17 E. Tulane Road", city: "Columbus", state: "OH", neighborhood: "Clintonville (at ILLIO Studios)",
    lat: 40.0135, lng: -82.9975, tradition: "zen", location_type: "hybrid",
    notes: "Soto Zen, White Plum lineage. Morning sit at ILLIO Studios + Zoom hybrid. Drop-in; free.",
    source_url: "https://www.mudlotussangha.org", event_url: "https://www.mudlotussangha.org/weekly-meditation",
  },

  // Zen Columbus Sangha — independent Soto Zen — Tue + Sat at First UU Church
  {
    org_id: "zen_columbus", org_name: "Zen Columbus Sangha",
    title: "Zazen",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 75,
    address: "93 W. Weisheimer Road", city: "Columbus", state: "OH", neighborhood: "Clintonville (at First UU Church)",
    lat: 40.0569, lng: -83.0201, tradition: "zen", location_type: "hybrid",
    notes: "Independent Soto Zen. Two 25-min zazen periods + kinhin + brief service. In-person + Zoom. Drop-in; free.",
    source_url: "http://zencolumbus.org", event_url: "http://zencolumbus.org/schedule.html",
  },
  {
    org_id: "zen_columbus", org_name: "Zen Columbus Sangha",
    title: "Zazen",
    days: ["Saturday"], time: { h: 8, m: 30 }, duration_min: 75,
    address: "93 W. Weisheimer Road", city: "Columbus", state: "OH", neighborhood: "Clintonville (at First UU Church)",
    lat: 40.0569, lng: -83.0201, tradition: "zen", location_type: "hybrid",
    notes: "Independent Soto Zen. Two 25-min zazen periods + kinhin + brief service. In-person + Zoom. Drop-in; free.",
    source_url: "http://zencolumbus.org", event_url: "http://zencolumbus.org/schedule.html",
  },

  // COCPB — Pragmatic Buddhism (Zen/Nikayan/Chan) — Sunday zazen at private zendo
  {
    org_id: "cocpb_columbus", org_name: "Central Ohio Center for Pragmatic Buddhism",
    title: "Sunday Zazen",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 150,
    address: "77 N. Brinker Avenue", city: "Columbus", state: "OH", neighborhood: "West Side",
    lat: 39.9706, lng: -83.0453, tradition: "zen", location_type: "in_person",
    notes: "Pragmatic Buddhism: synthesis of Nikayan, Chan, Zen, and Pragmatist philosophy. Zazen + dharma talk. Private zendo (2nd floor, enter via back). All welcome; donations appreciated.",
    source_url: "https://www.cocpb.com", event_url: "https://www.cocpb.com",
  },

  // Bliss Run Sangha — Plum Village / Thich Nhat Hanh — Thu evenings at Unity Church
  {
    org_id: "bliss_run_sangha", org_name: "Bliss Run Sangha",
    title: "Thursday Evening Practice",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "4211 Maize Road", city: "Columbus", state: "OH", neighborhood: "North Linden (at Unity Church)",
    lat: 40.0762, lng: -82.9981, tradition: "other", location_type: "in_person",
    notes: "Plum Village (Thich Nhat Hanh / Order of Interbeing). Walking meditation, sitting meditation, dharma discussion. Newcomer orientation 6:45pm. Drop-in; free.",
    source_url: "https://www.blissrun.org", event_url: "https://www.blissrun.org/home/meetings",
  },

  // ─── Research Triangle, NC (Raleigh-Durham-Chapel Hill) ────────────────────

  // Durham Shambhala Meditation Center — 733 Rutherford St, Durham NC
  {
    org_id: "durham_shambhala", org_name: "Durham Shambhala Meditation Center",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 180,
    address: "733 Rutherford Street", city: "Durham", state: "NC", neighborhood: "Duke Park",
    lat: 36.0018, lng: -78.9281, tradition: "tibetan", location_type: "in-person",
    notes: "Shambhala tradition. Group meditation open to all. In-person at Durham Shambhala Center. All welcome; no experience required. Free.",
    source_url: "https://durham.shambhala.org", event_url: "https://durham.shambhala.org/monthly-calendar/",
  },
  {
    org_id: "durham_shambhala", org_name: "Durham Shambhala Meditation Center",
    title: "Thursday Night Open House",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "733 Rutherford Street", city: "Durham", state: "NC", neighborhood: "Duke Park",
    lat: 36.0018, lng: -78.9281, tradition: "tibetan", location_type: "in-person",
    notes: "Shambhala tradition. Free meditation instruction at 7pm, group sitting + walking meditation until 8pm, then refreshments. Great introduction for newcomers. In-person.",
    source_url: "https://durham.shambhala.org", event_url: "https://durham.shambhala.org/monthly-calendar/",
  },
  {
    org_id: "durham_shambhala", org_name: "Durham Shambhala Meditation Center",
    title: "Saturday Dharma Discussions",
    days: ["Saturday"], time: { h: 10, m: 30 }, duration_min: 90,
    address: "733 Rutherford Street", city: "Durham", state: "NC", neighborhood: "Duke Park",
    lat: 36.0018, lng: -78.9281, tradition: "tibetan", location_type: "online",
    notes: "Shambhala tradition. Weekly Zoom gathering for meditations, contemplations, and group discussion. Online only.",
    source_url: "https://durham.shambhala.org", event_url: "https://durham.shambhala.org/monthly-calendar/",
  },
  {
    org_id: "durham_shambhala", org_name: "Durham Shambhala Meditation Center",
    title: "Heart of Recovery",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "733 Rutherford Street", city: "Durham", state: "NC", neighborhood: "Duke Park",
    lat: 36.0018, lng: -78.9281, tradition: "tibetan", location_type: "in-person",
    notes: "Shambhala Heart of Recovery support group — meditation and community for those in recovery. In-person. All welcome.",
    source_url: "https://durham.shambhala.org", event_url: "https://durham.shambhala.org/monthly-calendar/",
  },

  // Chapel Hill Zen Center — 5322 NC Hwy 86, Chapel Hill NC (SFZC Soto lineage)
  {
    org_id: "chapel_hill_zen", org_name: "Chapel Hill Zen Center",
    title: "Morning Zazen",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday"], time: { h: 6, m: 0 }, duration_min: 55,
    address: "5322 NC Highway 86", city: "Chapel Hill", state: "NC", neighborhood: "North Chapel Hill",
    lat: 35.9763, lng: -79.0485, tradition: "zen", location_type: "hybrid",
    notes: "Soto Zen (Shunryu Suzuki-roshi / SFZC lineage). Two periods of zazen: 6am and 6:50am. In-person and Zoom. All welcome; arrive on time.",
    source_url: "https://www.chzc.org", event_url: "https://www.chzc.org",
  },
  {
    org_id: "chapel_hill_zen", org_name: "Chapel Hill Zen Center",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 55,
    address: "5322 NC Highway 86", city: "Chapel Hill", state: "NC", neighborhood: "North Chapel Hill",
    lat: 35.9763, lng: -79.0485, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen. Two periods of zazen: 9am and 9:50am. Instruction available for newcomers. In-person only.",
    source_url: "https://www.chzc.org", event_url: "https://www.chzc.org",
  },
  {
    org_id: "chapel_hill_zen", org_name: "Chapel Hill Zen Center",
    title: "Tuesday Evening Zazen",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 55,
    address: "5322 NC Highway 86", city: "Chapel Hill", state: "NC", neighborhood: "North Chapel Hill",
    lat: 35.9763, lng: -79.0485, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen. Two periods of zazen: 7pm and 7:50pm. Instruction available for newcomers. In-person only.",
    source_url: "https://www.chzc.org", event_url: "https://www.chzc.org",
  },

  // North Carolina Zen Center — 390 Ironwood Rd, Pittsboro NC (Teshin Roshi)
  {
    org_id: "nc_zen_center", org_name: "North Carolina Zen Center",
    title: "Sunday Practice",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "390 Ironwood Road", city: "Pittsboro", state: "NC", neighborhood: "Rural Chatham County",
    lat: 35.7268, lng: -79.1823, tradition: "zen", location_type: "in-person",
    notes: "Two periods of zazen, chanting service, and dharma talk (Teisho). Community work period and brunch follow. All welcome. In-person.",
    source_url: "https://nczencenter.org", event_url: "https://nczencenter.org/practice-meetings/",
  },
  {
    org_id: "nc_zen_center", org_name: "North Carolina Zen Center",
    title: "Morning Zazen",
    days: ["Monday"], time: { h: 7, m: 0 }, duration_min: 50,
    address: "390 Ironwood Road", city: "Pittsboro", state: "NC", neighborhood: "Rural Chatham County",
    lat: 35.7268, lng: -79.1823, tradition: "zen", location_type: "online",
    notes: "Monday morning zazen, Zoom only.",
    source_url: "https://nczencenter.org", event_url: "https://nczencenter.org/practice-meetings/",
  },
  {
    org_id: "nc_zen_center", org_name: "North Carolina Zen Center",
    title: "Dharma Study and Zazen",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "390 Ironwood Road", city: "Pittsboro", state: "NC", neighborhood: "Rural Chatham County",
    lat: 35.7268, lng: -79.1823, tradition: "zen", location_type: "in-person",
    notes: "One period of zazen and dharma discussion. In-person.",
    source_url: "https://nczencenter.org", event_url: "https://nczencenter.org/practice-meetings/",
  },
  {
    org_id: "nc_zen_center", org_name: "North Carolina Zen Center",
    title: "Morning Zazen",
    days: ["Wednesday","Friday"], time: { h: 7, m: 0 }, duration_min: 50,
    address: "390 Ironwood Road", city: "Pittsboro", state: "NC", neighborhood: "Rural Chatham County",
    lat: 35.7268, lng: -79.1823, tradition: "zen", location_type: "hybrid",
    notes: "Morning zazen in-person and on Zoom.",
    source_url: "https://nczencenter.org", event_url: "https://nczencenter.org/practice-meetings/",
  },
  {
    org_id: "nc_zen_center", org_name: "North Carolina Zen Center",
    title: "Zazen and Chanting Service",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "390 Ironwood Road", city: "Pittsboro", state: "NC", neighborhood: "Rural Chatham County",
    lat: 35.7268, lng: -79.1823, tradition: "zen", location_type: "in-person",
    notes: "Chanting service and two periods of zazen. Dokusan (private teacher interview) available. In-person.",
    source_url: "https://nczencenter.org", event_url: "https://nczencenter.org/practice-meetings/",
  },

  // ─── Salt Lake City, UT ──────────────────────────────────────────────────

  // Two Arrows Zen — 21 G Street, Salt Lake City UT (White Plum Asanga / Soto Zen)
  {
    org_id: "two_arrows_zen", org_name: "Two Arrows Zen",
    title: "Morning Zazen",
    days: ["Monday","Tuesday","Wednesday","Thursday","Friday"], time: { h: 7, m: 0 }, duration_min: 75,
    address: "21 G Street", city: "Salt Lake City", state: "UT", neighborhood: "The Avenues",
    lat: 40.7729, lng: -111.8844, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen (White Plum Asanga lineage). Two periods of zazen (7:00am and 7:40am) with kinhin. In-person at the zendo. Drop-in welcome; arrive before the bell. Free.",
    source_url: "https://twoarrowszen.org", event_url: "https://twoarrowszen.org/events/",
  },
  {
    org_id: "two_arrows_zen", org_name: "Two Arrows Zen",
    title: "Evening Zen Service",
    days: ["Thursday"], time: { h: 17, m: 30 }, duration_min: 150,
    address: "21 G Street", city: "Salt Lake City", state: "UT", neighborhood: "The Avenues",
    lat: 40.7729, lng: -111.8844, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen. Thursday evening program (5:30–8pm): zazen, kinhin, dharma talk, and dokusan (private teacher interview). Beginners welcome. In-person.",
    source_url: "https://twoarrowszen.org", event_url: "https://twoarrowszen.org/events/",
  },

  // Urgyen Samten Ling Gonpa — 740 S 300 West, Salt Lake City UT (Nyingma Tibetan)
  {
    org_id: "urgyen_samten_ling", org_name: "Urgyen Samten Ling Gonpa",
    title: "Chenrezig Practice",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "740 South 300 West", city: "Salt Lake City", state: "UT", neighborhood: "Downtown Salt Lake City",
    lat: 40.7520, lng: -111.9006, tradition: "tibetan", location_type: "online",
    notes: "Nyingma Tibetan tradition. Weekly Chenrezig (Avalokiteshvara) practice via Zoom. Open to the public; no prior experience required. Register at urgyensamtenling.org.",
    source_url: "https://www.urgyensamtenling.org", event_url: "https://www.urgyensamtenling.org/classes",
  },

  // ─── New Orleans, LA ─────────────────────────────────────────────────────

  // New Orleans Zen Temple — 8338 Oak St 2nd Fl, New Orleans LA (Soto Zen / AZI)
  {
    org_id: "nozt", org_name: "New Orleans Zen Temple",
    title: "Evening Zazen",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "8338 Oak Street, 2nd Floor", city: "New Orleans", state: "LA", neighborhood: "Riverbend / Carrollton",
    lat: 29.9370, lng: -90.1195, tradition: "zen", location_type: "hybrid",
    notes: "Soto Zen (Taisen Deshimaru / Association Zen Internationale lineage). Tuesday evening zazen, in-person and Zoom. New practitioners register via noztinfo@gmail.com. Donation-based.",
    source_url: "https://www.neworleanszentemple.org", event_url: "https://www.neworleanszentemple.org",
  },
  {
    org_id: "nozt", org_name: "New Orleans Zen Temple",
    title: "Morning Zazen",
    days: ["Thursday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "8338 Oak Street, 2nd Floor", city: "New Orleans", state: "LA", neighborhood: "Riverbend / Carrollton",
    lat: 29.9370, lng: -90.1195, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen. Thursday early morning zazen, in-person only. New practitioners register via noztinfo@gmail.com. Donation-based.",
    source_url: "https://www.neworleanszentemple.org", event_url: "https://www.neworleanszentemple.org",
  },
  {
    org_id: "nozt", org_name: "New Orleans Zen Temple",
    title: "Sunday Zazen",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "8338 Oak Street, 2nd Floor", city: "New Orleans", state: "LA", neighborhood: "Riverbend / Carrollton",
    lat: 29.9370, lng: -90.1195, tradition: "zen", location_type: "in-person",
    notes: "Soto Zen. Sunday morning zazen, in-person. New practitioners register via noztinfo@gmail.com. Donation-based.",
    source_url: "https://www.neworleanszentemple.org", event_url: "https://www.neworleanszentemple.org",
  },

  // Mid City Zen — 3248 Castiglione St, New Orleans LA (Soto Zen / SFZC lineage)
  // Note: special events (dharma talks, retreats, queer zen, etc.) come from Google Calendar iCal
  {
    org_id: "mid_city_zen", org_name: "Mid City Zen",
    title: "Morning Zazen",
    days: ["Monday","Wednesday","Friday"], time: { h: 8, m: 0 }, duration_min: 45,
    address: "3248 Castiglione St", city: "New Orleans", state: "LA", neighborhood: "Mid-City",
    lat: 29.9634, lng: -90.0888, tradition: "zen", location_type: "hybrid",
    notes: "Soto Zen (Suzuki Roshi / SFZC lineage). Monday, Wednesday, and Friday morning zazen at 8am, in-person and Zoom. Drop-in welcome; dana basis.",
    source_url: "https://midcityzen.org", event_url: "https://midcityzen.org/schedule/",
  },
  {
    org_id: "mid_city_zen", org_name: "Mid City Zen",
    title: "Sunday Program",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 75,
    address: "3248 Castiglione St", city: "New Orleans", state: "LA", neighborhood: "Mid-City",
    lat: 29.9634, lng: -90.0888, tradition: "zen", location_type: "hybrid",
    notes: "Soto Zen. Sunday morning program: chanting, zazen, dharma talk or study group. In-person and Zoom. 2nd/4th Sundays: Beginner's Instruction at 8:45am. 1st Sunday: half-day sit.",
    source_url: "https://midcityzen.org", event_url: "https://midcityzen.org/schedule/",
  },

  // -----------------------------------------------------------------------
  // Tampa Bay Phase 3
  // -----------------------------------------------------------------------

  // Kadampa Meditation Center Tampa Bay (Safety Harbor, FL)
  {
    org_id: "kmc_tampa_bay", org_name: "Kadampa Meditation Center Tampa Bay",
    title: "General Program",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 75,
    address: "201 6th Ave S", city: "Safety Harbor", state: "FL", neighborhood: "Safety Harbor",
    lat: 27.9869, lng: -82.6932, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Sunday 'Meditations for World Peace' class: guided meditation and Buddhist teachings. Drop-in welcome; fee or by donation.",
    source_url: "https://meditationintampabay.org", event_url: "https://meditationintampabay.org/weekly-meditation-courses/classes-at-the-safety-harbor-center/",
  },
  {
    org_id: "kmc_tampa_bay", org_name: "Kadampa Meditation Center Tampa Bay",
    title: "General Program",
    days: ["Tuesday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "201 6th Ave S", city: "Safety Harbor", state: "FL", neighborhood: "Safety Harbor",
    lat: 27.9869, lng: -82.6932, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Tuesday morning General Program: guided meditation and Buddhist teachings. Drop-in welcome.",
    source_url: "https://meditationintampabay.org", event_url: "https://meditationintampabay.org/weekly-meditation-courses/classes-at-the-safety-harbor-center/",
  },
  {
    org_id: "kmc_tampa_bay", org_name: "Kadampa Meditation Center Tampa Bay",
    title: "General Program",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 75,
    address: "201 6th Ave S", city: "Safety Harbor", state: "FL", neighborhood: "Safety Harbor",
    lat: 27.9869, lng: -82.6932, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Thursday evening General Program with Kadam Michelle Gauthier: guided meditation and Buddhist teachings. Drop-in welcome.",
    source_url: "https://meditationintampabay.org", event_url: "https://meditationintampabay.org/weekly-meditation-courses/classes-at-the-safety-harbor-center/",
  },

  // Clear Water Zen Center (Clearwater, FL)
  {
    org_id: "clear_water_zen", org_name: "Clear Water Zen Center",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 120,
    address: "2476 Nursery Rd", city: "Clearwater", state: "FL", neighborhood: "South Clearwater",
    lat: 27.9328, lng: -82.7555, tradition: "zen", location_type: "in-person",
    notes: "Zen. Formal zazen: three 35-min rounds with walking meditation (kinhin) between. First Sunday: meditation and chanting. Other Sundays: zazen with dharma talk. Newcomers arrive by 9am.",
    source_url: "https://www.clearwaterzencenter.org", event_url: "https://www.clearwaterzencenter.org/my-calendar/schedule",
  },
  {
    org_id: "clear_water_zen", org_name: "Clear Water Zen Center",
    title: "Open Meditation",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "2476 Nursery Rd", city: "Clearwater", state: "FL", neighborhood: "South Clearwater",
    lat: 27.9328, lng: -82.7555, tradition: "zen", location_type: "in-person",
    notes: "Zen. Three 20-min zazen rounds with walking meditation between. Drop-in, all welcome. Free; donations appreciated.",
    source_url: "https://www.clearwaterzencenter.org", event_url: "https://www.clearwaterzencenter.org/my-calendar/schedule",
  },
  {
    org_id: "clear_water_zen", org_name: "Clear Water Zen Center",
    title: "Beginner Meditation Class",
    days: ["Wednesday"], time: { h: 18, m: 45 }, duration_min: 75,
    address: "2476 Nursery Rd", city: "Clearwater", state: "FL", neighborhood: "South Clearwater",
    lat: 27.9328, lng: -82.7555, tradition: "zen", location_type: "in-person",
    notes: "Zen. Beginner's meditation class: instruction at 6:45pm, practice begins promptly at 7pm. Suitable for newcomers and ongoing practitioners.",
    source_url: "https://www.clearwaterzencenter.org", event_url: "https://www.clearwaterzencenter.org/my-calendar/schedule",
  },
  {
    org_id: "clear_water_zen", org_name: "Clear Water Zen Center",
    title: "Open Meditation",
    days: ["Friday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "2476 Nursery Rd", city: "Clearwater", state: "FL", neighborhood: "South Clearwater",
    lat: 27.9328, lng: -82.7555, tradition: "zen", location_type: "in-person",
    notes: "Zen. Three 20-min zazen rounds with walking meditation between. Drop-in, all welcome. Free; donations appreciated.",
    source_url: "https://www.clearwaterzencenter.org", event_url: "https://www.clearwaterzencenter.org/my-calendar/schedule",
  },

  // Shambhala Meditation Center of St. Petersburg (St. Petersburg, FL)
  {
    org_id: "shambhala_stpete", org_name: "Shambhala Meditation Center of St. Petersburg",
    title: "Sunday Community Practice",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "5901 Haines Rd N", city: "St. Petersburg", state: "FL", neighborhood: "North St. Petersburg",
    lat: 27.8284, lng: -82.6788, tradition: "tibetan", location_type: "in-person",
    notes: "Shambhala lineage. Extended sitting and walking meditation 10am–noon; participants may come and go. Informal meditation instruction at 11am followed by open discussion. First Sunday monthly: 'Learn to Meditate' intro 9am–noon.",
    source_url: "https://stpetersburg.shambhala.org", event_url: "https://stpetersburg.shambhala.org/ongoing-offerings/",
  },
  {
    org_id: "shambhala_stpete", org_name: "Shambhala Meditation Center of St. Petersburg",
    title: "Tuesday Evening Contemplations",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "5901 Haines Rd N", city: "St. Petersburg", state: "FL", neighborhood: "North St. Petersburg",
    lat: 27.8284, lng: -82.6788, tradition: "tibetan", location_type: "online",
    notes: "Shambhala lineage. Zoom-only. Sitting meditation with instruction and contemplation practice. Online.",
    source_url: "https://stpetersburg.shambhala.org", event_url: "https://stpetersburg.shambhala.org/ongoing-offerings/",
  },

  // -----------------------------------------------------------------------
  // Charlotte, NC Phase 3
  // -----------------------------------------------------------------------

  // Charlotte Buddhist Vihara — 3423 Stonehaven Dr, Charlotte NC 28215 (Theravada)
  {
    org_id: "charlotte_vihara", org_name: "Charlotte Buddhist Vihara",
    title: "Evening of Personal Growth",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "3423 Stonehaven Dr", city: "Charlotte", state: "NC", neighborhood: "Northeast Charlotte",
    lat: 35.2379, lng: -80.7626, tradition: "theravada", location_type: "hybrid",
    notes: "Theravada. Tuesday evening: Dhamma talk and guided meditation. Led by Ayya Sudhamma. In-person and Zoom. Drop-in welcome; donations appreciated.",
    source_url: "https://www.charlottebuddhistvihara.org", event_url: "https://www.charlottebuddhistvihara.org/schedule/",
  },
  {
    org_id: "charlotte_vihara", org_name: "Charlotte Buddhist Vihara",
    title: "Morning Meditation",
    days: ["Wednesday"], time: { h: 10, m: 30 }, duration_min: 60,
    address: "3423 Stonehaven Dr", city: "Charlotte", state: "NC", neighborhood: "Northeast Charlotte",
    lat: 35.2379, lng: -80.7626, tradition: "theravada", location_type: "hybrid",
    notes: "Theravada. Wednesday morning meditation. In-person and Zoom. Drop-in welcome.",
    source_url: "https://www.charlottebuddhistvihara.org", event_url: "https://www.charlottebuddhistvihara.org/schedule/",
  },
  {
    org_id: "charlotte_vihara", org_name: "Charlotte Buddhist Vihara",
    title: "Meditation for Awakening",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "3423 Stonehaven Dr", city: "Charlotte", state: "NC", neighborhood: "Northeast Charlotte",
    lat: 35.2379, lng: -80.7626, tradition: "theravada", location_type: "hybrid",
    notes: "Theravada. Thursday evening: Dhamma talk and guided meditation. In-person and Zoom. Drop-in welcome; donations appreciated.",
    source_url: "https://www.charlottebuddhistvihara.org", event_url: "https://www.charlottebuddhistvihara.org/schedule/",
  },
  {
    org_id: "charlotte_vihara", org_name: "Charlotte Buddhist Vihara",
    title: "Buddhist Teachings",
    days: ["Saturday"], time: { h: 14, m: 0 }, duration_min: 90,
    address: "3423 Stonehaven Dr", city: "Charlotte", state: "NC", neighborhood: "Northeast Charlotte",
    lat: 35.2379, lng: -80.7626, tradition: "theravada", location_type: "hybrid",
    notes: "Theravada. Saturday afternoon: Dhamma talk and guided meditation. In-person and Zoom. Drop-in welcome; donations appreciated.",
    source_url: "https://www.charlottebuddhistvihara.org", event_url: "https://www.charlottebuddhistvihara.org/schedule/",
  },

  // Insight Meditation Community of Charlotte (IMCC) — 3900 Park Road, Charlotte NC 28209
  {
    org_id: "imcc", org_name: "Insight Meditation Community of Charlotte",
    title: "Dharma Talk and Meditation",
    days: ["Tuesday"], time: { h: 12, m: 0 }, duration_min: 60,
    address: "3900 Park Road", city: "Charlotte", state: "NC", neighborhood: "South Charlotte / Park Road",
    lat: 35.1870, lng: -80.8565, tradition: "theravada", location_type: "online",
    notes: "Vipassana / Insight Meditation. Tuesday noon: Dharma teaching followed by 30-min silent meditation. Zoom only. Drop-in welcome; dana basis.",
    source_url: "https://www.imccharlotte.org", event_url: "https://www.imccharlotte.org/schedule/",
  },
  {
    org_id: "imcc", org_name: "Insight Meditation Community of Charlotte",
    title: "Wednesday Evening Sit",
    days: ["Wednesday"], time: { h: 19, m: 30 }, duration_min: 90,
    address: "3900 Park Road", city: "Charlotte", state: "NC", neighborhood: "South Charlotte / Park Road",
    lat: 35.1870, lng: -80.8565, tradition: "theravada", location_type: "hybrid",
    notes: "Vipassana / Insight Meditation. Wednesday 7pm: newcomer instruction (in-person); 7:30pm: silent meditation and Dharma talk (in-person and Zoom). Drop-in welcome; dana basis.",
    source_url: "https://www.imccharlotte.org", event_url: "https://www.imccharlotte.org/schedule/",
  },

  // Kadampa Meditation Center North Carolina — 528 East Blvd, Charlotte NC 28203 (NKT Tibetan)
  {
    org_id: "kmc_nc", org_name: "Kadampa Meditation Center North Carolina",
    title: "General Program",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 90,
    address: "528 East Blvd", city: "Charlotte", state: "NC", neighborhood: "Dilworth",
    lat: 35.2153, lng: -80.8422, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Sunday morning drop-in class with guided meditation and Buddhist teachings. All welcome; no experience required.",
    source_url: "https://www.meditationcharlotte.org", event_url: "https://www.meditationcharlotte.org/calendar",
  },
  {
    org_id: "kmc_nc", org_name: "Kadampa Meditation Center North Carolina",
    title: "General Program",
    days: ["Tuesday"], time: { h: 17, m: 0 }, duration_min: 60,
    address: "528 East Blvd", city: "Charlotte", state: "NC", neighborhood: "Dilworth",
    lat: 35.2153, lng: -80.8422, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Tuesday drop-in class with guided meditation and Buddhist teachings. All welcome.",
    source_url: "https://www.meditationcharlotte.org", event_url: "https://www.meditationcharlotte.org/calendar",
  },
  {
    org_id: "kmc_nc", org_name: "Kadampa Meditation Center North Carolina",
    title: "General Program",
    days: ["Wednesday"], time: { h: 17, m: 0 }, duration_min: 90,
    address: "528 East Blvd", city: "Charlotte", state: "NC", neighborhood: "Dilworth",
    lat: 35.2153, lng: -80.8422, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Wednesday drop-in class with guided meditation and Buddhist teachings. Also Foundation Program on Wednesdays. All welcome.",
    source_url: "https://www.meditationcharlotte.org", event_url: "https://www.meditationcharlotte.org/calendar",
  },
  {
    org_id: "kmc_nc", org_name: "Kadampa Meditation Center North Carolina",
    title: "General Program",
    days: ["Thursday"], time: { h: 17, m: 0 }, duration_min: 90,
    address: "528 East Blvd", city: "Charlotte", state: "NC", neighborhood: "Dilworth",
    lat: 35.2153, lng: -80.8422, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Thursday drop-in class with guided meditation and Buddhist teachings. All welcome.",
    source_url: "https://www.meditationcharlotte.org", event_url: "https://www.meditationcharlotte.org/calendar",
  },
  {
    org_id: "kmc_nc", org_name: "Kadampa Meditation Center North Carolina",
    title: "General Program",
    days: ["Saturday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "528 East Blvd", city: "Charlotte", state: "NC", neighborhood: "Dilworth",
    lat: 35.2153, lng: -80.8422, tradition: "tibetan", location_type: "in-person",
    notes: "NKT Tibetan. Saturday morning drop-in class with guided meditation and Buddhist teachings. All welcome; no experience required.",
    source_url: "https://www.meditationcharlotte.org", event_url: "https://www.meditationcharlotte.org/calendar",
  },

  // Charlotte Community of Mindfulness (CCM) — 1931 Selwyn Ave, Charlotte NC 28207 (Plum Village)
  {
    org_id: "ccm_charlotte", org_name: "Charlotte Community of Mindfulness",
    title: "Sunday Morning Sangha",
    days: ["Sunday"], time: { h: 8, m: 30 }, duration_min: 90,
    address: "1931 Selwyn Ave", city: "Charlotte", state: "NC", neighborhood: "Myers Park",
    lat: 35.2025, lng: -80.8400, tradition: "zen", location_type: "hybrid",
    notes: "Plum Village (Thich Nhat Hanh lineage). Sunday morning: sitting meditation, walking meditation, Dharma reading, sharing circle. In-person and Zoom. Last Sunday: Recitation ceremony. Free; donations welcomed.",
    source_url: "https://www.charlottemindfulness.org", event_url: "https://www.charlottemindfulness.org/visit/schedule/",
  },

  // ── Oklahoma City, OK ─────────────────────────────────────────────────────
  // Oklahoma Buddhist Vihara — Theravada. Verified 2026-05-20.
  // 4820 N Portland Ave, Oklahoma City OK 73112. okbv.org
  {
    org_id: "okbv", org_name: "Oklahoma Buddhist Vihara",
    title: "Wednesday Silent Meditation",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "4820 N Portland Ave", city: "Oklahoma City", state: "OK", neighborhood: "Nichols Hills area / Uptown OKC",
    lat: 35.5005, lng: -97.5263, tradition: "theravada", location_type: "in-person",
    notes: "One-hour silent sitting meditation. In-person at the Vihara. Open to all traditions and backgrounds; no experience required. Free; donations welcome.",
    source_url: "https://okbv.org", event_url: "https://okbv.org/calendar",
  },
  {
    org_id: "okbv", org_name: "Oklahoma Buddhist Vihara",
    title: "Saturday Pali Chanting & Meditation",
    days: ["Saturday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "4820 N Portland Ave", city: "Oklahoma City", state: "OK", neighborhood: "Nichols Hills area / Uptown OKC",
    lat: 35.5005, lng: -97.5263, tradition: "theravada", location_type: "in-person",
    notes: "Pali chanting of the Buddha's teachings followed by silent meditation. In-person at the Vihara. All are welcome. Free; donations welcome.",
    source_url: "https://okbv.org", event_url: "https://okbv.org/calendar",
  },
  {
    org_id: "okbv", org_name: "Oklahoma Buddhist Vihara",
    title: "Sunday Guided Meditation & Discussion",
    days: ["Sunday"], time: { h: 17, m: 0 }, duration_min: 60,
    address: "4820 N Portland Ave", city: "Oklahoma City", state: "OK", neighborhood: "Nichols Hills area / Uptown OKC",
    lat: 35.5005, lng: -97.5263, tradition: "theravada", location_type: "hybrid",
    notes: "30-min guided meditation followed by 30-min Dhamma discussion. Hybrid: in-person + Google Meet. All backgrounds welcome. Free; donations welcome.",
    source_url: "https://okbv.org", event_url: "https://okbv.org/calendar",
  },
  // Buddha Mind Monastery OKC — Chinese Mahayana/Zen. Verified 2026-05-20.
  // 5800 S Anderson Rd, Oklahoma City OK 73150. ctbuddhamind.org
  {
    org_id: "buddha_mind_okc", org_name: "Buddha Mind Monastery",
    title: "Sunday Guided Meditation",
    days: ["Sunday"], time: { h: 15, m: 0 }, duration_min: 60,
    address: "5800 S Anderson Rd", city: "Oklahoma City", state: "OK", neighborhood: "SE Oklahoma City",
    lat: 35.3908, lng: -97.4218, tradition: "zen", location_type: "in-person",
    notes: "One-hour guided meditation open to all. Free. Chinese Mahayana/Zen monastery founded 2004. Monthly half-day retreats and dharma ceremonies also offered. Open daily 2–5pm.",
    source_url: "https://www.ctbuddhamind.org", event_url: "https://www.ctbuddhamind.org/class-event-schedule/?lang=en",
  },

  // ── Bloomington, IN ───────────────────────────────────────────────────────
  // TMBCC (Tibetan Mongolian Buddhist Cultural Center) — Tibetan (Gelug). Verified 2026-05-20.
  // 3655 S Snoddy Rd, Bloomington IN 47401. tmbcc.org. No iCal (?ical=1 → 404).
  {
    org_id: "tmbcc", org_name: "Tibetan Mongolian Buddhist Cultural Center",
    title: "Monday Group Meditation",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 60,
    address: "3655 S Snoddy Road", city: "Bloomington", state: "IN", neighborhood: "South Bloomington",
    lat: 39.1198, lng: -86.5097, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly group meditation at the TMBCC Kumbum Chamtse Ling campus. Open to all. Free. 108-acre center founded by Thubten Norbu, elder brother of the Dalai Lama.",
    source_url: "https://tmbcc.org", event_url: "https://tmbcc.org/events/",
  },
  {
    org_id: "tmbcc", org_name: "Tibetan Mongolian Buddhist Cultural Center",
    title: "Wednesday Open Meditation",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "3655 S Snoddy Road", city: "Bloomington", state: "IN", neighborhood: "South Bloomington",
    lat: 39.1198, lng: -86.5097, tradition: "tibetan", location_type: "in-person",
    notes: "Open meditation session: sit in stillness, prayer, or meditation. Open to anyone regardless of tradition or experience. Free.",
    source_url: "https://tmbcc.org", event_url: "https://tmbcc.org/events/",
  },
  {
    org_id: "tmbcc", org_name: "Tibetan Mongolian Buddhist Cultural Center",
    title: "Sunday Buddhist Philosophy Teachings",
    days: ["Sunday"], time: { h: 10, m: 30 }, duration_min: 90,
    address: "3655 S Snoddy Road", city: "Bloomington", state: "IN", neighborhood: "South Bloomington",
    lat: 39.1198, lng: -86.5097, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Buddhist philosophy teachings. Open to all. Free. First Sunday of the month includes newcomer orientation at 2pm.",
    source_url: "https://tmbcc.org", event_url: "https://tmbcc.org/events/",
  },
  // KMC Bloomington — NKT Tibetan. Verified 2026-05-20.
  // 234 N. Morton St, Bloomington IN 47404. meditationinbloomington.org. Wix site, no iCal.
  {
    org_id: "kmc_bloomington", org_name: "Kadampa Meditation Center Bloomington",
    title: "Tuesday Evening Meditation Class",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 75,
    address: "234 N. Morton Street", city: "Bloomington", state: "IN", neighborhood: "Downtown Bloomington",
    lat: 39.1662, lng: -86.5340, tradition: "tibetan", location_type: "in-person",
    notes: "Drop-in class combining guided meditation with Buddhist teachings (Kadampa style). No experience needed. Suggested donation. Also available via Zoom for members.",
    source_url: "https://www.meditationinbloomington.org", event_url: "https://www.meditationinbloomington.org/calendar",
  },
  {
    org_id: "kmc_bloomington", org_name: "Kadampa Meditation Center Bloomington",
    title: "Wednesday Lunchtime Meditation",
    days: ["Wednesday"], time: { h: 12, m: 15 }, duration_min: 30,
    address: "234 N. Morton Street", city: "Bloomington", state: "IN", neighborhood: "Downtown Bloomington",
    lat: 39.1662, lng: -86.5340, tradition: "tibetan", location_type: "in-person",
    notes: "30-min lunchtime guided meditation. Drop-in, no experience needed. Suggested donation. Downtown Bloomington near IU campus.",
    source_url: "https://www.meditationinbloomington.org", event_url: "https://www.meditationinbloomington.org/calendar",
  },
  {
    org_id: "kmc_bloomington", org_name: "Kadampa Meditation Center Bloomington",
    title: "Sunday General Program",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 75,
    address: "234 N. Morton Street", city: "Bloomington", state: "IN", neighborhood: "Downtown Bloomington",
    lat: 39.1662, lng: -86.5340, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly General Program: guided meditation + Buddhist teachings. Drop-in, all welcome. Suggested donation. Also available via streaming for members.",
    source_url: "https://www.meditationinbloomington.org", event_url: "https://www.meditationinbloomington.org/calendar",
  },
  // Open Mind Zen Indiana — Zen. Verified 2026-05-20.
  // Bloomington Friends Meeting House, 3820 E. Moores Pike, Bloomington IN 47402.
  {
    org_id: "open_mind_zen_indiana", org_name: "Open Mind Zen Indiana",
    title: "Monday Evening Zen Sit",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "3820 E. Moores Pike", city: "Bloomington", state: "IN", neighborhood: "East Bloomington / Friends Meeting House",
    lat: 39.1539, lng: -86.4839, tradition: "zen", location_type: "in-person",
    notes: "Weekly Monday evening Zen practice: zazen sitting and walking meditation, koan study, dharma talks. Open to all; no experience required. Free (donations welcomed).",
    source_url: "https://openmindzenbloomington.org", event_url: "https://openmindzenbloomington.org/schedule/",
  },
  // Hoosier Heartland Shambhala Meditation Group — Shambhala. Verified 2026-05-20.
  // Three weekly sits at three Bloomington venues. hhsmg.shambhala.org
  {
    org_id: "hoosier_heartland_shambhala", org_name: "Hoosier Heartland Shambhala Meditation Group",
    title: "Monday Open Sit",
    days: ["Monday"], time: { h: 12, m: 0 }, duration_min: 60,
    address: "2120 N Fee Lane", city: "Bloomington", state: "IN", neighborhood: "North Bloomington / UU Church",
    lat: 39.1810, lng: -86.5282, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly open sit at Unitarian Universalist Church. Hybrid: in-person + Zoom. No experience required. Shambhala tradition (Chögyam Trungpa lineage). Free.",
    source_url: "https://hhsmg.shambhala.org", event_url: "https://hhsmg.shambhala.org/ongoing-offerings/",
  },
  {
    org_id: "hoosier_heartland_shambhala", org_name: "Hoosier Heartland Shambhala Meditation Group",
    title: "Thursday Evening Sit",
    days: ["Thursday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "3655 S Snoddy Road", city: "Bloomington", state: "IN", neighborhood: "South Bloomington / TMBCC",
    lat: 39.1198, lng: -86.5097, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly evening sit held at the Tibetan Mongolian Buddhist Cultural Center (TMBCC) campus. No experience required. Shambhala tradition. Free.",
    source_url: "https://hhsmg.shambhala.org", event_url: "https://hhsmg.shambhala.org/ongoing-offerings/",
  },
  {
    org_id: "hoosier_heartland_shambhala", org_name: "Hoosier Heartland Shambhala Meditation Group",
    title: "Friday Night Sit",
    days: ["Friday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "2401 N. Walnut Street", city: "Bloomington", state: "IN", neighborhood: "North Bloomington / Center for Wholism",
    lat: 39.1752, lng: -86.5253, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Friday evening sit at Center for Wholism. Instruction 6–6:30pm; group sitting and walking meditation 6:30–7:30pm. No experience required. Shambhala tradition. Free.",
    source_url: "https://hhsmg.shambhala.org", event_url: "https://hhsmg.shambhala.org/ongoing-offerings/",
  },

  // -----------------------------------------------------------------------
  // Cleveland, OH — Phase 3 (heartbeat 51)
  // -----------------------------------------------------------------------

  // Cleveland Shambhala Meditation Center — Lakewood, OH
  // shambhala-koeln.de iCal (center=240) returning 522; seeding recurring sits.
  // cleveland.shambhala.org/ongoing-offerings/
  {
    org_id: "cleveland_shambhala", org_name: "Cleveland Shambhala Meditation Center",
    title: "Sunday Morning Sit",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "17309 Madison Avenue", city: "Cleveland", state: "OH", neighborhood: "Lakewood",
    lat: 41.4815, lng: -81.8025, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly Sunday morning open sit. Alternating sitting and walking meditation periods. No experience required; walk-in welcome. Shambhala tradition (Chögyam Trungpa lineage). Free.",
    source_url: "https://cleveland.shambhala.org", event_url: "https://cleveland.shambhala.org/ongoing-offerings/",
  },
  {
    org_id: "cleveland_shambhala", org_name: "Cleveland Shambhala Meditation Center",
    title: "Tuesday Evening Sit",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "17309 Madison Avenue", city: "Cleveland", state: "OH", neighborhood: "Lakewood",
    lat: 41.4815, lng: -81.8025, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly Tuesday evening open sit. Alternating sitting and walking meditation periods. No experience required; walk-in welcome. Shambhala tradition. Free.",
    source_url: "https://cleveland.shambhala.org", event_url: "https://cleveland.shambhala.org/ongoing-offerings/",
  },
  {
    org_id: "cleveland_shambhala", org_name: "Cleveland Shambhala Meditation Center",
    title: "Wednesday Morning Sit",
    days: ["Wednesday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "17309 Madison Avenue", city: "Cleveland", state: "OH", neighborhood: "Lakewood",
    lat: 41.4815, lng: -81.8025, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly Wednesday morning open sit. Alternating sitting and walking meditation periods. No experience required; walk-in welcome. Shambhala tradition. Free.",
    source_url: "https://cleveland.shambhala.org", event_url: "https://cleveland.shambhala.org/ongoing-offerings/",
  },

  // Insight Meditation Cleveland — Shaker Heights sitting group
  // First Unitarian Church of Cleveland, 21600 Shaker Blvd
  // imcleveland.org/groups/
  {
    org_id: "imc_cleveland", org_name: "Insight Meditation Cleveland",
    title: "Thursday Evening Sit",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "21600 Shaker Boulevard", city: "Cleveland", state: "OH", neighborhood: "Shaker Heights / First Unitarian Church",
    lat: 41.4726, lng: -81.5575, tradition: "vipassana", location_type: "in-person",
    notes: "Weekly Thursday evening Insight Meditation sitting group at First Unitarian Church of Cleveland. Includes guided sitting, walking meditation, and dharma discussion. Drop-in; no registration; dana-based. All levels welcome.",
    source_url: "https://imcleveland.org", event_url: "https://imcleveland.org/groups/",
  },

  // Crooked River Zen Center — Cleveland Heights, OH
  // Soto Zen; teacher Sensei Dean Williams. Site suspended on Bluehost.
  // szba.org/crooked-river-zen-center confirms schedule.
  {
    org_id: "crooked_river_zen", org_name: "Crooked River Zen Center",
    title: "Tuesday Evening Zazen",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "1813 Wilton Road", city: "Cleveland", state: "OH", neighborhood: "Cleveland Heights",
    lat: 41.5095, lng: -81.5695, tradition: "zen", location_type: "hybrid",
    notes: "Weekly Tuesday evening zazen: two 15-minute sitting periods, kinhin (walking meditation), chanting, and short dharma talk. In-person + Google Meet. Drop-in welcome. Soto Zen; no experience required.",
    source_url: "https://www.crookedriverzen.org", event_url: "https://www.crookedriverzen.org",
  },
  {
    org_id: "crooked_river_zen", org_name: "Crooked River Zen Center",
    title: "Thursday Evening Zazen",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "1813 Wilton Road", city: "Cleveland", state: "OH", neighborhood: "Cleveland Heights",
    lat: 41.5095, lng: -81.5695, tradition: "zen", location_type: "hybrid",
    notes: "Weekly Thursday evening zazen: two 25-minute sitting periods, kinhin, chanting, and dharma talk. In-person + Google Meet. Drop-in welcome. Soto Zen; no experience required.",
    source_url: "https://www.crookedriverzen.org", event_url: "https://www.crookedriverzen.org",
  },
  {
    org_id: "crooked_river_zen", org_name: "Crooked River Zen Center",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 90,
    address: "1813 Wilton Road", city: "Cleveland", state: "OH", neighborhood: "Cleveland Heights",
    lat: 41.5095, lng: -81.5695, tradition: "zen", location_type: "hybrid",
    notes: "Weekly Sunday morning zazen: two 30-minute sitting periods, kinhin, chanting, and dharma talk. In-person + Google Meet. Drop-in welcome. Soto Zen; no experience required.",
    source_url: "https://www.crookedriverzen.org", event_url: "https://www.crookedriverzen.org",
  },

  // Cleveland Zazen Group — Cleveland Heights, OH
  // Kapleau/Rochester Zen lineage. 40+ year continuous practice. zencleveland.com
  {
    org_id: "cleveland_zazen_group", org_name: "Cleveland Zazen Group",
    title: "Tuesday Evening Zazen",
    days: ["Tuesday"], time: { h: 19, m: 30 }, duration_min: 75,
    address: "1813 Wilton Road", city: "Cleveland", state: "OH", neighborhood: "Cleveland Heights",
    lat: 41.5097, lng: -81.5697, tradition: "zen", location_type: "in-person",
    notes: "Weekly Tuesday evening zazen: two rounds of sitting and kinhin (walking meditation), occasional chanting. Kapleau/Rochester Zen lineage. Drop-in; no prior experience necessary.",
    source_url: "https://www.zencleveland.com", event_url: "https://www.zencleveland.com/schedule-events",
  },
  {
    org_id: "cleveland_zazen_group", org_name: "Cleveland Zazen Group",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 120,
    address: "1813 Wilton Road", city: "Cleveland", state: "OH", neighborhood: "Cleveland Heights",
    lat: 41.5097, lng: -81.5697, tradition: "zen", location_type: "in-person",
    notes: "Weekly Sunday morning zazen with group instruction, dharma talks, teisho, and work practice. Kapleau/Rochester Zen lineage. Drop-in; no prior experience necessary.",
    source_url: "https://www.zencleveland.com", event_url: "https://www.zencleveland.com/schedule-events",
  },

  // CloudWater Zendo — Parma, OH (southwest Cleveland metro)
  // Chan Buddhist and Pure Land (Dragon Flower Ch'an Temples). cloudwater.org
  {
    org_id: "cloudwater_zendo", org_name: "CloudWater Zendo",
    title: "Tuesday Evening Meditation",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "4388 W Pleasant Valley Road", city: "Cleveland", state: "OH", neighborhood: "Parma",
    lat: 41.3738, lng: -81.7645, tradition: "zen", location_type: "in-person",
    notes: "Weekly Tuesday evening: two periods of seated meditation, walking meditation, chanting, and dharma talk. Chan Buddhist and Pure Land tradition (Dragon Flower Ch'an Temples lineage). All welcome.",
    source_url: "https://cloudwater.org", event_url: "https://cloudwater.org",
  },
  {
    org_id: "cloudwater_zendo", org_name: "CloudWater Zendo",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 90,
    address: "4388 W Pleasant Valley Road", city: "Cleveland", state: "OH", neighborhood: "Parma",
    lat: 41.3738, lng: -81.7645, tradition: "zen", location_type: "in-person",
    notes: "Weekly Sunday morning group Zen meditation. Chan Buddhist and Pure Land tradition (Dragon Flower Ch'an Temples lineage). All welcome; no experience required.",
    source_url: "https://cloudwater.org", event_url: "https://cloudwater.org",
  },

  // ── Madison, WI — Phase 3 (heartbeat 52) ───────────────────────────────────

  // Kadampa Meditation Center Madison — 1825 S. Park St, Madison WI 53713
  // NKT Tibetan. meditationinmadison.org. No iCal (WordPress/MEC broken feed).
  {
    org_id: "kmc_madison", org_name: "Kadampa Meditation Center Madison",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 75,
    address: "1825 S. Park Street", city: "Madison", state: "WI", neighborhood: "South Madison",
    lat: 43.0568, lng: -89.4019, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Sunday morning guided meditation class combining Buddhist teachings with meditation practice. NKT-IKBU tradition. Drop-in; suggested $12.",
    source_url: "https://www.meditationinmadison.org", event_url: "https://www.meditationinmadison.org/ongoing-classes/",
  },
  {
    org_id: "kmc_madison", org_name: "Kadampa Meditation Center Madison",
    title: "Meditation at Noon",
    days: ["Wednesday"], time: { h: 12, m: 0 }, duration_min: 30,
    address: "1825 S. Park Street", city: "Madison", state: "WI", neighborhood: "South Madison",
    lat: 43.0568, lng: -89.4019, tradition: "tibetan", location_type: "in-person",
    notes: "Midday drop-in meditation session. In-person only; $5 suggested donation.",
    source_url: "https://www.meditationinmadison.org", event_url: "https://www.meditationinmadison.org/ongoing-classes/",
  },
  {
    org_id: "kmc_madison", org_name: "Kadampa Meditation Center Madison",
    title: "Buddhist Wisdom for Daily Life",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 60,
    address: "1825 S. Park Street", city: "Madison", state: "WI", neighborhood: "South Madison",
    lat: 43.0568, lng: -89.4019, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Thursday evening: guided meditation with Buddhist teachings. NKT-IKBU tradition. Drop-in; suggested $12.",
    source_url: "https://www.meditationinmadison.org", event_url: "https://www.meditationinmadison.org/ongoing-classes/",
  },

  // Madison Zen Center — 1820 Jefferson St, Madison WI 53711
  // Kapleau/Rochester lineage (Sensei Rick Smith). madisonzen.org. No iCal.
  {
    org_id: "madison_zen_center", org_name: "Madison Zen Center",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 8, m: 30 }, duration_min: 120,
    address: "1820 Jefferson Street", city: "Madison", state: "WI", neighborhood: "Regent / UW Campus Area",
    lat: 43.0617, lng: -89.3957, tradition: "zen", location_type: "in-person",
    notes: "Weekly Sunday program: zazen sitting, kinhin (walking meditation), chanting, and dharma talk. Kapleau/Rochester Zen lineage. Drop-in; all levels welcome.",
    source_url: "https://www.madisonzen.org", event_url: "https://www.madisonzen.org/about/schedule/",
  },
  {
    org_id: "madison_zen_center", org_name: "Madison Zen Center",
    title: "Monday Evening Zazen",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "1820 Jefferson Street", city: "Madison", state: "WI", neighborhood: "Regent / UW Campus Area",
    lat: 43.0617, lng: -89.3957, tradition: "zen", location_type: "in-person",
    notes: "Monday evening: three 25-minute rounds of zazen with kinhin and occasional private instruction. Drop-in welcome.",
    source_url: "https://www.madisonzen.org", event_url: "https://www.madisonzen.org/about/schedule/",
  },
  {
    org_id: "madison_zen_center", org_name: "Madison Zen Center",
    title: "Tuesday Morning Zazen",
    days: ["Tuesday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "1820 Jefferson Street", city: "Madison", state: "WI", neighborhood: "Regent / UW Campus Area",
    lat: 43.0617, lng: -89.3957, tradition: "zen", location_type: "in-person",
    notes: "Early morning zazen, one 60-minute round. Kapleau/Rochester lineage. Drop-in welcome.",
    source_url: "https://www.madisonzen.org", event_url: "https://www.madisonzen.org/about/schedule/",
  },
  {
    org_id: "madison_zen_center", org_name: "Madison Zen Center",
    title: "Wednesday Evening Zazen",
    days: ["Wednesday"], time: { h: 18, m: 30 }, duration_min: 120,
    address: "1820 Jefferson Street", city: "Madison", state: "WI", neighborhood: "Regent / UW Campus Area",
    lat: 43.0617, lng: -89.3957, tradition: "zen", location_type: "in-person",
    notes: "Wednesday evening: three 35-minute rounds of zazen with kinhin and chanting. Kapleau/Rochester lineage. Drop-in welcome.",
    source_url: "https://www.madisonzen.org", event_url: "https://www.madisonzen.org/about/schedule/",
  },
  {
    org_id: "madison_zen_center", org_name: "Madison Zen Center",
    title: "Thursday Morning Zazen",
    days: ["Thursday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "1820 Jefferson Street", city: "Madison", state: "WI", neighborhood: "Regent / UW Campus Area",
    lat: 43.0617, lng: -89.3957, tradition: "zen", location_type: "in-person",
    notes: "Early morning zazen, one 60-minute round. Kapleau/Rochester lineage. Drop-in welcome.",
    source_url: "https://www.madisonzen.org", event_url: "https://www.madisonzen.org/about/schedule/",
  },
  {
    org_id: "madison_zen_center", org_name: "Madison Zen Center",
    title: "Friday Morning Zazen",
    days: ["Friday"], time: { h: 6, m: 30 }, duration_min: 70,
    address: "1820 Jefferson Street", city: "Madison", state: "WI", neighborhood: "Regent / UW Campus Area",
    lat: 43.0617, lng: -89.3957, tradition: "zen", location_type: "in-person",
    notes: "Friday morning: zazen (one round) followed by chanting. Kapleau/Rochester lineage. Drop-in welcome.",
    source_url: "https://www.madisonzen.org", event_url: "https://www.madisonzen.org/about/schedule/",
  },

  // Snowflower Sangha — Friends Meetinghouse, 1704 Roberts Court, Madison WI 53711
  // Plum Village / Thich Nhat Hanh. snowflower.org. No iCal.
  {
    org_id: "snowflower_sangha", org_name: "Snowflower Sangha",
    title: "Tuesday Evening Sangha",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "1704 Roberts Court", city: "Madison", state: "WI", neighborhood: "Vilas / Friends Meetinghouse",
    lat: 43.0676, lng: -89.3780, tradition: "zen", location_type: "hybrid",
    notes: "Weekly Tuesday evening: sitting meditation, walking meditation, Dharma sharing, and chanting in the Plum Village / Thich Nhat Hanh tradition. In-person at Friends Meetinghouse + Zoom. Free; dana welcome.",
    source_url: "https://snowflower.org", event_url: "https://snowflower.org/whenandwhere/",
  },
  {
    org_id: "snowflower_sangha", org_name: "Snowflower Sangha",
    title: "Saturday Morning Sangha",
    days: ["Saturday"], time: { h: 10, m: 0 }, duration_min: 90,
    address: "1704 Roberts Court", city: "Madison", state: "WI", neighborhood: "Vilas / Friends Meetinghouse",
    lat: 43.0676, lng: -89.3780, tradition: "zen", location_type: "in-person",
    notes: "Weekly Saturday morning: sitting and walking meditation in the Plum Village tradition. In-person at Friends Meetinghouse. Free; dana welcome.",
    source_url: "https://snowflower.org", event_url: "https://snowflower.org/whenandwhere/",
  },

  // Diamond Way Buddhist Center Madison — 104 King St Suite 302, Madison WI 53703
  // Karma Kagyu / Ole Nydahl. diamondway.org/madison. No iCal.
  {
    org_id: "diamond_way_madison", org_name: "Diamond Way Buddhist Center Madison",
    title: "Sunday Evening Meditation",
    days: ["Sunday"], time: { h: 19, m: 30 }, duration_min: 60,
    address: "104 King Street, Suite 302", city: "Madison", state: "WI", neighborhood: "Downtown Madison",
    lat: 43.0740, lng: -89.3840, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Sunday evening: short talk followed by guided Diamond Way meditation. Karma Kagyu / Lama Ole Nydahl lineage. Free; no registration required.",
    source_url: "https://diamondway.org/madison/", event_url: "https://diamondway.org/madison/",
  },
  {
    org_id: "diamond_way_madison", org_name: "Diamond Way Buddhist Center Madison",
    title: "Wednesday Evening Meditation",
    days: ["Wednesday"], time: { h: 19, m: 30 }, duration_min: 60,
    address: "104 King Street, Suite 302", city: "Madison", state: "WI", neighborhood: "Downtown Madison",
    lat: 43.0740, lng: -89.3840, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Wednesday evening: short talk followed by guided Diamond Way meditation. Karma Kagyu / Lama Ole Nydahl lineage. Free; no registration required.",
    source_url: "https://diamondway.org/madison/", event_url: "https://diamondway.org/madison/",
  },

  // ============================================================
  // Connecticut — Hartford / New Haven Phase 3 (heartbeat 53)
  // ============================================================

  // New Haven Zen Center — Kwan Um School of Zen. newhavenzen.org
  {
    org_id: "new_haven_zen", org_name: "New Haven Zen Center",
    title: "Wednesday Evening Sitting",
    days: ["Wednesday"], time: { h: 19, m: 30 }, duration_min: 90,
    address: "193 Mansfield Street", city: "New Haven", state: "CT", neighborhood: "East Rock",
    lat: 41.3117, lng: -72.9278, tradition: "zen", location_type: "in-person",
    notes: "Weekly Wednesday evening zazen at the New Haven Zen Center (Kwan Um School of Zen). Schedule: 7pm chanting, 7:30pm sitting, walking, sitting. Newcomer orientation 2nd and 4th Wednesdays at 6:30pm. Drop-in welcome; free; dana appreciated.",
    source_url: "https://www.newhavenzen.org", event_url: "https://www.newhavenzen.org/schedule",
  },
  {
    org_id: "new_haven_zen", org_name: "New Haven Zen Center",
    title: "Sunday Morning Sitting",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 110,
    address: "193 Mansfield Street", city: "New Haven", state: "CT", neighborhood: "East Rock",
    lat: 41.3117, lng: -72.9278, tradition: "zen", location_type: "in-person",
    notes: "Weekly Sunday morning program at the New Haven Zen Center (Kwan Um School of Zen). Sitting, walking, and chanting (9am–~10:50am) with dharma talk. Drop-in welcome; free; dana appreciated.",
    source_url: "https://www.newhavenzen.org", event_url: "https://www.newhavenzen.org/schedule",
  },

  // Shambhala Meditation Center of New Haven — Tibetan/Shambhala. newhaven.shambhala.org
  {
    org_id: "shambhala_new_haven", org_name: "Shambhala Meditation Center of New Haven",
    title: "Sunday Morning Open Meditation",
    days: ["Sunday"], time: { h: 9, m: 30 }, duration_min: 120,
    address: "493 Whitney Avenue, 2nd Floor", city: "New Haven", state: "CT", neighborhood: "East Rock / Whitney Avenue",
    lat: 41.3238, lng: -72.9303, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Sunday open meditation at Shambhala Meditation Center of New Haven (9:30–11:30am). Alternating sitting and walking periods with instruction available; dharma talk on the first Sunday of each month. Located at East Rock Health & Wellness. Drop-in welcome; suggested donation.",
    source_url: "https://newhaven.shambhala.org", event_url: "https://newhaven.shambhala.org/programs/monthly-calendar/",
  },

  // Odiyana Kadampa Meditation Center (NKT) — Glastonbury CT. meditationinconnecticut.org
  {
    org_id: "odiyana_kadampa", org_name: "Odiyana Kadampa Meditation Center",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 75,
    address: "450 New London Turnpike", city: "Glastonbury", state: "CT", neighborhood: "Glastonbury (Hartford suburb)",
    lat: 41.7084, lng: -72.5950, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Sunday 'Meditation Made Easy' class at Odiyana Kadampa Meditation Center (NKT), Glastonbury CT (11am–12:15pm). Guided meditation with Buddhist philosophy in the Kadampa style. Open to all levels; drop-in welcome. Suggested $8–12; free for members.",
    source_url: "https://www.meditationinconnecticut.org", event_url: "https://www.meditationinconnecticut.org/calendar/",
  },
  {
    org_id: "odiyana_kadampa", org_name: "Odiyana Kadampa Meditation Center",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 75,
    address: "450 New London Turnpike", city: "Glastonbury", state: "CT", neighborhood: "Glastonbury (Hartford suburb)",
    lat: 41.7084, lng: -72.5950, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Thursday evening meditation class at Odiyana Kadampa Meditation Center (NKT), Glastonbury CT (7–8:15pm). Guided meditation with Buddhist philosophy. Open to all levels; drop-in welcome. Suggested $8–12; free for members.",
    source_url: "https://www.meditationinconnecticut.org", event_url: "https://www.meditationinconnecticut.org/calendar/",
  },

  // Nalandabodhi Connecticut — Tibetan Kagyu/Nyingma. ct.nalandabodhi.org
  {
    org_id: "nalandabodhi_ct", org_name: "Nalandabodhi Connecticut",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 50,
    address: "3 Barnard Lane, Suite 305", city: "Bloomfield", state: "CT", neighborhood: "Bloomfield (Hartford suburb)",
    lat: 41.8438, lng: -72.7197, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Sunday morning meditation at Nalandabodhi Connecticut (10–10:50am), followed by dharma discussion (11–11:30am). Kagyu/Nyingma lineage of Dzogchen Ponlop Rinpoche. Hybrid in-person (Bloomfield) and Zoom. Free; open to all.",
    source_url: "https://ct.nalandabodhi.org", event_url: "https://ct.nalandabodhi.org/events/",
  },

  // Hartford Karma Thegsum Choling — Tibetan Karma Kagyu. ktchartford.org
  {
    org_id: "hartford_ktc", org_name: "Hartford Karma Thegsum Choling",
    title: "Tuesday Evening Practice",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "157 Elizabeth Street", city: "Hartford", state: "CT", neighborhood: "West End, Hartford",
    lat: 41.7627, lng: -72.6990, tradition: "tibetan", location_type: "in-person",
    notes: "Weekly Tuesday evening practice and study group at Hartford Karma Thegsum Choling (KTC), affiliated with Karma Triyana Dharmachakra (KTD Monastery), Woodstock NY — Karma Kagyu lineage of the Gyalwang Karmapa. Open to all; call (860) 232-8366 to confirm current schedule.",
    source_url: "https://ktchartford.org", event_url: "https://ktchartford.org",
  },

  // ============================================================
  // Omaha / Lincoln, NE Phase 3 (heartbeat 54)
  // ============================================================

  // Nebraska Zen Center / Heartland Temple — Soto Zen. nebraskazencenter.org
  {
    org_id: "nebraska_zen_center", org_name: "Nebraska Zen Center / Heartland Temple",
    title: "Sunday Open Zen",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "3625 Lafayette Avenue", city: "Omaha", state: "NE", neighborhood: "Bemis Park / Midtown Omaha",
    lat: 41.2613, lng: -96.0013, tradition: "zen", location_type: "in-person",
    notes: "Weekly Sunday Open Zen at Nebraska Zen Center (10am–noon): zazen, kinhin, dharma talk, and tea. Newcomers arrive 9:15am for orientation. Founded 1975 in the lineage of Dainin Katagiri Roshi; one of the oldest Zen centers in the Midwest. Drop-in welcome; by donation.",
    source_url: "https://nebraskazencenter.org", event_url: "https://nebraskazencenter.org/programs/sunday-open-zen/",
  },
  {
    org_id: "nebraska_zen_center", org_name: "Nebraska Zen Center / Heartland Temple",
    title: "Wednesday Evening Zazen",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 75,
    address: "3625 Lafayette Avenue", city: "Omaha", state: "NE", neighborhood: "Bemis Park / Midtown Omaha",
    lat: 41.2613, lng: -96.0013, tradition: "zen", location_type: "in-person",
    notes: "Weekly Wednesday evening zazen at Nebraska Zen Center (7pm): two 30-minute zazen periods with kinhin, Fukanzazengi recitation, and dharma discussion. Drop-in welcome; by donation.",
    source_url: "https://nebraskazencenter.org", event_url: "https://nebraskazencenter.org/schedule/",
  },
  {
    org_id: "nebraska_zen_center", org_name: "Nebraska Zen Center / Heartland Temple",
    title: "Morning Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], time: { h: 6, m: 0 }, duration_min: 90,
    address: "3625 Lafayette Avenue", city: "Omaha", state: "NE", neighborhood: "Bemis Park / Midtown Omaha",
    lat: 41.2613, lng: -96.0013, tradition: "zen", location_type: "hybrid",
    notes: "Weekday morning zazen at Nebraska Zen Center (6–7:30am), in-person and Zoom. Open to all practitioners; no experience required. By donation.",
    source_url: "https://nebraskazencenter.org", event_url: "https://nebraskazencenter.org/schedule/",
  },

  // Flatwater Collective — Pluralist / non-sectarian Buddhist. flatwatercollective.org
  {
    org_id: "flatwater_collective", org_name: "Flatwater Collective",
    title: "Meditation Practice and Reflection",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "1219 Leavenworth Street", city: "Omaha", state: "NE", neighborhood: "Downtown Omaha",
    lat: 41.2571, lng: -95.9350, tradition: "pluralist", location_type: "in-person",
    notes: "Weekly Thursday evening program at Flatwater Collective (7–8pm): dharma talk and sitting meditation. Beginner-friendly, freely offered. Non-sectarian Buddhist community in downtown Omaha. Drop-in welcome; dana appreciated.",
    source_url: "https://www.flatwatercollective.org", event_url: "https://www.flatwatercollective.org/calendar",
  },
  {
    org_id: "flatwater_collective", org_name: "Flatwater Collective",
    title: "Sunday Practice",
    days: ["Sunday"], time: { h: 16, m: 0 }, duration_min: 60,
    address: "1219 Leavenworth Street", city: "Omaha", state: "NE", neighborhood: "Downtown Omaha",
    lat: 41.2571, lng: -95.9350, tradition: "pluralist", location_type: "in-person",
    notes: "Weekly Sunday Practice at Flatwater Collective (4–5pm): guided and silent meditation with a different teacher each week. Non-sectarian Buddhist community. Drop-in welcome; dana appreciated.",
    source_url: "https://www.flatwatercollective.org", event_url: "https://www.flatwatercollective.org/calendar",
  },

  // Honey Locust Sangha — Plum Village / Thich Nhat Hanh. honeylocustsangha.org
  {
    org_id: "honey_locust_sangha", org_name: "Honey Locust Sangha",
    title: "Monday Evening Sitting",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 120,
    address: "7641 Pacific Street", city: "Omaha", state: "NE", neighborhood: "Midtown / Pacific Street",
    lat: 41.2376, lng: -96.0484, tradition: "pluralist", location_type: "in-person",
    notes: "Weekly Monday evening at Honey Locust Sangha (6:30–8:30pm) at The Yoga Path: sitting meditation, walking meditation, and dharma discussion in the Plum Village tradition of Thich Nhat Hanh. Zoom also available. Free; open to all.",
    source_url: "https://honeylocustsangha.org", event_url: "https://honeylocustsangha.org",
  },
  {
    org_id: "honey_locust_sangha", org_name: "Honey Locust Sangha",
    title: "Friday Evening Sitting",
    days: ["Friday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "7641 Pacific Street", city: "Omaha", state: "NE", neighborhood: "Midtown / Pacific Street",
    lat: 41.2376, lng: -96.0484, tradition: "pluralist", location_type: "in-person",
    notes: "Weekly Friday evening at Honey Locust Sangha (6–7pm) at The Yoga Path: sitting and walking meditation in noble silence. Plum Village tradition of Thich Nhat Hanh. Zoom also available. Free; open to all.",
    source_url: "https://honeylocustsangha.org", event_url: "https://honeylocustsangha.org",
  },

  // Lincoln Zen Center — Soto Zen. lincolnzencenter.org
  {
    org_id: "lincoln_zen_center", org_name: "Lincoln Zen Center",
    title: "Sunday Morning Sitting",
    days: ["Sunday"], time: { h: 10, m: 30 }, duration_min: 90,
    address: "3701 O Street, Suite 204", city: "Lincoln", state: "NE", neighborhood: "Near South Lincoln",
    lat: 40.8057, lng: -96.6720, tradition: "zen", location_type: "in-person",
    notes: "Weekly Sunday morning program at Lincoln Zen Center (10:30am–noon): sitting meditation followed by dharma talk and discussion. Soto Zen. Drop-in welcome; no experience required.",
    source_url: "https://www.lincolnzencenter.org", event_url: "https://www.lincolnzencenter.org/calendar",
  },
  {
    org_id: "lincoln_zen_center", org_name: "Lincoln Zen Center",
    title: "Monday Evening Sitting",
    days: ["Monday"], time: { h: 17, m: 30 }, duration_min: 75,
    address: "3701 O Street, Suite 204", city: "Lincoln", state: "NE", neighborhood: "Near South Lincoln",
    lat: 40.8057, lng: -96.6720, tradition: "zen", location_type: "in-person",
    notes: "Weekly Monday evening sitting at Lincoln Zen Center (5:30–6:45pm). Beginner instruction available. Soto Zen. Drop-in welcome; no experience required.",
    source_url: "https://www.lincolnzencenter.org", event_url: "https://www.lincolnzencenter.org/calendar",
  },
  {
    org_id: "lincoln_zen_center", org_name: "Lincoln Zen Center",
    title: "Wednesday Morning Sitting",
    days: ["Wednesday"], time: { h: 10, m: 30 }, duration_min: 75,
    address: "3701 O Street, Suite 204", city: "Lincoln", state: "NE", neighborhood: "Near South Lincoln",
    lat: 40.8057, lng: -96.6720, tradition: "zen", location_type: "in-person",
    notes: "Weekly Wednesday morning sitting at Lincoln Zen Center (10:30–11:45am). Soto Zen. Drop-in welcome; no experience required.",
    source_url: "https://www.lincolnzencenter.org", event_url: "https://www.lincolnzencenter.org/calendar",
  },

  // ============================================================
  // Boise, ID — Phase 3 (heartbeat 55)
  // ============================================================

  // Boise Zen Center — Soto Zen (SZBA). boisezencenter.org
  {
    org_id: "boise_zen_center", org_name: "Boise Zen Center",
    title: "Wednesday Morning Zazen",
    days: ["Wednesday"], time: { h: 7, m: 0 }, duration_min: 90,
    address: "1524 W. Hays Street, Suite 101a", city: "Boise", state: "ID", neighborhood: "Downtown Boise",
    lat: 43.6194, lng: -116.2052, tradition: "zen", location_type: "hybrid",
    notes: "Weekly Wednesday morning zazen at Boise Zen Center (7–8:30am): zazen and kinhin, in-person and Zoom. Soto Zen (SZBA member), teacher Jisen Coghlan. Drop-in welcome; donation-based.",
    source_url: "https://www.boisezencenter.org", event_url: "https://www.boisezencenter.org/schedule.html",
  },
  {
    org_id: "boise_zen_center", org_name: "Boise Zen Center",
    title: "Thursday Evening Zazen",
    days: ["Thursday"], time: { h: 18, m: 0 }, duration_min: 70,
    address: "1524 W. Hays Street, Suite 101a", city: "Boise", state: "ID", neighborhood: "Downtown Boise",
    lat: 43.6194, lng: -116.2052, tradition: "zen", location_type: "in-person",
    notes: "Weekly Thursday evening zazen at Boise Zen Center (6–7:10pm): two sitting periods with kinhin, in-person. Soto Zen. Drop-in welcome; donation-based.",
    source_url: "https://www.boisezencenter.org", event_url: "https://www.boisezencenter.org/schedule.html",
  },
  {
    org_id: "boise_zen_center", org_name: "Boise Zen Center",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 8, m: 0 }, duration_min: 90,
    address: "1524 W. Hays Street, Suite 101a", city: "Boise", state: "ID", neighborhood: "Downtown Boise",
    lat: 43.6194, lng: -116.2052, tradition: "zen", location_type: "hybrid",
    notes: "Weekly Saturday morning zazen at Boise Zen Center (8–9:30am): zazen and kinhin, in-person and Zoom. First Saturday monthly includes Introduction to Meditation. Soto Zen. Drop-in welcome; donation-based.",
    source_url: "https://www.boisezencenter.org", event_url: "https://www.boisezencenter.org/schedule.html",
  },

  // Empty Gate Zen Center Boise — Kwan Um School of Zen. bibscenter.org
  {
    org_id: "empty_gate_zen_boise", org_name: "Empty Gate Zen Center Boise",
    title: "Morning Sitting",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "901 N. 15th Street", city: "Boise", state: "ID", neighborhood: "North End Boise",
    lat: 43.6218, lng: -116.2118, tradition: "zen", location_type: "hybrid",
    notes: "Weekday morning sitting at Empty Gate Zen Center Boise (6:30–7:30am) at BIBS: sitting and kinhin, in-person and Zoom. Kwan Um School of Zen (Korean Zen), teacher Jeff Kitzes (Zen Master Bon Soeng). Drop-in welcome.",
    source_url: "https://bibscenter.org", event_url: "https://bibscenter.org/class-calendar/",
  },
  {
    org_id: "empty_gate_zen_boise", org_name: "Empty Gate Zen Center Boise",
    title: "Thursday Evening Sitting",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "901 N. 15th Street", city: "Boise", state: "ID", neighborhood: "North End Boise",
    lat: 43.6218, lng: -116.2118, tradition: "zen", location_type: "hybrid",
    notes: "Weekly Thursday evening sitting at Empty Gate Zen Center Boise (7pm) at BIBS, in-person and Zoom. Kwan Um School of Zen. Drop-in welcome.",
    source_url: "https://bibscenter.org", event_url: "https://bibscenter.org/class-calendar/",
  },

  // Boise Insight Sangha — Insight Meditation. boiseinsightsangha.wordpress.com
  {
    org_id: "boise_insight_sangha", org_name: "Boise Insight Sangha",
    title: "Tuesday Evening Sitting",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "901 N. 15th Street", city: "Boise", state: "ID", neighborhood: "North End Boise",
    lat: 43.6218, lng: -116.2118, tradition: "theravada", location_type: "in-person",
    notes: "Weekly Tuesday evening at Boise Insight Sangha (6–7:30pm) at BIBS: sitting meditation and dharma discussion. Insight Meditation tradition. Drop-in welcome; open to all levels.",
    source_url: "https://boiseinsightsangha.wordpress.com", event_url: "https://boiseinsightsangha.wordpress.com",
  },

  // Beginner's Mind Sangha — Plum Village / Thich Nhat Hanh. beginnersmindsangha.org
  {
    org_id: "beginners_mind_sangha_boise", org_name: "Beginner's Mind Sangha",
    title: "Wednesday Evening Practice",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 75,
    address: "901 N. 15th Street", city: "Boise", state: "ID", neighborhood: "North End Boise",
    lat: 43.6218, lng: -116.2118, tradition: "pluralist", location_type: "in-person",
    notes: "Weekly Wednesday evening at Beginner's Mind Sangha (7–8:15pm) at BIBS: sitting meditation, walking meditation, and dharma sharing. Plum Village tradition (Order of Interbeing, Thich Nhat Hanh lineage). Free; open to all.",
    source_url: "https://www.beginnersmindsangha.org", event_url: "https://www.beginnersmindsangha.org",
  },
  {
    org_id: "beginners_mind_sangha_boise", org_name: "Beginner's Mind Sangha",
    title: "Sunday Morning Sangha",
    days: ["Sunday"], time: { h: 10, m: 15 }, duration_min: 90,
    address: "901 N. 15th Street", city: "Boise", state: "ID", neighborhood: "North End Boise",
    lat: 43.6218, lng: -116.2118, tradition: "pluralist", location_type: "hybrid",
    notes: "Weekly Sunday morning at Beginner's Mind Sangha (10:15–11:45am) at BIBS: sitting meditation and dharma discussion, in-person and Zoom. Third Sunday includes Three Jewels ceremony; fifth Sunday is a Day of Mindfulness. Plum Village tradition. Free; open to all.",
    source_url: "https://www.beginnersmindsangha.org", event_url: "https://www.beginnersmindsangha.org",
  },

  // Heart of the Dharma — Nyingma Tibetan Buddhism. heartofdharma.org
  {
    org_id: "heart_of_the_dharma_boise", org_name: "Heart of the Dharma",
    title: "Sunday Practice",
    days: ["Sunday"], time: { h: 11, m: 0 }, duration_min: 75,
    address: "1627 S. Orchard Street, Suite 200", city: "Boise", state: "ID", neighborhood: "South Boise",
    lat: 43.5935, lng: -116.2210, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly Sunday practice at Heart of the Dharma (11am–12:15pm): in-person and livestream. Nyingma Tibetan Buddhism, teacher Dana Marsh (ordained by Anam Thubten Rinpoche). Dana-based; open to all.",
    source_url: "https://heartofdharma.org", event_url: "https://heartofdharma.org/calendar",
  },
  {
    org_id: "heart_of_the_dharma_boise", org_name: "Heart of the Dharma",
    title: "Tuesday Evening Practice",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "1627 S. Orchard Street, Suite 200", city: "Boise", state: "ID", neighborhood: "South Boise",
    lat: 43.5935, lng: -116.2210, tradition: "tibetan", location_type: "online",
    notes: "Weekly Tuesday evening practice at Heart of the Dharma (7pm): online/livestream only. Nyingma Tibetan Buddhism. Dana-based; open to all.",
    source_url: "https://heartofdharma.org", event_url: "https://heartofdharma.org/calendar",
  },

  // ============================================================
  // Spokane, WA — Phase 3 (heartbeat 56)
  // ============================================================
  // Note: Zen Center of Spokane has a live iCal feed — events seeded via abraxis_ingest.py
  // Recurring sits seeded here: Buddhist Institute of Universal Compassion (BIUC)

  // Buddhist Institute of Universal Compassion — Gelug Tibetan. universalcompassion.org
  {
    org_id: "biuc_spokane", org_name: "Buddhist Institute of Universal Compassion",
    title: "Saturday Morning Meditation and Teachings",
    days: ["Saturday"], time: { h: 9, m: 30 }, duration_min: 150,
    address: "728 E Rich Ave", city: "Spokane", state: "WA", neighborhood: "East Spokane",
    lat: 47.6608, lng: -117.3812, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly Saturday morning at Buddhist Institute of Universal Compassion (9:30am–12pm): meditation and teachings. Gelug Tibetan Buddhism, led by Venerable Geshe Thupten Phelgye. In-person at 728 E Rich Ave + Zoom (ID: 890 7744 2439). Open to all; dana-based.",
    source_url: "https://www.universalcompassion.org", event_url: "https://www.universalcompassion.org/schedule",
  },
  {
    org_id: "biuc_spokane", org_name: "Buddhist Institute of Universal Compassion",
    title: "Sunday Morning Meditation and Teachings",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "728 E Rich Ave", city: "Spokane", state: "WA", neighborhood: "East Spokane",
    lat: 47.6608, lng: -117.3812, tradition: "tibetan", location_type: "hybrid",
    notes: "Weekly Sunday morning at Buddhist Institute of Universal Compassion (10am–12pm): meditation and teachings. Gelug Tibetan Buddhism, led by Venerable Geshe Thupten Phelgye. In-person at 728 E Rich Ave + Zoom (ID: 890 7744 2439). Open to all; dana-based.",
    source_url: "https://www.universalcompassion.org", event_url: "https://www.universalcompassion.org/schedule",
  },

  // ============================================================
  // Fresno, CA — Phase 3 (heartbeat 57)
  // ============================================================

  // Zen Center of Fresno — Soto Zen (Central Valley Zen Foundation). zenfresno.org
  {
    org_id: "zen_center_fresno", org_name: "Zen Center of Fresno",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 9, m: 0 }, duration_min: 120,
    address: "371 E. Bullard Ave., Suite 102", city: "Fresno", state: "CA", neighborhood: "Central Fresno",
    lat: 36.8240, lng: -119.7965, tradition: "zen", location_type: "in_person",
    notes: "Weekly Saturday morning at Zen Center of Fresno (9am–11am): two 25-min zazen periods with kinhin (walking meditation), dharma talk at 10am, and closing vows. Soto Zen (Central Valley Zen Foundation). Drop-in welcome; free.",
    source_url: "https://zenfresno.org", event_url: "https://zenfresno.org/schedule",
  },

  // Fresno Buddhist Temple — Jodo Shinshu (BCA). fresnobuddhisttemple.org
  {
    org_id: "fresno_buddhist_temple", org_name: "Fresno Buddhist Temple",
    title: "Sunday Meditation Class",
    days: ["Sunday"], time: { h: 8, m: 30 }, duration_min: 45,
    address: "2690 E. Alluvial Ave.", city: "Fresno", state: "CA", neighborhood: "Northeast Fresno",
    lat: 36.8776, lng: -119.7590, tradition: "other", location_type: "in_person",
    notes: "Weekly Sunday Meditation Class at Fresno Buddhist Temple (8:30–9:15am): sitting and walking meditation in the Hondo. Jodo Shinshu / Buddhist Churches of America. Open to all; donations welcome.",
    source_url: "https://fresnobuddhisttemple.org", event_url: "https://fresnobuddhisttemple.org/buddhist-retreat-sundays-mindful-meditation-dharma-discussion/",
  },
  {
    org_id: "fresno_buddhist_temple", org_name: "Fresno Buddhist Temple",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 45,
    address: "2690 E. Alluvial Ave.", city: "Fresno", state: "CA", neighborhood: "Northeast Fresno",
    lat: 36.8776, lng: -119.7590, tradition: "other", location_type: "hybrid",
    notes: "Weekly Thursday Evening Meditation with Rev. Kaz at Fresno Buddhist Temple (7–7:45pm): hybrid in-person + Zoom. Email the temple for the Zoom link. Jodo Shinshu / Buddhist Churches of America. Free; donations welcome.",
    source_url: "https://fresnobuddhisttemple.org", event_url: "https://fresnobuddhisttemple.org",
  },

  // Asheville, NC — Phase 3 (heartbeat 58)
  // -------------------------------------------------------------------------

  // Zen Center of Asheville — Soto Zen. zcasheville.org
  // Morning zazen: Mon/Wed/Fri 6–6:50am
  {
    org_id: "zen_center_asheville", org_name: "Zen Center of Asheville",
    title: "Morning Zazen",
    days: ["Monday", "Wednesday", "Friday"], time: { h: 6, m: 0 }, duration_min: 50,
    address: "227 Edgewood Rd", city: "Asheville", state: "NC", neighborhood: "North Asheville",
    lat: 35.6182, lng: -82.5564, tradition: "zen", location_type: "in_person",
    notes: "Monday/Wednesday/Friday morning zazen at Zen Center of Asheville (6–6:50am): 40 minutes of seated meditation. Soto Zen. Drop-in welcome; free (dana accepted).",
    source_url: "https://zcasheville.org", event_url: "https://zcasheville.org/schedule.htm",
  },
  // Saturday extended morning
  {
    org_id: "zen_center_asheville", org_name: "Zen Center of Asheville",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 6, m: 0 }, duration_min: 100,
    address: "227 Edgewood Rd", city: "Asheville", state: "NC", neighborhood: "North Asheville",
    lat: 35.6182, lng: -82.5564, tradition: "zen", location_type: "in_person",
    notes: "Saturday extended zazen at Zen Center of Asheville (6–7:40am): two 40-min zazen periods with kinhin (walking meditation) and closing Heart Sutra chant. Soto Zen. Drop-in welcome; free.",
    source_url: "https://zcasheville.org", event_url: "https://zcasheville.org/schedule.htm",
  },
  // Tuesday evening zazen + talk
  {
    org_id: "zen_center_asheville", org_name: "Zen Center of Asheville",
    title: "Evening Zazen & Dharma Talk",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "227 Edgewood Rd", city: "Asheville", state: "NC", neighborhood: "North Asheville",
    lat: 35.6182, lng: -82.5564, tradition: "zen", location_type: "in_person",
    notes: "Tuesday evening at Zen Center of Asheville (7–8:30pm): 30-min zazen, then 7:30–8:30pm dharma talk and discussion. Dana $10 requested. See dharma-study page for current speaker schedule.",
    source_url: "https://zcasheville.org", event_url: "https://zcasheville.org/schedule.htm",
  },

  // Mountain Mindfulness Sangha of Asheville — Plum Village / TNH. mountainmindfulness.org
  {
    org_id: "mountain_mindfulness_asheville", org_name: "Mountain Mindfulness Sangha of Asheville",
    title: "Thursday Evening Sangha",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "227 Edgewood Road", city: "Asheville", state: "NC", neighborhood: "North Asheville",
    lat: 35.6182, lng: -82.5564, tradition: "other", location_type: "in_person",
    notes: "Weekly Thursday evening at Mountain Mindfulness Sangha (7–8:30pm) at Asheville Friends Meeting, 227 Edgewood Rd. Four rotating formats: 1st Thu: Heart Sutra chanting; 2nd Thu: Plum Village book reading; 3rd Thu: silent sitting and walking; 4th Thu: Five Mindfulness Trainings recitation. Plum Village / Thich Nhat Hanh tradition. Drop-in; free.",
    source_url: "https://www.mountainmindfulness.org", event_url: "https://www.mountainmindfulness.org/weekly-meditation-schedule.html",
  },

  // Asheville Insight Meditation — Vipassana/Theravada. ashevillemeditation.com
  {
    org_id: "asheville_insight_meditation", org_name: "Asheville Insight Meditation",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "85 Weaverville Road, Unit 5", city: "Woodfin", state: "NC", neighborhood: "Woodfin (North Asheville metro)",
    lat: 35.6481, lng: -82.5802, tradition: "theravada", location_type: "hybrid",
    notes: "Thursday Evening Meditation at Asheville Insight Meditation (7–8:30pm): 30-min guided meditation, 30-min dharma talk, 30-min Q&A/discussion. In-person at 85 Weaverville Road, Unit 5, Woodfin, plus Zoom. Vipassana / Insight tradition. Drop-in; free.",
    source_url: "https://www.ashevillemeditation.com", event_url: "https://www.ashevillemeditation.com/weekly-schedule/",
  },

  // Anattasati Magga — Soto Zen lay sangha. anattasatimagga.org
  {
    org_id: "anattasati_magga", org_name: "Anattasati Magga",
    title: "Sunday Morning Service",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "32 Mineral Dust Drive", city: "Asheville", state: "NC", neighborhood: "West Asheville",
    lat: 35.5668, lng: -82.6224, tradition: "zen", location_type: "hybrid",
    notes: "Sunday morning at Anattasati Magga (10am–12pm): 30-min sitting meditation, chants and recitations, and a dharma class. In-person at 32 Mineral Dust Drive (7 quiet acres, West Asheville) or Zoom. Soto Zen lay sangha. 2nd Sunday includes new-student orientation. Free; donations welcome.",
    source_url: "https://anattasatimagga.org", event_url: "https://anattasatimagga.org/practice/meditation/",
  },

  // Burlington Buddhist Sangha — Insight/Theravada. burlingtonbuddhist.org
  // 1st, 2nd, 3rd Sundays in-person; 4th Sunday Zoom-only (not seeded)
  {
    org_id: "burlington_buddhist_sangha", org_name: "Burlington Buddhist Sangha",
    title: "Sunday Sit & Dharma Talk",
    days: ["Sunday"], week_of_month: 1, time: { h: 9, m: 30 }, duration_min: 120,
    address: "187 S Winooski Ave", city: "Burlington", state: "VT", neighborhood: "Downtown Burlington",
    lat: 44.4710, lng: -73.2135, tradition: "theravada", location_type: "in-person",
    notes: "Burlington Buddhist Sangha 1st Sunday (9:30–11:30am): sitting meditation, dharma talk, and discussion at the Burlington Shambhala Center (187 S Winooski Ave). Peer-led Insight Meditation community. Drop-in for experienced practitioners; dana-based, free.",
    source_url: "https://burlingtonbuddhist.org", event_url: "https://burlingtonbuddhist.org",
  },
  {
    org_id: "burlington_buddhist_sangha", org_name: "Burlington Buddhist Sangha",
    title: "Sunday Sit & Dharma Talk",
    days: ["Sunday"], week_of_month: 2, time: { h: 9, m: 30 }, duration_min: 120,
    address: "187 S Winooski Ave", city: "Burlington", state: "VT", neighborhood: "Downtown Burlington",
    lat: 44.4710, lng: -73.2135, tradition: "theravada", location_type: "in-person",
    notes: "Burlington Buddhist Sangha 2nd Sunday (9:30–11:30am): sitting meditation, dharma talk, and discussion at the Burlington Shambhala Center (187 S Winooski Ave). Peer-led Insight Meditation community. Drop-in for experienced practitioners; dana-based, free.",
    source_url: "https://burlingtonbuddhist.org", event_url: "https://burlingtonbuddhist.org",
  },
  {
    org_id: "burlington_buddhist_sangha", org_name: "Burlington Buddhist Sangha",
    title: "Sunday Sit & Dharma Talk",
    days: ["Sunday"], week_of_month: 3, time: { h: 9, m: 30 }, duration_min: 120,
    address: "187 S Winooski Ave", city: "Burlington", state: "VT", neighborhood: "Downtown Burlington",
    lat: 44.4710, lng: -73.2135, tradition: "theravada", location_type: "in-person",
    notes: "Burlington Buddhist Sangha 3rd Sunday (9:30–11:30am): sitting meditation, dharma talk, and discussion at the Burlington Shambhala Center (187 S Winooski Ave). Peer-led Insight Meditation community. Drop-in for experienced practitioners; dana-based, free.",
    source_url: "https://burlingtonbuddhist.org", event_url: "https://burlingtonbuddhist.org",
  },

  // Burlington Dharma Collective — Vajrayana (Lama Rod Owens / Bhumisparsha). burlingtondharmacollective.com
  {
    org_id: "burlington_dharma_collective", org_name: "Burlington Dharma Collective",
    title: "Weekly Meditation",
    days: ["Friday"], time: { h: 8, m: 0 }, duration_min: 45,
    address: "241 N Winooski Ave", city: "Burlington", state: "VT", neighborhood: "Old North End Burlington",
    lat: 44.4777, lng: -73.2126, tradition: "tibetan", location_type: "in-person",
    notes: "Burlington Dharma Collective weekly meditation (Friday 8–8:45am) at Outright VT (241 N Winooski Ave, side door from driveway). Vajrayana community led by Zac Ispa-Landa (student of Lama Rod Owens, Bhumisparsha lineage). Fully open drop-in; donations welcome.",
    source_url: "https://www.burlingtondharmacollective.com", event_url: "https://www.burlingtondharmacollective.com",
  },
  {
    org_id: "burlington_dharma_collective", org_name: "Burlington Dharma Collective",
    title: "Monday Night Dharma",
    days: ["Monday"], week_of_month: 2, time: { h: 19, m: 0 }, duration_min: 90,
    address: "241 N Winooski Ave", city: "Burlington", state: "VT", neighborhood: "Old North End Burlington",
    lat: 44.4777, lng: -73.2126, tradition: "tibetan", location_type: "in-person",
    notes: "Burlington Dharma Collective Monday Night Dharma (2nd Monday monthly, 7–8:30pm) at Outright VT (241 N Winooski Ave). Vajrayana dharma discussion and practice. Led by Zac Ispa-Landa (Bhumisparsha / Lama Rod Owens lineage). Open to all; donations welcome.",
    source_url: "https://www.burlingtondharmacollective.com", event_url: "https://www.burlingtondharmacollective.com",
  },

  // -------------------------------------------------------------------------
  // Eugene, OR — Phase 3 (heartbeat 60)
  // -------------------------------------------------------------------------

  // Buddha Eye Temple — Soto Zen (Japanese). buddhaeye.org
  // Sunday public program: Intro to Meditation 8:45am, Zazen 9am, Assembly 10am
  {
    org_id: "buddha_eye_temple", org_name: "Buddha Eye Temple",
    title: "Sunday Morning Program",
    days: ["Sunday"], time: { h: 8, m: 45 }, duration_min: 105,
    address: "2190 Garfield St", city: "Eugene", state: "OR", neighborhood: "South Eugene",
    lat: 44.0268, lng: -123.0978, tradition: "zen", location_type: "in-person",
    notes: "Buddha Eye Temple Sunday Morning Program (8:45am–~10:30am): Introduction to Meditation 8:45–9:50am (open to all levels), Zazen 9:00am, Assembly/ceremony 10:00am. Soto Zen (registered Soto Zen School). Drop-in welcome; no registration needed.",
    source_url: "https://www.buddhaeye.org", event_url: "https://www.buddhaeye.org/schedule/",
  },

  // Blue Cliff Zen Center — Western Zen (Soto/Rinzai). bluecliffzen.org
  // Tuesday 7–8am in-person + online
  {
    org_id: "blue_cliff_zen_eugene", org_name: "Blue Cliff Zen Center",
    title: "Morning Zazen",
    days: ["Tuesday"], time: { h: 7, m: 0 }, duration_min: 60,
    address: "352 W 12th Ave", city: "Eugene", state: "OR", neighborhood: "West University / Downtown Eugene",
    lat: 44.0477, lng: -123.0888, tradition: "zen", location_type: "hybrid",
    notes: "Blue Cliff Zen Center Tuesday morning zazen (7–8am) at Everyday People Yoga studio (352 W 12th Ave). In-person + online hybrid. Teacher: Matt Shinkai Kane. Drop-in welcome; dana-based.",
    source_url: "https://www.bluecliffzen.org", event_url: "https://www.bluecliffzen.org",
  },
  // Thursday 7–8am in-person + online
  {
    org_id: "blue_cliff_zen_eugene", org_name: "Blue Cliff Zen Center",
    title: "Morning Zazen",
    days: ["Thursday"], time: { h: 7, m: 0 }, duration_min: 60,
    address: "352 W 12th Ave", city: "Eugene", state: "OR", neighborhood: "West University / Downtown Eugene",
    lat: 44.0477, lng: -123.0888, tradition: "zen", location_type: "hybrid",
    notes: "Blue Cliff Zen Center Thursday morning zazen (7–8am) at Everyday People Yoga studio (352 W 12th Ave). In-person + online hybrid. Teacher: Matt Shinkai Kane. Drop-in welcome; dana-based.",
    source_url: "https://www.bluecliffzen.org", event_url: "https://www.bluecliffzen.org",
  },
  // Sunday 4:30–6pm in-person + online
  {
    org_id: "blue_cliff_zen_eugene", org_name: "Blue Cliff Zen Center",
    title: "Sunday Evening Sitting",
    days: ["Sunday"], time: { h: 16, m: 30 }, duration_min: 90,
    address: "352 W 12th Ave", city: "Eugene", state: "OR", neighborhood: "West University / Downtown Eugene",
    lat: 44.0477, lng: -123.0888, tradition: "zen", location_type: "hybrid",
    notes: "Blue Cliff Zen Center Sunday evening sitting (4:30–6pm) at Everyday People Yoga studio (352 W 12th Ave). Zazen + dharma discussion. In-person + online hybrid. Teacher: Matt Shinkai Kane. Drop-in welcome; dana-based.",
    source_url: "https://www.bluecliffzen.org", event_url: "https://www.bluecliffzen.org",
  },

  // Zen West Eugene — Soto Zen (Dharma Rain affiliate). zenwesteugene.org
  // Thursday evening 7–8:45pm at UUCE
  {
    org_id: "zen_west_eugene", org_name: "Zen West Eugene",
    title: "Thursday Evening Zazen",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 105,
    address: "1685 W 13th Ave", city: "Eugene", state: "OR", neighborhood: "Jefferson Westside / West Eugene",
    lat: 44.0456, lng: -123.1172, tradition: "zen", location_type: "in-person",
    notes: "Zen West Eugene Thursday evening program (7:00–8:45pm) at UUCE (1685 W 13th Ave). Zazen, kinhin (walking meditation), zazen, chanting/recitation, dharma talk/discussion. Soto Zen; Dharma Rain affiliate, led by Debra Seido Martin. Drop-in welcome.",
    source_url: "https://www.zenwesteugene.org", event_url: "https://www.zenwesteugene.org/calendar",
  },

  // River Wisdom Insight Meditation Community — Theravada/Insight. riverwisdominsight.com
  // 1st Saturday 10:30am–12pm at UUCE
  {
    org_id: "river_wisdom_insight", org_name: "River Wisdom Insight Meditation Community",
    title: "Insight Meditation Sit & Dharma Talk",
    days: ["Saturday"], week_of_month: 1, time: { h: 10, m: 30 }, duration_min: 90,
    address: "1685 W 13th Ave", city: "Eugene", state: "OR", neighborhood: "Jefferson Westside / West Eugene",
    lat: 44.0456, lng: -123.1172, tradition: "theravada", location_type: "in-person",
    notes: "River Wisdom Insight Meditation Community 1st Saturday (10:30am–12pm) at UUCE (1685 W 13th Ave). Sitting meditation, dharma talk, and discussion. Led by Linda Rose (Spirit Rock / Howie Cohn lineage). Drop-in welcome; dana-based.",
    source_url: "https://riverwisdominsight.com", event_url: "https://riverwisdominsight.com/programs/",
  },
  // 3rd Saturday 10:30–11:30am at Buddha Eye Temple
  {
    org_id: "river_wisdom_insight", org_name: "River Wisdom Insight Meditation Community",
    title: "Insight Meditation Sit",
    days: ["Saturday"], week_of_month: 3, time: { h: 10, m: 30 }, duration_min: 60,
    address: "2190 Garfield St", city: "Eugene", state: "OR", neighborhood: "South Eugene",
    lat: 44.0268, lng: -123.0978, tradition: "theravada", location_type: "in-person",
    notes: "River Wisdom Insight Meditation Community 3rd Saturday (10:30–11:30am) at Buddha Eye Temple (2190 Garfield St, Eugene). Sitting meditation. Led by Linda Rose (Spirit Rock / Howie Cohn lineage). Drop-in welcome; dana-based.",
    source_url: "https://riverwisdominsight.com", event_url: "https://riverwisdominsight.com/programs/",
  },

  // ============================================================
  // Santa Cruz, CA — Phase 3 (heartbeat 61)
  // ============================================================

  // Santa Cruz Zen Center (SCZC) — Soto Zen (SZBA). sczc.org
  // Mon–Fri 6am morning zazen (hybrid)
  {
    org_id: "sczc", org_name: "Santa Cruz Zen Center",
    title: "Morning Zazen",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], time: { h: 6, m: 0 }, duration_min: 40,
    address: "113 School St", city: "Santa Cruz", state: "CA", neighborhood: "Downtown Santa Cruz",
    lat: 36.9783, lng: -122.0278, tradition: "zen", location_type: "hybrid",
    notes: "Santa Cruz Zen Center weekday morning zazen (6:00–6:40am) at 113 School St, Santa Cruz. Zazen followed by morning service at 6:40am. In-person + Zoom hybrid. Founded 1970, Soto Zen (SZBA). Drop-in welcome.",
    source_url: "https://sczc.org", event_url: "https://sczc.org/zazen-schedule",
  },
  // Wednesday evening dharma program (hybrid)
  {
    org_id: "sczc", org_name: "Santa Cruz Zen Center",
    title: "Wednesday Evening Dharma Program",
    days: ["Wednesday"], time: { h: 18, m: 30 }, duration_min: 60,
    address: "113 School St", city: "Santa Cruz", state: "CA", neighborhood: "Downtown Santa Cruz",
    lat: 36.9783, lng: -122.0278, tradition: "zen", location_type: "hybrid",
    notes: "Santa Cruz Zen Center Wednesday evening program (6:30–7:30pm): kinhin (walking meditation) at 6:30pm, dharma lecture and discussion at 6:40pm. In-person + Zoom hybrid. Drop-in welcome.",
    source_url: "https://sczc.org", event_url: "https://sczc.org/zazen-schedule",
  },
  // Saturday 8:30am zazen (hybrid)
  {
    org_id: "sczc", org_name: "Santa Cruz Zen Center",
    title: "Saturday Morning Zazen",
    days: ["Saturday"], time: { h: 8, m: 30 }, duration_min: 40,
    address: "113 School St", city: "Santa Cruz", state: "CA", neighborhood: "Downtown Santa Cruz",
    lat: 36.9783, lng: -122.0278, tradition: "zen", location_type: "hybrid",
    notes: "Santa Cruz Zen Center Saturday morning zazen (8:30–9:10am) at 113 School St, Santa Cruz. In-person + Zoom hybrid. Drop-in welcome; no registration needed.",
    source_url: "https://sczc.org", event_url: "https://sczc.org/zazen-schedule",
  },
  // Sunday 6pm zazen (hybrid)
  {
    org_id: "sczc", org_name: "Santa Cruz Zen Center",
    title: "Sunday Evening Zazen",
    days: ["Sunday"], time: { h: 18, m: 0 }, duration_min: 40,
    address: "113 School St", city: "Santa Cruz", state: "CA", neighborhood: "Downtown Santa Cruz",
    lat: 36.9783, lng: -122.0278, tradition: "zen", location_type: "hybrid",
    notes: "Santa Cruz Zen Center Sunday evening zazen (6:00–6:40pm) at 113 School St, Santa Cruz. In-person + Zoom hybrid. No service follows. Drop-in welcome.",
    source_url: "https://sczc.org", event_url: "https://sczc.org/zazen-schedule",
  },

  // Insight Santa Cruz — Insight/Vipassana. insightsantacruz.org
  // Sunday 9am volunteer-led sit (hybrid)
  {
    org_id: "insight_santa_cruz", org_name: "Insight Santa Cruz",
    title: "Sunday Morning Sit",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 45,
    address: "740 Front Street, Suite 240", city: "Santa Cruz", state: "CA", neighborhood: "Downtown Santa Cruz",
    lat: 36.9742, lng: -122.0308, tradition: "theravada", location_type: "hybrid",
    notes: "Insight Santa Cruz Sunday 9:00–9:45am volunteer-led sitting meditation with short reading. In-center (740 Front St, Suite 240) + online hybrid. Drop-in welcome; dana-based.",
    source_url: "https://www.insightsantacruz.org", event_url: "https://www.insightsantacruz.org/practice/",
  },
  // Tuesday 12pm All-Community Sit with teacher (hybrid)
  {
    org_id: "insight_santa_cruz", org_name: "Insight Santa Cruz",
    title: "Tuesday Community Sit",
    days: ["Tuesday"], time: { h: 12, m: 0 }, duration_min: 60,
    address: "740 Front Street, Suite 240", city: "Santa Cruz", state: "CA", neighborhood: "Downtown Santa Cruz",
    lat: 36.9742, lng: -122.0308, tradition: "theravada", location_type: "hybrid",
    notes: "Insight Santa Cruz Tuesday 12:00–1:00pm All-Community Sit with teacher (in-center + online hybrid). Vipassana/Insight Meditation; drop-in welcome; dana-based.",
    source_url: "https://www.insightsantacruz.org", event_url: "https://www.insightsantacruz.org/practice/",
  },
  // Wednesday 6pm All-Community Sit (hybrid)
  {
    org_id: "insight_santa_cruz", org_name: "Insight Santa Cruz",
    title: "Wednesday Evening Community Sit",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 75,
    address: "740 Front Street, Suite 240", city: "Santa Cruz", state: "CA", neighborhood: "Downtown Santa Cruz",
    lat: 36.9742, lng: -122.0308, tradition: "theravada", location_type: "hybrid",
    notes: "Insight Santa Cruz Wednesday 6:00–7:15pm All-Community Sit (in-center + online hybrid). Vipassana/Insight Meditation; drop-in welcome; dana-based.",
    source_url: "https://www.insightsantacruz.org", event_url: "https://www.insightsantacruz.org/practice/",
  },

  // Land of Medicine Buddha — FPMT/Gelug Tibetan. landofmedicinebuddha.org
  // Sunday 9am Drop-In Meditation (in-person at Gompa)
  {
    org_id: "land_of_medicine_buddha", org_name: "Land of Medicine Buddha",
    title: "Sunday Drop-In Meditation",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 60,
    address: "5800 Prescott Rd", city: "Soquel", state: "CA", neighborhood: "Santa Cruz Mountains / Soquel Hills",
    lat: 37.0061, lng: -121.9497, tradition: "tibetan", location_type: "in-person",
    notes: "Land of Medicine Buddha Sunday Drop-In Meditation (9:00–10:00am) at the Gompa, 5800 Prescott Rd, Soquel. Led by Ven. Yangchen. Sitting and walking meditation; suitable for all levels. No registration required. FPMT/Gelug Tibetan Buddhist center.",
    source_url: "https://www.landofmedicinebuddha.org", event_url: "https://www.landofmedicinebuddha.org/programs/",
  },

  // -------------------------------------------------------------------------
  // Wichita, KS — Phase 3 (heartbeat 62)
  // -------------------------------------------------------------------------

  // Southwind Sangha — Soto Zen (SZBA). southwindsangha.org
  // Meets at Pine Valley Christian Church, 5620 E 21st St N, Wichita KS 67208
  // Sunday 9–10:30am (zazen, kinhin, Heart Sutra)
  {
    org_id: "southwind_sangha", org_name: "Southwind Sangha",
    title: "Sunday Zazen",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 90,
    address: "5620 E 21st St N", city: "Wichita", state: "KS", neighborhood: "Northeast Wichita",
    lat: 37.7220, lng: -97.2520, tradition: "zen", location_type: "hybrid",
    notes: "Southwind Sangha Sunday service (9:00–10:30am) at Pine Valley Christian Church, 5620 E 21st St N, Wichita KS. Two rounds of seated zazen separated by kinhin (walking meditation), Heart Sutra chanting. In-person + Zoom hybrid. SZBA member. Drop-in welcome; contact harold.sanki@gmail.com or Facebook for Zoom link.",
    source_url: "https://southwindsangha.org", event_url: "https://southwindsangha.org",
  },
  // Wednesday 7–8pm sit
  {
    org_id: "southwind_sangha", org_name: "Southwind Sangha",
    title: "Wednesday Evening Zazen",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "5620 E 21st St N", city: "Wichita", state: "KS", neighborhood: "Northeast Wichita",
    lat: 37.7220, lng: -97.2520, tradition: "zen", location_type: "hybrid",
    notes: "Southwind Sangha Wednesday evening sit (7:00–8:00pm) at Pine Valley Christian Church, Wichita KS. First Wednesday = Introduction to Zen & Zazen. Third Wednesday = single 30-min sit + dharma discussion. In-person + Zoom hybrid. Drop-in welcome.",
    source_url: "https://southwindsangha.org", event_url: "https://southwindsangha.org",
  },

  // Wichita KTC — Karma Kagyu Tibetan. wichitaktc.org
  // 425 S Yale Ave, Wichita KS 67218
  // Every Sunday 10am (1st/3rd = Chenrezik Sadhana; 2nd/4th = Sitting Meditation)
  {
    org_id: "wichita_ktc", org_name: "Wichita KTC",
    title: "Sunday Program",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 105,
    address: "425 S Yale Ave", city: "Wichita", state: "KS", neighborhood: "East Wichita",
    lat: 37.6810, lng: -97.2680, tradition: "tibetan", location_type: "in-person",
    notes: "Wichita KTC Sunday program (10:00am–11:45am) at 425 S Yale Ave, Wichita KS. Karma Kagyu lineage. 1st and 3rd Sundays: Chenrezik Sadhana (compassion practice, mantra, sitting meditation) followed by dharma talk. 2nd and 4th Sundays: Sitting Meditation (10:00am) + discussion/book study (10:40–11:45am). All welcome. Contact ktcwichita@yahoo.com.",
    source_url: "https://wichitaktc.org", event_url: "https://wichitaktc.org",
  },

  // Dhammakaya Meditation Center Kansas — Thai Theravada. meditationkansas.org
  // 1650 S Water St, Wichita KS 67213
  // Saturday 3:30–5pm (most weeks; first Sat of month off)
  {
    org_id: "dmck", org_name: "Dhammakaya Meditation Center Kansas",
    title: "Saturday Meditation Class",
    days: ["Saturday"], time: { h: 15, m: 30 }, duration_min: 90,
    address: "1650 S Water St", city: "Wichita", state: "KS", neighborhood: "South Wichita",
    lat: 37.6635, lng: -97.3305, tradition: "theravada", location_type: "in-person",
    notes: "Dhammakaya Meditation Center Kansas Saturday public meditation class (3:30–5:00pm) at 1650 S Water St, Wichita KS. Thai Theravada (Dhammakaya tradition). No experience necessary; open to all. First Saturday of each month and special holidays may be off — check meditationkansas.org for updates.",
    source_url: "https://www.meditationkansas.org", event_url: "https://www.meditationkansas.org",
  },

  // ---------------------------------------------------------------------------
  // Missoula, MT — Phase 3 (heartbeat 63)
  // ---------------------------------------------------------------------------

  // Open Way Sangha — Plum Village / Vietnamese Zen (Thich Nhat Hanh lineage). openway.org
  {
    org_id: "open_way_sangha", org_name: "Open Way Sangha",
    title: "Tuesday Evening Sit",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "702 Brooks St", city: "Missoula", state: "MT", neighborhood: "South Missoula",
    lat: 46.8533, lng: -114.0078, tradition: "zen", location_type: "in-person",
    notes: "Open Way Sangha Tuesday evening sit (7:00–9:00pm) at 702 Brooks St, Missoula MT. Plum Village / Thich Nhat Hanh lineage. Rotating monthly format: dharma talk + sharing; meditation + sutra service + sharing; Mindfulness Trainings recitation + sharing; tea ceremony + sharing; special programs. All are welcome. Free (dana). Contact openwaysangha@gmail.com.",
    source_url: "https://www.openway.org", event_url: "https://www.openway.org/calendar",
  },
  {
    org_id: "open_way_sangha", org_name: "Open Way Sangha",
    title: "Saturday Morning Sit",
    days: ["Saturday"], time: { h: 10, m: 0 }, duration_min: 120,
    address: "702 Brooks St", city: "Missoula", state: "MT", neighborhood: "South Missoula",
    lat: 46.8533, lng: -114.0078, tradition: "zen", location_type: "in-person",
    notes: "Open Way Sangha Saturday morning sit (10:00am–noon) at 702 Brooks St, Missoula MT. Plum Village / Thich Nhat Hanh lineage. Rotating monthly format: dharma talk + sharing; meditation + sutra service + sharing; Mindfulness Trainings recitation + sharing; tea ceremony + sharing; special programs. All are welcome. Free (dana). Contact openwaysangha@gmail.com.",
    source_url: "https://www.openway.org", event_url: "https://www.openway.org/calendar",
  },

  // Osel Shen Phen Ling — FPMT Gelug Tibetan. fpmtosel.wordpress.com
  {
    org_id: "osel_shen_phen_ling", org_name: "Osel Shen Phen Ling",
    title: "Monday Evening Meditation",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "500 N Higgins Ave, Suite 208A", city: "Missoula", state: "MT", neighborhood: "Downtown Missoula",
    lat: 46.8723, lng: -113.9940, tradition: "tibetan", location_type: "in-person",
    notes: "Osel Shen Phen Ling Monday evening guided meditation (7:00pm, ~1 hour) at 500 N Higgins Ave Suite 208A, Missoula MT. FPMT Gelug Tibetan Buddhist center established 1986. Shamatha stabilizing meditation + brief prayers. No experience necessary; drop-in welcome. Free. Contact oselshenphenling@gmail.com or 406-327-1204.",
    source_url: "https://fpmtosel.wordpress.com", event_url: "https://fpmtosel.wordpress.com",
  },

  // Rocky Mountain Buddhist Center — Triratna (FWBO). rockymountainbuddhistcenter.org
  {
    org_id: "rocky_mountain_bc", org_name: "Rocky Mountain Buddhist Center",
    title: "Sangha Night",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 120,
    address: "540 South 2nd West", city: "Missoula", state: "MT", neighborhood: "University District",
    lat: 46.8645, lng: -114.0120, tradition: "other", location_type: "in-person",
    notes: "Rocky Mountain Buddhist Center Wednesday Sangha Night (7:00–9:00pm) at 540 South 2nd West, Missoula MT. Triratna Buddhist Community (formerly FWBO). Teaches Mindfulness of Breathing and Metta Bhavana. Open to those who have completed the 5-week Intro to Meditation and Buddhism course. Located near University of Montana campus. Contact fwbomissoula@gmail.com.",
    source_url: "http://rockymountainbuddhistcenter.org", event_url: "http://rockymountainbuddhistcenter.org",
  },

  // -------------------------------------------------------------------------
  // Knoxville, TN — Phase 3 (heartbeat 66)
  // -------------------------------------------------------------------------

  // Mountain Solid, Water Reflecting Sangha — Plum Village / TNH lineage. knoxmindful.org
  // West Knoxville Friends Meeting House, 1517 Meeting House Rd, Knoxville TN 37909.
  // Active since 1998. Weekly Sunday 4–5:30pm, hybrid (in-person + Zoom).
  {
    org_id: "mountain_solid_water_reflecting", org_name: "Mountain Solid, Water Reflecting Sangha",
    title: "Sunday Sangha Sitting",
    days: ["Sunday"], time: { h: 16, m: 0 }, duration_min: 90,
    address: "1517 Meeting House Rd", city: "Knoxville", state: "TN", neighborhood: "West Knoxville",
    lat: 35.9388, lng: -84.0801, tradition: "zen", location_type: "hybrid",
    notes: "Mountain Solid, Water Reflecting Sangha Sunday sit (4:00–5:30pm) at West Knoxville Friends Meeting House, 1517 Meeting House Rd. Plum Village / Order of Interbeing in the tradition of Thich Nhat Hanh. 1st Sundays: book discussion. 2nd Sundays: Mindfulness Trainings recitation + potluck. All welcome; no experience needed. In-person + Zoom (passcode 800925 — see knoxmindful.org).",
    source_url: "https://www.knoxmindful.org", event_url: "https://www.knoxmindful.org/events",
  },

  // Knoxville Community of Mindfulness — multi-tradition Vipassana/Zen/Dzogchen. knoxcomind.org
  // Meaningful Life Center, 116 Carr St, Knoxville TN. 1st & 3rd Thursdays in-person 6:30–8pm.
  {
    org_id: "knoxville_community_mindfulness", org_name: "Knoxville Community of Mindfulness",
    title: "Thursday Evening Sit",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 90,
    week_of_month: 1,
    address: "116 Carr St", city: "Knoxville", state: "TN", neighborhood: "Old North Knoxville",
    lat: 35.9837, lng: -83.9424, tradition: "other", location_type: "hybrid",
    notes: "Knoxville Community of Mindfulness 1st Thursday evening sit (6:30–8:00pm) at the Meaningful Life Center, 116 Carr St, Knoxville TN. Led by John Blackburn (50+ years practice in Vipassana, Zen, and Dzogchen). In-person + Zoom. All traditions welcome; no charge. knoxcomind.org.",
    source_url: "https://www.knoxcomind.org", event_url: "https://www.knoxcomind.org",
  },
  {
    org_id: "knoxville_community_mindfulness", org_name: "Knoxville Community of Mindfulness",
    title: "Thursday Evening Sit",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 90,
    week_of_month: 3,
    address: "116 Carr St", city: "Knoxville", state: "TN", neighborhood: "Old North Knoxville",
    lat: 35.9837, lng: -83.9424, tradition: "other", location_type: "hybrid",
    notes: "Knoxville Community of Mindfulness 3rd Thursday evening sit (6:30–8:00pm) at the Meaningful Life Center, 116 Carr St, Knoxville TN. Led by John Blackburn (50+ years practice in Vipassana, Zen, and Dzogchen). In-person + Zoom. All traditions welcome; no charge. knoxcomind.org.",
    source_url: "https://www.knoxcomind.org", event_url: "https://www.knoxcomind.org",
  },

  // Je Tsongkhapa Kadampa Buddhist Center – Knoxville (NKT outreach from KMC Asheville).
  // OASIS Institute, 4918 Homberg Dr, Knoxville TN. Weekly Tuesday 7:15–8:30pm.
  {
    org_id: "je_tsongkhapa_knoxville", org_name: "Je Tsongkhapa Kadampa Buddhist Center – Knoxville",
    title: "Tuesday Drop-In Meditation Class",
    days: ["Tuesday"], time: { h: 19, m: 15 }, duration_min: 75,
    address: "4918 Homberg Dr", city: "Knoxville", state: "TN", neighborhood: "Bearden",
    lat: 35.9488, lng: -84.0165, tradition: "tibetan", location_type: "in-person",
    notes: "Je Tsongkhapa Kadampa Buddhist Center Tuesday drop-in meditation class (7:15–8:30pm) at the OASIS Institute, 4918 Homberg Dr, Bearden, Knoxville TN. NKT outreach program of KMC Asheville (NC). Teachings from Kadampa Buddhist philosophy; no background or reservation needed. Part of 1,300+ center NKT-IKBU network. Info: meditationinasheville.org.",
    source_url: "https://www.meditationinasheville.org/tuesday-evening-drop-in-meditation-class-knoxville-tn/",
    event_url: "https://www.meditationinasheville.org/tuesday-evening-drop-in-meditation-class-knoxville-tn/",
  },

  // Lotus Light Contemplative Community Center — multi-tradition hub. lotuslightcenter.org
  // 501 Arthur St, Knoxville TN 37921 (Mechanicsville, ~1 mi west of UT). Two primary sits:
  //   Insight Meditation: Monday 7:00–8:30pm
  //   Zazen: Sunday 4:00–5:00pm
  {
    org_id: "lotus_light_knoxville", org_name: "Lotus Light Contemplative Community Center",
    title: "Insight Meditation",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "501 Arthur St", city: "Knoxville", state: "TN", neighborhood: "Mechanicsville",
    lat: 35.9764, lng: -83.9567, tradition: "other", location_type: "hybrid",
    notes: "Lotus Light Contemplative Community Center Insight Meditation (7:00–8:30pm every Monday) at 501 Arthur St, Mechanicsville, Knoxville TN. Vipassana-style sitting in a welcoming multi-tradition setting. Zoom also available (PW: lotus — link at lotuslightcenter.org). Free, all welcome.",
    source_url: "https://lotuslightcenter.org", event_url: "https://lotuslightcenter.org/calendar/",
  },
  {
    org_id: "lotus_light_knoxville", org_name: "Lotus Light Contemplative Community Center",
    title: "Zazen",
    days: ["Sunday"], time: { h: 16, m: 0 }, duration_min: 60,
    address: "501 Arthur St", city: "Knoxville", state: "TN", neighborhood: "Mechanicsville",
    lat: 35.9764, lng: -83.9567, tradition: "zen", location_type: "hybrid",
    notes: "Lotus Light Contemplative Community Center Zazen (4:00–5:00pm every Sunday) at 501 Arthur St, Mechanicsville, Knoxville TN. Zen sitting meditation in a community hub home to Losel Shedrup Ling (Tibetan Buddhist) and other groups. Zoom available (PW: lotus — link at lotuslightcenter.org). Free, all welcome.",
    source_url: "https://lotuslightcenter.org", event_url: "https://lotuslightcenter.org/calendar/",
  },

  // -------------------------------------------------------------------------
  // Lehigh Valley, PA — Phase 3 (heartbeat 65)
  // -------------------------------------------------------------------------

  // Dharma Moon Sangha — Plum Village / Order of Interbeing. dharmamoonsangha.com
  // Living Room Yoga, 1328 Chestnut St, Emmaus PA 18049. Active since 2009.
  {
    org_id: "dharma_moon_sangha", org_name: "Dharma Moon Sangha",
    title: "Tuesday Evening Sit",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "1328 Chestnut St", city: "Emmaus", state: "PA", neighborhood: "Emmaus",
    lat: 40.5380, lng: -75.4998, tradition: "zen", location_type: "hybrid",
    notes: "Dharma Moon Sangha Tuesday sit (7:00–8:30pm) at Living Room Yoga, 1328 Chestnut St, Emmaus PA. Plum Village / Order of Interbeing. 20-min zazen, kinhin (walking meditation), more seated meditation, dharma sharing. In-person + simultaneous Zoom. Free, drop-in welcome. Contact emmaussangha@gmail.com for Zoom link.",
    source_url: "https://dharmamoonsangha.com", event_url: "https://dharmamoonsangha.com",
  },

  // Blue Mountain Zendo — Rinzai Zen. bluemountainzendo.org
  // Bethlehem PA 18017 (private address; call 484-735-0636). Rev. Ryuun Joriki Baker.
  {
    org_id: "blue_mountain_zendo", org_name: "Blue Mountain Zendo",
    title: "Sunday Zen Service",
    days: ["Sunday"], time: { h: 17, m: 0 }, duration_min: 120,
    address: "Bethlehem, PA", city: "Bethlehem", state: "PA", neighborhood: "Bethlehem",
    lat: 40.6259, lng: -75.3705, tradition: "zen", location_type: "in-person",
    notes: "Blue Mountain Zendo (Koryu-ji) Sunday Zen service (5:00–7:00pm) in Bethlehem, PA. Rinzai Zen; led by Rev. Ryuun Joriki Baker. Full service: chanting, zazen, kinhin (walking meditation), formal eating (oryoki), dharma talk, tea fellowship. Newcomers welcome — arrive 15 min early. Private home; call 484-735-0636 or visit bluemountainzendo.org for directions.",
    source_url: "https://www.bluemountainzendo.org", event_url: "https://www.bluemountainzendo.org",
  },

  // Lehigh Valley Buddhist Group — non-sectarian ecumenical. lvbuddhistgroup.org
  // Unity of Lehigh Valley, 26 N 3rd St, Emmaus PA 18049. Monthly Sundays.
  // 2026 upcoming dates: Jun 21, Jul 12, Aug 16 (3rd Sun), Sep 20 (3rd Sun), Oct 18 (3rd Sun)
  {
    org_id: "lv_buddhist_group", org_name: "Lehigh Valley Buddhist Group",
    title: "Monthly Sunday Gathering",
    days: ["Sunday"], time: { h: 16, m: 0 }, duration_min: 90,
    dates: ["2026-06-21", "2026-07-12", "2026-08-16", "2026-09-20", "2026-10-18"],
    address: "26 N 3rd St", city: "Emmaus", state: "PA", neighborhood: "Emmaus",
    lat: 40.5378, lng: -75.4965, tradition: "other", location_type: "in-person",
    notes: "Lehigh Valley Buddhist Group monthly Sunday gathering (4:00–5:30pm) at Unity of Lehigh Valley church, 26 N 3rd St, Emmaus PA. Non-sectarian; guest teachers from Theravada, Tibetan, Zen, and other traditions lead meditation and dharma talks. Open to all. Free. Info@lvbuddhistgroup.org.",
    source_url: "https://www.lvbuddhistgroup.org", event_url: "https://www.lvbuddhistgroup.org/events-2-1",
  },

  // -------------------------------------------------------------------------
  // Chattanooga, TN — Phase 3 (heartbeat 67)
  // -------------------------------------------------------------------------

  // Chattanooga Insight Group — Vipassana/Insight tradition. chattanoogainsight.com
  // Center for Mindful Living, 400 E Main St Ste 150, Chattanooga TN 37408.
  // Continues community after CIMC closed Dec 2025. Weekly Thursday 6:30–7:45pm.
  {
    org_id: "chattanooga_insight_group", org_name: "Chattanooga Insight Group",
    title: "Thursday Evening Sit",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 75,
    address: "400 E Main St Ste 150", city: "Chattanooga", state: "TN", neighborhood: "Downtown Chattanooga",
    lat: 35.0484, lng: -85.3087, tradition: "theravada", location_type: "in-person",
    notes: "Chattanooga Insight Group Thursday evening sit (6:30–7:45pm) at Center for Mindful Living, 400 E Main St Ste 150, downtown Chattanooga TN. Insight/Vipassana tradition. Begins with 30 min silent meditation, followed by dharma talk or sharing and Q&A. Continues the community of the former CIMC (closed Dec 2025). Free, all welcome. chattanoogainsight.com.",
    source_url: "https://chattanoogainsight.com", event_url: "https://breathingbody.net/events/chattanooga-insight-group/",
  },

  // Zen Group of Chattanooga — Soto Zen, Silent Thunder Order (Matsuoka lineage).
  // 335 Crestway Drive, Chattanooga TN 37411. Weekly Sunday 7:30–9:00am.
  // Format: 3x20–25 min zazen + 2x5 min kinhin. Contact: tlrieth@comcast.net.
  {
    org_id: "zen_group_chattanooga", org_name: "Zen Group of Chattanooga",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 7, m: 30 }, duration_min: 90,
    address: "335 Crestway Drive", city: "Chattanooga", state: "TN", neighborhood: "Eastdale",
    lat: 35.0203, lng: -85.2395, tradition: "zen", location_type: "in-person",
    notes: "Zen Group of Chattanooga Sunday morning zazen (7:30–9:00am) at 335 Crestway Drive, Chattanooga TN. Soto Zen, Silent Thunder Order (Soyu Matsuoka Roshi lineage). Three 20–25 min zazen periods alternating with kinhin (walking meditation). Newcomers welcome; instruction available. Free, donations appreciated. Contact: tlrieth@comcast.net.",
    source_url: "https://storder.org/portfolio/chattanooga-zen-group/", event_url: "https://storder.org/portfolio/chattanooga-zen-group/",
  },

  // Paramita Center Southeast — Tibetan Gelug, Paramita lineage (Quebec/India).
  // St Andrews Center, 1918 Union Ave, Chattanooga TN 37405.
  // Regular "Happy Hour" meditation: Tuesday 5:30–6:30pm. All traditions welcome.
  {
    org_id: "paramita_center_southeast", org_name: "Paramita Center Southeast",
    title: "Tuesday Happy Hour Meditation",
    days: ["Tuesday"], time: { h: 17, m: 30 }, duration_min: 60,
    address: "1918 Union Ave", city: "Chattanooga", state: "TN", neighborhood: "North Chattanooga",
    lat: 35.0713, lng: -85.3128, tradition: "tibetan", location_type: "in-person",
    notes: "Paramita Center Southeast Tuesday 'Happy Hour' meditation (5:30–6:30pm) at St Andrews Center, 1918 Union Ave, North Chattanooga TN. Tibetan Gelug tradition (Paramita Centres lineage); senior teacher Tenzin Gawa (Jason Simard). Brief intro teaching, group practice, and discussion. All traditions and levels welcome. Free. buddhismsoutheast.org.",
    source_url: "https://buddhismsoutheast.org", event_url: "https://buddhismsoutheast.org/calendar/",
  },

  // -----------------------------------------------------------------------
  // Colorado Springs, CO — Phase 3 (heartbeat 68)
  // -----------------------------------------------------------------------

  // Springs Mountain Sangha — Pacific Zen School / Sanbo Kyodan lineage.
  // Shove Chapel, Colorado College, Colorado Springs CO 80903.
  // Mon 6–8pm (dharma talk), Wed 6:30–7:30am, Sat 6:30–8:30am. Drop-in, free.
  {
    org_id: "springs_mountain_sangha", org_name: "Springs Mountain Sangha",
    title: "Monday Evening Zen Sitting",
    days: ["Monday"], time: { h: 18, m: 0 }, duration_min: 120,
    address: "1010 N Nevada Ave", city: "Colorado Springs", state: "CO", neighborhood: "Colorado College",
    lat: 38.8433, lng: -104.8225, tradition: "zen", location_type: "in-person",
    notes: "Springs Mountain Sangha Monday Evening Zen Sitting (6:00–8:00pm) at Shove Chapel, Colorado College, Colorado Springs CO. Pacific Zen School / Open Source Zen / Sanbo Kyodan lineage. Two sitting periods + dharma talk. Also available via Zoom. Drop-in, free. smszen.org.",
    source_url: "https://www.smszen.org", event_url: "https://www.smszen.org/sangha-event-calendar/",
  },
  {
    org_id: "springs_mountain_sangha", org_name: "Springs Mountain Sangha",
    title: "Wednesday Morning Zen Sitting",
    days: ["Wednesday"], time: { h: 6, m: 30 }, duration_min: 60,
    address: "1010 N Nevada Ave", city: "Colorado Springs", state: "CO", neighborhood: "Colorado College",
    lat: 38.8433, lng: -104.8225, tradition: "zen", location_type: "in-person",
    notes: "Springs Mountain Sangha Wednesday Morning Zen Sitting (6:30–7:30am) at Shove Chapel, Colorado College, Colorado Springs CO. Two sitting periods with walking meditation. Drop-in, free. smszen.org.",
    source_url: "https://www.smszen.org", event_url: "https://www.smszen.org/sangha-event-calendar/",
  },
  {
    org_id: "springs_mountain_sangha", org_name: "Springs Mountain Sangha",
    title: "Saturday Morning Zen Sitting",
    days: ["Saturday"], time: { h: 6, m: 30 }, duration_min: 120,
    address: "1010 N Nevada Ave", city: "Colorado Springs", state: "CO", neighborhood: "Colorado College",
    lat: 38.8433, lng: -104.8225, tradition: "zen", location_type: "in-person",
    notes: "Springs Mountain Sangha Saturday Morning Zen Sitting (6:30–8:30am) at Shove Chapel, Colorado College, Colorado Springs CO. Four sitting periods with walking meditation. Drop-in, free. smszen.org.",
    source_url: "https://www.smszen.org", event_url: "https://www.smszen.org/sangha-event-calendar/",
  },

  // Rocky Mountain Insight — Vipassana/Insight Meditation (Theravada).
  // 2525 W Pikes Peak Ave Suite A, Colorado Springs CO 80904 (Old Colorado City).
  // Sun 9–10am, Wed 6–7pm. Drop-in, free, in-person + Zoom.
  {
    org_id: "rocky_mountain_insight_cs", org_name: "Rocky Mountain Insight",
    title: "Sunday Morning Vipassana Sit",
    days: ["Sunday"], time: { h: 9, m: 0 }, duration_min: 60,
    address: "2525 W Pikes Peak Ave Suite A", city: "Colorado Springs", state: "CO", neighborhood: "Old Colorado City",
    lat: 38.8673, lng: -104.8806, tradition: "theravada", location_type: "in-person",
    notes: "Rocky Mountain Insight Sunday Morning Vipassana Sit (9:00–10:00am) at 2525 W. Pikes Peak Ave. Suite A, Old Colorado City, Colorado Springs CO. Sitting practice and dharma reading. Drop-in, in-person + Zoom. Free; donations welcome. rockymountaininsight.org.",
    source_url: "https://rockymountaininsight.org", event_url: "https://rockymountaininsight.org/classes/",
  },
  {
    org_id: "rocky_mountain_insight_cs", org_name: "Rocky Mountain Insight",
    title: "Wednesday Sangha Night",
    days: ["Wednesday"], time: { h: 18, m: 0 }, duration_min: 60,
    address: "2525 W Pikes Peak Ave Suite A", city: "Colorado Springs", state: "CO", neighborhood: "Old Colorado City",
    lat: 38.8673, lng: -104.8806, tradition: "theravada", location_type: "in-person",
    notes: "Rocky Mountain Insight Wednesday Sangha Night (6:00–7:00pm) at 2525 W. Pikes Peak Ave. Suite A, Old Colorado City, Colorado Springs CO. Walking meditation, sitting, dharma talk, and community. Open to all. In-person + Zoom. Free; donations welcome. rockymountaininsight.org.",
    source_url: "https://rockymountaininsight.org", event_url: "https://rockymountaininsight.org/classes/",
  },

  // BodhiMind Center — Nonsectarian Buddhist, rooted in Tibetan tradition.
  // 2955 Professional Place Suite 101, Colorado Springs CO 80904.
  // Tue & Thu 6–8pm. Drop-in, free, in-person + Zoom.
  {
    org_id: "bodhimind_center_cs", org_name: "BodhiMind Center",
    title: "Tuesday Evening Meditation",
    days: ["Tuesday"], time: { h: 18, m: 0 }, duration_min: 120,
    address: "2955 Professional Place Suite 101", city: "Colorado Springs", state: "CO", neighborhood: "Old Colorado City",
    lat: 38.8670, lng: -104.8731, tradition: "tibetan", location_type: "in-person",
    notes: "BodhiMind Center Tuesday Evening Meditation (6:00–8:00pm) at 2955 Professional Place Suite 101, Colorado Springs CO. Nonsectarian Buddhist center rooted in Tibetan tradition (founded with support of Khen Rinpoche Lobzang Tsetan). Two 20-min sitting periods + teaching + discussion. Drop-in, free, in-person + Zoom. bodhimindcenter.org.",
    source_url: "https://bodhimindcenter.org", event_url: "https://bodhimindcenter.org/event-calendar/",
  },
  {
    org_id: "bodhimind_center_cs", org_name: "BodhiMind Center",
    title: "Thursday Evening Meditation",
    days: ["Thursday"], time: { h: 18, m: 0 }, duration_min: 120,
    address: "2955 Professional Place Suite 101", city: "Colorado Springs", state: "CO", neighborhood: "Old Colorado City",
    lat: 38.8670, lng: -104.8731, tradition: "tibetan", location_type: "in-person",
    notes: "BodhiMind Center Thursday Evening Meditation (6:00–8:00pm) at 2955 Professional Place Suite 101, Colorado Springs CO. Two 20-min sitting periods + teaching + discussion. Drop-in, free, in-person + Zoom. bodhimindcenter.org.",
    source_url: "https://bodhimindcenter.org", event_url: "https://bodhimindcenter.org/event-calendar/",
  },

  // Kadampa Meditation Center — Colorado Springs. New Kadampa Tradition (NKT/Gelug).
  // Edenology Holistic Wellness, 2611 W Colorado Ave Studio B, Colorado Springs CO 80904.
  // Mon 6:30–7:45pm. Drop-in, $15/class.
  {
    org_id: "kadampa_cs", org_name: "Kadampa Meditation Center — Colorado Springs",
    title: "Monday Evening Meditation Class",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 75,
    address: "2611 W Colorado Ave Studio B", city: "Colorado Springs", state: "CO", neighborhood: "Old Colorado City",
    lat: 38.8590, lng: -104.8780, tradition: "tibetan", location_type: "in-person",
    notes: "Kadampa Meditation Center — Colorado Springs Monday Evening Meditation Class (6:30–7:45pm) at Edenology Holistic Wellness, 2611 W. Colorado Ave. Studio B, Colorado Springs CO. New Kadampa Tradition (Gelug lineage, Geshe Kelsang Gyatso). Drop-in, no registration. $15/class; low-income accommodations available. meditationincolorado.org/colorado-springs/.",
    source_url: "https://meditationincolorado.org/colorado-springs/", event_url: "https://meditationincolorado.org/colorado-springs/",
  },

  // Tibetan Meditation Center Colorado — Tibetan Buddhism (Gelug).
  // 3560 Hartsock Lane, Colorado Springs CO 80917.
  // Sun 10–11am. Drop-in, free.
  {
    org_id: "tibetan_meditation_center_cs", org_name: "Tibetan Meditation Center Colorado",
    title: "Sunday Morning Meditation",
    days: ["Sunday"], time: { h: 10, m: 0 }, duration_min: 60,
    address: "3560 Hartsock Lane", city: "Colorado Springs", state: "CO", neighborhood: "Northeast Colorado Springs",
    lat: 38.9017, lng: -104.7558, tradition: "tibetan", location_type: "in-person",
    notes: "Tibetan Meditation Center Colorado Sunday Morning Meditation (10:00–11:00am) at 3560 Hartsock Lane, Colorado Springs CO 80917. Led by Geshe Wangden Tashi (trained 20+ years at Sera Je Monastery, Gelug lineage). Includes compassion teaching, silent meditation, mantra recitation, and group discussion. Drop-in, all welcome, free. tibetanmeditationcentercolorado.com.",
    source_url: "https://www.tibetanmeditationcentercolorado.com", event_url: "https://www.tibetanmeditationcentercolorado.com",
  },

  // -----------------------------------------------------------------------
  // Fort Collins, CO — Phase 3 (heartbeat 69)
  // -----------------------------------------------------------------------

  // Prairie Mountain Zen Center — Fort Collins group. Soto Zen (Katagiri lineage).
  // Plymouth Congregational Church, 916 W Prospect Rd, Fort Collins CO 80526.
  // Thu 6:30–8:00pm. Drop-in, free.
  {
    org_id: "prairie_mountain_zen_fc", org_name: "Prairie Mountain Zen Center — Fort Collins",
    title: "Thursday Evening Zazen",
    days: ["Thursday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "916 W Prospect Rd", city: "Fort Collins", state: "CO", neighborhood: "CSU Area",
    lat: 40.5684, lng: -105.0969, tradition: "zen", location_type: "in-person",
    notes: "Prairie Mountain Zen Center — Fort Collins Thursday Evening Zazen (6:30–8:00pm) at Plymouth Congregational Church, 916 W Prospect Rd, Fort Collins CO 80526 (enter from north parking lot door, follow signs to choir room). 30 minutes sitting + 10 minutes walking + tea and dharma discussion. Teacher trained under Dainin Katagiri Roshi at Minnesota Zen Center 1977–1989; listed with Soto Zen Buddhist Association (SZBA). Drop-in welcome, no fee. Contact: cliff@prairiemountain.org. prairiemountain.org/fort-collins.html.",
    source_url: "https://www.prairiemountain.org/fort-collins.html", event_url: "https://www.prairiemountain.org/fort-collins.html",
  },

  // Zen Meditation with Cathy Wright — Iyengar Yoga of Fort Collins.
  // Harada-Yasutani Zen (Dharma transmission 2023, Zen Center of Denver lineage).
  // Mon 5:30–6:30pm. Drop-in, free. Note: resumed June 1, 2026.
  {
    org_id: "zen_fc_wright", org_name: "Zen Meditation with Cathy Wright — Fort Collins",
    title: "Monday Evening Zen Sitting",
    days: ["Monday"], time: { h: 17, m: 30 }, duration_min: 60,
    address: "Fort Collins", city: "Fort Collins", state: "CO", neighborhood: "Fort Collins",
    lat: 40.5853, lng: -105.0844, tradition: "zen", location_type: "in-person",
    notes: "Monday Evening Zen Sitting (5:30–6:30pm) at Iyengar Yoga of Fort Collins (Sunrise Room), Fort Collins CO. Led by Cathy 'Seizan' Wright, who received Dharma transmission in 2023 from Peggy Metta Roshi at the Zen Center of Denver (Harada-Yasutani lineage, Soto and Rinzai styles). One hour silent sitting. Drop-in welcome; free, donations accepted for space rental. Resumed June 2026. cwrightyoga.com/zen-meditation/.",
    source_url: "https://www.cwrightyoga.com/zen-meditation/", event_url: "https://www.cwrightyoga.com/zen-meditation/",
  },

  // -----------------------------------------------------------------------
  // Bend / Central Oregon — Phase 3 (heartbeat 71)
  // -----------------------------------------------------------------------

  // Bend Zen — lay-led Zen group since 2003. Mon 7–8pm at Trinity Episcopal.
  {
    org_id: "bend_zen", org_name: "Bend Zen",
    title: "Monday Evening Zen Sitting",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "469 NW Wall St", city: "Bend", state: "OR", neighborhood: "Downtown Bend",
    lat: 44.0578, lng: -121.3155, tradition: "zen", location_type: "in-person",
    notes: "Monday Evening Zen Sitting (7:00–8:00pm) at Brooks Hall, Trinity Episcopal Church (469 NW Wall St, east entrance), Bend OR 97703. Social tea starts 6:40pm; dharma discussion group follows 8:00–8:30pm. Lay-led Zen group practicing since 2003, welcoming all traditions. Drop-in welcome; no fee. bendzen.net.",
    source_url: "https://www.bendzen.net", event_url: "https://www.bendzen.net",
  },

  // Natural Mind Dharma Center — Nyingma Tibetan (Dudjom Tersar), Bend OR.
  // Sun 8–9am (open to all) + Wed 7–8pm (Vajrayana experience preferred).
  {
    org_id: "natural_mind_bend", org_name: "Natural Mind Dharma Center",
    title: "Sunday Morning Vajrayana Practice",
    days: ["Sunday"], time: { h: 8, m: 0 }, duration_min: 60,
    address: "345 SW Century Dr, Suite 2", city: "Bend", state: "OR", neighborhood: "Southwest Bend",
    lat: 44.0422, lng: -121.3358, tradition: "tibetan", location_type: "hybrid",
    notes: "Sunday Morning Vajrayana Buddhist Practices and Dharma Talk (8:00–9:00am) at Natural Mind Dharma Center, 345 SW Century Dr #2, Bend OR 97702. Open to everyone. In-person and online (link via newsletter). Nyingma Tibetan tradition, Dudjom Tersar lineage. Teacher: Michael Scott Stevens (Pema Kunsang). Founded 1996. naturalminddharma.org.",
    source_url: "https://naturalminddharma.org/our-schedule/", event_url: "https://naturalminddharma.org/our-schedule/",
  },
  {
    org_id: "natural_mind_bend", org_name: "Natural Mind Dharma Center",
    title: "Wednesday Evening Practice and Teachings",
    days: ["Wednesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "345 SW Century Dr, Suite 2", city: "Bend", state: "OR", neighborhood: "Southwest Bend",
    lat: 44.0422, lng: -121.3358, tradition: "tibetan", location_type: "hybrid",
    notes: "Wednesday Evening Practice and Focused Teachings (7:00–8:00pm) at Natural Mind Dharma Center, 345 SW Century Dr #2, Bend OR 97702. Best for those with some experience in the Vajrayana tradition. In-person and online (link via newsletter). Nyingma Tibetan tradition, Dudjom Tersar lineage. naturalminddharma.org.",
    source_url: "https://naturalminddharma.org/our-schedule/", event_url: "https://naturalminddharma.org/our-schedule/",
  },

  // IIMC Redmond — non-sectarian Theravada/Vipassana, Redmond OR (~15 mi N of Bend).
  // Sun 1pm community practice (walking + sitting + metta). In-person.
  {
    org_id: "iimc_redmond", org_name: "International Insight Meditation Center of Oregon",
    title: "Sunday Community Practice",
    days: ["Sunday"], time: { h: 13, m: 0 }, duration_min: 120,
    address: "805 NW 95th St", city: "Redmond", state: "OR", neighborhood: "Redmond",
    lat: 44.2780, lng: -121.1519, tradition: "theravada", location_type: "in-person",
    notes: "Sunday Community Practice (1:00–3:00pm) at International Insight Meditation Center of Oregon (IIMC), 805 NW 95th St, Redmond OR 97756 (~15 miles north of Bend). Includes walking meditation, sitting meditation, and metta (loving-kindness). Non-sectarian Buddhist center founded 2015, dedicated to the Buddha's teachings as found in the Suttas. Monthly Peace Weekends on the third weekend. iimc-redmond.org.",
    source_url: "https://www.iimc-redmond.org/", event_url: "https://www.iimc-redmond.org/",
  },

  // -----------------------------------------------------------------------
  // Birmingham, Alabama — Phase 3 (heartbeat 73)
  // -----------------------------------------------------------------------

  // Birmingham Shambhala — Monday Evening Sitting (hybrid)
  {
    org_id: "birmingham_shambhala", org_name: "Birmingham Shambhala Meditation Center",
    title: "Monday Evening Sitting",
    days: ["Monday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "714 37th Street South", city: "Birmingham", state: "AL", neighborhood: "Avondale",
    lat: 33.5132, lng: -86.7684, tradition: "tibetan", location_type: "hybrid",
    notes: "Monday Evening Sitting (7:00–8:00pm) at Birmingham Shambhala Meditation Center, 714 37th Street South, Birmingham AL 35222 (Avondale). In-person and Zoom. Newcomers receive abbreviated instruction at the start. Shambhala Buddhist tradition; all are welcome. Free. birmingham.shambhala.org. (205) 515-1756.",
    source_url: "https://birmingham.shambhala.org", event_url: "https://birmingham.shambhala.org",
  },

  // Birmingham Shambhala — Tuesday Evening Sitting (hybrid)
  {
    org_id: "birmingham_shambhala", org_name: "Birmingham Shambhala Meditation Center",
    title: "Tuesday Evening Sitting",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "714 37th Street South", city: "Birmingham", state: "AL", neighborhood: "Avondale",
    lat: 33.5132, lng: -86.7684, tradition: "tibetan", location_type: "hybrid",
    notes: "Tuesday Evening Sitting (7:00–8:00pm) at Birmingham Shambhala Meditation Center, 714 37th Street South, Birmingham AL 35222 (Avondale). In-person and Zoom. Newcomers welcome; abbreviated instruction provided. Free. birmingham.shambhala.org.",
    source_url: "https://birmingham.shambhala.org", event_url: "https://birmingham.shambhala.org",
  },

  // Birmingham Shambhala — Wednesday Morning Sitting (in-person)
  {
    org_id: "birmingham_shambhala", org_name: "Birmingham Shambhala Meditation Center",
    title: "Wednesday Morning Sitting",
    days: ["Wednesday"], time: { h: 7, m: 0 }, duration_min: 60,
    address: "714 37th Street South", city: "Birmingham", state: "AL", neighborhood: "Avondale",
    lat: 33.5132, lng: -86.7684, tradition: "tibetan", location_type: "in-person",
    notes: "Wednesday Morning Sitting (7:00–8:00am) at Birmingham Shambhala Meditation Center, 714 37th Street South, Birmingham AL 35222 (Avondale). In-person only. Shambhala Buddhist meditation. Free and open to all. birmingham.shambhala.org.",
    source_url: "https://birmingham.shambhala.org", event_url: "https://birmingham.shambhala.org",
  },

  // Birmingham Shambhala — Friday Morning Sitting (hybrid)
  {
    org_id: "birmingham_shambhala", org_name: "Birmingham Shambhala Meditation Center",
    title: "Friday Morning Sitting",
    days: ["Friday"], time: { h: 7, m: 0 }, duration_min: 60,
    address: "714 37th Street South", city: "Birmingham", state: "AL", neighborhood: "Avondale",
    lat: 33.5132, lng: -86.7684, tradition: "tibetan", location_type: "hybrid",
    notes: "Friday Morning Sitting (7:00–8:00am) at Birmingham Shambhala Meditation Center, 714 37th Street South, Birmingham AL 35222 (Avondale). In-person and Zoom. Shambhala Buddhist meditation. Free and open to all. birmingham.shambhala.org.",
    source_url: "https://birmingham.shambhala.org", event_url: "https://birmingham.shambhala.org",
  },

  // Birmingham Shambhala — First Sunday Community Sit (hybrid, monthly)
  {
    org_id: "birmingham_shambhala", org_name: "Birmingham Shambhala Meditation Center",
    title: "First Sunday Community Sit",
    days: ["Sunday"], week_of_month: 1, time: { h: 10, m: 0 }, duration_min: 120,
    address: "714 37th Street South", city: "Birmingham", state: "AL", neighborhood: "Avondale",
    lat: 33.5132, lng: -86.7684, tradition: "tibetan", location_type: "hybrid",
    notes: "First Sunday Community Sit (10:00am–noon) at Birmingham Shambhala Meditation Center, 714 37th Street South, Birmingham AL 35222 (Avondale). First Sunday of each month. In-person and Zoom. Longer community gathering including meditation, dharma discussion, and community time. Free and open to all. birmingham.shambhala.org.",
    source_url: "https://birmingham.shambhala.org", event_url: "https://birmingham.shambhala.org",
  },

  // Burning Rock Soto Zen — Sunday Zazen (in-person, at Shambhala)
  {
    org_id: "burning_rock_soto_zen", org_name: "Burning Rock Soto Zen",
    title: "Sunday Zazen",
    days: ["Sunday"], time: { h: 13, m: 15 }, duration_min: 45,
    address: "714 37th Street South", city: "Birmingham", state: "AL", neighborhood: "Avondale",
    lat: 33.5132, lng: -86.7684, tradition: "zen", location_type: "in-person",
    notes: "Sunday Zazen (1:15–2:00pm) at Burning Rock Soto Zen, meeting at Birmingham Shambhala Meditation Center, 714 37th Street South, Birmingham AL 35222 (Avondale). Beginner orientation 1:15–1:30pm, zazen 1:30–2:00pm. Soto Zen tradition, affiliated with the Silent Thunder Order and Atlanta Soto Zen Center. Teacher: Andrew Keitt. Free; drop-in welcome. alabamameditationnetwork.com/burning-rock-soto-zen/.",
    source_url: "https://alabamameditationnetwork.com/burning-rock-soto-zen/", event_url: "https://alabamameditationnetwork.com/burning-rock-soto-zen/",
  },

  // Cahaba River Sangha — Thursday Evening Sit (hybrid, Plum Village)
  {
    org_id: "cahaba_river_sangha", org_name: "Cahaba River Sangha",
    title: "Thursday Evening Sit",
    days: ["Thursday"], time: { h: 19, m: 0 }, duration_min: 90,
    address: "2803 Highland Ave", city: "Birmingham", state: "AL", neighborhood: "Southside",
    lat: 33.5011, lng: -86.7975, tradition: "zen", location_type: "hybrid",
    notes: "Thursday Evening Sit (7:00–8:30pm) at Cahaba River Sangha, Unity Church of Birmingham, 2803 Highland Ave, Birmingham AL 35205 (Southside). In-person and Zoom. Plum Village / Thich Nhat Hanh tradition. Includes sitting meditation, walking meditation, and dharma talk/discussion. All are welcome; free. cahabariversangha.com.",
    source_url: "https://cahabariversangha.com", event_url: "https://cahabariversangha.com",
  },

  // Losel Maitri Tibetan Buddhist Center — Tuesday Evening Worship
  {
    org_id: "losel_maitri", org_name: "Losel Maitri Tibetan Buddhist Center",
    title: "Tuesday Evening Worship",
    days: ["Tuesday"], time: { h: 19, m: 0 }, duration_min: 60,
    address: "3224 Green Valley Rd", city: "Vestavia Hills", state: "AL", neighborhood: "Cahaba Heights",
    lat: 33.4728, lng: -86.7332, tradition: "tibetan", location_type: "in-person",
    notes: "Tuesday Evening Worship Service (7:00–8:00pm) at Losel Maitri Tibetan Buddhist Center, 3224 Green Valley Rd, Cahaba Heights (Vestavia Hills), AL 35243. Open to all. Affiliated with Namgyal Monastery (Ithaca, NY), the personal North American monastery of His Holiness the Dalai Lama. Resident teacher: Ven. Tenzin Deshek. Introduction to Buddhism class at 5:50pm. (205) 470-6940.",
    source_url: "https://www.facebook.com/LoselMaitriBuddhist/", event_url: "https://www.facebook.com/LoselMaitriBuddhist/",
  },

  // -----------------------------------------------------------------------
  // Anchorage, Alaska — Phase 3 (heartbeat 72)
  // -----------------------------------------------------------------------

  // Anchorage Zen Community — Soto Zen, ordained teacher Genmyo Zeedyk.
  // Sun 8:30–9:55am hybrid (zazen + kinhin; dharma talk 10am). Drop-in welcome.
  {
    org_id: "anchorage_zen", org_name: "Anchorage Zen Community",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 8, m: 30 }, duration_min: 85,
    address: "711 Barrow St", city: "Anchorage", state: "AK", neighborhood: "Downtown Anchorage",
    lat: 61.2143, lng: -149.9003, tradition: "zen", location_type: "hybrid",
    notes: "Sunday Morning Zazen (8:30–9:55am) at Anchorage Zen Community (AZC), 711 Barrow St, Anchorage AK 99501 (between 7th and 8th Ave, downtown). In-person and Zoom. Multiple zazen periods with kinhin (walking meditation); Dharma talk and discussion at 10:00am. Beginner instruction available before the 9am session. Drop-in welcome; no cost. Led by Genmyo Zeedyk (ordained 2009, Dharma transmission 2013). anchoragezen.com.",
    source_url: "http://www.anchoragezen.com", event_url: "http://www.anchoragezen.com",
  },

  // Upright Noble Zen — Soto Zen, White Plum Asanga (Chozen/Hogen Bays lineage).
  // Sun 5–6:30pm hybrid at Pioneer Schoolhouse + Mon–Thu 6:30am Zoom.
  {
    org_id: "upright_noble_zen", org_name: "Upright Noble Zen",
    title: "Sunday Evening Zazen",
    days: ["Sunday"], time: { h: 17, m: 0 }, duration_min: 90,
    address: "437 E 3rd Ave", city: "Anchorage", state: "AK", neighborhood: "Downtown Anchorage",
    lat: 61.2163, lng: -149.8775, tradition: "zen", location_type: "hybrid",
    notes: "Sunday Evening Zazen (5:00–6:30pm) at Upright Noble Zen, Pioneer Schoolhouse, 437 E 3rd Avenue, Anchorage AK 99501. In-person and Zoom (ID 898-544-2353, password: zazen). Includes two 25-minute zazen periods, Dharma Talk, brief check-in, and chanting. Arrive by 4:55pm. Teacher: Dana Kojun Lederhos-Hull (Dharma Successor of Chozen and Hogen Bays, White Plum Asanga). Everyone welcome; drop-in. uprightnoble.wordpress.com.",
    source_url: "https://uprightnoble.wordpress.com", event_url: "https://uprightnoble.wordpress.com",
  },
  {
    org_id: "upright_noble_zen", org_name: "Upright Noble Zen",
    title: "Weekday Morning Zazen (Zoom)",
    days: ["Monday", "Tuesday", "Wednesday", "Thursday"], time: { h: 6, m: 30 }, duration_min: 30,
    address: "Zoom", city: "Anchorage", state: "AK", neighborhood: "Online",
    lat: 61.2163, lng: -149.8775, tradition: "zen", location_type: "online",
    notes: "Weekday Morning Zazen (6:30–7:00am) via Zoom only. Upright Noble Zen, Anchorage AK. 25-minute sitting period followed by Heart Sutra chanting. Zoom ID 898-544-2353, password: zazen. Monday through Thursday. Drop-in welcome. uprightnoble.wordpress.com.",
    source_url: "https://uprightnoble.wordpress.com", event_url: "https://uprightnoble.wordpress.com",
  },

  // Katog Sangyey Ling — Nyingma Tibetan (Katog Choling lineage).
  // Tue 6:30–7:30pm hybrid. Alternates Tonglen, Shamatha, Heart Sutra monthly.
  {
    org_id: "katog_sangyey_ling", org_name: "Katog Sangyey Ling",
    title: "Tuesday Evening Meditation",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 60,
    address: "4105 E Turnagain Blvd, Suite C3", city: "Anchorage", state: "AK", neighborhood: "Turnagain",
    lat: 61.2061, lng: -149.9448, tradition: "tibetan", location_type: "hybrid",
    notes: "Tuesday Evening Meditation (6:30–7:30pm) at Katog Sangyey Ling, 4105 E Turnagain Blvd, Suite C3, Anchorage AK 99517 (Turnagain neighborhood). In-person and Zoom (email katogsangyeyling@gmail.com for Zoom link). Nyingma Tibetan Buddhist tradition, Katog Choling lineage under Khentrul Lodrö Thayé Rinpoche. Sessions alternate monthly between Tonglen (loving-kindness), Shamatha (calm-abiding), and Heart Sutra. No prior experience necessary; everyone welcome. (907) 947-8881. katogsangyeyling.org.",
    source_url: "https://www.katogsangyeyling.org", event_url: "https://www.katogsangyeyling.org",
  },

  // Green Mountain Zen Center — Korean/Rinzai Zen (Single Flower Sangha / Kwan Um lineage).
  // Sun 6–7:30pm hybrid at private zendo, 12035 Mountcrest Rd SE, Huntsville AL 35803.
  // Founded 1993. Guiding teacher: Zen Master George Bowman (BoMun); local teachers Gary Beard + Jim Gordon.
  {
    org_id: "green_mountain_zen", org_name: "Green Mountain Zen Center",
    title: "Sunday Evening Meditation",
    days: ["Sunday"], time: { h: 18, m: 0 }, duration_min: 90,
    address: "12035 Mountcrest Rd SE", city: "Huntsville", state: "AL", neighborhood: "Green Mountain",
    lat: 34.6279, lng: -86.5183, tradition: "zen", location_type: "hybrid",
    notes: "Sunday Evening Meditation (6:00–7:30pm) at Green Mountain Zen Center, 12035 Mountcrest Rd SE, Huntsville AL 35803 (Green Mountain neighborhood). In-person and Zoom. Brief chanting period followed by two zazen periods with kinhin (walking meditation). Newcomers welcome; optional social gathering at a local deli after the service. Email greenmountainzenhsv@gmail.com or call (256) 426-3344 before first visit. Kwan Um School of Zen / Single Flower Sangha lineage. gmzc.us.",
    source_url: "https://www.gmzc.us", event_url: "https://www.gmzc.us/weekly-practice/",
  },

  // -----------------------------------------------------------------------
  // Flagstaff, Arizona — Phase 3 (heartbeat 75)
  // -----------------------------------------------------------------------

  // Flagstaff Insight Meditation Community (FIMC) — Theravada/Vipassana.
  // Mon 6:30–8:00pm hybrid at Beacon UU (510 N Leroux St, downtown Flagstaff).
  // Confirmed at flagstaffinsight.org ("at 6:30PM (MST)" per live site JS).
  {
    org_id: "fimc_flagstaff", org_name: "Flagstaff Insight Meditation Community",
    title: "Monday Evening Meditation & Dharma Talk",
    days: ["Monday"], time: { h: 18, m: 30 }, duration_min: 90,
    address: "510 N Leroux St", city: "Flagstaff", state: "AZ", neighborhood: "Downtown Flagstaff",
    lat: 35.2004, lng: -111.6519, tradition: "theravada", location_type: "hybrid",
    notes: "Monday Evening Meditation (6:30–8:00pm) at Flagstaff Insight Meditation Community (FIMC), Beacon Unitarian Universalist Congregation, 510 N Leroux St, Flagstaff AZ 86001 (downtown). In-person and Zoom. Sitting meditation followed by a dharma talk and optional discussion. Free, dana-based; all are welcome. flagstaffinsight.org.",
    source_url: "https://flagstaffinsight.org", event_url: "https://flagstaffinsight.org/calendar/",
  },

  // Flagstaff Zen Sangha — Diamond Sangha lineage (Robert Aitken Roshi).
  // Sun 8:30am in-person at Human Nature Studio, 2 S Beaver St Suite 150.
  {
    org_id: "flagstaff_zen_sangha", org_name: "Flagstaff Zen Sangha",
    title: "Sunday Morning Zazen",
    days: ["Sunday"], time: { h: 8, m: 30 }, duration_min: 90,
    address: "2 S Beaver St, Suite 150", city: "Flagstaff", state: "AZ", neighborhood: "Downtown Flagstaff",
    lat: 35.1988, lng: -111.6510, tradition: "zen", location_type: "in-person",
    notes: "Sunday Morning Zazen (8:30am) at Flagstaff Zen Sangha, Human Nature Studio, 2 South Beaver St Suite 150, Flagstaff AZ 86001 (downtown). Sutra service, kinhin (walking meditation), and two 25-minute zazen periods. First-time visitors welcome at 8:00am for brief orientation. Diamond Sangha lineage (Robert Aitken Roshi). In-person only; drop-in welcome. Free. (928) 699-6651.",
    source_url: "https://flagstaff365.com/organization/flagstaff-zen-sangha/", event_url: "https://flagstaff365.com/organization/flagstaff-zen-sangha/",
  },

  // IKRC Grand Canyon — Flagstaff outreach class. NKT/Kadampa.
  // Tue 6:30–7:45pm at Beacon UU (510 N Leroux St), $10/$5 students.
  {
    org_id: "ikrc_flagstaff", org_name: "Kadampa Meditation — Flagstaff Class",
    title: "Tuesday Evening Meditation Class",
    days: ["Tuesday"], time: { h: 18, m: 30 }, duration_min: 75,
    address: "510 N Leroux St", city: "Flagstaff", state: "AZ", neighborhood: "Downtown Flagstaff",
    lat: 35.2004, lng: -111.6519, tradition: "tibetan", location_type: "in-person",
    notes: "Tuesday Evening Meditation Class (6:30–7:45pm) at Beacon Unitarian Universalist Congregation, 510 N Leroux St, Flagstaff AZ 86001 (downtown). Outreach class from the International Kadampa Retreat Center Grand Canyon (Williams, AZ). Beginner-friendly guided meditation and Buddhist teaching; no experience needed. Cost: $10 / $5 students and seniors / free for monthly members. New Kadampa Tradition (NKT). meditationinnorthernarizona.org/flagstaff/.",
    source_url: "https://meditationinnorthernarizona.org/flagstaff/", event_url: "https://meditationinnorthernarizona.org/flagstaff/",
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
