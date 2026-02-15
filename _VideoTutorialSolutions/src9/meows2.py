# Demonstrates TypeError
#
# EXPLANATION:
# This shows what happens with wrong types at RUNTIME!
#
# KEY CONCEPTS:
# - input() returns a STRING
# - range() needs an INTEGER
# - Passing string to range() causes TypeError
#
# THE PROBLEM:
# number = input("Number: ")  # Returns "3" (string)
# range(number)  # Error! range() needs int, not str
#
# TypeError:
# "'str' object cannot be interpreted as an integer"
#
# RUNTIME VS DEVELOPMENT:
# - This error happens when you RUN the program
# - Python doesn't catch it until execution
# - Type hints can warn you earlier!
#
# See meows3.py for type hints!


def meow(n):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)
