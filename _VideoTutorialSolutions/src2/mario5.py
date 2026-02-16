# Prints square of bricks using a function with nested loops
#
# EXPLANATION:
# This program prints a square (grid) of bricks using nested loops.
#
# KEY CONCEPTS:
# - Nested loops: a loop inside another loop
# - The outer loop (i) controls ROWS
# - The inner loop (j) controls COLUMNS within each row
# - end="" prevents newlines so bricks stay on the same row
# - print() alone prints a newline to end each row
#
# HOW IT WORKS (for size=3):
# Outer loop i=0: Inner loop prints ### , then print() ends the row
# Outer loop i=1: Inner loop prints ### , then print() ends the row
# Outer loop i=2: Inner loop prints ### , then print() ends the row
#
# OUTPUT:
# ###
# ###
# ###
#
# UNDERSTANDING NESTED LOOPS:
# for i in range(3):        <- Run 3 times (once per row)
#     for j in range(3):    <- Run 3 times per row (once per column)
#         print("#", end="")
#     print()               <- End the row with a newline
#
# Total prints of "#": 3 rows × 3 columns = 9
#
# See mario6.py for a simpler version using string multiplication!


def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()
