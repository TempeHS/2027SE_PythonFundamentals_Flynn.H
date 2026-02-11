# Validates email address by checking for @ with regex
#
# EXPLANATION:
# This introduces REGULAR EXPRESSIONS (regex) - a pattern language!
#
# KEY CONCEPTS:
# - 're' is Python's regular expression module
# - re.search(pattern, string) searches for pattern in string
# - Returns a Match object if found, None if not
# - Regex patterns can describe complex string formats
#
# HOW IT WORKS:
# re.search("@", email) searches for "@" in email
# - If found: returns a Match object (truthy)
# - If not found: returns None (falsy)
#
# THIS IS SIMPLE:
# Using "@" as a regex pattern is the same as 'in' operator.
# The power of regex comes from special characters!
#
# REGEX SPECIAL CHARACTERS:
# . (dot) - matches ANY single character
# * - matches 0 or more of the previous character
# + - matches 1 or more of the previous character
# ^ - start of string
# $ - end of string
#
# See validate5.py for using these special characters!

import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
