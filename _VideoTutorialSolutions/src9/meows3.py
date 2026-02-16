# Argument ... has incompatible type
#
# EXPLANATION:
# TYPE HINTS help catch errors before running!
#
# KEY CONCEPTS:
# - def meow(n: int): says n should be an integer
# - Type checker (like mypy) warns about wrong types
# - Catches errors at development time, not runtime
#
# THE TYPE HINT:
# def meow(n: int):  # n must be int
#
# THE WARNING:
# number = input(...)  # This is str
# meow(number)  # Warning: str passed where int expected
#
# TYPE CHECKERS:
# - mypy: Popular static type checker
# - Pylance: Built into VS Code
# - They analyze code WITHOUT running it!
#
# NOTE:
# Python itself ignores type hints at runtime.
# They're for tools and documentation.
#
# See meows4.py for annotating the variable too!


def meow(n: int):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)
