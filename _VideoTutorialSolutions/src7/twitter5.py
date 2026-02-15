# Ignores query and fragment
#
# EXPLANATION:
# This extracts just the username, ignoring ? and # parts of the URL.
#
# KEY CONCEPTS:
# - URLs can have query strings: ?param=value
# - URLs can have fragments: #section
# - We want just the username, not these extras
# - Use [a-z0-9_]+ to match only valid username characters
#
# PATTERN: r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)"
# - (.+) would capture EVERYTHING after twitter.com/
# - ([a-z0-9_]+) captures only valid username chars
#
# INPUT: https://twitter.com/davidmalan?ref=home
# With (.+): captures "davidmalan?ref=home" (too much!)
# With ([a-z0-9_]+): captures just "davidmalan" ✓
#
# HOW IT WORKS:
# [a-z0-9_]+ stops matching when it hits ? or #
# Because ? and # aren't in the character class!
# The regex naturally stops at non-username characters.
#
# re.IGNORECASE makes [a-z] also match A-Z.
#
# This is a robust Twitter username extractor!

import re

url = input("URL: ").strip()

matches = re.search(
    r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE
)
if matches:
    print("Username:", matches.group(1))
