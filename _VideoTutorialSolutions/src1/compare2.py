# Demonstrates fewer conditions
#
# EXPLANATION:
# This program uses 'else' as a catch-all for the final condition.
#
# KEY CONCEPTS:
# - 'else' catches everything that didn't match previous conditions
# - No condition needs to be specified for else
# - If x is not less than y, and not greater than y, it MUST be equal
# - This is called "logical deduction" - we know the answer without checking
#
# HOW IT WORKS:
# 1. User enters x = 10 and y = 10
# 2. Python checks: Is 10 < 10? No.
# 3. Python checks: Is 10 > 10? No.
# 4. Python runs the else block: "x is equal to y"
#
# WHY THIS IS BETTER:
# - Fewer conditions to write and check
# - Logically complete - all possibilities are covered
# - The else acts as a "default" or "fallback" case
#
# IF/ELIF/ELSE STRUCTURE:
# if condition1:
#     # runs if condition1 is True
# elif condition2:
#     # runs if condition1 is False AND condition2 is True
# else:
#     # runs if ALL above conditions are False

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
