# *********************** CREATING MODULES ******************
# modules = is a file that contains related codes,
#           use to section our code instead of using one file for all codes.

# import a specific function from module
from sales import calc_shipping, calc_tax

# import a module as an object
import sales

sales.calc_tax()
sales.calc_shipping()

calc_tax()
calc_shipping()

# ************* COMPILED PYTHON FILES *************************

# Once we run app.py, python compiled it
#           in folder "__pycache__" so that when we load the module again, python will look for compiled module
#           and the compiled module will load. Result faster loading of module
