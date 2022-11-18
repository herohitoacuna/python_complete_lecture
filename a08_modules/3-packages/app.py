# *************** PACKAGES **************
# PACKAGE = is a container for one or mode modules

# importing from a sub direcotries

# normally when importing a module, the file must be the same directories from module.
# to import a module from different directories:
#       ADD a file to the sub directories(ecommerce), name it "__init__.py"

# Python will treat "ecommerce" folder as a package


# import ecommerce.sales
# ecommerce.sales.calc_tax()

# ISSUE: if we want to import more function from sales module, it will become messy
from ecommerce.sales import calc_tax, calc_shipping
# calc_tax()

# Instead we import diffent function from sales module, we import the sales module as an object
from ecommerce import sales
sales.calc_tax()
