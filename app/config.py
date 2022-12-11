from os import environ
from dotenv import find_dotenv, load_dotenv
import logging

load_dotenv(find_dotenv())

MODE = environ.get("MODE") or "production"

DATABASE_URL = environ.get("DATABASE_URL")
if MODE == "test":
    DATABASE_URL = environ.get("TEST_DATABASE_URL")
if not DATABASE_URL:
    logging.error("DATABASE_URL is not set.")
    exit(1)
DATABASE_URL = DATABASE_URL.replace('://', 'ql://', 1) \
    if DATABASE_URL.startswith('postgres://') else DATABASE_URL


class Config:
    FLASK_ENV = MODE
    DATABASE_URL = DATABASE_URL
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
