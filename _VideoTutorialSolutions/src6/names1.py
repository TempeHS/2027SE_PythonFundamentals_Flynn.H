# Stores names in a list
#
# EXPLANATION:
# This stores multiple names in a list - still temporary though!
#
# KEY CONCEPTS:
# - Lists can store multiple values
# - _ is used as a loop variable when we don't need the value
# - sorted() returns a sorted copy of the list
# - All data is still lost when the program ends
#
# HOW IT WORKS:
# 1. Create empty list: names = []
# 2. Loop 3 times, asking for a name each time
# 3. Append each name to the list
# 4. Print names in alphabetical order using sorted()
#
# THE UNDERSCORE (_):
# for _ in range(3): means "repeat 3 times"
# We use _ because we don't need the number (0, 1, 2)
# It's a Python convention for "throwaway" variables.
#
# STILL TEMPORARY!
# Run the program, enter 3 names, see them printed...
# Close the program, run again - the names are gone!
# We need FILES to save data permanently.

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")
