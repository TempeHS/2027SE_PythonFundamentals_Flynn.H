# Reformats "last, first" as "first last"
#
# EXPLANATION:
# This converts "Malan, David" to "David Malan" using string methods.
#
# KEY CONCEPTS:
# - split(", ") splits on comma+space
# - Unpack into two variables: last, first
# - Rearrange with f-string
#
# HOW IT WORKS:
# Input: "Malan, David"
# 1. Check if "," in name (might be "David Malan" already)
# 2. Split at ", ": ["Malan", "David"]
# 3. Unpack: last = "Malan", first = "David"
# 4. Rearrange: f"{first} {last}" = "David Malan"
#
# INPUT FORMATS:
# - "Malan, David" -> split and rearrange
# - "David Malan" -> use as-is (no comma)
#
# LIMITATION:
# The comma and space must be exact: ", "
# "Malan,David" (no space) wouldn't work.
#
# See format1.py for a regex approach!

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
