# Implements a bank account
#
# EXPLANATION:
# This introduces GLOBAL VARIABLES - variables defined outside functions.
#
# KEY CONCEPTS:
# - 'balance = 0' is a global variable (at module level)
# - Global variables can be READ from any function
# - Printing balance inside main() works!
#
# SCOPE:
# - Global scope: Accessible everywhere in the file
# - Local scope: Only inside a function
#
# This works because we're only READING balance.
# See bank1.py for what happens when we try to MODIFY it!

balance = 0


def main():
    print("Balance:", balance)


if __name__ == "__main__":
    main()
