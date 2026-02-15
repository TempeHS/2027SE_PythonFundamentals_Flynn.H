# Returns a list of sheep
#
# EXPLANATION:
# Return all results at once in a list!
#
# KEY CONCEPTS:
# - sheep(n) returns a LIST of strings
# - Build list with append(), return at end
# - Caller can iterate over the result
#
# THE FUNCTION:
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock
#
# Creates entire list in memory, then returns it.
#
# MEMORY:
# For large n, the entire list is in memory.
# What if n is 1 million? That's a lot of sheep!
#
# See sleep4.py for GENERATORS - memory efficient!


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
