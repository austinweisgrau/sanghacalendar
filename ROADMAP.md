# Sangha Calendar — Dev Roadmap

_Last updated: 2026-05-04 (heartbeat)_

## Current Status

**✅ Live at [sangha-calendar.fly.dev](https://sangha-calendar.fly.dev)**

- 370+ events in 30-day window, 25 organizations with sits
- 640 manual recurring sit instances seeded May 3 (27 sit definitions)
- Map view live at `/map` — all 25 centers pinned with tradition colors
- 25 center bio pages (centers.py now complete)
- City filter now includes all 11 cities (added Alameda, Kensington, Pleasant Hill, Richmond, Tiburon)
- Ingestion sources: 27 iCal feeds + manually-seeded recurring sits (27 definitions) + 45 Algolia (Spirit Rock) + 12 Momence (Berkeley Alembic) + Eventbrite (Nyingma, Insight Berkeley) + static HTML (Bay Zen, Berkeley Priory, Insight Berkeley)
- Coverage: East Bay (incl. Pleasant Hill/Contra Costa) + SF + Marin

---

## Phase Log

| Phase | Status | Description |
|-------|--------|-------------|
| 0 | ✅ Done | Repo scaffold, schema design, 16 East Bay centers mapped, local dev env |
| 1 | ✅ Done | Live iCal subscriptions (EBMC, IMC, SF Buddhist Center), basic calendar served on Fly.io |
| 1.5 | ✅ Done | Manually-seeded recurring sits (~50 centers), Spirit Rock Algolia scraper, Momence scraper, Abraxis weekly ingest pipeline, center bio pages, tradition colors, identity/online filters |
| 2 | 🔄 In progress | Non-iCal center scrapers (WordPress, Eventbrite, HTML) — see below |
| 3 | 📋 Queued | National expansion — top 10 metro areas |
| 4 | 📋 Queued | Full US coverage via discovery agent |
| 5 | 📋 Queued | Public launch features (ICS subscriptions, GCal deep links) |

---

## Active Work

### Bug: IMC Berkeley — missing events (iCal SUMMARY field empty)

✅ **Fixed May 1** — `ingestion/feeds/ical_feed.py` updated to fall back to first line of DESCRIPTION, then `"{org_name} Sit"` when SUMMARY is empty. Both sangha-ingest.js workaround and ical_feed.py now handle this. IMC Berkeley events will appear in next daily GH Actions ingest.

### Bug: abraxis_ingest enrichment silently failing (JSON markdown fences)

✅ **Fixed May 1** — `enrich_event()` in `abraxis_ingest.py` was failing to parse LLM responses because Haiku wraps JSON in markdown fences (```json...```). Added fence-stripping before `json.loads()`. Enrichment now works — location_type, identity_focus, and tradition overrides will apply correctly on next ingest.

---

### Phase 2: Non-iCal Center Scrapers

Priority order for East Bay centers not yet on live ingestion:

| Center | Approach | Difficulty | Status |
|--------|----------|------------|--------|
| Nyingma Institute | Eventbrite API | Low | ✅ **Live May 1** — `ingestion/scrapers/eventbrite.py` built and tested. Returns 6 upcoming events. Wired into coordinator.py (daily ingest) + abraxis_ingest.py. Uses `__NEXT_DATA__` JSON scraping, no API key needed. |
| Insight Berkeley | Eventbrite API + static HTML | Low-Med | ✅ **Live May 1** — Eventbrite (organizer_id: 32673197525) for retreats + static HTML scrape of insightberkeley.org/events for weekly Thursday sits at Berkeley Buddhist Monastery (23 events through Aug 2026, hybrid). |
| Empty Gate Zen | WordPress `?ical=1` test | Low | ❌ Site back up May 1 but calendar is JS-rendered Squarespace — `schedule` page returns empty div (143 chars). No `__NEXT_DATA__`, no date fields. Would need headless browser. Skip for now; note in Phase 4. |
| Everyday Zen | WordPress `?ical=1` | Low | ✅ **Live** — added Apr 29. 21 events ingested (Weekly Metta Sitting, Group Recitation, All-Day Sittings, Everyday Caring). Hybrid/online focus; meets at Community Congregational Church in Tiburon. Note: EXCL_KW filter updated to title-only to avoid WordPress description noise. |
| Metta Dharma | WordPress `?ical=1` test | Low | ❌ No iCal — `?ical=1` returns homepage HTML (different events plugin or no plugin) |
| Bay Zen | LLM-assisted HTML scrape | Med | ✅ **Live May 1** — Squarespace calendar. 4 upcoming events (2 sesshin, 2 zazenkai). Wired into coordinator.py + abraxis_ingest.py. |
| Berkeley Priory | LLM-assisted HTML scrape | Med | ✅ **Live May 1** — WordPress text calendar. 19 upcoming events (meditations, retreats, ceremonies through Jul 2026). OBC Soto Zen. |
| Berkeley Buddhist Monastery | Research complete | — | ✅ **No action needed** — James Baraz Thursday sits are covered via Insight Berkeley (insightberkeley.org). Steven Tainer Wednesday sits are Zoom-only (series ends May 13). BBM's own site is Weebly with broken/JS-rendered calendar. Daily sits (Thu/Fri 6:15am, daily 5:15pm) already seeded as recurring. |
| Berkeley Zen Center | iCal feed + recurring sits | — | ✅ **Live May 2** — `/my-calendar-ics/` feed (18 special events: sesshins, half-day sittings, dharma talks). Daily zazen seeded as recurring (Mon–Sat 6am, Mon–Fri 5:40pm, Wed 7:10pm drop-in). One of most historically significant Soto Zen centers in North America. |
| Orgyen Dorje Den | iCal feed | Low | ✅ **Wired May 2**, ✅ **Resolved May 3** — 0 events visible (all `is_sit=0`) and that's correct. Verified: no regular sitting meditation open to general public. Programs are Vajrayana sadhanas, tsog pujas, and lineage practices (Ngondro-based). Only in-person events are monthly tsog days (already in DB). Accept as-is — tsog ≠ sit. Address: 2244 Santa Clara Ave, Alameda. |
| Ewam Choden | Recurring sit | Low | ✅ **Live May 2** — Weekly Sunday 10am sit seeded. Oldest Tibetan Buddhist center in Western hemisphere (1971, Sakya). No structured calendar online. |
| IMC New Berkeley Monday Group | Recurring sit | Low | ✅ **Live May 2** — Weekly Monday 7pm sit seeded at Berkeley Finnish Hall (1970 Chestnut St). New satellite group of IMC; intro class through May 18, open sitting from May 25. |

**Remaining research targets (lower priority):**

| Center | Notes |
|--------|-------|
| Dharmata Foundation (Richmond) | ✅ **Added May 2** — Public Google Calendar iCal feed. 10 upcoming events: monthly Anam Thubten teachings (hybrid in-person + Zoom), occasional retreats. Will appear in next weekly ingest (Mon May 4). |
| Karuna Buddhist Vihara — East Bay (Berkeley) | ✅ **Added May 3** — Monthly Saturday sits (mostly 2nd Saturday) at 1438 Neilson St, Berkeley (Westbrae). 3–5pm, guided meditation + Dhammapada reading/discussion. Hybrid in-person + Zoom. Specific 2026 dates seeded (karunabv.org/eastbay-dhamma.html). Needs annual date refresh (dates published on their site each year). |
| Mount Diablo Zen Group (Pleasant Hill) | ✅ **Added May 3** — Weekly Wednesday 7pm hybrid zazen. 404 Gregory Lane, Room 9, Pleasant Hill. Soto Zen (SZBA member). In-person 1st/3rd/5th Wednesdays, Zoom 2nd/4th Wednesdays. Drop-in, free. |
| Berkeley Buddhist Vihara | ❌ **Skip** — Sri Lankan Theravada temple at 6200 Columbia Ave, Richmond. Functions primarily as a community temple (puja services, children's Sinhala school, ceremonies). No public meditation sits offered to general public. |

**Scraper targets in codebase:**
- `ingestion/scrapers/eventbrite.py` ✅ — live, Nyingma + Insight Berkeley wired in
- `ingestion/scrapers/static_html.py` ✅ — live, Bay Zen + Berkeley Priory + Insight Berkeley wired in. LLM (Claude Haiku) extracts events from arbitrary HTML calendar pages. Text cap: 16k chars / 4k tokens output.
- `ingestion/utils.py` ✅ — shared classification helpers (detect_location_type, is_likely_sit)
- `ingestion/scrapers/wordpress_events.py` — not yet created (may not be needed; static_html handles WP text calendars)
- `ingestion/scrapers/squarespace.py` — not yet created (static_html handles Squarespace too)

---

### GCal Integration Button

Placeholder is live in the UI. Feature pending:
- Generate `https://calendar.google.com/calendar/r?cid=...` deep links for filtered views
- Requires serving a stable per-filter ICS URL first (see Phase 5)

---

## Phase 3 — National Expansion

Target: top 10 US metro areas by Buddhist population + center density.

Candidate metros (rough priority):
1. Bay Area ✅ (in progress)
2. NYC
3. LA
4. Boston/Cambridge
5. DC
6. Chicago
7. Seattle
8. Denver/Boulder
9. Austin
10. Portland

**Approach:** Abraxis monthly ingest cadence per metro once added. Research doc per metro in `memory/`. Start with centers already well-documented online (Spirit Rock → national Vipassana network is a good model).

---

## Phase 4 — Discovery Agent

Build out the full agent swarm from `coordinator/`:
- `discovery_agent.py` — find new centers via Google Maps, directories, web search
- `scraper_agent.py` — extract events from any center web presence
- `classifier_agent.py` — filter: is this an actual sit?
- `normalizer_agent.py` — map to canonical schema

Goal: submit a URL (or just a city name) and get back a list of verified, normalized sits. This is what enables Phase 4 national scale.

---

## Phase 5 — Public Launch Features

- [x] **ICS subscription URLs** — `/feed.ics` with same filter params as `/api/events` (city, tradition, location_type, days). Calendar name adapts to active filters. ✅ **Live May 4**
- [x] **GCal / Apple Calendar deep links** — Subscribe buttons in header, update dynamically as filters change. GCal uses `?cid=` deep link; Apple Calendar uses `webcal://`. ✅ **Live May 4**
- [x] **Map view** — `/map` route with Leaflet.js, all 25 centers as color-coded tradition pins. Popup shows upcoming sits + center info link. Supports tradition/location/days filters. ✅ **Live May 4**
- [x] **Donate button** — ko-fi link in footer. ✅ **Live May 4**
- [ ] **Email digest** — weekly "sits near you" for subscribers
- [ ] **Custom domain** — ~$12/year, worth it for public launch
- [x] **Submission form** — `/submit` page with name/city/website/tradition/notes fields. POST to `/api/submit`, stored in `center_submissions` SQLite table. Admin view at `/api/admin/submissions` (requires INGEST_TOKEN). "Submit a center" link in footer. ✅ **Live May 4**

---

## Infrastructure Notes

### Hosting
- **Fly.io** — `sangha-calendar` app, sjc region
- 256MB shared CPU, persistent SQLite on `/data` volume
- ~$2/month
- **Scaling path:** Postgres when hitting 100k+ events (unsolved but cheap)

### Ingestion Cadence
- **Daily (GitHub Actions):** iCal feeds only — zero-maintenance, structured data
- **Weekly (Abraxis, Mon 8am PT):** Bay Area enrichment + Phase 2 scraping + recurring sit refresh
- **Quarterly:** Re-seed all manually-maintained recurring sits (90-day window)
- **Monthly (future):** Other metros

### LLM Usage
- Model: `claude-haiku-4-5-20251001`
- Cost: ~$0.01/week Bay Area scale; ~$5–10/year at full national scale
- Used only for: location_type classification, is_sit detection, identity focus extraction on ambiguous events

### Shambhala Berkeley iCal
- `shambhala-koeln.de/ical.php?center=178` has been timing out for weeks (Apr 2026)
- Manual recurring sits still in DB; removed from automated feed
- Monitor: if Shambhala network restores this endpoint, re-add to automated feeds

---

## Research Docs

| File | Contents |
|------|----------|
| `memory/research-eastbay-meditation-calendar.md` | 16 East Bay centers, Phase 1–4 breakdown, notes per center |
| `memory/research-east-bay-buddhist-calendar-aggregation.md` | Detailed center registry, iCal URLs, scraping difficulty ratings |
| `memory/research-sf-marin-meditation-calendar.md` | SF + Marin expansion (10 centers, pipeline summary) |
| `journals/llm/abraxis-proposals/sangha-calendar-imc-missing-title-bug.md` | IMC Berkeley bug report + fix spec |
