# Sorts a list of dictionaries using a lambda function
#
# EXPLANATION:
# This uses a LAMBDA - an anonymous (nameless) function!
#
# KEY CONCEPTS:
# - lambda creates a small function without 'def'
# - Syntax: lambda parameters: expression
# - lambda student: student["name"] returns the name
# - Perfect for simple, one-line functions used once
#
# COMPARISON:
# Using def (students6.py):
#   def get_name(student):
#       return student["name"]
#   sorted(students, key=get_name)
#
# Using lambda (this file):
#   sorted(students, key=lambda student: student["name"])
#
# Same result, but lambda is inline - no need for separate function!
#
# LAMBDA SYNTAX:
# lambda student: student["name"]
#        ^^^^^    ^^^^^^^^^^^^^^^
#        input    what to return
#
# WHEN TO USE LAMBDA:
# - Simple, one-expression functions
# - Used only once (like a key function)
# - When a full def feels like overkill
#
# SORT BY HOUSE INSTEAD:
# sorted(students, key=lambda student: student["house"])

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
