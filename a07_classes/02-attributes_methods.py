# ***************** CLASS vs INSTANCE ATTRIBUTES *******************

# class Point:
#     # class attribute -> these are attributes that we define at the class level
#     # these are all the same accross all the instances
#     default_color = "red"

#     def __init__(self, x, y):
#         # instance attribute -> these attributes that belong to point instances
#         # every intsance it can have different attributes
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# Point.default_color = "yellow"          # changing the class attribute

# point = Point(1, 2)
# # value = red change value = yellow, accessing a class level attribute
# print(point.default_color)
# # value = red change value = yellow, accessing a class level attribute
# print(Point.default_color)
# point.draw()

# another = Point(3, 4)
# # value = red change value = yellow, accessing a class level attribute
# print(another.default_color)
# another.draw()


# ********************** CLASS vs INSTANCE METHODS ********************

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # decorator -> it's a way to extend the behavior of a method or function.
#     @classmethod
#     def zero(cls):      # by convention whenever we define a class method we call it's first parameter "cls"
#         return cls(0, 0)       # same as Point(0, 0)

#     def draw(self):     # instance method
#         print(f"Point ({self.x}, {self.y})")


# point = Point.zero()   # classs method
# point.draw()


# ********************** MAGIC METHODS ********************
# magic methods, have two underscores at the beginning and end of their name
# called by python interpreter dependingon how we use our objects and classes

# search python 3 magic methods
# class Point:
#     def __init__(self, x, y):           # magic methods
#         self.x = x
#         self.y = y

#     def __str__(self):                  # returns the value of the class
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# # when we create point object __init__ method will call automatically by python interpreter
# point = Point(1, 2)
# print(point)                # (1, 2), returns the value of the class

# point2 = Point(3, 2)
# print(type(point2))         # <class '__main__.Point'>
