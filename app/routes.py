from flask import Blueprint, request, jsonify, render_template
import json
import os

main = Blueprint("main", __name__)

# Load the career data
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, "../data/careers.json"), "r", encoding="utf-8") as f:
    career_data = json.load(f)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        message = data.get("message", "").lower()

        for career, details in career_data.items():
            skills = [skill.lower() for skill in details["skills"]]
            if any(message in skill for skill in skills):
                return jsonify({
                    "career": career,
                    "description": details["description"],
                    "skills": details["skills"],
                    "resources": details["resources"]
                })

        return jsonify({
            "error": "No matching career found."
        })

    except Exception as e:
        return jsonify({"error": str(e)})

