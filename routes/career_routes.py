from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from services.groq_service import ask_ai

# ✅ Blueprint MUST be defined first
career_bp = Blueprint("career", __name__)


@career_bp.route("/counsel")
def counsel():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return render_template("counsel.html", user=session["user"])


@career_bp.route("/generate_career_path", methods=["POST"])
def generate_career_path():
    if "user" not in session:
        return jsonify({"result": "Unauthorized"}), 401

    career = request.json.get("career", "").strip()
    if not career:
        return jsonify({"result": "Career is required"}), 400

    prompt = f"Create a detailed career roadmap for {career}"

    try:
        result = ask_ai(prompt)
        return jsonify({"result": result})
    except Exception as e:
        print("Career Path Error:", e)
        return jsonify({"result": "⚠️ AI service failed."}), 500


@career_bp.route("/generate_courses", methods=["POST"])
def generate_courses():
    if "user" not in session:
        return jsonify({"result": "Unauthorized"}), 401

    career = request.json.get("career", "").strip()
    if not career:
        return jsonify({"result": "Career is required"}), 400

    prompt = f"""
You are a professional career counselor.

For the career "{career}", recommend 5 high-quality online courses.
For each course, include:
- Course name
- Platform
- Short description
- Skill level

Format the response clearly.
"""

    try:
        result = ask_ai(prompt)
        return jsonify({"result": result})
    except Exception as e:
        print("Course Error:", e)
        return jsonify({"result": "⚠️ AI service failed."}), 500


@career_bp.route("/job_market_insights", methods=["POST"])
def job_market_insights():
    if "user" not in session:
        return jsonify({"result": "Unauthorized"}), 401

    career = request.json.get("career", "").strip()
    if not career:
        return jsonify({"result": "Career is required"}), 400

    prompt = f"""
You are a job market analyst.

Provide job market insights for "{career}" in India.
Include demand, salary, locations, skills, and future outlook.
"""

    try:
        result = ask_ai(prompt)
        return jsonify({"result": result})
    except Exception as e:
        print("Market Error:", e)
        return jsonify({"result": "⚠️ AI service failed."}), 500
