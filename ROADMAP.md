# Sangha Calendar — Dev Roadmap

_Last updated: 2026-05-07 (heartbeat 11)_

## Current Status

**✅ Live at [sangha-calendar.fly.dev](https://sangha-calendar.fly.dev)**

- 500+ events in 30-day window (500 cap), 36 organizations
- 640 manual recurring sit instances seeded May 3 (27 sit definitions)
- Map view live at `/map` — all centers pinned with tradition colors
- 28 center bio pages (centers.py complete)
- City filter includes 11 cities (Alameda, Kensington, Pleasant Hill, Richmond, Tiburon + more)
- Ingestion sources: 30 iCal feeds + manually-seeded recurring sits + 45 Algolia (Spirit Rock) + 12 Momence (Berkeley Alembic) + Eventbrite (Nyingma, Insight Berkeley, Tibet House US) + static HTML (Bay Zen, Berkeley Priory, Insight Berkeley, ZCNYC)
- Coverage: East Bay (incl. Pleasant Hill/Contra Costa) + SF + Marin + NorCal Plum Village network

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
| Green Gulch Farm / SFZC Marin (Muir Beach) | ✅ **Added May 4** — No iCal (SFZC Drupal 10, no ical endpoint). Seeded as recurring sits: morning zazen 6am Mon/Wed–Sun, evening zazen 7:50pm Wed–Sat, Sunday Morning Program 9:30am (hybrid). 56 events in 90-day window. |
| San Francisco Shambhala Center (SF — Glen Park) | ✅ **Added May 4 (heartbeat 4)** — iCal server (shambhala-koeln.de center=177) still dead. Manually seeded from website: 2nd/4th Wed 7pm Beginners Night (in-person), 3rd Sat 9am (in-person), 1st/2nd Sun 10am (online). 12 events in 90-day window. Added to centers.py bio + east_bay.py CENTERS. |

### Bug: SF Buddhist Center missing from daily GH Actions ingest

✅ **Fixed May 4 (heartbeat 5)** — `sf_buddhist_center` was in `sangha-ingest.js` (weekly only) but not in `ingestion/sources/east_bay.py`. Added to both `CENTERS` and `ICAL_FEEDS` in east_bay.py. Now picked up by daily `coordinator.py` via GH Actions. Feed verified: `sfbuddhistcenter.org/events/?ical=1` returns valid iCal (WP Events Calendar 7.2.3.1), 17 upcoming events including drop-in sits, morning meditations, Sangha nights, and identity-specific sits.

### NorCal Sangha Community (Plum Village Bay Area network)

✅ **Added May 5** — `https://norcalsangha.org/events/?ical=1` added to east_bay.py ICAL_FEEDS. WordPress Events Calendar plugin. Monthly Days of Mindfulness (frequently at EBMC Oakland and Shantideva Monastery, Castro Valley) + special retreats. Added center bio to centers.py. 28 orgs total.

Note: NorCal Sangha events span multiple Bay Area and NorCal locations. Events outside the Bay Area (Deer Park Monastery in Escondido, etc.) will be filtered by EXCLUDE_KEYWORDS ("retreat") or LLM classification.

### Research: Mangalam Research Center (Berkeley)

❌ **Skip** — Calendar shows "No event found." Academic courses/lectures only, no public meditation sits. Not a fit for sangha calendar.

### Research: Empty Gate Zen Google Calendar

❌ **Blocked** — Website mentions "Check the Google Calendar above for live updates" but the embed is dynamically loaded (JavaScript-rendered). No static iCal URL or calendar ID accessible via HTTP. Would need headless browser. Defer to Phase 4. Recurring sits (Mon 7pm + Sat 8am) are already seeded.

---

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
1. Bay Area ✅ (complete — 28 centers)
2. NYC ✅ **Phase 3 complete May 5** (8 centers)
3. LA 🔄 **Phase 3 LA live May 5** (2 centers) — see below
4. Boston/Cambridge 🔄 **Phase 3 Boston live May 6** (5 centers) — see below
5. DC 🔄 **Phase 3 DC live May 6** (2 centers) — see below
6. Chicago 🔄 **Phase 3 Chicago live May 6** (15+ centers via Tockify aggregator)
7. Seattle 🔄 **Phase 3 Seattle live May 7** (5 centers) — see below
8. Denver/Boulder 🔄 **Phase 3 Denver/Boulder live May 7** (5 centers) — see below
9. Austin
10. Portland

**Approach:** Abraxis monthly ingest cadence per metro once added. Research doc per metro in `memory/`. Start with centers already well-documented online (Spirit Rock → national Vipassana network is a good model).

### NYC Phase 3a — ✅ Live May 5 (3 centers)

| Center | iCal URL | Tradition | Status |
|--------|----------|-----------|--------|
| NY Insight Meditation Center (NYIMC) | `nyimc.org/events/?ical=1` | Theravada | ✅ Live |
| Brooklyn Zen Center | `brooklynzen.org/?ical=1` | Soto Zen | ✅ Live |
| Kadampa NYC (meditationinnewyork.org) | `meditationinnewyork.org/events/?ical=1` | Tibetan (NKT) | ✅ Live |

`ingestion/sources/nyc.py` + `run_nyc_phase3a()` in coordinator + abraxis. City filter updated (Manhattan, Brooklyn, Muir Beach). Events appear after next daily GH Actions ingest.

### NYC Phase 3b — ✅ Live May 5 (3 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Shambhala NYC | Parse `const eventsDatas` JSON from `ny.shambhala.org/calendar/` | ✅ Live (119 events) |
| NYZCCC (zencare.org) | Seeded stable schedule | ✅ Live (182 events: Mid-Day Zazen + Sun/Mon/Wed sits) |
| Tibet House US | Eventbrite + seeded Lunchtime Meditation | ✅ Live (Mon-Fri 1pm online seeded; Eventbrite wired for ticketed events) |

### NYC Phase 3c — ✅ Live May 5 (2 centers)

| Center | Approach | Status |
|--------|----------|--------|
| New York Zendo Shobo-Ji (Zen Studies Society) | iCal feed (`zenstudies.org/events/new-york-zendo-calendar/?ical=1`) with "NYZ:"/"DBZ:"/"Online:" prefix stripping | ✅ Live — `fetch_zenstudies_nyc()` in nyc.py. Daily zazen + Sunday service seeded. |
| ZCNYC / Fire Lotus Temple | LLM-assisted static HTML scrape of `zcnyc.org/calendar/` | ✅ Live — in `STATIC_HTML_FEEDS`. Sunday Morning Program + LGBTQIA+ sits seeded. |

### LA Phase 3 — ✅ Live May 5 (2 centers)

| Center | Approach | Status |
|--------|----------|--------|
| InsightLA (Santa Monica) | Schema.org Event HTML parser — `/fullcalendar/` page is server-side rendered with structured markup | ✅ Live — `fetch_insightla()` in la.py. ~18 events/page (online morning sits, Santa Monica Dharma Nights, Recovery Dharma, Qigong, MBSR classes). 2 pages fetched. |
| Zen Center of Los Angeles (Koreatown) | LLM-assisted static HTML scrape of `zcla.org/calendars/` | ✅ Wired into STATIC_HTML_FEEDS in la.py. Will pick up on next Abraxis weekly run. |

City filter updated: "Santa Monica (LA)" and "Los Angeles (LA)" added to index.html.
Center bios added to centers.py for insightla + zcla.

**Skipped for now:**
- Shambhala LA (`shambhala-koeln.de/ical.php?center=208`) — Cologne server unreachable (same issue as Berkeley center=178)
- Kadampa LA (`meditationinlosangeles.org`) — site down/offline
- Against the Stream (`againstthestream.com`) — Squarespace, no iCal, retreat-focused

### Boston Phase 3 — ✅ Live May 6 (5 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Boston Shambhala Meditation Center (Brookline) | iCal feed — `shambhala-koeln.de/ical.php?center=204` (confirmed working unlike center=178/208) | ✅ Live — wired in coordinator + abraxis. Weekly events: Nyinthün, Dharma Gathering, Heart of Recovery, LGBTQ+ sit, Shambhala Training weekends. |
| Greater Boston Zen Center (Central Square, Cambridge) | Recurring sits seeded — Google Calendar feed is stale/historical | ✅ Live — Tue 7pm hybrid, Sat 9am online. ~130 events in 90-day window. |
| Cambridge Insight Meditation Center / CIMC (Cambridge) | Recurring sits seeded — FullCalendar JS-rendered, no iCal endpoint | ✅ Live — Mon 6pm Sitting & Sangha + Tue/Thu/Fri 6pm Evening Sit. ~250 events in 90-day window. |
| Cambridge Zen Center (Cambridge) | Recurring sits seeded — site is Squarespace with no iCal | ✅ Live — Tue 7:30pm hybrid + Sun 9am hybrid. ~180 events in 90-day window. |
| Kadampa Meditation Center Boston (Cambridge) | Recurring sits seeded — Squarespace, no iCal | ✅ Live — Wed 7pm + Sun 11am in-person. ~180 events in 90-day window. |

City filter updated: Cambridge, Brookline, Boston added (MA state).
Center bios added to centers.py for all 5 centers.
1233 total recurring sit instances seeded (was ~900 before Boston).

**Skipped/deferred:**
- CIMC iCal: uses FullCalendar JS, no API endpoint — monitor for future fix
- Barre Center for Buddhist Studies: rural retreat center (Barre, MA), not urban metro

### DC Phase 3 — ✅ Live May 6 (2 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Insight Meditation Community of Washington (IMCW) | Custom EventAgent API scraper — fetch ea-key from HTML, call `api.eventagent.ai/api/ListView`, expand RRULE for recurring events | ✅ Live — `fetch_imcw()` in dc.py. River Road Drop-in (Wed 7pm, Bethesda hybrid), Vienna Drop-in (Sun 9am, Vienna VA hybrid), Midday Meditation (Tue/Thu/Fri 1pm online), Heartfelt Wisdom (Thu 9am online), plus special events at DC venues. 81 events live. |
| Shambhala Meditation Center of Washington DC | Recurring sit seeded — iCal (shambhala-koeln.de center=205) is down (522) | ✅ Live — 1st Sunday monthly 1:30pm at Seekers Church (276 Carroll St NW, Takoma DC). |

City filter updated: Washington, Bethesda, Arlington, Vienna added with DC state option (auto-selects all since metro spans DC/MD/VA).
Center bios added for IMCW + DC Shambhala.

**Skipped/deferred:**
- DC Shambhala iCal: shambhala-koeln.de server down (522) for all centers — monitor for recovery
- Washington Buddhist Vihara (16th St NW): broken website, dead SSL cert, no calendar — skip
- Meditation Center DC (Dhammakaya, Alexandria VA): AJAX-only calendar, Dhammakaya tradition — low priority
- Kadampa DC: no accessible web presence found

### Chicago Phase 3 — ✅ Live May 6 (15+ centers)

Primary source: **Sit Around Chicago** Tockify aggregator iCal at
`https://tockify.com/api/feeds/ics/sitaroundchicagocalendar` — a community-maintained
calendar covering 15+ Chicago-area Buddhist centers in a single feed. 1466 events
upserted (90-day window across all centers).

| Center | Tradition | Notes |
|--------|-----------|-------|
| Ancient Dragon Zen Gate (Ravenswood) | Soto Zen | SFZC lineage, daily online zazen |
| Daiyuzenji Rinzai Zen Temple (Ravenswood) | Rinzai Zen | Tue/Thu 7pm, Fri 5:30am, Sun 8:30am |
| Zen Buddhist Temple of Chicago (Evanston) | Soto Zen | Oldest Chicago Zen center, founded 1949 |
| Shambhala Meditation Center of Chicago (West Loop) | Tibetan/Shambhala | Sun/Tue sits, Queer Dharma |
| Chicago Buddhist Meditation Group (Ravenswood) | Pluralist | Sun 3:30pm hybrid |
| Chicago Zen Meditation Community (West Town) | Soto Zen | 8 sessions/week hybrid |
| Insight Chicago Meditation Community | Theravada | Multiple sanghas citywide |
| Dharma Drum Mountain | Chan/Zen | Tai chi, Chan workshops |
| Diamond Way Buddhist Center Chicago | Tibetan | Diamond Way lineage |
| Great Plains Zen Center (Palatine) | Zen | NW suburb, online sessions |
| Bultasa Buddhist Temple | Korean Zen | Wednesday evenings |
| Won Buddhism of Chicago | Won Buddhism | Korean won-Buddhist tradition |
| Ten Directions Zen Community | Zen | — |
| Zen Life & Meditation Center | Zen | — |
| + others from Tockify aggregator | various | — |

**Implementation:** `ingestion/sources/chicago.py` — `fetch_tockify_chicago()` parses
Tockify multi-center iCal with "CenterName: Title" SUMMARY format. Fixes Tockify's
malformed `P15M` duration header. City parsed from LOCATION field.

City filter: Illinois state + Chicago/Evanston/Oak Park/Palatine cities.
Center bios added for 7 key Chicago centers.

**Skipped/deferred:**
- Kadampa Chicago (meditateinchicago.org): Wix-based, no iCal. Eventbrite possible future add.

### Seattle Phase 3 — ✅ Live May 7 (5 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Seattle Insight Meditation Society | iCal feed (`seattleinsight.org/events/?ical=1`) | ✅ Live — 27 events |
| KMC Washington (Kadampa Seattle) | iCal feed (`meditateinseattle.org/events/?ical=1`, Chrome UA required) | ✅ Live — 25 events |
| Nalandabodhi Seattle (Nalanda West) | iCal feed (`nalandabodhi.org/?ical=1`, filtered to "Nalandabodhi Seattle"/"Nalanda West" in LOCATION) | ✅ Live — 5 events |
| Shambhala Meditation Center of Seattle | Recurring sits seeded — Cloudflare blocks iCal, HTML scraping viable but deferred | ✅ Live — Thu 7pm, Sun 10am in-person; Mon 6:30pm online; Wed 7pm hybrid |
| Seattle Buddhist Center (Triratna) | Recurring sits seeded — no iCal, static schedule page | ✅ Live — Thu 7pm, Sun 6pm in-person |

City filter: Washington state + Seattle city added to `_filters.html`.
Center bios: 5 new entries in `centers.py`.
`ingestion/sources/seattle.py` created with `fetch_nalandabodhi_seattle()` custom scraper.

**Skipped/deferred:**
- Cloud Mountain Retreat Center: retreat-only, no regular drop-in sits
- Eastside Dharma Collective: no web presence found (possibly Meetup-only)
- Shambhala Seattle iCal: Cloudflare blocks `?ical=1`. Monthly HTML calendar at `/monthly-calendar/` is scrapable if needed.

### Denver/Boulder Phase 3 — ✅ Live May 7 (5 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Zen Center of Denver | iCal feed (`zencenterofdenver.org/events/?ical=1`) | ✅ Live — 29 events. Weekly zazen Tue/Thu morning + evening, Zoom Zen daily, Queer Dharma, Zen of Recovery, Kannon Ceremony. |
| Boulder Zen Center | Google Calendar ICS | ✅ Live — 197 events. Weekly zazen, dharma talks, sesshins, half-day sits. |
| Orgyen Khandroling (Denver) | Google Calendar ICS | ✅ Live — 1218 events (full calendar history). Open Meditation Wed/Sun, Tara, Tsok. |
| Boulder Shambhala Center | Recurring sits seeded — Cologne server (center=191) down | ✅ Live — Thu 7pm Open Class seeded (13 instances, 90-day window). |
| Shambhala Meditation Center of Denver | Recurring sits seeded — Cologne server (center=218) down | ✅ Live — Sun 10am Group Meditation seeded (13 instances, 90-day window). |

City filter: Colorado state + Denver/Boulder cities added to `_filters.html`.
Center bios: 5 new entries in `centers.py`.
`ingestion/sources/denver.py` created with `CENTERS`, `ICAL_FEEDS`, wired into coordinator + abraxis.

**Skipped/deferred:**
- Nalandabodhi Colorado (Boulder): FullCalendar JS-rendered, no iCal. Regular schedule could be seeded.
- Kadampa Meditation Center Colorado (Denver): `?ical=1` returns 403. Possible Eventbrite.
- Eyes of Compassion Sangha (Denver, Plum Village): no iCal. Thu 7pm + Sun 10am could be seeded.

### NYC Phase 3d — Deferred

| Center | Approach |
|--------|----------|
| Village Zendo | HARD: JS-rendered (Divi + EventOrganiser plugin), no iCal found, no `__NEXT_DATA__`. Needs headless browser. |

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
- [x] **Email digest** — subscriber infrastructure built May 4: `subscribers` table + `/api/subscribe` + `/unsubscribe` endpoints + inline form in footer + `scripts/send_digest.py` (Resend API). **Needs:** `RESEND_API_KEY` env var + `EMAIL_SECRET` env var + domain for sender address. Set `RESEND_FROM=digest@yourdomain.com` once custom domain is live.
- [ ] **Custom domain** — ~$12/year, worth it for public launch. Needed for: email deliverability (RESEND_FROM sender domain), branded URL. Steps: buy domain → add to Fly.io (`fly certs add yourdomain.com`) → point DNS CNAME to `sanghacalendar.fly.dev`.
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
