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
