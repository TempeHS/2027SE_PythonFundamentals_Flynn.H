# Writes a CSV file using csv.DictWriter
#
# EXPLANATION:
# This uses csv.DictWriter - write rows as dictionaries!
#
# KEY CONCEPTS:
# - csv.DictWriter(file, fieldnames=[...]) creates a dict writer
# - fieldnames specifies the column order
# - writerow({"col": value, ...}) writes a dict as a row
# - More readable than writing lists
#
# HOW IT WORKS:
# writer = csv.DictWriter(file, fieldnames=["name", "home"])
# writer.writerow({"name": name, "home": home})
#
# COMPARISON:
# csv.writer:
#   writer.writerow([name, home])  # Must remember column order!
#
# csv.DictWriter:
#   writer.writerow({"name": name, "home": home})  # Explicit keys!
#
# BENEFITS:
# - Column order in fieldnames, not scattered in code
# - Dict keys make the code self-documenting
# - Easier to add/remove columns later
#
# WRITE HEADER ROW:
# writer.writeheader() writes: name,home as the first line
# Useful when creating a new file!

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
