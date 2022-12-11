from app import db
from app.models.reference import Reference
from app.models.field import Field
from sqlalchemy import select, delete


def get_by_id(id_):
    return db.session.execute(
        select(Reference).where(Reference.id == id_)
    ).scalar_one()


def get_all():
    return db.session.execute(select(Reference)).all()


def get_titles():
    return db.session.query(Reference.id, Reference.name, Field.content.label(
        "title")).select_from(Reference).join(Field).filter(
            Field.name == "title").all()


def create(name, type_, fields={}):
    if len(name) == 0:
        raise ValueError("Name is invalid")
    if len(type) == 0:
        raise ValueError("Type is unknown")

    reference = Reference(name=name, type=type_)

    for ref_name, content in fields.items():
        reference.fields.append(Field(name=ref_name, content=content))

    db.session.add(reference)
    db.session.commit()


def delete_by_id(id_):
    db.session.execute(delete(Reference).where(Reference.id == id_))
    db.session.commit()
