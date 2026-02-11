# Represents a student with multiple variables
#
# EXPLANATION:
# This is the SIMPLEST way to store student data - separate variables.
#
# KEY CONCEPTS:
# - Each piece of data is a separate variable
# - Simple and works for one student
# - But what if we have 100 students?
#
# THE PROBLEM:
# Variables are disconnected. name and house aren't "linked."
# With many students, we'd need: name1, house1, name2, house2...
# There's no way to pass "a student" to a function.
#
# SOLUTION:
# Group related data together! Options:
# - Tuples: (name, house)
# - Lists: [name, house]
# - Dicts: {"name": name, "house": house}
# - Classes: Custom Student type (best for complex data)
#
# This file is just the starting point.
# See student1.py for the next step: using functions!

name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
