from flask import render_template, request, redirect
from app.app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    if request.method == "POST":
        author = request.form["author"]
        name = request.form["name"]
        year = request.form["year"]
        publisher = request.form["publisher"]

        #tässä tapahtuu sitten save_reference moduulin funktion kutsu
        #ja talletus tapahtuu

    return redirect("/")