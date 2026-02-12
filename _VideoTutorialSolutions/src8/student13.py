# Prints student without __str__
#
# EXPLANATION:
# What happens when you print(student) directly?
#
# KEY CONCEPTS:
# - print(object) uses the object's __str__ method
# - Default __str__ shows: <__main__.Student object at 0x...>
# - This is not very helpful for humans!
#
# THE PROBLEM:
# print(student) outputs something like:
# <__main__.Student object at 0x7f1234567890>
#
# This tells us:
# - It's a Student object
# - Its memory address
# But NOT the actual data (name, house)!
#
# THE SOLUTION:
# Define our own __str__ method to control what prints.
# See student14.py for custom __str__!
#
# DUNDER METHODS (double underscore):
# __init__, __str__ are "dunder" methods.
# They have special meanings to Python.
# We can override them to customize behavior.


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
