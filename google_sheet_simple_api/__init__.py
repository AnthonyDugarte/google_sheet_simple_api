from googleapiclient.discovery import build
from google.auth.credentials import Credentials

# Docs by API
## https://github.com/googleapis/google-api-python-client/blob/master/docs/README.md


class Sheet:
    """
    Simple google sheet API communication class for python based on official google api

    Complete Sheet v4 docs:
        http://googleapis.github.io/google-api-python-client/docs/dyn/sheets_v4.html

    """

    def __init__(self, spreadsheet_id: str, credentials: Credentials):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_service = build(
            'sheets',
            'v4',
            credentials=credentials,
        )

        self.sheet = self.sheet_service.spreadsheets()

    def append(self, values, sheet_range: str):
        return self.sheet.values().append(
            spreadsheetId=self.spreadsheet_id,
            range=sheet_range,
            body={'values': values},
            valueInputOption="USER_ENTERED",
        ).execute()

    def update(self, values, sheet_range: str):
        return self.sheet.values().update(
            spreadsheetId=self.spreadsheet_id,
            range=sheet_range,
            body={'values': values},
            valueInputOption="USER_ENTERED",
        ).execute()

    def get(self, sheet_range: str):
        return self.sheet.values().get(
            spreadsheetId=self.spreadsheet_id,
            range=sheet_range,
        ).execute()
