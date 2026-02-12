# Adds validation in __init__ using raise
#
# EXPLANATION:
# This adds VALIDATION - the class rejects invalid data!
#
# KEY CONCEPTS:
# - Validate data in __init__ before storing
# - 'raise ValueError(message)' creates an error
# - Invalid objects can't be created
# - This is called "defensive programming"
#
# VALIDATION LOGIC:
# 1. if not name: - Reject empty name
# 2. if house not in [...]: - Reject invalid house
# 3. Only store data if valid
#
# RAISE STATEMENT:
# 'raise' creates an exception (error).
# The program stops unless the error is caught with try/except.
# This prevents bad data from entering our system.
#
# WHY VALIDATE IN CLASS?
# The CLASS is responsible for its own integrity.
# No matter where Student is created, validation happens.
# "A Student object is always valid."
#
# See student13.py for what happens when you print an object!


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
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
