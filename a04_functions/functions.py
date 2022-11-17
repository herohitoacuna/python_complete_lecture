# ******************* FUNCTIONS **************
# function - reusable piece of code
def greet():
    print("Hi there")
    print("Welcome aborad")


greet()


# ********************** ARGUMENTS ********************
# parameters - use when defining a function
# arguments - use when invoking a function
def greeting(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aborad")


greeting("Herohito", "Acuña")


# **************** TYPES OF FUNCTION **********
# 1- Perform a task
# 2- Return a value

def greets(name):           # Perform a task
    print(f"Hi {name}")
    # return "..."


def get_greeting(name):     # Return a value
    return f"Hi {name}"


message = get_greeting("Mosh")
# print(message)
# file = open("content.txt", "w")
# file.write(message)

# result = None , all functions that perform a task when we printed it will return None
print(greets("Mosh"))


# ***************** KEYWORD ARGUMENTS****************
def increment(number, by):
    return number + by


print(increment(2, by=1))       # by=1 is a keyword argument


# ***************** DEFAULT ARGUMENTS ************
def default_increment(number, by=1):
    return number + by


print(default_increment(2))         # result = 3
print(default_increment(2, 5))      # result = 7
print("------")


# **************** XARGS *******************
# xargs - pass multiple arguments without specifying it in parameters
def multiply(*numbers):
    total = 1                   # return a Tauple
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
print("------")


# ***************** XXARGS ***************
def save_user(**user):              # return a dictionary or an Object(javascript)
    # we can access dictionary using bracket notation (user["id"])
    print(user)


save_user(id=1, name="John", age=22)
print("------")


# **************** SCOPE ****************
# scope = refers to the region of the code where variable is defined
# local variable = only accessible in one code block like function, conditional statement and loops
# Global variable = accessible anywhere in the code

message = "a"           # global vairable


def scope_greet(name):
    message = "a"       # local variable


# result = error, because the scope of message is only exist in local scope wherein the scope_greet function
# print(message)


# ***************** DEBUGGING ***********************
# in vscode click the debugger mode.
#   1- Add breakpoints
#   2- step in
def multiply_debugging(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply_debugging(1, 2, 3))
