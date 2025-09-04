import time
import feedparser

def fetch_rss(url: str):
    d = feedparser.parse(url)
    items = []
    for e in d.entries:
        items.append({
            "title": getattr(e, "title", ""),
            "link": getattr(e, "link", ""),
            "published_at": getattr(e, "published", time.strftime("%Y-%m-%d")),
            "source": d.feed.get("title", url)
        })
    return items
