from app import db
from app.models.reference import Reference
from app.models.field import Field
from sqlalchemy import select, delete


def is_valid_type(type):
    # TODO
    return len(type) > 0


def get_by_id(id):
    return db.get_session().execute(
        select(Reference).where(Reference.id == id)
    ).scalar_one()


def get_all():
    return db.get_session().execute(
        select(Reference)
        .order_by(Reference.created_at.desc())
    ).scalars().all()


def get_titles():
    return (
        db.get_session().execute(
            select(Reference.id, Reference.type, Reference.name, Field.content.label("title"))
            .join(Field, isouter=True)
            .filter(Field.name == "title")
            .order_by(Reference.created_at.desc())
        ).all()
    )


def create(name, type, fields=None):
    if len(name) == 0:
        raise ValueError("Name is invalid")
    if not is_valid_type(type):
        raise ValueError("Type is unknown")

    reference = Reference(name=name, type=type)

    if fields:
        for name, content in fields.items():
            reference.fields.append(Field(name=name, content=content))

    db.get_session().add(reference)
    db.get_session().commit()


def delete_by_id(id):
    db.get_session().execute(delete(Reference).where(Reference.id == id))
    db.get_session().commit()
