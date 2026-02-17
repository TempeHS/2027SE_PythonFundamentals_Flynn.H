# Prompts for patronus too, but doesn't display yet
#
# EXPLANATION:
# Classes can have multiple attributes - here we add a third!
#
# KEY CONCEPTS:
# - Add new parameter and attribute in __init__
# - Validate all data that needs validation
# - Store the new attribute: self.patronus = patronus
#
# PATRONUS:
# In Harry Potter, a Patronus is a protective charm.
# Here we add it as a third attribute of Student.
#
# CHANGES FROM PREVIOUS:
# 1. __init__ now takes name, house, patronus
# 2. self.patronus = patronus stores it
# 3. __str__ doesn't show it yet (just name and house)
#
# NOTE:
# No validation for patronus yet - that comes in the next
# version. Here we're just collecting the data.
#
# See student16.py for adding a METHOD to use the patronus!


class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
