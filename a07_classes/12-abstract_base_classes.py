from abc import ABC, abstractmethod

# ******************* ABSTRACT BASE CLASSES *******************

# ABSTRACT BASE CLASS - is a class that is used as a blueprint for other classes.
# ABSTRACT BASE CLASSES are a powerful feature in Python since they help you
#           define a blueprint for other classes that may have something in common.

# ISSUES:
#       1- We cannot create an instance from the base class, we only instance in the subclass
#       2- FileStream class and NetwrokStream class have a same read() method

# Steps: to solve our issue:
#   1- import ABC, abstractmenthod from abc
#   2- extend the base class (Stream class) into ABC -->> Stream(ABC)
#   3- define a common interface in all streams. read() method


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
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

    @abstractmethod  # decorate
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")

# stream = Stream()       # We cannot instantiate the abstract class
# stream.open()


# if a class derives or base from stream class,
#       it has to implement read() method, otherwise that class will also become abstract

# all subclass base from Stream class must have a common interface such as read() method.
# If subclass doesn't have common interface as Abstrace Base Class, that subclass is also considered as Abstract
stream = MemoryStream()
stream.open()
