# Removes continue
#
# EXPLANATION:
# This is a simplified version of cat9.py - we don't need 'continue'!
#
# KEY CONCEPTS:
# - Instead of checking if invalid then continue, check if valid then break
# - This eliminates the need for both 'continue' and 'else'
# - The logic is simpler: "keep asking until you get a good answer"
#
# HOW IT WORKS:
# 1. while True: infinite loop
# 2. User enters a number
# 3. if n > 0: the number is valid, break out of the loop
# 4. Otherwise, the loop continues (asks again)
#
# COMPARISON:
# cat9.py (more complex):
#   if n <= 0:
#       continue
#   else:
#       break
#
# cat10.py (simpler):
#   if n > 0:
#       break
#
# SIMPLIFICATION PRINCIPLE:
# If you find yourself writing if/continue/else/break,
# consider if you can just write if/break instead!
#
# This pattern works when you just want to wait for valid input.
# The loop naturally repeats until the break condition is met.

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
