import traceback
import datetime


class EmailAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__()
        self.date = datetime.datetime.now()
        # self.traceback = traceback.format_exc()
        self.traceback = 'EmailAlreadyExistsException'