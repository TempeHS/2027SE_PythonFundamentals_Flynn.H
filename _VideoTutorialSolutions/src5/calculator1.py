# Demonstrates defining a function with a return value
#
# EXPLANATION:
# This calculator can be safely imported for testing!
#
# KEY CONCEPTS:
# - if __name__ == "__main__" prevents main() from running on import
# - When run directly: python calculator1.py -> runs main()
# - When imported: from calculator1 import square -> does NOT run main()
# - This is essential for unit testing
#
# HOW IT WORKS:
# 1. Define square(n) that returns n * n
# 2. Define main() that uses square()
# 3. Only call main() if this file is the main program
#
# WHY THIS MATTERS FOR TESTING:
# test_calculator1.py does: from calculator1 import square
# This imports ONLY the square function, without triggering input()
# Then it can test: assert square(2) == 4
#
# See test_calculator1.py for the test file that tests this!


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
