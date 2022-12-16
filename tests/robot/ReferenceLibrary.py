from DatabaseLibrary import DatabaseLibrary
from app.models.reference import Reference
from app.models.field import Field
from sqlalchemy import delete, select


class ReferenceLibrary():
    def __init__(self, db=DatabaseLibrary()):
        self.db = db

    def get_by_id(self, id):
        return self.db.session.execute(
            select(Reference).where(Reference.id == id)
        ).scalar_one()

    def get_all(self):
        return self.db.session.execute(select(Reference)).all()

    def get_titles(self):
        return self.db.session.query(
            Reference.id, Reference.name,
            Field.content.label("title")).select_from(Reference).join(
            Field).filter(Field.name == "title").all()

    def create(self, name, type, fields={}, project_id=1):
        if len(name) == 0:
            raise ValueError("Name is invalid")
        if len(type) == 0:
            raise ValueError("Type is unknown")

        reference = Reference(name=name, type=type, project_id=project_id)

        for name, content in fields.items():
            reference.fields.append(Field(name=name, content=content))

        self.db.session.add(reference)
        self.db.session.commit()

    def delete_by_id(self, id):
        self.db.session.execute(delete(Reference).where(Reference.id == id))
        self.db.session.commit()

    # helper functions for robotframework

    def get_newest_id(self):
        return self.get_titles()[0][0]

    def save_fields(self, author, title, year, publisher):
        return {'author': author, 'title': title,
                'year': year, 'publisher': publisher}

    def form_fields(self, reference):
        fields = {}
        for field in reference.fields:
            fields[field.name] = field.content

        return fields
