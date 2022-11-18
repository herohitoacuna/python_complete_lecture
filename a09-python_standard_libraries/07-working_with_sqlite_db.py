# ***************** WORKING WITH SQLITE DATABASE ************

import sqlite3
import json
from pathlib import Path

# SAVE JSON file into database

# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# syntax: connect("database_file"), if file doesn't exist it will create it for us
# need to close so use "with statement"

# with sqlite3.connect("db.sqlite3") as connection:
#     # ? = placeholder to the values we'll supply in the future
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()
# it will throw an error, because we need to create a table in database first

# In google search for "https://sqlitebrowser.org/"
# download and install SQLite
# create a table in Db Browser with column id, title, year


# READ DATA from database
with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    # result:
    #   (1, 'Terminator', 1989)
    #   (2, 'Kindergarten', 1993)
    movies = cursor.fetchall()      # to run this  we need to comment the for loop
    print(movies)
    # result: [(1, 'Terminator', 1989), (2, 'Kindergarten', 1993)]
