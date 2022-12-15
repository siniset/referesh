from pytest import fixture
from app import db


def populate_database():
    db.connection.create_tables()
    db.connection.create_session()


def reset_database():
    db.connection.close_session()
    db.connection.drop_tables()


class UnitTest:
    @fixture(scope="class", autouse=True)
    def setup_suite(self):
        db.connect()

    @fixture(scope='function', autouse=True)
    def setup_suite_test(self):
        populate_database()
        self.session = db.get_session()
        yield
        reset_database()
