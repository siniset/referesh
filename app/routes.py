from flask import render_template, request, redirect
from app.app import app, db
from app import save_reference


@app.route("/")
def index():
    res = db.session.execute("SELECT * FROM fields"
                             " WHERE name='author' OR name='title'")
    references = res.fetchall()
    return render_template("index.html", references=references)
# Need to combine results from same ids,
# GET route func for clean code, add del() route


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
        else:
            return render_template("error.html")
