# Demonstrates iterating over and index into a dict
#
# EXPLANATION:
# This program shows how to loop through all items in a dictionary.
#
# KEY CONCEPTS:
# - for key in dict: iterates over the KEYS of the dictionary
# - Use the key to look up the value: dict[key]
# - sep=", " changes the separator between print arguments
# - By default, print uses a space; sep changes it to ", "
#
# HOW IT WORKS:
# 1. First iteration: student = "Hermione"
#    print("Hermione", students["Hermione"], sep=", ")
#    Output: "Hermione, Gryffindor"
# 2. Continues for Harry, Ron, Draco...
#
# SEP PARAMETER:
# - print("a", "b") -> "a b" (space between)
# - print("a", "b", sep=", ") -> "a, b" (comma-space between)
# - print("a", "b", sep="") -> "ab" (no separator)
# - print("a", "b", sep="\n") -> "a" then "b" (on separate lines)
#
# OTHER WAYS TO ITERATE DICTS:
# - for key in dict: -> iterate over keys only
# - for value in dict.values(): -> iterate over values only
# - for key, value in dict.items(): -> iterate over both
#
# EXAMPLE WITH .ITEMS():
# for name, house in students.items():
#     print(name, house, sep=", ")

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")
