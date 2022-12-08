from io import BytesIO

def export_as_bibtex(references):
    bibtex_file = BytesIO()
    reference_objects = list(map(lambda r: r[0], references))
    bibtex_content = list(map(bibtexify_reference,reference_objects))
    for i in bibtex_content:
        bibtex_file.write(bytes(i,'utf-8'))
    bibtex_file.seek(0)
    return bibtex_file

def bibtexify_reference(reference):
    bibtex = f"@{reference.type}"+"{"+f"{reference.name},"+"\n"
    for field in reference.fields:
        bibtex += "\t"+f"{field.name} = "+"{"+f"{field.content}"+"},\n"
    bibtex += "}\n\n"
    return bibtex
