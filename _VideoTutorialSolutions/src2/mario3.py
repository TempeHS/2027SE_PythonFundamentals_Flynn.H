# Prints column of bricks using a function with str multiplication
#
# EXPLANATION:
# This program uses string multiplication as a clever alternative.
#
# KEY CONCEPTS:
# - "#\n" * height creates a string with 'height' copies of "#\n"
# - \n is the newline character
# - end="" prevents print from adding an extra newline
#
# HOW IT WORKS:
# 1. "#\n" * 3 creates "#\n#\n#\n"
# 2. print() displays this string
# 3. end="" prevents the default newline (we already have 3)
#
# OUTPUT:
# #
# #
# #
#
# LOOP VS STRING MULTIPLICATION:
# Loop approach (mario2.py):
#   for _ in range(height):
#       print("#")
#
# String multiplication (this file):
#   print("#\n" * height, end="")
#
# Both produce the same output! The string multiplication is more
# compact, but the loop is often clearer for beginners.


def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="")


main()
