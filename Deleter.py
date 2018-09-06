from Directory import Directory
from File import File
from datetime import datetime
import os.path


class Deleter:
    def __init__(self, path, extensions, lm_str):
        self.path = path
        self.extensions = extensions
        self.lm_str = lm_str

    def check_last_modified(self, file):
        custom_lm = get_datetime(self.lm_str)
        return file.last_modified() < custom_lm

    def check_file_type(self, file):
        if not self.extensions:
            return True
        elif file.file_extension in self.extensions:
            return True
        return False

    def run_deleter(self):
        removed = []
        directory = Directory(self.path)
        for item in directory.items():
            file = File(item)
            if self.check_last_modified(file) and self.check_file_type(file):
                print("Deleting Files...")
                removed.append(file.filename)
                file.remove()
        print("Cleanup Finished!")
        print("Files Removed:")
        for file in removed:
            print(file)


def get_datetime(datetime_string):
    datetime_object = datetime.strptime(datetime_string, '%b %d %Y %I:%M%p')
    return datetime_object