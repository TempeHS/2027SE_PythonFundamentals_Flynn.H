# Stores student as dict
#
# EXPLANATION:
# This uses a DICTIONARY for named access to data!
#
# KEY CONCEPTS:
# - Dictionaries use key-value pairs: {"name": value}
# - Access by name: student["name"] instead of student[0]
# - Much clearer and self-documenting!
#
# HOW IT WORKS:
# 1. Create empty dict: student = {}
# 2. Add key-value pairs: student["name"] = name
# 3. Return the dict with all data
#
# COMPARISON:
# Tuple/List: student[0], student[1] - confusing!
# Dict: student["name"], student["house"] - clear!
#
# BENEFITS OF DICTS:
# - Named access (self-documenting)
# - Order doesn't matter
# - Easy to add more fields later
# - Mutable (can change values)
#
# See student7.py for a more compact dict creation!


def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
