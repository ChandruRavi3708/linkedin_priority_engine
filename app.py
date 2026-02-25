from flask import Flask, render_template, request
import json
from scorer import PriorityEngine

app = Flask(__name__)

# Load candidates
with open("candidates.json") as f:
    candidates = json.load(f)

engine = PriorityEngine()

@app.route("/", methods=["GET", "POST"])
def index():
    ranked = []

    if request.method == "POST":
        skills_input = request.form.get("skills")
        required_skills = [s.strip() for s in skills_input.split(",") if s.strip()]
        ranked = engine.rank_candidates(candidates, required_skills)

    return render_template("index.html", ranked=ranked)

if __name__ == "__main__":
    app.run(debug=True)