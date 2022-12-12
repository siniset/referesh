from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.models.reference import Reference
from sqlalchemy import delete, select
from dotenv import find_dotenv, load_dotenv
from os import environ

load_dotenv(find_dotenv())

class DatabaseLibrary():
    def __init__(self):
        self.engine = None
        self.Base = declarative_base()
        self.session = None
        self.Session = None

        self.create_database_connection(environ.get("DATABASE_URL"))
        self.create_session()


    def create_database_connection(self, url, echo=False):
        global engine, Base
        self.engine = create_engine(url, echo=echo)


    def create_tables(self):
        self.Base.metadata.create_all(engine)


    def drop_tables(self):
        self.Base.metadata.drop_all(engine)


    def create_session(self):
        global Session, session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def close_session(self):
        self.session.close()