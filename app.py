from flask import Flask


class MyAplication:
    def __init__(self):
        self.app = Flask(__name__, template_folder="src/templates")
        self.build_blueprints()

    def build_blueprints(self):
        pass

    def run_application(self):
        self.app.run(debug=True, port=5000)
