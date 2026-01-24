from flask import Blueprint, render_template, request, redirect, url_for, session
from services.db_service import create_user, authenticate_user

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
            return redirect(url_for("career.counsel"))
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.home"))
