# Sorts a list of dictionaries using a function
#
# EXPLANATION:
# This shows how to sort dictionaries using a custom KEY function!
#
# KEY CONCEPTS:
# - sorted() can take a 'key' parameter
# - 'key' is a function that extracts the value to sort by
# - sorted() calls key(item) for each item to determine order
#
# THE PROBLEM:
# sorted(students) doesn't know HOW to compare dictionaries!
# Should it sort by name? By house? By something else?
#
# THE SOLUTION:
# Define a function that returns the value to sort by:
# def get_name(student):
#     return student["name"]
#
# Then: sorted(students, key=get_name)
# sorted() calls get_name() for each student and sorts by that value.
#
# HOW KEY WORKS:
# For [Harry, Hermione, Ron], sorted calls:
# - get_name({name: "Harry", ...}) -> "Harry"
# - get_name({name: "Hermione", ...}) -> "Hermione"
# - get_name({name: "Ron", ...}) -> "Ron"
# Then sorts by those values: Harry, Hermione, Ron
#
# See students7.py for a shorter way using lambda!

students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
