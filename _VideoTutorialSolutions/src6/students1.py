# Unpacks a list
#
# EXPLANATION:
# This uses LIST UNPACKING for cleaner variable names!
#
# KEY CONCEPTS:
# - List unpacking: name, house = ["Hermione", "Gryffindor"]
# - Creates separate variables from a list
# - Much clearer than row[0], row[1]
#
# HOW IT WORKS:
# split(",") returns: ["Hermione", "Gryffindor"]
# name, house = ["Hermione", "Gryffindor"]
# This creates:
#   name = "Hermione"
#   house = "Gryffindor"
#
# COMPARISON:
# Before: row = line.rstrip().split(",")
#         print(row[0], row[1])  # What's row[0]? row[1]?
#
# After:  name, house = line.rstrip().split(",")
#         print(name, house)  # Clear!
#
# UNPACKING REQUIREMENT:
# The number of variables must match the list length.
# name, house = ["Harry", "Gryffindor", "Seeker"]  # Error!
# Need: name, house, position = [...]

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
