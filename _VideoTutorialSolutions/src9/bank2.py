# Uses global
#
# EXPLANATION:
# The 'global' keyword lets you MODIFY global variables!
#
# KEY CONCEPTS:
# - 'global balance' says "use the global balance"
# - Now balance += n modifies the global variable
# - Must declare global BEFORE using the variable
#
# HOW IT WORKS:
# def deposit(n):
#     global balance  # "I want the GLOBAL balance"
#     balance += n    # Now this works!
#
# WITHOUT 'GLOBAL':
# Python creates a new local variable (and fails).
#
# WITH 'GLOBAL':
# Python uses the existing global variable.
#
# WARNING:
# Global variables can make code hard to understand!
# The state can change from anywhere.
# See bank3.py for a better OOP approach!

balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
