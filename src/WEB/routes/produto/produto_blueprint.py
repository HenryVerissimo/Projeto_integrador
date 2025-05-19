from flask import Blueprint, render_template, request
from flask.views import MethodView


from src.WEB.controllers.select_controller import SelectController


class ProdutoBlueprint:
    def __init__(self):
        self.produto_bp = Blueprint("produto", __name__, url_prefix="/produto/<int:id>", template_folder="templates/produto")
        self.build_routes()

    def build_routes(self):
        self.produto_bp.add_url_rule("/", view_func=ProdutoRoute.as_view("produto"), methods=["GET"])


class ProdutoRoute(MethodView):
    def get(self, id):

        response = SelectController.select_games_by_filter("ID", id)
        url_trailer = f"static/imgs/trailers/{response['response'][0]["name"].lower().replace(' ', '_')}_trailer.txt"

        try:
            with open(url_trailer, "r") as arquivo:
                link_trailer = arquivo.read()
            
            return render_template("produto/produto.html", game=response["response"][0], trailer=link_trailer)
        except:

            return render_template("produto/produto.html", game=response["response"][0])
    

