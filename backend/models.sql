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
