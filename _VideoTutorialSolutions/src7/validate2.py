# Validates email address by checking username and domain separately
#
# EXPLANATION:
# This splits the email at @ and validates each part!
#
# KEY CONCEPTS:
# - email.split("@") splits into [username, domain]
# - List unpacking: username, domain = email.split("@")
# - Check that username exists and domain has a dot
#
# HOW IT WORKS:
# For "harry@hogwarts.edu":
# 1. Split at @: ["harry", "hogwarts.edu"]
# 2. username = "harry", domain = "hogwarts.edu"
# 3. Check: username is not empty AND domain contains "."
#
# PYTHON TRUTHY VALUES:
# 'if username' checks if username is not empty.
# Empty string "" is False (falsy)
# Any non-empty string is True (truthy)
#
# STILL LIMITED:
# - "a@b.c" is valid (domain could be anything)
# - "a@b." is valid (ends with dot?)
# - What if we want only .edu emails?
#
# See validate3.py for checking domain endings!

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
