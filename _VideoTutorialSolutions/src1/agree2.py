# Lowercases string before comparing
#
# EXPLANATION:
# This program handles both extra spaces AND different capitalizations.
#
# KEY CONCEPTS:
# - .lower() converts all characters to lowercase
# - "YES", "Yes", "yeS" all become "yes" after .lower()
# - Method chaining: .strip().lower() runs both methods in sequence
# - The result is stored in 'answer' before the comparison
#
# HOW IT WORKS:
# 1. User enters "  YES  " (uppercase with spaces)
# 2. .strip() removes spaces: "YES"
# 3. .lower() converts to lowercase: "yes"
# 4. The comparison answer == "yes" succeeds!
#
# METHOD CHAINING EXPLAINED:
# .strip().lower() is like doing this:
#   temp = input("Do you agree? ").strip()
#   answer = temp.lower()
# But in one line!
#
# ORDER MATTERS (sort of):
# .strip().lower() and .lower().strip() give the same result here,
# but it's conventional to strip first, then transform the text.

answer = input("Do you agree? ").strip().lower()
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")
