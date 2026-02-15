# Demonstrates defining functions
#
# EXPLANATION:
# This program organizes the cat code into well-designed functions.
#
# KEY CONCEPTS:
# - Breaking code into functions makes it more organized and reusable
# - main() is the entry point that controls the overall flow
# - get_number() handles getting valid input from the user
# - meow(n) handles the meowing logic
# - Each function has ONE job (this is called "separation of concerns")
#
# HOW IT WORKS:
# 1. main() is called
# 2. main() calls get_number(), which returns a valid number
# 3. That number is passed directly to meow()
# 4. meow(n) prints "meow" n times
#
# GET_NUMBER() EXPLAINED:
# - Uses while True: for infinite loop
# - Uses 'return' instead of 'break' to exit AND return the value
# - 'return n' both exits the function and gives back the value
# - Much cleaner than using break and a separate variable!
#
# FUNCTION DESIGN PRINCIPLES:
# 1. Each function should do ONE thing well
# 2. Function names should describe what they do
# 3. Functions should be reusable in other contexts
#
# MAIN FUNCTION:
# Putting the main logic in main() makes the code structure clear
# and allows you to control when the program starts.


def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
