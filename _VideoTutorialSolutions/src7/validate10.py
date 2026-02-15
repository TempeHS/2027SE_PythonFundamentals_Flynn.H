# Replaces character class with \w
#
# EXPLANATION:
# \w is a SHORTHAND for [a-zA-Z0-9_] - much easier to type!
#
# KEY CONCEPTS:
# - \w = "word character" = [a-zA-Z0-9_]
# - \d = digit = [0-9]
# - \s = whitespace = [ \t\n\r\f\v]
# - Uppercase versions are the OPPOSITE (\W = non-word char)
#
# PATTERN: r"^\w+@\w+\.edu$"
# Same as: r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"
# Much shorter!
#
# SHORTHAND CLASSES:
# \w = word character [a-zA-Z0-9_]
# \W = NON-word character
# \d = digit [0-9]
# \D = NON-digit
# \s = whitespace (space, tab, newline)
# \S = NON-whitespace
#
# USING SHORTHAND:
# r"\d{3}-\d{4}" matches phone numbers like "555-1234"
# r"\s+" matches one or more whitespace characters
#
# See validate11.py for case-insensitive matching!

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
