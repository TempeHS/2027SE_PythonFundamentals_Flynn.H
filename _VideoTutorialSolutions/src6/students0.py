# Reads a CSV file
#
# EXPLANATION:
# This reads a CSV (Comma-Separated Values) file.
#
# KEY CONCEPTS:
# - CSV files store data with commas between values
# - Example: "Hermione,Gryffindor" (name,house)
# - split(",") breaks a string into a list at each comma
# - row[0] is the first value, row[1] is the second
#
# HOW IT WORKS:
# 1. Read each line from the CSV
# 2. rstrip() removes the trailing newline
# 3. split(",") creates a list: ["Hermione", "Gryffindor"]
# 4. row[0] = "Hermione", row[1] = "Gryffindor"
#
# CSV EXAMPLE (students0.csv):
# Hermione,Gryffindor
# Harry,Gryffindor
# Ron,Gryffindor
# Draco,Slytherin
#
# LIMITATION:
# Using row[0] and row[1] is fragile:
# - What if columns are reordered?
# - What if there are more columns?
# See students1.py for a cleaner approach!

with open("students0.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
