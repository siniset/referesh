from flask import Flask
from database import db
from config import DATABASE_URL, ENV
from controllers.book_controller import book_controller 
from controllers.test_controller import test_controller
from controllers.ping_controller import ping_controller


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(book_controller)
    app.register_blueprint(ping_controller)

    if ENV == "development":
        app.register_blueprint(test_controller)

    db.init_app(app)

    return app
