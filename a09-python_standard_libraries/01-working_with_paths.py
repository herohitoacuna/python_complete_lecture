# ************ WORKING WITH PATHS **************
from pathlib import Path

# Path("C:\\Path Files\\Microsoft")   # windows
# Path(r"C:\Path Files\Microsoft")    # simplify
# Path("/usr/local/bin")              # mac

# Path()                              # Referencing to the current folder

# relative path --> sub folder in our current folder
# Path("ecommerce/__init__.py")
# Path() / Path("ecommerce")          # combine path using " / "
# Path() / "ecommerce" / "__init__.py"    # combine path with string using " / "
# Path.home()                         # path of the current user

# CREATING A PATH OBJECT **************
path = Path("ecommerce/__init__.py")
print(path.exists())                    # False
print(path.is_file())                   # False
print(path.is_dir())                    # False
print(path.name)                        # __init__ .py, filename
print(path.stem)                        # __init__ , filename w/o extension
print(path.suffix)                      # .py , extension
print(path.parent)                      # ecommerce , parent of this path

# ecommerce\file.txt , it create another path in the parent
path = path.with_name("file.txt")
print(path)

# D:\PYTHON Lecture\ecommerce\file.txt , this get where the file is located in our computer
print(path.absolute())

# ecommerce\file.txt , it change the suffix of file
path = path.with_suffix(".txt")
print(path)
