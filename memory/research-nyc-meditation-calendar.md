# NYC Meditation Calendar — Phase 3 Research
*Created: 2026-05-05*

## Status: Research complete. Ready for implementation.

---

## Easy Wins (WordPress iCal feeds — implement like Bay Area centers)

### New York Insight Meditation Center (NYIMC)
- **Address:** 115 West 29th Street, 12th Floor, Manhattan (Midtown South)
- **Tradition:** Theravada / Secular Vipassana
- **Website:** https://www.nyimc.org
- **iCal:** `https://www.nyimc.org/events/?ical=1` ✅ **CONFIRMED**
  - Note: site returns 403 without browser User-Agent — use standard headers
- **Schedule:**
  - Thursdays 1:00–2:00pm ET — Community Sit (in-person + online, weekly; co-presented with Rubin Museum)
  - Wednesdays 6:30–8:30pm ET — Community Meditation Gathering (in-person + online, weekly)
  - First Sundays 10:00am–12:00pm ET — Sitting on Sunday (monthly)
  - MBSR courses, retreats, special events
- **Scrape difficulty:** EASY

### Brooklyn Zen Center (BZC)
- **Address:** 326 Clinton St, Carroll Gardens, Brooklyn, NY 11231
- **Tradition:** Soto Zen (socially-engaged, progressive)
- **Website:** https://brooklynzen.org
- **iCal:** `https://brooklynzen.org/?ical=1` ✅ **CONFIRMED**
  - `PRODID:-//Brooklyn Zen Center//NONSGML Events//EN`
- **Schedule:**
  - Online Morning Meditation Mon–Fri 7:30am ET
  - Wednesday Dharma Share: 7:00–8:30pm ET (in-person, weekly)
  - Saturday Morning Program: 9:00am–12:40pm (most Saturdays, in-person)
  - Monthly Full Moon Ceremony, Zazenkai one-day sits
- **Scrape difficulty:** EASY

### Kadampa Meditation Center New York (NYC branch)
- **Address:** 127 W 24th St, Chelsea, Manhattan
- **Tradition:** Tibetan (New Kadampa Tradition / NKT-IKBU)
- **Website:** https://meditationinnewyork.org (NYC branch)
- **iCal:** `https://meditationinnewyork.org/events/?ical=1` ✅ **CONFIRMED** (WordPress + The Events Calendar)
- **Schedule:** 30+ classes/week — Mon/Wed evenings 7pm, Tue lunchtime 11:15am, Tue/Fri evenings 5:30pm, Sun 11am
- **Scrape difficulty:** EASY

---

## Medium Difficulty

### Shambhala Meditation Center of New York
- **Address:** 151 W 30th St, 3rd Floor, Midtown South, NY 10001
- **Tradition:** Shambhala Buddhist (Tibetan/Vajrayana, Chögyam Trungpa lineage)
- **Website:** https://ny.shambhala.org
- **Calendar:** WordPress + custom `shambhala-event-templates` plugin. Events served as inline JSON: `const eventsDatas = {...}` in calendar page HTML. Server-side rendered (no JS needed).
- **iCal:** The calendar page offers Google Cal / Apple Cal subscription links, but the actual iCal URL is loaded client-side. `/?ical=1` is blocked by Cloudflare.
- **Approach:** Parse `const eventsDatas = {...}` JSON from `ny.shambhala.org/calendar/` via regex. Very clean structured data.
- **Schedule:**
  - Tuesday Evening Meditation: 1st/3rd Tuesdays, 7:15–8:15pm (in-person)
  - Virtual Healing Circle: monthly (last Saturday 12:30pm, online)
  - Sunday Dharma Gatherings: monthly (2nd Sunday)
  - Learn to Meditate (online): recurring Tuesdays 6pm
- **Scrape difficulty:** MEDIUM

### NY Zen Center for Contemplative Care (NYZCCC)
- **Address:** 119 W 23rd St, 4th Floor, Chelsea, NY 10011
- **Tradition:** Soto Zen (contemplative care / healthcare-oriented)
- **Website:** https://zencare.org
- **Calendar:** Webflow site — no calendar plugin, no iCal. Schedule is stable static HTML at `zencare.org/online-zendo`.
- **Schedule:**
  - Mid-Day Zazen Mon–Sat 12:30pm (online only, Zoom)
  - Sunday Morning: in-person + online, 10am zazen + 11:30am dharma talk
  - Monday Evening: in-person + online, 6pm
  - Wednesday Evening: in-person + online, 6pm
- **Approach:** Seed from stable static schedule; re-verify quarterly. Or scrape `/online-zendo` page.
- **Scrape difficulty:** MEDIUM (seed it manually)

