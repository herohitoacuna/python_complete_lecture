#  ************ COMPARISON OPERATORS *****************
print(10 > 3)           # True
print(10 >= 3)          # True
print(10 < 20)          # True
print(10 <= 20)         # True
print(10 == 10)         # True
print(10 == "10")       # False
print(10 != "10")       # True

print("bag" > "apple")  # True , if we sort these two words, bag comes first
print("bag" == "BAG")   # False, "b" and  "B" have different numeric value
print(ord("b"), ord("B"))


# ***************** CONDITIONAL STATEMENTS ****************
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


# ******************* TERNARY OPERATOR *******************
age = 12
# if age >= 18:
#     message = "Eligible"  # print("Eligible")
# else:
#     message = "Not eligible"  # print("Not eligible")


message = "Eligible" if age >= 18 else "Not eligible"
print(message)              # result = Not eligible


# *************** LOGICAL OPERATORS ****************

# and, both condition must be True
# or, either one of the condition it will become True
# not, inverses the value of the boolean

high_income = True
good_credit = True

if high_income and good_credit:     # True
    print("Eligible")
else:
    print("Not eligible")
# result = Eligible


high_income = False
good_credit = True

if high_income or good_credit:      # True
    print("Eligible")
else:
    print("Not eligible")
# result = Eligible


high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:    # True
    print("Eligible")
else:
    print("Not eligible")
# result = Eligible


# **************** SHORT-CIRCUIT EVALUATION ****************
# (and) evaluation stops once one of the arguments equals to False
# (or) evaluation stops once one of the arguments equals to True

high_income = True
good_credit = True
student = True

if high_income and good_credit and not student:     # False
    print("Eligible")
else:
    print("Not eligible")
# result = Not eligible


# *************** CHAINING COMPARiSON OPERATORS ******************

# age shoulb be between 18 and 65
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:      # this is chaining comparison operators
    print("Eligible")


# QUIZ ********************
if 10 == "10":                              # False
    print("a")
elif "bag" > "apple" and "bag" > "cat":     # False
    print("b")
else:
    print("c")
# answer = "c"


# ******************** FOR LOOPS ******************
# print("Sending a message") # printing message multiple times

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
    print("Attempted 3 times and failed")
print("-----")


# ******************** NESTED LOOPS *******************
for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")
print("-----")


# ************************** ITERABLES ***********************
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

# QUIZ ***************
# write a program that display even numbers from 1 to 10
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")
