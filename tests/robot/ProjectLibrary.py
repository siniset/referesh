from tests.robot.DatabaseLibrary import DatabaseLibrary
from app.models.project import Project
from sqlalchemy import delete, select


class ProjectLibrary():
    def __init__(self, db=DatabaseLibrary()):
        self.db = db

    def create_default_project(self):
        if not self.get_all():
            project = Project(name="default")

            self.db.session.add(project)
            self.db.session.commit()


    def get_by_id(self, id):
        return self.db.session.execute(
            select(Project).where(Project.id == id)
        ).scalar_one()


    def get_all(self):
        return self.db.session.execute(select(Project)).all()


    def create_project(self, name):
        if len(name) == 0:
            raise ValueError("Name is invalid")

        project = Project(name=name)

        self.db.session.add(project)
        self.db.session.commit()


    def delete_by_id(self, id):
        self.db.session.execute(delete(Project).where(Project.id == id))
        self.db.session.commit()
