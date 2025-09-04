# 📡 Market Scout Agent

An AI-powered intelligence engine for **Haycarb** that continuously scans markets, competitors, and regulations to uncover business opportunities in **PFAS water treatment, soil remediation, gold mining, and industrial carbon applications**.

---

## 🚀 Features

- **Data Ingestion** → RSS feeds + lightweight scrapers (Requests, BeautifulSoup, Feedparser).
- **Enrichment** → OpenAI LLM extracts structured insights (region, segment, competitors, deadlines, relevance scores).
- **Database** → SQLite (MVP) with migration path to PostgreSQL + pgvector for retrieval.
- **API Layer** → FastAPI endpoints for opportunities, competitors, and regulations.
- **UI (planned)** → React + Tailwind dashboard (or lightweight Flask + HTMX).
- **Alerts** → Slack webhook for high-priority opportunities & weekly digests.
- **Deployment** → Local with Uvicorn/Docker; future cloud deploy to Render / Fly.io / Cloud Run.

---

## 🛠️ Tech Stack

### Backend
- **Python 3.11+**
- [FastAPI](https://fastapi.tiangolo.com/) — REST API
- [Uvicorn](https://www.uvicorn.org/) — ASGI server
- [SQLite](https://www.sqlite.org/) — lightweight DB (Postgres later)
- [SQLAlchemy (planned)](https://www.sqlalchemy.org/) — ORM layer (future)

### Ingestion
- [Requests](https://docs.python-requests.org/) — HTTP client
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing
- [Feedparser](https://pypi.org/project/feedparser/) — RSS ingestion
- [Tenacity](https://tenacity.readthedocs.io/) — retry logic

### Enrichment (AI)
- [OpenAI API](https://platform.openai.com/) — LLM-based summarization & entity extraction
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

### Utilities
- [Hashlib](https://docs.python.org/3/library/hashlib.html) — deduplication
- [Slugify](https://github.com/un33k/python-slugify) — safe IDs

### Frontend (planned)
- [React](https://react.dev/) + [Vite](https://vitejs.dev/) — frontend framework
- [TailwindCSS](https://tailwindcss.com/) — styling
- [Recharts](https://recharts.org/) — charts & visualizations
- [Leaflet / Mapbox](https://leafletjs.com/) — opportunity heatmaps

### Orchestration & Deployment
- Cron (local) / Task Scheduler (Windows)
- GitHub Actions (CI/CD)
- Docker + Docker Compose
- Cloud: Render / Fly.io / Google Cloud Run

---

## 📂 Project Structure

```bash
Scout_Agent/
│── backend/
│   ├── app.py              # FastAPI app
│   ├── db.py               # DB init + connection
│   ├── models.sql          # schema (opportunities table)
│   ├── ingest/             # RSS + scraping modules
│   ├── enrich/             # LLM enrichment (OpenAI)
│   ├── jobs/               # scheduled jobs (ingest, enrich)
│   ├── utils/              # helper functions (hash, text clean)
│── market_scout.db         # SQLite DB
│── requirements.txt        # Python dependencies
│── .env.example            # env variables template
│── docker-compose.yml      # local dev setup
│── Dockerfile              # container build
│── README.md               # project docs (this file)



