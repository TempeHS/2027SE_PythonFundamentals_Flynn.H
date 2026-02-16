# Tests square() function with more test cases
#
# EXPLANATION:
# This adds more test cases for better coverage.
#
# KEY CONCEPTS:
# - Test multiple scenarios: positive, negative, zero
# - More tests = more confidence your code works
# - Think about edge cases and special values
#
# TEST CASES:
# - square(2) == 4   - positive number
# - square(3) == 9   - another positive
# - square(-2) == 4  - negative (squared = positive)
# - square(-3) == 9  - another negative
# - square(0) == 0   - zero (edge case)
#
# WHAT ELSE COULD WE TEST?
# - Large numbers: square(1000000)
# - Decimal inputs (if supported): square(2.5)
# - Invalid inputs: square("cat") - should raise TypeError
#
# The more edge cases you think of, the more robust your code becomes!
#
# NOTE: This manual approach is very verbose.
# See test_calculator5.py for the pytest version - much cleaner!

from calculator4 import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()
