from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = None
Base = declarative_base()
session = None
Session = None


def create_database_connection(url, echo=False):
    global engine, Base
    engine = create_engine(url, echo=echo)


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def create_session():
    global Session, session
    Session = sessionmaker(bind=engine)
    session = Session()


def close_session():
    session.close()
