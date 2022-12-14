from app import db
from app.models.project import Project
from sqlalchemy import select, delete


def create_default_project():
    if not db.session.execute(select(Project)).all():
        project = Project(name="default")

        db.session.add(project)
        db.session.commit()


def get_by_id(id):
    return db.session.execute(
        select(Project).where(Project.id == id)
    ).scalar_one()


def get_all():
    return db.session.execute(select(Project)).all()


def create_project(name):
    if len(name) == 0:
        raise ValueError("Name is invalid")

    project = Project(name=name)

    db.session.add(project)
    db.session.commit()


def delete_by_id(id):
    db.session.execute(delete(Project).where(Project.id == id))
    db.session.commit()