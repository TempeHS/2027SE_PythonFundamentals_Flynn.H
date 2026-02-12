# Tests square() function - manual approach
#
# EXPLANATION:
# This is a basic, manual way to test the square() function.
#
# KEY CONCEPTS:
# - Import the function we want to test: from calculator1 import square
# - Call the function with known inputs
# - Check if the output matches expected results
# - Print an error message if something is wrong
#
# HOW IT WORKS:
# 1. Call square(2) and check if it equals 4
# 2. Call square(3) and check if it equals 9
# 3. If any test fails, print an error message
#
# LIMITATIONS OF THIS APPROACH:
# - No output if tests pass (silence = success?)
# - Have to manually run this file
# - Lots of repetitive if statements
# - Tests stop at first failure (if we used elif)
#
# This works, but there are better ways! See test_calculator2.py for assert.

from calculator1 import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()
