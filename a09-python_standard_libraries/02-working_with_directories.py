# ******************* WORKING WITH DIRECTORIES *****************88
# directory = is a folder
from pathlib import Path


path = Path("ecommerce")
# path.exists()                 # check if directory is exist
# path.mkdir()                  # create this directory
# path.rmdir()                  # remove directory
# path.rename("ecommerce2")     # renaming directory


# iterdir() method , we can get list of files in this directory
# print(path.iterdir())
# result = <generator object Path.iterdir at 0x0000021A87701E00>
# generator object returns a new value every time we iterate it

for p in path.iterdir():
    print(p)
# result = ecommerce\2-example_file.py
#          ecommerce\2-example_folder


# creating list for iterable object
paths = [p for p in path.iterdir()]
print(paths)
# result = [WindowsPath('ecommerce/2-example_file.py'), WindowsPath('ecommerce/2-example_folder')]


# filtering a list of paths returns only a directory
# limitation: We cannot search by pattern and recursively
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
# result = [WindowsPath('ecommerce/2-example_folder')]


# glob() method to search by pattern
py_files = [p for p in path.glob("*.py")]
print(py_files)
# result = [WindowsPath('ecommerce/2-example_file.py')]


# rglob() method to search recursively
# py_files = [p for p in path.glob("**/*.py")]
py_files = [p for p in path.rglob("*.py")]
print(py_files)
# result = [WindowsPath('ecommerce/2-example_file.py')]
