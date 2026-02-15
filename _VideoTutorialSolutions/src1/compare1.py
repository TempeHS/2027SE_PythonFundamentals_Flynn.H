# Demonstrates mutually exclusive conditions
#
# EXPLANATION:
# This program uses elif to make the conditions mutually exclusive.
#
# KEY CONCEPTS:
# - 'elif' stands for "else if" - it's checked only if previous conditions were False
# - Once one condition is True, the rest are skipped
# - This is more efficient for mutually exclusive conditions
# - "Mutually exclusive" means only one can be true at a time
#
# HOW IT WORKS:
# 1. User enters x = 5 and y = 10
# 2. Python checks: Is 5 < 10? Yes! Prints "x is less than y"
# 3. Python SKIPS the elif and else blocks entirely
#
# IF VS ELIF:
# - Multiple 'if' statements: Each is checked independently
# - if/elif/else chain: Only one block runs, and Python stops checking
#
# EFFICIENCY:
# In compare0.py, Python always checks all 3 conditions.
# Here, Python might only check 1 condition (if the first is True).
#
# NOTE: The last elif (x == y) could be simplified to 'else'
# since if x is not < y and not > y, it must be equal.
# See compare2.py for this improvement.

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
