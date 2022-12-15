from app.models.field import Field
from app.models.reference import Reference
from app.services import export_service
from utils import UnitTest


class TestExportService(UnitTest):
    def create_book_reference(self):
        reference = Reference(name="Reference1", type="book")
        reference.fields.append(Field(name="author", content="Author"))
        reference.fields.append(Field(name="title", content="Title"))
        reference.fields.append(Field(name="year", content="2000"))
        reference.fields.append(Field(name="publisher", content="Publisher"))
        return (reference,)

    def create_article_reference(self):
        reference = Reference(name="Test_article", type="article")
        reference.fields.append(Field(name="author", content="Author"))
        reference.fields.append(Field(name="title", content="Title"))
        reference.fields.append(Field(name="year", content="2000"))
        reference.fields.append(Field(name="publisher", content="Publisher"))
        return (reference,)

    def test_book_is_exported_correctly(self):
        references = self.create_book_reference()
        f = export_service.export_as_bibtex([references])
        content = f.read()
        assert bytes.decode(content) == "@book{Reference1,\n\
\tauthor = {Author},\n\ttitle = {Title},\n\tyear = {2000},\n\
\tpublisher = {Publisher},\n}\n\n"

    def test_article_is_exported_correctly(self):
        references = self.create_article_reference()
        f = export_service.export_as_bibtex([references])
        content = f.read()
        assert bytes.decode(
            content) == "@article{Test_article,\n\tauthor = {Author},\n\
\ttitle = {Title},\n\tyear = {2000},\n\tpublisher = {Publisher},\n}\n\n"

    def test_empty_file_is_returned_if_no_references(self):
        f = export_service.export_as_bibtex([])
        content = f.read()
        assert len(content) == 0
