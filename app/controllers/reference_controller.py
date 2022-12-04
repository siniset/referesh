from app.app import db
from app.models.reference import Reference
from app.models.field import Field


def get_all():
    return Reference.query.all()

def get_titles():
    return db.session.query(Reference.name, Field.content.label("title")).select_from(Reference).join(Field).filter(Field.name == "title").all()
