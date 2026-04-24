"""
Sangha Calendar web server.
Reads from SQLite on Fly.io persistent volume (DB_PATH env var → /data/sangha.db).
"""

import os
from flask import Flask, jsonify, render_template, request
from data.store import init_db, get_upcoming_events, upsert_dicts

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


@app.route("/api/events")
def events():
    rows = get_upcoming_events(
        city=request.args.get("city"),
        tradition=request.args.get("tradition"),
        location_type=request.args.get("location_type"),
    )
    return jsonify(rows)


@app.route("/api/admin/events", methods=["POST"])
def admin_ingest():
    """Abraxis ingestion endpoint. Accepts a list of event dicts, upserts to DB."""
    auth = request.headers.get("Authorization", "")
    if not INGEST_TOKEN or auth != f"Bearer {INGEST_TOKEN}":
        return jsonify({"error": "unauthorized"}), 401

    body = request.get_json(silent=True)
    if not body or "events" not in body:
        return jsonify({"error": "expected {events: [...]}"}), 400

    n = upsert_dicts(body["events"])
    return jsonify({"upserted": n})


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
