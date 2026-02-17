# Adds __str__
#
# EXPLANATION:
# __str__ defines how an object is converted to a string!
#
# KEY CONCEPTS:
# - __str__(self) returns a string representation
# - Called automatically by print() and str()
# - We control what gets displayed!
#
# HOW IT WORKS:
# def __str__(self):
#     return f"{self.name} from {self.house}"
#
# Now print(student) shows:
# "Harry from Gryffindor"
# Instead of:
# "<__main__.Student object at 0x...>"
#
# __STR__ VS __REPR__:
# - __str__: Human-readable output (for users)
# - __repr__: Developer-readable output (for debugging)
# print() uses __str__, the REPL uses __repr__.
#
# COMMON DUNDER METHODS:
# - __init__: Constructor (initialize object)
# - __str__: String representation
# - __repr__: Developer representation
# - __eq__: Equality comparison (==)
# - __lt__: Less than comparison (<)
#
# See student15.py for adding more attributes!


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
