# Adds ^ and $ to regex
#
# EXPLANATION:
# This uses ANCHORS to match the entire string, not just part of it!
#
# KEY CONCEPTS:
# - ^ means "start of string"
# - $ means "end of string"
# - Together they ensure the WHOLE string matches the pattern
#
# PATTERN: r"^.+@.+\.edu$"
# - ^ = must start here
# - .+ = one or more characters
# - @ = literal @
# - .+ = one or more characters
# - \.edu = literal .edu
# - $ = must end here
#
# WITHOUT ANCHORS:
# "evil.edu.hacker@fake.com" matches (contains .+@.+\.edu somewhere)
#
# WITH ANCHORS:
# "evil.edu.hacker@fake.com" doesn't match (doesn't END with .edu)
#
# ANCHORS ARE ESSENTIAL:
# Without them, you're searching for a pattern WITHIN the string.
# With them, you're validating the ENTIRE string matches.
#
# See validate9.py for being more specific about allowed characters!

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
