from flask import Blueprint, render_template, request
from flask.views import MethodView


from src.WEB.controllers.select_controller import SelectController


class CatalogoBlueprint:
    def __init__(self):
        self.catalogo_bp = Blueprint("catalogo", __name__, url_prefix="/catalogo", template_folder="templates/catalogo")
        self.build_routes()

    def build_routes(self):
        self.catalogo_bp.add_url_rule("/", view_func=CatalogoRoute.as_view("catalogo"), methods=["GET", "POST"])


class CatalogoRoute(MethodView):
    def get(self):

        request = SelectController.select_all_games()

        return render_template("catalogo/catalogo.html", games=request["response"])
    
    def post(self):
        
        pesquisa = request.form["pesquisa"]
        response = SelectController.select_all_games()

        return render_template("catalogo/catalogo.html", games=response["response"], pesquisa=pesquisa)
