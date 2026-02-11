# Demonstrates conditional expressions (ternary operators)
#
# EXPLANATION:
# This program uses Python's "ternary operator" - a one-line if/else.
#
# KEY CONCEPTS:
# - A ternary operator is: value_if_true if condition else value_if_false
# - return True if n % 2 == 0 else False
# - It reads like: "return True if n is even, else return False"
# - This is a shorthand for if/else when assigning or returning values
#
# HOW IT WORKS:
# 1. n % 2 == 0 is evaluated
# 2. If True: return True
# 3. If False: return False
#
# TERNARY OPERATOR SYNTAX:
# result = value_if_true if condition else value_if_false
#
# EXAMPLES:
# - status = "adult" if age >= 18 else "minor"
# - max_value = a if a > b else b
# - greeting = "Good morning" if hour < 12 else "Good afternoon"
#
# WHEN TO USE:
# - Simple if/else that assigns or returns a value
# - When it makes the code more readable (not more confusing!)
# - Avoid nesting ternary operators - they become hard to read
#
# This is still a bit redundant - see parity3.py for the cleanest version!


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False


main()
