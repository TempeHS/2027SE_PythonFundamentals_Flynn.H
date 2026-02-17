# Changes * to +
#
# EXPLANATION:
# Changing * to + requires at least one character on each side of @.
#
# KEY CONCEPTS:
# - + means "1 or more" of the previous thing
# - .+ means "1 or more of any character"
# - Unlike *, + requires at least one match
#
# PATTERN: .+@.+
# - .+ = one or more characters (required!)
# - @ = literal @ symbol
# - .+ = one or more characters (required!)
#
# MATCHES:
# - "a@b" ✓ (at least one char on each side)
# - "hello@world" ✓
#
# DOESN'T MATCH:
# - "@" ✗ (nothing before @)
# - "a@" ✗ (nothing after @)
# - "@b" ✗ (nothing before @)
#
# REGEX QUANTIFIERS:
# * = 0 or more (optional, any amount)
# + = 1 or more (required, any amount)
# ? = 0 or 1 (optional, at most one)
# {n} = exactly n
# {n,m} = between n and m
#
# See validate7.py for checking .edu ending!

import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
