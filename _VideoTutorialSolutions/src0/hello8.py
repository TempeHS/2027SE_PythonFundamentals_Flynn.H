# Demonstrates defining a function without parameters
#
# EXPLANATION:
# This program shows how to create your own function - a reusable block of code.
#
# KEY CONCEPTS:
# - 'def' is the keyword used to define (create) a function
# - The function name follows 'def' (in this case, 'hello')
# - Empty parentheses () mean the function takes no parameters (no inputs)
# - The colon : marks the start of the function's body
# - The indented code below is the function's body - what it does when called
# - To use the function, you "call" it by writing its name with parentheses: hello()
#
# HOW IT WORKS:
# 1. Python reads the 'def' statement and remembers the hello function
# 2. User enters their name
# 3. hello() is called, which prints "hello"
# 4. print(name) prints the user's name
#
# WHY CREATE FUNCTIONS:
# - Reusability: Write code once, use it many times
# - Organization: Break complex programs into smaller, manageable pieces
# - Readability: Give meaningful names to blocks of code
#
# NOTE: This output appears on two lines because hello() and print(name)
# are two separate print operations.


def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
