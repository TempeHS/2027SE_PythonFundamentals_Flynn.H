# Reads a CSV file into a list of dict objects
#
# EXPLANATION:
# This creates and appends the dict in ONE line!
#
# KEY CONCEPTS:
# - Combine dict creation and append in one statement
# - students.append({"name": name, "house": house})
# - No intermediate 'student' variable needed
#
# COMPARISON:
# Two lines:
#   student = {"name": name, "house": house}
#   students.append(student)
#
# One line:
#   students.append({"name": name, "house": house})
#
# WHEN TO USE EACH:
# - One line: Simple, quick, when dict is used immediately
# - Two lines: When you need to modify the dict before appending
#
# This is the most compact way to build a list of dictionaries.
# Now let's learn to SORT these dictionaries - see students6.py!

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in students:
    print(f"{student['name']} is in {student['house']}")
