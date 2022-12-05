from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
app.app_context().push()

from app import routes  # noqa: #F401, E402

db.create_all()
