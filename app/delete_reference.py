from app.app import db

def delete(id):
    try:
        sql = "DELETE FROM reference_entries WHERE id=:id"
        db.session.execute(sql, {"id": id})
        db.session.commit()
    except:
        return False
    return True

