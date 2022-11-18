# ***************  IMPORTING FROM SUB PACKAGES ****************

# we add a file with name "__init__.py" to our sub package
# Use the "dot notation" to access that sub package

from ecommerce.shopping import sales

sales.calc_tax()
