import datetime
from pytest import raises, fixture
from sqlalchemy import select

from app import db
from app.controllers import reference_controller
from app.controllers import project_controller
from app.models.field import Field
from app.models.reference import Reference


def append_fields(reference, fields):
    for field in fields:
        reference.fields.append(field)


def insert_reference(name, type, created_at=None):
    reference = Reference(
        name=name,
        type=type,
        created_at=created_at,
        project_id=1)
    db.get_session().add(reference)
    return reference


def get_references():
    return db.get_session().execute(select(Reference)).all()


class TestReferenceController:
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

    def test_create_adds_reference_with_valid_values(self):
        reference_controller.create("BOOKNAME", "book")
        reference_controller.create("ARTNAME", "article")
        assert 2 == len(get_references())

    def test_create_fails_with_invalid_name(self):
        with raises(ValueError) as err:
            reference_controller.create("", "book")

        assert str(err.value) == "Name is invalid"
        assert 0 == len(get_references())

    def test_create_fails_with_invalid_type(self):
        with raises(ValueError) as err:
            reference_controller.create("ref", "")

        assert str(err.value) == "Type is unknown"
        assert 0 == len(get_references())

    def test_get_by_id_returns_correct_reference(self):
        self.session.add_all([
            Reference(name="REF_NAME_1", type="book", project_id=1),
            Reference(name="REF_NAME_2", type="book", project_id=1),
            Reference(name="REF_NAME_3", type="book", project_id=1)
        ])
        self.session.commit()

        assert "REF_NAME_2" == reference_controller.get_by_id(2).name

    def test_references_are_ordered_by_most_recent_first(self):
        now = datetime.datetime.now()

        append_fields(
            insert_reference("non-empty-1", "book", now),
            [
                Field(name="year", content="2000"),
                Field(name="title", content="Book Title"),
                Field(name="author", content="Book Author")
            ]
        )

        append_fields(
            insert_reference("non-empty-2", "book",
                             now + datetime.timedelta(0, 1)),
            [
                Field(name="year", content="1000"),
                Field(name="title", content="Book Title 2"),
                Field(name="author", content="Book Author 2"),
            ]
        )

        insert_reference(name="jdsk", type="book", created_at=now)
        insert_reference(name="REF_NAME_2", type="article",
                         created_at=now + datetime.timedelta(0, 1))
        insert_reference(name="REF_aaaNAME_3", type="book",
                         created_at=now + datetime.timedelta(0, 5))

        self.session.commit()

        assert 5 == reference_controller.get_all()[0].id
        assert 2 == reference_controller.get_titles()[0].id

    def test_get_titles_return_correct_format(self):
        append_fields(insert_reference("REF_NAME_1", "book"), [
            Field(name="year", content="2000"),
            Field(name="title", content="Book Title"),
            Field(name="author", content="Book Author")
        ])

        append_fields(insert_reference("REF_NAME_2", "book"), [
            Field(name="year", content="1000"),
            Field(name="title", content="Book Title 2"),
            Field(name="author", content="Book Author 2")
        ])

        self.session.commit()
        references = reference_controller.get_titles()

        assert 2 == len(references)
        assert "Book Title" == references[0].title

    def test_delete_removes_existing_reference(self):
        insert_reference("ref_name_1", "book")
        self.session.commit()

        reference_controller.delete_by_id(1)
        assert 0 == len(reference_controller.get_all())

    def test_delete_removes_associated_fields(self):
        append_fields(insert_reference("REF_NAME_1", "book"), [
            Field(name="year", content="2000"),
            Field(name="title", content="Book Title"),
            Field(name="author", content="Book Author")
        ])

        self.session.commit()
        reference_controller.delete_by_id(1)

        assert 0 == len(get_references())
