from app.app import app

@app.route("/")
def index():
    return "index"
