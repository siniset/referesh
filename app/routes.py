from flask import render_template, request, redirect
from app.app import app
from app import save_reference, get_references, delete_reference
from app.controllers import reference_controller


@app.route("/")
def index():
    references = reference_controller.get_titles()
    return render_template("index.html", references=references)


@app.route("/save", methods=["POST"])
def save():
    if request.method == "POST":
        type = request.form["type"]
        author = request.form["author"]
        book_name = request.form["name"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        reference_name = request.form["reference_name"]

        if save_reference.save(type, author, book_name, year, publisher, reference_name):
            return redirect("/")
        else:
            return render_template("error.html")


@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        id = request.form["id"]

        if delete_reference.delete(id):
            return redirect("/")
        else:
            return render_template("error.html")
