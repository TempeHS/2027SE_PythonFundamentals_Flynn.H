# Removes break
#
# EXPLANATION:
# This program simplifies get_int() by using return directly in the else block.
#
# KEY CONCEPTS:
# - 'return x' both exits the function AND returns the value
# - No need for break when return does both jobs!
# - return immediately exits the function (and the loop)
#
# HOW IT WORKS:
# 1. Loop starts
# 2. try to convert input
# 3. If ValueError: print error, loop continues
# 4. If success: else block runs, return x exits function with value
#
# COMPARISON:
# Before (number5.py):
#     else:
#         break
#     return x
#
# After (this file):
#     else:
#         return x
#
# The second version is cleaner - return does the job of both break and return!
#
# RETURN VS BREAK:
# - break: Exits the loop, function continues
# - return: Exits the function immediately (and any loops in it)
#
# See number7.py for an even cleaner version!


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()
