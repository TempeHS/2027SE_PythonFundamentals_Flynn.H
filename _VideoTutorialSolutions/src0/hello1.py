# Demonstrates a function with a positional argument and a return value
#
# EXPLANATION:
# This program asks for the user's name and then greets them.
#
# KEY CONCEPTS:
# - input() is a function that pauses the program and waits for user to type something
# - input() has a "return value" - it gives back whatever the user typed
# - A "variable" (like 'name') stores data so we can use it later
# - The = sign is the "assignment operator" - it stores a value in a variable
#
# HOW IT WORKS:
# 1. input() displays the prompt "What's your name? " and waits
# 2. When the user types something and presses Enter, input() returns that text
# 3. The returned text is stored in the variable called 'name'
# 4. Two separate print() calls display "hello," and then the name on different lines
#
# NOTE: This prints on two lines because each print() starts a new line by default.

name = input("What's your name? ")
print("hello,")
print(name)
