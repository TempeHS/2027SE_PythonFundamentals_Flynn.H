# Uses yield
#
# EXPLANATION:
# GENERATORS produce values one at a time!
#
# KEY CONCEPTS:
# - yield instead of return: Makes function a generator
# - Values produced on demand, not all at once
# - Memory efficient for large sequences
#
# THE GENERATOR:
# def sheep(n):
#     for i in range(n):
#         yield "🐑" * i
#
# YIELD VS RETURN:
# - return: Exits function, gives all data at once
# - yield: Pauses function, gives one value, continues
#
# HOW IT WORKS:
# for s in sheep(n):
#     print(s)
#
# Each iteration calls sheep() and gets next yield.
# No big list in memory - just one item at a time!
#
# WHEN TO USE:
# - Large or infinite sequences
# - When you don't need all items at once
# - Reading files line by line


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
