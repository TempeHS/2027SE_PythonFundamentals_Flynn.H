# Tests square() function using pytest
#
# EXPLANATION:
# This uses PYTEST - the professional way to test Python code!
#
# KEY CONCEPTS:
# - pytest is a testing framework - install with: pip install pytest
# - Test functions must start with 'test_'
# - Just use assert statements - pytest handles the rest!
# - Run with: pytest test_calculator5.py
#
# HOW PYTEST WORKS:
# 1. Finds files matching test_*.py
# 2. Finds functions matching test_*
# 3. Runs each test function
# 4. Catches assert failures and reports them
# 5. Shows a summary: X passed, Y failed
#
# BENEFITS:
# - No need for try/except - pytest handles failures
# - Clear output showing what passed/failed
# - Runs ALL tests, even if some fail
# - Shows detailed info when tests fail
#
# NOTICE:
# No main(), no if __name__ == "__main__"
# Just test functions! pytest discovers and runs them.

from calculator5 import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
