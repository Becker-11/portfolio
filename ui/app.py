import sys
from pathlib import Path

# make portfolio/ the root of imports
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from flask import Flask, render_template
from research_aggregator.ui.research import research_bp

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app.route("/")
def home():
    return render_template("home.html")

app.register_blueprint(research_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
