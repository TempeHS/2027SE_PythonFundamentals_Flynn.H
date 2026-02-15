# Demonstrates defining a function with a return value
#
# EXPLANATION:
# Same calculator - test_calculator4.py adds more test cases!
#
# KEY CONCEPTS:
# - Good tests cover many cases: positive, negative, zero, edge cases
# - test_calculator4.py tests: 2, 3, -2, -3, 0
# - More tests = more confidence your code works
#
# WHAT TO TEST?
# - Normal cases: square(2) == 4, square(3) == 9
# - Edge cases: square(0) == 0
# - Negative numbers: square(-2) == 4 (negatives squared are positive!)
# - Boundary cases: very large or very small numbers
#
# TEST COVERAGE:
# The goal is to test all important scenarios.
# Think about what could go wrong!
# - What if n is negative?
# - What if n is zero?
# - What if n is very large?
#
# The more cases you test, the more bugs you'll catch early!


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
