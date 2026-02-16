# Unpacks a list
#
# EXPLANATION:
# UNPACKING assigns multiple values from a sequence!
#
# KEY CONCEPTS:
# - first, _ = split result assigns to two variables
# - _ is convention for "don't care about this value"
# - Cleaner than using index: result[0]
#
# THE UNPACKING:
# "Harry Potter".split(" ")  # Returns ["Harry", "Potter"]
# first, _ = ["Harry", "Potter"]
# first = "Harry", _ = "Potter" (discarded)
#
# THE UNDERSCORE:
# _ means "I don't need this value"
# It's a valid variable name but signals intent.
#
# MULTIPLE VALUES:
# a, b, c = [1, 2, 3]
# a=1, b=2, c=3
#
# ERROR IF MISMATCH:
# a, b = [1, 2, 3]  # Error! Too many values

first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
