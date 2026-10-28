"""
Sioux Falls, South Dakota — Phase 3 expansion (heartbeat 118).

Sioux Falls (pop. ~200k; metro ~270k) is South Dakota's largest city. The
Buddhist scene is small — one confirmed Vietnamese Mahayana temple with regular
public services.

Centers included:
  - Chua Ky Vien (chua_ky_vien)
    Vietnamese Mahayana (Pure Land / Zen mix)
    2601 S Marion Rd, Sioux Falls SD 57106
    chuakyvien.wordpress.com
    Sunday 10:00am–1:00pm services (chanting, prayers, meditation, dharma talk)
    No iCal — seeded as recurring.

Research notes (2026-10-28):
  - Chua Ky Vien (Wonderful Garden Buddhist Meditation Center): Founded December
    2013 by Venerable Thich Minh Dieu; current abbot Venerable Thich Minh Tong.
    Vietnamese Mahayana / Pure Land tradition. Sunday services run 3 hours (10am–
    1pm) and include chanting, prayers, seated meditation, walking meditation, and
    dharma talks in English. Daily hours 9am–9pm; drop-in visitors welcome.
    Annual festivals: Tet (Feb), Buddha's Birthday (May), Ullambana (Aug).
    Website inactive since ~2015; Facebook page most current presence:
    facebook.com/p/Chùa-Kỳ-Viên-Buddhist-Meditation-Center-100073870632482.
    EIN 46-3912687. thichminhdieu@gmail.com.
  - SD Buddhist Vihara: Same address as Chua Ky Vien (2601 S Marion Rd). Website
    southdakotabv.org is down (ECONNREFUSED). Administered from Minnesota Buddhist
    Vihara (Minneapolis) under Ven. Witiyala Seewalie Thero; (612) 522-1811;
    sdbuddhist@mnbv.org. Appears to be a satellite mission rather than an
    independent local congregation. Deferred pending confirmation of active local
    programming.
  - Heartland Meditation Center (zip 57103): Vipassana group listed in GoSit.org.
    No street address, no website (heartlandmeditation.org ECONNREFUSED), phone
    605-339-1098. Possibly dormant. Deferred.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "chua_ky_vien": Center(
        id="chua_ky_vien",
        name="Chua Ky Vien",
        url="https://chuakyvien.wordpress.com",
        address="2601 S Marion Rd",
        city="Sioux Falls",
        state="SD",
        zip_code="57106",
        lat=43.5003,
        lng=-96.7654,
        neighborhood="South Sioux Falls",
        tradition=Tradition.OTHER,
        notes=(
            "Chua Ky Vien (Wonderful Garden Buddhist Meditation Center) is a "
            "Vietnamese Mahayana temple at 2601 S Marion Rd, Sioux Falls SD. "
            "Founded in December 2013, the center holds Sunday services from "
            "10:00am–1:00pm, which include chanting, prayers, seated and walking "
            "meditation, and dharma talks in English. Abbot: Venerable Thich Minh "
            "Tong. All backgrounds welcome; dana-based. Daily hours 9am–9pm. "
            "thichminhdieu@gmail.com."
        ),
    ),
}

# ---------------------------------------------------------------------------
# Live iCal feeds
# ---------------------------------------------------------------------------

ICAL_FEEDS = {}
# No live iCal feeds — seeded via scripts/sangha-seed-recurring.js
