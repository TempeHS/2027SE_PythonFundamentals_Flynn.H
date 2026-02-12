# Demonstrates modulo operator
#
# EXPLANATION:
# This program checks if a number is even or odd using the modulo operator.
#
# KEY CONCEPTS:
# - % is the "modulo" operator - it gives the remainder after division
# - 10 % 3 = 1 (10 divided by 3 is 3 with remainder 1)
# - x % 2 gives the remainder when dividing by 2
# - If x % 2 == 0, the number is EVEN (divides evenly by 2)
# - If x % 2 == 1, the number is ODD
#
# HOW IT WORKS:
# 1. User enters 8
# 2. 8 % 2 = 0 (8 divides evenly by 2)
# 3. 0 == 0 is True, so "Even" is printed
#
# Example for odd number:
# 1. User enters 7
# 2. 7 % 2 = 1 (7 = 3*2 + 1, remainder is 1)
# 3. 1 == 0 is False, so "Odd" is printed
#
# MODULO EXAMPLES:
# - 10 % 3 = 1 (10 = 3*3 + 1)
# - 15 % 5 = 0 (15 = 5*3 + 0)
# - 17 % 4 = 1 (17 = 4*4 + 1)
#
# COMMON USES OF MODULO:
# - Check if even/odd (% 2)
# - Check divisibility (% n == 0)
# - Wrap around values (like clock arithmetic)
# - Extract last digit (% 10)

x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
