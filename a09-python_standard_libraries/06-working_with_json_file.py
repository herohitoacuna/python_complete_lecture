# **************** WORKING WITH JSON FILES *************
# JSON = JavaScript Object Notation, use to format our data to readable

import json
from pathlib import Path


# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarten", "year": 1993},
# ]

# # dumps() method, use to convert python Obj to JSON String
# data = json.dumps(movies)

# print(type(data))               # String
# print(type(movies))             # list

# # create a file called "movies.json" and write the JSON data into the file
# Path("movies.json").write_text(data)
# # result = -- created movies.json file with movies JSON data with it


# READ A JSON FILE
data = Path("movies.json").read_text()
movies = json.loads(data)

print(movies)                       # movies.json in a LIST data type
#result = [{'id': 1, 'title': 'Terminator', 'year': 1989}, {'id': 2, 'title': 'Kindergarten', 'year': 1993}]

print(type(movies))                 # list
