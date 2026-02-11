# Reads a CSV file into a list of dict objects, creating dict first
#
# EXPLANATION:
# This creates dictionaries in ONE line using literal syntax!
#
# KEY CONCEPTS:
# - Dict literal: {"name": name, "house": house}
# - Creates the dict with values already set
# - Cleaner than creating empty dict and adding keys
#
# COMPARISON:
# Verbose (students3.py):
#   student = {}
#   student["name"] = name
#   student["house"] = house
#
# Compact (this file):
#   student = {"name": name, "house": house}
#
# Same result, less code!
#
# HOW IT WORKS:
# {"name": name, "house": house} creates:
# - Key "name" with value from the 'name' variable
# - Key "house" with value from the 'house' variable
#
# See students5.py for an even more compact version!

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
