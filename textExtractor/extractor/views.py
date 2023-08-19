from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .extract_text_with_nltk import extract_text_with_nltk
from .text_to_document import create_google_doc


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def extract_text(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            extracted_text = soup.get_text()

            with open('text_document.txt', 'w') as file:
                file.write(extracted_text)

            return HttpResponse('Text extracted and saved successfully.')

        return HttpResponse('Error: Could not fetch the URL.')

    return HttpResponse('Invalid request method.')


def nltk(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            extracted_text = extract_text_with_nltk(text)

            # google_doc_url = create_google_doc('Extracted Text', extracted_text)

            if extracted_text:
                return HttpResponse(extracted_text)

            return HttpResponse('Error: Could not extract text.')


    return HttpResponse('Error: Could not fetch the URL.')
