# Uses capture group
#
# EXPLANATION:
# CAPTURE GROUPS let us extract specific parts of a match!
#
# KEY CONCEPTS:
# - (...) creates a capture group
# - matches.group(1) gets what the first group captured
# - (?:...) is a NON-capturing group (groups without saving)
# - This approach validates AND extracts in one step
#
# PATTERN: r"^https?://(?:www\.)?twitter\.com/(.+)$"
# - https?:// = http:// or https://
# - (?:www\.)? = optional www. (non-capturing)
# - twitter\.com/ = literal twitter.com/
# - (.+)$ = one or more chars until end (CAPTURED!)
#
# NON-CAPTURING (?:...):
# (?:www\.)? matches www. but doesn't save it.
# We don't need www. later, so we don't capture it.
# The username (.+) IS captured because we need it!
#
# HOW IT WORKS:
# matches = re.search(pattern, url)
# if matches:  # Did it match?
#     matches.group(1)  # Get first capture group (username)
#
# See twitter5.py for filtering out query strings!

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))
