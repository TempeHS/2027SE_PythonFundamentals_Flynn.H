# Adds @property for house
#
# EXPLANATION:
# PROPERTIES let you control how attributes are accessed!
#
# KEY CONCEPTS:
# - @property creates a GETTER (reads value)
# - @house.setter creates a SETTER (writes value)
# - self._house stores the actual data (underscore = "private")
# - Validation runs every time the value is set!
#
# HOW PROPERTIES WORK:
# When you write: student.house = "Gryffindor"
# Python calls: house.setter(student, "Gryffindor")
# This runs validation EVERY time!
#
# When you read: print(student.house)
# Python calls: house.getter(student)
# This returns self._house
#
# THE UNDERSCORE (_house):
# - Convention for "internal" attributes
# - Signals "don't use directly"
# - The actual data is stored here
# - The property provides controlled access
#
# IN __INIT__:
# self.house = house  # Uses the setter!
# This means validation runs at creation too.
#
# NOW PROTECTED:
# student.house = "Invalid"  # Raises ValueError!
# Our validation can't be bypassed.
#
# See student19.py for adding a property for name too!


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
