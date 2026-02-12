# Defines class for a student
#
# EXPLANATION:
# This introduces CLASSES - custom data types in Python!
#
# KEY CONCEPTS:
# - 'class Student:' defines a new type called Student
# - '...' is a placeholder (empty class body)
# - student = Student() creates an instance (object)
# - student.name and student.house are ATTRIBUTES
#
# OBJECT-ORIENTED PROGRAMMING (OOP):
# - Class: A blueprint for creating objects
# - Object: An instance of a class
# - Attribute: Data stored in an object (like name, house)
# - Method: Function that belongs to a class (coming soon!)
#
# HOW IT WORKS:
# 1. Define the Student class (even if empty)
# 2. Create instance: student = Student()
# 3. Add attributes: student.name = "Harry"
# 4. Access attributes: student.name
#
# ATTRIBUTE ACCESS:
# - Dict: student["name"] (square brackets)
# - Object: student.name (dot notation - cleaner!)
#
# See student10.py for the __init__ method - automatic setup!


class Student: ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
