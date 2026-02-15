# Filters by house using list comprehension
#
# EXPLANATION:
# List comprehensions are a more Pythonic way to filter!
#
# KEY CONCEPTS:
# - [expression for item in list if condition]
# - Creates a new list in one line
# - Replaces loop + append pattern
#
# THE COMPREHENSION:
# gryffindors = [
#     student["name"]
#     for student in students
#     if student["house"] == "Gryffindor"
# ]
#
# TRANSLATION:
# "Give me student's name, for each student in students,
#  but only if their house is Gryffindor"
#
# COMPARISON:
# Loop: 4 lines (empty list, for, if, append)
# Comprehension: 1 expression!
#
# See gryffindors2.py for filter() function approach!

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
