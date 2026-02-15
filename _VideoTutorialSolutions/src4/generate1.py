# Demonstrates from
#
# EXPLANATION:
# This program shows an alternative way to import: 'from module import function'.
#
# KEY CONCEPTS:
# - 'from random import choice' imports just the choice function
# - Now you can use choice() directly, without the 'random.' prefix
# - This is useful when you only need specific functions from a module
#
# COMPARISON:
# import random:
#   coin = random.choice(["heads", "tails"])  <- need 'random.' prefix
#
# from random import choice:
#   coin = choice(["heads", "tails"])  <- no prefix needed!
#
# WHICH TO USE?
# - 'import module': Clear where functions come from, avoids name conflicts
# - 'from module import function': Shorter code, convenient for common functions
#
# IMPORTING MULTIPLE FUNCTIONS:
# from random import choice, randint, shuffle
# This imports multiple specific functions.
#
# IMPORT EVERYTHING (not recommended):
# from random import *
# This imports ALL functions. Avoid this - it can cause name conflicts
# and makes it unclear where functions come from.

from random import choice

coin = choice(["heads", "tails"])
print(coin)
