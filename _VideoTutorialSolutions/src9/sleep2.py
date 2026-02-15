# Returns n sheep from helper function
#
# EXPLANATION:
# Breaking code into small helper functions!
#
# KEY CONCEPTS:
# - sheep(n) returns a string of n sheep
# - main() uses the helper function
# - Each function does ONE thing
#
# THE HELPER:
# def sheep(n):
#     return "🐑" * n
#
# Simple, reusable, easy to understand.
#
# FUNCTION DECOMPOSITION:
# - Break big problems into small functions
# - Each function has one responsibility
# - Easier to test, read, and maintain
#
# See sleep3.py for returning a list of sheep!


def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))


def sheep(n):
    return "🐑" * n


if __name__ == "__main__":
    main()
