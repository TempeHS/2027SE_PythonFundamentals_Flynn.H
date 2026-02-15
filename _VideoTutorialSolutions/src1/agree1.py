# Strips string before comparing
#
# EXPLANATION:
# This program improves agree0.py by removing extra whitespace from input.
#
# KEY CONCEPTS:
# - .strip() removes spaces and whitespace from the start and end of a string
# - " yes " becomes "yes" after stripping
# - This handles users who accidentally add spaces
#
# HOW IT WORKS:
# 1. User enters " yes " (with accidental spaces)
# 2. .strip() removes the spaces: "yes"
# 3. The comparison answer == "yes" now works correctly!
#
# WHY THIS MATTERS:
# Users often accidentally add spaces when typing. Good programs
# should be forgiving and handle these common mistakes.
#
# STILL A PROBLEM:
# This still doesn't handle "Yes" or "YES" - those are different strings!
# See agree2.py for the complete solution.

answer = input("Do you agree? ").strip()
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")
