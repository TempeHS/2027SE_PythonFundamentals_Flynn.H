# Prints named arguments
#
# EXPLANATION:
# **kwargs captures any number of keyword arguments!
#
# KEY CONCEPTS:
# - def f(**kwargs): Accepts any number of named args
# - kwargs is a dict of name=value pairs
# - Can use with *args for ultimate flexibility
#
# THE FUNCTION:
# def f(*args, **kwargs):
#     print("Named:", kwargs)
#
# f(galleons=100, sickles=50, knuts=25)
# kwargs = {"galleons": 100, "sickles": 50, "knuts": 25}
#
# *ARGS AND **KWARGS TOGETHER:
# def f(*args, **kwargs):
#     # args: tuple of positional arguments
#     # kwargs: dict of keyword arguments
#
# This is how many library functions accept any arguments!


def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)
