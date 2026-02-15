# Annotates return value, ... does not return a value
#
# EXPLANATION:
# You can annotate RETURN TYPES too!
#
# KEY CONCEPTS:
# - def meow(n: int) -> None: says it returns None
# - -> None indicates no meaningful return value
# - Now type checker warns: assigning None to str!
#
# RETURN TYPE SYNTAX:
# def function(param: type) -> return_type:
#     ...
#
# COMMON RETURN TYPES:
# -> None: Function doesn't return anything useful
# -> str: Returns a string
# -> int: Returns an integer
# -> list[str]: Returns list of strings
# -> bool: Returns True or False
#
# THE WARNING:
# meows: str = meow(number)  # Error: None assigned to str
#
# See meows8.py for actually returning a string!


def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
