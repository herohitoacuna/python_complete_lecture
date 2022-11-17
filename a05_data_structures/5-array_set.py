# **************************** ARRAYS ****************************
# from array import array
# array(typecode, iterable)
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
