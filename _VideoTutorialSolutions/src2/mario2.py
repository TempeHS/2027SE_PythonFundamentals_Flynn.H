# Prints column of bricks using a function with a loop
#
# EXPLANATION:
# This program wraps the column-printing logic in a reusable function.
#
# KEY CONCEPTS:
# - print_column(height) is a function that prints a column of given height
# - The function is parameterized - you can call it with any height
# - main() calls print_column(3) to print 3 bricks
# - This design makes the code reusable and easy to modify
#
# HOW IT WORKS:
# 1. main() is called
# 2. main() calls print_column(3)
# 3. print_column loops 3 times, printing "#" each time
#
# OUTPUT:
# #
# #
# #
#
# FUNCTION BENEFITS:
# - Reusability: Call print_column(5) or print_column(10) anywhere
# - Abstraction: main() doesn't need to know HOW the column is printed
# - Testing: You can test print_column separately
#
# This is good function design - the function does ONE thing
# (prints a column) and does it well.


def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()
