# Has function return a str instead
#
# EXPLANATION:
# This version is designed to be TESTABLE - hello() returns a string!
#
# KEY CONCEPTS:
# - Functions that RETURN values are easy to test
# - Tests can check: assert hello("David") == "hello, David"
# - main() handles the printing; hello() just creates the string
# - This separation of concerns makes code more testable
#
# COMPARISON:
# hello0.py: hello() prints directly -> hard to test
# hello1.py: hello() returns a string -> easy to test!
#
# HOW IT WORKS:
# 1. main() gets the name from the user
# 2. hello(name) returns the greeting string
# 3. print() displays it
#
# WHY RETURN IS BETTER FOR TESTING:
# - We can call hello("David") and check the result
# - No need to capture printed output
# - The function becomes more flexible (caller decides what to do)
#
# This is a key insight for writing testable code:
# Separate the "logic" (creating data) from "side effects" (printing, saving).


def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
