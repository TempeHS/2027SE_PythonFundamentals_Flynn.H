# Creates list of dicts using loop
#
# EXPLANATION:
# This creates structured data from a simple list.
#
# KEY CONCEPTS:
# - Start with list of names: ["Hermione", "Harry", "Ron"]
# - Transform each name into a dict
# - Result: List of dicts with name and house
#
# THE PATTERN:
# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
#
# This transforms:
# ["Hermione", "Harry", "Ron"]
# Into:
# [{"name": "Hermione", "house": "Gryffindor"}, ...]
#
# See gryffindors5.py for list comprehension version!

students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)
