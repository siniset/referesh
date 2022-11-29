from os import environ
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


class Config:
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")
