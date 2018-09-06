from Deleter import Deleter

if __name__ == "__main__":
    path = input("Input Directory Path: ")
    extensions = input("Input File Extensions: ")
    datetime = input("Input Date and Time: ")
    deleter = Deleter(path, extensions, datetime)
    deleter.run_deleter()