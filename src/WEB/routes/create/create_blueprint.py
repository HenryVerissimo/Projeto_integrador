from flask import Blueprint, render_template, redirect, url_for, request
from flask.views import MethodView

from src.WEB.controllers.create_user_controller import CreateUserController


class CreateBlueprint:
    def __init__(self):
        self.create_bp = Blueprint("create", __name__, url_prefix="/create", template_folder="templates/create")
        self.build_routes()

    def build_routes(self):
        self.create_bp.add_url_rule("/", view_func=CreateRoute.as_view("create"), methods=["GET", "POST"])


class CreateRoute(MethodView):
    def get(self):
        return render_template("create/create.html")

    def post(self):
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        response = CreateUserController().create_user(name=name, email=email, password=password, confirm_password=confirm_password)

        if response["status"] == "success":
            return redirect("/login")
        
        return render_template("create/create.html", error=response["message"])


