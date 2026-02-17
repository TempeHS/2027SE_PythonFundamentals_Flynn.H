# Demonstrates equality
#
# EXPLANATION:
# This program checks if two numbers are equal using ==.
#
# KEY CONCEPTS:
# - == is the equality operator (checks if two values are the same)
# - Don't confuse with = (assignment operator)
# - x = 5 assigns the value 5 to x
# - x == 5 checks if x is equal to 5 (returns True or False)
#
# HOW IT WORKS:
# 1. User enters x = 10 and y = 10
# 2. Python checks: Is 10 == 10? Yes!
# 3. "x is equal to y" is printed
#
# COMMON BEGINNER MISTAKE:
# Writing if x = y: instead of if x == y:
# The first is assignment (and will cause a syntax error in if statements)
# The second is comparison (what you want)
#
# EQUALITY WITH DIFFERENT TYPES:
# - 5 == 5 is True
# - 5 == 5.0 is True (Python converts for comparison)
# - "5" == 5 is False (string is not equal to integer)

x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
