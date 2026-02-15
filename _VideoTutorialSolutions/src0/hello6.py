# Demonstrates str functions
#
# EXPLANATION:
# This program cleans up user input using string methods (functions that
# belong to string objects).
#
# KEY CONCEPTS:
# - Strings have built-in methods (functions) you can call using dot notation
# - .strip() removes whitespace (spaces, tabs) from the beginning and end
# - .title() capitalizes the first letter of each word
# - "Method chaining" lets you call multiple methods in a row: .strip().title()
#
# HOW IT WORKS:
# 1. User types "  david malan  " (with extra spaces and lowercase)
# 2. .strip() removes leading/trailing spaces: "david malan"
# 3. .title() capitalizes each word: "David Malan"
# 4. The cleaned name is stored in the variable and printed
#
# WHY THIS MATTERS:
# Users often make typos - extra spaces, wrong capitalization, etc.
# Good programs "clean" or "sanitize" user input to handle these cases.
#
# OTHER USEFUL STRING METHODS:
# - .lower() - converts to all lowercase: "HELLO" -> "hello"
# - .upper() - converts to all uppercase: "hello" -> "HELLO"
# - .capitalize() - capitalizes first letter only: "hello world" -> "Hello world"

name = input("What's your name? ").strip().title()
print(f"hello, {name}")
