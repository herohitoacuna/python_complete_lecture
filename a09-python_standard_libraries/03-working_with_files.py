# *************** WORKING WITH FILES ************

from pathlib import Path    # to create a Path object
from time import ctime      # to format the st_ctime in stat() method
import shutil               # use to copy and moving files

# path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()                           # delete a file

# print(path.stat())      # returns the information of the file
# result:
#   os.stat_result
#       (st_mode=33206,
#       st_ino=6192449488038460,
#       st_dev=983966191, st_nlink=1,
#       st_uid=0, st_gid=0,
#       st_size=0,                          # size of the files in byte
#       st_atime=1668759775,                # last access time
#       st_mtime=1668759775,                # last modified time
#       st_ctime=1668759761)                # created time

# print(ctime(path.stat().st_ctime))  # Fri Nov 18 16:22:41 2022

# FROM STACKOVERFLOW **************

# from datetime import datetime, timezone
# ...
# stat_result = path.stat()
# modified = datetime.fromtimestamp(stat_result.st_mtime, tz=timezone.utc)
# print('modified', modified)

# print(path.read_bytes())
# # result = b'print("Ecommerce Initialized")\r\n' , returns a string represent in binary data

# print(path.read_text())         # read the content of file in a String
# print(path.write_text("..."))   # write textual data to a file
# print(path.write_bytes("..."))  # write a binary data in a file

#  **** PATH CLASS IS NOT AN IDEAL WAY TO COPY A FILE ***


# COPYING A FILE *****************
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# UGLY WAY TO COPY A FILE
# target.write_text(source.read_text)

# BETTER WAY TO COPY A FILE
shutil.copy(source, target)     # syntax: shutil.copy(source_copy, final_copy)
