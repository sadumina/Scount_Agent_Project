# backend/app.py
from fastapi import FastAPI
import sqlite3
from pathlib import Path

app = FastAPI(title="Market Scout API", version="0.2.0")

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "market_scout.db"

def conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

@app.get("/")
def health():
    return {"status": "ok", "service": "Market Scout API"}

@app.get("/opportunities")
def list_ops(limit: int = 25):
    c = conn().execute(
        "SELECT id, headline, region, segment, url, published_at, relevance_score "
        "FROM opportunities ORDER BY rowid DESC LIMIT ?",
        (limit,)
    )
    cols = [d[0] for d in c.description]
    return [dict(zip(cols, r)) for r in c.fetchall()]
