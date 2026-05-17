"""
Charlotte, NC — Phase 3 expansion.

Charlotte has a small but active Buddhist community spanning Theravada,
Zen, Tibetan, and Plum Village traditions. Four centers serve the metro.

Centers included:
  - Charlotte Buddhist Vihara (charlotte_vihara) — Theravada, NE Charlotte
    3423 Stonehaven Dr, Charlotte NC 28215
    Recurring sits: Tue 6pm, Wed 10:30am, Thu 7pm, Sat 2pm
    Cloudflare-blocked iCal; sits seeded as recurring.

  - Insight Meditation Community of Charlotte (imcc) — Vipassana, South Charlotte
    3900 Park Road (Park Road Baptist Church), Charlotte NC 28209
    Recurring sits: Tue 12pm (Zoom), Wed 7:30pm (hybrid)
    Cloudflare-blocked iCal (MEC plugin); sits seeded as recurring.

  - Kadampa Meditation Center North Carolina (kmc_nc) — NKT Tibetan, Dilworth
    528 East Blvd, Charlotte NC 28203
    Recurring sits: Sun 9:30am, Tue 5pm, Wed 5pm, Thu 5pm, Sat 10am
    Wix site — no accessible iCal; sits seeded as recurring.

  - Charlotte Community of Mindfulness (ccm_charlotte) — Plum Village / Zen, Myers Park
    1931 Selwyn Ave (Myers Park Baptist Church), Charlotte NC 28207
    Recurring sits: Sun 8:30am
    No iCal; sit seeded as recurring.

Research notes (2026-05-17):
  - Charlotte Buddhist Vihara (charlottebuddhistvihara.org): Founded under
    Ayya Sudhamma (fully ordained Theravada bhikkhuni). WordPress site with
    The Events Calendar plugin confirmed. iCal/tribe_events blocked by
    Cloudflare WAF. Also has Meetup group. Confirmed schedule:
      Tue 6pm: "An Evening of Personal Growth" — talk + meditation (hybrid)
      Wed 10:30am: Meditation (in-person + Zoom)
      Thu 7pm: "Meditation for Awakening" — talk + meditation (hybrid)
      Sat 2pm: "Buddhist Teachings" — talk + meditation (hybrid)

  - IMCC (imccharlotte.org): Founded 2009 by Joy LiBethe. Modern Events
    Calendar (MEC) WordPress plugin. iCal blocked by Cloudflare WAF.
    Schedule confirmed from website:
      Tue 12pm: Dharma teaching + 30-min silent meditation (Zoom only)
      Wed 7pm: Newcomer instruction (in-person, 30 min)
      Wed 7:30pm: Silent meditation + Dharma talk (hybrid, ~90 min)
      Fri 7:30am: 20-min silent meditation (Zoom only — too brief to seed)
    Meets at Park Road Baptist Church, Milford Chapel / Meditation Hall.

  - KMC NC (meditationcharlotte.org): Founded 2004, restructured 2016.
    NKT-IKBU center in Dilworth. Wix calendar at /calendar — no iCal export.
    Confirmed schedule from website:
      Sun 9:30am–12:30pm: Drop-in class
      Sun 5–6pm: Drop-in class
      Tue 5–6pm: Drop-in class
      Wed 5–8pm: Drop-in class / Foundation Program
      Thu 5–6:30pm: Drop-in class
      Fri 11:30am–3pm: Drop-in class
      Fri 6–7:30pm: Drop-in class
      Sat 10am–1pm: Drop-in class
    Seeding core drop-in times only (Sun 9:30am, Tue–Thu 5pm, Sat 10am).

  - Charlotte Community of Mindfulness (charlottemindfulness.org): Founded
    1993. Thich Nhat Hanh / Plum Village lineage. Meets at Myers Park Baptist
    Church, 1931 Selwyn Ave. No iCal. Confirmed schedule:
      Sun 8:30–10am: Sitting meditation, walking meditation, Dharma reading,
        sharing circle (in-person + Zoom). Last Sunday: Recitation ceremony.
    One of the oldest Plum Village sanghas in the Southeast.

  Skipped for now:
  - Greatwoods Zen (greatwoodszen.org): Plum Village, 28-acre property in
    east Charlotte (2631 Buckleigh Dr, 28215). Squarespace calendar, 404.
    Meetup group exists but contains general wellness retreats, not standard
    Buddhist sits. Monitor for a reliable schedule source.
  - Charlotte Zen Meditation Society (Meetup): Meetup iCal exists but 0
    upcoming events as of 2026-05-17. Meets at Harmony House (726 East Blvd),
    Soto Zen / Katagiri Roshi lineage. Monitor for activity resumption.
  - Charlotte True Buddha Temple: Vajrayana/Chinese Tantric (True Buddha
    School), static HTML site, no calendar. Not standard sitting practice.
  - Charlotte Vipassana Group (Goenka/dhamma.org): Weekly group sits for
    established students only; no public-facing calendar. Skip.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "charlotte_vihara": Center(
        id="charlotte_vihara",
        name="Charlotte Buddhist Vihara",
        url="https://www.charlottebuddhistvihara.org",
        address="3423 Stonehaven Dr",
        city="Charlotte",
        state="NC",
        zip_code="28215",
        lat=35.2379,
        lng=-80.7626,
        neighborhood="Northeast Charlotte",
        tradition=Tradition.THERAVADA,
        notes=(
            "Charlotte Buddhist Vihara is a Theravada Buddhist center in northeast "
            "Charlotte, led by Ayya Sudhamma — one of the first fully ordained "
            "Theravada bhikkhunis (nuns) in the West. Regular weekly offerings include "
            "Tuesday 'Evening of Personal Growth' (6pm, talk and meditation, hybrid), "
            "Wednesday Meditation (10:30am, in-person and Zoom), Thursday 'Meditation "
            "for Awakening' (7pm, talk and meditation, hybrid), and Saturday 'Buddhist "
            "Teachings' (2pm, talk and meditation, hybrid). All sessions include guided "
            "meditation and Dhamma discussion. Drop-in welcome; donations appreciated."
        ),
    ),
    "imcc": Center(
        id="imcc",
        name="Insight Meditation Community of Charlotte",
        url="https://www.imccharlotte.org",
        address="3900 Park Road",
        city="Charlotte",
        state="NC",
        zip_code="28209",
        lat=35.1870,
        lng=-80.8565,
        neighborhood="South Charlotte / Park Road",
        tradition=Tradition.THERAVADA,
        notes=(
            "The Insight Meditation Community of Charlotte (IMCC) is a Theravada / "
            "Vipassana sangha founded in 2009 by Joy LiBethe in the Insight Meditation "
            "tradition. The community meets at the Milford Chapel inside Park Road "
            "Baptist Church. Weekly offerings: Tuesday noon Dharma teaching + 30-minute "
            "silent meditation (Zoom); Wednesday 7pm newcomer instruction (in-person), "
            "followed by 7:30pm silent meditation and Dharma talk (in-person and Zoom). "
            "Friday 7:30am brief sit (Zoom). Drop-in welcome; no experience required. "
            "Dana (generosity) basis."
        ),
    ),
    "kmc_nc": Center(
        id="kmc_nc",
        name="Kadampa Meditation Center North Carolina",
        url="https://www.meditationcharlotte.org",
        address="528 East Blvd",
        city="Charlotte",
        state="NC",
        zip_code="28203",
        lat=35.2153,
        lng=-80.8422,
        neighborhood="Dilworth",
        tradition=Tradition.TIBETAN,
        notes=(
            "Kadampa Meditation Center North Carolina (KMC NC) is a New Kadampa "
            "Tradition (NKT-IKBU) Tibetan Buddhist center in the Dilworth neighborhood "
            "of Charlotte. Founded 2004, the center offers extensive weekly drop-in "
            "classes including guided meditation and Buddhist teachings in the Kadampa "
            "tradition. Core drop-in times: Sunday 9:30am–12:30pm, Tuesday 5–6pm, "
            "Wednesday 5–8pm, Thursday 5–6:30pm, and Saturday 10am–1pm. Also hosts "
            "Foundation Program, Teacher Training Program, and special events and "
            "empowerments. All welcome; no experience required."
        ),
    ),
    "ccm_charlotte": Center(
        id="ccm_charlotte",
        name="Charlotte Community of Mindfulness",
        url="https://www.charlottemindfulness.org",
        address="1931 Selwyn Ave",
        city="Charlotte",
        state="NC",
        zip_code="28207",
        lat=35.2025,
        lng=-80.8400,
        neighborhood="Myers Park",
        tradition=Tradition.ZEN,
        notes=(
            "The Charlotte Community of Mindfulness (CCM) is one of the oldest Plum "
            "Village sanghas in the Southeast, founded in 1993 in the tradition of "
            "Thich Nhat Hanh. The sangha meets at Myers Park Baptist Church. Weekly "
            "Sunday Morning Sangha (8:30–10am) includes sitting meditation, walking "
            "meditation, Dharma reading, and a sharing circle. Hybrid in-person and "
            "Zoom. Last Sunday of the month: Recitation ceremony. 2nd Sunday: "
            "occasional Sutra study follows (10:15–11am). No experience needed; "
            "all traditions welcome. Free; donations appreciated."
        ),
    ),
}
