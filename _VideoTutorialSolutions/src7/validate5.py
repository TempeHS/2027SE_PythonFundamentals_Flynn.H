# Adds .*
#
# EXPLANATION:
# This uses .* - one of the most common regex patterns!
#
# KEY CONCEPTS:
# - . (dot) matches ANY single character (except newline)
# - * (star) means "0 or more" of the previous thing
# - .* means "0 or more of any character" (match anything!)
#
# PATTERN: .*@.*
# - .* = any characters (or nothing)
# - @ = literal @ symbol
# - .* = any characters (or nothing)
#
# MATCHES:
# - "a@b" ✓ (one char, @, one char)
# - "hello@world" ✓ (multiple chars on each side)
# - "@" ✓ (zero chars on each side - * allows zero!)
#
# THE PROBLEM:
# "@" by itself matches! We need at least something before and after @.
#
# SOLUTION:
# Use + instead of *
# + means "1 or more" (at least one required)
#
# See validate6.py for using +!

import re

email = input("What's your email? ").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")
