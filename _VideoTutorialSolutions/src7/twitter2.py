# Uses re.sub
#
# EXPLANATION:
# re.sub() substitutes (replaces) text matching a regex pattern!
#
# KEY CONCEPTS:
# - re.sub(pattern, replacement, string) does regex substitution
# - Like str.replace() but with regex power!
# - ^ anchors to the start of string
#
# PATTERN: r"^https://twitter\.com/"
# - ^ = start of string (only matches at beginning)
# - https://twitter\.com/ = literal text (\.  = literal dot)
#
# HOW IT WORKS:
# re.sub(r"^https://twitter\.com/", "", url)
# Replaces the pattern with empty string "" (removes it)
# Leaves just the username!
#
# WHY USE ^ (start anchor)?
# Without ^, pattern could match ANYWHERE.
# With ^, only matches at the START.
# This is like removeprefix() but with regex!
#
# See twitter3.py for handling URL variations!

import re

url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username: {username}")
