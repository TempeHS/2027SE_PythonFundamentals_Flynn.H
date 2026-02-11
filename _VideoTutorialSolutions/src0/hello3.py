# Demonstrates a function with two positional arguments
#
# EXPLANATION:
# This program shows an alternative way to print multiple items on one line.
#
# KEY CONCEPTS:
# - print() can accept multiple arguments separated by commas
# - Each argument is a "positional argument" - its position matters
# - Python automatically adds a space between each argument when printing
# - This is often cleaner than using + for concatenation
#
# HOW IT WORKS:
# 1. User enters their name
# 2. print() receives TWO arguments: "hello," and the name variable
# 3. Python prints both arguments with a space between them automatically
#
# COMPARISON:
# print("hello, " + name)  <- You must include the space yourself
# print("hello,", name)    <- Python adds the space automatically
#
# The second approach is generally preferred as it's cleaner and less error-prone.

name = input("What's your name? ")
print("hello,", name)
