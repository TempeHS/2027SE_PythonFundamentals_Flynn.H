# Demonstrates a for loop, using a list
#
# EXPLANATION:
# This program introduces the 'for' loop - a cleaner way to iterate!
#
# KEY CONCEPTS:
# - A 'for' loop iterates over items in a sequence (like a list)
# - for i in [0, 1, 2]: means "for each value in this list"
# - The variable i takes on each value in the list, one at a time
# - No need to manually initialize or increment i!
#
# HOW IT WORKS:
# 1. First iteration: i = 0, print "meow"
# 2. Second iteration: i = 1, print "meow"
# 3. Third iteration: i = 2, print "meow"
# 4. No more items in list, loop ends
#
# FOR VS WHILE:
# While loop: You manage the counter (initialize, check, increment)
# For loop: Python manages the counter for you!
#
# [0, 1, 2] is a LIST:
# - Lists are collections of items in square brackets
# - Lists can contain any type: [1, 2, 3] or ["a", "b", "c"]
# - The for loop visits each item in order
#
# See cat6.py for an even cleaner way using range().

for i in [0, 1, 2]:
    print("meow")
