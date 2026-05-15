#!/usr/bin/env bun
/**
 * Sangha Calendar — Abraxis ingestion script (bun)
 * Fetches iCal feeds, enriches with Claude, POSTs to Fly app.
 */

import ical from "node-ical";

const APP_URL      = "https://sangha-calendar.fly.dev";
const INGEST_TOKEN = Bun.file("/workspace/group/memory/sangha-ingest-token.txt").text().then(t => t.trim());
const API_KEY      = process.env.ANTHROPIC_SDK_API_KEY;

// ── Center definitions ──────────────────────────────────────────────────────

// ── Eventbrite sources ───────────────────────────────────────────────────────
// Uses __NEXT_DATA__ JSON scraping — no API key required.

const EVENTBRITE_CENTERS = {
  nyingma_institute: {
    id: "nyingma_institute", name: "Nyingma Institute",
    url: "https://www.nyingmainstitute.com",
    address: "1815 Highland Pl", city: "Berkeley", state: "CA", zip: "94709",
    neighborhood: "North Berkeley", tradition: "tibetan",
    lat: 37.8781, lng: -122.2607,
  },
  insight_berkeley: {
    id: "insight_berkeley", name: "Insight Meditation Community of Berkeley",
    url: "https://www.insightberkeley.org",
    address: "2304 McKinley Ave", city: "Berkeley", state: "CA", zip: "94703",
    neighborhood: "North Berkeley", tradition: "theravada",
    lat: 37.8758, lng: -122.2637,
  },
};

const EVENTBRITE_FEEDS = {
  nyingma_institute: { organizerId: "336367203", filterToSits: false },
  insight_berkeley: { organizerId: "32673197525", filterToSits: true },
};

// ── iCal sources ─────────────────────────────────────────────────────────────

const CENTERS = {
  imc_berkeley: {
    id: "imc_berkeley", name: "Insight Meditation Center",
    url: "https://www.insightmeditationcenter.org",
    address: "1205 Hopkins St", city: "Berkeley", state: "CA", zip: "94702",
    neighborhood: "West Berkeley", tradition: "theravada",
    lat: 37.8789, lng: -122.2865,
  },
  ebmc: {
    id: "ebmc", name: "East Bay Meditation Center",
    url: "https://eastbaymeditation.org",
    address: "285 17th St", city: "Oakland", state: "CA", zip: "94612",
    neighborhood: "Uptown Oakland", tradition: "pluralist",
    lat: 37.8076, lng: -122.2697,
    notes: "Justice-oriented, identity-centered practice. Many affinity sanghas.",
  },
  shambhala_berkeley: {
    id: "shambhala_berkeley", name: "Berkeley Shambhala Center",
    url: "https://berkeley.shambhala.org",
    address: "2288 Fulton St", city: "Berkeley", state: "CA", zip: "94704",
    neighborhood: "South Campus Berkeley", tradition: "tibetan",
    lat: 37.8696, lng: -122.2677,
  },
  sf_buddhist_center: {
    id: "sf_buddhist_center", name: "San Francisco Buddhist Center",
    url: "https://sfbuddhistcenter.org",
    address: "37 Belcher St", city: "San Francisco", state: "CA", zip: "94114",
    neighborhood: "Castro", tradition: "pluralist",
    lat: 37.7649, lng: -122.4327,
    notes: "Triratna Buddhist Community. Identity-affirming — LGBTQ+ and BIPOC programs.",
  },
  everyday_zen: {
    id: "everyday_zen", name: "Everyday Zen Foundation",
    url: "https://everydayzen.org",
    address: "145 Rock Hill Rd", city: "Tiburon", state: "CA", zip: "94920",
    neighborhood: "Tiburon / Marin", tradition: "zen",
    lat: 37.8816, lng: -122.4577,
    notes: "Soto Zen lineage (Norman Fischer). Weekly Metta Sittings, sutra recitation, all-day sittings. Meets at Community Congregational Church in Tiburon; many events hybrid or online.",
  },
};

const ICAL_FEEDS = {
  imc_berkeley: {
    url: "https://calendar.google.com/calendar/ical/f2671ba813e15027485f84235a37074c4d3a113cc0135f83f46212744f55dc09%40group.calendar.google.com/public/basic.ics",
  },
  ebmc: {
    url: "https://eastbaymeditation.org/?ical=1&eventDisplay=list",
  },
  shambhala_berkeley: {
    url: "http://shambhala-koeln.de/ical.php?center=178",
  },
  sf_buddhist_center: {
    url: "https://sfbuddhistcenter.org/events/?ical=1",
  },
  everyday_zen: {
    url: "https://everydayzen.org/?ical=1",
  },
};

// ── iCal helpers ─────────────────────────────────────────────────────────────

