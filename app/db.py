import logging
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import declarative_base, sessionmaker


engine = None
Base = declarative_base()
session = None
Session = None


def create_database_connection(url, echo=False):
    global engine, Base
    engine = create_engine(url, echo=echo, pool_recycle=20, pool_size=10, pool_pre_ping=True)


def create_tables():
    try:
        Base.metadata.create_all(engine)
    except exc.OperationalError:
        logging.error("Cannot connect to database!")
        exit(1)


def drop_tables():
    Base.metadata.drop_all(engine)


def create_session():
    global Session, session
    Session = sessionmaker(bind=engine)
    session = Session()


def close_session():
    session.close()
