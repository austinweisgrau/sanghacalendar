# Sangha Calendar — Dev Roadmap

_Last updated: 2026-05-15 (heartbeat 36)_

## Current Status

**✅ Live at [sangha-calendar.fly.dev](https://sangha-calendar.fly.dev)**

- 500+ events in 30-day window (500 cap), 44+ organizations
- 95+ recurring sit definitions → 2100+ instances seeded (as of heartbeat 23)
- Map view live at `/map` — all centers pinned with tradition colors
- 32+ center bio pages (centers.py)
- City filter includes 11 cities (Alameda, Kensington, Pleasant Hill, Richmond, Tiburon + more)
- Subscribe button: filter-aware GCal / Apple Calendar / .ics popup (heartbeat 23)
- Ingestion sources: 31 iCal feeds + manually-seeded recurring sits + 45 Algolia (Spirit Rock) + 12 Momence (Berkeley Alembic) + Eventbrite (Nyingma, Insight Berkeley, Tibet House US) + static HTML (Bay Zen, Berkeley Priory, Insight Berkeley, ZCNYC) + Squarespace JSON (Houston Zen Center)
- Coverage: East Bay (incl. Pleasant Hill/Contra Costa) + SF + Marin + NorCal Plum Village network + 19 Phase 3 metros

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

### GCal / iCal Subscribe Buttons (filter-aware)

Removed from header May 8 — static links aren't useful without filter state.
Feature pending:
- Buttons should appear *after* filters are applied and generate URLs that reflect active filters
- Generate `https://calendar.google.com/calendar/r?cid=...` deep links for filtered views
- Generate `webcal://...` links for Apple Calendar
- Requires stable per-filter ICS URL (already live at `/feed.ics`) — just need UI/UX placement post-filter

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
9. Portland 🔄 **Phase 3 Portland live May 7** (4 centers) — see below
10. Austin 🔄 **Phase 3 Austin live May 8** (2 centers) — see below
11. Minneapolis/Saint Paul 🔄 **Phase 3 Minneapolis live May 8** (4 centers) — see below
12. Phoenix 🔄 **Phase 3 Phoenix live May 9** (1 center) — see below
13. Houston 🔄 **Phase 3 Houston live May 9** (4 centers) — see below
14. Albuquerque/Santa Fe 🔄 **Phase 3 NM live May 10** (2 centers) — see below
15. Miami/South Florida 🔄 **Phase 3 Miami live May 10** (2 centers) — see below
16. San Diego 🔄 **Phase 3 San Diego live May 11** (2 centers) — see below
17. Atlanta 🔄 **Phase 3 Atlanta live May 11** (5 centers) — see below
18. Philadelphia 🔄 **Phase 3 Philadelphia live May 12** (4 centers) — see below
19. Las Vegas 🔄 **Phase 3 Las Vegas live May 12** (4 centers) — see below
20. Nashville 🔄 **Phase 3 Nashville live May 12** (4 centers) — see below
21. Detroit/SE Michigan 🔄 **Phase 3 Detroit live May 13** (4 centers) — see below
22. Sacramento 🔄 **Phase 3 Sacramento live May 13** (4 centers) — see below
23. Baltimore 🔄 **Phase 3 Baltimore live May 13** (4 centers) — see below
24. Pittsburgh 🔄 **Phase 3 Pittsburgh live May 14** (5 centers) — see below
25. Ann Arbor 🔄 **Phase 3 Ann Arbor live May 14** (3 centers) — see below
26. St. Louis 🔄 **Phase 3 St. Louis live May 14** (3 centers) — see below
27. Kansas City 🔄 **Phase 3 Kansas City live May 15** (2 centers) — see below
28. Richmond (VA) 🔄 **Phase 3 Richmond live May 15** (4 centers) — see below
29. Columbus (OH) 🔄 **Phase 3 Columbus live May 16** (5 centers) — see below
30. Raleigh-Durham-Chapel Hill (NC) 🔄 **Phase 3 Triangle live May 16** (3 centers) — see below
31. Salt Lake City (UT) 🔄 **Phase 3 SLC live May 16** (2 centers) — see below
32. New Orleans (LA) 🔄 **Phase 3 New Orleans live May 17** (2 centers) — see below
33. Tampa Bay (FL) 🔄 **Phase 3 Tampa Bay live May 17** (4 centers) — see below
34. Charlotte (NC) 🔄 **Phase 3 Charlotte live May 17** (4 centers) — see below
35. Tucson (AZ) 🔄 **Phase 3 Tucson live May 18** (1 center) — see below
36. Honolulu (HI) 🔄 **Phase 3 Honolulu live May 18** (4 centers) — see below
37. Rochester (NY) 🔄 **Phase 3 Rochester live May 18** (3 centers) — see below
38. Louisville (KY) 🔄 **Phase 3 Louisville live May 19** (6 centers) — see below
39. Providence (RI) 🔄 **Phase 3 Providence live May 19** (5 centers) — see below
40. Indianapolis (IN) 🔄 **Phase 3 Indianapolis live May 19** (2 centers) — see below
41. Oklahoma City (OK) 🔄 **Phase 3 OKC live May 20** (2 centers) — see below
42. Bloomington (IN) 🔄 **Phase 3 Bloomington live May 20** (4 centers) — heartbeat 50
43. Cleveland (OH) 🔄 **Phase 3 Cleveland live May 20** (5 centers) — heartbeat 51
44. Madison (WI) 🔄 **Phase 3 Madison live May 21** (5 centers) — heartbeat 52
45. Hartford/New Haven (CT) 🔄 **Phase 3 Connecticut live May 21** (5 centers) — heartbeat 53
46. Omaha/Lincoln (NE) 🔄 **Phase 3 Omaha live May 21** (4 centers) — heartbeat 54
47. Boise (ID) 🔄 **Phase 3 Boise live May 22** (5 centers) — heartbeat 55

### Oklahoma City Phase 3 — ✅ Live May 20 (2 centers, heartbeat 49)

| Center | Approach | Status |
|--------|----------|--------|
| Oklahoma Buddhist Vihara (4820 N Portland Ave, Oklahoma City OK 73112) | Recurring sits seeded — no iCal. Theravada. Wed 6pm (Silent Meditation), Sat 6pm (Pali Chanting + Sit), Sun 5pm (Guided Meditation + Discussion, hybrid). Free. | ✅ Live heartbeat 49 |
| Buddha Mind Monastery (5800 S Anderson Rd, Oklahoma City OK 73150) | Recurring sit seeded — no iCal. Chinese Mahayana/Zen. Sun 3pm (One-Hour Guided Meditation). Free. Founded 2004. | ✅ Live heartbeat 49 |

Oklahoma state + Oklahoma City city added to `_filters.html`.
Center bios added to centers.py for both centers.
`ingestion/sources/oklahoma_city.py` created; coordinator + abraxis wired.
`sangha-seed-recurring.js`: 4 new sit defs (283 → 287 total, 5300 instances).

**Research notes (2026-05-20):**
- Memphis TN investigated first: Memphis Zen Community (memphiszen.org) domain dead; Tennessee Buddhist Vihara Wed sits are Skype-only; Pema Karpo no clear schedule (thin placeholder site). OKC chosen instead.
- Ganden Ling Buddhist Center (NKT, 4813 N MacArthur Blvd): website offline — deferred.
- Rissho Kosei-kai Dharma Center (2745 NW 40th St): Nichiren-influenced, services/Hoza circles not sit-focused. Skipped.
- No Shambhala center found in OKC.

---

### Omaha/Lincoln NE Phase 3 — ✅ Live May 21 (4 centers, heartbeat 54)

| Center | Approach | Status |
|--------|----------|--------|
| Nebraska Zen Center / Heartland Temple (3625 Lafayette Ave, Omaha NE 68131) | Recurring sits seeded — WordPress JS-rendered calendar, no iCal. Soto Zen (Katagiri lineage). Sun 10am Open Zen, Wed 7pm evening zazen, Mon–Fri 6am morning zazen. Founded 1975. | ✅ Live heartbeat 54 |
| Flatwater Collective (1219 Leavenworth St, Omaha NE 68102) | Recurring sits seeded — Squarespace, no master iCal feed. Pluralist/non-sectarian. Thu 7pm Dharma Talk & Meditation, Sun 4pm Sunday Practice. | ✅ Live heartbeat 54 |
| Honey Locust Sangha (at The Yoga Path, 7641 Pacific St, Omaha NE 68114) | Recurring sits seeded — static HTML, no calendar. Plum Village (Thich Nhat Hanh). Mon 6:30pm, Fri 6pm. | ✅ Live heartbeat 54 |
| Lincoln Zen Center (3701 O Street #204, Lincoln NE 68510) | Recurring sits seeded — Wix site, no iCal. Soto Zen. Sun 10:30am, Mon 5:30pm, Wed 10:30am. | ✅ Live heartbeat 54 |

Nebraska state + Omaha + Lincoln cities added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/omaha.py` created; coordinator + abraxis wired.
`sangha-seed-recurring.js`: 10 new sit defs (328 → 338 total, 6015 instances).

**Research notes (2026-05-21):**
- Mindfulness Outreach Initiative (3015 Pacific St): physical location closed Jan 2025. Retreat-only (3x/year). Skipped.
- Midwest Dharma Wheel (Lincoln): enrollment-based with waitlist; not drop-in. Skipped.
- Nebraska Zen Center iCal: tried /?ical=1, /events/?ical=1, /events/feed/ical — all return HTML (not a Tribe Events Calendar despite appearance).
- Flatwater Collective iCal: tested ?format=ical on calendar root — returns HTML; individual events expose per-event ICS but no unified feed.

---

### Tucson Phase 3 — ✅ Live May 18 (1 center, heartbeat 43)

| Center | Approach | Status |
|--------|----------|--------|
| Kadampa Meditation Center Arizona (5326 E. Pima St, Tucson AZ 85712) | Recurring sits seeded — Wix site, no iCal. Sun 10am (75 min), Tue 6:30pm (75 min), Sat 10am (30 min). NKT Tibetan. | ✅ Live heartbeat 43 |

City filter: Tucson added to AZ state cities in `_filters.html`.
Center bio added to centers.py. `ingestion/sources/tucson.py` created.
`sangha-seed-recurring.js`: 3 new sit defs (235 → 238 total, 4540 instances).

**Research notes (2026-05-18):**
- Shambhala Tucson (tucson.shambhala.org): redirects to main shambhala.org — appears inactive.
- Rincon Mountain Insight / Tucson Insight: domains dead.
- Old Pueblo Zen: domain dead.
- Diamond Way Tucson: domain dead; no AZ centers in global Diamond Way directory.
- KMC Arizona is the only Tucson Buddhist center with an active web presence and confirmable schedule.

---

### Honolulu Phase 3 — ✅ Live May 18 (4 centers, heartbeat 44)

| Center | Approach | Status |
|--------|----------|--------|
| Honolulu Diamond Sangha / Ko Ko An Zendo (2747 Waiomao Rd, Palolo HI 96816) | Recurring sits seeded — no iCal (static PDF calendar). Zen (Robert Aitken lineage). Mon–Fri 5:30am, Wed 7pm, Sun 9am. | ✅ Live heartbeat 44 |
| Soto Mission of Hawaii / Shoboji (1708 Nuuanu Ave, Honolulu HI 96817) | Recurring sits seeded — no iCal. Soto Zen. Drop-in Mon/Wed/Fri 6:30am + Sun 9:30am. No reservation required. | ✅ Live heartbeat 44 |
| Bodhi Tree Dharma Center (654A N. Judd St, Palama, Honolulu HI 96817) | Recurring sits seeded — no iCal (Meetup-based). Multi-tradition. Mon 6:30pm (Vipassana), Tue 6:30pm (Plum Village), Wed 6pm (Stillness), Sat 9am. | ✅ Live heartbeat 44 |
| Aloha Sangha (2439 Holomua Pl, Palolo Valley, Honolulu HI 96816) | Recurring sit seeded — no iCal. Theravada/Insight, since 1998. Thu 6pm. | ✅ Live heartbeat 44 |

Hawaii state + Honolulu city added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/honolulu.py` created; wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 10 new sit defs (238 → 248 total, 4748 instances).

**Research notes (2026-05-18):**
- Daihonzan Chozen-ji (3565 Kalihi St): Rinzai Zen — appointment-only, no drop-in. Skip.
- Hawaii Kadhampa Buddhist Association (Waipahu, 20 mi west): different Kadhampa lineage (not NKT). Deferred.
- Kagyu Thegchen Ling (26 Gartley Pl): stale events page (last 2023). Deferred.
- Honolulu Shambhala: no active center found. Skip.
- Insight Meditation Hawaii: Big Island based; Honolulu = Zoom-only. Skip.
- KMC Hawaii (NKT): no Hawaii center found.
- Buddhist Study Center (Jodo Shinshu): devotional/educational, not meditation-focused. Skip.

---

### Rochester Phase 3 — ✅ Live May 18 (3 centers, heartbeat 45)

| Center | Approach | Status |
|--------|----------|--------|
| Rochester Zen Center (7 Arnold Park, Rochester NY 14607) | Recurring sits seeded — Cloudflare blocks iCal scraping. Tue–Fri 6am, Mon/Thu 7pm, Sat 6:30am, Sun 8:30am. Kapleau lineage Zen, founded 1966. | ✅ Live heartbeat 45 |
| Endless Path Zendo (56 Brighton St, Rochester NY 14607) | Recurring sits seeded — static HTML site, no iCal. Mon 7pm, Tue 7pm, Wed 6:30am, Sat 9am. Diamond Sangha / Kapleau lineage (Roshi Rafe Martin). | ✅ Live heartbeat 45 |
| Dharma Refuge (1124 Culver Rd, Rochester NY 14609) | Recurring sits seeded — Weebly site, no iCal. Wed 7pm, Sat 10am. Tibetan-influenced (Anam Thubten / Lojong), hybrid. | ✅ Live heartbeat 45 |

Rochester city filter added to NY state in `_filters.html`.
Center bios added to centers.py for all 3 centers.
`ingestion/sources/rochester.py` created; wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 7 new sit defs (248 → 255 total).

**Research notes (2026-05-18):**
- Rochester Zen Center iCal: WordPress site but Cloudflare blocks all automated scraping. Recurring sits seeded instead.
- White Lotus Buddhist Center (815 Park Ave, Drikung Kagyu): iCal endpoint returns 0 VEVENTs. Deferred — monitor.
- Rochester Chan Buddhist Temple (1040 Winton Rd N): website inaccessible. Deferred.
- Blooming Lilac Sangha (Brighton): Plum Village lineage, private home — contact required. Skip.
- No Shambhala or Kadampa/KMC center found in Rochester.

### Louisville Phase 3 — ✅ Live May 19 (6 centers, heartbeat 46)

| Center | Approach | Status |
|--------|----------|--------|
| Louisville Zen Center (917 Rosemary Dr, Louisville KY 40205) | Recurring sits seeded — no iCal. Tue 6:30pm (Rosemary Dr) + Sun 6:30pm (Bardstown Rd). Kapleau lineage. | ✅ Live heartbeat 46 |
| Open Mind Zen Louisville (1013 Bardstown Rd, Louisville KY 40204) | Recurring sit seeded — Sat 10:30am. White Plum Asanga. | ✅ Live heartbeat 46 |
| Louisville Community of Mindful Living / Sangha Lou (115 S Ewing Ave, Louisville KY 40206) | Recurring sit seeded — Sun 10am. Plum Village / TNH. | ✅ Live heartbeat 46 |
| Louisville Vipassana Community (2231 Payne St, Louisville KY 40206) | Recurring sit seeded — Mon 6:30pm. IMS-style Insight. | ✅ Live heartbeat 46 |
| Drepung Gomang Center for Engaging Compassion (411 N Hubbards Ln, Louisville KY 40207) | Recurring sits seeded — Wed noon + Wed 7pm. Gelugpa Tibetan. | ✅ Live heartbeat 46 |
| Kentucky Meditation Peace Center (4815 Manslick Rd, Louisville KY 40216) | Recurring sits seeded — Mon 7pm + Wed 7pm. Theravada. | ✅ Live heartbeat 46 |

Louisville city filter added to KY state in `_filters.html`.
`ingestion/sources/louisville.py` created; wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 13 new sit defs (255 → 268 total), 5047 instances seeded.

### Providence Phase 3 — ✅ Live May 19 (5 centers, heartbeat 47)

| Center | Approach | Status |
|--------|----------|--------|
| Providence Zen Center (99 Pound Rd, Cumberland RI 02864) | Tockify ICS feed — `tockify.com/api/feeds/ics/providence.zen.center`. Korean Zen (Kwan Um), founded by Seung Sahn 1972. | ✅ Live heartbeat 47 |
| Atisha Kadampa Buddhist Center (339 Ives St, Providence RI 02906) | Recurring sits seeded — NKT Tibetan. Sun 11am, Mon 12:15pm, Wed 6pm, Thu 12:15pm. | ✅ Live heartbeat 47 |
| Insight Meditation Community of Providence (354 Broadway, Providence RI 02909) | Recurring sits seeded — 1st & 3rd Thursday 7pm. Vipassana/Theravada. | ✅ Live heartbeat 47 |
| Insight Meditation Sangha Providence (27 Sims Ave, Providence RI 02909) | Recurring sit seeded — Wednesday evenings 7pm. Vipassana. | ✅ Live heartbeat 47 |
| RI Community of Mindfulness – Radiant Bell Sangha (5 Bell St, Providence RI 02909) | Recurring sit seeded — Saturday mornings 8am. Plum Village / TNH. | ✅ Live heartbeat 47 |

Providence + Cumberland city filters added to RI state in `_filters.html`.
`ingestion/sources/providence.py` created; wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 8 new sit defs (268 → 276 total), 5131 instances seeded.

**Research notes (2026-05-19):**
- Shambhala Providence: confirmed CLOSED (Facebook confirms; no active center). Skip.
- PZC in Cumberland (15 mi N of Providence) — still the Providence metro's primary Zen center.
- Wat Thormikaram (177 Hanover St): Khmer Theravada, community-focused, no public drop-in program. Skip.
- RICM Hope Street Sangha (1st & 4th Wed at 500 Hope St): skipped to avoid doubling Wed coverage with Insight PVD.

### Indianapolis Phase 3 — ✅ Live May 19 (2 centers, heartbeat 48)

| Center | Approach | Status |
|--------|----------|--------|
| KMC Indianapolis / Dromtonpa (4010 W 86th St Ste C, Indianapolis IN 46268) | Recurring sits seeded — Squarespace, no iCal. Sun 11am, Thu 6pm, Fri 10am. NKT Tibetan. | ✅ Live heartbeat 48 |
| Indianapolis Zen Center (3703 N. Washington Blvd, Indianapolis IN 46205) | Recurring sits seeded — Wix site, no iCal. Mon/Wed 7pm evenings, Mon/Wed/Fri 6:45am mornings, Sat 9:30am. Kwan Um Korean Zen (Seung Sahn lineage, est. 1991). Hybrid. | ✅ Live heartbeat 48 |

Indiana state + Indianapolis city added to `_filters.html`.
Center bios added to centers.py for both centers.
`ingestion/sources/indianapolis.py` created; wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 7 new sit defs (276 → 283 total), 5248 instances seeded.

**Research notes (2026-05-19):**
- KMC Indianapolis: Squarespace site; no iCal (?ical=1 returns homepage, events-calendar?format=json returns HTML). Founded 1998.
- IndyZen schedule confirmed via web search: Mon/Wed 7pm, Mon/Wed/Fri 6:45am, Sat 9:30am.
- Indiana Buddhist Center (9260 E 10th St, Indianapolis IN 46229): Gelugpa / Dalai Lama lineage. Wix site, JS-rendered, schedule unclear; events currently in Greenwood (suburb). 0 Eventbrite upcoming events. Deferred.
- Hoosier Heartland Shambhala: Based in Bloomington IN (IU town, 50 mi south). Not Indianapolis metro. Deferred.
- TMBCC (Tibetan Mongolian Buddhist Cultural Center): 3655 S Snoddy Rd, Bloomington IN. Gelugpa, founded by Dalai Lama's brother. Bloomington-only; separate metro. Deferred.

---

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

### LA Phase 3 — ✅ Live May 5–8 (3 centers)

| Center | Approach | Status |
|--------|----------|--------|
| InsightLA (Santa Monica) | Schema.org Event HTML parser — `/fullcalendar/` page is server-side rendered with structured markup | ✅ Live — `fetch_insightla()` in la.py. ~18 events/page (online morning sits, Santa Monica Dharma Nights, Recovery Dharma, Qigong, MBSR classes). 2 pages fetched. |
| Zen Center of Los Angeles (Koreatown) | LLM-assisted static HTML scrape of `zcla.org/calendars/` | ✅ Wired into STATIC_HTML_FEEDS in la.py. Will pick up on next Abraxis weekly run. |
| Shambhala Meditation Center of Los Angeles (Koreatown) | iCal feed — `shambhala-koeln.de/ical.php?center=208` — restored 2026-05-08 (388 events) | ✅ Live May 8 — new center addition in la.py ICAL_FEEDS + coordinator + abraxis. |

City filter updated: "Santa Monica (LA)" and "Los Angeles (LA)" added to index.html.
Center bios added to centers.py for insightla + zcla.

**Skipped for now:**
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

### Portland Phase 3 — ✅ Live May 7 (4 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Dharma Rain Zen Center (Roseway NE) | iCal feed (`dharma-rain.org/events/?ical=1`) | ✅ Live — 17 events. Soto Zen, oldest in Oregon (1975). Wed evenings + Sun mornings + early morning zazen. |
| Kagyu Changchub Chuling (Beaumont-Wilshire NE) | iCal feed (`kcc.org/calendar/month/?ical=1`) | ✅ Live — 25 events. Karma Kagyu Tibetan. Sun Shamatha AM/PM, Wed Chenrezi, Thu Silent Sit, daily AM online. |
| Portland Insight Meditation Community (Brentwood SE) | Recurring sits seeded — Wix site, no iCal | ✅ Live — 4 sits: Sun 9:30am hybrid, Mon 7:30am hybrid, Tue 6:30pm in-person, Wed 7pm hybrid. |
| Portland Shambhala (Buckman/Richmond SE) | Recurring sits seeded — dynamic FullCalendar, no static iCal | ✅ Live — Mon/Fri 6pm in-person + Sun 10am online. |

City filter: Oregon state + Portland city added to `_filters.html`.
Center bios: 4 new entries in `centers.py`.
`ingestion/sources/portland.py` created, wired into coordinator + abraxis.
`sangha-seed-recurring.js` now includes Portland sits (+ Seattle and Denver/Boulder added retroactively).

**Skipped/deferred:**
- Heart of Wisdom Zen Temple (zendust.org): ❌ Tested 2026-05-08 — `?ical=1` returns homepage HTML (WordPress without iCal plugin). Skip.
- Dorje Ling Portland (Forest Park): no iCal, weekly sits could be seeded — deferred
- Tathagata Meditation Center: is San Jose, CA (Bay Area) — not a Portland center

---

### Austin Phase 3 — ✅ Live May 8 (2 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Kadampa Meditation Center Austin (North Austin) | iCal feed (`meditationinaustin.org/events/?ical=1`) | ✅ Live — 23 events. NKT Tibetan. Main Austin location (7101 Easy Wind Drive) + Georgetown branch. Heart Jewel, Tsog, Foundation Program, Sunday General Program, weekend empowerments. |
| Austin Zen Center (Hyde Park) | Recurring sits seeded — site under maintenance as of 2026-05-08 | ✅ Live — 4 sit types seeded: Tue–Fri 6am Morning Zazen, Tue–Thu 12pm Midday Zazen, Tue–Thu 5:40pm Evening Zazen, Sat 9:15am Weekend Zazen + Dharma Talk. Soto Zen (SFZC lineage). |

City filter: Texas state + Austin city added to `_filters.html`.
Center bios added to centers.py for kadampa_austin + austin_zen.
`ingestion/sources/austin.py` created, wired into coordinator.py + abraxis_ingest.py.
`sangha-seed-recurring.js` updated: 4 AZC sit types added (73 total sit defs, 1574 instances).

**Skipped/deferred:**
- Austin Insight Meditation (austininsightmeditation.org): iCal exists but stale (last event Oct 2024). Possibly dormant. Monitor.
- Austin Shambhala: Domain parked/expired — skip.
- Austin Zen Center iCal: Site under maintenance since at least 2026-03. Monitor for recovery.

---

### Minneapolis Phase 3 — ✅ Live May 8 (4 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Common Ground Meditation Center (Seward, Minneapolis) | Sanity CMS public GROQ API — `https://4tyz2xuc.apicdn.sanity.io/` — 546 events/90-day window. Resolves `eventTemplate->` refs for titles. | ✅ Live — `fetch_common_ground()` in minneapolis.py. Daily Open Meditation (7am), weekly practice groups, community sits, retreats. |
| Minnesota Zen Meditation Center (Bde Maka Ska, Minneapolis) | Recurring sits seeded — Squarespace, no iCal | ✅ Live — Daily zazen Mon–Fri 6:30am, Sat–Sun 7:30am; evening zazen Mon–Thu 5:30pm; Sunday Morning Program 9:30am. Katagiri Roshi lineage. |
| Clouds in Water Zen Center (Lowertown, Saint Paul) | Recurring sits seeded — Squarespace, no iCal | ✅ Live — Morning zazen Mon–Fri 7am (90 min), Sunday Morning Program 9:30am. |
| Shambhala Meditation Center of Minneapolis (Whittier) | Recurring sits seeded — Cloudflare-blocked WordPress | ✅ Live — Weekly Wednesday 7pm sit seeded. |

City filter: Minnesota state + Minneapolis/Saint Paul cities added to `_filters.html`.
Center bios: 4 new entries in `centers.py`.
`ingestion/sources/minneapolis.py` created, wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 7 new sit defs (MZMC ×4, CiW ×2, Shambhala ×1).

**Key technique: Sanity CMS public API**
Common Ground uses Next.js + Sanity CMS. The Sanity public query API (`project_id.apicdn.sanity.io`) requires no auth for public datasets. GROQ syntax supports dereferencing with `->`. This pattern may apply to other centers using Sanity CMS.

**Skipped/deferred:**
- Kadampa Minneapolis (`meditationinminneapolis.org`): DNS failure — site down
- Minneapolis Shambhala schedule: confirmed weekly Wed 7pm only (Cloudflare blocks detailed schedule check)
- Twin Cities Vipassana Collective (tcvc.info): rural retreat center, no urban drop-in sits

### Phoenix Phase 3 — ✅ Live May 9 (1 center)

| Center | Approach | Status |
|--------|----------|--------|
| Kadampa Meditation Center Phoenix (Sunnyslope) | Recurring sits seeded — Wix site, no accessible iCal | ✅ Live — Sun 11am, Mon 7pm, Wed 7pm General Program classes. 39 instances in 90-day window. |

City filter: Arizona state + Phoenix/Scottsdale cities added to `_filters.html`.
Center bio added to centers.py. `ingestion/sources/phoenix.py` created.

**Research notes (2026-05-09):**
- Phoenix Shambhala (phoenix.shambhala.org): **CLOSED Dec 31, 2025** — merged into Albuquerque Shambhala. Current programming (Sunday sits, Heart of Recovery) continues via Albuquerque Center zoom links.
- KMC Phoenix (meditationinarizona.org): Wix site — no iCal accessible. Has satellite groups in Scottsdale, Surprise, Fountain Hills, Mesa, Tucson.
- No other Phoenix Buddhist centers with accessible online calendars found.

**Skipped/deferred:**
- Phoenix Shambhala: Closed — not appropriate to add
- KMC Scottsdale/Surprise/Fountain Hills/Mesa: satellite locations under same center
- Albuquerque Shambhala: new metro (separate heartbeat)

---

### Houston Phase 3 — ✅ Live May 9–10 (6 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Chung Tai Zen Center of Houston (Bellaire/Westchase) | iCal feed (`cthouston.org/events/?ical=1`) — WordPress The Events Calendar | ✅ Live — Chan (Taiwanese) Zen. Mon 7:30pm + Sat 10am Beginner, Wed 7:30pm Intermediate/Advanced, Thu 7pm Sutra Study, monthly half-day retreats. |
| Dawn Mountain Center for Tibetan Buddhism (Galleria) | Google Calendar public ICS (`dawnmountain.org_98i9a9njars99imv86omhfmebs@group.calendar.google.com`) | ✅ Live — Ecumenical Tibetan (Dzogchen, Ngondro). Free Sunday guided meditations, Teaching Tuesdays, weekend retreats. |
| Insight Meditation Houston (Museum District) | Recurring sits seeded — WordPress site, no iCal endpoint | ✅ Live — Monday 7–8:30pm hybrid at Covenant Church, 4949 Caroline St. Vipassana/Theravada. |
| Diamond Way Buddhist Center Houston (Heights) | Recurring sits seeded — no structured calendar | ✅ Live — Wednesday 7:30pm in-person at 5102 Center St. Karma Kagyu (Lama Ole Nydahl). |
| Houston Zen Center (The Heights) | Squarespace JSON API (`/events-calendar?format=json`) + 4 recurring sit defs | ✅ Live — Soto Zen. Daily zazen Mon–Thu (5:50am + 5:30pm), Sat 8:20am, Sun 8:50am. Weekly dharma talks via Squarespace scraper. |
| Drepung Loseling Institute of Texas (Westbury) | **NEW heartbeat 19** — Recurring sits seeded — Wix site, no iCal | ✅ Live — Gelugpa Tibetan (Dalai Lama lineage). Thu 7–9am, Sun 10am–noon, Sun 3–7pm. 11510 S Garden St. |

City filter: Houston city in `_filters.html` (TX state present).
Center bios: 6 entries in `centers.py`.
`ingestion/sources/houston.py`: CENTERS + ICAL_FEEDS + SQUARESPACE_FEEDS.
`ingestion/scrapers/squarespace.py`: new generic Squarespace JSON scraper.
`sangha-seed-recurring.js`: 92 sit defs → ~2055 instances (added DLI-TX heartbeat 19).

**Research notes:**
- KMC Houston: on hiatus, referring students to Dallas. Skip.
- Houston Shambhala: no active programs — dormant. Skip.

**Skipped/deferred:**
- Lone Star Buddhist (Mahamevnawa): pop-up locations, no stable feed

---

### New Mexico Phase 3 — ✅ Live May 10 (2 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Albuquerque Shambhala Meditation Center (Old Town) | Cologne iCal server (shambhala-koeln.de center=268) — 244 events | ✅ Live — Sunday Public Sitting (in-person + online), Heart of Recovery, Nyinthün, Shambhala Training. 1102 Mountain Rd NW. Now also absorbing Phoenix Shambhala programming (closed Dec 31, 2025). |
| Upaya Zen Center (Santa Fe) | WordPress iCal feed (`upaya.org/events/?ical=1`) — 30 events | ✅ Live — Daily Morning Zazen (7am), Midday Zazen (~12:20pm), Evening Zazen (5:30pm) + weekly Dharma talks + sesshins. 1404 Cerro Gordo Rd, Santa Fe NM. Roshi Joan Halifax lineage; one of the most prominent Soto Zen communities in the Southwest. |

City filter: New Mexico state + Albuquerque/Santa Fe cities added to `_filters.html`.
Center bios added to centers.py. `ingestion/sources/albuquerque.py` created, wired into coordinator + abraxis.

**Skipped/deferred:**
- Kadampa Albuquerque (`meditationinalbuquerque.org`): site returning 403 — monitor
- Kagyu Shenpen Ösel Chöling (`shenpen.org`): 403 on main site — monitor
- NM Vipassana: retreat center only, no drop-in sits

---

### Miami / South Florida Phase 3 — ✅ Live May 10 (2 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Kadampa Meditation Center Miami (Coral Gables) | Recurring sits seeded — Wix site with AJAX calendar, no public iCal | ✅ Live — 5 sit types: Sun 11am, Mon 7:30pm, Tue 7:30pm (en español), Thu 7:30pm, Fri 12:15pm lunchtime |
| Kadampa Meditation Center Fort Lauderdale (Lauderdale-by-the-Sea) | 2 Google Calendar public iCal feeds: GP Classes + Free Activities | ✅ Live — weekly GP sits (Sun/Wed/Thu), Tsog days, monthly events |

City filter: Florida state + Coral Gables + Lauderdale-by-the-Sea cities added to `_filters.html`.
Center bios added to centers.py.

**Research notes (2026-05-10):**
- Miami Shambhala: `miami.shambhala.org` redirects to main site — no active Miami center.
- Insight Miami (`insightmiami.org`): small Wix sangha, private email-based locations — skip.
- Southern Palm Zen Group (Boca Raton, `floridazen.com`): ~45 miles from Miami, no iCal — deferred.
- KMC Florida (Sarasota): 65 miles north — separate metro; skip for now.
- No Theravada/Vipassana centers with public calendars found in Miami metro.

---

### San Diego Phase 3 — ✅ Live May 11 (2 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Kadampa Meditation Center San Diego (Normal Heights) | Google Calendar ICS (`sddharma.com_81dvn4rrqjn21vv23kqo4m66hs@group.calendar.google.com`) for special events + recurring sits seeded (Sun 10:30am, Mon 6:30pm, Thu 6:30pm) | ✅ Live — NKT Tibetan. Special events: retreats, empowerments, Tsog days. Branch locations in Chula Vista and Oceanside. |
| San Diego Shambhala Meditation Center (Clairemont) | Cologne iCal server (shambhala-koeln.de center=254) — 232 events | ✅ Live — Shambhala lineage. Sunday public sitting (10–11am in-person), bi-weekly Wed online meditation (7pm), monthly EcoDharma group, Nyinthün. |

City filter: "San Diego" added to CA state cities in `_filters.html`.
Center bios added to centers.py. `ingestion/sources/san_diego.py` created, wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 3 new KMC San Diego sit defs (Sun/Mon/Thu).

**Research notes (2026-05-11):**
- Deer Park Monastery (Escondido, 35 mi north): retreat monastery, no regular public drop-in sits — skip.
- Diamond Way San Diego: no accessible web presence found.
- San Diego Zen Center (sdzc.org): domain not resolving — monitor.
- Insight Meditation San Diego: domain not resolving — monitor.

**Skipped/deferred:**
- Deer Park Monastery: retreat-focused, no public drop-in calendar
- KMC San Diego Google Calendar: mostly special events (2018–present); regular sits seeded separately

---

### Atlanta Phase 3 — ✅ Live May 11 (5 centers, heartbeat 24)

| Center | Approach | Status |
|--------|----------|--------|
| Atlanta Shambhala Meditation Center (1447 Church St, Decatur GA) | Cologne iCal server (shambhala-koeln.de center=196) — 372 events. Drop-in sits: Fri noon, Sun 10am, Tue 7pm. One Breath Group Mon/Wed/Thu. BIPOC + Queer Dharma groups. | ✅ Live — wired into coordinator + abraxis. |
| Atlanta Soto Zen Center (1167 Zonolite Pl NE, Atlanta GA) | Recurring sits seeded — Squarespace site, no iCal | ✅ Live — Daily Sunrise Sangha 6am (hybrid), Wed 7pm Intro to Zen (in-person), Sun 9am Sunday Service (hybrid). Founded 1977. |
| Kadampa Meditation Center Georgia (741 Edgewood Ave NE, Inman Park, Atlanta GA) | Recurring sits seeded — Squarespace site, no iCal | ✅ Live — Sun 10:30am, Tue 7pm Beginners, Wed 7pm Modern Buddhism. NKT tradition. |
| Red Clay Sangha (3315 Chamblee Dunwoody Rd, Chamblee GA) | **Wild Apricot RSS scraper** — new `ingestion/scrapers/wild_apricot_rss.py`. Multi-tradition (Theravada/Chan/Plum Village). 91 events from RSS feed (243 total items). | ✅ Live heartbeat 24 — Sunday Morning Meditation 9am, Plum Village Tradition 5pm, Insight Dialog 3rd Mon 7pm. |
| Drepung Loseling Institute (1781 Dresden Dr NE, Brookhaven, Atlanta GA) | LLM-assisted static HTML scraper (`drepung.org/changing/calendar/current.htm`) + recurring Sun 11am seeded. Major Gelugpa institution, Emory CBCT partner, resident monks. | ✅ Live heartbeat 24 — Sun 11am Meditation seeded; monthly HTML scraper for special events. |

City filter: Georgia state + Atlanta + Chamblee + Decatur cities in `_filters.html`.
Center bios added to centers.py for all 5 Atlanta centers.
`ingestion/sources/atlanta.py`: RSS_FEEDS + STATIC_HTML_FEEDS added.
`ingestion/scrapers/wild_apricot_rss.py`: new generic Wild Apricot RSS scraper.
`data/schemas/event.py`: SourceType.RSS_FEED added.
`sangha-seed-recurring.js`: Drepung Loseling Atlanta Sun 11am added (now 96 sit defs).

**Skipped/deferred:**
- Atlanta Insight Meditation Community (atlinsight.org): small Squarespace community. Tue 6:30pm + Thu 8am Zoom satsang. Low priority.
- Diamond Way Atlanta: no active center found.

---

### Philadelphia Phase 3 — ✅ Live May 12 (4 centers)

| Center | Approach | Status |
|--------|----------|--------|
| Shambhala Meditation Center of Philadelphia (2030 Sansom St, Center City) | Recurring sits seeded — Cologne iCal (center=210) returning 522 as of 2026-05-12. Sun 10am, Thu 6pm in-person. | ✅ Live heartbeat 25 |
| Kadampa Meditation Center Philadelphia (47-49 N 2nd St, Old City) | Recurring sits seeded — Wix site, no iCal. Mon/Wed/Thu 6:30pm, Sun 10:30am in-person. | ✅ Live heartbeat 25 |
| Zen Center of Philadelphia (4904 Cedar Ave, West Philadelphia) | Recurring sits seeded — WordPress + Simple Calendar plugin (Google Cal embedded; no extractable iCal). Sun 10am, Wed 7pm hybrid. Ordinary Mind Zen School lineage. | ✅ Live heartbeat 25 |
| Chenrezig Tibetan Buddhist Center (954 N Marshall St, Northern Liberties) | Recurring sits seeded — Wix site, no iCal. Sun 10am hybrid, Thu 7pm Green Tara Puja in-person. Founded 1989 by Lama Losang Samten. | ✅ Live heartbeat 25 |

City filter: Pennsylvania state + Philadelphia city added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/philadelphia.py` created (CENTERS registry + commented-out iCal entry for Shambhala).
`sangha-seed-recurring.js`: 10 new sit defs (Shambhala ×2, Kadampa ×4, ZCP ×2, Chenrezig ×2).

**Research notes (2026-05-12):**
- Shambhala Philadelphia iCal (center=210): 522 error. Will re-activate when Cologne server recovers.
- Kadampa Philadelphia: extremely active (daily program). Wix site; no iCal. Meetup presence possible future scrape.
- Zen Center of Philadelphia: Google Calendar via Simple Calendar WP plugin. `data-calendar-id="6098"` is internal WP ID; Google Calendar ID not exposed in HTML. Monitor for public iCal workaround.
- Nalandabodhi Philadelphia: WordPress iCal exists but returns empty VCALENDAR. No fixed address. Deferred.
- Delaware Valley Insight Meditation: sitting groups at home locations/community spaces. Deferred.
- Heart Sangha: sporadic Sunday Sangha (not weekly). Deferred.

**Skipped/deferred:**
- Nalandabodhi Philadelphia: empty iCal, no stable address — monitor
- Heart Sangha: sporadic programming — skip for now
- Delaware Valley Insight: peer-led home sitting groups, no stable venue

---

### Las Vegas Phase 3 — ✅ Live May 12 (4 centers, heartbeat 26)

| Center | Approach | Status |
|--------|----------|--------|
| Chaiya Meditation Monastery (7925 Virtue Ct, Enterprise/SW Las Vegas NV 89113) | Recurring sits seeded — Bravesites platform, no iCal. Daily sessions: 9am, 2pm, 5pm (Mon–Sun). Theravada (Burmese). | ✅ Live heartbeat 26 |
| Zen Center of Las Vegas (7925 Virtue Ct, same campus as Chaiya) | Recurring sits seeded — static HTML schedule, no feed. Sun 1pm + 1st Sun noon Intro. Kwan Um School (Seung Sahn). | ✅ Live heartbeat 26 |
| Diamond Way Buddhist Center Las Vegas (3743 N Rosecrest Circle, East Las Vegas NV 89121) | Recurring sit seeded — global network site, no iCal. Tue 7pm. Karma Kagyu (Lama Ole Nydahl). | ✅ Live heartbeat 26 |
| Nevada Buddhist Temple (2040 Abels Lane, North Las Vegas NV 89115) | Recurring sits seeded — WordPress, no Events Calendar plugin. Wed 7pm in-person + Mon/Tue/Thu/Sat/Sun 7:30pm online. Sri Lankan Theravada. | ✅ Live heartbeat 26 |

City filter: Nevada state + Las Vegas + North Las Vegas cities added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/las_vegas.py` created (CENTERS registry, ICAL_FEEDS empty).
`sangha-seed-recurring.js`: 9 new sit defs (Chaiya ×3, Zen Center LV ×2, Diamond Way LV ×1, Nevada Buddhist Temple ×3). Now 125 sit defs → 2838 instances.

**Research notes (2026-05-12):**
- Kadampa LV (meditationinlasvegas.org): redirects to IKRC Grand Canyon AZ — appears closed.
- Bhodhiyana Meditation Center (bhodhiyana.org): website offline — monitor.
- Las Vegas Buddhist Sangha (lvbs.org): Jodo Shinshu / Pure Land devotional — not meditation-focused. Skip.
- Lohan Spiritual Center (lvlohans.org): syncretic (Chan/Tibetan/Taoist/Shaolin) — deferred.
- Nevada Buddhist Vihara (nbvlv.org): WordPress/Astra shell, no Events Calendar. Same tradition as Nevada Buddhist Temple; may be same or related entity.

**Skipped/deferred:**
- Kadampa LV: appears closed, redirecting to Arizona center
- Bhodhiyana: site offline — monitor for recovery
- Lohan Center: unusual tradition classification; deferred

---

### Nashville Phase 3 — ✅ Live May 12 (4 centers, heartbeat 27)

| Center | Approach | Status |
|--------|----------|--------|
| One Dharma Nashville (530 26th Ave N, Germantown, Nashville TN 37209) | Recurring sits seeded — WordPress iCal exists but contains only out-of-area retreats; Mon 7pm in-person+Zoom sit seeded. Insight/Vipassana. Teacher: Lisa Ernst. | ✅ Live heartbeat 27 |
| Wild Heart Meditation Center (3123 Gallatin Pike, East Nashville TN 37216) | Recurring sits seeded — Squarespace, no site-wide iCal. Wed 7pm, Fri 7pm, Sun 9am. Secular/multi-tradition (Dharma Punx lineage). Co-located with Nashville Zen Center. | ✅ Live heartbeat 27 |
| Nashville Zen Center (3123 Gallatin Pike, East Nashville TN 37216) | Recurring sits seeded — Squarespace, no iCal. Tue 7pm + Sat 7am zazen. Soto Zen (Silent Thunder Order, Matsuoka lineage). | ✅ Live heartbeat 27 |
| Padmasambhava Buddhist Center of Tennessee (419 East Iris Drive, 12South Nashville TN 37204) | Recurring sit seeded — Wix, no iCal. Sun 9:30am Calm Abiding Meditation. Tibetan (Nyingma/Dzogchen). Founded 1990, oldest Tibetan center in the region. | ✅ Live heartbeat 27 |

Tennessee state + Nashville city added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/nashville.py` created (CENTERS registry).
`sangha-seed-recurring.js`: 7 new sit defs (One Dharma ×1, Wild Heart ×3, NZC ×2, PBC-TN ×1).

**Research notes (2026-05-12):**
- One Dharma Nashville iCal (onedharmanashville.com/events/?ical=1): Active feed but only retreat events — all filtered out by filter_to_sits. Regular Monday sits seeded as recurring.
- Wild Heart: Squarespace with per-event ICS links. No site-wide feed. Rich schedule (also Recovery Dharma, Queer Sangha, POC Sangha) — only core weekly sits seeded.
- Nashville Zen Center: Squarespace, static schedule page only.
- PBC-TN: Wix site. No iCal. Sun 9:30am confirmed from website.
- Snow Lion Nashville (nashvillemeditates.org): Site unreachable — deferred until recovery.
- Sitagu Buddhist Monastery (99 Lyle Lane): Burmese Theravada monastery — primarily devotional, no structured public sit calendar — skip.

**Skipped/deferred:**
- Snow Lion Nashville (Shambhala-derived): site down — monitor for recovery
- Sitagu Buddhist Monastery: devotional focus, no public sit calendar

---

### Detroit / SE Michigan Phase 3 — ✅ Live May 13 (4 centers, heartbeat 28)

| Center | Approach | Status |
|--------|----------|--------|
| Detroit Zen Center (3030 Casmere St, Hamtramck MI) | Recurring sits seeded — Wix site, no iCal. Sun 10am Zen Workshop (2hr). Korean Zen (Chogye / Sudeok-sa), founded 1990. | ✅ Live heartbeat 28 |
| Still Point Zen Buddhist Temple (4345 Trumbull Ave, Detroit MI) | Recurring sits seeded — Wix site, no iCal. Sun 8:30am + Sat 10am service (in-person + livestream). Korean Zen (Samu Sunim lineage). | ✅ Live heartbeat 28 |
| Field Temple (5333 Elmwood Ave, Detroit MI) | Recurring sits seeded — simple static site, no iCal. Sun 10am outdoor zazen in garden. Korean Zen tradition. | ✅ Live heartbeat 28 |
| Dharma Gate Zen Center (360 East Maple Suite K, Troy MI) | Recurring sits seeded — WordPress, weekday sittings on hiatus. Sun 10am service. Soto Zen. | ✅ Live heartbeat 28 |

Michigan state + Detroit/Hamtramck/Troy cities added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/detroit.py` created (CENTERS registry).
`sangha-seed-recurring.js`: 5 new sit defs (DZC ×1, Still Point ×2, Field Temple ×1, Dharma Gate ×1). Now 137 sit defs → 2994 instances.

**Research notes (2026-05-13):**
- Detroit Zen Center: Wix-based events page, no `?ical=1` feed. Sunday Workshop confirmed
  10am–12pm weekly. First Sunday Beginners Workshop 9am–12pm.
- Still Point Zen Buddhist Temple: Wix site. Sunday hours confirmed 8:30am–11:30am.
  Saturday service also confirmed but exact start time unverified — seeded at 10am.
- Field Temple: Simple site, Sunday 10–11am confirmed. Garden/outdoor location.
- Dharma Gate Zen: WordPress but weekday sittings on hiatus. Sunday 10am only active sit.
  Recovery Dharma also meets here (Sat 10am, Wed noon) — not seeded (recovery program).
- Midwest Buddhist Meditation Center (Warren MI): Thai Theravada temple — daily practice
  but not structured as public drop-in sits. Deferred.
- Great Lakes Buddhist Vihara (Southfield MI): Theravada monastery — online courses only,
  no regular public drop-in sittings. Deferred.
- Ann Arbor centers (45 mi west): separate metro — deferred.

**Skipped/deferred:**
- Midwest Buddhist Meditation Center: Thai temple, not clear public drop-in format
- Great Lakes Buddhist Vihara: Theravada monastery, online courses only
- Ann Arbor centers: separate metro ~45 miles west (Insight Meditation Ann Arbor, Still
  Mountain, Zen Buddhist Temple Ann Arbor, Jewel Heart) — future metro
- Detroit St. Zen Center (detroitstzencenter.com): site returning 522 error — monitor

---

### Sacramento Phase 3 — ✅ Live May 13 (4 centers, heartbeat 29)

| Center | Approach | Status |
|--------|----------|--------|
| Sacramento Buddhist Meditation Group (3111 Wissemann Dr, Sacramento CA 95826) | WordPress Events Calendar iCal — `sbmg.org/events/?ical=1`. Sun 10am sits with rotating teachers (pluralist), Tue 7am online. BIPOC Sangha 4th Sun. | ✅ Live heartbeat 29 |
| Valley Streams Zen Sangha (3111 Wissemann Dr, Sacramento CA 95826) | WordPress Events Calendar iCal — `valleystreamszen.org/events/?ical=1`. Thu 6am Morning Zazen + Service (hybrid), Mon 7pm Evening Program. | ✅ Live heartbeat 29 |
| Sacramento Insight Meditation (3111 Wissemann Dr, Sacramento CA 95826) | Recurring sits seeded — Incapsula blocks iCal at sactoinsight.org. Thu 7pm Meditation & Dharma Talk + Tue 6:30pm Dharma Recovery. Theravada/Vipassana. | ✅ Live heartbeat 29 |
| Lion's Roar Dharma Center (3240 B Street, Sacramento CA 95816) | Google Calendar ICS — `9ohgorq8dhupc1u8b0hhtiafbc@group.calendar.google.com`. Monthly Vajrayana practices, Sunday services. Tibetan (Gelugpa). | ✅ Live heartbeat 29 |

Sacramento city added to CA state filter in `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/sacramento.py` created.
`sangha-seed-recurring.js`: 2 new SIM sit defs (Thu 7pm + Tue 6:30pm). Now 139 sit defs → 3020 instances.

**Research notes (2026-05-13):**
- Sacramento Dharma Center (sacdharma.org): 3111 Wissemann Drive, Sacramento CA 95826.
  Shared campus (1.7 acres, 8000 sq ft) hosting SBMG, VSZS, and SIM. Central hub for
  secular/pluralist Sacramento Buddhist community since 1970s.
- SBMG (sbmg.org): Active iCal confirmed. Pluralist — rotating teachers from all traditions.
  Also has BIPOC Sangha 4th Sunday at 1:15pm (identity-focused).
- VSZS (valleystreamszen.org): Active iCal confirmed. Ordinary Mind Zen / Charlotte Joko Beck
  lineage. Thu 6am zazen is a real sit (early but active). Export .ics visible on website.
- SIM (sactoinsight.org): Incapsula/Imperva blocks all HTTP requests. Thu 7pm confirmed from
  web search results + Sacramento Dharma Center event listings.
- Lion's Roar (lionsroardharmacenter.org): Google Calendar ID decoded from iframe embed src
  (base64-encoded). Calendar active, events 2024–2026. Monthly moon-phase Vajrayana practices.
- Sacramento Shambhala: No independent center — NorCal Shambhala network (Berkeley/SF/Davis/
  Silicon Valley/Sonoma). No Sacramento entry.
- KMC Sacramento (meditationinsacramento.org): Domain not resolving — appears defunct.
- Sacramento Zen (sacramentozen.com): Ordinary Mind Zen, private Elmhurst zendo, address
  not published. Mon 7am + Tue 7pm sits; deferred (private location).

**Skipped/deferred:**
- KMC Sacramento: domain dead — monitor
- Sacramento Zen: private location not listed; deferred
- Davis Shambhala (25 mi west): separate NorCal Shambhala entry — deferred
- Davis Dharma Study Group: small group, deferred

---

### Baltimore Phase 3 — ✅ Live May 13 (4 centers, heartbeat 30)

| Center | Approach | Status |
|--------|----------|--------|
| Baltimore Shambhala Centre (33 W 33rd St, Baltimore MD 21218) | Recurring sits seeded — Shambhala iCal server (center=201) returns 522. Biweekly Sat 9am hybrid (2nd/4th Sat) at 33rd Street YMCA. Shambhala / Tibetan. | ✅ Live heartbeat 30 |
| Kadampa Meditation Center Maryland (901 Dartmouth Rd, Baltimore MD 21212) | Recurring sits seeded — Squarespace site, no iCal. Wed 11am, Wed 6pm, Thu 6:30pm, Sun 10:30am in-person. New Kadampa Tradition (Tibetan/Gelug). | ✅ Live heartbeat 30 |
| KMC Maryland Canton (1025 S Potomac St, Baltimore MD 21224) | Recurring sit seeded — Canton branch, Tue 7pm in-person at Church on the Square. | ✅ Live heartbeat 30 |
| Baltimore Dharma Group (3107 N Charles St, Baltimore MD 21218) | Recurring sits seeded — Wix site, no iCal. Sun 8am + Thu 7pm zazen at Homewood Friends Meeting. Soto Zen, shikantaza style. | ✅ Live heartbeat 30 |

Maryland state + Baltimore city added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/baltimore.py` created (CENTERS registry).
`sangha-seed-recurring.js`: 9 new sit defs (Shambhala ×2, KMC MD ×4, KMC Canton ×1, BDG ×2). Now 148 sit defs → 3117 instances.

**Research notes (2026-05-13):**
- Baltimore Shambhala Centre: shambhala-koeln.de/ical.php?center=201 returns 522
  (same as DC 205, Boulder 191, Denver 218 — Shambhala iCal server broadly down).
  Meets at 33rd Street YMCA, Baltimore. 2nd/4th Sat Meditation@33rd (hybrid 9am).
  Mon-Fri 7am online morning sit; Sun 9am online; Thu Lojong study group (Zoom).
- KMC Maryland (meditationmd.org): Squarespace. 901 Dartmouth Rd, Roland Park.
  Very active schedule: Wed 11am, Wed 6pm, Thu 6:30pm, Sun 10:30am. Also Canton
  branch (1025 S Potomac St, Tue 7pm) and Columbia branch (Owen Brown Interfaith
  Center, Tue 7:30pm) — Columbia deferred (25 mi from Baltimore center).
- Baltimore Dharma Group (baltimoredharmagroup.org): Wix site, no iCal. Small lay
  Soto Zen community at Homewood Friends Meeting House (3107 N Charles St).
  Sun 8am zazen (two 30-min periods + kinhin). Thu evenings alternating dharma
  class and open zazen. Free, all welcome.
- Gampopa Center (Annapolis): Kagyu Tibetan, 918 Chesapeake Ave, ~30 mi south.
  Deferred to future Annapolis/Chesapeake expansion.
- Burning House Zendo (Westminster): Friday in-person canceled until July 2026.
  Monitor for resumption; weekday Zoom sits only active currently.
- Clare Sangha / ZC Baltimore: Primarily online Zen community. Deferred.

**Skipped/deferred:**
- Gampopa Center (Annapolis): 30 miles south — future Annapolis expansion
- KMC Columbia: Owen Brown Interfaith Center, 25 miles from Baltimore — future metro
- Columbia Insight Meditation Group (Ellicott City): 25 miles, school-year dependent
- Burning House Zendo (Westminster): in-person sits canceled until July 2026
- Clare Sangha: primarily online community

---

### Pittsburgh Phase 3 — ✅ Live May 14 (5 centers, heartbeat 31)

| Center | Approach | Status |
|--------|----------|--------|
| Stillpoint — A Pittsburgh Zen Community (137 41st St, Lawrenceville, PA 15201) | Recurring sits seeded — WordPress, no iCal. Sun 9:30am + Wed 7pm zazen. Lay Zen community. | ✅ Live heartbeat 31 |
| Pittsburgh Buddhist Center (58 QSI Lane, Allison Park, PA 15101) | Recurring sit seeded — WordPress, no iCal. Wed 7pm sit with resident Burmese monks. Theravada. Beginners 6:30pm. | ✅ Live heartbeat 31 |
| Pittsburgh Buddhist Center — Oakmont (700 Allegheny River Blvd, Oakmont, PA 15139) | Recurring sit seeded — outreach location at Oakmont Carnegie Library. Tue 6pm. | ✅ Live heartbeat 31 |
| Olmo Ling Bon Center and Institute (1101 Greenfield Ave, Greenfield, PA 15217) | Recurring sits seeded — Wix, no iCal. Dzogchen Practice Group 1st & 3rd Sundays 4pm hybrid. Tibetan Bon. | ✅ Live heartbeat 31 |
| Three Rivers Tibetan Cultural Center (1660 Lincoln Way, White Oak, PA 15131) | Recurring sits seeded — static HTML, no iCal. Wed 7pm + Sun 10am hybrid. Drikung Kagyu. | ✅ Live heartbeat 31 |

Pennsylvania state already present from Philadelphia; Pittsburgh + Allison Park + Oakmont + White Oak cities added to `_filters.html`.
Center bios added to centers.py for all 5 centers.
`ingestion/sources/pittsburgh.py` created (CENTERS registry, ICAL_FEEDS empty).
`ingestion/coordinator.py`: `run_pittsburgh_phase3()` added.
`sangha-seed-recurring.js`: 8 new sit defs (Stillpoint ×2, PBC main ×1, PBC Oakmont ×1, Olmo Ling ×2, TRTCC ×2). Now 156 sit defs → 3201 instances.

**Research notes (2026-05-14):**
- Stillpoint Zen (stillpointzen.org): Active lay Zen community in Lawrenceville. Sun 9:30–10:40am, Wed 7–8pm. Fourth Saturday all-day zazenkai (not seeded as weekly). Walk-in welcome.
- Pittsburgh Buddhist Center (pittsburghbuddhistcenter.org): Theravada monastery with resident Burmese monks. Wed main sit + Tue/Mon/Thu outreach at Carnegie Libraries. Only Wed + Tue Oakmont seeded.
- Olmo Ling (olmoling.org): Rare Tibetan Bon center (pre-Buddhist tradition). Wed Ngondro + Silent Meditation temporarily cancelled. Dzogchen Practice Group 1st/3rd Sundays 4pm (meditation) + 2nd/4th (reading/discussion, not seeded).
- Three Rivers Tibetan CC (threeriverstibetancc.org): Drikung Kagyu, resident teachers Khenpo Choephel + Lama Kalsang. 12 miles SE of Pittsburgh in White Oak. Wed 7pm rotating practices; Sun 10am Vajrasattva.
- Pittsburgh Shambhala: Disaffiliated from Shambhala International (2019). Website redirects to main shambhala.org. Skip.
- Deep Spring Zen Temple (Sewickley, 20mi N): SZBA Soto Zen, orientation required. Deferred.
- Neighborhood Zen (Greenfield): Soto Zen private community, sign-up required. Has Google Calendar. Deferred.

**Skipped/deferred:**
- Pittsburgh Shambhala: disaffiliated/inactive — skip
- Deep Spring Zen Temple (Sewickley): orientation required, 20+ miles north — deferred
- Neighborhood Zen: semi-private, registration required — deferred
- Zen Group of Pittsburgh (Kwan Um, Wilkinsburg): small group, verify still active — deferred
- Insight Meditation Community of Pittsburgh: Zoom-only, no stable website — deferred

---

### Ann Arbor Phase 3 — ✅ Live May 14 (3 centers, heartbeat 32)

| Center | Approach | Status |
|--------|----------|--------|
| Jewel Heart (1129 Oak Valley Dr, SE Ann Arbor, MI 48108) | Google Calendar public iCal (`annarbor@jewelheart.org`) — courses, retreats, special events. Tibetan Gelugpa. | ✅ Live heartbeat 32 — wired into coordinator + abraxis. Tue 6pm free community sit seeded as recurring. |
| Insight Meditation Ann Arbor (180 Little Lake Dr #1, Ann Arbor, MI 48103) | Recurring sits seeded — WordPress, no Events Calendar iCal. Sun 10am in-person + Sat 10am online. Theravada/Vipassana. | ✅ Live heartbeat 32 |
| Zen Buddhist Temple Ann Arbor (1214 Packard St, Ann Arbor, MI 48104) | Recurring sit seeded — Wix, no iCal. Sun 10am Korean Zen public service, in-person + livestreamed. | ✅ Live heartbeat 32 |

Ann Arbor city added to MI state filter in `_filters.html` (Michigan state + Detroit cities already present from heartbeat 28).
Center bios added to centers.py for all 3 centers.
`ingestion/sources/ann_arbor.py` created (CENTERS registry + Jewel Heart Google Calendar ICAL_FEEDS).
`ingestion/coordinator.py`: `run_ann_arbor_phase3()` added.
`ingestion/abraxis_ingest.py`: Ann Arbor iCal section added.
`sangha-seed-recurring.js`: 4 new sit defs (IMAA Sun + Sat, Zen Temple Sun, Jewel Heart Tue). 156+4 = 160 sit defs.

**Research notes (2026-05-14):**
- Jewel Heart (jewelheart.org): Founded by Kyabje Gelek Rimpoche (1988), current director Demo Rinpoche. 14th Dalai Lama taught here 2008. Google Calendar ID `annarbor@jewelheart.org` — active, public. Weekly free Community Meditation Tuesdays 6–6:45pm seeded as recurring (calendar also covers it but recurring ensures continuity). Sun White Tara program (9:30am) also in iCal.
- IMAA (insightmeditationannarbor.org): WordPress site without The Events Calendar plugin; no iCal endpoint. Sun in-person (10–11:15am, 45-min sit + talk) seeded. Sat online Zoom (10–11:30am) seeded. Weekday 7:30am Zoom sits not seeded (Mon–Fri daily is complex to manage; can add if needed).
- Zen Buddhist Temple (zenbuddhisttemple.org/annarbor): Wix site, no iCal. Korean Zen (Son Buddhism). Samu Sunim lineage. Resident priests Haju Sunim and Maum. Sunday service 10am seeded.
- Still Mountain (stillmountain.org): Tai Chi center — false positive, skip.

**Skipped/deferred:**
- UMich Buddhist groups: website offline
- Great Lakes Buddhist Vihara: Detroit-based, not Ann Arbor
- Ann Arbor Karma Thegsum Choling: no accessible web presence found
- SGI Ann Arbor: national org, deferred

---

### St. Louis Phase 3 — ✅ Live May 14 (3 centers, heartbeat 33)

| Center | Approach | Status |
|--------|----------|--------|
| Confluence Zen Center STL (3544 Oxford Ave, Maplewood, MO 63143) | WordPress All-in-One Event Calendar iCal feed — recurring Morning Zazen (Mon/Tue/Thu 6:20am), Evening Zazen (Mon 7pm), Sunday Zazen (2nd/3rd/4th/5th Sun 9am), Beginner's Night (1st Tue monthly). Soto Zen. | ✅ Live heartbeat 33 — wired into coordinator + abraxis |
| Sunday Sangha St. Louis (Brentwood, MO) | Recurring sit seeded — Sunday 11am hybrid. Theravada/Insight. | ✅ Live heartbeat 33 |
| Center for Pragmatic Buddhism STL (5007 Waterman Blvd, St. Louis MO 63108) | Recurring sit seeded — Thursday 7pm in-person at First Unitarian Church. Chan/Zen/Pragmatist. | ✅ Live heartbeat 33 |

Missouri state + St. Louis/Maplewood/Brentwood cities added to `_filters.html`.
Center bios added to centers.py for all 3 centers.
`ingestion/sources/st_louis.py` created, wired into coordinator + abraxis.
`sangha-seed-recurring.js`: 2 new sit defs (Sunday Sangha STL + CPB STL). Now 162 sit defs → 3279 instances.

**Research notes (2026-05-14):**
- Confluence Zen Center STL (confluencezen.org): SZBA-authorized teacher Daigaku Rumme.
  Address: 3544 Oxford Ave, Maplewood MO 63143 (also listed as 7112 St. James Square in
  older entries — same corner building). Active ai1ec iCal feed with RRULE-based recurring
  events. Morning Zazen Mon/Tue/Thu 6:20am confirmed live in feed.
- Sunday Sangha STL (sundaysangha-stl.org): Insight Meditation community in Brentwood.
  Every Sunday 11am–12:30pm hybrid. Venue address not published publicly (email-list only).
  Free; donation-based space rental.
- Center for Pragmatic Buddhism STL (pragmaticbuddhism.org/stlouis): Thu 7–8:30pm Central
  at First Unitarian Church of St. Louis. Syncretic Nikayan/Chan/Zen/Pragmatist approach.
- St. Louis Shambhala: stlouis.shambhala.org redirects to main shambhala.org — likely
  closed/inactive. Skip.
- Missouri Zen Center (missourizencenter.org, 220 Spring Ave, Webster Groves): 500 error
  on iCal endpoint. Schedule not publicly accessible. Defer.
- Mid-America Buddhist Association (maba-usa.org): Chinese Chan, open Fri/Sat/Sun.
  Primarily devotional; no structured public sit calendar found. Defer.

**Skipped/deferred:**
- St. Louis Shambhala: appears inactive/merged
- Missouri Zen Center: 500 error on iCal — monitor for recovery
- Mid-America Buddhist Association: devotional focus, no public sit calendar accessible

---

### Chicago — Kadampa Chicago Eventbrite added May 8

| Center | Approach | Status |
|--------|----------|--------|
| Kadampa Meditation Center Chicago (Hyde Park) | Eventbrite organizer_id: 32772634747 | ✅ Live May 8 — 4 upcoming events confirmed (classes, retreats, special programs). Added to chicago.py CENTERS_EXTRA + EVENTBRITE_FEEDS. |

---

### NYC Phase 3d — Deferred

| Center | Approach |
|--------|----------|
| Village Zendo | HARD: JS-rendered (Divi + EventOrganiser plugin), no iCal found, no `__NEXT_DATA__`. Needs headless browser. |

---

### Cincinnati Phase 3 — ✅ Live May 15 (3 centers, heartbeat 34)

| Center | Approach | Status |
|--------|----------|--------|
| Cincinnati Zen Center (6015 Vine St, Cincinnati OH 45216) | Recurring sits seeded — JS-rendered calendar, no iCal. Sun 8am, Mon 7pm, Wed 5:30pm, Thu 7pm in-person; Sat 8:30am online. Korean/Soto Zen. Furnace Mountain Sangha lineage. | ✅ Live heartbeat 34 |
| Buddhist Dharma Center of Cincinnati (15 Moline Court, Northside, OH 45223) | Recurring sits seeded — Joomla JEvents calendar, iCal export 403. Daily 7am Zoom, Sun 10am hybrid, Tue 7pm in-person, Wed 7pm hybrid. Ecumenical/Theravada-leaning. | ✅ Live heartbeat 34 |
| Gaden Samdrupling Buddhist Monastery (3046 Pavlova Drive, Colerain Township OH 45251) | Recurring sit seeded — custom visual calendar, no iCal. Wed 7–8pm Open Meditation (public drop-in). Gelugpa Tibetan (Gaden lineage). | ✅ Live heartbeat 34 |

Ohio state + Cincinnati city added to `_filters.html`.
Center bios added to centers.py for all 3 centers.
`ingestion/sources/cincinnati.py` created (no active iCal feeds).
`sangha-seed-recurring.js`: 10 new sit defs (CZC ×5, BDCC ×4, GSL ×1). Now 172 sit defs → 3487 instances.

**Research notes (2026-05-15):**
- Cincinnati Zen Center (cincinnatizencenter.org): Founded under Zen Master Dae Gak (Furnace
  Mountain Sangha). Korean Kwan Um / Soto Zen. Calendar page is JS-rendered — no accessible
  iCal feed. Confirmed schedule: Sun 8am, Mon 7pm, Wed 5:30pm, Thu 7pm in-person; Sat 8:30am Zoom.
- Buddhist Dharma Center (cincinnatidharma.org): 15 Moline Court, Northside neighborhood.
  Ecumenical/non-sectarian (Theravada-leaning). JEvents (Joomla) calendar — iCal export
  endpoint returns 403. Daily 7am Zoom (all 7 days), Sun 10am hybrid, Tue 7pm in-person,
  Wed 7pm hybrid instruction+discussion.
- Gaden Samdrupling (gslmonastery.org): Tibetan Gelug monastery, West Side. Wed 7pm Open
  Meditation specifically listed as public drop-in. Custom visual calendar, no iCal.
- Cincinnati Shambhala: No active web presence found — defunct. Skip.
- Tri-State Dharma: Insight Meditation, currently Zoom-only. Deferred.
- Loveland Zen (Grailville, ~20 miles NE): Monday evenings hybrid. Deferred — outer suburb.
- Being Peace Sangha (beingpeacecommunity.org): Thich Nhat Hanh lineage, online-only.

**Skipped/deferred:**
- Cincinnati Shambhala: defunct
- Tri-State Dharma: Zoom-only
- Loveland Zen: 20 miles NE of city center
- Being Peace Sangha: online-only

---

### Kansas City Phase 3 — ✅ Live May 15 (2 centers, heartbeat 35)

| Center | Approach | Status |
|--------|----------|--------|
| Rime Buddhist Center (2939 Wayne Ave, Waldo/Brookside, KC MO 64109) | Recurring sits seeded — custom website calendar, no iCal. Mon–Fri noon, Mon 7pm Zen, Wed 7pm Group Meditation, Thu 7pm Tibetan practice, Sun 10:30am Service. Non-sectarian Rimé pluralist; 30+ years. | ✅ Live heartbeat 35 |
| Kansas Zen Center — KC branch (Unity Temple on the Plaza, 707 W 47th St, KC MO 64112) | Recurring sit seeded — per-event ICS only, no subscription feed. Thu 7pm in-person. Kwan Um School of Zen. | ✅ Live heartbeat 35 |

Kansas City city added to MO state filter in `_filters.html`.
Center bios added to centers.py for both centers.
`ingestion/sources/kansas_city.py` created (no active iCal feeds).
`sangha-seed-recurring.js`: 6 new sit defs (Rime ×5, KZC ×1). Now 178 sit defs → 3617 instances.

**Research notes (2026-05-15):**
- Rime Buddhist Center (rimecenter.org): 2939 Wayne Ave, Waldo/Brookside. Non-sectarian Rimé
  philosophy — all four Tibetan schools + Zen. 30+ years active. Most active KC center.
  No iCal feed; custom website calendar. Confirmed schedule from website.
- Kansas Zen Center KC branch (kansaszencenter.org): Meets at Unity Temple on the Plaza,
  707 W 47th St (47th & Jefferson). Kwan Um School of Zen. KC branch: Thu 7pm in-person only.
  Per-event ICS links on Events page; no centralized subscription feed.
- Temple Buddhist Center / IMCKC (templebuddhistcenter.com): Vipassana/Theravada-leaning,
  also at Unity Temple. JS-rendered Squarespace calendar; specific sit times not confirmed.
  Deferred for now.
- Shambhala Kansas City: Defunct (kcshambhala.org gone). Skip.
- Heartland Community of Mindful Living (Plum Village): Online-only Zoom. Deferred.

**Skipped/deferred:**
- Temple Buddhist Center / IMCKC: Squarespace JS-rendered calendar, times unconfirmed
- Shambhala KC: defunct
- Heartland Community of Mindful Living: online-only

---

### Richmond VA Phase 3 — ✅ Live May 15 (4 centers, heartbeat 36)

All centers meet at **Ekoji Buddhist Sangha** (3411 Grove Ave, Fan District, Richmond VA 23221) — a multi-tradition Buddhist community hub.

| Center | Approach | Status |
|--------|----------|--------|
| Insight Meditation Community of Richmond / IMCR (imcrva.org) | WordPress iCal feed (`?ical=1`, Chrome UA) for retreats/specials + Tue 7pm + Fri 5:45pm weekly sits seeded. Theravada/Vipassana. | ✅ Live heartbeat 36 |
| Richmond Zen (richmondzen.org) | Recurring sits seeded — Soto Zen (Branching Streams/Shunryu Suzuki). Sun 9am, Tue 6:30am, Wed 7pm, Fri 6:30am. All in-person. | ✅ Live heartbeat 36 |
| Nyama Sangha (ekojirichmond.org/richmond-shambhala/) | Recurring sit seeded — Shambhala-lineage, Sat 10:30am hybrid. | ✅ Live heartbeat 36 |
| Palpung Shenpen Tharchin (palpungrichmond.org) | Recurring sit seeded — Tibetan Kagyu (Palpung), teacher Lama Linda. Thu 7pm hybrid; rotating practices by week. | ✅ Live heartbeat 36 |

Virginia state + Richmond city added to `_filters.html`.
Center bios added to centers.py for all 4 centers.
`ingestion/sources/richmond.py` created with CENTERS + IMCR ICAL_FEEDS.
`sangha-seed-recurring.js`: 8 new sit defs (IMCR ×2, Richmond Zen ×4, Nyama ×1, Palpung ×1). Now 186 sit defs → 3721 instances.

**Research notes (2026-05-15):**
- IMCR iCal feed (`imcrva.org/?ical=1`): WordPress Events Calendar, blocks default httpx UA
  with 406; Chrome UA succeeds. Feed contains only retreats and special off-site events
  (not regular weekly sits). Weekly sits (Tue 7pm, Fri 5:45pm) seeded as recurring.
- Richmond Zen: Soto Zen, Branching Streams lineage. No iCal; static WordPress site.
  Confirmed schedule from website. Guiding teacher: Josho Phelan Roshi.
- Nyama Sangha: Richmond Shambhala-derived community at Ekoji. No dedicated website.
- Palpung Shenpen Tharchin: Kagyu lineage. Thu 7pm confirmed; 4th Sun 2pm teaching
  NOT seeded (low attendance monthly events — would need week_of_month=4).

**Skipped/deferred:**
- Integral Zen (at Ekoji): Mon 7–8:45pm. Ken Wilber/integral-influenced — unclear Buddhist tradition; deferred
- Meditative Inquiry (at Ekoji): Sun 7–8:45pm + Wed 12:15pm Zoom. Non-traditional — deferred
- Pure Land (at Ekoji): Sat 2pm. Pure Land devotional — deferred
- Won Buddhism of Richmond (Mechanicsville): 20 miles north — deferred
- Guhyasamaja Center (Fairfax VA): DC metro suburb, 45 miles north — covered under DC expansion if needed

### Columbus OH Phase 3 — ✅ Live May 16 (5 centers, heartbeat 37)

| Center | Approach | Status |
|--------|----------|--------|
| Columbus Karma Thegsum Choling / KTC (645 W. Rich St, Franklinton, Columbus OH 43215) | WordPress Events Calendar iCal feed (`columbusktc.org/events/?ical=1`). Karma Kagyu (affiliated with KTD monastery). Founded 1977. | ✅ Live heartbeat 37 — Sun 10am Intro Meditation (hybrid) + 11:30am Dharma Talk; Tue 7pm Chenrezig (virtual); Wed 12:15pm Midday Meditation (virtual). |
| Mud Lotus Sangha (17 E. Tulane Rd, Clintonville / ILLIO Studios, Columbus OH 43202) | Recurring sits seeded — Squarespace, no master iCal feed. Most active Zen community in Columbus. | ✅ Live heartbeat 37 — Tue 7:30am Morning Sit (in-person), Wed 7pm Evening Zen (in-person), Thu 9am Morning Meditation (hybrid). |
| Zen Columbus Sangha (93 W. Weisheimer Rd, First UU Church, Clintonville, Columbus OH 43214) | Recurring sits seeded — static HTML schedule, no iCal. Independent Soto Zen community. | ✅ Live heartbeat 37 — Tue 7pm + Sat 8:30am zazen, both hybrid. |
| Central Ohio Center for Pragmatic Buddhism / COCPB (77 N. Brinker Ave, West Side, Columbus OH 43204) | Recurring sit seeded — Wix site, no iCal. Private residence zendo. | ✅ Live heartbeat 37 — Sun 9:30am zazen + dharma talk (in-person). |
| Bliss Run Sangha (4211 Maize Rd, Unity Church, North Linden, Columbus OH 43224) | Recurring sit seeded — static site, no iCal. Plum Village lineage. | ✅ Live heartbeat 37 — Thu 7pm walking meditation + sitting + dharma discussion (in-person). |

Columbus city added to OH state filter in `_filters.html`.
Center bios added to centers.py for all 5 centers.
`ingestion/sources/columbus.py` created with CENTERS + KTC ICAL_FEEDS.
`sangha-seed-recurring.js`: 8 new sit defs (KTC ×1, Mud Lotus ×3, Zen Columbus ×2, COCPB ×1, Bliss Run ×1). 186 → 194 sit defs.

**Research notes (2026-05-16):**
- Columbus KTC: iCal confirmed. Most active Tibetan center in Columbus; 40+ years.
- Columbus Shambhala (1271 E. Cooke Rd): Calendar empty as of May 2026 — monitor for revival.
- BBAC (5208 Dierker Rd): Website offline — skip until restored.
- NKT / Kadampa Columbus: no NKT center found in Columbus metro.
- Grove City Zen: website ECONNREFUSED — likely inactive.

**Skipped/deferred:**
- Columbus Shambhala: no active events on calendar — monitor
- Bodhi Buddhist Association (BBAC): website offline — monitor
- NKT Columbus: no center found in Columbus

---

### Raleigh-Durham-Chapel Hill NC Phase 3 — ✅ Live May 16 (3 centers, heartbeat 38)

| Center | Approach | Status |
|--------|----------|--------|
| Durham Shambhala Meditation Center (733 Rutherford St, Durham NC 27705) | Recurring sits seeded — Shambhala custom WordPress, no iCal. | ✅ Live — Sun 9am–noon (in-person), Thu 7pm Open House (in-person), Sat 10:30am Dharma Discussions (Zoom), Wed 7pm Heart of Recovery (in-person). |
| Chapel Hill Zen Center (5322 NC Hwy 86, Chapel Hill NC 27514) | Recurring sits seeded — WordPress ?ical=1 returns 404. Soto Zen, SFZC lineage. | ✅ Live — Mon–Fri 6am morning zazen (hybrid), Tue 7pm evening zazen (in-person), Sun 9am zazen (in-person). |
| North Carolina Zen Center (390 Ironwood Rd, Pittsboro NC 27312) | Recurring sits seeded — WP Events Calendar iCal returns empty (0 bytes). 15 acres, Teshin Roshi. | ✅ Live — Sun 10am practice (in-person), Mon Zoom zazen, Tue 7pm dharma study (in-person), Wed/Fri 7am hybrid zazen, Thu 7pm chanting + zazen (in-person). |

NC state + Chapel Hill/Durham/Pittsboro city filters added to `_filters.html`.
Center bios added to centers.py for all 3 centers.
`ingestion/sources/raleigh.py` created with CENTERS registry.
`sangha-seed-recurring.js`: 12 new sit defs. 194 → 206 sit defs.

**Skipped/deferred:**
- Kadampa Center Raleigh (FPMT, kadampa-center.org): Drupal 7, JS-rendered calendar — no accessible iCal. Monitor for API access.
- Kosala Kadampa Triangle (NKT, meditationinthetriangle.org): Squarespace, no iCal.
- Sit Raleigh (sitraleigh.com): Tiny community, Tue 7pm only. Could seed if requested.

---

### Salt Lake City UT Phase 3 — ✅ Live May 16 (2 centers, heartbeat 39)

| Center | Approach | Status |
|--------|----------|--------|
| Two Arrows Zen (21 G Street, The Avenues, Salt Lake City UT 84103) | Recurring sits seeded — EventON AJAX calendar, no static iCal. Mon–Fri 7am Morning Zazen + Thu 5:30pm Evening Zen Service. Soto Zen, White Plum Asanga lineage. | ✅ Live heartbeat 39 |
| Urgyen Samten Ling Gonpa (740 S 300 West, Downtown, Salt Lake City UT 84101) | Recurring sit seeded — Wix site, no iCal. Sun 10am Chenrezig Practice (Zoom/online). Nyingma Tibetan (Dzogchen). | ✅ Live heartbeat 39 |

Utah state + Salt Lake City city added to `_filters.html`.
Center bios added to centers.py for both centers.
`ingestion/sources/salt_lake_city.py` created (CENTERS registry, no iCal feeds).
`sangha-seed-recurring.js`: 3 new sit defs (Two Arrows ×2, Urgyen Samten Ling ×1). 206 → 209 sit defs.

**Research notes (2026-05-16):**
- SLC has a small but earnest Buddhist community in a heavily LDS region.
- Two Arrows Zen: Well-established Soto Zen zendo in the Avenues. Genro Gauntt Roshi.
  EventON AJAX calendar — no static iCal. Mon–Fri 7am (two periods) + Thu 5:30pm confirmed.
- Urgyen Samten Ling: Nyingma gonpa near downtown. Khenpo Ugyen Tenzin Rinpoche.
  Wix site, no iCal. Sunday 10am Chenrezig (Zoom) + Friday 10am Green Tara (Zoom) +
  Saturday 10am Ngondro (Zoom). Only Chenrezig seeded as primary public sit.
- SLC Shambhala (saltlake.shambhala.org): Redirects to shambhalanetwork.org — center
  appears to have reorganized under the disaffiliated Shambhala Network. No schedule
  accessible. Monitor for recovery.
- Katog Janaling (katogjanaling.org): Nyingma, 3540 S 2208 E Keller Lane. Meetup-based;
  specific weekly sit schedule not confirmed. Deferred.
- Salt Lake Buddhist Temple (slbuddhist.org): Squarespace. Jodo Shinshu (Pure Land),
  primarily devotional. Deferred.

**Skipped/deferred:**
- SLC Shambhala: redirected, no accessible schedule — monitor
- Katog Janaling: weekly schedule unconfirmed via website — monitor
- Salt Lake Buddhist Temple: Pure Land / devotional focus — deferred
- Salt Lake Buddhist Fellowship: Jodo Shinshu, WordPress.com — deferred

---

### New Orleans LA Phase 3 — ✅ Live May 17 (2 centers, heartbeat 40)

| Center | Approach | Status |
|--------|----------|--------|
| New Orleans Zen Temple (8338 Oak St 2nd Fl, Riverbend, New Orleans LA 70118) | Recurring sits seeded — Squarespace site, no iCal. AZI / Taisen Deshimaru lineage, founded 1983, Robert Livingston Roshi. | ✅ Live heartbeat 40 — Tue 7pm hybrid, Thu 6:30am in-person, Sun 10am in-person. |
| Mid City Zen (3248 Castiglione St, Mid-City, New Orleans LA 70119) | Google Calendar ICS (decoded from base64 iframe src) + recurring sits seeded for regular morning zazen. Suzuki Roshi / SFZC lineage, peer-led since 2011. | ✅ Live heartbeat 40 — Mon/Wed/Fri 8am hybrid, Sun 9:30am hybrid. Google Calendar wired for special events (dharma talks, retreats, identity sits). Note: calendar is historically focused — 0 future events as of May 2026; will auto-populate if calendar is updated. |

Louisiana state + New Orleans city added to `_filters.html`.
Center bios added to centers.py for both centers.
`ingestion/sources/new_orleans.py` created with CENTERS + ICAL_FEEDS.
`sangha-seed-recurring.js`: 5 new sit defs. 209 → 214 sit defs → 4228 instances.
61 events in 60-day window verified on live API.

**Research notes (2026-05-17):**
- Mid City Zen Google Calendar: active feed but all historical events (most recent March 2026).
  Regular sits best covered as recurring; iCal will capture future special events if maintained.
- NOIMG (noimg.org): domain offline as of research. Theravada, Tue 7:30pm + Sat 3pm at Aikido
  of New Orleans (3124 Magazine St). Monitor for recovery.
- Sangha House NOLA (sanghahousenola.org): Opened 2024, Tremé neighborhood. Multi-tradition,
  community-focused (Black, queer). Wix site, schedule unclear. Monitor for confirmed schedule.
- Samten Choling (samtenchoeling.org): Tibetan Gelugpa, 7803 Nelson St. Founded 2020. Calendar
  is dynamic. Monitor for iCal access.
- MCGNO (mcgno.org): Plum Village tradition. Announced weekly group dissolution late 2024. Skip.

**Skipped/deferred:**
- NOIMG: domain offline — monitor for recovery
- Sangha House NOLA: schedule unconfirmed on website — monitor
- Samten Choling: dynamic calendar, no iCal — monitor

---

### Tampa Bay FL Phase 3 — ✅ Live May 17 (4 centers, heartbeat 41)

| Center | Approach | Status |
|--------|----------|--------|
| Kadampa Meditation Center Tampa Bay (201 6th Ave S, Safety Harbor FL 34695) | Recurring sits seeded — Wix site, no iCal. NKT Tibetan. | ✅ Live heartbeat 41 — Sun 10am, Tue 10am, Thu 7pm in-person. |
| Clear Water Zen Center (2476 Nursery Rd, Clearwater FL 33764) | Recurring sits seeded — Google Sites, no iCal. Non-sectarian Zen. | ✅ Live heartbeat 41 — Sun 9:30am, Mon 7pm, Wed 6:45pm (beginner), Fri 7pm in-person. |
| Florida Community of Mindfulness (6501 N Nebraska Ave, Tampa FL 33604) | Wild Apricot RSS (`/page-1861378/RSS`) — 39 events. Daily 7am Morning Meditation + Sun 9:30am. Plum Village / Thich Nhat Hanh, teacher Fred Eppsteiner. | ✅ Live heartbeat 41 — RSS wired in coordinator + abraxis. |
| Shambhala Meditation Center of St. Petersburg (5901 Haines Rd N, St. Petersburg FL 33714) | Recurring sits seeded — dynamic WordPress, no accessible iCal. | ✅ Live heartbeat 41 — Sun 10am in-person, Tue 7pm online. |

FL state cities Tampa/Clearwater/Safety Harbor/St. Petersburg added to `_filters.html`.
Center bios in centers.py; `ingestion/sources/tampa.py` created with CENTERS + RSS_FEEDS.
`sangha-seed-recurring.js`: 9 new sit defs. 214 → 223 sit defs → 4345 instances.

**Skipped/deferred:**
- Samadhi Buddhist Meditation Center (St. Pete): small Wix sangha, Wed 7:30pm — deferred
- Florida Buddhist Vihara: temple-focused, no public drop-in sits confirmed

---

### Charlotte NC Phase 3 — ✅ Live May 17 (4 centers, heartbeat 42)

| Center | Approach | Status |
|--------|----------|--------|
| Charlotte Buddhist Vihara (3423 Stonehaven Dr, Charlotte NC 28215) | Recurring sits seeded — iCal (tribe_events) Cloudflare-blocked. Theravada, Ayya Sudhamma. | ✅ Live heartbeat 42 — Tue 6pm, Wed 10:30am, Thu 7pm, Sat 2pm hybrid. |
| Insight Meditation Community of Charlotte (3900 Park Road, Charlotte NC 28209) | Recurring sits seeded — iCal (MEC/WP) Cloudflare-blocked. Vipassana. | ✅ Live heartbeat 42 — Tue 12pm (Zoom), Wed 7:30pm (hybrid). |
| Kadampa Meditation Center North Carolina (528 East Blvd, Charlotte NC 28203) | Recurring sits seeded — Wix site, no iCal. NKT Tibetan. | ✅ Live heartbeat 42 — Sun 9:30am, Tue 5pm, Wed 5pm, Thu 5pm, Sat 10am in-person. |
| Charlotte Community of Mindfulness (1931 Selwyn Ave, Charlotte NC 28207) | Recurring sits seeded — no iCal. Plum Village / Thich Nhat Hanh. | ✅ Live heartbeat 42 — Sun 8:30am hybrid. |

Charlotte city filter added to `_filters.html`. Center bios in centers.py.
`ingestion/sources/charlotte.py` created; coordinator + abraxis wired.
`sangha-seed-recurring.js`: 12 new sit defs. 223 → 235 sit defs → 4501 instances.

**Skipped/deferred:**
- Charlotte Zen Meditation Society (726 East Blvd): Meetup exists, 0 upcoming events — monitor
- Greatwoods Zen (2631 Buckleigh Dr, east Charlotte): Plum Village, Squarespace 404 — monitor
- Charlotte True Buddha Temple: Vajrayana/Chinese Tantric, no calendar system
- Charlotte Vipassana Group (Goenka): private sits for established students only

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

### Shambhala Berkeley / SF / LA iCal
- `shambhala-koeln.de` server came back online 2026-05-08 (was down since ~Apr 2026)
- Berkeley (center=178): 408 events — re-added to east_bay.py ICAL_FEEDS
- SF (center=177): 120 events — newly wired to live feed (was manually seeded only)
- LA (center=208): 388 events — new center; wired in la.py ICAL_FEEDS
- DC (center=205), Boulder (center=191), Denver (center=218): valid iCal but 0 events — may be inactive chapters or different calendar IDs. Monitor.

---

## Research Docs

| File | Contents |
|------|----------|
| `memory/research-eastbay-meditation-calendar.md` | 16 East Bay centers, Phase 1–4 breakdown, notes per center |
| `memory/research-east-bay-buddhist-calendar-aggregation.md` | Detailed center registry, iCal URLs, scraping difficulty ratings |
| `memory/research-sf-marin-meditation-calendar.md` | SF + Marin expansion (10 centers, pipeline summary) |
| `journals/llm/abraxis-proposals/sangha-calendar-imc-missing-title-bug.md` | IMC Berkeley bug report + fix spec |
