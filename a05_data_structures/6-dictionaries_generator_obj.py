# used in GENERATOR EXPRESSION to get the size of the object
from sys import getsizeof

# ************************* DICTIONARIES ********************
point = {"x": 1, "y": 2}
# list()
# tuple()
# set()
# dict()
point = dict(x=1, y=2)
print(point["x"])           # 1, accessing the value of dictionary
point["x"] = 10             # {"x":10, "y":2}
point["z"] = 20             # {"x":10, "y":2, "z":20}
print(point)

# error, because there is no value of a in dictionary
# print(point["a"])

if "a" in point:
    print(point["a"])

# using get method if value of "a" is
#       not on dictionaries it will get "None",
#       but we can make a default using 2nd argument
print(point.get("a", 0))

del point["x"]              # {'y': 2, 'z': 20}
print(point)

# Iterating over dictionary
for key in point:
    print(key, point[key])

for key, value in point.items():    # items() -> will return the tuple value of dictionary
    print(key, value)
# result:
# y 2
# z 20


# ********************* DICTIONARY COMPREHENSIONS *******************
values = []
for x in range(5):
    values.append(x * 2)

# SYNTAX: comprehension
# [expression for item in items]
list_values = [x * 2 for x in range(5)]     # comprehension for list
print(list_values)                          # [0, 2, 4, 6, 8]

set_values = {x * 2 for x in range(5)}      # comprehension for set
print(set_values)                           # [0, 2, 4, 6, 8]

dict_values = {x: x * 2 for x in range(5)}  # comprehension for dictionaries
print(dict_values)                          # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

tuple_values = (x * 2 for x in range(5))
print(tuple_values)                         # generator object


# *********************** GENERATOR OBJECT *******************
# Generator Objects are iterable
# Use for a large number of data
# cannot get a total number of data because its not store in memory unlike in list

values = (x * 2 for x in range(100000))     # generator object
print("gen:", getsizeof(values))            # gen: 104
# print(len(values))                          # will get an error

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))           # list: 800984


# ************************** UNPACKING OPERATOR **************************
numbers = [1, 2, 3]
print(*numbers)                             # 1 2 3

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)       # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)       # [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']

# UNPACK DICTIONARIES ***
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)  # {'x': 10, 'y': 2, 'z': 1}
