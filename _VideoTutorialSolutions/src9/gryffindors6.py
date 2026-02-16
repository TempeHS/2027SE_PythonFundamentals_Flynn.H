# Uses dictionary comprehension instead
#
# EXPLANATION:
# DICT COMPREHENSION creates a dictionary, not a list!
#
# KEY CONCEPTS:
# - {key: value for item in list}
# - Uses curly braces {} not square brackets []
# - Creates a dictionary directly
#
# THE COMPREHENSION:
# gryffindors = {student: "Gryffindor" for student in students}
#
# RESULT:
# {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor"}
#
# COMPARE:
# - List comp: [{...} for x in y] -> List of dicts
# - Dict comp: {k: v for x in y} -> Single dict
#
# WHEN TO USE DICT COMPREHENSION:
# When you want key-value pairs, not a list of items.

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
