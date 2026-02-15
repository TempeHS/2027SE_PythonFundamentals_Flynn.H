# Adds re.IGNORECASE
#
# EXPLANATION:
# re.IGNORECASE makes the pattern match regardless of case!
#
# KEY CONCEPTS:
# - re.search() can take a third argument: flags
# - re.IGNORECASE (or re.I) ignores case differences
# - "EDU", "edu", "Edu" all match
#
# HOW IT WORKS:
# re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE)
# Now matches:
# - harry@hogwarts.edu ✓
# - Harry@Hogwarts.EDU ✓
# - HARRY@HOGWARTS.EDU ✓
#
# COMMON FLAGS:
# re.IGNORECASE (re.I) - case insensitive
# re.MULTILINE (re.M) - ^ and $ match line starts/ends
# re.DOTALL (re.S) - . matches newlines too
# re.VERBOSE (re.X) - allows comments in regex
#
# COMBINING FLAGS:
# re.search(pattern, string, re.I | re.M)
# Use | (pipe) to combine multiple flags.
#
# See validate12.py for handling subdomains!

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
