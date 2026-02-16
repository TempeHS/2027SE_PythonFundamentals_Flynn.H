# Demonstrates conversion of str to float
#
# EXPLANATION:
# This program works with decimal numbers (floating-point numbers).
#
# KEY CONCEPTS:
# - A "float" is a number with a decimal point: 3.14, 2.5, 1.0
# - float() converts a string to a floating-point number
# - Use float() instead of int() when you need decimal precision
# - int() would lose the decimal part: int("3.7") = 3 (the .7 is lost!)
#
# HOW IT WORKS:
# 1. User enters "1.5" -> float("1.5") = 1.5
# 2. User enters "2.3" -> float("2.3") = 2.3
# 3. z = 1.5 + 2.3 = 3.8
# 4. print(z) outputs: 3.8
#
# INT VS FLOAT:
# - int (integer): Whole numbers only: 1, 42, -7, 0
# - float (floating-point): Numbers with decimals: 1.5, 3.14159, -0.001
#
# WHY "FLOATING-POINT"?
# The decimal point can "float" to different positions to represent
# very small numbers (0.00001) or very large numbers (1000000.0).
#
# WHEN TO USE WHICH:
# - Use int for counting things: number of students, items in a list
# - Use float for measurements: temperature, price, distance

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x + y

print(z)
