# Demonstrates conditionals
#
# EXPLANATION:
# This program compares two numbers using multiple if statements.
#
# KEY CONCEPTS:
# - < means "less than"
# - > means "greater than"
# - == means "equal to" (remember: single = is assignment!)
# - Each 'if' statement is evaluated independently
#
# HOW IT WORKS:
# 1. User enters x = 5 and y = 10
# 2. Python checks: Is 5 < 10? Yes! Prints "x is less than y"
# 3. Python checks: Is 5 > 10? No. Skips this block.
# 4. Python checks: Is 5 == 10? No. Skips this block.
#
# THE PROBLEM:
# All three conditions are checked every time, which is inefficient!
# For comparing x and y, only ONE of these can be true at a time.
# If x < y is True, we don't need to check the others.
#
# COMPARISON OPERATORS:
# - <   less than
# - >   greater than
# - ==  equal to
# - <=  less than or equal to
# - >=  greater than or equal to
# - !=  not equal to
#
# See compare1.py for a more efficient solution using elif.

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
