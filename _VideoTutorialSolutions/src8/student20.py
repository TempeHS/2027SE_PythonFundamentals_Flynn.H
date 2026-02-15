# Moves get_student into Student class
#
# EXPLANATION:
# CLASS METHODS are alternative ways to create objects!
#
# KEY CONCEPTS:
# - @classmethod decorator makes a class method
# - First parameter is 'cls' (the class itself, not an instance)
# - Can create instances: cls(name, house)
# - Called on the class: Student.get()
#
# WHY USE @classmethod?
# Sometimes you want different ways to create an object:
# - Student("Harry", "Gryffindor")  # Direct
# - Student.get()  # From user input
# - Student.from_csv("Harry,Gryffindor")  # From CSV string
#
# THE GET METHOD:
# @classmethod
# def get(cls):
#     name = input("Name: ")
#     house = input("House: ")
#     return cls(name, house)
#
# This moves input logic INTO the class.
# Call with: Student.get()  # No instance needed!
#
# CLS VS SELF:
# - self: Refers to an instance (object)
# - cls: Refers to the class itself
# - Class methods work on the class, not instances
#
# COMMON USES:
# - Factory methods (alternative constructors)
# - Creating from different input formats
# - Utility functions related to the class


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
