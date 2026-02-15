# Uses or
#
# EXPLANATION:
# This program simplifies house0.py using the 'or' operator.
#
# KEY CONCEPTS:
# - 'or' lets you combine multiple conditions
# - If ANY of the conditions is True, the whole expression is True
# - This avoids repeating the same print statement multiple times
#
# HOW IT WORKS:
# 1. User enters "Hermione"
# 2. Python checks: Is name == "Harry"? No.
# 3. Python checks: Is name == "Hermione"? Yes!
# 4. The whole 'or' expression is True, so "Gryffindor" is printed
#
# SHORT-CIRCUIT EVALUATION:
# Python stops checking as soon as it finds a True condition.
# For "Harry", Python doesn't check "Hermione" or "Ron".
#
# COMPARISON TO HOUSE0:
# Before (house0.py): 4 separate if/elif blocks for Gryffindor members
# After (house1.py): 1 condition using 'or' for all Gryffindor members
#
# COMMON MISTAKE:
# Don't write: if name == "Harry" or "Hermione"  <- WRONG!
# This is incorrect because "Hermione" alone is always "truthy".
# You must write: if name == "Harry" or name == "Hermione"

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
