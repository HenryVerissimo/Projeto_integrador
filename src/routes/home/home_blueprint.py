from flask import Blueprint, render_template
from flask.views import MethodView


class HomeBlueprint:
    def __init__(self):
        self.home_bp = Blueprint("home", __name__, url_prefix="/", template_folder="src/templates/home")
        self.build_routes()

    def build_routes(self):
        self.home_bp.add_url_rule("/", view_func=HomeRoute.as_view("home"), methods=["GET", "POST"])


class HomeRoute(MethodView):
    def get(self):
        return render_template("home/home.html")
    
    def post(self):
        pass
