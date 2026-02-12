# Tests square() function - organized into multiple test functions
#
# EXPLANATION:
# This organizes tests into separate functions by category.
#
# KEY CONCEPTS:
# - Group related tests into separate functions
# - test_positive() tests positive numbers
# - test_negative() tests negative numbers
# - test_zero() tests the zero edge case
# - Each function has a clear, descriptive name
#
# WHY ORGANIZE TESTS?
# 1. Clarity: Easy to see what each test covers
# 2. Isolation: If test_negative fails, you know where to look
# 3. Selective running: pytest test_calculator6.py::test_zero
# 4. Maintenance: Easier to add or modify tests
#
# PYTEST OUTPUT EXAMPLE:
# test_calculator6.py::test_positive PASSED
# test_calculator6.py::test_negative PASSED
# test_calculator6.py::test_zero PASSED
#
# If a test fails, you immediately know which category failed!
#
# This is a good pattern for larger test suites.

from calculator6 import square


def test_positive():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
