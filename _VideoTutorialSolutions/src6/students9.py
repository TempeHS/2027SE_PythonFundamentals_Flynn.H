# Reads a CSV file using csv.DictReader
#
# EXPLANATION:
# This uses csv.DictReader - returns dictionaries with column names as keys!
#
# KEY CONCEPTS:
# - csv.DictReader uses the first row as column headers
# - Each row becomes a dictionary: {"name": "Harry", "home": "London"}
# - Access values by column name: row["name"], row["home"]
# - No need to remember column indices!
#
# CSV FILE (students2.csv):
# name,home       <- header row (column names)
# Harry,London
# Hermione,Paris
# Ron,Dublin
#
# HOW IT WORKS:
# reader = csv.DictReader(file)
# for row in reader:  # row is a dictionary!
#     # row = {"name": "Harry", "home": "London"}
#     row["name"] = "Harry"
#     row["home"] = "London"
#
# WHY DICTREADER?
# - row["name"] is clearer than row[0]
# - If columns are reordered, code still works!
# - Self-documenting - column names explain the data
#
# BEST PRACTICE:
# Use DictReader for CSV files with header rows.
# Much more readable and maintainable than index-based access.

import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
