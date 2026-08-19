"""
Springfield, Missouri — Phase 3 expansion (heartbeat 100).

Springfield (pop. ~170k city, ~460k metro) is the third-largest city in Missouri
and the cultural hub of the Ozarks. Buddhist presence is small but active.

Centers included:
  - Ozarks Dharma Community (ozarks_dharma)
    Non-sectarian / Theravada-influenced (Insight tradition)
    National Avenue Christian Church, 1515 S National Ave, Springfield MO 65806
    ozarksdharma.org · Sat 9am + Thu 7pm (hybrid)
    Live Google Calendar iCal feed available

  - Dinh Quang Buddhist Temple (dinh_quang)
    Vietnamese Lâm Tế (Linji/Zen) + Pure Land, bilingual
    2901 W. High Street, Springfield MO 65803
    dinhquangtemple.com · Sun 9am + Wed 6pm English services (recurring seeded)

Research notes (2026-08-19):
  - Ozarks Dharma Community (ozarksdharma.org): Founded 2001, lay-led ecumenical
    community drawing on Insight teachers (Kornfield, Shinzen Young, Kenneth Folk).
    Saturday 9:00–10:15am + Thursday 7:00–8:30pm, hybrid in-person + Zoom.
    Monthly day-long silent retreats. Google Calendar publicly accessible at
    ozarksdharma@gmail.com.
  - Dinh Quang Buddhist Temple (dinhquangtemple.com): Vietnamese Zen (Lâm Tế /
    Linji lineage) + Pure Land. Sunday 9am English chanting + meditation, 10:30am
    Vietnamese service. Wednesday 6pm English chanting + meditation. Third Saturday
    Days of Mindfulness. Teacher: Giac Vien. Phone: 417-866-1095.
  - No Kadampa, Shambhala, or Tibetan centers found in Springfield.
  - Vo Uu Temple (1926 E Division St): Vietnamese temple with no online schedule;
    contact-only. Skipped — no verifiable public sit schedule.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "ozarks_dharma": Center(
        id="ozarks_dharma",
        name="Ozarks Dharma Community",
        url="https://www.ozarksdharma.org",
        address="1515 S National Ave",
        city="Springfield",
        state="MO",
        zip_code="65806",
        lat=37.1864,
        lng=-93.2875,
        neighborhood=None,
        tradition=Tradition.THERAVADA,
        notes=(
            "Ozarks Dharma Community is a lay-led non-sectarian meditation community "
            "founded in 2001. Rooted in the Insight/Vipassana tradition, drawing on teachers "
            "including Jack Kornfield, Shinzen Young, Kenneth Folk, and Daniel Ingram. "
            "Saturday mornings 9:00–10:15am and Thursday evenings 7:00–8:30pm, hybrid "
            "in-person at National Avenue Christian Church (Parlor Room) and Zoom. "
            "Monthly day-long silent retreats. Drop-in welcome, free. ozarksdharma.org."
        ),
    ),
    "dinh_quang": Center(
        id="dinh_quang",
        name="Dinh Quang Buddhist Temple",
        url="https://dinhquangtemple.com",
        address="2901 W High St",
        city="Springfield",
        state="MO",
        zip_code="65803",
        lat=37.2177,
        lng=-93.3213,
        neighborhood=None,
        tradition=Tradition.ZEN,
        notes=(
            "Dinh Quang Buddhist Temple is a Vietnamese Buddhist community in Springfield "
            "practicing in the Lâm Tế (Linji) Zen lineage blended with Pure Land. "
            "Bilingual (English and Vietnamese). English-language services open to all: "
            "Sunday 9:00am (chanting + meditation) and Wednesday 6:00pm (chanting + "
            "meditation), followed by Dharma class. Third Saturday Days of Mindfulness. "
            "Teacher: Giac Vien. Free and open to all. Phone: 417-866-1095. "
            "dinhquangtemple.com."
        ),
    ),
}

# Ozarks Dharma Community — public Google Calendar ICS
ICAL_FEEDS = {
    "ozarks_dharma": {
        "url": "https://calendar.google.com/calendar/ical/ozarksdharma%40gmail.com/public/basic.ics",
        "filter_to_sits": True,  # Sat meditation sits + Thu sits; filter out retreats if needed
    },
}
