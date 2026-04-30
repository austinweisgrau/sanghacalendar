# Sangha Calendar — Dev Roadmap

_Last updated: 2026-04-30_

## Current Status

**✅ Live at [sangha-calendar.fly.dev](https://sangha-calendar.fly.dev)**

- 409 events across 18 organizations (updated Apr 30)
- Ingestion sources: 25+ iCal feeds + manually-seeded recurring sits + 45 Algolia (Spirit Rock) + 12 Momence (Berkeley Alembic)
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

**File:** `ingestion/feeds/ical_feed.py` line ~120
**Issue:** IMC Berkeley's Google Calendar exports events without `SUMMARY` fields. Current code silently drops any event with an empty title. Result: all IMC Berkeley events absent from calendar despite a valid, active iCal feed.
**Affected events:**
- Introductory Meditation Series (five Mondays Apr 20–May 18, 2026, 7–8:30pm)
- Monday Evening Sangha (recurring weekly from May 25 onward)

**Fix:** When `SUMMARY` is empty, fall back to first line of `DESCRIPTION`, then fall back to `"{org_name} Sit"`:

```python
title = str(component.get("SUMMARY", "")).strip()
if not title:
    import re
    raw_desc = str(component.get("DESCRIPTION", ""))
    clean = re.sub(r'<[^>]+>', ' ', raw_desc).strip()
    first_line = clean.split('\n')[0][:80].strip() if clean else ""
    title = first_line or f"{org_name} Sit"
```

**Status:** Workaround applied in `scripts/sangha-ingest.js` (Apr 29). Fix still needed in `ingestion/feeds/ical_feed.py` (used by GitHub Actions daily ingest).

---

### Phase 2: Non-iCal Center Scrapers

Priority order for East Bay centers not yet on live ingestion:

| Center | Approach | Difficulty | Status |
|--------|----------|------------|--------|
| Nyingma Institute | Eventbrite API | Low | 📋 Queued — **organizer_id: 336367203** (confirmed Apr 30). 11 upcoming events incl. Daily Kum Nye (recurring monthly), Women's Meditation Group (weekly Sun), Sunday Dharma Talks (weekly Sun). Website has no iCal. Eventbrite page scrape or API via organizer ID. |
| Insight Berkeley | Eventbrite API or scrape | Low-Med | 📋 Queued |
| Empty Gate Zen | WordPress `?ical=1` test | Low | ⚠️ Connection failed — site may be down or blocking crawlers (Apr 29) |
| Everyday Zen | WordPress `?ical=1` | Low | ✅ **Live** — added Apr 29. 21 events ingested (Weekly Metta Sitting, Group Recitation, All-Day Sittings, Everyday Caring). Hybrid/online focus; meets at Community Congregational Church in Tiburon. Note: EXCL_KW filter updated to title-only to avoid WordPress description noise. |
| Metta Dharma | WordPress `?ical=1` test | Low | ❌ No iCal — `?ical=1` returns homepage HTML (different events plugin or no plugin) |
| Bay Zen | LLM-assisted HTML scrape | Med | 📋 Queued |
| Berkeley Priory | LLM-assisted HTML scrape | Med | 📋 Queued |
| Berkeley Buddhist Monastery | LLM-assisted HTML scrape | Med | 📋 Queued |

**Scraper targets already in codebase (stubs):**
- `ingestion/scrapers/eventbrite.py`
- `ingestion/scrapers/wordpress_events.py`
- `ingestion/scrapers/squarespace.py`
- `ingestion/scrapers/static_html.py`

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
