from readability.readability import Document
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')


def extract_text_with_nltk(text):

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered_words = [
        word for word in words if word.lower() not in stop_words]

    processed_text = " ".join(filtered_words)

    doc = Document(processed_text)
    extracted_text = doc.summary()

    return extracted_text
