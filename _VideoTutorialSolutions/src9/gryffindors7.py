# Iterates over a list by index
#
# EXPLANATION:
# Sometimes you need both the INDEX and the VALUE.
#
# KEY CONCEPTS:
# - range(len(students)) gives indices: 0, 1, 2
# - students[i] accesses item at index i
# - i + 1 for 1-based numbering (for humans)
#
# THE LOOP:
# for i in range(len(students)):
#     print(i + 1, students[i])
#
# Output:
# 1 Hermione
# 2 Harry
# 3 Ron
#
# THIS WORKS, BUT...
# It's a bit clunky: range(len(...)) and students[i].
# Python has a better way: enumerate()!
# See gryffindors8.py!

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
