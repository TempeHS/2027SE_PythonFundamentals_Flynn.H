# Demonstrates defining a function with a parameter
#
# EXPLANATION:
# This program creates a function that accepts input (a parameter).
#
# KEY CONCEPTS:
# - A "parameter" is a variable defined in a function's parentheses: def hello(to)
# - When you call the function, you pass an "argument" that fills the parameter
# - The parameter 'to' receives whatever value is passed when hello() is called
# - Inside the function, 'to' can be used like any other variable
#
# HOW IT WORKS:
# 1. def hello(to): defines a function with one parameter named 'to'
# 2. User enters their name, stored in 'name'
# 3. hello(name) is called - the value of 'name' is passed to the function
# 4. Inside hello(), 'to' now contains the user's name
# 5. print("hello,", to) outputs the greeting
#
# PARAMETER VS ARGUMENT:
# - Parameter: The variable in the function definition (to)
# - Argument: The actual value passed when calling the function (name)
# These terms are often used interchangeably, but there is a subtle difference.
#
# This is more flexible than hello8.py because now the function can greet
# anyone, not just print a fixed message!


def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)
