# Function to be tested
#
# EXPLANATION:
# This program has a hello() function that PRINTS instead of returning.
#
# KEY CONCEPTS:
# - Functions that print are HARD to test automatically
# - We can't easily check what was printed
# - For testing, functions should RETURN values instead
# - This is why hello1.py changes to return a string
#
# THE PROBLEM:
# hello("David") prints "hello, David" to the screen
# But how do we write a test to check if that's correct?
# We'd need to capture the printed output - it's complicated!
#
# THE SOLUTION:
# Change hello() to RETURN the string instead of printing it.
# Then our test can easily check: assert hello("David") == "hello, David"
#
# DEFAULT PARAMETERS:
# hello(to="world") means:
# - hello() with no argument -> uses "world"
# - hello("David") -> uses "David"
#
# This version is harder to test. See hello1.py for the testable version!


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()
