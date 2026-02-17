# Demonstrates own module
#
# EXPLANATION:
# This program imports a function from YOUR OWN module (sayings0.py)!
#
# KEY CONCEPTS:
# - You can create your own modules (just Python files!)
# - 'from sayings0 import hello' imports the hello function from sayings0.py
# - Your modules work just like built-in modules
# - This is how you organize code across multiple files
#
# HOW IT WORKS:
# 1. sayings0.py defines a hello(name) function
# 2. This file imports that function
# 3. Calls hello(sys.argv[1]) to greet the user
#
# FILE STRUCTURE:
# say2.py (this file) - the main program
# sayings0.py - your module with hello() and goodbye() functions
#
# WHY CREATE MODULES?
# - Organization: Keep related functions together
# - Reusability: Use the same functions in multiple programs
# - Testing: Test modules independently
# - Collaboration: Different team members work on different modules
#
# The sayings0.py file just defines functions - no main() call.
# See sayings1.py and sayings2.py for more complex examples.

import sys

from sayings0 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
