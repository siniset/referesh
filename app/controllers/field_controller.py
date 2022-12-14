from app import db
from app.models.field import Field
from sqlalchemy import select, delete


def update(id, content):
    db.session.query(Field).filter(Field.id == id).update({"content": content})
    db.session.commit()


def delete_by_id(id):
    db.session.execute(delete(Field).where(Field.id == id))
    db.session.commit()
