from database import db
from app import create_app

app = create_app()
app.app_context().push()


def create_tables():
    db.session.execute("""
        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            author TEXT NOT NULL,
            book_name TEXT NOT NULL,
            year INTEGER NOT NULL,
            publisher TEXT NOT NULL
        );
    """)

    db.session.commit()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS books;
    """)

    db.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()
