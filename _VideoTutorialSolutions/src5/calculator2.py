# Demonstrates defining a function with a return value
#
# EXPLANATION:
# Same calculator, but test_calculator2.py introduces 'assert'!
#
# KEY CONCEPTS:
# - This file is identical to calculator1.py
# - The difference is in the TEST file (test_calculator2.py)
# - test_calculator2.py uses 'assert' instead of if statements
#
# WHAT IS ASSERT?
# assert expression - raises AssertionError if expression is False
# assert square(2) == 4 means: "I assert that square(2) equals 4"
# If it's true, nothing happens. If false, the program crashes.
#
# ASSERT VS IF:
# Before (test_calculator1.py):
#     if square(2) != 4:
#         print("2 squared was not 4")
#
# After (test_calculator2.py):
#     assert square(2) == 4
#
# Much cleaner! assert is the foundation of automated testing.


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
