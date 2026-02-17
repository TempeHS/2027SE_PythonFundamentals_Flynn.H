# Demonstrates a NameError
#
# EXPLANATION:
# This program shows what happens when a variable isn't defined.
#
# KEY CONCEPTS:
# - If the except block runs, the variable x is never assigned
# - Trying to use an undefined variable causes a NameError
# - This is a DIFFERENT error from the ValueError we're catching!
#
# THE PROBLEM:
# 1. User enters "cat"
# 2. int("cat") raises ValueError
# 3. except block runs, prints error message
# 4. x was never assigned a value!
# 5. print(f"x is {x}") crashes with NameError: name 'x' is not defined
#
# WHAT WENT WRONG:
# The print statement is OUTSIDE the try block, so it always runs.
# But x only exists if the try block succeeded!
#
# LESSON:
# Be careful about variable scope with try/except.
# Code that uses x should either be:
# - Inside the try block, OR
# - Inside an 'else' block (see number3.py)
#
# NameError means you're using a variable that doesn't exist.
# This is different from ValueError (bad value for conversion).

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
