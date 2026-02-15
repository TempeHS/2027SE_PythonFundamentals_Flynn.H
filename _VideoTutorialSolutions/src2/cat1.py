# Demonstrates a while loop, counting down
#
# EXPLANATION:
# This program introduces the 'while' loop - code that repeats while a condition is True.
#
# KEY CONCEPTS:
# - 'while' repeatedly executes its block as long as the condition is True
# - The loop checks the condition BEFORE each iteration
# - You need to update the variable (i = i - 1) to eventually end the loop
# - Without updating, you'd have an "infinite loop" that never stops!
#
# HOW IT WORKS:
# 1. i = 3 (start value)
# 2. Is 3 != 0? Yes! Print "meow", then i = 3 - 1 = 2
# 3. Is 2 != 0? Yes! Print "meow", then i = 2 - 1 = 1
# 4. Is 1 != 0? Yes! Print "meow", then i = 1 - 1 = 0
# 5. Is 0 != 0? No! Exit the loop.
# Result: "meow" is printed 3 times
#
# WHILE LOOP STRUCTURE:
# while condition:
#     # code to repeat
#     # update the condition variable!
#
# COMMON MISTAKE - INFINITE LOOP:
# Forgetting "i = i - 1" would make i stay at 3 forever,
# and the loop would never end! (Use Ctrl+C to stop a runaway program)

i = 3
while i != 0:
    print("meow")
    i = i - 1
