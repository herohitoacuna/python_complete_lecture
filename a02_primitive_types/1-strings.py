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
