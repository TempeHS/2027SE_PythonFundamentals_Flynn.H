# Uses filter and key with lambda
#
# EXPLANATION:
# filter() and lambda are functional programming tools!
#
# KEY CONCEPTS:
# - filter(function, iterable): Keeps items where function returns True
# - lambda: Anonymous (unnamed) function
# - sorted(list, key=function): Sort by custom key
#
# THE FILTER:
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"
# gryffindors = filter(is_gryffindor, students)
#
# Filter calls is_gryffindor for each student.
# Only keeps students where it returns True.
#
# THE SORTED KEY:
# sorted(gryffindors, key=lambda s: s["name"])
# Sorts by the "name" key of each dict.
#
# FUNCTIONAL PROGRAMMING:
# - Pass functions as arguments
# - No explicit loops
# - More declarative style
#
# See gryffindors3.py for using lambda IN filter!

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
