# ********************* COMPARING OBJECTS ****************************

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # evaluated the value of two objects, if its true then True
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     # use to work with greater than comparison operator
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(1, 2)
# other = Point(1, 2)

# # False, by default "==" comapre the reference memory of an object
# print(point == other)           # True

# point = Point(10, 20)
# other = Point(1, 2)

# # by default it is error
# print(point > other)            # True


# ********************* PERFORMING ARITHMETIC OPERATIONS ****************************

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):       # use to work with addition
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 2)
other = Point(1, 2)
# print(point + other)            # <__main__.Point object at 0x0000024117813E50>
combine = point + other
print(combine.x)                  # 11
