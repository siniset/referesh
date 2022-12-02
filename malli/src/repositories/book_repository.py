from models.book import Book
from app import db


class BookRepository:
    def find_all(self):
        return Book.query.all()

    def create(self, book):
        db.session.add(book)
        db.session.commit()

        return book

    def delete_all(self):
        result = Book.query.delete()
        db.session.commit()

        return result

    def delete_by_id(self, todo_id):
        result = Book.query.filter(Book.id == todo_id).delete()
        db.session.commit()

        return result


book_repository = BookRepository()
