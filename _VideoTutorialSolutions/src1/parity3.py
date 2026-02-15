# Demonstrates returning the value of a Boolean expression
#
# EXPLANATION:
# This is the CLEANEST way to return a boolean - just return the expression!
#
# KEY CONCEPTS:
# - n % 2 == 0 is already a boolean expression - it evaluates to True or False
# - You can return it directly: return n % 2 == 0
# - No need for if/else or ternary operators!
# - This is more elegant and Pythonic
#
# HOW IT WORKS:
# 1. n = 8
# 2. n % 2 == 0 evaluates to: 8 % 2 == 0 -> 0 == 0 -> True
# 3. return True
#
# EVOLUTION OF IS_EVEN:
# Version 1 (parity1.py):
#   if n % 2 == 0:
#       return True
#   else:
#       return False
#
# Version 2 (parity2.py):
#   return True if n % 2 == 0 else False
#
# Version 3 (parity3.py):
#   return n % 2 == 0
#
# All three do the same thing, but version 3 is the most Pythonic!
#
# WHEN TO USE THIS PATTERN:
# Whenever you find yourself writing:
#   if condition:
#       return True
#   else:
#       return False
# Just write: return condition


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
