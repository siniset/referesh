from app.app import db
from app.models.reference import Reference
from app.models.field import Field


def get_one(id):
    return Reference.query.get(id)


def get_all():
    return Reference.query.all()


def get_titles():
    return db.session.query(Reference.id, Reference.name, Field.content.label(
        "title")).select_from(Reference).join(Field).filter(
            Field.name == "title").all()


def create(name, type, fields={}):
    reference = Reference(name=name, type=type)

    for name, content in fields.items():
        reference.fields.append(Field(name=name, content=content))

    db.session.add(reference)
    db.session.commit()


def delete_by_id(id):
    db.session.execute(db.delete(Reference).where(Reference.id == id))
    db.session.commit()
