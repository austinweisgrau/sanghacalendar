#!/usr/bin/env bun
/**
 * One-time Austin Phase 3 iCal ingest.
 * Seeds Kadampa Meditation Center Austin.
 * Run once to populate the live DB; ongoing ingest handled by coordinator.py / abraxis_ingest.py.
 */

import ical from "node-ical";
import crypto from "crypto";

const APP_URL      = "https://sangha-calendar.fly.dev";
const INGEST_TOKEN = (await Bun.file("/workspace/group/memory/sangha-ingest-token.txt").text()).trim();

const CENTERS = {
  kadampa_austin: {
    id: "kadampa_austin", name: "Kadampa Meditation Center Austin",
    url: "https://meditationinaustin.org",
    address: "7101 Easy Wind Drive, Unit 3108", city: "Austin", state: "TX", zip: "78752",
    neighborhood: "North Austin / Rundberg",
    lat: 30.3785, lng: -97.7115, tradition: "tibetan",
  },
};

const ICAL_FEEDS = {
  kadampa_austin: { url: "https://meditationinaustin.org/events/?ical=1", filterToSits: true },
};

const SIT_KEYWORDS = [
  "zazen","meditation","sit","sitting","dharma","satsang","mindfulness","vipassana","metta",
  "dzogchen","samadhi","kinhin","sangha","practice","retreat","sesshin","zazenkai",
  "chenrezi","shamatha","chanting","service","yoga","inquiry","dharma talk","recovery dharma",
  "open house","evening sit","morning sit","weekly","heart jewel","lamrim","tsog","puja",
  "empowerment","initiation","mahamudra","foundation program","general program",
];

const EXCLUDE_TITLE_KEYWORDS = [
  "workshop","training","webinar","conference","fundraiser","social",
  "party","festival","concert","performance","art show","exhibit","film","movie",
  "volunteer","cleanup","fundraising","gala","graduation","orientation",
  "board","committee","staff","administrative",
];

function isLikelySit(title, description) {
  const t = title.toLowerCase();
  const d = (description || "").toLowerCase();
  if (EXCLUDE_TITLE_KEYWORDS.some(kw => t.includes(kw))) return false;
  return SIT_KEYWORDS.some(kw => t.includes(kw) || d.includes(kw));
}

function detectLocation(title, description, location, url) {
  const all = [title, description, location, url].join(" ").toLowerCase();
  if (/zoom|online|virtual|livestream|webinar|stream/i.test(all)) {
    if (/in.?person|location|address|\d{4,}/i.test(all)) return "hybrid";
    return "online";
  }
  return "in-person";
}

function eventId(orgId, title, start) {
  return crypto.createHash("sha256").update(`${orgId}:${title}:${start}`).digest("hex").slice(0, 16);
}

const allEvents = [];
const today = new Date().toISOString().slice(0, 10);

for (const [orgId, feedCfg] of Object.entries(ICAL_FEEDS)) {
  const center = CENTERS[orgId];
  console.log(`Fetching ${center.name}...`);

  try {
    const resp = await fetch(feedCfg.url, { redirect: "follow" });
    const text = await resp.text();
    const parsed = await ical.async.parseICS(text);

    let count = 0;
    for (const comp of Object.values(parsed)) {
      if (comp.type !== "VEVENT") continue;

      let title         = (comp.summary || "").trim();
      const description = (comp.description || "").trim();
      const location    = (comp.location || "").trim();
      const eventUrl    = (comp.url || "").trim() || null;
      const dtstart     = comp.start;
      const dtend       = comp.end;

      if (!dtstart) continue;

      if (!title && description) {
        const firstLine = description.replace(/<[^>]+>/g, " ").split(/\n/)[0].trim().slice(0, 80);
        title = firstLine || `${center.name} Sit`;
      } else if (!title) {
        title = `${center.name} Sit`;
      }

      if (feedCfg.filterToSits && !isLikelySit(title, description)) continue;

      // Skip past events
      if (dtstart < new Date()) continue;

      const startStr = dtstart.toISOString().replace("Z", "");
      const endStr   = dtend ? dtend.toISOString().replace("Z", "") : null;

      // Use iCal location if it's a real address (not a URL), otherwise use center address
      let address = center.address;
      let city    = center.city;
      if (location && !/^https?:\/\//i.test(location) && location.includes(",")) {
        address = location;
        if (/Georgetown/i.test(location)) city = "Georgetown";
      }
      const locType = detectLocation(title, description, location, eventUrl || "");

      allEvents.push({
        id:             eventId(orgId, title, startStr),
        org_id:         orgId,
        org_name:       center.name,
        title,
        start_time:     startStr,
        end_time:       endStr,
        address,
        city,
        state:          center.state,
        neighborhood:   center.neighborhood,
        lat:            center.lat,
        lng:            center.lng,
        tradition:      center.tradition,
        location_type:  locType,
        is_sit:         true,
        accessibility_notes: null,
        identity_focus: null,
        source:         "ical_feed",
        source_url:     feedCfg.url,
        event_url:      eventUrl,
        last_verified:  today,
        recurrence:     null,
        notes:          description.slice(0, 300) || null,
      });
      count++;
    }
    console.log(`  → ${count} sits`);
  } catch (err) {
    console.error(`  ✗ Failed: ${err.message}`);
  }
}

console.log(`\nTotal events: ${allEvents.length}`);
if (allEvents.length === 0) {
  console.log("Nothing to post.");
  process.exit(0);
}

const postResp = await fetch(`${APP_URL}/api/admin/events`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${INGEST_TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ events: allEvents }),
});

if (!postResp.ok) {
  console.error(`POST failed: ${postResp.status} ${await postResp.text()}`);
  process.exit(1);
}

const result = await postResp.json();
console.log(`✓ ${result.upserted} events upserted`);
