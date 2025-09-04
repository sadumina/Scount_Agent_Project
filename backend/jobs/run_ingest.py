# --- add near top (with other imports)
import sqlite3
from pathlib import Path

# ... existing imports ...

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "market_scout.db"

def ensure_schema(conn: sqlite3.Connection):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS opportunities (
        id TEXT PRIMARY KEY,
        source TEXT,
        url TEXT UNIQUE,
        region TEXT,
        segment TEXT,
        headline TEXT,
        published_at TEXT,
        raw_text TEXT,
        llm_summary TEXT,
        est_value_usd REAL,
        est_carbon_mt REAL,
        status TEXT DEFAULT 'open',
        relevance_score REAL,
        competitors TEXT,
        deadline TEXT
    );
    """)
    conn.commit()

def run():
    conn = sqlite3.connect(DB_PATH)
    ensure_schema(conn)  # <— ADD THIS LINE
    # ... rest of your code ...
