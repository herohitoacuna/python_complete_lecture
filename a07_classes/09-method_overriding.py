# ************************* METHOD OVERRIDING **************

class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()              # use to extend the animal class __init__ method
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()

# error because __init__ method from base class is not called
# use "super().__init__()" to inherit the constructor from base class
print(m.age)
print(m.weight)
