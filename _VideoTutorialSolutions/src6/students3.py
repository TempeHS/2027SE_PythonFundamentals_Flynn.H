# Reads a CSV file into a list of dict objects, creating empty dict first
#
# EXPLANATION:
# This stores each student as a DICTIONARY instead of a string!
#
# KEY CONCEPTS:
# - Dictionaries store key-value pairs: {"name": "Harry", "house": "Gryffindor"}
# - Access values with: student["name"], student["house"]
# - More structured than plain strings
# - Easier to work with individual fields
#
# HOW IT WORKS:
# 1. Create empty dict: student = {}
# 2. Add key-value pairs: student["name"] = name
# 3. Append dict to list
# 4. Each student is now a complete object with named fields
#
# WHY DICTIONARIES?
# With strings: "Harry is in Gryffindor" - can't easily get just the name
# With dicts: student["name"] gives us "Harry" directly!
#
# This is a verbose way to create dicts.
# See students4.py for a more compact approach.

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
