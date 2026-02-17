# Adds optional subdomain
#
# EXPLANATION:
# This handles optional subdomains like mail.hogwarts.edu!
#
# KEY CONCEPTS:
# - (...) creates a GROUP
# - (...)? makes the group OPTIONAL (0 or 1 occurrence)
# - (\w+\.)? = optionally: word characters followed by a dot
#
# PATTERN: r"^\w+@(\w+\.)?\w+\.edu$"
# - \w+ = username (required)
# - @ = literal @
# - (\w+\.)? = optional subdomain (like "mail.")
# - \w+ = domain name (required)
# - \.edu$ = .edu at the end
#
# MATCHES:
# - harry@hogwarts.edu ✓ (no subdomain)
# - harry@mail.hogwarts.edu ✓ (with subdomain)
#
# GROUPS IN REGEX:
# - (...) captures what's inside for later use
# - (...)? makes the group optional
# - (?:...) is a non-capturing group (groups without saving)
#
# FINAL NOTES:
# Email validation is actually VERY complex!
# Real email addresses can have +, -, and other characters.
# For production, use a library or send a verification email.
# These examples teach regex patterns, not perfect email validation.

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
