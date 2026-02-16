# Tests hello() function - basic tests
#
# EXPLANATION:
# This tests the hello() function from hello1.py.
#
# KEY CONCEPTS:
# - Test the default behavior: hello() with no argument
# - Test with an argument: hello("David")
# - hello() returns a string, so we can compare with ==
#
# HOW IT WORKS:
# test_default():
#   - Calls hello() with no argument
#   - Checks that it returns "hello, world" (the default)
#
# test_argument():
#   - Calls hello("David")
#   - Checks that it returns "hello, David"
#
# WHY RETURN MATTERS:
# Because hello() returns a string (not prints), we can:
# - Store the result: result = hello("David")
# - Compare it: assert result == "hello, David"
# - Test it automatically!
#
# If hello() printed instead of returning, testing would be harder.

from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"
