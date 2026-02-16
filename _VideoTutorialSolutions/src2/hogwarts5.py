# Demonstrates iterating over a list of dict objects
#
# EXPLANATION:
# This program shows how to work with complex data structures!
#
# KEY CONCEPTS:
# - A list can contain dictionaries as its elements
# - Each dictionary represents one "record" with multiple fields
# - This is a common pattern for storing structured data
# - Access nested data: list[index]["key"]
#
# DATA STRUCTURE:
# students is a LIST of DICTS. Each dict has:
# - "name": the student's name
# - "house": their Hogwarts house
# - "patronus": their patronus (or None if unknown)
#
# HOW IT WORKS:
# for student in students:
#     - student is a dict like {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}
#     - student["name"] is "Hermione"
#     - student["house"] is "Gryffindor"
#     - student["patronus"] is "Otter"
#
# NONE IN PYTHON:
# - None represents "no value" or "nothing"
# - Draco's patronus is None because he doesn't have one
# - This is different from an empty string ""
#
# OUTPUT:
# Hermione, Gryffindor, Otter
# Harry, Gryffindor, Stag
# Ron, Gryffindor, Jack Russell terrier
# Draco, Slytherin, None
#
# This pattern is similar to a database table or spreadsheet!

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
