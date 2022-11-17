# ************** MULTIPLE-LEVEL INHERITANCE ***************

# too much inheritance is bad, its make our code more complex and produce more issues.

# "pass" -> makes our class empty

class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


# EXAMPLE OF BAD USE OF INHERITANCE.
# chicken cannot fly
c = Chicken()
c.fly()

# Employee -> Person -> LivingCreature -> Thing         # Multi-level inheritance
