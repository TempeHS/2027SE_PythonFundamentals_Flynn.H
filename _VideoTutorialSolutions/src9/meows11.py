# Uses command-line argument
#
# EXPLANATION:
# Programs can accept arguments from the command line!
#
# KEY CONCEPTS:
# - sys.argv: List of command-line arguments
# - sys.argv[0]: The script name
# - sys.argv[1]: First argument, sys.argv[2]: second, etc.
# - len(sys.argv): Number of arguments
#
# USAGE:
# python meows11.py -n 3
# sys.argv = ["meows11.py", "-n", "3"]
#
# THE LOGIC:
# - len == 1: No args, just meow once
# - len == 3 and argv[1] == "-n": Use argv[2] as count
# - else: Print usage message
#
# MANUAL PARSING:
# This manually checks arguments.
# It works but gets complex with many options.
#
# See meows12.py for argparse - automatic argument parsing!

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows11.py [-n NUMBER]")
