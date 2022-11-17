# *************** MULTIPLE INHERITANCE **********

# BAD INHERITANCE *************
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()

# Employee Greet, python check first if the first base clas has a greet() method
manager.greet()


# GOOD INHERITANCE ***************
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


# ******************* GOOD EXAMPLE OF INHERITANCE *******************

# creating custom EXCEPTION
class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class Network(Stream):
    def read(self):
        print("Reading data from a network")
