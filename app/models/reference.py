from app.app import db


class Reference(db.Model):
    id = db.Column(db.Interer, autoincrement=True, unique=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    field = db.relationship("Field")
