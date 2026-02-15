# Extracts Twitter username from URL using str.removeprefix
#
# EXPLANATION:
# removeprefix() only removes from the START of the string!
#
# KEY CONCEPTS:
# - str.removeprefix(prefix) removes prefix only if at the start
# - Safer than replace() which removes everywhere
# - Added in Python 3.9
#
# HOW IT WORKS:
# Input: "https://twitter.com/davidmalan"
# removeprefix("https://twitter.com/")
# Output: "davidmalan"
#
# REPLACE VS REMOVEPREFIX:
# replace: Removes ALL occurrences
# removeprefix: Only removes from the START
#
# RELATED:
# - str.removeprefix(prefix) - remove from start
# - str.removesuffix(suffix) - remove from end
#
# STILL LIMITED:
# Doesn't handle http://, www., or other URL variations.
# See twitter2.py for regex solution!

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
