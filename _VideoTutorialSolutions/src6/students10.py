# Writes a CSV file using csv.writer
#
# EXPLANATION:
# This WRITES to a CSV file using csv.writer!
#
# KEY CONCEPTS:
# - csv.writer(file) creates a writer for CSV output
# - writer.writerow([values]) writes one row
# - Automatically handles commas, quotes, and escaping
# - Much safer than manually building CSV strings
#
# HOW IT WORKS:
# 1. Get name and home from user
# 2. Open file for appending ("a")
# 3. Create csv.writer
# 4. writerow([name, home]) adds the row
#
# WHY USE CSV.WRITER?
# If name = "Smith, Jr." (with a comma):
# - Manual: "Smith, Jr.,London" - broken CSV!
# - csv.writer: "\"Smith, Jr.\",London" - properly quoted!
#
# CSV WRITER HANDLES:
# - Quoting fields that contain commas
# - Escaping quote characters
# - Proper line endings
#
# See students11.py for csv.DictWriter!

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
