#!/usr/bin/env python3
# ingest/arxiv_fetcher.py

import os
import sys
import warnings
import argparse
from pathlib import Path
from typing import Dict, List
from datetime import datetime

from dotenv import load_dotenv
from transformers import logging as hf_logging
import yaml
import arxiv
from supabase import create_client

# ──────────────────────────────────────────────────────────────────────────────
#  Load .env (locally) then Supabase HTTP client
# ──────────────────────────────────────────────────────────────────────────────
load_dotenv()  # turn on if you have research_aggregator/.env

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
if not (SUPABASE_URL and SUPABASE_KEY):
    raise RuntimeError("Need SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY env‑vars")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ──────────────────────────────────────────────────────────────────────────────
#  Quiet down transformers warnings
# ──────────────────────────────────────────────────────────────────────────────
hf_logging.set_verbosity_error()
warnings.filterwarnings("ignore", message=".*torch.tensor.*", category=UserWarning)

# ──────────────────────────────────────────────────────────────────────────────
#  Make your repo root importable so `summarize/` is visible
# ──────────────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[1]  # research_aggregator/
sys.path.insert(0, str(ROOT))

from summarize.summarizer import enrich_paper

# ──────────────────────────────────────────────────────────────────────────────
#  Load your sources.yaml
# ──────────────────────────────────────────────────────────────────────────────
CONFIG_PATH = ROOT / "config" / "sources.yaml"
def load_sources() -> Dict:
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f)

# ──────────────────────────────────────────────────────────────────────────────
#  Fetch + debug print
# ──────────────────────────────────────────────────────────────────────────────
def fetch_arxiv(max_results: int) -> List[Dict]:
    cfg   = load_sources().get("arxiv", {})
    cats  = cfg.get("categories", [])
    kws   = cfg.get("keywords", [])

    cat_q = " OR ".join(f"cat:{c}" for c in cats)
    ti_q  = " OR ".join(f"ti:{kw}"  for kw in kws)
    abs_q = " OR ".join(f"abs:{kw}" for kw in kws)
    kw_q  = f"({ti_q}) OR ({abs_q})" if kws else ""

    #query = f"({cat_q}) AND ({kw_q})" if cat_q and kw_q else cat_q or kw_q

    base_q = f"({cat_q}) AND ({kw_q})" if cat_q and kw_q else cat_q or kw_q

    # ── date‐range for last 48 hours ─────────────────────────────────────────
    from datetime import datetime, timedelta
    now = datetime.utcnow()
    ago48 = now - timedelta(days=2)
    # ArXiv wants YYYYMMDDhhmm (we’ll zero‐pad minutes/hours)
    r1 = ago48.strftime("%Y%m%d%H%M")
    r2 = now.strftime   ("%Y%m%d%H%M")
    date_q = f"lastUpdatedDate:[{r1} TO {r2}]"

    query = f"{base_q} AND ({date_q})"

    print("🔍 ArXiv query string:", query)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    client = arxiv.Client()
    results = []
    for result in client.results(search):
        print("  •", result.published.isoformat(), "→", result.title[:60] + "…")
        results.append({
            "id":        result.get_short_id(),
            "title":     result.title,
            "abstract":  result.summary,
            "url":       result.pdf_url,
            "published": result.published.isoformat(),
        })
    return results



# ──────────────────────────────────────────────────────────────────────────────
#  Save via Supabase HTTP upsert
# ──────────────────────────────────────────────────────────────────────────────
def save_papers(papers: List[Dict]):
    for p in papers:
        supabase.table("papers").upsert({
            "id":        p["id"],
            "title":     p["title"],
            "abstract":  p["abstract"],
            "url":       p["url"],
            "published": p["published"],
            "summary":   p.get("summary", ""),
            "keywords":  ",".join(p.get("keywords", [])),
        }).execute()

# ──────────────────────────────────────────────────────────────────────────────
#  Orchestrator
# ──────────────────────────────────────────────────────────────────────────────
def process_papers(max_results: int):
    raw      = fetch_arxiv(max_results)
    enriched = [enrich_paper(p) for p in raw]
    save_papers(enriched)
    print(f"\n✅  Processed {len(enriched)} papers:")
    for p in enriched:
        print(" •", p["id"], "-", p["title"])

# ──────────────────────────────────────────────────────────────────────────────
#  CLI entrypoint
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and ingest ArXiv AI-safety papers")
    parser.add_argument(
        "--max_results", "-n",
        type=int,
        default=10,
        help="How many of the most recent papers to pull (default: 10)"
    )
    args = parser.parse_args()
    process_papers(max_results=args.max_results)
