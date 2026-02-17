# Catches a ValueError
#
# EXPLANATION:
# This program introduces try/except to handle exceptions gracefully.
#
# KEY CONCEPTS:
# - 'try' wraps code that MIGHT cause an exception
# - 'except' catches the exception and runs alternative code
# - ValueError is the type of exception raised by int() for bad input
# - The program no longer crashes - it handles the error gracefully!
#
# HOW IT WORKS:
# TRY BLOCK:
# 1. Try to convert input to int and print it
# 2. If this succeeds, skip the except block
#
# EXCEPT BLOCK:
# 3. If a ValueError occurs, run this code instead
# 4. Print a friendly error message
#
# EXAMPLE RUNS:
# Input: 42 -> Output: "x is 42"
# Input: cat -> Output: "x is not an integer"
#
# THE PROBLEM:
# This only tries ONCE. If the user enters bad input, the program just
# prints an error and ends. See number4.py for a loop that keeps asking.
#
# DIFFERENT EXCEPTION TYPES:
# - ValueError: Invalid value (like int("hello"))
# - TypeError: Wrong type used
# - ZeroDivisionError: Division by zero
# - FileNotFoundError: File doesn't exist

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
