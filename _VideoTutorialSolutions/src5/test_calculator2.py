# Tests square() function using assert
#
# EXPLANATION:
# This introduces the 'assert' statement for testing.
#
# KEY CONCEPTS:
# - 'assert' checks if a condition is True
# - If True: nothing happens, program continues
# - If False: raises AssertionError and program crashes
# - Much cleaner than if statements!
#
# HOW ASSERT WORKS:
# assert square(2) == 4
# This says: "I assert that square(2) equals 4"
# If it does, great! If not, the program crashes with an error.
#
# COMPARISON:
# Before: if square(2) != 4: print("error")
# After:  assert square(2) == 4
#
# THE PROBLEM:
# If assert fails, you get an ugly error and the program stops.
# No nice error message, no indication of what failed.
# See test_calculator3.py for handling AssertionError.

from calculator2 import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()
