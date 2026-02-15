# Uses map
#
# EXPLANATION:
# map() applies a function to every item in a sequence!
#
# KEY CONCEPTS:
# - map(function, iterable): Apply function to each item
# - str.upper: The function to apply (without ()!)
# - Returns map object (iterator)
#
# THE CODE:
# uppercased = map(str.upper, words)
#
# EQUIVALENT TO:
# uppercased = []
# for word in words:
#     uppercased.append(str.upper(word))  # Same as word.upper()
#
# FUNCTIONAL STYLE:
# map() is a functional programming approach.
# No explicit loop - just "apply this to each".
#
# STR.UPPER VS WORD.UPPER():
# str.upper(word) is same as word.upper()
# str.upper is the unbound method - can pass to map.
#
# See yell4.py for list comprehension alternative!


def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
