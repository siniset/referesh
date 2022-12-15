import sys
import logging
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import declarative_base, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

Base = declarative_base()
connection = None


class DatabaseConnection:
    def create_engine(self, url):
        self.engine = create_engine(url, echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def create_tables(self):
        try:
            Base.metadata.create_all(self.engine)
        except exc.OperationalError:
            logging.error("Unable to create tables")
            sys.exit(1)

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)

    def create_session(self):
        self.session = self.Session()

    def close_session(self):
        self.session.close()
        self.session = None


def connect(app=None):
    global connection, Base

    if Config.FLASK_ENV == "test":
        connection = DatabaseConnection()
        connection.create_engine(Config.DATABASE_URL)
    elif app:
        app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URL
        connection = SQLAlchemy(app)
        Base = connection.Model


def get_session():
    return connection.session
