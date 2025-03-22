from flask import Blueprint, render_template
from flask.views import MethodView


class LoginBlueprint:
    def __init__(self):
        self.login_bp = Blueprint("Login", __name__, url_prefix="/login", template_folder="src/templates/login")
        self.build_routes()

    def build_routes(self):
        self.login_bp.add_url_rule("/", view_func=LoginRoute.as_view("login"), methods=["GET", "POST"])


class LoginRoute(MethodView):
    def get(self):
        return render_template("login/login.html")
    
    def post(self):
        pass