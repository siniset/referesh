from app.app import db

def get_all():

    sql = """SELECT * FROM fields WHERE name='author' OR name='title'"""
    result = db.session.execute(sql)

    return list(result.fetchall())