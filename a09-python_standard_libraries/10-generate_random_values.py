import random
import string

print(random.random())      # return random number between 0 and 1
print(random.randint(1, 10))    # return random integers
print(random.choice([1, 2, 3, 4]))  # return random numbers from list

# return random numbers from list, using "k" keyword we can choice how many numbers to choose
print(random.choices([1, 2, 3, 4], k=2))

char_choices = string.ascii_letters + string.punctuation + string.digits

# generate random password
print("".join(random.choices(char_choices, k=10)))

# shuffling an array
numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)


# generate random password No.2


def generate_pass(num_loops=1):
    arr_chars = list(string.ascii_letters + string.digits +
                     string.punctuation[:random.randint(1, len(string.punctuation))])

    for x in range(num_loops):
        random.shuffle(arr_chars)

    password = "".join(random.choices(arr_chars, k=20))

    return password


print("Random Generated Password")
for x in range(1, 3):
    print(f"pass_{x}: {generate_pass()}")
