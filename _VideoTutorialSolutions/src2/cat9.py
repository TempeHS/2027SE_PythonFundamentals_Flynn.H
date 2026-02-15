# Introduces continue, break
#
# EXPLANATION:
# This program shows how to control loops with 'continue' and 'break'.
#
# KEY CONCEPTS:
# - while True: creates an intentional infinite loop
# - 'continue' skips to the next iteration of the loop
# - 'break' exits the loop entirely
# - This pattern is useful for input validation!
#
# HOW IT WORKS:
# 1. while True: starts an infinite loop
# 2. User enters a number
# 3. if n <= 0: the number is invalid
#    - 'continue' skips back to the start of the loop
#    - User is asked again
# 4. else: the number is valid
#    - 'break' exits the loop
# 5. The for loop uses the validated n to print "meow" n times
#
# CONTINUE VS BREAK:
# - continue: "Skip the rest of this iteration, start the next one"
# - break: "Stop the loop completely, exit now"
#
# INPUT VALIDATION PATTERN:
# while True:
#     get input
#     if input is invalid:
#         continue (or just don't break)
#     else:
#         break (input is good, exit loop)
#
# See cat10.py for a simpler version of this same logic.

while True:
    n = int(input("What's n? "))
    if n <= 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")
