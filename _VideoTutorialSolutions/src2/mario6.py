# Prints square of bricks using a function with a loop and str multiplication
#
# EXPLANATION:
# This program simplifies mario5.py by using string multiplication for each row.
#
# KEY CONCEPTS:
# - Instead of nested loops, use one loop + string multiplication
# - The outer loop handles rows
# - "#" * size creates each row (no inner loop needed!)
# - This is simpler and more Pythonic
#
# HOW IT WORKS:
# for _ in range(3):     <- 3 iterations (3 rows)
#     print("#" * 3)     <- Each prints "###" with a newline
#
# OUTPUT:
# ###
# ###
# ###
#
# COMPARISON:
# Nested loops (mario5.py):
#   for i in range(size):
#       for j in range(size):
#           print("#", end="")
#       print()
#
# Loop + string multiplication (this file):
#   for _ in range(size):
#       print("#" * size)
#
# The second version is shorter and easier to understand!
#
# See mario7.py for an even more modular version with separate functions.


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print("#" * size)


main()
