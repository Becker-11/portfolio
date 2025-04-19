# scheduler.py

import sys
from pathlib import Path

# Ensure our project packages are importable
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "research_aggregator"))

from apscheduler.schedulers.blocking import BlockingScheduler
from ingest.arxiv_fetcher import process_papers

def scheduled_job():
    print("🕓 Running scheduled fetch/enrich…")
    process_papers(max_results=10)

if __name__ == "__main__":
    sched = BlockingScheduler()
    # Run once at startup
    scheduled_job()
    # Then every hour on the hour
    sched.add_job(scheduled_job, 'cron', minute=0)
    print("Scheduler started: fetching new papers every hour.")
    sched.start()
