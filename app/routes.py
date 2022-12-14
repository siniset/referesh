from flask import render_template, request, redirect, abort, send_file
from app.app import app
from app.controllers import reference_controller
from app.controllers import field_controller
from app.services import export_service


@app.route("/")
def index():
    references = reference_controller.get_titles()
    return render_template("index.html", references=references)


@app.route("/references/<id>")
def reference(id):
    reference = reference_controller.get_by_id(id)

    fields = []
    for field in reference.fields:
        fields.append({
            "id": field.id,
            "name": field.name,
            "content": field.content
        })

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


@app.route("/references/edit/<id>", methods=["GET", "PUT"])
def edit(id):
    reference_controller.edit(
        id, "ilari", "book", {
            "author": "kjfdlkfjl author"})
    return redirect("/")


@app.route("/fields/<id>", methods=["PUT"])
def update_field(id):
    content = request.json["content"]
    field_controller.update(id, content)
    return {"content": content}


@app.route("/references/<id>", methods=["DELETE"])
def delete_reference(id):
    reference_controller.delete_by_id(id)
    return {"id": id}


@app.route("/fields/<id>", methods=["DELETE"])
def delete_field(id):
    field_controller.delete_by_id(id)
    return {"id": id}


@app.route("/export")
def export():
    references = reference_controller.get_all()
    bibtex_file = export_service.export_as_bibtex(references)
    return send_file(bibtex_file, download_name="references.bib")
