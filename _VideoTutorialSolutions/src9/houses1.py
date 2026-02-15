# Filters out duplicate houses using set
#
# EXPLANATION:
# SETS automatically handle uniqueness!
#
# KEY CONCEPTS:
# - set(): A collection that stores only unique values
# - houses.add(value): Adds to set (ignores duplicates)
# - No 'if' check needed - set handles it!
#
# WHY SETS ARE BETTER:
# 1. Simpler code - no manual duplicate check
# 2. Faster - O(1) lookup vs O(n) for list
# 3. Designed for this exact purpose!
#
# SET VS LIST:
# List: ["a", "b", "a"] - allows duplicates
# Set:  {"a", "b"} - automatically unique
#
# CREATING SETS:
# set()      - empty set
# {1, 2, 3}  - set with values (not {} - that's a dict!)

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
