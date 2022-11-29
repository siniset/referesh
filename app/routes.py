from flask import render_template, request, redirect
from app.app import app
from app import save_reference

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    if request.method == "POST":
        type = request.form["type"]
        author = request.form["author"]
        book_name = request.form["name"]
        year = request.form["year"]
        publisher = request.form["publisher"]

        if save_reference.save(type, author, book_name, year, publisher):
            return redirect("/")
