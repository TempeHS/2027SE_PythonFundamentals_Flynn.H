# Passes a list
#
# EXPLANATION:
# Pass a LIST of words to uppercase them all!
#
# KEY CONCEPTS:
# - yell(["This", "is", "CS50"]): Pass list as one argument
# - Loop through list, uppercase each word
# - Build new list of uppercased words
#
# THE FUNCTION:
# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)
#
# PRINT WITH *:
# print(*uppercased) unpacks the list.
# Prints: "THIS IS CS50" (space-separated)
# Without *: Prints ["THIS", "IS", "CS50"] (as list)
#
# LIMITATION:
# Caller must pass a list.
# See yell2.py for accepting multiple arguments directly!


def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
