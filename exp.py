'''class file:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print("Exit")
        self.file.close()

with file("file.txt", "w") as f:
    print("middle")
    f.write("yayay")
'''

from contextlib import contextmanager as cm

@cm
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()
    
