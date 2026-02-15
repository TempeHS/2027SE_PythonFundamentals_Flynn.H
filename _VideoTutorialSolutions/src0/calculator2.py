# Demonstrates conversion from str to int
#
# EXPLANATION:
# This program fixes the bug from calculator1.py by converting strings to integers.
#
# KEY CONCEPTS:
# - int() is a function that converts a value to an integer (whole number)
# - int("42") converts the string "42" to the number 42
# - This process is called "type conversion" or "casting"
# - After conversion, + performs addition instead of concatenation
#
# HOW IT WORKS:
# 1. User types 1 -> x contains the string "1"
# 2. User types 2 -> y contains the string "2"
# 3. int(x) converts "1" to 1, int(y) converts "2" to 2
# 4. z = 1 + 2 = 3 (actual math!)
# 5. print(z) outputs: 3
#
# TYPE CONVERSION FUNCTIONS:
# - int() -> converts to integer (whole number): int("42") = 42
# - float() -> converts to floating-point (decimal): float("3.14") = 3.14
# - str() -> converts to string: str(42) = "42"
#
# WARNING: int("hello") will cause an error because "hello" can't become a number!

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
