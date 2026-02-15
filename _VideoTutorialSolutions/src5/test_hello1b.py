# Tests hello() function - using a loop for multiple test cases
#
# EXPLANATION:
# This uses a loop to test multiple names efficiently!
#
# KEY CONCEPTS:
# - Use loops to test many values with less code
# - for name in ["Hermione", "Harry", "Ron"]: tests three names
# - f-strings help create expected results dynamically
#
# HOW IT WORKS:
# for name in ["Hermione", "Harry", "Ron"]:
#     assert hello(name) == f"hello, {name}"
#
# This tests:
# - hello("Hermione") == "hello, Hermione"
# - hello("Harry") == "hello, Harry"
# - hello("Ron") == "hello, Ron"
#
# WHY USE LOOPS IN TESTS?
# - Less repetitive code
# - Easy to add more test cases
# - Same pattern for all similar tests
#
# CAUTION:
# If a loop assertion fails, you might not know WHICH iteration failed.
# For critical tests, separate assert statements might be clearer.

from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
