# used in GENERATOR EXPRESSION to get the size of the object
from sys import getsizeof

# more control on printing stuff
# from pprint import pprint

# ******************** STACKS ****************
# stack = resembles of stack of items in the real world.
# LIFO = last In First Out
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)             # [1, 2, 3]
last = browsing_session.pop()
print(last)                         # 3
print(browsing_session)             # [1, 2]
print("redirect", browsing_session[-1])  # redirect 2

if not browsing_session:           # not = Falsy, if browsing_session is = [] = Falsy, so Falsy and Falsy will result True
    print("disable")


# ******************** QUEUES ****************
# FIFO = First In First Out

# when dealing with a large item, its more efficient to use a "DEQUE" object
# from collections import deque

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")


# ******************* TUPLES ***************************
# tuples:
#   is a basically a read only list. We can use it to contain a sequence
#   of objects but we cannot modify this sequence.

point = 1, 2  # OR (1, 2)
point = (1, 2) + (3, 4)         # (1, 2, 3, 4)
point = (1, 2) * 3              # (1, 2, 1, 2, 1, 2)
point = tuple([1, 3, 5])        # (1, 3, 5)
point = tuple("hello")          # ('h', 'e', 'l', 'l', 'o')
point = tuple(range(1, 4))      # (1, 2, 3)
print(point)

# Accessing tuple
print(point[0:2])               # (1, 2)
# Tuple unpacking
x, y, z = point
if 10 in point:
    print("exist")

# point[0] = 10  # cannot modify a tuple


# ********************* SWAPPING VARIABLES ***********************
x = 10
y = 11

# z = x
# x = y
# y = z

x, y = y, x
x, y = (11, 10)  # unpacking

print("x", x)
print("y", y)


# **************************** ARRAYS ****************************
# from array import array
# array(typecode)
# google "python 3 typecode"

# numbers = array("i", [1, 2, 3])
# numbers[0] = 1.0                    # error, because every item in array should be same type.


# ************************* SETS ***************************
# SET = a collection with no duplicate
# SET does not support INDEX.
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
second = {1, 4}
second.add(5)                   # {1, 4, 5} , add() use only in set function
second.remove(5)                # {1, 4}
print(second)
print(len(second))              # 2


# UNION of two sets
first = set(numbers)
second = {1, 5}

print(first | second)   # {1, 2, 3, 4, 5} -> all numbers but no duplication
print(first & second)   # {1} -> numbers in both set
print(first - second)   # {2, 3, 4} -> difference between 2 set

# {2, 3, 4, 5}-> number with no duplicate in 1st or 2nd set
print(first ^ second)


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


# *************** EXERCISE *********************
# using dictionaries we can count a key value pair of every character in dictionary
# once you count it, transform into a list of tuple so that we can use a sorted() function.
# reverse it into descending order

sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])
