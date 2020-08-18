import google.auth
from google.auth.credentials import Credentials

DEFAULT_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def default_google_credentials(scopes=DEFAULT_SCOPES) -> Credentials:
    credentials, project = google.auth.default(scopes=scopes)
    return credentials
