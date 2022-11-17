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
