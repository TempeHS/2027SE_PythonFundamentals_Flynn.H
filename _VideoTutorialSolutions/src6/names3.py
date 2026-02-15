# Appends to a file
#
# EXPLANATION:
# This APPENDS to a file - adds to the end instead of overwriting!
#
# KEY CONCEPTS:
# - "a" mode = append (adds to end of file)
# - \n adds a newline so each name is on its own line
# - File is created if it doesn't exist
# - Existing content is preserved
#
# HOW IT WORKS:
# 1. Get name from user
# 2. Open "names.txt" for appending ("a")
# 3. Write name with \n (newline) at the end
# 4. Close the file
#
# WRITE VS APPEND:
# "w" mode: Alice -> run again -> Bob -> file contains only "Bob"
# "a" mode: Alice -> run again -> Bob -> file contains "Alice\nBob"
#
# WHY \n (NEWLINE)?
# Without \n, all names run together: "AliceBobCharlie"
# With \n, each name is on a new line:
#   Alice
#   Bob
#   Charlie
#
# See names4.py for the better 'with' syntax!

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
