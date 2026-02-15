# Doesn't check __name__
#
# EXPLANATION:
# This module has a PROBLEM - it runs main() even when imported!
#
# KEY CONCEPTS:
# - This file defines functions AND calls main() at the end
# - When you run it directly: python sayings1.py -> works as expected
# - When you import it: from sayings1 import hello -> ALSO runs main()!
# - This is usually unintended behavior
#
# THE PROBLEM:
# When Python imports a module, it executes ALL the code in that file.
# The function definitions just create functions (good).
# But main() at the end actually runs (bad when importing!).
#
# EXAMPLE:
# from sayings1 import hello
# # This prints "hello, world" and "goodbye, world" as a side effect!
#
# THE FIX:
# See sayings2.py for the solution using __name__ == "__main__"
#
# REMEMBER:
# If your module file calls any functions at the top level,
# those calls will run whenever someone imports your module!


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


main()
