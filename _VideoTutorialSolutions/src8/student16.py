# Adds charm method to cast a charm
#
# EXPLANATION:
# METHODS are functions that belong to a class!
#
# KEY CONCEPTS:
# - Methods are defined inside the class
# - First parameter is always 'self'
# - Call with object.method(): student.charm()
# - Methods can access the object's attributes via self
#
# NEW FEATURES:
# - patronus=None: Default parameter (optional patronus)
# - Validation for patronus if provided
# - charm() method returns emoji based on patronus
#
# THE CHARM METHOD:
# def charm(self):
#     match self.patronus:
#         case "Stag": return "🐴"
#         ...
#
# This method returns an emoji based on the patronus.
# It uses self.patronus to access the attribute.
#
# METHODS VS FUNCTIONS:
# Function: print("hello")    - standalone
# Method:   student.charm()   - attached to object
#
# ENCAPSULATION:
# - Data (attributes) + Behavior (methods) = Object
# - The class bundles related data and functions
# - This is a core OOP principle!
#
# See student17.py for a problem: what if someone
# bypasses our validation?


class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
