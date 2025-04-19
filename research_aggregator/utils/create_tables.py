import sys
from pathlib import Path

# Ensure portfolio root is on path so we can import the package
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import os
from dotenv import load_dotenv
load_dotenv(ROOT / ".env")

from research_aggregator.db.session import engine
from research_aggregator.db.models  import Base

if __name__ == "__main__":
    print("▶️  Connecting to database at:", engine.url)
    Base.metadata.create_all(bind=engine)
    print("✅  All tables created or already exist!")
