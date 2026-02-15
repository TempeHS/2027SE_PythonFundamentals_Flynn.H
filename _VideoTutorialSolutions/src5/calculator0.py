# Demonstrates defining a function with a return value
#
# EXPLANATION:
# This is a simple calculator with a testable square() function.
#
# KEY CONCEPTS:
# - square(n) returns n * n, which makes it easy to test
# - We can verify: square(2) == 4, square(3) == 9
# - Functions that return values are the foundation of unit testing
#
# THE PROBLEM:
# This version calls main() directly at the bottom.
# When we import this file for testing, main() runs automatically!
# We'd get the "What's x?" prompt when trying to run tests.
#
# THE FIX:
# See calculator1.py which uses: if __name__ == "__main__": main()
# This prevents main() from running when the file is imported.
#
# UNIT TESTING PREVIEW:
# A unit test for square() might look like:
# assert square(2) == 4
# assert square(3) == 9
# assert square(0) == 0
#
# Simple, pure functions like square() are ideal for testing!


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
