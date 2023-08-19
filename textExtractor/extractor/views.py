from django.http import HttpResponse
import requests
from .extract_text_with_nltk import extract_text_with_nltk
from .text_to_document import create_google_doc
from .clean_text import clean_html_text, clean_text
from .summarize_with_openai import summarize_with_openai


def index(request):
    return HttpResponse("Hello, world")


def extract_text(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        response = requests.get(url)

        if response.status_code == 200:

            text_from_html = clean_html_text(response.text)
            text = clean_text(text_from_html)

            with open('simple_text.txt', 'w') as file:
                file.write(text)

            return HttpResponse('Text extracted and saved successfully.')

        return HttpResponse('Error: Could not fetch the URL.')

    return HttpResponse('Invalid request method.')


def nltk(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        response = requests.get(url)

        if response.status_code == 200:
            text_from_html = clean_html_text(response.text)
            text = clean_text(text_from_html)
            extracted_text = extract_text_with_nltk(text)

            # google_doc_url = create_google_doc('Extracted Text', extracted_text)

            with open('cleaned_text.txt', 'w') as file:
                file.write(extracted_text)


            if extracted_text:
                return HttpResponse(extracted_text)

            return HttpResponse('Error: Could not extract text.')

    return HttpResponse('Error: Could not fetch the URL.')


def openai(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        response = requests.get(url)

        if response.status_code == 200:
            text_from_html = clean_html_text(response.text)
            text = clean_text(text_from_html)
            nltk_text = extract_text_with_nltk(text)
            prompt = "given the following text, don't summarize but make it meaningful by seperating into title and paragraphs"
            summarized_text = summarize_with_openai(prompt, nltk_text)

            with open('summarized_text.txt', 'w') as file:
                file.write(summarized_text)

            if summarized_text:
                return HttpResponse(summarized_text)

            return HttpResponse('Error: Could not extract text.')

    return HttpResponse('Error: Could not fetch the URL.')
