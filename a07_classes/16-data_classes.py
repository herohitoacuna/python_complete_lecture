# ************** DATA CLASSES *************

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)                             # False

# # id() --> use to get the memory id.
# print(f"p1-id:{id(p1)} \np2-id:{id(p2)}")


# -------------------------------------------
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])     # creating a tuple object
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)


# If you are working with classes with only data and no methods, you might want to use "namedtuple"
# namedtuple are immutable
