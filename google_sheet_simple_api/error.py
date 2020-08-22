import contextlib
from googleapiclient.errors import HttpError
import json
import re


@contextlib.contextmanager
def rescueRepeatedSheetTitle(title: str, silent: bool):
    try:
        yield
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

            if silent:
                return False
        return True
