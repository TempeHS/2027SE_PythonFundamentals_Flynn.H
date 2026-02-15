# Tests square() function - catches AssertionError
#
# EXPLANATION:
# This shows how to catch AssertionError for better error messages.
#
# KEY CONCEPTS:
# - When assert fails, it raises AssertionError
# - try/except can catch AssertionError like any exception
# - This lets us print custom error messages
#
# HOW IT WORKS:
# try:
#     assert square(2) == 4
# except AssertionError:
#     print("2 squared was not 4")
#
# If square(2) != 4, the assert fails, but we catch the error
# and print a helpful message instead of crashing.
#
# THE PROBLEM:
# This is getting verbose and repetitive!
# Every test needs its own try/except block.
# Testing frameworks like pytest handle this automatically.
#
# See test_calculator5.py for the pytest solution!

from calculator3 import square


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


if __name__ == "__main__":
    main()
