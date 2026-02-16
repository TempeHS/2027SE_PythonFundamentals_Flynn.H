# Adds context manager
#
# EXPLANATION:
# This uses 'with' - the BEST way to work with files!
#
# KEY CONCEPTS:
# - 'with open() as file:' is called a "context manager"
# - Automatically closes the file when the block ends
# - No need for file.close() - it's automatic!
# - Safer: file closes even if an error occurs
#
# HOW IT WORKS:
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
# # file is automatically closed here!
#
# COMPARISON:
# Old way (names3.py):
#   file = open("names.txt", "a")
#   file.write(f"{name}\n")
#   file.close()  # Easy to forget!
#
# Better way (this file):
#   with open("names.txt", "a") as file:
#       file.write(f"{name}\n")
#   # Automatically closed!
#
# ALWAYS USE 'WITH':
# It's cleaner, safer, and the Python standard.
# You'll see this pattern in professional code.

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
