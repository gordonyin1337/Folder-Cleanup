import os
import os.path
from datetime import datetime


class File:
    def __init__(self, path):
        self.path = path
        self.filename, self.file_extension = os.path.splitext(self.path)

    def __repr__(self):
        return os.path.basename(self.path)

    def get_abs_path(self):
        return os.path.abspath(self.path)

    def remove(self):
        os.remove(self.path)

    def last_modified(self):
        unix_time = int(os.path.getmtime(self.path))
        return datetime.fromtimestamp(unix_time)