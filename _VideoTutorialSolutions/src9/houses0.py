# Filters out duplicate houses using loop
#
# EXPLANATION:
# This removes duplicates manually using a loop.
#
# KEY CONCEPTS:
# - Check 'if item not in list' before adding
# - Manually track unique values
# - Works, but there's a better way!
#
# THE PATTERN:
# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
#
# This builds a list with no duplicates.
# But checking 'not in' is slow for large lists!
#
# See houses1.py for using SET - designed for uniqueness!

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
