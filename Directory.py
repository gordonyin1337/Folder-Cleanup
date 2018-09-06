import os, os.path
from File import File


class Directory:
    def __init__(self, path):
        self.path = path

    def __len__(self):
        return len(os.listdir(self.path))

    def items(self):
        files = []
        for item in os.listdir(self.path):
            path = os.path.join(self.path, item)
            if not os.path.isdir(path):
                files.append(path)
        return files
