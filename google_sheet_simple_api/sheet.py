from googleapiclient.discovery import build
from google.auth.credentials import Credentials


def sheet_builder(credentials: Credentials):
    sheet_service = build(
        'sheets',
        'v4',
        credentials=credentials,
    )

    return sheet_service.spreadsheets()
