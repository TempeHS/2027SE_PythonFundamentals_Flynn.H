# Prints arbitrarily many args in uppercase
#
# EXPLANATION:
# *args lets the function accept any number of arguments!
#
# KEY CONCEPTS:
# - def yell(*words): Accepts any number of args
# - words is a tuple of all arguments
# - Caller writes: yell("This", "is", "CS50")
#
# THE FUNCTION:
# def yell(*words):  # Note the *
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)
#
# COMPARISON:
# yell(["This", "is", "CS50"])  # List version
# yell("This", "is", "CS50")    # *args version - cleaner!
#
# See yell3.py for using map() instead of loop!


def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
