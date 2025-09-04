import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from backend.utils.text import strip_html

HEADERS = {"User-Agent": "Mozilla/5.0 (MarketScoutBot)"}

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=6))
def fetch_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.text

def clean_text_from_url(url: str) -> str:
    try:
        return strip_html(fetch_html(url))[:20000]
    except Exception as e:
        return f"FETCH_ERROR: {e}"
