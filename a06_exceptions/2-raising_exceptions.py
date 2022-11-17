# ******************** RAISING EXCEPTIONS ***************
# search for built-in Exceptions
from timeit import timeit


# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)


# ************************* COST OF RAISING EXCEPTIONS ***************
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass        # use it so except block cannot be empty
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""


# timeit(codeblock, number of execution)
print("first code=", timeit(code1, number=1000))
print("second code=", timeit(code2, number=1000))

# Building an application for few users, raising an exception in your functions is not have a bad impact in our application

# Building an application with big data, and
#       where perforomance and scalability are important then raise an exception when you really have to.

# Using exception makes our program slower when we dealing with large data
# before using exception think twice if you can handle it with If statement.
