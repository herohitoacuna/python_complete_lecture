# ******************* LIST ***************
# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 3
# combined = zeros + letters
# numbers = list(range(10))
# chars = list("Hello")
# print(combined)
# print(numbers)
# print(chars)
# print(len(chars))


# **************** ACCESSING ITEMS ******************
letters = ["a", "b", "c", "d"]
letters[0] = "A"             # changing the first element of an list
print(letters)               # -1 index access the last index of list
# print the 1st element of array into the 3rd element(not an index)
print(letters[0:3])
print(letters[0:])           # return the original list
print(letters[:])            # return the original list

# slicing the list, return every 2nd of the list, [the initial index::sequence(example, every 2nd of the list)]
print(letters[::2])         # return ["A", "c"]
print(letters[1::2])        # return ["b", "d"]


numbers = list(range(20))
print(numbers[::2])         # return every even number in range(20)
print(numbers[::-1])        # return original list in reverse order


# ****************** LIST UNPACKING ********************
# get individual items on a list and assign them in different variables
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, second, *other = numbers
print(first)                    # return  1
print(other)                    # return [3, 4, 4, 4, 4, 9]

first, *other, last = numbers
print(first, last)              # return  1 9
print(other)                    # return [2, 3, 4, 4, 4, 4]

# first, second, third = numbers      # just like array destructuring


# ***************** LOOPING OVER LISTS *******************
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
# result
# a
# b
# c
print("-------")


for letter in enumerate(letters):
    print(letter)
# result = tuple
# (0, 'a')
# (1, 'b')
# (2, 'c')
print("-------")

for letter in enumerate(letters):
    print(letter[0], letter[1])
# result
# 0 a
# 1 b
# 2 c
print("-------")

items = (1, 2, 3)                   # tuple
first, second, third = items        # tuple unpacking

for index, letter in enumerate(letters):
    print(index, letter)
# result
# 0 a
# 1 b
# 2 c
print("-------")


# ****************** ADDING OR REMOVING ITEMS ******************
letters = ["a", "b", "c"]

# Addd
letters.append("d")         # added to the end of the list
letters.insert(0, "-")      # insert(index, to be insert in the list)
print(letters)

# Remove
letters.pop()               # removing the last element in the list
# removing the element with the same index in the argument
letters.pop(0)
letters.remove("b")          # remove the first occurance in the list
del letters[0:3]            # we can delete multiple element on the list
letters.clear()             # remove all the objects on the list
print(letters)


# ******************* FINDING ITEMS IN LISTS *****************
letters = ["a", "b", "c"]

# return 1, index() return the index of the given item on the list
# if the item is not on the list, error
print(letters.index("b"))
# Do this instead to check if there is an item that match to what we are looking
if "d" in letters:
    print(letters.index("d"))


print(letters.count("d"))       # return 0, because "d" is not on the list


# *************************** SORTING LISTS **************************
numbers = [3, 51, 2, 8, 6]
# numbers.sort()                # return [2, 3, 6, 8, 51], ASCENDING ORDER
numbers.sort(reverse=True)
# return [51, 8, 6, 3, 2], DESCENDING ORDER

# sorted(numbers), does not modify our original numbers list
print(sorted(numbers))
# print(sorted(numbers, reverse=True))  # return in DESCENDING ORDER
print(numbers)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# Python does not know how to sort a list of tuples


# def sort_item(item):
#     return item[1]


# we can get the key in every items and name it as an "item" and sort it base on the 1 index of tuple
# specifying a "key" function that transforms each element before comparison
# items.sort(key=sort_item)
# print(items)


# ********************* LAMBDA FUNCTIONS ****************************
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# items.sort(key=lambda parameters:expression)
items.sort(key=lambda item: item[1])
print(items)
# result = [('Product2', 9), ('Product1', 10), ('Product3', 12)]


# ***************************** MAP FUNCTION **********************
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# transform items list into a new list of prices
# prices = []
# for item in items:
#     prices.append(item[1])

# map(fun, iterables)
x = list(map(lambda item: item[1], items))       # return a new iterable
print(x)


# ******************** FILTER FUNCTION *********************
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
x = list(filter(lambda item: item[1] >= 10, items))
print(x)


# ******************* LIST COMPREHENSIONS *************************
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = list(map(lambda item: item[1], items))
# [expression for item in items]
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
# print(prices)
# print(filtered)


# **************** ZIP FUNCTION *******************
# combining multiple list and make a new list of tuple
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# result must be [(1, 10), (2, 20), (3, 30)]
# syntax : zip(iterable1, iterable2, iterable3)
print(list(zip(list1, list2)))
