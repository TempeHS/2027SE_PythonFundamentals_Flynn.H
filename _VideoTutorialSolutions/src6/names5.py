# Reads from a file
#
# EXPLANATION:
# This READS from a file - loading data that was saved earlier!
#
# KEY CONCEPTS:
# - open() with no mode defaults to "r" (read)
# - file.readlines() returns a list of all lines
# - Each line includes the \n at the end
# - line.rstrip() removes trailing whitespace (including \n)
#
# HOW IT WORKS:
# 1. Open names.txt for reading (no mode needed, "r" is default)
# 2. readlines() loads ALL lines into a list
# 3. Loop through each line
# 4. rstrip() removes the trailing newline
# 5. Print the greeting
#
# WHY RSTRIP()?
# File contains: "Alice\n", "Bob\n", "Charlie\n"
# Without rstrip: print("hello,", line) adds extra blank line
# With rstrip: print("hello,", line.rstrip()) looks clean
#
# READLINES() NOTE:
# Loads entire file into memory at once.
# Fine for small files, but see names6.py for a more
# memory-efficient approach for large files.

with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
