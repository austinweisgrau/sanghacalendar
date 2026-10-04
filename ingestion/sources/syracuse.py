"""
Syracuse, NY — Phase 3 expansion.

Syracuse (~650k metro, Onondaga County / Central New York) has two main
centers for public drop-in meditation:

Centers included:
  - Zen Center of Syracuse / Hoen-ji (zen_center_syracuse)
    — Rinzai Zen (Zen Studies Society / Dai Bosatsu Zendo lineage)
    266 W Seneca Turnpike, Syracuse NY 13207
    zencenterofsyracuse.org
    Guiding teacher: Shinge Roko Sherry Chayat Roshi (first American woman
    with Dharma transmission in Rinzai school). Daily zazen, public evening
    sits Tuesday + Thursday, full Sunday program.
    iCal blocked (403); recurring sits seeded.

  - Thekchen Choling USA Syracuse (thekchen_choling_syracuse)
    — Vajrayana Tibetan Buddhism (Singha Namdrol Rinpoche)
    109 East Avenue, Minoa NY 13116 (Village of Minoa, east of Syracuse)
    thekchencholing.us
    Tuesday 7pm Meditation for Beginners; special events via Eventbrite.
    Recurring sit seeded; Eventbrite feed wired for retreats/special events.

Research notes (2026-10-04):
  - ZCS iCal: WordPress events page exposes Google/iCal subscribe links but
    the raw ?ical=1 endpoint returns 403. Recurring sits seeded instead.
  - ZCS founded 1972 by Eido Shimano Roshi; Shinge Chayat Roshi has led
    since 1996. One of oldest and most historically significant Rinzai Zen
    centers in the US. Affiliated with Zen Studies Society (NYC).
  - Thekchen Choling: Eventbrite organizer_id 62351787513. Day-to-day
    sits are free/donation; Eventbrite used for ticketed retreats.
  - Apple Blossom Sangha (Plum Village): Zoom-only as of 2026; skipped.
  - SU Buddhist Chaplaincy (Hendricks Chapel): campus-focused, no persistent
    calendar feed; skipped.
"""

from data.schemas.event import Center, Tradition

# ---------------------------------------------------------------------------
# Center registry
# ---------------------------------------------------------------------------

CENTERS = {
    "zen_center_syracuse": Center(
        id="zen_center_syracuse",
        name="Zen Center of Syracuse",
        url="https://www.zencenterofsyracuse.org",
        address="266 W Seneca Turnpike",
        city="Syracuse",
        state="NY",
        zip_code="13207",
        lat=43.0182,
        lng=-76.1502,
        neighborhood="South Valley, Syracuse",
        tradition=Tradition.ZEN,
        notes=(
            "Zen Center of Syracuse (Hoen-ji) is one of the oldest and most "
            "historically significant Rinzai Zen centers in the United States, "
            "founded in 1972 and affiliated with the Zen Studies Society (Dai Bosatsu "
            "Zendo / New York Zendo Shobo-Ji). Guiding teacher Shinge Roko Sherry "
            "Chayat Roshi was the first American woman to receive Dharma transmission "
            "in the Japanese Rinzai school. Daily zazen (Mon–Sat 6am). Evening public "
            "sits: Tuesdays 6–7pm 'Just Sitting' (two periods of zazen + kinhin), "
            "Thursdays 6–8pm (instruction + zazen, newcomers especially welcome). "
            "Sunday program 9am–noon (chanting, kinhin, two periods of zazen; dharma "
            "talks 1st Sunday). Sesshins four times yearly. All sessions also via Zoom. "
            "zencenterofsyracuse.org. (315) 492-9773."
        ),
    ),
    "thekchen_choling_syracuse": Center(
        id="thekchen_choling_syracuse",
        name="Thekchen Choling USA — Syracuse Temple",
        url="https://thekchencholing.us",
        address="109 East Avenue",
        city="Minoa",
        state="NY",
        zip_code="13116",
        lat=43.0748,
        lng=-76.0066,
        neighborhood="Village of Minoa (east of Syracuse)",
        tradition=Tradition.TIBETAN,
        notes=(
            "Thekchen Choling USA Syracuse Temple is the North American seat of "
            "Singha Namdrol Rinpoche, a Vajrayana Tibetan Buddhist lama. Part of the "
            "Thekchen Choling organization headquartered in Singapore. Located in the "
            "Village of Minoa (eastern Syracuse metro). Offers Tuesday 7pm Meditation "
            "for Beginners, weekly Shantideva discussion group, Medicine Buddha pujas, "
            "and special retreats with visiting teachers. All are welcome. "
            "thekchencholing.us. tccl.syracuse@gmail.com. (315) 480-1088."
        ),
    ),
}


# Eventbrite organizer configs — Thekchen Choling Syracuse uses Eventbrite
# for ticketed retreats and special teachings
EVENTBRITE_FEEDS = {
    "thekchen_choling_syracuse": {
        "organizer_id": "62351787513",
        "filter_to_sits": False,  # include retreats, teachings, and special programs
    },
}


# No live iCal feeds extractable for ZCS (403 blocked) —
# recurring sits seeded in scripts/sangha-seed-recurring.js
ICAL_FEEDS: dict = {}
