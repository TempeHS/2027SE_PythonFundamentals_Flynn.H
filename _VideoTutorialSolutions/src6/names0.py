# Stores a name in a variable
#
# EXPLANATION:
# This program stores a name in memory - but it's lost when the program ends!
#
# KEY CONCEPTS:
# - Variables exist only while the program is running
# - When you close the program, all data is lost
# - This is why we need FILE I/O (Input/Output)
#
# THE PROBLEM:
# 1. User enters their name
# 2. We store it in 'name' variable
# 3. Program prints the greeting
# 4. Program ends - 'name' variable is deleted from memory!
#
# Next time you run the program, it doesn't remember the name.
# To save data PERMANENTLY, we need to write it to a FILE.
#
# FILE I/O PREVIEW:
# - Write data to a file (like names.txt)
# - Data persists even after program ends
# - Read data back when program starts again
#
# See names2.py for writing to a file!

name = input("What's your name? ")
print(f"hello, {name}")
