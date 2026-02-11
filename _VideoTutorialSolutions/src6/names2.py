# Writes to a file
#
# EXPLANATION:
# This writes a name to a FILE - now it's saved permanently!
#
# KEY CONCEPTS:
# - open(filename, mode) opens a file for reading or writing
# - "w" mode = write (creates new file or OVERWRITES existing)
# - file.write(text) writes text to the file
# - file.close() closes the file (important!)
#
# HOW IT WORKS:
# 1. Get name from user
# 2. Open "names.txt" for writing ("w")
# 3. Write the name to the file
# 4. Close the file
#
# FILE MODES:
# - "r" = read (default)
# - "w" = write (overwrites existing content!)
# - "a" = append (adds to end of file)
#
# WARNING WITH "w" MODE:
# Each time you run this, it OVERWRITES the file!
# If you want to keep adding names, use "a" (append) instead.
# See names3.py for the append version.
#
# ALWAYS CLOSE:
# file.close() is important! It ensures data is saved.
# A better approach is 'with' (see names4.py).

name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
