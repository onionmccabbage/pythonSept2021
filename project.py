# imagine this is the top level of some Python project

# we can import entire modules
# either from the SAME location
# import using_functions
# or from an accessible locaiton
import my_modules.using_functions
from my_modules.using_functions import pythag

# we can import from the standard python library
import random
# or we can import just the bits we need
from random import randrange

result = pythag(-3, -4) # 5

# print(result)