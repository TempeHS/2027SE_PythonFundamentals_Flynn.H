# Demonstrates a for loop, using range
#
# EXPLANATION:
# This program uses range() - the standard way to repeat something n times!
#
# KEY CONCEPTS:
# - range(3) generates the sequence 0, 1, 2 (three values, starting at 0)
# - It's equivalent to [0, 1, 2] but more efficient for large ranges
# - for i in range(3): runs 3 times, with i = 0, 1, 2
# - This is the most common pattern for repeating code n times
#
# HOW RANGE WORKS:
# - range(n) gives you n values: 0, 1, 2, ..., n-1
# - range(3) -> 0, 1, 2
# - range(5) -> 0, 1, 2, 3, 4
# - range(1) -> 0
# - range(0) -> (empty - loop runs 0 times)
#
# RANGE VARIATIONS:
# - range(stop): 0 to stop-1
# - range(start, stop): start to stop-1
# - range(start, stop, step): start to stop-1, counting by step
#
# EXAMPLES:
# - range(3) -> 0, 1, 2
# - range(1, 4) -> 1, 2, 3
# - range(0, 10, 2) -> 0, 2, 4, 6, 8 (even numbers)
# - range(5, 0, -1) -> 5, 4, 3, 2, 1 (countdown)

for i in range(3):
    print("meow")
