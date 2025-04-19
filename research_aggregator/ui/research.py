# research_aggregator/ui/research.py

from flask import Blueprint, render_template

from research_aggregator.db.session import SessionLocal
from research_aggregator.db.models  import Paper

research_bp = Blueprint(
    "research",
    __name__,
    template_folder="templates",
    url_prefix="/research"
)

@research_bp.route("/")
def index():
    session = SessionLocal()
    papers = (
        session
        .query(Paper)
        .order_by(Paper.published.desc())
        .all()
    )
    session.close()
    return render_template("index.html", papers=papers)
