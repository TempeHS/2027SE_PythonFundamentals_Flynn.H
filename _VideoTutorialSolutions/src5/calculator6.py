# Tests a function with multiple functions via pytest
#
# EXPLANATION:
# test_calculator6.py shows organizing tests into multiple functions.
#
# KEY CONCEPTS:
# - Group related tests into separate test functions
# - test_positive() - tests positive numbers
# - test_negative() - tests negative numbers
# - test_zero() - tests the zero case
# - This organization makes tests easier to understand and maintain
#
# WHY MULTIPLE TEST FUNCTIONS?
# 1. If one fails, you know which category of tests failed
# 2. Easier to read and understand
# 3. Can run specific test functions: pytest test_calculator6.py::test_positive
# 4. Better organization as tests grow
#
# TEST FUNCTION NAMING:
# def test_positive():  # Tests positive inputs
# def test_negative():  # Tests negative inputs
# def test_zero():      # Tests zero input
#
# Good test names describe what they're testing!
#
# See test_calculator6.py for the organized test file.


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
