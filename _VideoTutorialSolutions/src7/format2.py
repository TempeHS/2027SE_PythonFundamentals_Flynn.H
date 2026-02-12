# Uses .group
#
# EXPLANATION:
# This accesses capture groups by NUMBER instead of unpacking.
#
# KEY CONCEPTS:
# - matches.group(1) = first capture group
# - matches.group(2) = second capture group
# - matches.group(0) = the ENTIRE match (rarely used)
#
# PATTERN: r"^(.+), (.+)$"
# - Group 1: (.+) before comma = last name
# - Group 2: (.+) after comma = first name
#
# HOW IT WORKS:
# Input: "Malan, David"
# matches.group(1) = "Malan"
# matches.group(2) = "David"
# name = group(2) + " " + group(1) = "David Malan"
#
# WHEN TO USE EACH:
# - groups(): When you want ALL groups at once
# - group(n): When you need specific groups
# - group(n): Useful when groups are used multiple times
#
# See format3.py for the walrus operator!

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
