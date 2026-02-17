# Filters by house using loop
#
# EXPLANATION:
# This filters a list using a traditional for loop.
#
# KEY CONCEPTS:
# - List of dicts: Each student has name and house
# - Filter: Keep only Gryffindor students
# - Build new list with append()
#
# HOW IT WORKS:
# 1. Create empty list: gryffindors = []
# 2. Loop through students
# 3. If house is Gryffindor, add name to list
# 4. Print sorted result
#
# This is the "explicit" way - easy to understand.
# See gryffindors1.py for a shorter LIST COMPREHENSION!

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
