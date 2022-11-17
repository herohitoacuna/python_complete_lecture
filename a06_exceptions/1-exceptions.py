# ***************** EXCEPTIONS *********************
# to prevent the crashing of our program

# **************** HANDLING EXCEPTIONS ***************20
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    # run if there is no exceptions were thrown
    print("No exceptions were thrown")

print("Execution continues")
