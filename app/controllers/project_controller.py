from app import db
from app.models.project import Project
from sqlalchemy import select, delete


def create_default_project():
    if not get_all():
        project = Project(name="default")

        db.get_session().add(project)
        db.get_session().commit()


def get_by_id(id):
    return db.get_session().execute(
        select(Project).where(Project.id == id)
    ).scalar_one()


def get_all():
    return db.get_session().execute(select(Project)).all()


def create_project(name):
    if len(name) == 0:
        raise ValueError("Name is invalid")

    project = Project(name=name)

    db.get_session().add(project)
    db.get_session().commit()


def delete_by_id(id):
    db.get_session().execute(delete(Project).where(Project.id == id))
    db.get_session().commit()
