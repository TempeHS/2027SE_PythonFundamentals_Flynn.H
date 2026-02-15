# Incompatible types in assignment
#
# EXPLANATION:
# You can annotate VARIABLES, not just parameters!
#
# KEY CONCEPTS:
# - number: int = ... annotates the variable as int
# - But input() returns str, not int!
# - Type checker warns: "Incompatible types in assignment"
#
# THE PROBLEM:
# number: int = input(...)  # Says int, but gets str
#
# This makes the type mismatch more visible.
# The checker knows number should be int, but isn't.
#
# VARIABLE ANNOTATIONS:
# name: str = "Harry"
# age: int = 17
# gpa: float = 3.9
# is_wizard: bool = True
#
# See meows5.py for the fix - actually convert to int!


def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number)
