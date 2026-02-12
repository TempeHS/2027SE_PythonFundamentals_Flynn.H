# Demonstrates else
#
# EXPLANATION:
# This program uses 'else' with try/except to run code only when no exception occurs.
#
# KEY CONCEPTS:
# - 'else' (after except) runs ONLY if no exception occurred in try
# - This ensures print(f"x is {x}") only runs when x was successfully assigned
# - The else block fixes the NameError from number2.py!
#
# TRY/EXCEPT/ELSE STRUCTURE:
# try:
#     # Code that might raise an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Code that runs ONLY if no exception occurred
#
# HOW IT WORKS:
# CASE 1: User enters "42"
# - try block succeeds, x = 42
# - except block is skipped
# - else block runs: prints "x is 42"
#
# CASE 2: User enters "cat"
# - try block fails, ValueError raised
# - except block runs: prints "x is not an integer"
# - else block is skipped (no NameError!)
#
# WHY USE ELSE?
# It keeps the try block focused on just the risky code.
# Only the code that might raise an exception should be in try.

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
