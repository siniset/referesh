from pytest import raises, fixture
from sqlalchemy import select

from app import db
from app.controllers import project_controller
from app.models.project import Project


def get_projects():
    return db.get_session().execute(select(Project)).all()


class TestProjectController:
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

    def test_create_project_with_valid_name(self):
        project_controller.create_project("Project-1")

        assert 2 == len(get_projects())

    def test_create_project_with_invalid_name(self):
        with raises(ValueError) as err:
            project_controller.create_project("")

        assert str(err.value) == "Name is invalid"
        assert 1 == len(get_projects())