const SIT_KW = ["sit","zazen","sitting","meditation","vipassana","samadhi","open practice","drop-in","morning sit","evening sit","daily sit","meditation group","sangha sit"];
const EXCL_KW = ["retreat","sesshin","workshop","dharma talk","lecture","seminar","course","class","training","daylong","ceremony","social","book club","study group","teacher training","orientation"];
const ONLINE_KW = ["online","virtual","zoom","webinar","livestream","live stream","google meet","teams","remote"];
const HYBRID_KW = ["hybrid","in-person and online","online and in-person"];

function isLikelySit(title, desc = "") {
  // Exclusion check on title only — descriptions can contain noisy HTML/template
  // text (WordPress shortcodes, nav links) that trips false positives.
  const titleLower = title.toLowerCase();
  const fullText   = (title + " " + desc).toLowerCase();
  if (EXCL_KW.some(k => titleLower.includes(k))) return false;
  return SIT_KW.some(k => fullText.includes(k));
}

function detectLocation(title, desc = "", location = "", eventUrl = "") {
  const urlPath = (() => { try { return new URL(eventUrl).pathname; } catch { return ""; } })();
  const t = (title + " " + desc + " " + location + " " + urlPath).toLowerCase();
  if (HYBRID_KW.some(k => t.includes(k))) return "hybrid";
  if (["zoom.us","meet.google","teams.microsoft"].some(k => location.toLowerCase().includes(k))) return "online";
  if (ONLINE_KW.some(k => t.includes(k))) return "online";
  return null; // uncertain — ask Claude
}

function eventId(orgId, title, start) {
  const raw = `${orgId}:${title}:${start}`;
  // Simple hash using bun's built-in crypto
  const hash = require("crypto").createHash("sha256").update(raw).digest("hex");
  return hash.slice(0, 16);
}

// ── Claude enrichment ─────────────────────────────────────────────────────────

async function enrichWithClaude(events) {
  if (!API_KEY) { console.warn("No ANTHROPIC_SDK_API_KEY — skipping enrichment"); return events; }

  console.log(`  Enriching ${events.length} events with Claude Haiku...`);
  const enriched = [];

  for (const e of events) {
    const prompt = `Classify this meditation event. Return JSON only, no markdown.

org: ${e.org_name}
title: ${e.title}
location field: ${e.address || ""} ${e.city || ""}
event url: ${e.event_url || "(none)"}
notes/description: ${(e.notes || "").slice(0, 400)}

Return exactly:
{"location_type":"in-person"|"online"|"hybrid","is_sit":true|false,"identity_focus":"<group or null>","tradition":"theravada"|"zen"|"tibetan"|"secular"|"pluralist"|"other"|"unknown"}

Rules:
- location_type "online" if primary attendance is via video even if venue listed
- is_sit true only if sitting meditation is PRIMARY activity
- identity_focus: BIPOC, LGBTQ+, women, disabled, etc — or null
- tradition: best match`;

    try {
      const resp = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "x-api-key": API_KEY,
          "anthropic-version": "2023-06-01",
          "content-type": "application/json",
        },
        body: JSON.stringify({
          model: "claude-haiku-4-5-20251001",
          max_tokens: 150,
          messages: [{ role: "user", content: prompt }],
        }),
      });
      const data = await resp.json();
      const raw = data.content[0].text.trim().replace(/^```(?:json)?\n?/, "").replace(/\n?```$/, "");
      const result = JSON.parse(raw);
      enriched.push({
        ...e,
        location_type:  result.location_type  ?? e.location_type,
        is_sit:         result.is_sit          ?? e.is_sit,
        identity_focus: result.identity_focus  ?? null,
        tradition:      result.tradition       ?? e.tradition,
      });
    } catch (err) {
      console.warn(`  ⚠ Enrichment failed for "${e.title}": ${err.message}`);
      enriched.push(e);
    }
  }

  return enriched;
}

// ── Eventbrite scraper ────────────────────────────────────────────────────────

function extractEventbriteEvents(nextData) {
  const events = [];
  function search(obj, depth = 0) {
    if (depth > 10) return;
    if (Array.isArray(obj)) { obj.forEach(item => search(item, depth + 1)); return; }
    if (obj && typeof obj === "object") {
      // Format: flat start_date + start_time (from __NEXT_DATA__ organizer page)
      if ("start_date" in obj && "start_time" in obj && "name" in obj) {
        events.push(obj);
        return;
      }
      // Format: nested start.local (API v3 style)
      if ("name" in obj && obj.start && typeof obj.start === "object" && "local" in obj.start) {
        events.push(obj);
        return;
      }
      Object.values(obj).forEach(v => search(v, depth + 1));
    }
  }
  search(nextData);
  return events;
}

