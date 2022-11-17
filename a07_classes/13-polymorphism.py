# ****************** POLYMORPHISM ***********************

# POLYMORPHISM, use of a single symbol to represent multiple different types

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    # control.draw()
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
# draw(ddl)
# draw(textbox)
draw([ddl, textbox])

# print(isinstance(ddl, UIControl))     #result = True

