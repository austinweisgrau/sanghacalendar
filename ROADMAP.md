# Sangha Calendar — Dev Roadmap

_Last updated: 2026-05-01 (late heartbeat)_

## Current Status

**✅ Live at [sangha-calendar.fly.dev](https://sangha-calendar.fly.dev)**

- 105+ dynamic events across 21+ organizations (updated May 1 evening)
- Ingestion sources: 25+ iCal feeds + manually-seeded recurring sits + 45 Algolia (Spirit Rock) + 12 Momence (Berkeley Alembic) + Eventbrite (Nyingma, Insight Berkeley) + static HTML (Bay Zen, Berkeley Priory, Insight Berkeley)
- Coverage: East Bay + SF + Marin

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
| Berkeley Buddhist Monastery | LLM-assisted HTML scrape | Med | ⏸ Lower priority — primarily online (Zoom/YouTube). James Baraz Thursday Insight Meditation and Steven Tainer Wednesday sits are real in-person events but may be at BBM. Research needed. |

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

- [ ] **ICS subscription URLs** — personalized by filter (tradition, city, location type, day)
  - e.g., `sangha-calendar.fly.dev/subscribe?tradition=zen&city=Oakland`
  - Requires stable feed endpoint serving valid iCal
- [ ] **GCal / Apple Calendar deep links** — one-click add-to-calendar
- [ ] **Map view** — pin all centers, click for upcoming sits
- [ ] **Email digest** — weekly "sits near you" for subscribers
- [ ] **Donate button** — ko-fi or similar; this is free forever but costs ~$2/mo
- [ ] **Custom domain** — ~$12/year, worth it for public launch
- [ ] **Submission form** — "Know a center we're missing? Submit it."

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
