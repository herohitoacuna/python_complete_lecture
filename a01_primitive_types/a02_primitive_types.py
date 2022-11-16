# Variables & Data Types
# students_count = 1000               # interger
# rating = 4.99                       # float
# is_published = False                # Boolean


# # ******************* STRINGS *****************
# course = "Python Programming"
# print(len(course))                  # return number of characters

# Accessing the character of string using index--> return first character of string = P
# BRACKER NOTATIOn
# print(course[0])
# print(course[-1])       # return the last character
# print(course[0:3])      # return 0 to the 2nd index
# print(course[0:])       # return 0 to last character
# print(course[:3])       # return the first 3 character of string
# print(course[:])        # return all character in string


# ************** ESCAPE SEQUENCE *******************

# \"    - to use double quote in string
# \'    - to use single qoute in string
# \\    - to use backlash in string
# \n    - to create new line of string

# course = "Python \"Programming"     # result = Python "Programming
# print(course)


# ************ FORMATTED STRINGS ***************

# first = "Mosh"
# last = "Hamedani"
# full_name = first + " " + last
# print(full_name)        # result = Mosh Hamedani

# full = f"{first} {last}"
# print(full)             # result = Mosh Hamedani


# *************** STRING METHODS *************

# len()         --> use to get all characters
course = "python programming"
print(course.upper())       # result = PYTHON PROGRAMMING
print(course)               # result = python programming
print(course.lower())       # result = python programming
# result = Python programming  --> make into capital letter
print(course.title())
