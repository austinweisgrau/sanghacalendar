"""
SQLite event store.

DB_PATH env var controls location (defaults to data/sangha.db for local dev).
On Fly.io: persistent volume mounted at /data, DB_PATH=/data/sangha.db.
"""

import os
import sqlite3
from pathlib import Path
from typing import Optional

from data.schemas.event import Event

DB_PATH = Path(os.environ.get("DB_PATH", Path(__file__).parent / "sangha.db"))

_CREATE_SQL = """
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
"""


def _conn() -> sqlite3.Connection:
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with _conn() as c:
        c.executescript(_CREATE_SQL)


def upsert_events(events: list[Event]) -> int:
    """Insert or update events. Returns rowcount."""
    rows = [
        (
            e.id, e.org_id, e.org_name, e.title, e.start_time, e.end_time,
            e.address, e.city, e.state, e.neighborhood, e.lat, e.lng,
            e.tradition.value if hasattr(e.tradition, "value") else e.tradition,
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
                tradition, is_sit, accessibility_notes, identity_focus,
                source, source_url, event_url, last_verified, recurrence, notes
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
                last_verified = excluded.last_verified,
                end_time      = excluded.end_time,
                notes         = excluded.notes
            """,
            rows,
        )
        return cur.rowcount


def get_upcoming_events(
    city: Optional[str] = None,
    tradition: Optional[str] = None,
    days_ahead: int = 60,
    limit: int = 500,
) -> list[dict]:
    q = """
        SELECT * FROM events
        WHERE start_time >= datetime('now')
          AND start_time <= datetime('now', ? || ' days')
          AND is_sit = 1
    """
    params: list = [str(days_ahead)]
    if city:
        q += " AND city = ?"
        params.append(city)
    if tradition:
        q += " AND tradition = ?"
        params.append(tradition)
    q += " ORDER BY start_time LIMIT ?"
    params.append(limit)
    with _conn() as c:
        return [dict(r) for r in c.execute(q, params).fetchall()]


