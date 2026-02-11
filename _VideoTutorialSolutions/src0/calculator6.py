# Demonstrates fewer variables
#
# EXPLANATION:
# This program shows that you don't always need intermediate variables.
#
# KEY CONCEPTS:
# - You can put expressions directly inside function calls
# - round(x + y) adds x and y, then rounds the result
# - print(round(x + y)) does the calculation, rounds it, and prints it
# - This reduces the number of variables needed
#
# HOW IT WORKS:
# 1. Get x and y from user
# 2. print() receives round(x + y) as its argument
# 3. Python evaluates from inside out:
#    - First: x + y (e.g., 3.8)
#    - Then: round(3.8) = 4
#    - Finally: print(4) displays the result
#
# COMPARISON:
# More variables (explicit):
#   z = x + y
#   z = round(z)
#   print(z)
#
# Fewer variables (compact):
#   print(round(x + y))
#
# WHEN TO USE EACH:
# - Use intermediate variables when debugging or when the code is complex
# - Use compact form for simple, obvious operations
# - Always prioritize readability over brevity!
#
# Remember: Code is read more often than it's written. Make it clear!

x = float(input("What's x? "))
y = float(input("What's y? "))

print(round(x + y))
