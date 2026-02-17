# Uses filter with lambda
#
# EXPLANATION:
# Lambda can be used directly in filter - no named function!
#
# KEY CONCEPTS:
# - lambda s: s["house"] == "Gryffindor"
# - This IS the filter function, inline
# - Shorter, but less readable for complex logic
#
# LAMBDA SYNTAX:
# lambda parameters: expression
# - No 'def', no name, no 'return'
# - Just parameters and a single expression
#
# COMPARISON:
# Named function:
#   def is_gryffindor(s): return s["house"] == "Gryffindor"
#   filter(is_gryffindor, students)
#
# Lambda:
#   filter(lambda s: s["house"] == "Gryffindor", students)
#
# WHEN TO USE LAMBDA:
# - Simple one-liner functions
# - Used only once (as an argument)
# - When named function would be overkill

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
