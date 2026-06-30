from pypdf import PdfReader


def extract_text_from_pdf(filepath):
    reader = PdfReader(filepath)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text