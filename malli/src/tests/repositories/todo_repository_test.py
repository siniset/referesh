import unittest
from repositories.book_repository import book_repository
from models.book import Book


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        book_repository.delete_all()

    def test_create(self):
        book_repository.create(Book(author="Mauri Kunnas", book_name = "Koiramäki", year = 1990, publisher ="Otava"))
        books = book_repository.find_all()    
        
        self.assertEqual(len(books), 1)
        #self.assertEqual(todos[0].content, "learn python") tähän jotain
