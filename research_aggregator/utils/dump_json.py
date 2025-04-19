#!/usr/bin/env python
import json
from pathlib import Path

from research_aggregator.db.session import SessionLocal
from research_aggregator.db.models  import Paper

def dump_to_static():
    """Query all papers from SQLite and write them out as JSON."""
    session = SessionLocal()
    papers = (
        session
        .query(Paper)
        .order_by(Paper.published.desc())
        .all()
    )
    session.close()

    data = []
    for p in papers:
        data.append({
            "id":        p.id,
            "title":     p.title,
            "url":       p.url,
            "published": p.published.isoformat(),
            "summary":   p.summary,
            "keywords":  p.keywords.split(",") if p.keywords else []
        })

    # write into your UI static folder
    out = Path(__file__).resolve().parent.parent / "ui" / "static" / "data.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {len(data)} papers to {out}")

if __name__ == "__main__":
    dump_to_static()
