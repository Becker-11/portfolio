# api/index.py
import os
from pathlib import Path
from flask import Flask, render_template

# Make sure Flask can find your templates
BASE = Path(__file__).resolve().parent.parent
template_folder = BASE / "ui" / "templates"
static_folder   = BASE / "ui" / "static"

app = Flask(
    __name__,
    template_folder=str(template_folder),
    static_folder=str(static_folder),
)

# Portfolio homepage
@app.route("/")
def home():
    return render_template("home.html")

# Mount the research blueprint
from research_aggregator.ui.research import research_bp
app.register_blueprint(research_bp)

# **IMPORTANT**: Vercel’s Python builder expects `app` or `handler`
# for WSGI. Flask’s `app` works out-of-the-box.

