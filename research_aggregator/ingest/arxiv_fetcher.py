import warnings
from transformers import logging as hf_logging

# 1) Only show errors from the transformers library
hf_logging.set_verbosity_error()

# 2) Ignore the torch.tensor copy‑construct UserWarning spam
warnings.filterwarnings(
    "ignore",
    message=".*torch.tensor.*",
    category=UserWarning
)

import sys
from pathlib import Path

# Determine project root and add to PYTHONPATH
ROOT = Path(__file__).resolve().parents[1]  # points to portfolio/research_aggregator
sys.path.insert(0, str(ROOT))

import yaml
import arxiv
from typing import Dict, List
from datetime import datetime

from summarize.summarizer import enrich_paper

from db.session import SessionLocal
from db.models import Paper

# Path to the config file
CONFIG_PATH = ROOT / "config" / "sources.yaml"

def load_sources(path: Path = CONFIG_PATH) -> Dict:
    """Load source configuration from YAML file."""
    with path.open() as f:
        return yaml.safe_load(f)


def fetch_arxiv(max_results: int = 10) -> List[Dict]:
    """Fetch recent AI-safety papers from arXiv using settings in sources.yaml."""
    cfg = load_sources()
    arxiv_cfg = cfg.get("arxiv", {})
    categories = arxiv_cfg.get("categories", [])
    keywords = arxiv_cfg.get("keywords", [])

    cat_query = " OR ".join(f"cat:{cat}" for cat in categories)
    kw_query = " OR ".join(keywords)
    query = f"({cat_query}) AND ({kw_query})" if cat_query and kw_query else cat_query or kw_query

    client = arxiv.Client()
    items: List[Dict] = []
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    for result in client.results(search):
        items.append({
            "id": result.get_short_id(),
            "title": result.title,
            "abstract": result.summary,
            "url": result.pdf_url,
            "published": result.published.isoformat()
        })
    return items


def save_papers(papers: List[Dict]) -> None:
    """
    Persist new papers to the database, skipping duplicates.
    Now includes summary and keywords.
    """
    session = SessionLocal()
    for p in papers:
        # Skip if paper already exists
        if session.query(Paper).filter_by(id=p["id"]).first():
            continue

        paper = Paper(
            id        = p["id"],
            title     = p["title"],
            abstract  = p["abstract"],
            url       = p["url"],
            published = datetime.fromisoformat(p["published"]),
            summary   = p.get("summary", ""),                     # new field
            keywords  = ",".join(p.get("keywords", []))          # new field
        )
        session.add(paper)

    session.commit()
    session.close()

def process_papers(max_results: int = 10):
    """
    Fetch latest arXiv papers, enrich them, save to DB, and print.
    """
    raw_papers = fetch_arxiv(max_results=max_results)
    enriched   = [enrich_paper(p) for p in raw_papers]
    save_papers(enriched)
    for p in enriched:
        print(f"{p['id']}: {p['title']} ({p['published']})")
        print("  Summary:", p["summary"])
        print("  Keywords:", ", ".join(p["keywords"]))
        print("-" * 80)

if __name__ == "__main__":
    process_papers(max_results=10)

