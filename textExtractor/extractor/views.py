from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


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
