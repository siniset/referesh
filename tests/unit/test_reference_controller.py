from pytest import fixture, raises
from sqlalchemy import select

from app import db
from app.config import Config
from app.models.field import Field
from app.models.reference import Reference
from app.controllers import reference_controller


@fixture(scope="class", autouse=True)
def setup_suite():
    db.create_database_connection(Config.DATABASE_URL)


@fixture(scope='function', autouse=True)
def setup_suite_test():
    db.drop_tables()
    db.create_tables()
    db.create_session()
    yield
    db.close_session()


class TestReferenceController:
    def test_create_adds_reference_with_valid_values(self):
        reference_controller.create("REFNAME", "Book title")
        assert 1 == 1

    def test_create_fails_with_invalid_values(self):
        with raises(Exception) as excinfo:
            reference_controller.create("", "Book title")

        assert str(excinfo.value) == "Name is invalid"
        assert 0 == len(db.session.execute(select(Reference)).all())

    def test_get_by_id_returns_correct_reference(self):
        db.session.add(Reference(name="REF_NAME_1", type="book"))
        db.session.add(Reference(name="REF_NAME_2", type="book"))
        db.session.add(Reference(name="REF_NAME_3", type="book"))
        db.session.commit()

        reference = reference_controller.get_by_id(2)
        assert "REF_NAME_2" == reference.name

    def test_get_titles_return_correct_format(self):
        reference = Reference(name="REF_NAME_1", type="book")
        reference.fields.append(Field(name="year", content="2000"))
        reference.fields.append(Field(name="title", content="Book Title"))
        reference.fields.append(Field(name="author", content="Book Author"))

        db.session.add(reference)

        reference = Reference(name="REF_NAME_2", type="book")
        reference.fields.append(Field(name="year", content="1000"))
        reference.fields.append(Field(name="title", content="Book Title 2"))
        reference.fields.append(Field(name="author", content="Book Author 2"))

        db.session.add(reference)

        db.session.commit()
        references = reference_controller.get_titles()

        assert 2 == len(references)
        assert references[0].title == "Book Title"

    def test_delete_removes_existing_reference(self):
        reference = Reference(name="REF_NAME_1", type="book")
        db.session.add(reference)
        db.session.commit()

        reference_controller.delete_by_id(1)
        assert 0 == len(reference_controller.get_all())

    def test_delete_removes_child_fields(self):
        reference = Reference(name="REF_NAME_1", type="book")
        reference.fields.append(Field(name="year", content="2000"))
        reference.fields.append(Field(name="title", content="Book Title"))
        reference.fields.append(Field(name="author", content="Book Author"))
        db.session.add(reference)
        db.session.commit()

        reference_controller.delete_by_id(1)
        assert 0 == len(db.session.execute(select(Field)).all())
