# Uses class
#
# EXPLANATION:
# Classes are a BETTER way to manage state than globals!
#
# KEY CONCEPTS:
# - Account class encapsulates balance and operations
# - self._balance is per-instance (not global)
# - Methods modify the instance's own balance
# - @property provides read-only access
#
# WHY CLASSES ARE BETTER:
# 1. No global state - each Account has its own balance
# 2. Multiple accounts possible: potter = Account(), weasley = Account()
# 3. Encapsulation - balance is protected (_balance)
# 4. Methods keep related code together
#
# COMPARE:
# Global approach: One balance, accessible everywhere
# Class approach: Each account has its own balance
#
# REAL-WORLD:
# Banks have millions of accounts - classes model this well!
# Each Account object is independent.


class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
