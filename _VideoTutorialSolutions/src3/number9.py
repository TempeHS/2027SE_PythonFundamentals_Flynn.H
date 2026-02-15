# Adds prompt
#
# EXPLANATION:
# This is the FINAL, most flexible version of get_int()!
#
# KEY CONCEPTS:
# - get_int(prompt) takes a parameter for the input prompt
# - This makes the function reusable for ANY integer input
# - The caller can customize the prompt for their needs
#
# HOW IT WORKS:
# 1. main() calls get_int("What's x? ")
# 2. get_int() uses the prompt when calling input()
# 3. Returns the valid integer
#
# FLEXIBILITY:
# You can now use get_int() for any integer input:
#   age = get_int("How old are you? ")
#   score = get_int("Enter your score: ")
#   count = get_int("How many items? ")
#
# THE COMPLETE GET_INT FUNCTION:
# This is a professional-quality utility function that:
# 1. Keeps asking until valid input
# 2. Handles errors gracefully
# 3. Is reusable with any prompt
#
# WHAT YOU'VE LEARNED (number0 to number9):
# 1. Exceptions crash your program (number0)
# 2. try/except catches exceptions (number1)
# 3. Be careful with variable scope (number2)
# 4. Use else for success-only code (number3)
# 5. Add loops for retry (number4)
# 6. Put it in a function (number5-7)
# 7. Use pass for silent handling (number8)
# 8. Add parameters for flexibility (number9)


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
