# Sorts a list of strings
#
# EXPLANATION:
# This reads CSV data, stores formatted strings, and sorts them.
#
# KEY CONCEPTS:
# - Build a list of strings to sort
# - sorted() sorts strings alphabetically
# - Print the sorted results
#
# HOW IT WORKS:
# 1. Create empty list: students = []
# 2. For each line, extract name and house
# 3. Create formatted string: "Harry is in Gryffindor"
# 4. Append to list
# 5. Sort and print
#
# OUTPUT (sorted alphabetically by the start of each string):
# Draco is in Slytherin
# Harry is in Gryffindor
# Hermione is in Gryffindor
# Ron is in Gryffindor
#
# LIMITATION:
# We're sorting the ENTIRE string, not just the name.
# What if we want to sort by house instead?
# See students6.py for sorting dictionaries with custom keys!

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
