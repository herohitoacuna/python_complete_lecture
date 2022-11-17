# ********************* EXTENDING BUILT-IN TYPES ***********8

class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")

# python --> since we inherit the base class "str", we can use lower() method
print(text.lower())

print(text.duplicate())         # PythonPython

# ----------------------


class TrackableList(list):
    # we are only extending the append method of list, we are not replacing
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
