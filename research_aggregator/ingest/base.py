# research_aggregator/ingest/base.py

from typing import List, Dict

class BaseFetcher:
    def fetch(self, max_results: int) -> List[Dict]:
        """
        Fetch and return a list of paper-dicts from this source.
        Required keys: id, title, abstract, url, published
        Optional keys: summary, keywords, source
        """
        raise NotImplementedError("Subclasses must implement fetch()")

    def save(self, papers: List[Dict]) -> None:
        """
        Save the list of papers to your database (e.g., Supabase).
        Use upserts to avoid duplicates.
        """
        raise NotImplementedError("Subclasses must implement save()")
