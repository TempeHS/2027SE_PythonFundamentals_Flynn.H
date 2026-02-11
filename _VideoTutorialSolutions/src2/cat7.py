# Demonstrates a for loop, with _ as a variable
#
# EXPLANATION:
# This program uses _ as the loop variable - a Python convention.
#
# KEY CONCEPTS:
# - The underscore _ is a valid variable name in Python
# - Using _ signals "I don't actually need this variable"
# - It tells other programmers: "we're just counting, not using the value"
# - This is a Pythonic convention for "throwaway" variables
#
# HOW IT WORKS:
# Same as cat6.py! The loop runs 3 times.
# We just don't care about the values 0, 1, 2 - we're only counting.
#
# WHEN TO USE _:
# - Looping a specific number of times without needing the index
# - Unpacking values you don't need: first, _ = get_name_and_age()
# - In the Python shell, _ holds the last result
#
# READABILITY:
# for i in range(3):    <- "we're using i for something"
# for _ in range(3):    <- "we're just repeating 3 times"
#
# Using _ makes your intent clearer to other programmers.
#
# NOTE: _ is just a regular variable. You CAN use it (print(_) works),
# but by convention, you shouldn't if you chose _ to indicate "unused."

for _ in range(3):
    print("meow")
