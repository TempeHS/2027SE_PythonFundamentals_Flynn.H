# Adds @property for name
#
# EXPLANATION:
# Now BOTH name and house are protected by properties!
#
# KEY CONCEPTS:
# - Each property needs a getter and setter
# - All attributes that need validation should be properties
# - The underscore versions store actual data (_name, _house)
#
# PROPERTIES IN THIS CLASS:
# 1. name property:
#    - @property def name: returns self._name (getter)
#    - @name.setter def name: validates and sets self._name
#
# 2. house property:
#    - @property def house: returns self._house (getter)
#    - @house.setter def house: validates and sets self._house
#
# NOW IN __INIT__:
# self.name = name   # Uses name setter (validates!)
# self.house = house # Uses house setter (validates!)
#
# FULLY PROTECTED:
# - Can't create with empty name
# - Can't create with invalid house
# - Can't CHANGE to empty name
# - Can't CHANGE to invalid house
#
# See student20.py for @classmethod - alternative constructors!


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

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
