from app.app import db


def save_book_fields(author, book_name, year, publisher, id):

    fields = {"author": author, "book_name": book_name,
              "year": year, "publisher": publisher}

    try:
        for key in fields.keys():
            sql = """INSERT INTO fields (name, content, reference_entry)
                VALUES (:name, :content, :id)"""
            db.session.execute(
                sql, {
                    "name": key, "content": fields[key], "id": id})
    except BaseException:
        return False

    return True


def save(type, author=None, book_name=None, year=None,
         publisher=None, reference_name=None):

    try:
        sql = """INSERT INTO reference_entries (name, type, created_at)
             VALUES (:name, :type, NOW()) RETURNING id"""
        id = db.session.execute(
            sql, {"name": reference_name, "type": type}).fetchone()[0]

        if type == "book":
            if not save_book_fields(author, book_name, year, publisher, id):
                raise

        db.session.commit()

    except BaseException:
        return False

    return True
