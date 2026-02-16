# Tests hello() function - in a test subfolder
#
# EXPLANATION:
# This test file lives in a 'test' subfolder!
#
# KEY CONCEPTS:
# - Tests can be organized in folders
# - pytest finds tests in subdirectories too
# - The __init__.py file makes 'test' a package (required)
# - This helps organize larger projects
#
# FOLDER STRUCTURE:
# src5/
#   hello1.py         <- the module being tested
#   test/
#     __init__.py     <- makes this a package (can be empty)
#     test_hello1c.py <- this test file
#
# HOW TO RUN:
# From src5 folder: pytest test/
# Or: pytest test/test_hello1c.py
#
# WHY ORGANIZE TESTS IN FOLDERS?
# - Keeps source and test code separate
# - Cleaner project structure
# - Easier to find and manage tests
# - Standard practice in larger projects
#
# IMPORT PATH:
# Since hello1.py is in the parent folder, Python can still find it
# when running pytest from the src5 directory.

from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"
