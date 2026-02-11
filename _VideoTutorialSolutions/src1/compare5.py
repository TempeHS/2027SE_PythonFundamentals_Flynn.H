# Demonstrates inequality
#
# EXPLANATION:
# This program uses the != (not equal) operator.
#
# KEY CONCEPTS:
# - != means "not equal to"
# - It's the opposite of ==
# - x != y is True when x and y have different values
# - This is cleaner than writing: x < y or x > y
#
# HOW IT WORKS:
# 1. User enters x = 5 and y = 10
# 2. Python checks: Is 5 != 10? Yes! (5 is not equal to 10)
# 3. "x is not equal to y" is printed
#
# ALL COMPARISON OPERATORS:
# - ==  equal to
# - !=  not equal to
# - <   less than
# - >   greater than
# - <=  less than or equal to
# - >=  greater than or equal to
#
# READING != :
# Some people read != as "not equal to"
# Others read it as "bang equals" (! is sometimes called "bang")
# In Python, you might also write: not (x == y) for the same effect

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
