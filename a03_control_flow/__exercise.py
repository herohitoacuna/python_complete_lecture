# ************** QUIZ ********************
# Conditional Statements
# by look at it what is the value will be printed

if 10 == "10":                              # False
    print("a")
elif "bag" > "apple" and "bag" > "cat":     # False
    print("b")
else:
    print("c")
# answer = "c"


# ************** QUIZ ***************
# Loops
# write a program that display even numbers from 1 to 10

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")
