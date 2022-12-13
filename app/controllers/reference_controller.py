import logging
from app import db
from app.models.reference import Reference
from app.models.field import Field
from sqlalchemy import select, delete


def get_by_id(id):
    return db.session.execute(
        select(Reference).where(Reference.id == id)
    ).scalar_one()


def get_all():
    return db.session.execute(select(Reference)).all()


def get_titles():
    return db.session.query(Reference.id, Reference.name, Field.content.label(
        "title")).select_from(Reference).join(Field).filter(
            Field.name == "title").all()


def create(name, type, fields={}):
    if len(name) == 0:
        raise ValueError("Name is invalid")
    if len(type) == 0:
        raise ValueError("Type is unknown")

    reference = Reference(name=name, type=type)

    for name, content in fields.items():
        reference.fields.append(Field(name=name, content=content))

    db.session.add(reference)
    db.session.commit()


def edit(id, name, type_, fields={}):


    db.session.query(Reference).filter(id == Reference.id).update({'name': name})

    for field_name, field_content in fields.items():
        db.session.query(Field)
            .filter(Field.reference_id == id)
            .filter(Field.name == field_name).update({"content": field_content})
    db.session.commit()


def delete_by_id(id):
    db.session.execute(delete(Reference).where(Reference.id == id))
    db.session.commit()