# Demonstrates defining a function with a parameter with a default value
#
# EXPLANATION:
# This program shows how to give a function parameter a default value.
#
# KEY CONCEPTS:
# - A default value is set using = in the parameter list: def hello(to="world")
# - If you call hello() without an argument, 'to' automatically gets "world"
# - If you call hello(name), the argument overrides the default value
# - Default values make functions more flexible and easier to use
#
# HOW IT WORKS:
# 1. def hello(to="world"): creates a function with a default parameter
# 2. hello() is called without arguments - 'to' becomes "world" -> prints "hello, world"
# 3. User enters their name
# 4. hello(name) is called with an argument - 'to' becomes the user's name
#
# WHY USE DEFAULT VALUES:
# - Makes functions easier to call (fewer required arguments)
# - Provides sensible default behavior
# - The built-in print() function uses this: print("hi", end="\n")
#   The default end is "\n" (newline), but you can override it with end=""
#
# RULES FOR DEFAULT PARAMETERS:
# Parameters with default values must come AFTER parameters without defaults.
# def greet(greeting, name="friend")  <- Valid
# def greet(name="friend", greeting)  <- Invalid!


def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)
