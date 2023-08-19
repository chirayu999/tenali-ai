from readability.readability import Document


def extract_text_with_nltk(text):

    doc = Document(text)
    extracted_text = doc.summary()

    return extracted_text
