# Adds \.edu
#
# EXPLANATION:
# This checks for .edu at the end, with a properly ESCAPED dot!
#
# KEY CONCEPTS:
# - . in regex means "any character"
# - To match a literal dot, use \.
# - r"..." is a raw string - backslashes are literal
#
# PATTERN: r".+@.+\.edu"
# - .+ = one or more of any character
# - @ = literal @
# - .+ = one or more of any character
# - \. = literal dot (escaped!)
# - edu = literal "edu"
#
# WHY ESCAPE THE DOT?
# Without escape: ".edu" matches "aedu", "bedu", "xedu", etc.
# With escape: "\.edu" matches only ".edu"
#
# RAW STRINGS (r"..."):
# In normal strings: \\ = one backslash
# In raw strings: \ = one backslash
# Raw strings are easier for regex!
#
# THE PROBLEM:
# Pattern finds .edu ANYWHERE in the string.
# "evil.edu.hacker@domain.com" would match!
#
# See validate8.py for anchoring to start and end!

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
