# Uses dictionary comprehension instead
#
# EXPLANATION:
# List comprehension can create complex objects too!
#
# KEY CONCEPTS:
# - [{expression} for item in list]
# - The expression can be a dict: {"name": student, "house": "Gryffindor"}
# - Creates list of dicts in one line
#
# THE COMPREHENSION:
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
#
# This is the same as:
# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
#
# But in one elegant line!
# See gryffindors6.py for DICT comprehension!

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)
