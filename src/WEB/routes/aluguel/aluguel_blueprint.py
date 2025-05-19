from flask import Blueprint, render_template
from flask.views import MethodView

from src.WEB.controllers.select_controller import SelectController


class AluguelBlueprint:
    def __init__(self):
        self.aluguel_bp = Blueprint("aluguel", __name__, url_prefix="/aluguel", template_folder="templates/aluguel")
        self.build_routes()

    def build_routes(self):
        self.aluguel_bp.add_url_rule("/", view_func=AluguelRoute.as_view("aluguel"), methods=["GET", "POST"])


class AluguelRoute(MethodView):
    def get(self):

        request = SelectController.select_all_games_rental()
        request2 = SelectController.select_all_games()

        return render_template("aluguel/aluguel.html", alugueis=request["response"], games=request2["response"])
    
    def post(self):
        pass