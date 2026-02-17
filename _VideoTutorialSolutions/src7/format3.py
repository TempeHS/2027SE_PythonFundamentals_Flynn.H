# Uses walrus operator
#
# EXPLANATION:
# The WALRUS OPERATOR (:=) assigns AND returns a value in one expression!
#
# KEY CONCEPTS:
# - := is called the "walrus operator" (looks like a walrus: :=)
# - It assigns a value AND returns it
# - Allows assignment inside expressions (like if conditions)
# - Added in Python 3.8
#
# PATTERN: if matches := re.search(...):
# This does TWO things:
# 1. Runs re.search() and assigns result to 'matches'
# 2. Uses 'matches' as the if condition
#
# WITHOUT WALRUS:
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
#
# WITH WALRUS:
# if matches := re.search(r"^(.+), (.+)$", name):
#     name = matches.group(2) + " " + matches.group(1)
#
# One line shorter! The assignment is INSIDE the if.
#
# WALRUS USE CASES:
# - Assigning in if/while conditions
# - Avoiding repeated function calls
# - Cleaner code in some situations

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
