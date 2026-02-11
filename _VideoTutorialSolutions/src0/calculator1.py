# Demonstrates (unintended) concatenation of strings
#
# EXPLANATION:
# This program has a BUG! It shows what happens when you try to add user input
# without converting it to numbers first.
#
# KEY CONCEPTS:
# - input() ALWAYS returns a string, even if the user types numbers
# - When the user types "1", Python receives the TEXT "1", not the NUMBER 1
# - Using + with strings concatenates (joins) them: "1" + "2" = "12", not 3
# - This is a common beginner mistake!
#
# THE BUG:
# If you type 1 and 2, you might expect to see 3, but you'll see "12" instead!
# That's because Python is joining the strings "1" and "2" together.
#
# HOW IT HAPPENS:
# 1. User types 1 -> x = "1" (a string containing the character '1')
# 2. User types 2 -> y = "2" (a string containing the character '2')
# 3. z = x + y concatenates: z = "12"
# 4. print(z) outputs: 12
#
# THE FIX: You need to convert the input to integers using int().
# See calculator2.py for the corrected version!

# Prompt user for two integers
x = input("What's x? ")
y = input("What's y? ")

# Print sum
z = x + y
print(z)
