print("Sales initialize", __name__)
# result = Sales initialize __main__


def calc_tax():
    pass


def calc_shipping():
    pass


# if we run app.py these piece of code will not going to run because __name__ is equal to the filename
if __name__ == "__main__":
    print("Sales started")
    calc_tax()
