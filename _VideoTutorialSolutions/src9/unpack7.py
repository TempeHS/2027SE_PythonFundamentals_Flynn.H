# Prints positional arguments
#
# EXPLANATION:
# *args captures any number of positional arguments!
#
# KEY CONCEPTS:
# - def f(*args): Accepts any number of positional args
# - args is a tuple of all values passed
# - **kwargs captures named arguments (shown next)
#
# THE FUNCTION:
# def f(*args, **kwargs):
#     print("Positional:", args)
#
# f(100, 50, 25)
# args = (100, 50, 25)  # Tuple of positional args
#
# USE CASES:
# - Functions that accept variable number of args
# - print() uses *args: print("a", "b", "c")
# - Wrapper functions that pass args through
#
# See unpack8.py for **kwargs!


def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)
