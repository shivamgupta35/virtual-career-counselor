from flask import Blueprint, render_template, request, redirect, url_for, session
from services.db_service import create_user, authenticate_user
from services.sns_service import send_notification

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    return render_template("index.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        create_user(
            request.form["name"],
            request.form["email"],
            request.form["password"]
        )

        # Optional: SNS notification on new registration (LAB BONUS)
        send_notification(
            subject="New User Registration",
            message=f"New user registered: {request.form['email']}"
        )

        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = authenticate_user(
            request.form["email"],
            request.form["password"]
        )

        if user:
            session["user"] = user

            # SNS notification on login (LAB REQUIREMENT)
            send_notification(
                subject="Login Alert",
                message=f"{user['email']} logged in to Virtual Career Counselor"
            )

            return redirect(url_for("career.counsel"))

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.home"))
