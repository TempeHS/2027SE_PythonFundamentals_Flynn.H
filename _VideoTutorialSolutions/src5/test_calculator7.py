# Tests square() function - including testing for exceptions
#
# EXPLANATION:
# This shows how to test that a function raises the correct exception!
#
# KEY CONCEPTS:
# - Sometimes you WANT a function to raise an error
# - pytest.raises() tests that an exception is raised
# - with pytest.raises(TypeError): square("cat")
# - This test PASSES if TypeError is raised, FAILS if not!
#
# HOW PYTEST.RAISES WORKS:
# with pytest.raises(TypeError):
#     square("cat")
#
# This says: "I expect square('cat') to raise a TypeError"
# - If TypeError is raised: Test PASSES
# - If no error raised: Test FAILS
# - If different error raised: Test FAILS
#
# WHY TEST EXCEPTIONS?
# - Ensure functions reject invalid input properly
# - Verify error handling works correctly
# - Document expected behavior for edge cases
#
# COMMON EXCEPTIONS TO TEST:
# - TypeError: Wrong type passed (string instead of number)
# - ValueError: Right type but invalid value (negative for sqrt)
# - IndexError: List index out of bounds
# - KeyError: Dictionary key not found

import pytest

from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
