# Demonstrates defining a function with a return value
#
# EXPLANATION:
# Same calculator - test_calculator3.py shows handling AssertionError.
#
# KEY CONCEPTS:
# - When assert fails, it raises AssertionError
# - You CAN catch AssertionError with try/except
# - But this is rarely a good idea in practice!
# - Testing frameworks (pytest) handle this automatically
#
# WHY CATCH ASSERTIONERROR? (test_calculator3.py)
# try:
#     assert square(2) == 4
# except AssertionError:
#     print("2 squared was not 4")
#
# This shows the MANUAL way to handle test failures.
# It's educational, but not how real testing is done.
#
# THE BETTER WAY:
# Use pytest! It automatically catches assert failures,
# reports them nicely, and continues running other tests.
# See test_calculator5.py and later for pytest examples.


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
