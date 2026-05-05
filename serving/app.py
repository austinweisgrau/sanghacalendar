"""
Sangha Calendar web server.
Reads from SQLite on Fly.io persistent volume (DB_PATH env var → /data/sangha.db).
"""

import os
from datetime import datetime, timezone

from dateutil import parser as dateutil_parser
from flask import Flask, Response, abort, jsonify, render_template, request
from icalendar import Calendar as ICalCalendar
from icalendar import Event as ICalEvent

from data.store import (
    add_submission,
    add_subscriber,
    dedup_events,
    get_active_subscribers,
    get_submissions,
    get_upcoming_events,
    init_db,
    unsubscribe_by_token,
    upsert_dicts,
)
from serving.centers import CENTERS

BASE_URL = os.environ.get("BASE_URL", "https://sangha-calendar.fly.dev")


def _parse_dt(s: str) -> datetime:
    """Parse ISO datetime string to UTC-aware datetime."""
    dt = dateutil_parser.parse(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _events_to_ical(events: list[dict], cal_name: str = "Sangha Calendar") -> bytes:
    """Serialize event dicts to iCal bytes."""
    cal = ICalCalendar()
    cal.add("prodid", "-//Sangha Calendar//sangha-calendar.fly.dev//EN")
    cal.add("version", "2.0")
    cal.add("calscale", "GREGORIAN")
    cal.add("method", "PUBLISH")
    cal.add("x-wr-calname", cal_name)
    cal.add("x-wr-timezone", "America/Los_Angeles")
    cal.add("refresh-interval;value=duration", "PT12H")
    cal.add("x-published-ttl", "PT12H")

    for e in events:
        vevent = ICalEvent()
        vevent.add("uid", e["id"] + "@sangha-calendar.fly.dev")

        summary = e["org_name"]
        if e.get("title") and e["title"] != e["org_name"]:
            summary = f"{e['org_name']} — {e['title']}"
        vevent.add("summary", summary)

        try:
            vevent.add("dtstart", _parse_dt(e["start_time"]))
            if e.get("end_time"):
                vevent.add("dtend", _parse_dt(e["end_time"]))
        except Exception:
            continue  # skip malformed datetimes

        desc_parts = []
        if e.get("title"):
            desc_parts.append(e["title"])
        if e.get("tradition"):
            desc_parts.append(f"Tradition: {e['tradition'].title()}")
        if e.get("notes"):
            desc_parts.append(e["notes"])
        if e.get("event_url"):
            desc_parts.append(f"Details: {e['event_url']}")
        if desc_parts:
            vevent.add("description", "\n".join(desc_parts))

        location_parts = [p for p in [e.get("address"), e.get("city"), e.get("state")] if p]
        if location_parts:
            vevent.add("location", ", ".join(location_parts))

        if e.get("event_url"):
            vevent.add("url", e["event_url"])

        cal.add_component(vevent)

    return cal.to_ical()

app = Flask(__name__)
INGEST_TOKEN = os.environ.get("INGEST_TOKEN")


@app.before_request
def setup():
    if not hasattr(app, "_db_ready"):
        init_db()
        app._db_ready = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map")
def map_view():
    return render_template("map.html")


@app.route("/submit")
def submit_page():
    return render_template("submit.html")


@app.route("/centers/<org_id>")
def center_page(org_id):
    center = CENTERS.get(org_id)
    if not center:
        abort(404)
    return render_template("center.html", center=center)


@app.route("/feed.ics")
def ical_feed():
    days_ahead = 60
    if request.args.get("days"):
        try:
            days_ahead = int(request.args.get("days"))
        except ValueError:
            pass
    cities = request.args.getlist("city")
    states = request.args.getlist("state")
    rows = get_upcoming_events(
        city=cities if cities else None,
        state=states if states else None,
        tradition=request.args.get("tradition"),
        location_type=request.args.get("location_type"),
        days_ahead=days_ahead,
        start_date=request.args.get("start_date"),
        end_date=request.args.get("end_date"),
        limit=500,
    )

    # Build a descriptive calendar name from active filters
    parts = ["Sangha Calendar"]
    if request.args.get("tradition"):
        parts.append(request.args["tradition"].title())
    if states:
        parts.append(", ".join(states))
    if cities:
        parts.append(", ".join(cities))
    if request.args.get("location_type"):
        parts.append(f"({request.args['location_type']})")
    cal_name = " — ".join(parts) if len(parts) > 1 else parts[0]

    ical_bytes = _events_to_ical(rows, cal_name=cal_name)
    return Response(
        ical_bytes,
        mimetype="text/calendar; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="sangha-calendar.ics"'},
    )


@app.route("/api/events")
def events():
    days_ahead = 60
    if request.args.get("days"):
        try:
            days_ahead = int(request.args.get("days"))
        except ValueError:
            pass
    cities = request.args.getlist("city")
    states = request.args.getlist("state")
    rows = get_upcoming_events(
        city=cities if cities else None,
        state=states if states else None,
        tradition=request.args.get("tradition"),
        location_type=request.args.get("location_type"),
        days_ahead=days_ahead,
        start_date=request.args.get("start_date"),
        end_date=request.args.get("end_date"),
    )
    return jsonify(rows)


@app.route("/api/events/<org_id>")
def events_by_org(org_id):
    rows = get_upcoming_events(
        org_id=org_id,
        location_type=request.args.get("location_type"),
    )
    return jsonify(rows)


@app.route("/api/centers")
def centers_list():
    return jsonify(list(CENTERS.values()))


@app.route("/api/centers/<org_id>")
def center_detail(org_id):
    center = CENTERS.get(org_id)
    if not center:
        return jsonify({"error": "not found"}), 404
    return jsonify(center)


@app.route("/api/submit", methods=["POST"])
def submit_center():
    body = request.get_json(silent=True)
    if not body or not body.get("name") or not body.get("city"):
        return jsonify({"error": "name and city are required"}), 400
    # Basic length guards
    for field in ("name", "city", "website", "tradition", "notes", "submitter"):
        val = body.get(field)
        if val and len(val) > 1000:
            return jsonify({"error": f"{field} too long"}), 400
    row_id = add_submission(
        name=body["name"].strip(),
        city=body["city"].strip(),
        website=body.get("website"),
        tradition=body.get("tradition"),
        notes=body.get("notes"),
        submitter=body.get("submitter"),
    )
    return jsonify({"ok": True, "id": row_id}), 201


@app.route("/api/admin/submissions", methods=["GET"])
def admin_submissions():
    auth = request.headers.get("Authorization", "")
    if not INGEST_TOKEN or auth != f"Bearer {INGEST_TOKEN}":
        return jsonify({"error": "unauthorized"}), 401
    return jsonify(get_submissions())


@app.route("/api/subscribe", methods=["POST"])
def subscribe():
    body = request.get_json(silent=True)
    if not body or not body.get("email"):
        return jsonify({"error": "email is required"}), 400
    cities = body.get("cities")
    if cities and not isinstance(cities, list):
        return jsonify({"error": "cities must be an array"}), 400
    tradition = body.get("tradition") or None
    try:
        result = add_subscriber(
            email=body["email"],
            cities=cities or None,
            tradition=tradition,
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    if result.get("exists"):
        return jsonify({"ok": True, "message": "already subscribed"}), 200
    return jsonify({"ok": True}), 201


@app.route("/unsubscribe")
def unsubscribe():
    token = request.args.get("token", "")
    if not token:
        return "Missing unsubscribe token.", 400
    ok = unsubscribe_by_token(token)
    if ok:
        return (
            '<html><body style="font-family:sans-serif;max-width:480px;margin:4rem auto;text-align:center">'
            "<h2>Unsubscribed</h2><p>You've been removed from the Sangha Calendar digest.</p>"
            '<p><a href="/">Return to calendar</a></p></body></html>'
        )
    return (
        '<html><body style="font-family:sans-serif;max-width:480px;margin:4rem auto;text-align:center">'
        "<h2>Link expired or invalid</h2>"
        "<p>This unsubscribe link may have already been used.</p>"
        '<p><a href="/">Return to calendar</a></p></body></html>'
    )


@app.route("/api/admin/subscribers")
def admin_subscribers():
    auth = request.headers.get("Authorization", "")
    if not INGEST_TOKEN or auth != f"Bearer {INGEST_TOKEN}":
        return jsonify({"error": "unauthorized"}), 401
    return jsonify(get_active_subscribers())


@app.route("/api/admin/events", methods=["POST"])
def admin_ingest():
    auth = request.headers.get("Authorization", "")
    if not INGEST_TOKEN or auth != f"Bearer {INGEST_TOKEN}":
        return jsonify({"error": "unauthorized"}), 401
    body = request.get_json(silent=True)
    if not body or "events" not in body:
        return jsonify({"error": "expected {events: [...]}"}), 400
    n = upsert_dicts(body["events"])
    dedup_events()
    return jsonify({"upserted": n})


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
