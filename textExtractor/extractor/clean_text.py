from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def clean_html_text(html_text):

    soup = BeautifulSoup(html_text, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    clean_text = soup.get_text()

    clean_text = re.sub(r'\s+', ' ', clean_text).strip()

    return clean_text


def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    cleaned_text = ' '.join(words)
    return cleaned_text
