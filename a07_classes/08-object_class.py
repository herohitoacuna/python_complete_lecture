# ***************** INHERITANCE ***************************

# Inheritance = is a mechanism that allows us to define the common behavior or common functions

# object = is base classes for python

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base-class
# Mammal: Child, Sub-class


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(isinstance(m, Animal))                # True
print(isinstance(m, object))                # True
print(issubclass(Mammal, object))           # True

o = object()                                # creating empty object
