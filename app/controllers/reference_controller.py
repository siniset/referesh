from app.app import db
from app.models.reference import Reference
from app.models.field import Field


def get_all():
    return db.session.execute(db.session.query(Reference)).all()
