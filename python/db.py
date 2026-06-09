import sqlite3
import json
from datetime import datetime

DB = "database/iot.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id TEXT,
        device_type TEXT,
        event_type TEXT,
        payload TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_event(device_id, device_type, event_type, payload):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO events (device_id, device_type, event_type, payload, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        device_id,
        device_type,
        event_type,
        json.dumps(payload),
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def get_latest_per_device():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    SELECT e.*
    FROM events e
    INNER JOIN (
        SELECT device_id, MAX(timestamp) as max_time
        FROM events
        GROUP BY device_id
    ) latest
    ON e.device_id = latest.device_id AND e.timestamp = latest.max_time
    """)

    rows = c.fetchall()
    conn.close()
    return rows