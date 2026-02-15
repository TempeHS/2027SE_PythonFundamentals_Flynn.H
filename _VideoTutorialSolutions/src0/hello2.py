# Demonstrates concatenation of strings
#
# EXPLANATION:
# This program greets the user with their name on a single line using concatenation.
#
# KEY CONCEPTS:
# - "Concatenation" means joining strings together end-to-end
# - The + operator can be used to concatenate (join) two strings
# - "hello, " + "David" becomes "hello, David"
# - Notice the space after the comma in "hello, " - without it, the output
#   would be "hello,David" (no space between)
#
# HOW IT WORKS:
# 1. User enters their name (e.g., "David")
# 2. Python joins "hello, " with "David" to create "hello, David"
# 3. The combined string is printed to the screen
#
# NOTE: The + operator works differently depending on the data type.
# For strings, it concatenates. For numbers, it adds mathematically.

name = input("What's your name? ")
print("hello, " + name)
