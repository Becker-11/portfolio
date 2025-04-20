# ingest/arxiv_fetcher.py

import os
import warnings
from transformers import logging as hf_logging

# 1) Only show real errors from transformers
hf_logging.set_verbosity_error()
warnings.filterwarnings("ignore", message=".*torch.tensor.*", category=UserWarning)

import yaml
from pathlib import Path
from typing import Dict, List
from datetime import datetime

from supabase import create_client
import arxiv
from summarize.summarizer import enrich_paper

# ————————————————————————————————————————————————
#  Supabase client setup (HTTP)
# ————————————————————————————————————————————————
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
if not (SUPABASE_URL and SUPABASE_KEY):
    raise RuntimeError("Need SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY env‑vars")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ————————————————————————————————————————————————
#  Config loader
# ————————————————————————————————————————————————
ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.yaml"
def load_sources() -> Dict:
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f)

# ————————————————————————————————————————————————
#  Fetch + enrich
# ————————————————————————————————————————————————
def fetch_arxiv(max_results: int = 10) -> List[Dict]:
    cfg = load_sources().get("arxiv", {})
    cats = cfg.get("categories", [])
    kws  = cfg.get("keywords", [])
    cat_q = " OR ".join(f"cat:{c}" for c in cats)
    kw_q  = " OR ".join(kws)
    q = f"({cat_q}) AND ({kw_q})" if cat_q and kw_q else cat_q or kw_q

    search = arxiv.Search(query=q, max_results=max_results, sort_by=arxiv.SortCriterion.SubmittedDate)
    return [
        {
          "id": r.get_short_id(),
          "title": r.title,
          "abstract": r.summary,
          "url": r.pdf_url,
          "published": r.published.isoformat()
        }
        for r in arxiv.Client().results(search)
    ]

# ————————————————————————————————————————————————
#  Save via Supabase HTTP
# ————————————————————————————————————————————————
def save_papers(papers: List[Dict]):
    # Use upsert so you never get dup errors
    for p in papers:
        supabase.table("papers").upsert({
          "id":        p["id"],
          "title":     p["title"],
          "abstract":  p["abstract"],
          "url":       p["url"],
          "published": p["published"],   # ISO string is fine
          "summary":   p["summary"],
          "keywords":  ",".join(p["keywords"]),
        }).execute()

def process_papers(max_results: int = 10):
    raw      = fetch_arxiv(max_results)
    enriched = [enrich_paper(p) for p in raw]
    save_papers(enriched)
    for p in enriched:
        print(f"{p['id']}: {p['title']}")

if __name__ == "__main__":
    process_papers(max_results=20)
