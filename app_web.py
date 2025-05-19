from flask import Flask

from src.WEB.routes.home import HomeBlueprint
from src.WEB.routes.login import LoginBlueprint
from src.WEB.routes.create import CreateBlueprint
from src.WEB.routes.catalogo import CatalogoBlueprint
from src.WEB.routes.aluguel import AluguelBlueprint
from src.WEB.routes.produto import ProdutoBlueprint

class MyApplication:
    def __init__(self):
        self.app = Flask(__name__, template_folder="templates", static_url_path="/static", static_folder="static")
        self.build_blueprints()

    def build_blueprints(self):
        self.app.register_blueprint(HomeBlueprint().home_bp)
        self.app.register_blueprint(LoginBlueprint().login_bp)
        self.app.register_blueprint(CreateBlueprint().create_bp)
        self.app.register_blueprint(CatalogoBlueprint().catalogo_bp)
        self.app.register_blueprint(AluguelBlueprint().aluguel_bp)
        self.app.register_blueprint(ProdutoBlueprint().produto_bp)

    def run_application(self):
        self.app.run(debug=True, port=5000)

if __name__ == "__main__":

    app = MyApplication()
    app.run_application()