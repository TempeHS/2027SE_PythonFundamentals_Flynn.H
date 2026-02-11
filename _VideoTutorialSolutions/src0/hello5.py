# Demonstrates a format string
#
# EXPLANATION:
# This program uses an "f-string" (formatted string literal) - the preferred
# modern way to include variables inside strings in Python.
#
# KEY CONCEPTS:
# - An f-string starts with the letter 'f' before the opening quote: f"..."
# - Inside an f-string, you can put variables in curly braces: {variable_name}
# - Python automatically replaces {name} with the actual value of the variable
# - This is cleaner and more readable than concatenation with +
#
# HOW IT WORKS:
# 1. User enters their name (e.g., "David")
# 2. In f"hello, {name}", Python substitutes {name} with "David"
# 3. The result "hello, David" is printed
#
# WHY F-STRINGS ARE GREAT:
# - More readable: f"hello, {name}" vs "hello, " + name
# - Can include expressions: f"2 + 2 = {2 + 2}" prints "2 + 2 = 4"
# - Can format values: f"{price:.2f}" formats price to 2 decimal places
#
# NOTE: F-strings were introduced in Python 3.6 and are now the standard way
# to format strings.

name = input("What's your name? ")
print(f"hello, {name}")
