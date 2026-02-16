# Check __name__
#
# EXPLANATION:
# This is the CORRECT way to create a module that can also run as a script!
#
# KEY CONCEPTS:
# - if __name__ == "__main__": checks HOW the file is being used
# - When run directly: __name__ is "__main__" -> run main()
# - When imported: __name__ is "sayings2" -> don't run main()
# - This is a standard Python pattern!
#
# HOW __NAME__ WORKS:
# Every Python file has a special variable called __name__
# - If you run the file directly: __name__ == "__main__"
# - If you import the file: __name__ == the module name
#
# EXAMPLES:
# python sayings2.py -> __name__ is "__main__" -> runs main()
# from sayings2 import hello -> __name__ is "sayings2" -> skips main()
#
# WHY THIS MATTERS:
# Your file can be BOTH:
# 1. A standalone program (python sayings2.py)
# 2. A reusable module (from sayings2 import hello)
#
# BEST PRACTICE:
# Always use this pattern when your module has a main() function!
# It's one of the most common patterns in Python.


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()
