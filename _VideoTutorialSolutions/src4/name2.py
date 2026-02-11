# Adds error checking
#
# EXPLANATION:
# This program validates argument count before using sys.argv.
#
# KEY CONCEPTS:
# - len(sys.argv) tells you how many arguments were provided
# - Check the length before accessing specific indices
# - This prevents IndexError by checking first
#
# HOW IT WORKS:
# - len(sys.argv) < 2: No name provided (only script name)
# - len(sys.argv) > 2: Too many arguments provided
# - len(sys.argv) == 2: Exactly one name, which is correct!
#
# ARGUMENT COUNTING:
# Command: python name2.py David
# len(sys.argv) = 2 (["name2.py", "David"])
#
# Command: python name2.py David Malan
# len(sys.argv) = 3 (["name2.py", "David", "Malan"]) <- too many!
#
# EXAMPLE RUNS:
# python name2.py         -> "Too few arguments"
# python name2.py David   -> "hello, my name is David"
# python name2.py A B     -> "Too many arguments"
#
# This is the "Look Before You Leap" (LBYL) approach -
# check conditions before attempting the operation.

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
