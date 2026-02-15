# Demonstrates sys.exit
#
# EXPLANATION:
# This program uses sys.exit() to stop the program with an error message.
#
# KEY CONCEPTS:
# - sys.exit() immediately stops the program
# - sys.exit("message") prints the message and exits
# - This is useful for "guard clauses" - check errors at the start
# - The main logic is only reached if all checks pass
#
# HOW IT WORKS:
# 1. Check if too few arguments -> exit with message
# 2. Check if too many arguments -> exit with message
# 3. If we reach print(), the arguments are valid!
#
# GUARD CLAUSES:
# Instead of:
#   if valid:
#       do_stuff()
#   else:
#       error()
#
# Use:
#   if not valid:
#       sys.exit("error")
#   do_stuff()
#
# Guard clauses make the "happy path" (main logic) less indented
# and easier to read.
#
# EXIT CODES:
# - sys.exit() or sys.exit(0) - success
# - sys.exit(1) or sys.exit("message") - failure
# Exit codes tell other programs whether this script succeeded.

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
