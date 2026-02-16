# Compares strings
#
# EXPLANATION:
# This program introduces "conditionals" - code that makes decisions using if/else.
#
# KEY CONCEPTS:
# - 'if' checks whether a condition is True or False
# - == is the equality operator (checks if two values are the same)
# - Don't confuse == (comparison) with = (assignment)!
# - 'else' runs when the if condition is False
# - The indented code under if or else is called a "block"
#
# HOW IT WORKS:
# 1. User enters a response (e.g., "yes" or "no")
# 2. Python checks: is answer exactly equal to "yes"?
# 3. If True: prints "Agreed"
# 4. If False: prints "Not agreed"
#
# THE PROBLEM WITH THIS CODE:
# This code is case-sensitive! "Yes", "YES", and " yes" will all fail.
# Only the exact string "yes" (lowercase, no spaces) will work.
#
# See agree1.py and agree2.py for improvements!

answer = input("Do you agree? ")
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")
