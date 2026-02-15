# Validates email address by checking whether domain ends with .edu
#
# EXPLANATION:
# This checks if the email is a .edu email specifically!
#
# KEY CONCEPTS:
# - string.endswith(suffix) checks if string ends with suffix
# - domain.endswith(".edu") returns True if domain ends with ".edu"
# - Great for validating specific domain types
#
# HOW IT WORKS:
# For "harry@hogwarts.edu":
# 1. Split: username = "harry", domain = "hogwarts.edu"
# 2. Check username exists: True
# 3. Check domain.endswith(".edu"): True
# 4. Print "Valid"
#
# RELATED METHODS:
# - string.endswith(".edu") - ends with suffix
# - string.startswith("https://") - starts with prefix
#
# LIMITATIONS OF THIS APPROACH:
# As validation gets complex, if statements get messy.
# What if we want to allow .edu, .com, AND .org?
# What if we want to validate the username characters?
#
# ENTER REGULAR EXPRESSIONS (regex)!
# A powerful pattern-matching language for strings.
# See validate4.py for our first regex!

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
