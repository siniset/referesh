from os import environ
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Config:
    FLASK_ENV = environ.get("development") or "production"
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    DATABASE_URL = environ.get("DATABASE_URL")
    TEST_DATABASE_URL = environ.get("TEST_DATABASE_URL")
