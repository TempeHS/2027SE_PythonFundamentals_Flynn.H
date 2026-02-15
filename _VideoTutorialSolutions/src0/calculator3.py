# Demonstrates nesting of function calls
#
# EXPLANATION:
# This program shows a cleaner way to get integer input by "nesting" functions.
#
# KEY CONCEPTS:
# - "Nesting" means putting one function call inside another
# - int(input(...)) takes the result of input() and immediately converts it
# - The inner function (input) runs first, then the outer function (int)
# - This is more concise than using two separate lines
#
# HOW IT WORKS:
# 1. input("What's x? ") runs first, returning a string like "5"
# 2. int("5") runs second, converting the string to the number 5
# 3. The result (5) is stored in variable x
# 4. Same process for y
# 5. x + y now does real addition because both are integers
#
# COMPARISON:
# Without nesting (more lines):
#   x_str = input("What's x? ")
#   x = int(x_str)
#
# With nesting (one line):
#   x = int(input("What's x? "))
#
# Both do the same thing, but nesting is more compact!
# Just don't nest too many functions - it can become hard to read.

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y

print(z)
