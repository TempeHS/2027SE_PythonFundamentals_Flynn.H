# Demonstrates a function that returns a bool
#
# EXPLANATION:
# This program creates a reusable function that returns True or False.
#
# KEY CONCEPTS:
# - A function can return a boolean value (True or False)
# - 'bool' is a data type with only two values: True and False
# - if is_even(x): works because is_even() returns True or False
# - Returning booleans makes functions reusable and testable
#
# HOW IT WORKS:
# 1. User enters 8
# 2. is_even(8) is called
# 3. Inside is_even: 8 % 2 = 0, which equals 0, so return True
# 4. Back in main: if True: prints "Even"
#
# WHY RETURN A BOOL?
# - The function can be used in any context: if, while, variables, etc.
# - It's more reusable than a function that just prints
# - You can write: result = is_even(x) and use result later
#
# THE IF/ELSE IN IS_EVEN:
# if n % 2 == 0:
#     return True
# else:
#     return False
#
# This works, but it's verbose. See parity2.py and parity3.py for improvements!


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
