# Demonstrates rounding to nearest int
#
# EXPLANATION:
# This program uses the round() function to round the result to a whole number.
#
# KEY CONCEPTS:
# - round() rounds a number to the nearest integer
# - round(2.4) = 2 (rounds down because .4 is less than .5)
# - round(2.6) = 3 (rounds up because .6 is greater than .5)
# - round(2.5) = 2 (Python uses "banker's rounding" - rounds to nearest EVEN number)
#
# HOW IT WORKS:
# 1. User enters decimal numbers (e.g., 1.5 and 2.3)
# 2. x + y = 3.8
# 3. round(3.8) = 4 (rounded to nearest whole number)
# 4. Output: 4
#
# ROUND FUNCTION SYNTAX:
# - round(number) -> rounds to nearest integer
# - round(number, digits) -> rounds to specified decimal places
#   round(3.14159, 2) = 3.14
#   round(3.14159, 3) = 3.142
#
# BANKER'S ROUNDING (interesting fact!):
# When a number is exactly halfway (like 2.5), Python rounds to the
# nearest EVEN number. So round(2.5) = 2, but round(3.5) = 4.
# This reduces bias when rounding many numbers.

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)
