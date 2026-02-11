# Tests a function with one function via pytest
#
# EXPLANATION:
# This calculator is tested with PYTEST - a professional testing framework!
#
# KEY CONCEPTS:
# - pytest automatically finds and runs test files (test_*.py)
# - It finds test functions (def test_...)
# - It catches assert failures and reports them nicely
# - Install with: pip install pytest
# - Run with: pytest test_calculator5.py
#
# PYTEST ADVANTAGES:
# - Auto-discovery: Finds all test_*.py files automatically
# - Clear reports: Shows exactly which tests passed/failed
# - Continues on failure: Runs ALL tests, even if some fail
# - Detailed errors: Shows what was expected vs what was received
#
# HOW TO USE PYTEST:
# 1. Create a test file: test_calculator5.py
# 2. Write test functions that start with test_
# 3. Use assert statements in your tests
# 4. Run: pytest
#
# See test_calculator5.py for a clean pytest test file!


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
