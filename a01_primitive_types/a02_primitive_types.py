# Variables & Data Types
students_count = 1000               # interger
rating = 4.99                       # float
is_published = False                # Boolean


# # ******************* STRINGS *****************
course = "Python Programming"
print(len(course))                  # return number of characters

# Accessing the character of string using index--> return first character of string = P
# BRACKER NOTATIOn
print(course[0])
print(course[-1])       # return the last character
print(course[0:3])      # return 0 to the 2nd index
print(course[0:])       # return 0 to last character
print(course[:3])       # return the first 3 character of string
print(course[:])        # return all character in string


# ************** ESCAPE SEQUENCE *******************

# \"    - to use double quote in string
# \'    - to use single qoute in string
# \\    - to use backlash in string
# \n    - to create new line of string

course = "Python \"Programming"     # result = Python "Programming
print(course)


# ************ FORMATTED STRINGS ***************

first = "Mosh"
last = "Hamedani"
full_name = first + " " + last
print(full_name)            # result = Mosh Hamedani

# instead of "+" in concatination, we can use f"" to concat our strings
full = f"{first} {last}"

print(full)                 # result = Mosh Hamedani


# *************** STRING METHODS *************

# len()         --> use to get all characters
course = "python programming"
print(course.upper())       # result = PYTHON PROGRAMMING
print(course)               # result = python programming
print(course.lower())       # result = python programming

# result = Python Programming  --> make every word first letter into capital letter
print(course.title())

# remove space from beginning and in the end of the string
print(course.strip)

# result = 9 --> return the index of characters in string
print(course.find("pro"))

# result = jython jroggraming  --> replace all p with j
print(course.replace("p", "j"))

# result = True --> return Boolean value, check if the characters are in the string
print("pro" in course)

# result = True, check if characters are NOT in the string
print("swift" not in course)


# **************** NUMBERS ******************
x = 1               # integer
x = 1.1             # float
x = 1 + 2j          # a + bi, complex number

print(10 + 3)       # addition
print(10 - 3)       # subtraction
print(10 * 3)       # multiplication
print(10 / 3)       # result = 3.3333 , division
print(10 // 3)      # result = 3 , get the whole number
print(10 % 3)       # result = 1 , modulo -->  return the remainder
print(10 ** 3)      # result = 1000 , exponent

# augmentor assignment operator
x = 10
x = x + 3
x += 3


# **************** USEFUL FUNCTIONS to work in NUMBERS *********************
print(round(2.9))       # round off the number
print(abs(-2.9))        # return a positive value

# using a complex math, use math module
# example:
# import math

# print(math.ceil(2.2))   # result = 2


# ***************** TYPE CONVERSION ***********************
# x = input("x: ")        # data type = String
y = int(x) + 1               # "1" + 1

# print(f"x: {x}, y: {y}")

# print(type(x))        # result = <class "str">, type() --> return the data type of argument
# int(x)                # convert into integer
# float(x)              # convert into float
# bool(x)               # convert into boolean
# str(x)                # convert into string

# Falsy ***
# ""
# 0
# None      --> absence of value

print(bool(0))          # False
print(bool(""))         # False
print(bool(None))       # False
print(bool(-1))         # True
print(bool(1))          # True
print(bool("Hero"))     # True


# QUIZ *****************

# 1.) What are the primitive types in python ?
# answer: String, numbers, and boolean

# 2.) What are the value of these expression ?
fruit = "Apple"
print(fruit[1])
# answer: "p"

print(fruit[1:-1])
# answer: "ppl"

print(10 % 3)
# answer: 1

print(bool("False"))
# answer: True
