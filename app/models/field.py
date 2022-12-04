from app.app import db


class Field(db.Model):
    id = db.Column(db.Interer, autoincrement=True, unique=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    reference_id = db.Column(db.Integer, db.ForeignKey("reference.id", ondelete="CASCDE"), nullable=False)
