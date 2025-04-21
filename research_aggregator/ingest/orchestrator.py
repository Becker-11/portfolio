#!/usr/bin/env python3
# ingest/orchestrator.py

import argparse
import traceback
from typing import List, Type

from ingest.base import BaseFetcher
from ingest.arxiv_fetcher import ArxivFetcher
from summarize.summarizer import enrich_paper


# ─────────────────────────────────────────────────────────────
#  List all fetchers here
# ─────────────────────────────────────────────────────────────
FETCHERS: List[Type[BaseFetcher]] = [
    ArxivFetcher,
    # Add future fetchers here (e.g., AlignmentForumFetcher)
]


def process_fetcher(fetcher: BaseFetcher, max_results: int, dry_run: bool = False) -> int:
    """Fetch, enrich, and save papers from a given source."""
    papers = fetcher.fetch(max_results)
    enriched = [enrich_paper(p) for p in papers]

    if dry_run:
        print(f"🧪 {fetcher.__class__.__name__} would save {len(enriched)} papers (dry run)")
    else:
        fetcher.save(enriched)
        print(f"✅ {fetcher.__class__.__name__} saved {len(enriched)} papers")

    for p in enriched:
        print(" •", p["id"], "-", p["title"])

    return len(enriched)


def main(max_results: int, dry_run: bool = False):
    total = 0
    for FetcherClass in FETCHERS:
        fetcher_name = FetcherClass.__name__
        print(f"\n🚀 Running fetcher: {fetcher_name}")

        try:
            fetcher = FetcherClass()
            count = process_fetcher(fetcher, max_results, dry_run)
            total += count
        except Exception as e:
            print(f"❌ Error in {fetcher_name}: {e}")
            traceback.print_exc()

    print(f"\n🎉 Finished running {len(FETCHERS)} fetchers. Total papers: {total}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run all research ingest fetchers")
    parser.add_argument("--max_results", "-n", type=int, default=10, help="Max papers to fetch per source")
    parser.add_argument("--dry_run", action="store_true", help="Print results but don't write to DB")

    args = parser.parse_args()
    main(max_results=args.max_results, dry_run=args.dry_run)
