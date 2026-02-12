# Compares multiple strings
#
# EXPLANATION:
# This program accepts multiple valid inputs using the 'or' operator.
#
# KEY CONCEPTS:
# - 'or' is a logical operator that returns True if EITHER condition is True
# - answer == "yes" or answer == "y" accepts both "yes" and "y"
# - The entire condition is True if at least one part is True
# - This makes the program more user-friendly
#
# HOW IT WORKS:
# 1. User enters "y"
# 2. Python checks: Is answer == "yes"? No.
# 3. Python checks: Is answer == "y"? Yes!
# 4. Since one condition is True, the whole 'or' expression is True
# 5. "Agreed" is printed
#
# LOGICAL OPERATORS IN PYTHON:
# - 'or' : True if at least one condition is True
# - 'and': True only if ALL conditions are True
# - 'not': Inverts the condition (True becomes False, False becomes True)
#
# COMMON MISTAKE:
# Don't write: if answer == "yes" or "y":  <- This is WRONG!
# Python reads this as: (answer == "yes") or ("y")
# The string "y" is always truthy, so this is always True!

answer = input("Do you agree? ").strip().lower()
if answer == "yes" or answer == "y":
    print("Agreed")
else:
    print("Not agreed")
