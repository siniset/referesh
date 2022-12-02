from flask import render_template, Blueprint, request, redirect
from services.book_service import book_service

book_controller = Blueprint("todo", __name__)


@book_controller.route("/")
def get_all_books():
    references = book_service.get_all_books()
    return render_template("index.html", references=references)

@book_controller.route("/save", methods=["POST"])
def create_book():
    if request.method == "POST":
        author = request.form["author"]
        book_name = request.form["name"]
        year = request.form["year"]
        publisher = request.form["publisher"]

        if book_service.create_book(author, book_name, year, publisher):
            return redirect("/")
        else:
            return render_template("error.html")

#@todo_controller.route("/todos/delete/<todo_id>", methods=["POST"])
#def delete_todo(todo_id):
#    todo_service.delete_todo(int(todo_id))
#
#    return redirect("/")
