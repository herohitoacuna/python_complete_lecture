# ***************** INHERITANCE ***************************

# Inheritance = is a mechanism that allows us to define the common behavior or common functions

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
m.eat()                     # result = "eat"
print(m.age)                # result = 1
