# Adds __init__
#
# EXPLANATION:
# __init__ is the CONSTRUCTOR - it initializes new objects!
#
# KEY CONCEPTS:
# - __init__ is called automatically when creating an object
# - 'self' refers to the object being created
# - self.name = name stores data in the object
# - Parameters define what data is needed to create the object
#
# HOW __INIT__ WORKS:
# Student("Harry", "Gryffindor") does two things:
# 1. Creates a new Student object
# 2. Calls __init__(self, "Harry", "Gryffindor")
#
# SELF:
# - 'self' is the object being created/used
# - It's passed automatically by Python
# - self.name stores name IN THE OBJECT
# - Just 'name' is the parameter (temporary)
#
# BENEFITS:
# - Object is ready to use immediately
# - All required data must be provided
# - Cleaner than adding attributes later
#
# See student11.py for an even cleaner version!


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
