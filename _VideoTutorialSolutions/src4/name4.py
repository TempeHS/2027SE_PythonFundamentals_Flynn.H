# Demonstrates list slice
#
# EXPLANATION:
# This program greets multiple people using list slicing!
#
# KEY CONCEPTS:
# - sys.argv[1:] is a "slice" - it gets everything from index 1 onward
# - Slices create a new list from part of the original
# - This skips the script name (sys.argv[0]) and gets all arguments
# - The for loop processes each name
#
# HOW IT WORKS:
# Command: python name4.py Alice Bob Charlie
# sys.argv = ["name4.py", "Alice", "Bob", "Charlie"]
# sys.argv[1:] = ["Alice", "Bob", "Charlie"]
#
# The loop greets each person!
#
# SLICE NOTATION:
# - list[start:end] - elements from start to end-1
# - list[start:] - elements from start to the end
# - list[:end] - elements from beginning to end-1
# - list[:] - copy of the entire list
#
# EXAMPLES:
# nums = [0, 1, 2, 3, 4]
# nums[1:3] = [1, 2]
# nums[2:] = [2, 3, 4]
# nums[:2] = [0, 1]
#
# Slicing is a powerful Python feature for working with sequences!

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
