# Sangha Calendar

**Every in-person meditation sit in the US, in one place. Free forever.**

Sangha Calendar is a public aggregator for meditation events — zazen, vipassana, open sits, drop-in groups — scraped from hundreds of centers and served as a filterable calendar anyone can subscribe to.

## Vision

Two components:

1. **Ingestion Engine** — LLM-assisted agent swarm that discovers, scrapes, and normalizes meditation events from centers across the US. Handles iCal feeds, Eventbrite, WordPress, Squarespace, and static HTML alike.

2. **Serving Layer** — Public website with map + list views, tradition/type/location filters, and personalized ICS subscription URLs you can load directly into Google Calendar or Apple Calendar.

No ads. No accounts required. Donation button. Built as a public service for practitioners.

## Why Now

LLMs make event extraction and classification trivially cheap. Scraping at national scale used to be painful — now it's a solved problem. Estimated cost at full national scale: ~$60/year in LLM API costs.

## Project Status

**Phase 0 (current):** Infrastructure setup. East Bay prototype with 16 mapped centers, 3 live iCal feeds.

## Architecture

### Ingestion (Agent Swarm)

```
coordinator/
├── discovery_agent.py    # Find new centers (Google Maps, Yelp, directories)
├── scraper_agent.py      # Extract events from a center's web presence
├── classifier_agent.py   # Filter: is this actually a meditation sit?
└── normalizer_agent.py   # Map to canonical event schema

scrapers/
├── ical_feed.py          # Subscribe to existing iCal feeds (zero-maintenance)
├── eventbrite.py         # Eventbrite API
├── wordpress_events.py   # WordPress Events Calendar plugin (?ical=1 endpoints)
├── squarespace.py        # Squarespace event pages
└── static_html.py        # LLM-assisted extraction from static calendars
```

Events flow through: `discover → scrape → classify → normalize → store`

### Serving

```
serving/
├── app.py               # Flask/FastAPI web app
├── templates/           # Calendar views (map, list, month)
└── static/              # CSS, JS
```

Outputs:
- Web UI with filters (tradition, location, day/time, accessibility)
- ICS subscription URLs (personalized by filter)
- GCal/iCal deep links

### Data Model

Each event:
```json
{
  "id": "...",
  "org_name": "East Bay Meditation Center",
  "org_jid": "ebmc",
  "title": "BIPOC Sangha Sit",
  "tradition": "vipassana",
  "address": "285 17th St, Oakland, CA 94612",
  "neighborhood": "Uptown Oakland",
  "lat": 37.8076,
  "lng": -122.2697,
  "day_of_week": "Tuesday",
  "time_start": "19:00",
  "time_end": "20:30",
  "recurrence": "weekly",
  "url": "https://eastbaymeditation.org/...",
  "notes": "Open to all BIPOC practitioners",
  "source": "ical_feed",
  "last_verified": "2026-04-22"
}
```

## Local Prototype — East Bay

16 centers mapped. Tiered by data availability:

| Phase | Approach | Centers |
|-------|----------|---------|
| 1 | Direct iCal subscribe | IMC Berkeley, EBMC, Berkeley Shambhala |
| 2 | Eventbrite API / light scrape | Nyingma Institute, Insight Berkeley |
| 3 | WP iCal endpoint test | Empty Gate Zen, Everyday Zen, Metta Dharma |
| 4 | Static scrape / manual | Bay Zen, Berkeley Priory, Spirit Rock, BBM |

## Roadmap

- [ ] Phase 0: Repo setup, schemas, local dev environment
- [ ] Phase 1: East Bay MVP — subscribe to 3 live iCal feeds, filter to sits, serve basic calendar
- [ ] Phase 2: Add scraper agents for remaining East Bay centers
- [ ] Phase 3: National expansion — top 10 metro areas
- [ ] Phase 4: Full US coverage via discovery agent swarm
- [ ] Phase 5: Public launch, ICS subscriptions, GCal links

## Contributing

PRs welcome. If you know of a meditation center whose events should be included, open an issue.

## License

MIT
