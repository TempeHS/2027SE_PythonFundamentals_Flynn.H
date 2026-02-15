# Success
#
# EXPLANATION:
# Convert the input to match the expected type!
#
# KEY CONCEPTS:
# - int(input(...)) converts string to integer
# - number: int = int(...) now actually IS an int
# - No more type errors!
#
# THE FIX:
# number: int = int(input("Number: "))
#               ^-- Convert to int
#
# Type hint ----^     ^---- Actual conversion
#
# BOTH ARE NEEDED:
# - Type hint: Documents intent, enables checking
# - Conversion: Actually changes the type at runtime
#
# NOW EVERYTHING MATCHES:
# number is int ✓
# meow(n: int) expects int ✓
# range(n) gets int ✓


def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meow(number)
