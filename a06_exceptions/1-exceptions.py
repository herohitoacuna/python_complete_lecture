# ***************** EXCEPTIONS *********************
# to prevent the crashing of our program
# instead of crashing our program, it will throw another value.

# **************** HANDLING EXCEPTIONS ***************20
# try:
#     age = int(input("Age: "))
# except ValueError as error:
#     print("You didn't enter a valid age.")
#     print(error)
#     print(type(error))
# else:
#     # run if there is no exceptions were thrown
#     print("No exceptions were thrown")

# print("Execution continues")


# ********************** HANDLING DIFFERENT EXCEPTIONS *********************
# try:
#     age = int(input("Age: "))
#     # ZeroDivisionError = exception, error when we enter value 0
#     xfactor = 10 / age
# except (ValueError,  ZeroDivisionError):
#     print("You didn't enter a valid age.")
# # except ZeroDivisionError:
# #     print("You didn't enter a valid age.")
# else:
#     # run if there is no exceptions were thrown
#     print("No exceptions were thrown")
# print("Execution continues")


# ********************** CLEANING UP ************************
# try:
#     # file = open("content.txt")
#     age = int(input("Age: "))
#     # ZeroDivisionError = exception, error when we enter value 0
#     xfactor = 10 / age
# except (ValueError,  ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     # run if there is no exceptions were thrown
#     print("No exceptions were thrown")
# # finally:
# #     file.close()


# *************** the WITH statement ***********************
# try:
#     with open("content.txt") as file:  # , open(another.txt) as target:
#         print("File opened")
#         file.__enter__
#     age = int(input("Age: "))
#     # ZeroDivisionError = exception, error when we enter value 0
#     xfactor = 10 / age
# except (ValueError,  ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     # run if there is no exceptions were thrown
#     print("No exceptions were thrown")
