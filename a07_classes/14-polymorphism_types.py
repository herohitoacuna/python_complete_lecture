# ************** DUCKING TYPE **********************

# Duck typing is a concept related to dynamic typing,
#   where the type or the class of an object is less important
#   than the methods it defines. When you use duck typing,
#   you do not check types at all. Instead, you check for the presence of a given method or attribute

# from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


textbox = TextBox()
ddl = DropDownList()

draw([textbox, ddl])
