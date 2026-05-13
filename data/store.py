"""
SQLite event store.

DB_PATH env var controls location (defaults to data/sangha.db for local dev).
On Fly.io: persistent volume mounted at /data, DB_PATH=/data/sangha.db.
"""

import hashlib
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from data.schemas.event import Event

DB_PATH = Path(os.environ.get("DB_PATH", Path(__file__).parent / "sangha.db"))

_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS subscribers (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    email            TEXT NOT NULL UNIQUE,
    cities           TEXT,          -- JSON array, NULL means all cities
    tradition        TEXT,          -- NULL means all traditions
    unsubscribe_token TEXT NOT NULL UNIQUE,
    subscribed_at    TEXT NOT NULL,
    is_active        INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_subscribers_token ON subscribers(unsubscribe_token);

CREATE TABLE IF NOT EXISTS events (
    id                TEXT PRIMARY KEY,
    org_id            TEXT NOT NULL,
    org_name          TEXT NOT NULL,
    title             TEXT NOT NULL,
    start_time        TEXT NOT NULL,
    end_time          TEXT,
    address           TEXT,
    city              TEXT,
    state             TEXT,
    neighborhood      TEXT,
    lat               REAL,
    lng               REAL,
    tradition         TEXT,
    location_type     TEXT DEFAULT 'in-person',
    is_sit            INTEGER DEFAULT 1,
    accessibility_notes TEXT,
    identity_focus    TEXT,
    source            TEXT,
    source_url        TEXT,
    event_url         TEXT,
    last_verified     TEXT,
    recurrence        TEXT,
    notes             TEXT
);
CREATE INDEX IF NOT EXISTS idx_events_start     ON events(start_time);
CREATE INDEX IF NOT EXISTS idx_events_city      ON events(city);
CREATE INDEX IF NOT EXISTS idx_events_tradition ON events(tradition);

CREATE TABLE IF NOT EXISTS center_submissions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    city        TEXT,
    website     TEXT,
    tradition   TEXT,
    notes       TEXT,
    submitter   TEXT,
    submitted_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS corrections (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    org_id       TEXT,
    org_name     TEXT,
    description  TEXT NOT NULL,
    contact      TEXT,
    submitted_at TEXT NOT NULL
);
"""


def _conn() -> sqlite3.Connection:
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def _make_unsubscribe_token(email: str) -> str:
    """Deterministic unsubscribe token derived from the email address."""
    secret = os.environ.get("EMAIL_SECRET", os.environ.get("INGEST_TOKEN", "sangha-dev"))
    return hashlib.sha256(f"{secret}:{email}".encode()).hexdigest()[:40]


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with _conn() as c:
        c.executescript(_CREATE_SQL)
        # Migration: add location_type if upgrading an existing DB
        try:
            c.execute("ALTER TABLE events ADD COLUMN location_type TEXT DEFAULT 'in-person'")
            c.execute("CREATE INDEX IF NOT EXISTS idx_events_location_type ON events(location_type)")
        except sqlite3.OperationalError:
            pass  # column already exists


def upsert_events(events: list[Event]) -> int:
    """Insert or update events. Returns rowcount."""
    rows = [
        (
            e.id, e.org_id, e.org_name, e.title, e.start_time, e.end_time,
            e.address, e.city, e.state, e.neighborhood, e.lat, e.lng,
            e.tradition.value if hasattr(e.tradition, "value") else e.tradition,
            e.location_type.value if hasattr(e.location_type, "value") else e.location_type,
            int(e.is_sit), e.accessibility_notes, e.identity_focus,
            e.source.value if hasattr(e.source, "value") else e.source,
            e.source_url, e.event_url, e.last_verified, e.recurrence, e.notes,
        )
        for e in events
    ]
    with _conn() as c:
        cur = c.executemany(
            """
            INSERT INTO events (
                id, org_id, org_name, title, start_time, end_time,
                address, city, state, neighborhood, lat, lng,
                tradition, location_type, is_sit, accessibility_notes, identity_focus,
                source, source_url, event_url, last_verified, recurrence, notes
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
                last_verified = excluded.last_verified,
                end_time      = excluded.end_time,
                location_type = excluded.location_type,
                notes         = excluded.notes
            """,
            rows,
        )
        return cur.rowcount


_COLUMNS = [
    "id", "org_id", "org_name", "title", "start_time", "end_time",
    "address", "city", "state", "neighborhood", "lat", "lng",
    "tradition", "location_type", "is_sit", "accessibility_notes", "identity_focus",
    "source", "source_url", "event_url", "last_verified", "recurrence", "notes",
]


def upsert_dicts(events: list[dict]) -> int:
    """Upsert raw event dicts (e.g. from Abraxis POST). Returns rowcount."""
    rows = [tuple(e.get(col) for col in _COLUMNS) for e in events]
    with _conn() as c:
        cur = c.executemany(
            f"""
            INSERT INTO events ({', '.join(_COLUMNS)})
            VALUES ({', '.join(['?'] * len(_COLUMNS))})
            ON CONFLICT(id) DO UPDATE SET
                last_verified = excluded.last_verified,
                end_time      = excluded.end_time,
                location_type = excluded.location_type,
                is_sit        = excluded.is_sit,
                identity_focus = excluded.identity_focus,
                notes         = excluded.notes
            """,
            rows,
        )
        return cur.rowcount


def dedup_events() -> int:
    """
    Remove duplicate events that represent the same real occurrence.
    Duplicates arise when the same iCal feed mixes UTC (Z) and TZID-local timestamps
    across ingestion runs — the IDs differ but the events are the same.

    Strategy: group by (org_id, title), parse all start_times to UTC, and delete
    any event within 2 minutes of another in the same group, preferring the one
    whose start_time contains a timezone offset.
    """
    def _parse_utc(s: str) -> datetime | None:
        if not s:
            return None
        for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z",
                    "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"):
            try:
                dt = datetime.strptime(s, fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt.astimezone(timezone.utc)
            except ValueError:
                continue
        return None

    with _conn() as c:
        rows = c.execute("SELECT id, org_id, title, start_time FROM events").fetchall()

    by_key: dict[tuple, list] = {}
    for row in rows:
        key = (row["org_id"], row["title"])
        by_key.setdefault(key, []).append(dict(row))

    to_delete: set[str] = set()
    for group in by_key.values():
        if len(group) < 2:
            continue
        # Annotate with parsed UTC time
        parsed = [(e, _parse_utc(e["start_time"])) for e in group]
        parsed = [(e, t) for e, t in parsed if t is not None]
        # Find pairs within 2 minutes of each other
        for i, (e1, t1) in enumerate(parsed):
            for e2, t2 in parsed[i + 1:]:
                if abs((t1 - t2).total_seconds()) <= 120:
                    # Prefer the one with explicit timezone offset in the string
                    has_tz1 = "+" in e1["start_time"] or e1["start_time"].endswith("Z")
                    has_tz2 = "+" in e2["start_time"] or e2["start_time"].endswith("Z")
                    if has_tz1 and not has_tz2:
                        to_delete.add(e2["id"])
                    elif has_tz2 and not has_tz1:
                        to_delete.add(e1["id"])
                    else:
                        # Both or neither have tz — delete the one with .000
                        if ".000" in e1["start_time"]:
                            to_delete.add(e1["id"])
                        else:
                            to_delete.add(e2["id"])

    if not to_delete:
        return 0
    with _conn() as c:
        c.executemany("DELETE FROM events WHERE id = ?", [(id_,) for id_ in to_delete])
    return len(to_delete)


def add_submission(name: str, city: str = None, website: str = None,
                   tradition: str = None, notes: str = None, submitter: str = None) -> int:
    """Insert a center submission. Returns the new row id."""
    submitted_at = datetime.now(timezone.utc).isoformat()
    with _conn() as c:
        cur = c.execute(
            """INSERT INTO center_submissions (name, city, website, tradition, notes, submitter, submitted_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (name, city, website, tradition, notes, submitter, submitted_at),
        )
        return cur.lastrowid


def get_submissions() -> list[dict]:
    """Return all center submissions, newest first."""
    with _conn() as c:
        return [dict(r) for r in c.execute(
            "SELECT * FROM center_submissions ORDER BY submitted_at DESC"
        ).fetchall()]


def add_correction(org_id: str = None, org_name: str = None,
                   description: str = "", contact: str = None) -> int:
    """Insert a correction report. Returns the new row id."""
    submitted_at = datetime.now(timezone.utc).isoformat()
    with _conn() as c:
        cur = c.execute(
            """INSERT INTO corrections (org_id, org_name, description, contact, submitted_at)
               VALUES (?, ?, ?, ?, ?)""",
            (org_id, org_name, description, contact, submitted_at),
        )
        return cur.lastrowid


def get_corrections() -> list[dict]:
    """Return all correction reports, newest first."""
    with _conn() as c:
        return [dict(r) for r in c.execute(
            "SELECT * FROM corrections ORDER BY submitted_at DESC"
        ).fetchall()]


def add_subscriber(email: str, cities: list[str] | None = None, tradition: str | None = None) -> dict:
    """
    Subscribe an email address. Returns {"ok": True} or {"exists": True} if already active.
    Raises ValueError on invalid input.
    """
    email = email.strip().lower()
    if not email or "@" not in email or len(email) > 320:
        raise ValueError("invalid email")
    token = _make_unsubscribe_token(email)
    cities_json = json.dumps(cities) if cities else None
    subscribed_at = datetime.now(timezone.utc).isoformat()
    with _conn() as c:
        existing = c.execute(
            "SELECT id, is_active FROM subscribers WHERE email = ?", (email,)
        ).fetchone()
        if existing:
            if existing["is_active"]:
                return {"exists": True}
            # Reactivate
            c.execute(
                "UPDATE subscribers SET is_active=1, cities=?, tradition=?, subscribed_at=? WHERE email=?",
                (cities_json, tradition, subscribed_at, email),
            )
            return {"ok": True, "reactivated": True}
        c.execute(
            "INSERT INTO subscribers (email, cities, tradition, unsubscribe_token, subscribed_at) VALUES (?,?,?,?,?)",
            (email, cities_json, tradition, token, subscribed_at),
        )
        return {"ok": True}


def unsubscribe_by_token(token: str) -> bool:
    """Deactivate subscription by unsubscribe token. Returns True if found."""
    with _conn() as c:
        cur = c.execute(
            "UPDATE subscribers SET is_active=0 WHERE unsubscribe_token=? AND is_active=1",
            (token,),
        )
        return cur.rowcount > 0


def get_active_subscribers() -> list[dict]:
    """Return all active subscribers."""
    with _conn() as c:
        rows = c.execute(
            "SELECT id, email, cities, tradition, unsubscribe_token FROM subscribers WHERE is_active=1"
        ).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d["cities"] = json.loads(d["cities"]) if d["cities"] else None
            result.append(d)
        return result


def get_upcoming_events(
    city: Optional[str | list[str]] = None,
    state: Optional[str | list[str]] = None,
    tradition: Optional[str] = None,
    location_type: Optional[str] = None,
    org_id: Optional[str] = None,
    days_ahead: int = 30,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    limit: int = 500,
) -> list[dict]:
    if start_date and end_date:
        q = """
            SELECT * FROM events
            WHERE start_time >= ?
              AND start_time <= ?
              AND is_sit = 1
        """
        params: list = [start_date, end_date]
    elif start_date:
        q = """
            SELECT * FROM events
            WHERE start_time >= ?
              AND is_sit = 1
        """
        params = [start_date]
    else:
        q = """
            SELECT * FROM events
            WHERE start_time >= datetime('now')
              AND start_time <= datetime('now', ? || ' days')
              AND is_sit = 1
        """
        params = [str(days_ahead)]
    if city:
        cities = [city] if isinstance(city, str) else city
        if len(cities) == 1:
            q += " AND city = ?"
            params.append(cities[0])
        else:
            q += f" AND city IN ({','.join('?' * len(cities))})"
            params.extend(cities)
    if state:
        states = [state] if isinstance(state, str) else state
        if len(states) == 1:
            q += " AND state = ?"
            params.append(states[0])
        else:
            q += f" AND state IN ({','.join('?' * len(states))})"
            params.extend(states)
    if tradition:
        q += " AND tradition = ?"
        params.append(tradition)
    if org_id:
        q += " AND org_id = ?"
        params.append(org_id)
    if location_type == "in-person":
        q += " AND location_type IN ('in-person', 'hybrid')"
    elif location_type == "online":
        q += " AND location_type IN ('online', 'hybrid')"
    q += " ORDER BY start_time LIMIT ?"
    params.append(limit)
    with _conn() as c:
        return [dict(r) for r in c.execute(q, params).fetchall()]
