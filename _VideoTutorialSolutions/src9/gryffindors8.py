# Uses enumerate instead
#
# EXPLANATION:
# enumerate() gives you both index AND value!
#
# KEY CONCEPTS:
# - enumerate(list) returns (index, value) pairs
# - Unpack with: for i, student in enumerate(students)
# - Cleaner than range(len(...))
#
# THE LOOP:
# for i, student in enumerate(students):
#     print(i + 1, student)
#
# ENUMERATE RETURNS:
# (0, "Hermione"), (1, "Harry"), (2, "Ron")
#
# COMPARE:
# Before: for i in range(len(students)): ... students[i]
# After:  for i, student in enumerate(students): ... student
#
# PYTHONIC:
# enumerate() is the Pythonic way to get indices.
# It's clearer and avoids off-by-one errors.

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)
