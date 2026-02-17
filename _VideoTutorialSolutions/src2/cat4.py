# Demonstrates (more succinct) incrementation
#
# EXPLANATION:
# This program introduces the += operator - a shorthand for incrementing.
#
# KEY CONCEPTS:
# - i += 1 is shorthand for i = i + 1
# - This is called the "augmented assignment operator"
# - It's shorter, cleaner, and less error-prone
# - Most programmers prefer this style
#
# AUGMENTED ASSIGNMENT OPERATORS:
# - i += 1  is the same as  i = i + 1
# - i -= 1  is the same as  i = i - 1
# - i *= 2  is the same as  i = i * 2
# - i /= 2  is the same as  i = i / 2
#
# WHY USE +=?
# 1. Less typing
# 2. Clearer intent (you're modifying i, not creating something new)
# 3. Less error-prone (you can't accidentally use wrong variable)
#
# NO ++ IN PYTHON!
# Some languages (like C, Java) have i++ for incrementing.
# Python doesn't! Use i += 1 instead.
# i++ will cause a SyntaxError in Python.

i = 0
while i < 3:
    print("meow")
    i += 1
