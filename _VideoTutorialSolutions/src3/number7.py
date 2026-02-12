# Removes else
#
# EXPLANATION:
# This is the cleanest version - return the result directly from try!
#
# KEY CONCEPTS:
# - If int() succeeds, return the result immediately
# - If int() fails, the except block runs and the loop continues
# - No need for 'else' when we return directly from try
#
# HOW IT WORKS:
# 1. Try to return int(input(...))
# 2. If int() succeeds, return exits the function with the value
# 3. If int() fails, ValueError is raised
# 4. except block runs (prints error)
# 5. Loop continues, asks again
#
# THE PATTERN:
# while True:
#     try:
#         return <risky operation>
#     except:
#         <handle error>
#
# This is very clean: "keep trying until it works, then return the result"
#
# WHY THIS WORKS:
# return int(input(...)) does three things:
# 1. Gets input
# 2. Converts to int
# 3. Returns the result
#
# If step 2 fails, we never reach the return, so the function doesn't exit.


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


main()
