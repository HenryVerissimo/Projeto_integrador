from flask import Blueprint, render_template
from flask.views import MethodView


from src.WEB.controllers.select_controller import SelectController


class HomeBlueprint:
    def __init__(self):
        self.home_bp = Blueprint("home", __name__, url_prefix="/", template_folder="templates/home")
        self.build_routes()

    def build_routes(self):
        self.home_bp.add_url_rule("/", view_func=HomeRoute.as_view("home"), methods=["GET", "POST"])


class HomeRoute(MethodView):
    def get(self):

        request = SelectController.select_all_games()

        return render_template("home/home.html", games=request["response"])
    
    def post(self):
        pass
