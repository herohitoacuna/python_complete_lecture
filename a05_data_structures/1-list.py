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
