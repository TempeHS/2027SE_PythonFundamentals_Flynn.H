# Demonstrates iterating over and indexing into a list
#
# EXPLANATION:
# This program shows how to loop with both the index AND the value.
#
# KEY CONCEPTS:
# - len(students) returns the length of the list (3 in this case)
# - range(len(students)) creates range(3) -> 0, 1, 2
# - We use i to access both the position and the value
# - i + 1 gives us human-friendly numbering (1, 2, 3 instead of 0, 1, 2)
#
# HOW IT WORKS:
# 1. i = 0: print(0 + 1, students[0]) -> "1 Hermione"
# 2. i = 1: print(1 + 1, students[1]) -> "2 Harry"
# 3. i = 2: print(2 + 1, students[2]) -> "3 Ron"
#
# OUTPUT:
# 1 Hermione
# 2 Harry
# 3 Ron
#
# WHEN TO USE THIS PATTERN:
# - When you need to know the position of each item
# - When you need to number items (like a ranked list)
# - When you need to compare items at different positions
#
# PYTHONIC ALTERNATIVE:
# for i, student in enumerate(students):
#     print(i + 1, student)
# enumerate() is the more Pythonic way to get both index and value.

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
