# Adds pass
#
# EXPLANATION:
# This program uses 'pass' to silently handle errors (no message).
#
# KEY CONCEPTS:
# - 'pass' is a placeholder that does nothing
# - Using pass in except means "catch the error but don't do anything"
# - This silently ignores invalid input and keeps asking
#
# HOW IT WORKS:
# 1. User enters "cat"
# 2. ValueError is raised
# 3. except block runs: pass (do nothing)
# 4. Loop continues, asks again
# 5. User enters "42"
# 6. return 42 exits the function
#
# SILENT RETRY PATTERN:
# while True:
#     try:
#         return <risky operation>
#     except:
#         pass  # Silently retry
#
# WHEN TO USE PASS:
# - When you want to retry without showing an error
# - When the error message would be distracting
# - Use with caution: users might not know why it's asking again!
#
# TRADE-OFF:
# - With message: User knows what went wrong
# - With pass: Cleaner output, but user might be confused
#
# Generally, showing an error message is more user-friendly.


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


main()
