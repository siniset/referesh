from database import db

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Text, nullable=False)
    book_name = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.Text, nullable=False)
    
