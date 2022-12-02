import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_todo(self, author, book_name, year, publisher):
       
        data = {
            "author": author,
            "book_name": book_name,
            "year": year,
            "publisher": publisher
        }

        requests.post(f"{self._base_url}/tests/books", json=data)

