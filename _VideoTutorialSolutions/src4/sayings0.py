# A simple module with hello and goodbye functions
#
# EXPLANATION:
# This is a simple MODULE - a file that defines functions for other files to use.
#
# KEY CONCEPTS:
# - This file defines two functions: hello() and goodbye()
# - It doesn't call any functions - just defines them
# - Other files can: from sayings0 import hello, goodbye
# - This is the simplest form of a reusable module
#
# MODULE STRUCTURE:
# - Just function definitions
# - No main() function
# - No code that runs on import
#
# HOW TO USE:
# from sayings0 import hello
# hello("David")  # prints: hello, David
#
# WHY THIS WORKS:
# When Python imports this file, it defines the functions
# but doesn't execute anything. The functions just become
# available for the importing file to use.
#
# This is the most basic module pattern - just definitions!


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")
