from flask import Blueprint

ping_controller = Blueprint("ping", __name__)


@ping_controller.route("/ping")
def ping():
    return "pong"
