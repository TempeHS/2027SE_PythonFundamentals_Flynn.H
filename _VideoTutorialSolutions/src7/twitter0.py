# Extracts Twitter username from URL using str.replace
#
# EXPLANATION:
# This extracts a Twitter username from a URL using string replacement.
#
# KEY CONCEPTS:
# - str.replace(old, new) replaces all occurrences of old with new
# - Here we replace the URL prefix with nothing ("")
# - This leaves just the username!
#
# HOW IT WORKS:
# Input: "https://twitter.com/davidmalan"
# replace("https://twitter.com/", "")
# Output: "davidmalan"
#
# THE PROBLEM:
# replace() replaces ALL occurrences anywhere in the string.
# If username contains "https://twitter.com/", it would be removed!
# (Unlikely, but possible)
#
# Also, what about variations like:
# - http:// (no s)
# - www.twitter.com
# - just twitter.com
#
# See twitter1.py for removeprefix() - a safer option!

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
