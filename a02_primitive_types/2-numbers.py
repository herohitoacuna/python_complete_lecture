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
