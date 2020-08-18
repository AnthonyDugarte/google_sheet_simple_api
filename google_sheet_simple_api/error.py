class Error(Exception):
    """Base class for google sheet simple api errors."""
    pass

class RepeatedSheetTitle(Error):
    def __init__(self, message):
        self.message = message
