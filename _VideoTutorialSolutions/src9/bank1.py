# UnboundLocalError
#
# EXPLANATION:
# This demonstrates a common error when modifying globals!
#
# KEY CONCEPTS:
# - balance += n tries to MODIFY balance
# - Python thinks balance is LOCAL (because we're assigning)
# - But local balance doesn't exist yet!
# - Result: UnboundLocalError
#
# THE PROBLEM:
# When Python sees 'balance += n' it thinks:
# "balance is being assigned, so it must be local"
# But we never created a local balance first!
#
# WHY READING WORKS BUT WRITING DOESN'T:
# - Reading global: Python looks up in global scope
# - Writing: Python assumes you mean a new local variable
#
# See bank2.py for the 'global' keyword solution!

balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    balance += n


def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()
