# Demonstrates IndexError
#
# EXPLANATION:
# This program handles the case when no argument is provided using try/except.
#
# KEY CONCEPTS:
# - IndexError occurs when you try to access an index that doesn't exist
# - try/except catches the error and shows a friendly message
# - This is called "exception handling" or "error handling"
#
# HOW IT WORKS:
# 1. try to access sys.argv[1]
# 2. If it exists, print the greeting
# 3. If IndexError (no argument), print "Too few arguments"
#
# EXAMPLE RUNS:
# python name1.py David -> "hello, my name is David"
# python name1.py       -> "Too few arguments"
#
# THIS VS CHECKING LENGTH:
# Exception handling: try it, catch the error if it fails
# Length checking: Check len(sys.argv) before accessing
#
# Both approaches are valid! See name2.py for the length-checking approach.
#
# EAFP VS LBYL:
# - EAFP: "Easier to Ask Forgiveness than Permission" (try/except)
# - LBYL: "Look Before You Leap" (check conditions first)
# Python culture often prefers EAFP, but both work.

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
