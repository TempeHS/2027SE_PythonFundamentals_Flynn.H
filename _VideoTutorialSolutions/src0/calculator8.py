# Demonstrates division
#
# EXPLANATION:
# This program performs division, which always produces a float in Python.
#
# KEY CONCEPTS:
# - The / operator divides two numbers
# - Division ALWAYS returns a float, even if the result is a whole number
# - 10 / 2 = 5.0 (not 5)
# - This is because division might produce decimals: 10 / 3 = 3.333...
#
# HOW IT WORKS:
# 1. User enters x (e.g., 10) and y (e.g., 3)
# 2. z = 10 / 3 = 3.3333333333333335
# 3. Output: 3.3333333333333335
#
# PYTHON DIVISION OPERATORS:
# - / (true division): Always returns float: 10 / 3 = 3.333...
# - // (floor division): Returns int, rounds DOWN: 10 // 3 = 3
# - % (modulo): Returns remainder: 10 % 3 = 1
#
# WHY SO MANY DECIMALS?
# Computers store decimals in binary (base 2), which can't perfectly
# represent some decimal numbers. This leads to tiny imprecisions.
# 1/3 can't be exactly represented, just like you can't write 1/3
# exactly in decimals (0.33333... goes on forever).
#
# WARNING: Be careful dividing by zero! y = 0 will cause a ZeroDivisionError.

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)
