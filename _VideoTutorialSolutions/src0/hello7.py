# Demonstrates str functions
#
# EXPLANATION:
# This program splits a full name into parts and uses only the first name.
#
# KEY CONCEPTS:
# - .split(" ") breaks a string into a list wherever it finds a space
# - "David Malan".split(" ") returns ["David", "Malan"]
# - "Unpacking" lets you assign multiple variables at once from a list
# - first, last = ["David", "Malan"] assigns "David" to first, "Malan" to last
#
# HOW IT WORKS:
# 1. User enters "david malan"
# 2. .strip().title() cleans it to "David Malan"
# 3. .split(" ") creates a list: ["David", "Malan"]
# 4. Unpacking assigns: first = "David", last = "Malan"
# 5. Only the first name is printed: "hello, David"
#
# UNPACKING EXPLAINED:
# Instead of writing:
#   parts = name.split(" ")
#   first = parts[0]
#   last = parts[1]
# You can write the shorter:
#   first, last = name.split(" ")
#
# WARNING: This code assumes the user enters exactly two words (first and last name).
# If they enter just one name or more than two, Python will raise an error!

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")
