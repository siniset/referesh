from models.book import Book
from repositories.book_repository import book_repository as default_book_repository


class BookService:
    def __init__(self, book_repository=default_book_repository):
        self._book_repository = book_repository

    def create_book(self, author, book_name, year, publisher):
        return self._book_repository.create(Book(author=author, book_name = book_name, year = year, publisher =publisher))

    def get_all_books(self):
        return self._book_repository.find_all()

    def delete_book(self, book_id):
        return self._book_repository.delete_by_id(book_id)

    def delete_all_books(self):
        return self._book_repository.delete_all()

book_service = BookService()
