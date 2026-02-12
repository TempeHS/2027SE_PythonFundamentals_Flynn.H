# Demonstrates a function with a positional argument and a named argument
#
# EXPLANATION:
# This program introduces "named arguments" (also called "keyword arguments").
#
# KEY CONCEPTS:
# - A "named argument" uses the syntax: parameter_name=value
# - end="" is a named argument that controls what print() adds at the end
# - By default, print() adds a newline character (\n) at the end
# - Setting end="" means "add nothing at the end" - so the next print continues on same line
#
# HOW IT WORKS:
# 1. First print() outputs "hello, " but doesn't move to a new line (because of end="")
# 2. Second print() outputs the name, continuing on the same line
# 3. Result: "hello, David" appears all on one line
#
# NAMED VS POSITIONAL ARGUMENTS:
# - Positional: print("hello") - the value's position determines which parameter it fills
# - Named: print("hello", end="") - you explicitly name which parameter gets the value
#
# Named arguments must come AFTER positional arguments in a function call.

name = input("What's your name? ")
print("hello, ", end="")
print(name)
