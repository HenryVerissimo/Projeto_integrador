from flask import Flask

from src.routes.home import HomeBlueprint
from src.routes.login import LoginBlueprint

class MyApplication:
    def __init__(self):
        self.app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
        self.build_blueprints()

    def build_blueprints(self):
        self.app.register_blueprint(HomeBlueprint().home_bp)
        self.app.register_blueprint(LoginBlueprint().login_bp)

    def run_application(self):
        self.app.run(debug=True, port=5000)

if __name__ == "__main__":

    app = MyApplication()
    app.run_application()
