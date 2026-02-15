# Adds a loop
#
# EXPLANATION:
# This program keeps asking until the user enters a valid number.
#
# KEY CONCEPTS:
# - while True: creates an infinite loop
# - The loop keeps asking until we get valid input
# - 'break' exits the loop when input is valid
# - This pattern is called "input validation"
#
# HOW IT WORKS:
# 1. while True starts an infinite loop
# 2. try to convert input to int
# 3. If ValueError: print error and loop continues (ask again)
# 4. If no error: else block runs, break exits the loop
# 5. After the loop, x is guaranteed to be a valid integer
#
# EXAMPLE RUN:
# What's x? cat
# x is not an integer
# What's x? dog
# x is not an integer
# What's x? 42
# x is 42
#
# INPUT VALIDATION PATTERN:
# while True:
#     try:
#         get input
#     except:
#         show error
#     else:
#         break (input is valid)
#
# This is a robust pattern for getting valid input from users!

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
