# ***************  DIR FUNCTION****************

# dir() function -> when calling an imported object we use the "dot notation", sometimes it doesnt work.
#                   so we can use dir() function to check all the functions or methods in our modules.
from ecommerce.shopping import sales

# print(dir(sales))
# result = ['__builtins__', '__cached__', '__doc__', '__file__',
#       '__loader__', '__name__', '__package__', '__spec__',
#        'calc_shipping', 'calc_tax', 'contact']

print(sales.__name__)       # file_name = ecommerce.shopping.sales
print(sales.__package__)    # package_name = ecommerce.shopping

# path = d:\PYTHON Lecture\a08_modules\6-dir_function\ecommerce\shopping\sales.py
print(sales.__file__)
