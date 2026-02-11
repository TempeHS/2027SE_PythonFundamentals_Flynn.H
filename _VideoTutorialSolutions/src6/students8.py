# Reads a CSV file using csv.reader
#
# EXPLANATION:
# This uses Python's CSV module - the proper way to handle CSV files!
#
# KEY CONCEPTS:
# - import csv brings in the csv module
# - csv.reader(file) creates a reader that parses CSV properly
# - Each 'row' is already a list of values - no split() needed!
# - Handles edge cases like commas inside quoted values
#
# HOW IT WORKS:
# reader = csv.reader(file)
# for row in reader:  # row is already a list!
#     # row = ["Harry", "London"]
#     row[0] = "Harry"
#     row[1] = "London"
#
# WHY USE CSV MODULE?
# Manual split(",") fails with: "Smith, Jr.", New York
# The comma inside "Smith, Jr." would break split!
# csv.reader handles quoted fields correctly.
#
# CSV MODULE BENEFITS:
# - Handles quoted values with commas
# - Handles escape characters
# - Handles different delimiters
# - Standard, well-tested code
#
# See students9.py for csv.DictReader - even better!

import csv

students = []

with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
