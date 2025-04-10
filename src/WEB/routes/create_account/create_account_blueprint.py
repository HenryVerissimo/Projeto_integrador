from flask import Blueprint, render_template
from flask.views import MethodView


class CreateAccountBlueprint:
    def __init__(self):
        self.create_account_bp = Blueprint("create_account", __name__, url_prefix="/create_account", template_folder="src/WEB/templates/create_account")

    def build(self):
        self.create_account_bp.add_url_rule("/", view_func=CreateAccountBlueprint.as_view("create_account"), methods=["GET", "POST"])


class CreateAccountRoute(MethodView):
    def get():
        pass

    def post():
        pass