async function fetchEventbriteOrganizer(orgId, feedCfg, today) {
  const center = EVENTBRITE_CENTERS[orgId];
  const url = `https://www.eventbrite.com/o/${feedCfg.organizerId}/`;
  const resp = await fetch(url, {
    headers: {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    },
  });
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  const html = await resp.text();

  const match = html.match(/<script[^>]+id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
  if (!match) throw new Error("No __NEXT_DATA__ found");

  const nextData = JSON.parse(match[1]);
  const rawEvents = extractEventbriteEvents(nextData);

  const events = [];
  for (const raw of rawEvents) {
    // Build ISO datetime from flat or nested fields
    let startStr, endStr;
    if (raw.start && typeof raw.start === "object") {
      startStr = raw.start.local || raw.start.utc;
      endStr = raw.end && (raw.end.local || raw.end.utc);
    } else {
      const sd = raw.start_date || "";
      const st = raw.start_time || "";
      startStr = sd && st ? `${sd}T${st}` : sd || null;
      const ed = raw.end_date || "";
      const et = raw.end_time || "";
      endStr = ed && et ? `${ed}T${et}` : ed || null;
    }
    if (!startStr) continue;

    // Skip past events
    const startDt = new Date(startStr);
    if (isNaN(startDt) || startDt < new Date()) continue;

    const title = typeof raw.name === "object" ? (raw.name.text || "") : (raw.name || raw.summary || "");
    if (!title) continue;

    if (feedCfg.filterToSits && !isLikelySit(title, raw.summary || "")) continue;

    const description = typeof raw.description === "object"
      ? (raw.description.text || "")
      : (raw.description || raw.summary || "");

    const locType = detectLocation(title, description, "", raw.url || "");

    events.push({
      id:             eventId(orgId, title, startStr),
      org_id:         orgId,
      org_name:       center.name,
      title,
      start_time:     startStr,
      end_time:       endStr || null,
      address:        center.address,
      city:           center.city,
      state:          center.state,
      neighborhood:   center.neighborhood,
      lat:            center.lat,
      lng:            center.lng,
      tradition:      center.tradition,
      location_type:  raw.is_online_event ? "online" : (locType || "in-person"),
      _location_certain: raw.is_online_event !== undefined,
      is_sit:         !feedCfg.filterToSits || isLikelySit(title, description),
      accessibility_notes: null,
      identity_focus: null,
      source:         "eventbrite",
      source_url:     url,
      event_url:      raw.url || null,
      last_verified:  today,
      recurrence:     null,
      notes:          description.slice(0, 300) || null,
    });
  }
  return events;
}

// ── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  const token = await INGEST_TOKEN;
  const today = new Date().toISOString().slice(0, 10);
  const allEvents = [];

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

        // Some calendars (e.g., IMC Berkeley Google Calendar) export events without SUMMARY.
        // Fall back to first line of description, then org name + "Sit".
        if (!title && description) {
          const firstLine = description.replace(/<[^>]+>/g, " ").split(/\n/)[0].trim().slice(0, 80);
          title = firstLine || `${center.name} Sit`;
        } else if (!title) {
          title = `${center.name} Sit`;
        }
        if (!isLikelySit(title, description)) continue;

        // Skip past events
        if (dtstart < new Date()) continue;

        const startStr = dtstart.toISOString().replace("Z", "");
        const endStr   = dtend ? dtend.toISOString().replace("Z", "") : null;
        const locType  = detectLocation(title, description, location, eventUrl || "");

        allEvents.push({
          id:             eventId(orgId, title, startStr),
          org_id:         orgId,
          org_name:       center.name,
          title,
          start_time:     startStr,
          end_time:       endStr,
          address:        center.address,
          city:           center.city,
          state:          center.state,
          neighborhood:   center.neighborhood,
          lat:            center.lat,
          lng:            center.lng,
          tradition:      center.tradition,
          location_type:  locType || "in-person", // Claude will refine uncertain ones
          _location_certain: locType !== null,
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

  // Fetch Eventbrite sources
  for (const [orgId, feedCfg] of Object.entries(EVENTBRITE_FEEDS)) {
    const center = EVENTBRITE_CENTERS[orgId];
    console.log(`Fetching ${center.name} (Eventbrite)...`);
    try {
      const events = await fetchEventbriteOrganizer(orgId, feedCfg, today);
      console.log(`  → ${events.length} events`);
      allEvents.push(...events);
    } catch (err) {
      console.error(`  ✗ Failed: ${err.message}`);
    }
  }

  console.log(`\nTotal before enrichment: ${allEvents.length}`);

  // Enrich with Claude
  const enriched = await enrichWithClaude(allEvents);

  // Strip internal field before POST
  const toPost = enriched.map(({ _location_certain, ...e }) => e);

  // POST to app
  console.log(`\nPosting to ${APP_URL}...`);
  const postResp = await fetch(`${APP_URL}/api/admin/events`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ events: toPost }),
  });

  if (!postResp.ok) {
    console.error(`POST failed: ${postResp.status} ${await postResp.text()}`);
    process.exit(1);
  }

  const result = await postResp.json();
  console.log(`\n✓ ${result.upserted} events upserted`);
}

main().catch(e => { console.error(e); process.exit(1); });
