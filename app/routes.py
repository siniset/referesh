from flask import render_template, request, redirect, abort
from app.app import app
from app.controllers import reference_controller


@app.route("/")
def index():
    references = reference_controller.get_titles()
    return render_template("index.html", references=references)


@app.route("/references/<id>")
def reference(id):
    reference = reference_controller.get_by_id(id)

    fields = {}
    for field in reference.fields:
        fields[field.name] = field.content

    return fields


@app.route("/save", methods=["POST"])
def save():
    name = request.form["name"]
    type = request.form["type"]

    if len(name) == 0:
        abort(400)

    fields = {
        "author": request.form["author"],
        "title": request.form["title"],
        "year": request.form["year"],
        "publisher": request.form["publisher"]
    }

    reference_controller.create(name, type, fields)
    return redirect("/")


@app.route("/delete/<id>", methods=["GET", "DELETE"])
def delete(id):
    reference_controller.delete_by_id(id)
    return redirect("/")
