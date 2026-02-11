# Reads from a file, one line at a time
#
# EXPLANATION:
# This reads a file LINE BY LINE - more memory efficient!
#
# KEY CONCEPTS:
# - You can iterate directly over a file object
# - for line in file: reads one line at a time
# - More memory-efficient than readlines() for large files
# - Each line still includes \n, so use rstrip()
#
# HOW IT WORKS:
# with open("names.txt") as file:
#     for line in file:  # Reads one line at a time
#         print("hello,", line.rstrip())
#
# WHY THIS IS BETTER:
# readlines(): Loads ENTIRE file into memory first
# for line in file: Reads one line at a time
#
# For a file with 1 million names:
# - readlines() uses lots of memory
# - for line in file: uses minimal memory
#
# BEST PRACTICE:
# Use 'for line in file:' unless you specifically need
# all lines in a list at once.

with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())
