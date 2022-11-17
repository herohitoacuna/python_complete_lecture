# ******************** FOR LOOPS ******************
for number in range(3):
    print("Attempt", number)
print("end")

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
print("end")

for number in range(1, 4):
    print("Attempt", number, (number) * ".")
print("end")

# range(starting number, end of range, how many times to skip)
for number in range(1, 10, 4):
    print("Attempt", number, (number) * ".")
print("end")


# ******************* FOR ELSE *********************
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Succesful")
        break
else:
    print("Attempted 3 times and failed")  # run when for loop does not break
print("-----")


# ******************** NESTED LOOPS *******************
for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")
print("-----")


# ************************** ITERABLES ***********************
# an object that can be iterate or repeatedly perform
print(type(5))              # result = int
print(type(range(5)))       # result = range , it's iterable and use in for loop

# Iterable
for x in "Python":
    print(x)
print("-----")

# iterate in List
for x in [1, 2, 3]:
    print(x)
print("-----")


# ********************** WHILE LOOP ***********************
# while loop use to evaluate the condition and repeating the task.

# for loop is used when the number of iterations is known,
#   whereas execution is done in the while loop until
#     the statement in the program is proved wrong.

number = 100
while number > 0:
    print(number)
    number //= 2
print("-----")


# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# ***************** INFINITE LOOPS *****************
# while True:
#     command = input(">> ")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
