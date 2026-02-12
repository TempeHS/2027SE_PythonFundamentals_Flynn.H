# Prints column of bricks using a loop
#
# EXPLANATION:
# This program uses a for loop to print a column of bricks.
#
# KEY CONCEPTS:
# - for _ in range(3): repeats the code block 3 times
# - The underscore _ indicates we don't need the loop variable
# - Each iteration prints one brick and moves to a new line
#
# HOW IT WORKS:
# 1. Loop iteration 1: print "#" (then newline)
# 2. Loop iteration 2: print "#" (then newline)
# 3. Loop iteration 3: print "#" (then newline)
#
# OUTPUT (same as mario0.py):
# #
# #
# #
#
# ADVANTAGE:
# Change range(3) to range(10) and you get 10 bricks!
# No need to add more lines of code.
#
# See mario2.py for an even more reusable version with a function.

for _ in range(3):
    print("#")
