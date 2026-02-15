# Adds character class
#
# EXPLANATION:
# This uses a CHARACTER CLASS to specify exactly which characters are allowed!
#
# KEY CONCEPTS:
# - [abc] matches any ONE of a, b, or c
# - [a-z] matches any lowercase letter (a through z)
# - [a-zA-Z0-9_] matches letters, numbers, or underscore
# - Character classes replace the vague . with specific characters
#
# PATTERN: r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"
# - [a-zA-Z0-9_]+ = one or more letters, numbers, or underscores
# - @ = literal @
# - [a-zA-Z0-9_]+ = one or more letters, numbers, or underscores
# - \.edu$ = literal .edu at end
#
# CHARACTER CLASS EXAMPLES:
# - [aeiou] = vowels
# - [0-9] = digits
# - [a-z] = lowercase letters
# - [A-Z] = uppercase letters
# - [a-zA-Z] = any letter
# - [^abc] = anything EXCEPT a, b, c (^ at start means NOT)
#
# NOW "!@#$%@evil.edu" IS INVALID:
# Special characters like ! and $ aren't in [a-zA-Z0-9_]
#
# See validate10.py for a shortcut: \w!

import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
