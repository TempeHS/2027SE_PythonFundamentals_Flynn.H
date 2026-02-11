# Demonstrates defining a function with a return value
#
# EXPLANATION:
# This program creates a function that RETURNS a value instead of just printing.
#
# KEY CONCEPTS:
# - The 'return' keyword sends a value back to whoever called the function
# - square(4) doesn't just print 16 - it "becomes" 16 where it's called
# - The returned value can be stored in a variable, used in expressions, or printed
# - This makes functions reusable in many different contexts
#
# HOW IT WORKS:
# 1. main() is called at the bottom
# 2. User enters 4 for x
# 3. square(x) is called, passing 4 as the argument
# 4. In square(), n = 4, and 4 * 4 = 16
# 5. 'return 16' sends 16 back to main()
# 6. print("x squared is", 16) outputs: x squared is 16
#
# RETURN VS PRINT:
# - print() displays output to the screen (for humans to see)
# - return sends a value back to the code (for the program to use)
#
# Example:
#   def add(a, b):
#       return a + b
#
#   result = add(2, 3)  # result is now 5
#   print(result * 2)   # prints 10
#
# If add() used print() instead of return, we couldn't do math with its result!
#
# NOTE: A function without 'return' (or with just 'return') returns None.


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
