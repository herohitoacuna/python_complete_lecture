# *************** PROPERTIES ********************

# property("function getting an attribute", "setting an attribute", "deleting an attribute", "documentation")
#       = is an object that sits in front of an attribute and allows us to get or set the value

class Product:
    def __init__(self, price):
        self.__price = price

    # def get_price(self):                            # def __get_price(self) -> private
    #     return self.__price

    # # set price and price cannot be a negative
    # def set_price(self, value):                     # def __set_price(self) -> private
    #     if value < 0:
    #         raise ValueError("Price cannot be negative")
    #     self.__price = value

    # price = property(get_price, set_price)

    # **** instead of using "__" to private our method, use "decorator" instead ************
    @property               # decorator
    def price(self):        # getter
        return self.__price

    @price.setter
    def price(self, value):  # setter
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(10)
product.price = -1
# using "property()" you can access the attributes like normal.
print(product.price)
