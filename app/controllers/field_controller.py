from app import db
from app.models.field import Field
from sqlalchemy import delete


def create(name, content, reference_id):
    field = Field(name=name, content=content, reference_id=reference_id)

    db.get_session().add(field)
    db.get_session().commit()


def update(id, content):
    db.get_session().query(Field).filter(
        Field.id == id).update({"content": content})
    db.get_session().commit()


def delete_by_id(id):
    db.get_session().execute(delete(Field).where(Field.id == id))
    db.get_session().commit()


def collect(reference_id):
    result = Field.query.filter_by(reference_id=reference_id).all()

    return list(map(
        lambda row: {
            "id": row.id,
            "name": row.name,
            "content": row.content
        }, result
    ))
