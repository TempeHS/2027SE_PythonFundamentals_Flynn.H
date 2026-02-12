# Demonstrates own module
#
# EXPLANATION:
# This program imports the goodbye function from sayings2.py.
#
# KEY CONCEPTS:
# - You can import different functions from the same module
# - from sayings2 import goodbye just imports goodbye, not hello
# - sayings2.py defines both hello() and goodbye() functions
# - This demonstrates how modules can provide multiple related functions
#
# HOW IT WORKS:
# 1. Import only the goodbye function from sayings2
# 2. Call goodbye(sys.argv[1]) to say farewell to the user
#
# OUTPUT:
# python say5.py David -> "goodbye, David"
#
# IMPORTING MULTIPLE FUNCTIONS:
# from sayings2 import hello, goodbye
# This would import both functions.
#
# IMPORTING ALL FUNCTIONS (not recommended):
# from sayings2 import *
# This imports everything, but makes code harder to understand.
#
# BEST PRACTICE:
# Import only what you need. This makes dependencies clear
# and prevents naming conflicts.

import sys

from sayings2 import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
