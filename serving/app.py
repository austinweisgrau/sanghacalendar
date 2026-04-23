"""
Sangha Calendar web server.

Phase 1: reads from data/events.json (committed by GitHub Actions daily).
Phase 2: reads from SQLite on Fly.io persistent volume (set DB_PATH env var).
"""

import json
import os
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Phase 1: JSON file path (committed by Actions)
_EVENTS_JSON = Path(__file__).parent.parent / "data" / "events.json"


def _load_events_json() -> list[dict]:
    if not _EVENTS_JSON.exists():
        return []
    data = json.loads(_EVENTS_JSON.read_text())
    return data.get("events", [])


def _load_events_db(city=None, tradition=None) -> list[dict]:
    from data.store import get_upcoming_events
    return get_upcoming_events(city=city, tradition=tradition)


def _use_db() -> bool:
    return bool(os.environ.get("DB_PATH"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/events")
def events():
    city = request.args.get("city")
    tradition = request.args.get("tradition")

    if _use_db():
        rows = _load_events_db(city=city, tradition=tradition)
    else:
        rows = _load_events_json()
        if city:
            rows = [r for r in rows if r.get("city") == city]
        if tradition:
            rows = [r for r in rows if r.get("tradition") == tradition]

    return jsonify(rows)


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
