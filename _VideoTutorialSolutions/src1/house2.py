# Uses match with case
#
# EXPLANATION:
# This program introduces Python's match/case statement (added in Python 3.10).
#
# KEY CONCEPTS:
# - 'match' is like a switch statement in other languages
# - Each 'case' checks if the value matches a specific pattern
# - 'case _:' is the default case (like else) - the underscore _ matches anything
# - match/case can be cleaner than if/elif/else for multiple comparisons
#
# HOW IT WORKS:
# 1. User enters "Harry"
# 2. Python matches 'name' against each case
# 3. case "Harry": matches! "Gryffindor" is printed
# 4. Python exits the match block (doesn't check remaining cases)
#
# MATCH VS IF/ELIF:
# match is often cleaner when comparing ONE variable against MULTIPLE values.
# if/elif is more flexible for complex conditions.
#
# THE _ (UNDERSCORE) PATTERN:
# - case _: matches ANYTHING - it's the catch-all/default
# - This is like 'else' in an if/elif chain
# - Always put it last, or earlier cases won't be reached!
#
# NOTE: match/case requires Python 3.10 or newer.
# Older versions will give a SyntaxError.

name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
