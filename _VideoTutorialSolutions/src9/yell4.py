# Uses list comprehension
#
# EXPLANATION:
# List comprehension is often more readable than map()!
#
# KEY CONCEPTS:
# - [expression for item in iterable]
# - [arg.upper() for arg in words]
# - Pythonic and clear!
#
# THE CODE:
# uppercased = [arg.upper() for arg in words]
#
# COMPARISON OF APPROACHES:
# 1. Loop: Build list with append (verbose)
# 2. map(): Functional style (needs function reference)
# 3. Comprehension: Clear and Pythonic (preferred!)
#
# WHICH TO USE:
# - Simple transformations: List comprehension
# - Already have a function: map() can be cleaner
# - Complex logic: Explicit loop
#
# All three produce the same result!


def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
