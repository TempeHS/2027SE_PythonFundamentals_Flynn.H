# Prints square of bricks using a function with a loop and str multiplication
#
# EXPLANATION:
# This program demonstrates good function decomposition.
#
# KEY CONCEPTS:
# - print_square() calls print_row() - functions can call other functions!
# - Each function has a single responsibility:
#   - print_square: print multiple rows
#   - print_row: print one row
# - This is called "abstraction" and "separation of concerns"
#
# HOW IT WORKS:
# 1. main() calls print_square(3)
# 2. print_square loops 3 times, calling print_row(3) each time
# 3. print_row prints "###"
#
# OUTPUT:
# ###
# ###
# ###
#
# WHY SEPARATE FUNCTIONS?
# - Reusability: print_row could be used elsewhere
# - Testing: You can test print_row independently
# - Readability: print_square's logic is clear - "print 'size' rows"
# - Flexibility: You could change print_row without changing print_square
#
# FUNCTION HIERARCHY:
# main() -> print_square() -> print_row()
#
# This is a simple example, but in larger programs, this kind of
# decomposition is essential for managing complexity.


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
