# Demonstrates inequalities and logical operator
#
# EXPLANATION:
# This program uses 'or' to check if x is NOT equal to y.
#
# KEY CONCEPTS:
# - 'or' returns True if EITHER condition is True
# - If x < y OR x > y, then x is definitely not equal to y
# - This is logically equivalent to: if x != y
#
# HOW IT WORKS:
# 1. User enters x = 5 and y = 10
# 2. Python checks: Is 5 < 10? Yes!
# 3. Since the first part of 'or' is True, the whole expression is True
# 4. "x is not equal to y" is printed
#
# SHORT-CIRCUIT EVALUATION:
# With 'or', Python stops checking as soon as it finds a True condition.
# If x < y is True, Python doesn't bother checking x > y.
# This is called "short-circuit evaluation" and makes code faster.
#
# LOGICAL THINKING:
# This code shows that the same logic can be expressed different ways.
# "x is not equal to y" can be written as:
# - x != y
# - x < y or x > y
# - not (x == y)
#
# The != operator (see compare5.py) is cleaner for this purpose.

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
