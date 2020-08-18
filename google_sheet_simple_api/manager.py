import json
import re
from googleapiclient.errors import HttpError
from google_sheet_simple_api.error import RepeatedSheetTitle


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
        try:
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
        except HttpError as err:
            error_data = json.loads(err.content.decode())

            if(isinstance(error_data, dict)):
                error = error_data["error"]
            elif isinstance(error_data, list) and len(error_data) > 0:
                error = error_data[0]["error"]

            if error and \
                    error['status'] == 'INVALID_ARGUMENT' and \
                    bool(
                        re.search(
                            "A sheet with the name \"%s\" already exists" % title,
                            error['message']
                        )
                    ):

                if silent_repetition:
                    return False
                else:
                    raise RepeatedSheetTitle(error['message'])

            raise
