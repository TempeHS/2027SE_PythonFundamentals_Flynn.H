# Demonstrates defining a main function
#
# EXPLANATION:
# This program follows a best practice by using a main() function to organize code.
#
# KEY CONCEPTS:
# - main() is a conventional name for the function that starts your program
# - Python reads top to bottom, but doesn't RUN function code until you call it
# - This pattern lets you define helper functions anywhere in the file
# - The main() call at the bottom actually starts the program
#
# HOW IT WORKS:
# 1. Python reads def main(): - remembers it but doesn't run it yet
# 2. Python reads def hello(to="world"): - remembers it but doesn't run it yet
# 3. Python reaches main() at the bottom - NOW it runs the main function
# 4. main() asks for input and calls hello(name)
# 5. hello() prints the greeting
#
# WHY THIS PATTERN IS IMPORTANT:
# - Keeps code organized and professional
# - Makes it clear where your program starts
# - Lets you define helper functions before or after main()
# - Makes your code easier to test and reuse
#
# NOTE: In many programming languages (like C or Java), the program
# automatically starts at main(). In Python, you must explicitly call main()!
# Later, you'll learn about: if __name__ == "__main__": main()


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
