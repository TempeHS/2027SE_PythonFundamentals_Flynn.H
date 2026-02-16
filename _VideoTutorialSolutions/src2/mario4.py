# Prints row of coins using a function with str multiplication
#
# EXPLANATION:
# This program prints a HORIZONTAL row of coins (? blocks in Mario).
#
# KEY CONCEPTS:
# - "?" * width creates a string of question marks
# - "?" * 4 creates "????"
# - print() adds a newline at the end automatically
# - No end="" needed because we want the default newline
#
# HOW IT WORKS:
# 1. "?" * 4 creates "????"
# 2. print("????") displays it with a newline
#
# OUTPUT:
# ????
#
# COMPARISON TO COLUMNS:
# Column (vertical): Print one character, then newline, repeat
# Row (horizontal): Print many characters, then one newline
#
# STRING MULTIPLICATION IS PERFECT FOR ROWS:
# No need for a loop when you just want to repeat a character horizontally.
# "?" * width is simple and clear.


def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()
