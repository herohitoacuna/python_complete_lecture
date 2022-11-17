# ******************* TUPLES ***************************
# tuples:
#   is a basically a read only list. We can use it to contain a sequence
#   of objects but we cannot modify this sequence.

point = 1, 2  # OR (1, 2)
point = (1, 2) + (3, 4)         # (1, 2, 3, 4)
point = (1, 2) * 3              # (1, 2, 1, 2, 1, 2)
point = tuple([1, 3, 5])        # (1, 3, 5)
point = tuple("hello")          # ('h', 'e', 'l', 'l', 'o')
point = tuple(range(1, 4))      # (1, 2, 3)
print(point)

# Accessing tuple
print(point[0:2])               # (1, 2)
# Tuple unpacking
x, y, z = point
if 10 in point:
    print("exist")

# point[0] = 10  # cannot modify a tuple


# ********************* SWAPPING VARIABLES ***********************
x = 10
y = 11

# z = x
# x = y
# y = z

x, y = y, x
x, y = (11, 10)  # unpacking

print("x", x)
print("y", y)
