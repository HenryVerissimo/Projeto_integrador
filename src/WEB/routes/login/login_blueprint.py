from flask import Blueprint, render_template, redirect, url_for, request
from flask.views import MethodView

from src.WEB.controllers.login_account_controller import LoginAccountController


class LoginBlueprint:
    def __init__(self):
        self.login_bp = Blueprint("Login", __name__, url_prefix="/login", template_folder="templates/login")
        self.build_routes()

    def build_routes(self):
        self.login_bp.add_url_rule("/", view_func=LoginRoute.as_view("login"), methods=["GET", "POST"])


class LoginRoute(MethodView):
    def get(self):
        return render_template("login/login.html")
    
    def post(self):
        email = request.form["email"]
        password = request.form["password"]

        response = LoginAccountController().login_account(email=email, password=password)

        if response["status"] == "success":
            return redirect("/")
        
        return render_template("login/login.html", error=response["message"])

