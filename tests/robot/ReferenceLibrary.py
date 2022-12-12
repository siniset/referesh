from tests.robot.DatabaseLibrary import DatabaseLibrary
from app.models.reference import Reference
from sqlalchemy import delete, select

class ReferenceLibrary():
    def __init__(self, db=DatabaseLibrary()):
        self.db = db

    def get_by_id(self, id):
        return self.db.session.execute(
            select(Reference).where(Reference.id == id)
        ).scalar_one()

    def delete_by_id(self, id):
        self.db.session.execute(delete(Reference).where(Reference.id == id))
        self.db.session.commit()