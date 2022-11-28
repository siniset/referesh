from flask import render_template
from app.app import app

@app.route("/")
def index():
    return render_template("index.html")
