# ************* EXECUTING_MODULES_AS_SCRIPT *****************
# we can run a script in module and when we run this app.py, that script will automatically run.

# In "__init__.py" in ecommerce folder, we print("Ecommerce Initialize")
# In "__init__.py" in ecommerce.shopping folder, we input some code.

# All the codes in our imported modules that does not in the functions or class, it will automatically run.
from ecommerce.shopping import sales

# if we run this "app.py" file
#      result = Ecommerce Initialize                            # comes from Ecommerce "__init__.py"
#               Sales initialize ecommerce.shopping.sales       # comes from sales module
