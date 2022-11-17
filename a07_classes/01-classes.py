# ******************* CLASSES ***************
# Class: is a blueprint for creating new object
# Object: instance of a classs

# Class: Human
# Object: John, Mary, Jack


# ***************** CREATING CLASSES *******************
# class Point:
#     # every method we need atleast one parameter
#     def draw(self):
#         print("draw")


# point = Point()                     # creating a Point object
# print(type(point))

# # True, checking if point is intance of Point class
# print(isinstance(point, Point))


# ***************** CONSTRUCTORS *******************
# class Point:
#     # x and y ->  parameters
#     # self -> reference to the current object
#     # using "self" we can READ ATTRIBUTES of the current objecto OR we can CALL other METHODS in this object.
#     def __init__(self, x, y):       # constructor # magic method
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# print(point.x)                  # 1
# point.draw()                    # Point (1, 2)