### Tibet House US (thus.org)
- **Address:** 22 W 15th St, Chelsea, NY 10011
- **Tradition:** Tibetan Buddhist (Gelug / Vajrayana; connected to HH Dalai Lama)
- **Website:** https://thus.org
- **Calendar:** WordPress + Elementor (no events plugin). No iCal.
- **Eventbrite:** organizer_id `3903735193` — `https://www.eventbrite.com/o/tibet-house-us-3903735193`
- **Schedule:**
  - Lunchtime Meditation Mon–Fri 1:00–1:45pm ET (online, various teachers per day)
  - Occasional in-person lectures, exhibitions, special programs
- **Approach:** Eventbrite API (for ticketed events) + manually seed daily lunchtime meditation as recurring.
- **Scrape difficulty:** MEDIUM (Eventbrite + manual seed)

---

## Harder / Lower Priority

### Village Zendo
- **Address:** 260 W Broadway, Tribeca, NY 10013
- **Tradition:** Soto Zen (lineage of Glassman Roshi)
- **Website:** https://villagezendo.org
- **Calendar:** WordPress + Event Organiser plugin (FullCalendar frontend). No simple top-level iCal.
- **Approach:** HTML scrape `villagezendo.org/calendar/` — FullCalendar data is server-side rendered.
- **Schedule:** Daily zazen Mon–Fri morning 7:30am + evening 6:30pm; Sunday 9:30am. Monthly zazenkai.
- **Scrape difficulty:** MEDIUM-HARD (no iCal, need HTML calendar scrape)

### Zen Center of New York City / Fire Lotus Temple (ZCNYC)
- **Address:** 500 State St, Boerum Hill, Brooklyn, NY 11217
- **Tradition:** Soto Zen (Mountains and Rivers Order / Zen Mountain Monastery)
- **Website:** https://zcnyc.org
- **Calendar:** WordPress + Simple Calendar plugin backed by a private Google Calendar. Calendar HTML is server-rendered (scrapable), but no direct iCal.
- **Schedule:** Sunday Morning Program 9:30am–12:30pm; daily zazen (confirm schedule on site); LGBTQIA+ Sitting Group 1st/3rd Tuesdays 6pm (Zoom); TGNC Practice Night 2nd Thursdays 6:30pm (in-person); monthly half-day sits.
- **Scrape difficulty:** MEDIUM-HARD

---

## Skip / Not Applicable

| Center | Reason |
|--------|--------|
| Interdependence Project | DISSOLVED 2025 — organization wound down |
| IMS (Insight Meditation Society) | No NYC location; Barre, MA only. Use NYIMC for NYC |
| Rubin Museum | Physical museum CLOSED 2023. Meditation programming is co-hosted with NYIMC |
| Menla Mountain Retreat | Residential retreat center (Catskills). No public weekly sits |

---

## Additional Targets

- **Zen Studies Society / New York Zendo Shobo-Ji** — ✅ **Live May 5 (Phase 3c)**. iCal feed confirmed at `zenstudies.org/events/new-york-zendo-calendar/?ical=1`. Events prefixed NYZ:/Online:/DBZ: — strip prefix, filter DBZ (Catskills). 30 events/window.
- **ZCNYC / Fire Lotus Temple** — ✅ **Live May 5 (Phase 3c)**. LLM-assisted static HTML scraper on `zcnyc.org/calendar/`. Server-side rendered Simple Calendar plugin. Sunday Morning Program + LGBTQIA+ sits seeded.
- **Village Zendo** — ❌ HARD (JS-rendered, no iCal found). Defer to Phase 4.
- **InsightLA NYC satellite** — not researched; likely no NYC physical location
- **Common Ground Meditation (NYC)** — not researched
- **Brooklyn Tibetan Buddhist Center** — not researched

---

## Implementation Plan

### Phase 3a — Easy Wins (3 centers, implement first)
1. **NYIMC** → add to `ingestion/sources/nyc.py` + ICAL_FEEDS
2. **Brooklyn Zen Center** → same
3. **Kadampa NYC** → same
Total: 3 new WordPress iCal feeds, no new scraper code needed.

### Phase 3b — Medium (3 centers)
4. **Shambhala NYC** → new scraper: parse `const eventsDatas` JSON from calendar page
5. **NYZCCC** → seed script entry (stable schedule rarely changes)
6. **Tibet House** → Eventbrite API + recurring seed for lunchtime meditation

### Phase 3c — Deferred
7. **Village Zendo** → HTML scrape (medium effort)
8. **ZCNYC** → HTML scrape (medium effort)

---

## Infrastructure Notes

- NYC timezone: `America/New_York` (ET, UTC-5/4)
- All iCal fetches need browser User-Agent header (NYIMC and others return 403 otherwise)
- Will need new `ingestion/sources/nyc.py` analogous to `east_bay.py`
- City filter in app will need "Manhattan", "Brooklyn" added to city list
- Map view will need to handle NYC coordinates
