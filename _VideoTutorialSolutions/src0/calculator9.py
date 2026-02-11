# Demonstrates rounding after the decimal point
#
# EXPLANATION:
# This program uses round() with a second argument to control decimal places.
#
# KEY CONCEPTS:
# - round(number, ndigits) rounds to the specified number of decimal places
# - round(3.14159, 2) = 3.14 (two decimal places)
# - round(3.14159, 4) = 3.1416 (four decimal places, last digit rounded up)
# - This is useful for displaying clean, readable numbers
#
# HOW IT WORKS:
# 1. User enters x (e.g., 10) and y (e.g., 3)
# 2. x / y = 3.3333333333...
# 3. round(3.333..., 2) = 3.33 (only 2 decimal places)
# 4. Output: 3.33
#
# ROUNDING BEHAVIOR:
# - round(3.145, 2) = 3.15 (rounds up because next digit is 5)
# - round(3.144, 2) = 3.14 (rounds down)
# - round(3.335, 2) = 3.33 (banker's rounding to nearest even)
#
# NOTE: round() returns a float, so 3.33 is actually the float 3.33,
# not the string "3.33". See calculator10.py for string formatting.

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)
