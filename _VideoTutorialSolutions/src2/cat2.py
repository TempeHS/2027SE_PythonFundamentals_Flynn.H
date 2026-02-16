# Demonstrates a while loop, counting up from 1
#
# EXPLANATION:
# This program counts UP instead of down - an alternative approach.
#
# KEY CONCEPTS:
# - i starts at 1 and goes up to 3
# - while i <= 3: runs as long as i is 1, 2, or 3
# - i = i + 1 increases i by 1 each time
# - When i becomes 4, the condition i <= 3 is False, so the loop stops
#
# HOW IT WORKS:
# 1. i = 1 (start value)
# 2. Is 1 <= 3? Yes! Print "meow", then i = 1 + 1 = 2
# 3. Is 2 <= 3? Yes! Print "meow", then i = 2 + 1 = 3
# 4. Is 3 <= 3? Yes! Print "meow", then i = 3 + 1 = 4
# 5. Is 4 <= 3? No! Exit the loop.
#
# COUNTING UP VS DOWN:
# Both approaches work! Programmers often prefer counting up from 0.
# See cat3.py for the most common convention.
#
# ITERATION VALUES:
# This loop iterates with i = 1, 2, 3 (three values, three "meows")

i = 1
while i <= 3:
    print("meow")
    i = i + 1
