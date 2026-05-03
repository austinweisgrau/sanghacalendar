#!/usr/bin/env python3
"""
Weekly email digest sender for Sangha Calendar.

Queries upcoming sits for the next 7 days and emails each active subscriber
a personalized digest filtered to their saved city/tradition preferences.

Usage:
    python scripts/send_digest.py              # send to all subscribers
    python scripts/send_digest.py --dry-run    # print digest to stdout, no emails sent
    python scripts/send_digest.py --email foo@example.com  # send to a single address

Requires env vars:
    RESEND_API_KEY   — Resend API key (https://resend.com). If absent, --dry-run is forced.
    RESEND_FROM      — sender address (default: digest@sanghacalendar.org)
    BASE_URL         — base URL for unsubscribe links (default: https://sangha-calendar.fly.dev)
    DB_PATH          — path to SQLite DB (default: data/sangha.db)
"""

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Make sure the project root is on the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data.store import get_active_subscribers, get_upcoming_events, init_db

BASE_URL = os.environ.get("BASE_URL", "https://sangha-calendar.fly.dev")
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
RESEND_FROM = os.environ.get("RESEND_FROM", "Sangha Calendar <digest@sanghacalendar.org>")

TRADITION_LABELS = {
    "theravada": "Theravada / Insight",
    "zen": "Zen",
    "tibetan": "Tibetan / Shambhala",
    "secular": "Secular",
    "pluralist": "Non-sectarian",
}

TRADITION_COLORS = {
    "theravada": "#3d7a56",
    "zen": "#4a5f82",
    "tibetan": "#7a6e28",
    "secular": "#3a7070",
    "pluralist": "#5a6a5a",
}


def _fmt_time(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso)
        return dt.strftime("%-I:%M %p").replace(":00 ", " ")
    except Exception:
        return iso


def _fmt_date(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso)
        return dt.strftime("%A, %B %-d")
    except Exception:
        return iso


def _date_key(iso: str) -> str:
    try:
        return datetime.fromisoformat(iso).strftime("%Y-%m-%d")
    except Exception:
        return iso[:10]


def build_digest_html(events: list[dict], unsubscribe_url: str, week_label: str) -> str:
    """Render events into an HTML email body."""
    if not events:
        return f"""
<html><body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Georgia,sans-serif;
max-width:580px;margin:0 auto;padding:1.5rem;color:#2a2724;background:#f6f3ee">
<h2 style="color:#4d7060">Sangha Calendar — {week_label}</h2>
<p style="color:#6b6560">No meditation sits found for the coming week matching your preferences.</p>
<p style="color:#6b6560">
  <a href="{BASE_URL}" style="color:#4d7060">View full calendar</a>
</p>
<p style="font-size:0.75rem;color:#aaa;margin-top:2rem">
  <a href="{unsubscribe_url}" style="color:#aaa">Unsubscribe</a>
</p>
</body></html>
"""

    # Group by date
    by_date: dict[str, list[dict]] = {}
    for e in events:
        k = _date_key(e["start_time"])
        by_date.setdefault(k, []).append(e)

    days_html = ""
    for date_key_str in sorted(by_date.keys()):
        day_events = by_date[date_key_str]
        day_label = _fmt_date(day_events[0]["start_time"])
        cards = ""
        for e in day_events:
            trad_color = TRADITION_COLORS.get(e.get("tradition", ""), "#888")
            trad_label = TRADITION_LABELS.get(e.get("tradition", ""), "Other")
            title_html = f"<div style='font-style:italic;font-size:0.83rem;color:#6b6560'>{e['title']}</div>" if e.get("title") and e["title"] != e["org_name"] else ""
            addr_parts = [p for p in [e.get("address"), e.get("city")] if p]
            addr_html = f"<div style='font-size:0.78rem;color:#6b6560;margin-top:0.2rem'>📍 {', '.join(addr_parts)}</div>" if addr_parts else ""
            time_str = _fmt_time(e["start_time"])
            if e.get("end_time"):
                time_str += f" – {_fmt_time(e['end_time'])}"
            link_html = f"<a href='{e['event_url']}' style='font-size:0.78rem;color:#4d7060;text-decoration:none'>Details ↗</a>" if e.get("event_url") else ""
            org_id = e["org_id"]
            org_name = e["org_name"]
            org_link = f"<a href='{BASE_URL}/centers/{org_id}' style='font-weight:600;font-size:0.92rem;color:#2a2724;text-decoration:none'>{org_name}</a>"

            cards += f"""
<div style="background:white;border:1px solid #e4dfd6;border-left:3px solid {trad_color};
border-radius:0 7px 7px 0;padding:0.75rem 1rem;margin-bottom:0.4rem">
  <div style="display:flex;justify-content:space-between;align-items:baseline;gap:0.5rem">
    <span>{org_link}</span>
    <span style="font-size:0.83rem;color:#6b6560;white-space:nowrap">{time_str}</span>
  </div>
  {title_html}
  {addr_html}
  <div style="margin-top:0.3rem">
    <span style="font-size:0.7rem;padding:0.1rem 0.45rem;border-radius:2rem;
      background:{trad_color};color:white;font-weight:500">{trad_label}</span>
  </div>
  {('<div style="margin-top:0.3rem">' + link_html + '</div>') if link_html else ''}
</div>"""

        days_html += f"""
<div style="margin-bottom:1.5rem">
  <div style="font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.09em;
    color:#6b6560;padding-bottom:0.4rem;border-bottom:1px solid #e4dfd6;margin-bottom:0.5rem">
    {day_label}
  </div>
  {cards}
</div>"""

    return f"""
<html><body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Georgia,sans-serif;
max-width:580px;margin:0 auto;padding:1.5rem;color:#2a2724;background:#f6f3ee">

<div style="background:#4d7060;color:white;padding:1.5rem;border-radius:8px;margin-bottom:1.5rem;text-align:center">
  <h1 style="margin:0 0 0.3rem;font-size:1.4rem;font-weight:600">Sangha Calendar</h1>
  <p style="margin:0;opacity:0.85;font-size:0.88rem">{week_label} — Bay Area meditation sits</p>
</div>

{days_html}

<div style="margin-top:1.5rem;padding-top:1rem;border-top:1px solid #e4dfd6;
  text-align:center;font-size:0.78rem;color:#6b6560">
  <a href="{BASE_URL}" style="color:#4d7060;text-decoration:none">View full calendar</a>
  &nbsp;·&nbsp;
  <a href="{unsubscribe_url}" style="color:#aaa;text-decoration:none">Unsubscribe</a>
</div>

</body></html>
"""


