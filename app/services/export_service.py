from io import BytesIO
from pybtex.database import parse_file


def export_as_bibtex(references):
    bibtex_file = BytesIO()
    print(references, flush=True)
    reference_objects = references
    bibtex_content = list(map(bibtexify_reference, reference_objects))
    for i in bibtex_content:
        bibtex_file.write(bytes(i, 'utf-8'))
    bibtex_file.seek(0)
    return bibtex_file


def bibtexify_reference(reference):
    print(reference, flush=True)
    bibtex = f"@{reference.type}" + "{" + f"{reference.name}," + "\n"
    for field in reference.fields:
        bibtex += "\t" + f"{field.name} = " + "{" + f"{field.content}" + "},\n"
    bibtex += "}\n\n"
    return bibtex


def parse_from_bibtex(file):
    bib_data = parse_file(file)
    bib_dict = bib_data.entries
    references = []
    for reference in bib_dict.values():
        type = reference.type
        author = str(reference.persons['author'][0])
        title = reference.fields['title']
        year = reference.fields['year']
        publisher = reference.fields['publisher']
        ref_name = author.split()[0].strip(',') + year
        reference = [type, ref_name, author, title, year, publisher]
        references.append(reference)
    return references

# print(parse_from_bibtex('test.bib'))      # for testing
