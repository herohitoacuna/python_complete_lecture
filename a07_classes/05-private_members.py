# ********************* PRIVATE MEMBERS ****************************

class TagCloud:
    def __init__(self):
        self.__tags = {}        # self.tag -> self.__tags, so that it cannot access directly

    # add the tag in the tags dictionary, and if in the tags already increament it by 1
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    # __getitem__(self, key) -> use to get an item in dictionary in our class
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # __setitem__(self, key, value) -> use to set an item in dictionary in our class
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # __len__(self) -> use to get the length of object such as list, tuple, string, and dictionaries
    def __len__(self):
        return len(self.__tags)

    # __iter__(self) -> use to iterate our class
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
# print(cloud.__tags)             # error, this tags attribute is now private

# adding a python word in tags dictionary
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud["PYTHON"])          # result = 3
# print(cloud.tags["PYTHON"])   # error

# ACCESSING PRIVATE ATTRIBUTES ****
print(cloud.__dict__)           # {'_TagCloud__tags': {'python': 3}}
print(cloud._TagCloud__tags)    # {'python': 3}
