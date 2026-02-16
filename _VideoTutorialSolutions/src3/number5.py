# Adds functions, uses break and return
#
# EXPLANATION:
# This program creates a reusable get_int() function for input validation.
#
# KEY CONCEPTS:
# - get_int() encapsulates the input validation logic
# - It returns the valid integer when found
# - main() just uses get_int() without knowing the details
# - This is called "abstraction" - hiding complexity in functions
#
# HOW IT WORKS:
# 1. main() calls get_int()
# 2. get_int() loops until valid input
# 3. On success: break exits the loop, return x gives back the value
# 4. main() receives the valid integer and prints it
#
# FUNCTION STRUCTURE:
# def get_int():
#     while True:
#         try: ...
#         except: ...
#         else: break
#     return x
#
# WHY CREATE GET_INT()?
# - Reusability: Call get_int() anywhere you need an integer
# - Clean main(): main() just shows the high-level logic
# - Testability: You could test get_int() separately
#
# NOTE:
# This uses both break AND return. But we can simplify!
# See number6.py for a cleaner version.


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
            break
    return x


main()
