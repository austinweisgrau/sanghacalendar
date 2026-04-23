"""
Sangha Calendar web server.
Reads from SQLite on Fly.io persistent volume (DB_PATH env var → /data/sangha.db).
"""

import os
from flask import Flask, jsonify, render_template, request
from data.store import init_db, get_upcoming_events

app = Flask(__name__)


@app.before_request
def setup():
    # init_db is idempotent — safe to call on every cold start
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
    )
    return jsonify(rows)


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
