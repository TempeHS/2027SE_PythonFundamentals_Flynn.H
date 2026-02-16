# Adds docstring to function.
#
# EXPLANATION:
# DOCSTRINGS document what functions do!
#
# KEY CONCEPTS:
# - """Triple quotes""" right after def line
# - Describes what the function does
# - Accessible via help(function) or function.__doc__
#
# THE DOCSTRING:
# def meow(n):
#     """Meow n times."""
#     return "meow\n" * n
#
# Simple one-line docstring describes the purpose.
#
# VIEWING DOCSTRINGS:
# help(meow)  # Shows the docstring
# meow.__doc__  # Returns "Meow n times."
#
# IDEs show docstrings when you hover over functions!
#
# See meows10.py for more detailed docstring format!


def meow(n):
    """Meow n times."""
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")
