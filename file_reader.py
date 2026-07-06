from docx import Document
from PyPDF2 import PdfReader

def read_docx(file):

    doc=Document(file)

    text=[]

    for p in doc.paragraphs:
        if p.text.strip():
            text.append(
                p.text
            )

    return "\n".join(text)


def read_pdf(file):

    reader=PdfReader(file)

    text=[]

    for page in reader.pages:

        try:
            page_text=page.extract_text()

            if page_text:
                text.append(
                    page_text
                )

        except:
            pass

    return "\n".join(text)