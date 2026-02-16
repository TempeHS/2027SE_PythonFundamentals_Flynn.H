# Prints a word in uppercase
#
# EXPLANATION:
# Simple function to convert text to uppercase.
#
# KEY CONCEPTS:
# - word.upper() returns uppercase version
# - Strings are immutable - upper() returns new string
# - yell() takes a single string
#
# THE FUNCTION:
# def yell(word):
#     print(word.upper())
#
# yell("hello") prints "HELLO"
#
# LIMITATION:
# Takes only ONE string.
# What if we want: yell("This", "is", "CS50")?
#
# See yell1.py for handling a list of words!


def main():
    yell("This is CS50")


def yell(word):
    print(word.upper())


if __name__ == "__main__":
    main()
