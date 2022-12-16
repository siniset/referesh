from pytest import fixture
from sqlalchemy import select

from app import db
from app.controllers import field_controller
from app.controllers import project_controller
from app.models.field import Field
from app.models.reference import Reference


def append_fields(reference, fields):
    for field in fields:
        reference.fields.append(field)


def get_fields():
    return db.get_session().execute(select(Field)).all()


class TestFieldController:
    @fixture(scope="class", autouse=True)
    def setup_suite(self):
        db.connect()

    @fixture(scope='function', autouse=True)
    def setup_suite_test(self):
        db.connection.create_tables()
        db.connection.create_session()
        self.session = db.get_session()
        project_controller.create_default_project()
        yield
        db.connection.close_session()
        db.connection.drop_tables()

    def test_create_field_with_valid_values(self):
        self.session.add(
            Reference(
                name="REF_NAME_1",
                type="book",
                project_id=1))

        field_controller.create("author", "Joakim Korhonen", 1)
        field_controller.create("year", "2011", 1)
        assert 2 == len(get_fields())

    def test_delete_removes_existing_field(self):
        self.session.add(
            Reference(
                name="REF_NAME_1",
                type="book",
                project_id=1))

        field_controller.create("author", "Joakim Korhonen", 1)
        self.session.commit()

        field_controller.delete_by_id(1)
        assert 0 == len(get_fields())
