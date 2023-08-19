from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import googleapiclient.errors


def create_google_doc(title, content):

    creds = Credentials.from_authorized_user_file('path_to_credential.json', [
                                                  'https://www.googleapis.com/auth/documents'])
    service = build('docs', 'v1', credentials=creds)

    document = {
        'title': title
    }
    try:
        document = service.documents().create().execute()
        doc_id = document['documentId']

        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1
                    },
                    'text': content
                }
            }
        ]
        result = service.documents().batchUpdate(
            documentId=doc_id, body={'requests': requests}).execute()

        return f'https://docs.google.com/document/d/{doc_id}'
    except googleapiclient.errors.HttpError as e:
        return None
