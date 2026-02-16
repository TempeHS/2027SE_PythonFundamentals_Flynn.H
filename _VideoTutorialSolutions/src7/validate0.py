# Validates email address by checking for @
#
# EXPLANATION:
# This is a SIMPLE email validation - just checking for @.
#
# KEY CONCEPTS:
# - 'in' operator checks if a substring exists in a string
# - "@" in email returns True if @ is found anywhere
# - strip() removes whitespace from start and end of input
#
# HOW IT WORKS:
# 1. Get email from user, strip whitespace
# 2. Check if "@" appears in the email
# 3. Print Valid or Invalid
#
# LIMITATIONS:
# This is too simple! These would all be "Valid":
# - "@"           (just an @)
# - "@@@@"        (multiple @s)
# - "hello@"      (nothing after @)
# - "@world"      (nothing before @)
#
# Real email validation is complex. We'll build up to better
# solutions using Regular Expressions (regex)!
#
# See validate1.py for the next improvement.

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
