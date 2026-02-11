# Eliminates unneeded variable
#
# EXPLANATION:
# This returns the Student object directly - no temporary variable needed!
#
# KEY CONCEPTS:
# - return Student(name, house) creates and returns in one line
# - No need for intermediate 'student' variable
# - More concise and Pythonic
#
# COMPARISON:
# With variable (student10.py):
#   student = Student(name, house)
#   return student
#
# Direct return (this file):
#   return Student(name, house)
#
# Same result, fewer lines!
#
# WHEN TO USE EACH:
# - Direct return: Simple cases, no modification needed
# - Variable: When you need to modify or use the object first
#
# Our class is basic. What if someone creates:
# Student("", "InvalidHouse")
#
# See student12.py for adding VALIDATION!


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
    return Student(name, house)


if __name__ == "__main__":
    main()
