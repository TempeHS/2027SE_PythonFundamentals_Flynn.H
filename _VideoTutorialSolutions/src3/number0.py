# Gets a number from the user
#
# EXPLANATION:
# This program gets a number from the user - but what if they type letters?
#
# KEY CONCEPTS:
# - int() converts the user's input to an integer
# - This works fine if the user types a number like "42"
# - BUT: if the user types "cat", the program CRASHES with a ValueError!
#
# THE PROBLEM:
# Try running this and type "hello" instead of a number.
# You'll see an error like:
#   ValueError: invalid literal for int() with base 10: 'hello'
#
# The program crashes because "hello" can't be converted to a number.
# This is called an "exception" - an error that occurs while running.
#
# WHY THIS MATTERS:
# Real programs need to handle user errors gracefully.
# We can't trust users to always enter valid input!
#
# See number1.py for how to CATCH and handle this exception.

x = int(input("What's x? "))
print(f"x is {x}")
