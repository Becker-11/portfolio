import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

# Allow a .env file locally if you like (optional)
from dotenv import load_dotenv
load_dotenv()

print("▶️  DATABASE_URL =", os.getenv("DATABASE_URL"))


# Default to SQLite for local development
default_sqlite = (
    Path(__file__).resolve().parent.parent
    / "data" / "AI_Research.db"
)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{default_sqlite}"
)

# For SQLite you need check_same_thread; for Postgres you don’t
engine = (
    create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    if DATABASE_URL.startswith("sqlite")
    else create_engine(DATABASE_URL)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import your models and create tables if they don’t exist
from .models import Base
Base.metadata.create_all(bind=engine)
