# ********************* CREATING CUSTOM CONTAINER ****************************

class TagCloud:
    def __init__(self):
        self.tags = {}

    # add the tag in the tags dictionary, and if in the tags already increament it by 1
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    # __getitem__(self, key) -> use to get an item in dictionary in our class
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # __setitem__(self, key, value) -> use to set an item in dictionary in our class
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # __len__(self) -> use to get the length of object such as list, tuple, string, and dictionaries
    def __len__(self):
        return len(self.tags)

    # __iter__(self) -> use to iterate our class
    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()


# get a value in dictionary attribute using bracket notation
print(cloud["python"])                      # result = 0

# set a value in dictionary
cloud["python"] = 10
print(cloud["python"])                      # result = 10

# get the length of dictionary attribute
print(len(cloud))                           # result = 1

# use a iterable cloud in one of the built-in function
print(tuple(cloud))                         # ("python", )

# adding a python word in tags dictionary
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)                           # result = {"python: 3"}
