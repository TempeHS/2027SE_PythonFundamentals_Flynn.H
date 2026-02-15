# Uses |
#
# EXPLANATION:
# This program combines multiple match patterns using the | (pipe) operator.
#
# KEY CONCEPTS:
# - In match/case, the | symbol means "or"
# - case "Harry" | "Hermione" | "Ron": matches any of these three names
# - This is like using 'or' in an if statement
# - Much cleaner than repeating the same code for each case!
#
# HOW IT WORKS:
# 1. User enters "Ron"
# 2. Python checks: Does "Ron" match "Harry" | "Hermione" | "Ron"?
# 3. Yes! "Gryffindor" is printed
#
# | IN MATCH VS 'OR' IN IF:
# Match statement: case "a" | "b" | "c":
# If statement: if x == "a" or x == "b" or x == "c":
#
# The match version is shorter and more readable!
#
# THE FINAL CLEAN VERSION:
# This is the most elegant solution for this problem:
# - Uses match/case for clear structure
# - Groups related cases with |
# - Uses _ for the default case

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
