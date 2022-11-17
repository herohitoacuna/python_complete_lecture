# more control on printing stuff
from pprint import pprint

# *************** EXERCISE *********************
# using dictionaries we can count a key value pair of every character in dictionary
# once you count it, transform into a list of tuple so that we can use a sorted() function.
# reverse it into descending order

sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency)

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])
