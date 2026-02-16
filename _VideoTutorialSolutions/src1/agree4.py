# Compares multiple strings
#
# EXPLANATION:
# This program uses .startswith() as a clever shortcut to accept any "y" answer.
#
# KEY CONCEPTS:
# - .startswith("y") returns True if the string begins with "y"
# - This accepts "y", "yes", "yeah", "yep", "yo", etc.
# - It's a creative solution but might be TOO permissive!
#
# HOW IT WORKS:
# 1. User enters "yeah"
# 2. .strip().lower() cleans it to "yeah"
# 3. "yeah".startswith("y") returns True
# 4. "Agreed" is printed
#
# STRING METHODS FOR CHECKING:
# - .startswith("x") - does the string start with "x"?
# - .endswith("x") - does the string end with "x"?
# - "x" in string - does the string contain "x"?
#
# TRADE-OFF:
# This approach is very flexible, but might accept unintended inputs.
# "yellow" and "yolo" would also match!
# Sometimes being too clever can introduce bugs.

answer = input("Do you agree? ").strip().lower()
if answer.startswith("y"):
    print("Agreed")
else:
    print("Not agreed")
