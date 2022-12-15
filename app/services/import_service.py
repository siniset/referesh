from pybtex.database import parse_file
from app.controllers.reference_controller import create

def parse_from_bibtex(bib_data):
    bib_dict = bib_data.entries
    references = []
    for reference in bib_dict.values():
        type = reference.type
        author = str(reference.persons['author'][0])
        title = reference.fields['title']
        year = reference.fields['year']
        publisher = reference.fields['publisher']
        name = author.split()[0].strip(',')+year
        field = {author, title, year, publisher}
        reference = [name, type, field]
        references.append(reference)
    return references

def import_bibtex(file):
    bib_data = parse_file(file)
    references = parse_from_bibtex(bib_data)
    for reference in references:
        create(reference[0], reference[1], reference[2])

#import_bibtex('test.bib') # for testing ...
