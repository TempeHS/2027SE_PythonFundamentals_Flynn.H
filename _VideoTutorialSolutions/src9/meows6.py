# Prints None because mistakes meow as having a return value
#
# EXPLANATION:
# Functions without 'return' return None!
#
# KEY CONCEPTS:
# - meow(n) prints but doesn't return anything
# - meows: str = meow(number) captures None
# - print(meows) prints None
#
# THE PROBLEM:
# def meow(n: int):       # No return statement
#     for _ in range(n):
#         print("meow")
#
# meows: str = meow(3)  # meows is None, not a string!
#
# TYPE MISMATCH:
# We said meows: str, but meow returns None.
# Type checker could warn about this!
#
# See meows7.py for return type annotations!


def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
