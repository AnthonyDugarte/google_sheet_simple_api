import json
import re
from googleapiclient.errors import HttpError
from google_sheet_simple_api.error import rescueRepeatedSheetTitle


class SheetsManager():
    def __init__(self, spreadsheet_id: str, sheet):
        self.spreadsheet_id = spreadsheet_id
        self.sheet = sheet

    def create(self, title: str, silent_repetition: bool = True) -> bool:
        """Create a sheet tab with the given title.

        Returns if tab was created.

        Args:
          title: New Tab's Title.
          silent_repetition: Indicates if an attempt to recreate a tab should be treated as a successful one and an exception should not be raised. Defaults to True.
        """

        # NOTEEEEEE TO THE FUTURE ME:
        # If functionalities that may cause multiple errors to ocurre are added,
        # the handling of them must be considered

        with rescueRepeatedSheetTitle(title=title, silent=silent_repetition):
            self.sheet.batchUpdate(
                spreadsheetId=self.spreadsheet_id,
                body={
                    "requests": [
                        {
                            "addSheet": {
                                "properties": {
                                    "title": title,
                                },
                            },
                        },
                    ],
                },
            ).execute()
            return True
        return False

    def duplicate(self, new_title: str, source_sheet_id: int, silent_repetition: bool = True) -> bool:
        """Create a sheet tab with the given title based on another sheet.

        Returns if sheet tab was created.

        Args:
            new_title: New Tab's Title.
            source_sheet_id: New tab's base sheet.
            silent_repetition: Indicates if an attempt to recreate a tab should be treated as a successful one and an exception should not be raised. Defaults to True.
        """
        with rescueRepeatedSheetTitle(title=new_title, silent=silent_repetition):
            self.sheet.batchUpdate(
                spreadsheetId=self.spreadsheet_id,
                body={
                    "requests": [
                        {
                            "duplicateSheet": {
                                "newSheetName": new_title,
                                "sourceSheetId": source_sheet_id,
                            },
                        },
                    ],
                },
            ).execute()

            return True
        return False
