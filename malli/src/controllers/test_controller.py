from flask import Blueprint, request
from services.book_service import book_service

test_controller = Blueprint("test", __name__)


@test_controller.route("/tests/reset", methods=["POST"])
def reset():
    book_service.delete_all_books()

    return "ok"

@test_controller.route("/tests/todos", methods=["POST"])
def create_book():
    content = request.json["content"]
    done = request.json["done"]

    book_service.create_book(content, done)

    return "ok"
