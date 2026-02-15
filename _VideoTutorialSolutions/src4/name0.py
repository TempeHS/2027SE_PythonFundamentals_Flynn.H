# Demonstrates sys.argv
#
# EXPLANATION:
# This program reads command-line arguments using sys.argv.
#
# KEY CONCEPTS:
# - sys.argv is a list containing command-line arguments
# - sys.argv[0] is always the script name
# - sys.argv[1] is the first user-provided argument
# - Command-line arguments let users pass data when running the program
#
# HOW TO RUN:
# python name0.py David
# Output: hello, my name is David
#
# SYS.ARGV BREAKDOWN:
# For: python name0.py David
# - sys.argv[0] = "name0.py"
# - sys.argv[1] = "David"
#
# THE PROBLEM:
# If you run: python name0.py
# (without a name), you get an IndexError because sys.argv[1] doesn't exist!
#
# See name1.py for how to handle this error.
#
# WHY USE COMMAND-LINE ARGUMENTS?
# - Automation: Scripts can be run with different inputs
# - Integration: Other programs can call your script with arguments
# - Convenience: No need to edit code to change inputs

import sys

print("hello, my name is", sys.argv[1])
