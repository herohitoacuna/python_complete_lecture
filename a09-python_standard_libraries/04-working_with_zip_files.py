# *************** WORKING WITH FILES ************

from pathlib import Path
from zipfile import ZipFile

# # scenario: We want all files in ecommerce directory in our zip file
# # this code can failed, so we need to put in a try block

# zip = ZipFile("files.zip", "w")
# for path in Path("ecommerce").rglob("*.*"):
#     zip.write(path)
# zip.close()

# ANOTHER WAY TO DO THIS IF WE DONT WANT TO MAKE TRY BLOCK
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)
# result = -- created a zip file


# returns path of all files in zip file.
with ZipFile("files.zip") as zip:
    print(zip.namelist())
# result = ['ecommerce/2-example_file.py', 'ecommerce/__init__.py']
    info = zip.getinfo("ecommerce/2-example_file.py")
    print(info.file_size)       # 0
    print(info.compress_size)   # 0

    # use to extract all files in zip into anoher directory
    zip.extractall("extract")   # -- created new directory called "extract"
