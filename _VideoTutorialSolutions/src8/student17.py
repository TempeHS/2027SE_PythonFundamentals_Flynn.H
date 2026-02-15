# Removes patronus for simplicy, circumvents error-checking by setting attribute
#
# EXPLANATION:
# This demonstrates a PROBLEM - validation can be bypassed!
#
# KEY CONCEPTS:
# - Validation in __init__ only runs at creation time
# - Attributes can be changed directly after creation
# - student.house = "Invalid" bypasses our validation!
#
# THE PROBLEM:
# student = Student("Harry", "Gryffindor")  # Valid!
# student.house = "Number Four, Privet Drive"  # Not a house!
# print(student.house)  # Shows invalid value
#
# Our validation only checked during __init__.
# Direct assignment bypasses it completely.
#
# THIS IS BAD because:
# 1. Our "always valid" guarantee is broken
# 2. Invalid data can creep into our objects
# 3. Bugs become harder to find
#
# THE SOLUTION:
# Use PROPERTIES to control attribute access!
# Properties let us run code when attributes
# are read or written.
#
# See student18.py for @property!


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
