"""
Corpus Christi, Texas — Phase 3 expansion (heartbeat 96).

Corpus Christi (pop. ~330k metro, Coastal Bend region) has a small Buddhist
community anchored by Chua Huong Dam, described locally as "the only Buddhist
temple in the Coastal Bend." The center offers English-language Friday evening
meditation and Sunday services open to all backgrounds.

Centers included:
  - Chua Huong Dam Buddhist Center (chua_huong_dam_corpus_christi)
    Vietnamese Mahayana (Pure Land / Zen mix)
    1305 Farm To Market 43, Corpus Christi TX 78415
    No public website found; local press coverage confirms public programming.
    → Friday ~7pm English-language meditation (drop-in); Sunday 10am services
    → Seeded as recurring (no iCal)

Research notes (2026-08-07):
  - Chua Huong Dam: Vietnamese Mahayana temple described by KRISTV local news
    as "the only Buddhist temple in the Coastal Bend." Offers Friday evening
    English-language sitting meditation (chant, silent sit, walking meditation)
    explicitly open to newcomers and all backgrounds. Sunday 10am general
    service also open to the public. Phone: (361) 851-2680. Northwest side
    of Corpus Christi near FM 43.
  - Wat Corpus Buddhavanaram (1206 S Clarkwood Rd): Thai Theravada temple,
    Facebook presence only. No confirmed public drop-in schedule. Monitor for
    future addition when schedule is clarified.
  - Nalandabodhi Texas (6121 Coral Ridge Dr): Very small Tibetan study group,
    likely private/Zoom-only. No confirmed public sits. Deferred.
  - Bodhidhamma Buddhist Temple (7733 Outreau Dr): Low web presence, likely
    private ethnic community temple. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "chua_huong_dam_corpus_christi": Center(
        id="chua_huong_dam_corpus_christi",
        name="Chùa Hương Đàm Buddhist Center",
        url="https://www.facebook.com/profile.php?id=100063487073714",
        address="1305 Farm To Market 43",
        city="Corpus Christi",
        state="TX",
        zip_code="78415",
        lat=27.7923,
        lng=-97.4457,
        neighborhood="Northwest Corpus Christi",
        tradition=Tradition.OTHER,
        notes=(
            "Chùa Hương Đàm Buddhist Center is a Vietnamese Mahayana temple "
            "(Pure Land / Zen mix) at 1305 Farm To Market 43, Corpus Christi TX 78415, "
            "described locally as 'the only Buddhist temple in the Coastal Bend.' "
            "Friday evening: English-language meditation (chant, silent sit, walking "
            "meditation), open to newcomers and all backgrounds. "
            "Sunday 10am: weekly services, open to the public. "
            "Free. Phone: (361) 851-2680."
        ),
    ),
}

# No live iCal feeds — all sits seeded via sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
