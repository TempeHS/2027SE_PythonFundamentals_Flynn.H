# Uses re.search
#
# EXPLANATION:
# This uses regex capture groups to extract first and last names!
#
# KEY CONCEPTS:
# - (.+) is a capture group matching one or more characters
# - matches.groups() returns all captured groups as a tuple
# - Unpack the tuple: last, first = matches.groups()
#
# PATTERN: r"^(.+), (.+)$"
# - ^(.+) = capture everything at start (last name)
# - , = literal comma and space
# - (.+)$ = capture everything at end (first name)
#
# HOW IT WORKS:
# Input: "Malan, David"
# Group 1 captures: "Malan"
# Group 2 captures: "David"
# matches.groups() returns: ("Malan", "David")
# Unpack and rearrange!
#
# .GROUPS() VS .GROUP():
# - matches.groups() returns ALL groups as tuple
# - matches.group(1) returns specific group by number
# - matches.group(0) returns the entire match
#
# See format2.py for using .group() directly!

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = first + " " + last
print(f"hello, {name}")
