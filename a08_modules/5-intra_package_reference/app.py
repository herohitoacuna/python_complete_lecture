# ***************  INTRA-PACKAGES REFERENCE ****************
# IMPORTING FROM SIBLING PACKAGES

# SCENARIO:
#   We want to import the contact module from customer package,
#   and use it in our sales module from shopping package

# contact.py ************
# from ecommerce.customer import contact      # Absolute import
# from ..customer import contact              # relative import


from ecommerce.shopping import sales
sales.calc_tax()
