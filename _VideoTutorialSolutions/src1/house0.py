# Compares multiple strings with if/elif/else
#
# EXPLANATION:
# This program is a Harry Potter Sorting Hat! It assigns Hogwarts houses.
#
# KEY CONCEPTS:
# - Multiple elif statements check different possibilities
# - String comparison with == checks for exact matches
# - The else clause handles any unrecognized names
#
# HOW IT WORKS:
# 1. User enters a name (e.g., "Harry")
# 2. Python checks each condition until one matches
# 3. If name is "Harry", "Hermione", or "Ron" -> Gryffindor
# 4. If name is "Draco" -> Slytherin
# 5. Otherwise -> "Who?"
#
# THE PROBLEM:
# This code is repetitive! Three conditions all lead to "Gryffindor".
# We can simplify this using 'or' - see house1.py.
#
# DESIGN NOTE:
# The else clause with "Who?" is a good practice. It handles
# unexpected inputs gracefully instead of crashing or doing nothing.

name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
