# Demonstrates indexing into a dict
#
# EXPLANATION:
# This program introduces DICTIONARIES - collections of key-value pairs.
#
# KEY CONCEPTS:
# - A dictionary (dict) maps keys to values: {key: value}
# - Access values using the key: dict_name[key]
# - students["Hermione"] returns "Gryffindor"
# - Unlike lists, dicts use KEYS (usually strings), not numerical indices
# - Dicts are perfect for storing related data (name -> house)
#
# DICT SYNTAX:
# {
#     "key1": "value1",
#     "key2": "value2",
# }
#
# HOW IT WORKS:
# - students["Hermione"] looks up the key "Hermione" and returns "Gryffindor"
# - students["Draco"] looks up "Draco" and returns "Slytherin"
#
# KEYERROR:
# If you try to access a key that doesn't exist, Python raises a KeyError.
# students["Luna"] would fail because "Luna" is not a key in this dict.
#
# LISTS VS DICTS:
# - List: Ordered by position (index 0, 1, 2...)
# - Dict: Organized by key (any string or number)
#
# Use a dict when you want to look things up by name, not by position!

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
