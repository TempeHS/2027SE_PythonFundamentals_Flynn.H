# Demonstrates a while loop, counting up from 0
#
# EXPLANATION:
# This is the most common way to write a counting loop - starting from 0!
#
# KEY CONCEPTS:
# - Programmers conventionally start counting at 0, not 1
# - while i < 3: runs for i = 0, 1, 2 (three iterations)
# - Using < instead of <= is cleaner when starting from 0
# - The number in the condition (3) directly tells you how many times it runs
#
# HOW IT WORKS:
# 1. i = 0 (start at zero!)
# 2. Is 0 < 3? Yes! Print "meow", then i = 0 + 1 = 1
# 3. Is 1 < 3? Yes! Print "meow", then i = 1 + 1 = 2
# 4. Is 2 < 3? Yes! Print "meow", then i = 2 + 1 = 3
# 5. Is 3 < 3? No! Exit the loop.
#
# WHY START AT 0?
# - Array/list indices start at 0 in most languages
# - range(3) gives [0, 1, 2] - also starts at 0
# - Consistency makes code easier to read and understand
#
# THE PATTERN:
# i = 0
# while i < n:
#     # do something
#     i = i + 1
# This runs exactly n times (0 through n-1).

i = 0
while i < 3:
    print("meow")
    i = i + 1
