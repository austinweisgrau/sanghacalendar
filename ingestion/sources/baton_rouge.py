"""
Baton Rouge, Louisiana — Phase 3 expansion (heartbeat 92).

Baton Rouge (pop. ~870k metro, state capital of Louisiana) has a modest but
genuine Buddhist meditation community with Theravada and Vietnamese Mahayana
representation. No Zen, Tibetan, or Shambhala center confirmed in the city.

Centers included:
  - Louisiana Buddhist Vihara / Blue Lotus Meditation Center (blue_lotus_br)
    Theravada (Sri Lankan lineage; Bhante Dhammadassi, chief abbot)
    8470 Goodwood Blvd, Baton Rouge LA 70806 (Unitarian Church of BR)
    louisianablbv.org · Wed 5:30–6:30pm (in-person), Sat 5:00–6:00pm (in-person)
    → No iCal; seeded as recurring in sangha-seed-recurring.js

  - Tam Bao Meditation Center (tam_bao_br)
    Vietnamese Mahayana / Plum Village lineage (Order of Interbeing)
    975 Monterrey Blvd, Baton Rouge LA 70815
    batonrougebuddha.org · Fri 7:30pm (English-language sits + mindfulness)
    → Regular weekly sits seeded as recurring; special retreats via Eventbrite
    → Eventbrite organizer ID: 120793865302

Research notes (2026-07-28):
  - Blue Lotus / Louisiana BLBV: First Sri Lankan Buddhist temple in Louisiana,
    founded 2018. Chief abbot: Bhante Dhammadassi. Meets at the Unitarian Church
    of Baton Rouge, 8470 Goodwood Blvd (a shared venue arrangement). Publicly
    accessible guided meditation sessions on Wednesday evenings 5:30–6:30pm
    (in-person) and Saturday afternoons 5–6pm (in-person). Also Wednesday 7pm
    Zoom session. Focuses on loving-kindness (metta) and mindfulness. Welcomes
    all backgrounds. Contact: louisianabluelotus@gmail.com. Active Instagram:
    @bluelotustemplelouisiana. louisianablbv.org.
  - Tam Bao Meditation Center: Vietnamese Buddhist temple founded 1985 at
    975 Monterrey Blvd, Baton Rouge LA 70815. One of the oldest and largest
    Buddhist centers in Louisiana. Abbot: Thich Dao Quang. Meditation hall
    accommodates 150 practitioners. Regular sessions: Tue/Thu/Sat 7:30pm
    (primarily Vietnamese-language), Fri 7:30pm (English-language sits and
    mindfulness practice open to all). Special events (Days of Mindfulness,
    summer retreats) listed on Eventbrite (organizer ID: 120793865302).
    Contact: tambaobr@yahoo.com / (225) 248-8263. batonrougebuddha.org.
  - No Shambhala center in Baton Rouge (nearest: New Orleans).
  - No independent Tibetan or Zen center found in Baton Rouge.
  - Order of Interbeing group historically at same Goodwood Blvd location
    appears to be inactive / merged into BLBV programming.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "blue_lotus_br": Center(
        id="blue_lotus_br",
        name="Louisiana Buddhist Vihara — Blue Lotus Meditation Center",
        url="https://www.louisianablbv.org",
        address="8470 Goodwood Boulevard",
        city="Baton Rouge",
        state="LA",
        zip_code="70806",
        lat=30.4516,
        lng=-91.0798,
        neighborhood="Mid City",
        tradition=Tradition.THERAVADA,
        notes=(
            "Louisiana Buddhist Vihara / Blue Lotus Meditation Center is the first "
            "Sri Lankan Theravada Buddhist temple in Louisiana, founded in 2018. "
            "Chief abbot: Bhante Dhammadassi. Meets at the Unitarian Church of "
            "Baton Rouge, 8470 Goodwood Boulevard, Baton Rouge LA 70806 (Mid City). "
            "Public guided meditation sessions: Wednesday 5:30–6:30pm in-person "
            "(metta and mindfulness); Saturday 5:00–6:00pm in-person. "
            "All backgrounds welcome. Free (dana). "
            "Contact: louisianabluelotus@gmail.com. louisianablbv.org."
        ),
    ),
    "tam_bao_br": Center(
        id="tam_bao_br",
        name="Tam Bao Meditation Center",
        url="https://www.batonrougebuddha.org",
        address="975 Monterrey Boulevard",
        city="Baton Rouge",
        state="LA",
        zip_code="70815",
        lat=30.4618,
        lng=-91.0551,
        neighborhood="Broadmoor",
        tradition=Tradition.ZEN,
        notes=(
            "Tam Bao Meditation Center is a Vietnamese Buddhist temple and "
            "meditation center at 975 Monterrey Boulevard, Baton Rouge LA 70815 "
            "(Broadmoor neighborhood), founded in 1985. One of the largest and "
            "oldest Buddhist centers in Louisiana. Abbot: Thich Dao Quang. "
            "Affiliated with the Order of Interbeing (Thich Nhat Hanh lineage). "
            "English-language meditation and mindfulness sits: Friday 7:30pm, open "
            "to all backgrounds. Vietnamese-language sessions: Tuesday, Thursday, "
            "and Saturday 7:30pm. Special events (Days of Mindfulness, retreats) "
            "on Eventbrite. Hall capacity: 150. "
            "Contact: tambaobr@yahoo.com / (225) 248-8263. batonrougebuddha.org."
        ),
    ),
}

# Tam Bao Meditation Center — Eventbrite organizer ID: 120793865302
# Used for Days of Mindfulness and seasonal retreats (not regular weekly sits).
EVENTBRITE_FEEDS = {
    "tam_bao_br": {
        "organizer_id": "120793865302",
        "filter_to_sits": False,  # Days of Mindfulness / retreats are the primary draw
    },
}

# No live iCal feeds — regular sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