def send_via_resend(to: str, subject: str, html: str) -> bool:
    """Send one email via Resend API. Returns True on success."""
    import httpx

    resp = httpx.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {RESEND_API_KEY}", "Content-Type": "application/json"},
        json={"from": RESEND_FROM, "to": [to], "subject": subject, "html": html},
        timeout=30,
    )
    if resp.status_code not in (200, 201):
        print(f"  ✗ Resend error {resp.status_code}: {resp.text}", file=sys.stderr)
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Send Sangha Calendar weekly digest")
    parser.add_argument("--dry-run", action="store_true", help="Print digest HTML, don't send")
    parser.add_argument("--email", help="Send only to this address (for testing)")
    args = parser.parse_args()

    dry_run = args.dry_run or not RESEND_API_KEY
    if not RESEND_API_KEY and not args.dry_run:
        print("⚠️  RESEND_API_KEY not set — running in dry-run mode (no emails sent).", file=sys.stderr)

    init_db()

    now = datetime.now(timezone.utc)
    week_label = now.strftime("Week of %B %-d, %Y")

    if args.email:
        # Single test recipient — no saved prefs
        subscribers = [{"email": args.email, "cities": None, "tradition": None, "unsubscribe_token": "test"}]
    else:
        subscribers = get_active_subscribers()

    if not subscribers:
        print("No active subscribers. Nothing to send.")
        return

    print(f"Sending digest '{week_label}' to {len(subscribers)} subscriber(s)...")

    sent = 0
    failed = 0
    for sub in subscribers:
        events = get_upcoming_events(
            city=sub["cities"],
            tradition=sub["tradition"],
            days_ahead=7,
            limit=200,
        )
        unsubscribe_url = f"{BASE_URL}/unsubscribe?token={sub['unsubscribe_token']}"
        html = build_digest_html(events, unsubscribe_url, week_label)
        subject = f"Sangha Calendar — {week_label} ({len(events)} sits)"

        if dry_run:
            print(f"\n{'=' * 60}")
            print(f"TO: {sub['email']}")
            print(f"SUBJECT: {subject}")
            print(f"EVENTS: {len(events)}")
            if sub["cities"]:
                print(f"CITIES: {', '.join(sub['cities'])}")
            if sub["tradition"]:
                print(f"TRADITION: {sub['tradition']}")
            print("HTML preview (first 500 chars):")
            print(html[:500])
            sent += 1
        else:
            print(f"  → {sub['email']} ({len(events)} events)...", end=" ")
            ok = send_via_resend(sub["email"], subject, html)
            if ok:
                print("✓")
                sent += 1
            else:
                failed += 1

    print(f"\nDone. {sent} sent, {failed} failed.")


if __name__ == "__main__":
    main()
