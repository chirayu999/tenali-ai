# tenali-ai

## Installation

Clone the repository and install the requirements:

```pip install requirements.txt```

## Secret Keys

Create a project on GCP and generate a OAuth 2.0 key. Download the key as a JSON file and save it as `credentials.json` in the root directory of the project.

## Running the app

Make sure you are in the root directory of the project.

```cd textExtractor```

Run the app using the following command:

```python3 manage.py runserver```

## Testing the app

Open the following URL in POSTMAN:

```http://127.0.0.1:8000/```

There are total 3 endpoints:

1. Extract plain text from the webpage

```http://127.0.0.1:8000/extract?url=<TARGET_URL>```

2. Extract clean text after applying several data cleaning algorithms

```http://127.0.0.1:8000/nltk?url=<TARGET_URL>```

3. Summarize the clean text with OPEN AI

```http://127.0.0.1:8000/openai?url=<TARGET_URL>```

## Current Limitations

The app downloads text files locally due to some problems in google docs api key. The aim is to directly put the content on google docs and return the link to the user.

