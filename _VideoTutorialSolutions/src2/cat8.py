# Demonstrates str multiplication
#
# EXPLANATION:
# This program shows a clever Python feature: string multiplication!
#
# KEY CONCEPTS:
# - You can "multiply" a string by a number to repeat it
# - "meow\n" * 3 creates "meow\nmeow\nmeow\n"
# - \n is the "newline character" - it creates a line break
# - end="" prevents print from adding an extra newline at the end
#
# HOW IT WORKS:
# 1. "meow\n" is the string "meow" followed by a newline
# 2. Multiplying by 3 repeats it: "meow\nmeow\nmeow\n"
# 3. print() displays this, but would normally add another newline
# 4. end="" prevents that extra newline (we already have 3)
#
# STRING MULTIPLICATION:
# - "abc" * 3 = "abcabcabc"
# - "x" * 5 = "xxxxx"
# - "-" * 20 = "--------------------" (useful for separators!)
#
# WHY end=""?
# Without end="", the output would have 4 newlines (3 from the string, 1 from print).
# With end="", we get exactly 3 newlines.
#
# THIS IS CLEVER, BUT...
# While this is compact, a for loop is often clearer for beginners.
# Use whichever is more readable for your situation.

print("meow\n" * 3, end="")
