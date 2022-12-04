from sqlalchemy import func
from app.app import db


class Reference(db.Model):
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    field = db.relationship("Field")
