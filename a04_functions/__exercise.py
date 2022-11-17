# *************** EXERCISE *************************

# solve the fizz_buzz algorithm

# if divisible by 3, return Fizz
# if divisible by 5, return Buzz
# if divisible by 3 and 5, return FizzBuzz
# else return the number

def fizz_buzz(value_input):
    if (value_input % 3 == 0) and (value_input % 5 == 0):
        return "FizzBuzz"
    if value_input % 3 == 0:
        return "Fizz"
    if value_input % 5 == 0:
        return "Buzz"
    return value_input


print(fizz_buzz(15))
